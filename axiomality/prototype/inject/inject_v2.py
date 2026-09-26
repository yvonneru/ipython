"""Error injection for the SYNTHETIC v2 benchmark (noisy recordings, 3 task variants).

Same seven error classes and the same magnitude ranges as v1 (inject/inject.py); the
injectors are reused where they are object-agnostic and adapted where v1 hard-coded
"obj0 = mug, obj1 = laptop" or exact event-frame lookup (v2 frames can be dropped).
Errors are injected into the *recorded* (already noisy) episodes. 20 episodes per
class (140 = 47%), 20 valid failures (physically consistent slips, re-simulated with
the same sensor model) and 140 clean noisy episodes.
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from data.generate_v2 import CLEAN_V2, DATA_V2, make_episode  # noqa: E402
from inject.inject import CLASS_DOCS, ERROR_CLASSES, inj_c, inj_d, inj_e, inj_f  # noqa: E402
from kernel.geometry import box_penetration  # noqa: E402
from kernel.rulebook import ARM, VOCAB  # noqa: E402
from util import ROOT, read_jsonl, write_json, write_jsonl  # noqa: E402

INJECT_SEED_V2 = 2126
PER_CLASS_V2 = 20
N_VALID_FAILURE_V2 = 20
HELDOUT_V2 = DATA_V2 / "heldout_injected_v2.jsonl"
KEY_V2 = DATA_V2 / "injection_key_v2.json"


def _frame_of(ep, ev_type):
    t = np.asarray(ep["frames"]["t"])
    et = next(e["t"] for e in ep["events"] if e["type"] == ev_type)
    return int(np.argmin(np.abs(t - et)))


def _id_of(ep, label):
    return next(o["id"] for o in ep["scene"]["objects"] if o["label"] == label)


def inj_a(ep, rng):
    oid = str(rng.choice([o["id"] for o in ep["scene"]["objects"]]))
    obj = next(o for o in ep["scene"]["objects"] if o["id"] == oid)
    new = str(rng.choice([c for c in VOCAB if c != obj["label"]]))
    old, obj["label"] = obj["label"], new
    return {"object": oid, "from": old, "to": new}


def inj_b(ep, rng):
    sub = str(rng.choice(["interpenetration", "laptop_floating", "laptop_sunk", "manipulated_floating_after_release"]))
    lid = _id_of(ep, "laptop")
    fr = ep["frames"]["object_poses"]
    lap, man = np.array(fr[lid]), np.array(fr["obj0"])
    dims = {o["id"]: o["dimensions"] for o in ep["scene"]["objects"]}
    d3 = {k: (v["length"], v["width"], v["height"]) for k, v in dims.items()}
    if sub == "interpenetration":
        depth = rng.uniform(0.005, 0.08)
        direction = man[0, :2] - lap[0, :2]
        dist = np.linalg.norm(direction)
        direction /= dist
        lo, hi = 0.0, dist
        for _ in range(50):
            mid = (lo + hi) / 2
            p = lap[:1].copy()
            p[0, :2] += direction * mid
            if box_penetration(p, d3[lid], man[:1], d3["obj0"])[0] < depth:
                lo = mid
            else:
                hi = mid
        lap[:, :2] += direction * hi
        params = {"subtype": sub, "penetration_m": round(depth, 4), "laptop_shift_m": round(hi, 4)}
    elif sub == "laptop_floating":
        dz = rng.uniform(0.01, 0.12)
        lap[:, 2] += dz
        params = {"subtype": sub, "raise_m": round(dz, 4)}
    elif sub == "laptop_sunk":
        dz = rng.uniform(0.01, 0.10)
        lap[:, 2] -= dz
        params = {"subtype": sub, "sink_m": round(dz, 4)}
    else:
        dz = rng.uniform(0.01, 0.12)
        k0 = _frame_of(ep, "contact_end") + 2
        ramp = np.clip((np.arange(len(man)) - k0 + 1) / 3.0, 0, 1)
        man[:, 2] += dz * ramp
        params = {"subtype": sub, "raise_m": round(dz, 4), "from_frame": k0}
    fr[lid], fr["obj0"] = np.round(lap, 6).tolist(), np.round(man, 6).tolist()
    return params


def inj_g(ep, rng):
    fr = ep["frames"]
    t = fr["t"]
    sub = str(rng.choice(["gripper_open_while_carrying", "contact_begin_early", "contact_end_late"]))
    if sub == "gripper_open_while_carrying":
        tr = [i for i, p in enumerate(fr["phase"]) if p == "transport"]
        L = int(rng.integers(5, 21))
        s = int(rng.integers(tr[0], tr[-1] - L))
        for i in range(s, s + L):
            fr["gripper_cmd"][i] = 0
            fr["gripper_width"][i] = ARM["gripper_aperture"]
        return {"subtype": sub, "frames": [s, s + L - 1]}
    ev_type = "contact_begin" if sub == "contact_begin_early" else "contact_end"
    k = _frame_of(ep, ev_type)
    shift = int(rng.integers(8, 31)) if sub == "contact_begin_early" else int(rng.integers(5, 16))
    k2 = max(k - shift, 0) if sub == "contact_begin_early" else min(k + shift, len(t) - 1)
    next(e for e in ep["events"] if e["type"] == ev_type)["t"] = t[k2]
    return {"subtype": sub, "original_frame": k, "logged_frame": k2}


INJECTORS_V2 = dict(zip(ERROR_CLASSES, (inj_a, inj_b, inj_c, inj_d, inj_e, inj_f, inj_g)))


def main() -> None:
    clean = read_jsonl(CLEAN_V2)
    rng = np.random.default_rng(INJECT_SEED_V2)
    order = rng.permutation(len(clean))
    plan = {}
    for ci, cls in enumerate(ERROR_CLASSES):
        for i in order[ci * PER_CLASS_V2:(ci + 1) * PER_CLASS_V2]:
            plan[int(i)] = cls
    base = len(ERROR_CLASSES) * PER_CLASS_V2
    for i in order[base:base + N_VALID_FAILURE_V2]:
        plan[int(i)] = "valid_failure"
    heldout, key = [], {}
    for i, ep in enumerate(clean):
        cls = plan.get(i, "clean")
        if cls == "clean":
            heldout.append(copy.deepcopy(ep))
            key[ep["episode_id"]] = {"class": cls, "variant": ep["meta"]["variant"]}
        elif cls == "valid_failure":
            vf = make_episode(i, slip=True)
            heldout.append(vf)
            key[vf["episode_id"]] = {"class": cls, "variant": vf["meta"]["variant"]}
        else:
            ep2 = copy.deepcopy(ep)
            params = INJECTORS_V2[cls](ep2, rng)
            heldout.append(ep2)
            key[ep2["episode_id"]] = {"class": cls, "variant": ep["meta"]["variant"], **params}
    write_jsonl(HELDOUT_V2, heldout)
    counts = {c: sum(1 for v in key.values() if v["class"] == c) for c in list(CLASS_DOCS) + ["clean"]}
    write_json(KEY_V2, {"description": "Ground-truth key for the SYNTHETIC v2 injected held-out copy (noisy "
                                       "recordings). Never read by the engine or the baselines.",
                        "seed": INJECT_SEED_V2, "class_docs": CLASS_DOCS, "counts": counts, "episodes": key})
    print(f"[inject v2] {base} corrupted ({PER_CLASS_V2}/class x {len(ERROR_CLASSES)}), {counts['valid_failure']} "
          f"valid failures, {counts['clean']} clean -> {HELDOUT_V2.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
