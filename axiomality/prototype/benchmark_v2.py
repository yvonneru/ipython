"""SYNTHETIC benchmark v2: engine vs STRONG baseline vs structural baseline on NOISY data.

Protocol
  1. Calibration (fair, identical for all three checkers): each checker's noise-sensitive
     tolerances start at their v1 values and are widened x1.25 (rule by rule) until no
     episode of the calibration split is rejected. The calibration split is 120 clean +
     30 slip episodes generated with disjoint seeds; the benchmark episodes are never used.
  2. Benchmark: data/generated_v2/heldout_injected_v2.jsonl (300 SYNTHETIC noisy episodes:
     7 error classes x 20, 20 valid failures, 140 clean) with every checker at its
     calibrated tolerances. The engine is also run with its uncalibrated v1 tolerances to
     show what noise alone does.
  3. Outputs: results/benchmark_v2.{json,md}, verdict files, accepted split + passport
     (results/passport_AX-DEMO-109-v2.json), and results/rule_encoding_counts.json.
"""
from __future__ import annotations

import copy
import json
import time
from collections import Counter

import numpy as np

from baseline import strong_rules
from baseline.rules_only import check_episode as structural_check
from data.generate_v2 import CAL_V2, CLEAN_V2, SENSOR_MODEL, VARIANTS, make_episode
from engine.verifier import ENGINE_VERSION, verify_episode
from inject.inject import CLASS_DOCS, ERROR_CLASSES
from inject.inject_v2 import HELDOUT_V2, KEY_V2, PER_CLASS_V2
from kernel.profiles import (RULE_KNOBS, RULEBOOK_V2_VERSION, V2_START, phys_profile, rule_encoding_counts,
                             rulebook_v2_hash, widen)
from kernel.rulebook import PHYS
from passport.passport import issue_generic
from data.generate import simulate_episode
from util import HELDOUT_FILE, KEY_FILE, RESULTS_DIR, canonical_json, read_jsonl, sha256_hex, write_json, write_jsonl

EXPECTED_FAMILY = {"a_wrong_label": ("R-QTY", "R-TYPE"), "b_impossible_relation": ("R-SPAT", "R-SUP", "R-PERM"),
                   "c_phase_order": ("R-PHASE",), "d_teleport": ("R-PERM",), "e_timestamp_warp": ("R-TIME",),
                   "f_joint_limit": ("R-JNT",), "g_gripper_contact_mismatch": ("R-GRIP", "R-CONT")}
ACCEPTED_V2 = RESULTS_DIR / "accepted" / "accepted_episodes_v2.jsonl"
PASSPORT_V2 = RESULTS_DIR / "passport_AX-DEMO-109-v2.json"
CHECKERS = ("engine", "strong", "structural")
MAX_ITERS = 25


# ------------------------------------------------------------------ calibration
def calibrate_engine(cal: list[dict]) -> tuple[dict, list]:
    prof = {**{k: copy.deepcopy(v) for k, v in PHYS.items()}, **V2_START}
    log, tries = [], Counter()
    for it in range(MAX_ITERS):
        with phys_profile(prof):
            rs = [verify_episode(e) for e in cal]
        bad = Counter(rid for r in rs if r["verdict"] not in ("PASS", "REPAIR") for rid in {f["rule"] for f in r["findings"]})
        log.append({"iter": it, "false_rejects": sum(r["verdict"] not in ("PASS", "REPAIR") for r in rs),
                    "rules": dict(bad)})
        if not bad:
            break
        for rid in bad:
            knobs = RULE_KNOBS.get(rid)
            if knobs:
                widen(prof, knobs[tries[rid] % len(knobs)])
                tries[rid] += 1
    return prof, log


def calibrate_strong(cal: list[dict]) -> tuple[dict, list]:
    tol, log = dict(strong_rules.DEFAULT_TOL), []
    for it in range(MAX_ITERS):
        rs = [strong_rules.check_episode(e, tol) for e in cal]
        bad = Counter(c for r in rs if r["verdict"] != "PASS" for c in r["codes"])
        log.append({"iter": it, "false_rejects": sum(r["verdict"] != "PASS" for r in rs), "codes": dict(bad)})
        if not bad:
            break
        for c in bad:
            k = strong_rules.KNOB_OF.get(c)
            if k == "target_slack":
                tol[k] = round(tol[k] + 0.005, 4)
            elif k:
                tol[k] = round(tol[k] * 1.25, 6)
            elif c == "S-SUPPORT":
                tol["grace_s"] = round(tol["grace_s"] + 0.25, 3)
    return tol, log


