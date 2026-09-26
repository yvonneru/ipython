"""Error injection into a held-out copy of the SYNTHETIC dataset.

Seven error classes (one per corrupted episode, 10 episodes each = 35%) plus one
*valid failure* class (10 episodes re-simulated with a physically consistent
slip) that a good verifier must KEEP. The key file documents every change.
Injection magnitudes were fixed before the benchmark was run and include
near-threshold cases (some are expected to be undetectable).
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from data.generate import simulate_episode  # noqa: E402
from kernel.arm import Q_HI, Q_LO  # noqa: E402
from kernel.geometry import box_penetration  # noqa: E402
from kernel.rulebook import ARM, VOCAB  # noqa: E402
from util import CLEAN_FILE, HELDOUT_FILE, KEY_FILE, ROOT, read_jsonl, write_json, write_jsonl  # noqa: E402

INJECT_SEED = 2026
PER_CLASS = 10
N_VALID_FAILURE = 10

CLASS_DOCS = {
    "a_wrong_label": "Object label replaced by another class from the company vocabulary (mug or laptop, whole episode).",
    "b_impossible_relation": "Physically impossible relation: laptop box shifted into the mug (penetration 5-80 mm), "
                             "laptop floating (+10-120 mm), laptop sunk into table (10-100 mm), or mug hovering "
                             "10-120 mm above the table after release (3-frame ramp).",
    "c_phase_order": "Task-phase labels: swap two adjacent phase blocks, reverse all blocks, or relabel one block.",
    "d_teleport": "Mug position jumps 0.03-0.60 m horizontally at one frame (glitch lasting 1-3 frames, or persistent).",
    "e_timestamp_warp": "Three consecutive rows written out of order (rows carry their own timestamps) -> non-monotonic time.",
    "f_joint_limit": "One joint pushed 0.02-0.40 rad beyond its declared limit by a smooth 5-21 frame bump.",
    "g_gripper_contact_mismatch": "Gripper reported open while carrying (5-20 frames), contact_begin logged 8-30 frames "
                                  "early, or contact_end logged 5-15 frames late.",
    "valid_failure": "NOT an error: episode re-simulated with the mug slipping out of the gripper during transport and "
                     "falling ballistically (outcome=failure_slip). Must be KEPT.",
}
ERROR_CLASSES = [c for c in CLASS_DOCS if c != "valid_failure"]


def _segments(phase):
    starts = [0] + [i for i in range(1, len(phase)) if phase[i] != phase[i - 1]]
    ends = starts[1:] + [len(phase)]
    return [(phase[s], s, e) for s, e in zip(starts, ends)]


def _frame_of(ep, ev_type):
    t = ep["frames"]["t"]
    et = next(e["t"] for e in ep["events"] if e["type"] == ev_type)
    return t.index(et)


def inj_a(ep, rng):
    oid = str(rng.choice(["obj0", "obj1"]))
    obj = next(o for o in ep["scene"]["objects"] if o["id"] == oid)
    new = str(rng.choice([c for c in VOCAB if c != obj["label"]]))
    old, obj["label"] = obj["label"], new
    return {"object": oid, "from": old, "to": new}


def inj_b(ep, rng):
    sub = str(rng.choice(["interpenetration", "laptop_floating", "laptop_sunk", "mug_floating_after_release"]))
    fr = ep["frames"]["object_poses"]
    lap, mug = np.array(fr["obj1"]), np.array(fr["obj0"])
    dims = {o["id"]: o["dimensions"] for o in ep["scene"]["objects"]}
    d3 = {k: (v["length"], v["width"], v["height"]) for k, v in dims.items()}
    if sub == "interpenetration":
        depth = rng.uniform(0.005, 0.08)
        direction = mug[0, :2] - lap[0, :2]
        dist = np.linalg.norm(direction)
        direction /= dist
        lo, hi = 0.0, dist
        for _ in range(50):  # bisection on shift so penetration == depth at frame 0
            mid = (lo + hi) / 2
            p = lap[:1].copy()
            p[0, :2] += direction * mid
            if box_penetration(p, d3["obj1"], mug[:1], d3["obj0"])[0] < depth:
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
        ramp = np.clip((np.arange(len(mug)) - k0 + 1) / 3.0, 0, 1)
        mug[:, 2] += dz * ramp
        params = {"subtype": sub, "raise_m": round(dz, 4), "from_frame": k0}
    fr["obj1"], fr["obj0"] = np.round(lap, 6).tolist(), np.round(mug, 6).tolist()
    return params


def inj_c(ep, rng):
    ph = ep["frames"]["phase"]
    segs = _segments(ph)
    labels = [s[0] for s in segs]
    sub = str(rng.choice(["swap_adjacent", "reverse", "relabel_block"]))
    if sub == "swap_adjacent":
        i = int(rng.integers(0, len(labels) - 1))
        labels[i], labels[i + 1] = labels[i + 1], labels[i]
        params = {"subtype": sub, "blocks": [i, i + 1]}
    elif sub == "reverse":
        labels = labels[::-1]
        params = {"subtype": sub}
    else:
        i = int(rng.integers(0, len(labels)))
        new = str(rng.choice([p for p in ("approach", "grasp", "transport", "place", "release") if p != labels[i]]))
        params = {"subtype": sub, "block": i, "from": labels[i], "to": new}
        labels[i] = new
    ep["frames"]["phase"] = [lab for lab, (_, s, e) in zip(labels, segs) for _ in range(s, e)]
    params["new_sequence"] = labels
    return params


def inj_d(ep, rng):
    mug = np.array(ep["frames"]["object_poses"]["obj0"])
    n = len(mug)
    k = int(rng.integers(10, n - 10))
    mag = rng.uniform(0.03, 0.60)
    ang = rng.uniform(0, 2 * np.pi)
    off = mag * np.array([np.cos(ang), np.sin(ang)])
    mode = str(rng.choice(["glitch", "persistent"]))
    end = k + int(rng.integers(1, 4)) if mode == "glitch" else n
    mug[k:end, :2] += off
    ep["frames"]["object_poses"]["obj0"] = np.round(mug, 6).tolist()
    return {"frame": k, "magnitude_m": round(mag, 4), "mode": mode, "frames": [k, end - 1]}


def inj_e(ep, rng):
    fr = ep["frames"]
    n = len(fr["t"])
    k = int(rng.integers(5, n - 8))
    perms = [(0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
    perm = perms[int(rng.integers(len(perms)))]
    order = list(range(n))
    order[k:k + 3] = [k + p for p in perm]
    for key in ("t", "tcp_pose", "gripper_cmd", "gripper_width", "joints", "phase"):
        fr[key] = [fr[key][i] for i in order]
    fr["object_poses"] = {o: [v[i] for i in order] for o, v in fr["object_poses"].items()}
    return {"frames": [k, k + 2], "row_order": [k + p for p in perm]}


def inj_f(ep, rng):
    q = np.array(ep["frames"]["joints"])
    n = len(q)
    j = int(rng.integers(0, 7))
    k = int(rng.integers(12, n - 12))
    w = int(rng.integers(2, 11))
    delta = rng.uniform(0.02, 0.40)
    upper = (q[k, j] - Q_LO[j]) > (Q_HI[j] - q[k, j])
    amp = (Q_HI[j] + delta - q[k, j]) if upper else (Q_LO[j] - delta - q[k, j])
    idx = np.arange(k - w, k + w + 1)
    q[idx, j] += amp * np.sin(np.pi * (idx - (k - w)) / (2 * w)) ** 2
    ep["frames"]["joints"] = np.round(q, 6).tolist()
    return {"joint": j + 1, "peak_frame": k, "beyond_limit_rad": round(delta, 4), "frames": [k - w, k + w],
            "limit": "upper" if upper else "lower"}


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


INJECTORS = dict(zip(ERROR_CLASSES, (inj_a, inj_b, inj_c, inj_d, inj_e, inj_f, inj_g)))


def main() -> None:
    clean = read_jsonl(CLEAN_FILE)
    rng = np.random.default_rng(INJECT_SEED)
    order = rng.permutation(len(clean))
    plan = {}
    for ci, cls in enumerate(ERROR_CLASSES):
        for i in order[ci * PER_CLASS:(ci + 1) * PER_CLASS]:
            plan[int(i)] = cls
    for i in order[len(ERROR_CLASSES) * PER_CLASS:len(ERROR_CLASSES) * PER_CLASS + N_VALID_FAILURE]:
        plan[int(i)] = "valid_failure"
    heldout, key = [], {}
    for i, ep in enumerate(clean):
        cls = plan.get(i, "clean")
        if cls == "clean":
            heldout.append(copy.deepcopy(ep))
        elif cls == "valid_failure":
            heldout.append(simulate_episode(i, slip=True))
        else:
            ep2 = copy.deepcopy(ep)
            params = INJECTORS[cls](ep2, rng)
            heldout.append(ep2)
            key[ep2["episode_id"]] = {"class": cls, **params}
            continue
        key[ep["episode_id"]] = {"class": cls}
    write_jsonl(HELDOUT_FILE, heldout)
    counts = {c: sum(1 for v in key.values() if v["class"] == c) for c in list(CLASS_DOCS) + ["clean"]}
    write_json(KEY_FILE, {"description": "Ground-truth key for the injected held-out copy. Never read by the engine "
                                         "or the baseline. All episodes are SYNTHETIC.",
                          "seed": INJECT_SEED, "class_docs": CLASS_DOCS, "counts": counts, "episodes": key})
    print(f"[inject] {sum(counts[c] for c in ERROR_CLASSES)} corrupted ({PER_CLASS}/class x {len(ERROR_CLASSES)}), "
          f"{counts['valid_failure']} valid failures, {counts['clean']} clean -> {HELDOUT_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
