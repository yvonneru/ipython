"""Benchmark: engine vs rules-only baseline on the injected held-out copy.

Outputs results/benchmark.json, results/benchmark.md, results/engine_verdicts.json,
results/baseline_verdicts.json and the accepted split (PASS + REPAIR episodes, the
latter in repaired form) used for the Data Passport.
"""
from __future__ import annotations

import copy
import json
import time

import numpy as np

from baseline.rules_only import check_episode
from data.generate import simulate_episode
from engine.verifier import ENGINE_VERSION, verify_episode
from inject.inject import CLASS_DOCS, ERROR_CLASSES
from util import (ACCEPTED_FILE, CLEAN_FILE, HELDOUT_FILE, KEY_FILE, RESULTS_DIR, canonical_json, read_jsonl,
                  sha256_hex, write_json, write_jsonl)

EXPECTED_FAMILY = {"a_wrong_label": ("R-QTY", "R-TYPE"), "b_impossible_relation": ("R-SPAT", "R-SUP", "R-PERM"),
                   "c_phase_order": ("R-PHASE",), "d_teleport": ("R-PERM",), "e_timestamp_warp": ("R-TIME",),
                   "f_joint_limit": ("R-JNT",), "g_gripper_contact_mismatch": ("R-GRIP", "R-CONT")}
EXPECTED_ACTION = {c: ("REPAIR" if c == "e_timestamp_warp" else "REJECT") for c in ERROR_CLASSES}


def _h(ep):
    e = copy.deepcopy(ep)
    e["meta"].pop("ax_repairs", None)
    return sha256_hex(canonical_json(e))


def behaviour_checks() -> list[dict]:
    """Small targeted scenarios for UNKNOWN / unit repair / failure relabel / unrecoverable time."""
    base, slip = simulate_episode(0), simulate_episode(0, slip=True)
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
    cases.append(("slip episode relabelled as success", e, "REJECT"))
    e = copy.deepcopy(base)
    e["frames"]["t"][50] = e["frames"]["t"][49]
    cases.append(("duplicate timestamp (not re-sortable)", e, "REJECT"))
    out = []
    for name, ep, expect in cases:
        r, b = verify_episode(ep), check_episode(ep)
        out.append({"case": name, "expected": expect, "engine": r["verdict"], "engine_reason": r["reason"],
                    "baseline": b["verdict"], "ok": r["verdict"] == expect})
    return out


def main() -> dict:
    heldout = read_jsonl(HELDOUT_FILE)
    clean_by_id = {e["episode_id"]: e for e in read_jsonl(CLEAN_FILE)}
    key = json.loads(KEY_FILE.read_text())["episodes"]

    eng, base = [], []
    t0 = time.perf_counter()
    for ep in heldout:
        eng.append(verify_episode(ep))
    t_eng = time.perf_counter() - t0
    t0 = time.perf_counter()
    for ep in heldout:
        base.append(check_episode(ep))
    t_base = time.perf_counter() - t0

    accepted, repair_exact = [], []
    for ep, r in zip(heldout, eng):
        if r["verdict"] == "PASS":
            accepted.append(ep)
        elif r["verdict"] == "REPAIR":
            rep = r.pop("repaired_episode")
            accepted.append(rep)
            repair_exact.append(_h(rep) == _h(clean_by_id[ep["episode_id"]]))
    write_jsonl(ACCEPTED_FILE, accepted)
    write_json(RESULTS_DIR / "engine_verdicts.json", eng)
    write_json(RESULTS_DIR / "baseline_verdicts.json", base)

    def cls(i):
        return key[heldout[i]["episode_id"]]["class"]

    per_class = {}
    for c in ERROR_CLASSES + ["valid_failure", "clean"]:
        idx = [i for i in range(len(heldout)) if cls(i) == c]
        ev, bv = [eng[i]["verdict"] for i in idx], [base[i]["verdict"] for i in idx]
        row = {"n": len(idx), "engine_verdicts": {v: ev.count(v) for v in sorted(set(ev))},
               "baseline_verdicts": {v: bv.count(v) for v in sorted(set(bv))}}
        if c in ERROR_CLASSES:
            row["engine_recall"] = sum(v != "PASS" for v in ev) / len(idx)
            row["baseline_recall"] = sum(v != "PASS" for v in bv) / len(idx)
            row["engine_correct_action"] = sum(v == EXPECTED_ACTION[c] for v in ev) / len(idx)
            row["engine_rule_attribution"] = sum(any(f["rule"].startswith(EXPECTED_FAMILY[c]) for f in eng[i]["findings"]
                                                     + eng[i]["repairs"]) for i in idx) / len(idx)
            row["engine_missed"] = [{"episode": heldout[i]["episode_id"], **key[heldout[i]["episode_id"]]}
                                    for i in idx if eng[i]["verdict"] == "PASS"]
        else:
            row["engine_kept"] = sum(v in ("PASS", "REPAIR") for v in ev) / len(idx)
            row["baseline_kept"] = sum(v == "PASS" for v in bv) / len(idx)
        per_class[c] = row

    def overall(verdicts, keep):
        pos = [cls(i) in ERROR_CLASSES for i in range(len(heldout))]
        flag = [v != "PASS" for v in verdicts]
        tp = sum(p and f for p, f in zip(pos, flag))
        fp = sum((not p) and f for p, f in zip(pos, flag))
        clean_idx = [i for i in range(len(heldout)) if cls(i) == "clean"]
        vf_idx = [i for i in range(len(heldout)) if cls(i) == "valid_failure"]
        return {"precision": tp / (tp + fp) if tp + fp else None, "recall": tp / sum(pos), "tp": tp, "fp": fp,
                "fn": sum(pos) - tp,
                "false_reject_rate_clean": sum(verdicts[i] not in keep for i in clean_idx) / len(clean_idx),
                "valid_failures_kept": f"{sum(verdicts[i] in keep for i in vf_idx)}/{len(vf_idx)}",
                "classes_with_full_recall": None}

    ov_e, ov_b = overall([r["verdict"] for r in eng], ("PASS", "REPAIR")), overall([r["verdict"] for r in base], ("PASS",))
    ov_e["ms_per_episode"] = t_eng / len(heldout) * 1e3
    ov_b["ms_per_episode"] = t_base / len(heldout) * 1e3
    pristine = [verify_episode(e)["verdict"] for e in clean_by_id.values()]
    ov_e["false_reject_rate_pristine_200"] = sum(v != "PASS" for v in pristine) / len(pristine)
    ov_e["repairs_byte_identical_to_original"] = f"{sum(repair_exact)}/{len(repair_exact)}"
    caught_only_engine = [c for c in ERROR_CLASSES if per_class[c]["engine_recall"] > 0 and per_class[c]["baseline_recall"] == 0]
    ov_e["classes_with_full_recall"] = sum(per_class[c]["engine_recall"] == 1 for c in ERROR_CLASSES)
    ov_b["classes_with_full_recall"] = sum(per_class[c]["baseline_recall"] == 1 for c in ERROR_CLASSES)

    res = {"dataset": "AX-DEMO-109 injected held-out copy (SYNTHETIC)", "episodes": len(heldout),
           "engine_version": ENGINE_VERSION, "class_docs": CLASS_DOCS, "per_class": per_class,
           "overall": {"engine": ov_e, "baseline": ov_b},
           "classes_caught_by_engine_but_missed_entirely_by_baseline": caught_only_engine,
           "behaviour_checks": behaviour_checks(), "accepted_episodes": len(accepted)}
    write_json(RESULTS_DIR / "benchmark.json", res)
    (RESULTS_DIR / "benchmark.md").write_text(to_markdown(res))
    print(f"[benchmark] engine {ov_e['ms_per_episode']:.1f} ms/ep, baseline {ov_b['ms_per_episode']:.2f} ms/ep; "
          f"engine recall {ov_e['recall']:.2f} precision {ov_e['precision']:.2f}; baseline recall {ov_b['recall']:.2f}")
    return res