def calibrate_structural(cal: list[dict]) -> tuple[dict, list]:
    pol, log = {"max_single_drops": 2, "qd_margin": 1.0}, []
    for it in range(MAX_ITERS):
        rs = [structural_check(e, pol) for e in cal]
        bad = Counter(i.split(" at ")[0] for r in rs for i in r["issues"])
        log.append({"iter": it, "false_rejects": sum(r["verdict"] != "PASS" for r in rs), "issues": dict(bad)})
        if not bad:
            break
        if any("joint speed" in k for k in bad):
            pol["qd_margin"] = round(pol["qd_margin"] * 1.25, 6)
        else:
            break
    return pol, log


# ------------------------------------------------------------------ run
def run_checkers(eps, eng_prof, strong_tol, struct_pol):
    out = {c: [] for c in CHECKERS}
    ms = {}
    t0 = time.perf_counter()
    with phys_profile(eng_prof):
        out["engine"] = [verify_episode(e) for e in eps]
    ms["engine"] = (time.perf_counter() - t0) / len(eps) * 1e3
    t0 = time.perf_counter()
    out["strong"] = [strong_rules.check_episode(e, strong_tol) for e in eps]
    ms["strong"] = (time.perf_counter() - t0) / len(eps) * 1e3
    t0 = time.perf_counter()
    out["structural"] = [structural_check(e, struct_pol) for e in eps]
    ms["structural"] = (time.perf_counter() - t0) / len(eps) * 1e3
    return out, ms


def metrics(verdicts: list[str], classes: list[str], keep: tuple) -> dict:
    pos = [c in ERROR_CLASSES for c in classes]
    flag = [v not in ("PASS",) for v in verdicts]
    tp = sum(p and f for p, f in zip(pos, flag))
    fp = sum((not p) and f for p, f in zip(pos, flag))
    clean = [v for v, c in zip(verdicts, classes) if c == "clean"]
    vf = [v for v, c in zip(verdicts, classes) if c == "valid_failure"]
    return {"precision": tp / (tp + fp) if tp + fp else None, "recall": tp / sum(pos), "tp": tp, "fp": fp,
            "fn": sum(pos) - tp, "false_reject_rate_clean": sum(v not in keep for v in clean) / len(clean),
            "false_rejects_clean": f"{sum(v not in keep for v in clean)}/{len(clean)}",
            "valid_failures_kept": f"{sum(v in keep for v in vf)}/{len(vf)}",
            "valid_failure_retention": sum(v in keep for v in vf) / len(vf)}


def behaviour_checks_v2(eng_prof, strong_tol) -> list[dict]:
    base, slip = make_episode(1), make_episode(1, slip=True)
    cases = []
    e = copy.deepcopy(base)
    del e["frames"]["object_poses"]
    cases.append(("object poses missing", e, "UNKNOWN"))
    e = copy.deepcopy(base)
    e["frames"]["joints"] = np.round(np.rad2deg(e["frames"]["joints"]), 6).tolist()
    cases.append(("joint angles logged in degrees", e, "REPAIR"))
    e = copy.deepcopy(slip)
    e["meta"]["outcome"] = "success"
    e["frames"]["phase"] = [p if p != "abort" else "release" for p in e["frames"]["phase"]]
    cases.append(("slip relabelled as success (phases relabelled too)", e, "REJECT"))
    e = copy.deepcopy(base)
    e["frames"]["t"][50] = e["frames"]["t"][49]
    cases.append(("duplicate timestamp (not re-sortable)", e, "REJECT"))
    e = copy.deepcopy(base)
    ph = e["frames"]["phase"]
    tr = [i for i, p in enumerate(ph) if p == "transport"]
    k = next(ev for ev in e["events"] if ev["type"] == "contact_end")
    k["t"] = e["frames"]["t"][tr[len(tr) // 2]]
    cases.append(("contact ends mid-transport, gripper still closed (cross-rule)", e, "REJECT"))
    out = []
    for name, ep, expect in cases:
        with phys_profile(eng_prof):
            r = verify_episode(ep)
        s = strong_rules.check_episode(ep, strong_tol)
        out.append({"case": name, "expected": expect, "engine": r["verdict"], "engine_reason": r["reason"],
                    "strong": s["verdict"], "strong_issues": s["issues"][:2], "ok": r["verdict"] == expect})
    return out


def strong_on_v1() -> dict:
    """The strong baseline on the ORIGINAL v1 (noise-free) benchmark, next to the saved v1 engine
    verdicts. Its tolerances are calibrated on 60 fresh v1-generator episodes (indices 1000+,
    disjoint from the benchmark; 45 clean + 15 slips)."""
    cal = [simulate_episode(1000 + i) for i in range(45)] + [simulate_episode(1100 + i, slip=True) for i in range(15)]
    tol, log = calibrate_strong(cal)
    held = read_jsonl(HELDOUT_FILE)
    key = json.loads(KEY_FILE.read_text())["episodes"]
    eng = {v["episode_id"]: v["verdict"] for v in json.loads((RESULTS_DIR / "engine_verdicts.json").read_text())}
    base = {v["episode_id"]: v["verdict"] for v in json.loads((RESULTS_DIR / "baseline_verdicts.json").read_text())}
    st = {e["episode_id"]: strong_rules.check_episode(e, tol)["verdict"] for e in held}
    out = {"strong_tolerances": tol, "calibration_log": log, "per_class": {}}
    for c in ERROR_CLASSES + ["valid_failure", "clean"]:
        ids = [i for i, k in key.items() if k["class"] == c]
        f = (lambda d: sum(d[i] != "PASS" for i in ids) / len(ids)) if c in ERROR_CLASSES else \
            (lambda d: sum(d[i] in ("PASS", "REPAIR") for i in ids) / len(ids))
        out["per_class"][c] = {"n": len(ids), "engine": f(eng), "strong": f(st), "structural": f(base)}
    pos = [i for i, k in key.items() if k["class"] in ERROR_CLASSES]
    out["recall"] = {n: sum(d[i] != "PASS" for i in pos) / len(pos) for n, d in (("engine", eng), ("strong", st),
                                                                                 ("structural", base))}
    return out


SWEEP = {"laptop_sunk_mm": [5, 10, 15, 20, 25, 30, 40], "laptop_floating_mm": [5, 10, 15, 20, 25, 30, 40],
         "persistent_teleport_mm": [10, 20, 30, 40, 60, 80], "floating_after_release_mm": [5, 10, 20, 30, 40],
         "interpenetration_mm": [5, 10, 15, 20, 30]}


def _apply(ep, kind, mag):
    from inject.inject_v2 import _frame_of, _id_of
    e = copy.deepcopy(ep)
    fr = e["frames"]["object_poses"]
    m = mag / 1000.0
    if kind in ("laptop_sunk_mm", "laptop_floating_mm"):
        lid = _id_of(e, "laptop")
        a = np.array(fr[lid])
        a[:, 2] += -m if kind == "laptop_sunk_mm" else m
        fr[lid] = a.tolist()
    elif kind == "persistent_teleport_mm":
        a = np.array(fr["obj0"])
        k = _frame_of(e, "contact_end") + 3
        a[k:, 0] += m
        fr["obj0"] = a.tolist()
    elif kind == "floating_after_release_mm":
        a = np.array(fr["obj0"])
        k0 = _frame_of(e, "contact_end") + 2
        a[:, 2] += m * np.clip((np.arange(len(a)) - k0 + 1) / 3.0, 0, 1)
        fr["obj0"] = a.tolist()
    else:
        from kernel.geometry import box_penetration
        lid = _id_of(e, "laptop")
        lap, man = np.array(fr[lid]), np.array(fr["obj0"])
        dims = {o["id"]: o["dimensions"] for o in e["scene"]["objects"]}
        d3 = {k: (v["length"], v["width"], v["height"]) for k, v in dims.items()}
        direc = man[0, :2] - lap[0, :2]
        dist = np.linalg.norm(direc)
        direc /= dist
        lo, hi = 0.0, dist
        for _ in range(50):
            mid = (lo + hi) / 2
            q = lap[:1].copy()
            q[0, :2] += direc * mid
            if box_penetration(q, d3[lid], man[:1], d3["obj0"])[0] < m:
                lo = mid
            else:
                hi = mid
        lap[:, :2] += direc * hi
        fr[lid] = lap.tolist()
    return e


def sensitivity_sweep(eng_prof, strong_tol, struct_pol, n_base: int = 12) -> dict:
    """Same error types as class (b)/(d), controlled magnitudes, identical base episodes for all
    checkers (the first n_base clean benchmark episodes that are successes)."""
    held = read_jsonl(HELDOUT_V2)
    key = json.loads(KEY_V2.read_text())["episodes"]
    base = [e for e in held if key[e["episode_id"]]["class"] == "clean"][:n_base]
    out = {}
    for kind, mags in SWEEP.items():
        rows = []
        for mag in mags:
            eps = [_apply(e, kind, mag) for e in base]
            with phys_profile(eng_prof):
                ev = [verify_episode(e)["verdict"] != "PASS" for e in eps]
            sv = [strong_rules.check_episode(e, strong_tol)["verdict"] != "PASS" for e in eps]
            bv = [structural_check(e, struct_pol)["verdict"] != "PASS" for e in eps]
            rows.append({"mm": mag, "engine": float(np.mean(ev)), "strong": float(np.mean(sv)),
                         "structural": float(np.mean(bv))})
        out[kind] = rows
    return {"n_base_episodes": len(base), "curves": out}


def main() -> dict:
    cal = read_jsonl(CAL_V2)
    heldout = read_jsonl(HELDOUT_V2)
    key = json.loads(KEY_V2.read_text())["episodes"]
    classes = [key[e["episode_id"]]["class"] for e in heldout]
    t0 = time.perf_counter()
    eng_prof, eng_log = calibrate_engine(cal)
    strong_tol, strong_log = calibrate_strong(cal)
    struct_pol, struct_log = calibrate_structural(cal)
    t_cal = time.perf_counter() - t0
    res_by, ms = run_checkers(heldout, eng_prof, strong_tol, struct_pol)
    with phys_profile(V2_START):  # uncalibrated: v1 tolerances + v2 switches
        v1tol = [verify_episode(e)["verdict"] for e in heldout]
    v1pure = [verify_episode(e)["verdict"] for e in heldout]  # v1 engine exactly as shipped

    verd = {c: [r["verdict"] for r in res_by[c]] for c in CHECKERS}
    keep = {"engine": ("PASS", "REPAIR"), "strong": ("PASS",), "structural": ("PASS",)}
    per_class = {}
    for c in ERROR_CLASSES + ["valid_failure", "clean"]:
        idx = [i for i, k in enumerate(classes) if k == c]
        row = {"n": len(idx)}
        for ch in CHECKERS:
            vs = [verd[ch][i] for i in idx]
            row[f"{ch}_verdicts"] = dict(Counter(vs))
            if c in ERROR_CLASSES:
                row[f"{ch}_recall"] = sum(v != "PASS" for v in vs) / len(idx)
            else:
                row[f"{ch}_kept"] = sum(v in keep[ch] for v in vs) / len(idx)
        if c in ERROR_CLASSES:
            ev = [verd["engine"][i] for i in idx]
            row["engine_correct_action"] = sum(v == ("REPAIR" if c == "e_timestamp_warp" else "REJECT") for v in ev) / len(idx)
            row["engine_rule_attribution"] = sum(any(f["rule"].startswith(EXPECTED_FAMILY[c]) for f in
                                                     res_by["engine"][i]["findings"] + res_by["engine"][i]["repairs"])
                                                 for i in idx) / len(idx)
            row["engine_missed"] = [{"episode": heldout[i]["episode_id"], **key[heldout[i]["episode_id"]]}
                                    for i in idx if verd["engine"][i] == "PASS"]
            row["strong_missed"] = [{"episode": heldout[i]["episode_id"], **key[heldout[i]["episode_id"]]}
                                    for i in idx if verd["strong"][i] == "PASS"]
            row["engine_only"] = [{"episode": heldout[i]["episode_id"], **key[heldout[i]["episode_id"]],
                                   "engine_rules": sorted({f["rule"] for f in res_by["engine"][i]["findings"]})}
                                  for i in idx if verd["engine"][i] != "PASS" and verd["strong"][i] == "PASS"]
            row["strong_only"] = [{"episode": heldout[i]["episode_id"], **key[heldout[i]["episode_id"]],
                                   "strong_issues": res_by["strong"][i]["issues"][:3]}
                                  for i in idx if verd["strong"][i] != "PASS" and verd["engine"][i] == "PASS"]
        per_class[c] = row
    overall = {ch: {**metrics(verd[ch], classes, keep[ch]), "ms_per_episode": ms[ch]} for ch in CHECKERS}
    overall["engine_uncalibrated_v1_tolerances"] = metrics(v1tol, classes, keep["engine"])
    overall["engine_v1_as_shipped"] = metrics(v1pure, classes, keep["engine"])
    for ch in CHECKERS:
        overall[ch]["classes_with_full_recall"] = sum(per_class[c][f"{ch}_recall"] == 1 for c in ERROR_CLASSES)
        overall[ch]["macro_recall"] = float(np.mean([per_class[c][f"{ch}_recall"] for c in ERROR_CLASSES]))

    # engine-only catches by rule (why the strong baseline missed them)
    why = Counter()
    for c in ERROR_CLASSES:
        for m in per_class[c]["engine_only"]:
            why.update(m["engine_rules"])
    # accepted split + known-undetected (evaluation-only information)
    accepted, repair_exact = [], []
    clean_by_id = {e["episode_id"]: e for e in read_jsonl(CLEAN_V2)}
    for ep, r in zip(heldout, res_by["engine"]):
        if r["verdict"] == "PASS":
            accepted.append(ep)
        elif r["verdict"] == "REPAIR":
            rep = r.pop("repaired_episode")
            accepted.append(rep)
            a, b = copy.deepcopy(rep), clean_by_id[ep["episode_id"]]
            a["meta"].pop("ax_repairs", None)
            repair_exact.append(sha256_hex(canonical_json(a)) == sha256_hex(canonical_json(b)))
    for r in res_by["engine"]:
        r.pop("repaired_episode", None)
    write_jsonl(ACCEPTED_V2, accepted)
    undetected = [{"episode": ep["episode_id"], **key[ep["episode_id"]]} for ep, r in zip(heldout, res_by["engine"])
                  if r["verdict"] == "PASS" and key[ep["episode_id"]]["class"] in ERROR_CLASSES]
    repaired_injected = sum(1 for ep, r in zip(heldout, res_by["engine"])
                            if r["verdict"] == "REPAIR" and key[ep["episode_id"]]["class"] in ERROR_CLASSES)
    enc = rule_encoding_counts()
    write_json(RESULTS_DIR / "rule_encoding_counts.json", enc)

    # passport for the v2 accepted split (the passport cannot know about undetected errors)
    counts = Counter(verd["engine"])
    by_rule, by_family = Counter(), Counter()
    for r in res_by["engine"]:
        rules = {f["rule"] for f in r["findings"]} | {x["rule"] for x in r["repairs"]}
        by_rule.update(rules)
        by_family.update({x.rsplit("-", 1)[0] for x in rules})
    overrides = {k: v for k, v in eng_prof.items() if PHYS.get(k) != v}
    pp = issue_generic(PASSPORT_V2, accepted, ACCEPTED_V2, {
        "dataset_id": "AX-DEMO-109-v2",
        "title": "SYNTHETIC noisy pick-and-place episodes (3 task variants, 3 object classes) derived from sample 109",
        "rulebook": {"version": RULEBOOK_V2_VERSION, "hash": rulebook_v2_hash(overrides), "overrides": overrides},
        "verdict_counts": {"submitted": len(heldout), **{k: counts.get(k, 0) for k in ("PASS", "REPAIR", "REJECT", "UNKNOWN")}},
        "findings_summary": {"episodes_by_rule_family": dict(sorted(by_family.items())),
                             "episodes_by_rule": dict(sorted(by_rule.items()))},
        "real_synthetic": {"real": 0, "synthetic": len(accepted), "real_ratio": 0.0},
        "provenance": {"generator": sorted({e["meta"]["generator"] for e in accepted}),
                       "variants": dict(Counter(e["meta"]["variant"] for e in accepted)),
                       "sensor_model": SENSOR_MODEL,
                       "robot_ids": sorted({e["meta"]["robot_id"] for e in accepted})},
        "checks": {"engine": ENGINE_VERSION, "tolerance_profile": "calibrated on a disjoint clean calibration split"},
        "known_limitations": [
            "All episodes are SYNTHETIC; no real robot data in this split.",
            "Accepted means no rule in the rulebook was violated at the calibrated tolerances. Errors below those "
            "tolerances (e.g. small sinks/teleports hidden by sensor noise) or outside the rulebook (e.g. a wrong "
            "label whose box fits the wrong class) can remain in the accepted split. The passport cannot count them.",
            "Per episode, only 9 of 30 rules are decided by a Z3 query; the rest are numeric checks against the "
            "same constants (see rule_encoding_counts).",
            "Tolerances were widened on a calibration split until it had zero false rejects; they are recorded in "
            "rulebook.overrides.",
            "Not a safety certification. Kinematic physics only (no force/torque, friction, tipping).",
            "Demo signing key; issuer identity not established."],
    })

    res = {"dataset": "AX-DEMO-109 v2 injected held-out copy (SYNTHETIC, noisy)", "episodes": len(heldout),
           "per_class_n": PER_CLASS_V2, "variants": VARIANTS, "sensor_model": SENSOR_MODEL,
           "engine_version": ENGINE_VERSION, "class_docs": CLASS_DOCS,
           "calibration": {"split": f"{len(cal)} episodes ({sum('slip' in e['meta']['outcome'] for e in cal)} slips), "
                                    "disjoint seeds", "seconds": round(t_cal, 1),
                           "engine_overrides": overrides, "engine_log": eng_log,
                           "strong_tolerances": strong_tol, "strong_log": strong_log,
                           "structural_policy": struct_pol, "structural_log": struct_log},
           "per_class": per_class, "overall": overall,
           "engine_only_catches_by_rule": dict(why.most_common()),
           "behaviour_checks": behaviour_checks_v2(eng_prof, strong_tol),
           "v1_noise_free_with_strong_baseline": strong_on_v1(),
           "sensitivity_sweep": sensitivity_sweep(eng_prof, strong_tol, struct_pol),
           "accepted_episodes": len(accepted),
           "repairs_byte_identical_to_original": f"{sum(repair_exact)}/{len(repair_exact)}",
           "evaluation_only_known_undetected_in_accepted_split": {
               "count": len(undetected), "episodes": undetected,
               "repaired_injected_episodes_in_accepted_split": repaired_injected,
               "repaired_note": "timestamp-warp episodes accepted in repaired form; see repairs_byte_identical_to_original",
               "note": "Known only from the injection key. The passport cannot know this number and does not contain it."},
           "rule_encoding": {k: v for k, v in enc.items() if k != "scope"},
           "passport": {"file": str(PASSPORT_V2.name), "content_hash": pp["content"]["content_hash"]}}
    write_json(RESULTS_DIR / "benchmark_v2.json", res)
    for ch in CHECKERS:
        write_json(RESULTS_DIR / f"v2_{ch}_verdicts.json", res_by[ch])
    (RESULTS_DIR / "benchmark_v2.md").write_text(to_markdown(res))
    E, S, B = overall["engine"], overall["strong"], overall["structural"]
    print(f"[benchmark v2] recall engine {E['recall']:.2f} / strong {S['recall']:.2f} / structural {B['recall']:.2f}; "
          f"precision {E['precision']:.2f} / {S['precision']:.2f} / {B['precision']:.2f}; FRR clean "
          f"{E['false_rejects_clean']} / {S['false_rejects_clean']} / {B['false_rejects_clean']}; "
          f"undetected-in-accepted {len(undetected)}")
    return res


LAB = {"a_wrong_label": "(a) wrong object label", "b_impossible_relation": "(b) impossible relation",
       "c_phase_order": "(c) illegal phase order", "d_teleport": "(d) object teleport",
       "e_timestamp_warp": "(e) timestamp warp", "f_joint_limit": "(f) joint-limit violation",
       "g_gripper_contact_mismatch": "(g) gripper/contact mismatch"}


def to_markdown(res: dict) -> str:
    pc, ov = res["per_class"], res["overall"]
    E, S, B = ov["engine"], ov["strong"], ov["structural"]
    L = ["# Benchmark v2: engine vs strong baseline vs structural baseline (SYNTHETIC, noisy)", "",
         f"{res['episodes']} SYNTHETIC episodes, 3 task variants ({', '.join(res['variants'])}), 3 object classes "
         f"(mug, laptop, fruit). Sensor model: joint noise sigma 0.2-0.5 deg, object position noise 3 mm/axis, "
         f"+-5 ms timestamp jitter, one dropped frame in ~30% of episodes. {res['per_class_n']} episodes per error "
         f"class, {pc['valid_failure']['n']} valid failures, {pc['clean']['n']} clean. All tolerances calibrated on "
         f"a disjoint calibration split ({res['calibration']['split']}).", "",
         "| Error class | n | Engine | Strong baseline | Structural baseline | Engine correct action | Engine rule attribution |",
         "|---|---|---|---|---|---|---|"]
    for c in ERROR_CLASSES:
        r = pc[c]
        L.append(f"| {LAB[c]} | {r['n']} | {r['engine_recall']:.0%} | {r['strong_recall']:.0%} | "
                 f"{r['structural_recall']:.0%} | {r['engine_correct_action']:.0%} | {r['engine_rule_attribution']:.0%} |")
    L += ["", "| Overall | Engine | Strong | Structural |", "|---|---|---|---|",
          f"| Recall | {E['recall']:.2f} ({E['tp']}/{E['tp'] + E['fn']}) | {S['recall']:.2f} ({S['tp']}/{S['tp'] + S['fn']}) | "
          f"{B['recall']:.2f} ({B['tp']}/{B['tp'] + B['fn']}) |",
          f"| Precision | {E['precision']:.2f} | {S['precision']:.2f} | {B['precision']:.2f} |",
          f"| False rejects, clean noisy episodes | {E['false_rejects_clean']} ({E['false_reject_rate_clean']:.1%}) | "
          f"{S['false_rejects_clean']} ({S['false_reject_rate_clean']:.1%}) | {B['false_rejects_clean']} "
          f"({B['false_reject_rate_clean']:.1%}) |",
          f"| Valid failures kept | {E['valid_failures_kept']} | {S['valid_failures_kept']} | {B['valid_failures_kept']} |",
          f"| Classes at 100% recall | {E['classes_with_full_recall']}/7 | {S['classes_with_full_recall']}/7 | "
          f"{B['classes_with_full_recall']}/7 |",
          f"| ms / episode | {E['ms_per_episode']:.1f} | {S['ms_per_episode']:.1f} | {B['ms_per_episode']:.2f} |", "",
          f"Engine with uncalibrated v1 tolerances on the same noisy data: false rejects on clean "
          f"{ov['engine_uncalibrated_v1_tolerances']['false_rejects_clean']}, valid failures kept "
          f"{ov['engine_uncalibrated_v1_tolerances']['valid_failures_kept']} (v1 as shipped: "
          f"{ov['engine_v1_as_shipped']['false_rejects_clean']} / {ov['engine_v1_as_shipped']['valid_failures_kept']}).", "",
          f"Timestamp repairs byte-identical to the original noisy recording: {res['repairs_byte_identical_to_original']}.", "",
          "## Calibrated tolerances", "",
          f"Engine overrides: `{json.dumps(res['calibration']['engine_overrides'])}`", "",
          f"Strong baseline: `{json.dumps(res['calibration']['strong_tolerances'])}`", "",
          f"Structural baseline: `{json.dumps(res['calibration']['structural_policy'])}`", "",
          "## Where the two rule-based checkers differ", "",
          f"Engine-only catches by engine rule: `{json.dumps(res['engine_only_catches_by_rule'])}`", ""]
    for c in ERROR_CLASSES:
        for m in pc[c]["engine_only"]:
            L.append(f"- engine only, `{m['episode']}` {c} ({m.get('subtype', m.get('to', ''))}): {', '.join(m['engine_rules'])}")
        for m in pc[c]["strong_only"]:
            L.append(f"- strong only, `{m['episode']}` {c} ({m.get('subtype', m.get('to', ''))}): {m['strong_issues'][0]}")
    v1 = res["v1_noise_free_with_strong_baseline"]
    L += ["", "## The original v1 (noise-free) benchmark with the strong baseline added", "",
          "| Error class (n = 10) | Engine (v1) | Strong baseline | Structural baseline (v1) |", "|---|---|---|---|"]
    for c in ERROR_CLASSES:
        r = v1["per_class"][c]
        L.append(f"| {LAB[c]} | {r['engine']:.0%} | {r['strong']:.0%} | {r['structural']:.0%} |")
    L.append(f"| **Overall recall** | {v1['recall']['engine']:.2f} | {v1['recall']['strong']:.2f} | "
             f"{v1['recall']['structural']:.2f} |")
    L.append(f"| Clean kept / valid failures kept | {v1['per_class']['clean']['engine']:.0%} / "
             f"{v1['per_class']['valid_failure']['engine']:.0%} | {v1['per_class']['clean']['strong']:.0%} / "
             f"{v1['per_class']['valid_failure']['strong']:.0%} | {v1['per_class']['clean']['structural']:.0%} / "
             f"{v1['per_class']['valid_failure']['structural']:.0%} |")
    sw = res["sensitivity_sweep"]
    L += ["", f"## Sensitivity sweep (controlled magnitudes, {sw['n_base_episodes']} identical clean base episodes per point)", "",
          "Detection rate per injected magnitude. Same error types as classes (b) and (d); same base episodes for all checkers.", "",
          "| Error type | magnitude (mm) | Engine | Strong | Structural |", "|---|---|---|---|---|"]
    for kind, rows in sw["curves"].items():
        for r in rows:
            L.append(f"| {kind.replace('_mm', '').replace('_', ' ')} | {r['mm']} | {r['engine']:.0%} | {r['strong']:.0%} | "
                     f"{r['structural']:.0%} |")
    L += ["", "## Engine misses", ""]
    for c in ERROR_CLASSES:
        for m in pc[c]["engine_missed"]:
            L.append(f"- `{m['episode']}` {c}: " + ", ".join(f"{k}={v}" for k, v in m.items() if k not in ("episode", "class")))
    u = res["evaluation_only_known_undetected_in_accepted_split"]
    L += ["", "## Accepted split and passport", "",
          f"Accepted split: {res['accepted_episodes']} episodes; passport `{res['passport']['file']}`. "
          f"**Evaluation-only:** {u['count']} accepted episodes are known from the injection key to contain an injected "
          "error that the engine did not detect. The passport cannot know this and does not contain the number.", "",
          "## Behaviour checks", "", "| Case | Expected | Engine | Strong baseline |", "|---|---|---|---|"]
    for bc in res["behaviour_checks"]:
        L.append(f"| {bc['case']} | {bc['expected']} | {bc['engine']} | {bc['strong']} |")
    e = res["rule_encoding"]
    L += ["", "## Rule encoding (exact)", "",
          f"{e['total_rules']} rules: {e['z3_decides_per_episode']} are decided per episode by a Z3 query, "
          f"{e['z3_selfcheck_only']} more are Z3-encoded only in the rulebook self-check (evaluated per episode with "
          f"numpy), {e['numeric_only']} are numeric-only ({', '.join(e['numeric_only_rules'])}). The rulebook's own "
          f"kind labels say {e['rulebook_kind_label_counts']['z3']} z3 / {e['rulebook_kind_label_counts']['numeric']} "
          f"numeric; they disagree with the self-check for {', '.join(e['rulebook_kind_label_disagrees_with_selfcheck']) or 'none'}."]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