def to_markdown(res: dict) -> str:
    pc, e, b = res["per_class"], res["overall"]["engine"], res["overall"]["baseline"]
    L = ["# Benchmark: AXIOMALITY engine vs rules-only baseline", "",
         f"Dataset: {res['dataset']}, {res['episodes']} episodes (10 per error class, 10 valid failures, "
         f"{pc['clean']['n']} clean). All data SYNTHETIC; errors injected by `inject/inject.py`.", "",
         "| Error class | n | Engine recall | Baseline recall | Engine correct action | Engine rule attribution |",
         "|---|---|---|---|---|---|"]
    for c in ERROR_CLASSES:
        r = pc[c]
        L.append(f"| {c} | {r['n']} | {r['engine_recall']:.0%} | {r['baseline_recall']:.0%} | "
                 f"{r['engine_correct_action']:.0%} | {r['engine_rule_attribution']:.0%} |")
    L += ["", "| Overall | Engine | Baseline |", "|---|---|---|",
          f"| Precision (flagged episodes that were corrupted) | {e['precision']:.2f} | {b['precision']:.2f} |",
          f"| Recall (corrupted episodes flagged) | {e['recall']:.2f} ({e['tp']}/{e['tp'] + e['fn']}) | "
          f"{b['recall']:.2f} ({b['tp']}/{b['tp'] + b['fn']}) |",
          f"| False-reject rate, clean episodes in held-out set | {e['false_reject_rate_clean']:.1%} | "
          f"{b['false_reject_rate_clean']:.1%} |",
          f"| Valid failures (physically consistent slips) kept | {e['valid_failures_kept']} | {b['valid_failures_kept']} |",
          f"| Error classes with 100% recall | {e['classes_with_full_recall']}/7 | {b['classes_with_full_recall']}/7 |",
          f"| Runtime per episode | {e['ms_per_episode']:.1f} ms | {b['ms_per_episode']:.2f} ms |", "",
          f"Engine false-reject rate on the 200 pristine episodes: {e['false_reject_rate_pristine_200']:.1%}. "
          f"Timestamp repairs byte-identical to the original episode: {e['repairs_byte_identical_to_original']}.", "",
          "Recall = verdict other than PASS. Correct action = REPAIR for timestamp warps, REJECT otherwise. "
          "Rule attribution = at least one finding cites a rule from the expected family.", "",
          "## Engine misses", ""]
    for c in ERROR_CLASSES:
        for m in pc[c]["engine_missed"]:
            L.append(f"- `{m['episode']}` {c}: " + ", ".join(f"{k}={v}" for k, v in m.items() if k not in ("episode", "class")))
    L += ["", "## Behaviour checks", "", "| Case | Expected | Engine | Baseline |", "|---|---|---|---|"]
    for bc in res["behaviour_checks"]:
        L.append(f"| {bc['case']} | {bc['expected']} | {bc['engine']} | {bc['baseline']} |")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
