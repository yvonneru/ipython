"""REAL-data run: engine real-data mode + structural baseline on the converted OXE subsets.

Outputs results/real_data.{json,md}, results/passport_real_<name>.json (signed, one per
dataset, over the accepted split = PASS + REPAIR episodes) and the accepted splits in
results/accepted/real_<name>.jsonl.
"""
from __future__ import annotations

import json
import shutil
import tempfile
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd

from baseline.rules_only import check_real_episode
from data.real_fetch import REAL_DIR
from engine.real_mode import (CATALOGUE, FAMILIES, FAMILY_RULE, REAL_MODE_VERSION, accepted_split, catalogue_hash,
                              load_dataset, verify_real_dataset)
from kernel.rulebook import RULEBOOK_VERSION, rulebook_hash
from passport.passport import issue_generic, verify
from util import RESULTS_DIR, write_json, write_jsonl

DATASETS = ("droid_100", "jaco_play", "nyu_rot")
SEVERITY = ["action_state", "joint_limits", "frames", "gripper", "motion", "kinematics", "boundaries", "duplicates",
            "outcome", "numeric", "timing", "task"]


def timing_selftest() -> dict:
    """The real sets have no timestamps, so exercise the timing checks on a copy of one real
    episode with SYNTHETIC timestamps (clearly a unit test, not a finding)."""
    tmp = Path(tempfile.mkdtemp())
    try:
        src = REAL_DIR / "nyu_rot"
        shutil.copytree(src / "meta", tmp / "meta")
        (tmp / "data" / "chunk-000").mkdir(parents=True)
        info = json.loads((tmp / "meta" / "info.json").read_text())
        info["fps"] = 10.0
        (tmp / "meta" / "info.json").write_text(json.dumps(info))
        eps = [json.loads(x) for x in (tmp / "meta" / "episodes.jsonl").read_text().splitlines()][:3]
        (tmp / "meta" / "episodes.jsonl").write_text("\n".join(json.dumps(e) for e in eps) + "\n")
        cases = {0: "clean clock", 1: "two missing frames (gap of 3 periods)", 2: "two rows swapped"}
        for e in eps:
            df = pd.read_parquet(src / "data" / "chunk-000" / f"episode_{e['episode_index']:06d}.parquet")
            t = np.arange(len(df)) / 10.0
            if e["episode_index"] == 1:
                t[10:] += 0.2
            if e["episode_index"] == 2:
                t[[5, 6]] = t[[6, 5]]
            df["timestamp"] = t
            df.to_parquet(tmp / "data" / "chunk-000" / f"episode_{e['episode_index']:06d}.parquet")
        r = verify_real_dataset(tmp)
        return {"note": "SYNTHETIC timestamps added to 3 real nyu_rot episodes to unit-test the timing family",
                "cases": [{"case": cases[x["episode_index"]], "timing_verdict": x["families"]["timing"]["verdict"],
                           "finding": (x["families"]["timing"]["findings"] or [{}])[0].get("what")}
                          for x in r["episode_results"]]}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def collect_findings(name: str, res: dict, ds: dict) -> list[dict]:
    out = []
    for a in res["column_aliases"]:
        out.append({"dataset": name, "episode": "all", "frame": None, "family": "schema", "evidence": "hard",
                    "what": f"column '{a['column']}{a['slice']}' is bit-identical to '{a['equals']}' in all "
                            f"{res['frames']} frames",
                    "why": f"documented as \"{a['declared_as']}\" but it holds \"{a['other_declared_as']}\""})
    empty = [e["episode_index"] for e in res["episode_results"]
             if any("empty task" in f["what"] for f in e["families"]["task"]["findings"])]
    if empty:
        succ = [i for i in empty if "/success/" in (ds["episodes"][i].get("source_file_path") or "")]
        out.append({"dataset": name, "episode": f"{len(empty)}/{res['episodes']} episodes", "frame": 0, "family": "task",
                    "evidence": "hard", "what": f"no language instruction in any instruction field (episodes {empty}; "
                                                f"{len(succ)} of them recorded as success)",
                    "why": "unusable for language-conditioned training; task undocumented"})
    for e in res["episode_results"]:
        src = ds["episodes"][e["episode_index"]].get("source_file_path") or ""
        tag = "/".join(src.split("/")[6:9]) if src.startswith("/nfs") else src
        for fam in SEVERITY:
            for f in e["families"][fam]["findings"] + e["families"][fam]["advisories"]:
                if fam == "task" and "empty task" in f["what"]:
                    continue
                out.append({"dataset": name, "episode": e["episode_index"], "source": tag, "frame": f["frame"],
                            "family": fam, "evidence": f["evidence"], "what": f["what"], "why": f["why"],
                            "verdict_effect": "REJECT" if f["evidence"] == "hard" and "repair" not in f else
                            ("REPAIR" if "repair" in f else "advisory")})
    order = {"schema": -1, **{f: i for i, f in enumerate(SEVERITY)}}
    out.sort(key=lambda x: (x["evidence"] != "hard", order.get(x["family"], 99)))
    return out


def main() -> dict:
    report = {"real_mode": REAL_MODE_VERSION, "catalogue_hash": catalogue_hash(), "thresholds": CATALOGUE["thresholds"],
              "datasets": {}, "timing_selftest": timing_selftest()}
    for name in DATASETS:
        path = REAL_DIR / name
        ds = load_dataset(path)
        res = verify_real_dataset(path)
        info = ds["info"]
        # structural baseline on the same real data
        base = [check_real_episode(df, info) for df in ds["frames"]]
        eng_acc = [e["verdict"] in ("PASS", "REPAIR") for e in res["episode_results"]]
        base_acc = [b["verdict"] == "PASS" for b in base]
        agree = sum(a == b for a, b in zip(eng_acc, base_acc))
        dis = [{"episode": i, "engine": res["episode_results"][i]["verdict"], "baseline": base[i]["verdict"],
                "engine_reasons": sorted({f"{fam}: {x['what'][:90]}" for fam, v in res["episode_results"][i]["families"].items()
                                          for x in v["findings"]}),
                "baseline_issues": base[i]["issues"]}
               for i in range(len(base)) if eng_acc[i] != base_acc[i]]
        # shared checks only: joint limits / speed / finite / tcp spike
        shared = []
        for i, b in enumerate(base):
            fams = res["episode_results"][i]["families"]
            e_hit = any(fams[f]["verdict"] == "REJECT" for f in ("numeric", "joint_limits", "motion"))
            b_hit = any(not s.startswith("episode too short") for s in b["issues"])
            shared.append(e_hit == b_hit)
        # accepted split + passport
        acc = accepted_split(path, res)
        acc_file = RESULTS_DIR / "accepted" / f"real_{name}.jsonl"
        write_jsonl(acc_file, acc)
        fam_verdicts = {f: res["family_table"][f] for f in FAMILIES}
        unknown_all = {f: res["family_table"][f].get("note", "") for f in FAMILIES if res["family_table"][f]["UNKNOWN"] == 100.0}
        by_rule = Counter()
        for e in res["episode_results"]:
            by_rule.update({f for f, v in e["families"].items() if v["verdict"] in ("REJECT", "REPAIR")})
        pp_path = RESULTS_DIR / f"passport_real_{name}.json"
        issue_generic(pp_path, acc, acc_file, {
            "dataset_id": f"OXE/{info['source']['dataset']}@{info['source']['version']} (subset)",
            "title": f"REAL robot data: {name} ({info['robot_type']}), {len(ds['episodes'])} episodes from "
                     f"{len(info['source']['shards'])} RLDS shard(s)",
            "rulebook": {"version": RULEBOOK_VERSION, "hash": rulebook_hash(),
                         "used_for": "arm limits (Panda datasheet values), kinematic model, v_max"},
            "real_mode": {"version": REAL_MODE_VERSION, "catalogue_hash": catalogue_hash()},
            "verdict_counts": {"submitted": res["episodes"], **res["verdicts"]},
            "family_verdict_shares_pct": fam_verdicts,
            "checks_not_run": unknown_all,
            "findings_summary": {"episodes_with_reject_or_repair_by_family": dict(by_rule),
                                 "column_aliases": res["column_aliases"]},
            "real_synthetic": {"real": len(acc), "synthetic": 0, "real_ratio": 1.0 if acc else None},
            "provenance": {"source": info["source"], "robot_type": info["robot_type"], "fps": info["fps"],
                           "fps_source": info["fps_source"], "profile": info["axiomality_profile"]},
            "checks": {"engine": REAL_MODE_VERSION, "families": FAMILIES, "z3_in_loop": False},
            "known_limitations": [
                "Real data, but only a small subset (shards selected by size to stay under 300 MB).",
                "Semantic checks (object type/size, support, contact, permanence, spatial relations, phase grammar, "
                "task success) were NOT run: " + unknown_all.get("semantic", ""),
                "No per-frame timestamps in the source, so timing checks (monotonicity, gaps, jitter) were not run.",
                "Heuristic findings (robust-range outliers, assumed command semantics) are advisory only and do not "
                "affect verdicts; they are listed in results/real_data.json.",
                "Joint-limit and speed checks use external datasheet limits where stated (not the dataset's own "
                "metadata); if the arm model differs, those findings may be wrong.",
                "No Z3 query is made in real-data mode; all checks are numeric.",
                "Accepted means none of the runnable checks found a defect; it does not mean the data is correct. "
                "Not a safety certification. Demo signing key."],
        })
        ok, msgs = verify(pp_path)
        report["datasets"][name] = {
            "robot_type": info["robot_type"], "fps": info["fps"], "fps_source": info["fps_source"],
            "download_mb": round(info["source"]["download_bytes"] / 1e6, 1), "shards": len(info["source"]["shards"]),
            "episodes": res["episodes"], "frames": res["frames"], "verdicts": res["verdicts"],
            "family_table": res["family_table"], "column_aliases": res["column_aliases"],
            "dataset_stats": res["dataset_stats"],
            "max_fk_error_um": (round(max(e["families"]["kinematics"].get("max_fk_error_m", 0) for e in res["episode_results"]) * 1e6, 2)
                                if res["family_table"]["kinematics"]["UNKNOWN"] < 100 else None),
            "findings": collect_findings(name, res, ds),
            "baseline": {"verdicts": dict(Counter(b["verdict"] for b in base)), "checks_run": base[0]["checks_run"],
                         "agreement_accept_reject": f"{agree}/{len(base)}", "disagreements": dis,
                         "agreement_on_shared_checks": f"{sum(shared)}/{len(shared)}"},
            "accepted_episodes": len(acc),
            "passport": {"file": pp_path.name, "verify_ok": ok, "messages": msgs},
            "episode_results": res["episode_results"],
        }
        print(f"[real] {name}: {res['episodes']} episodes, {res['frames']} frames, verdicts {res['verdicts']}; "
              f"baseline {dict(Counter(b['verdict'] for b in base))}; passport {'VALID' if ok else 'INVALID'}")
    write_json(RESULTS_DIR / "real_data.json", report)
    (RESULTS_DIR / "real_data.md").write_text(to_markdown(report))
    return report


def to_markdown(rep: dict) -> str:
    L = ["# Real-data mode results (REAL robot data, Open X-Embodiment RLDS subsets)", "",
         "Hugging Face (LeRobot) was unreachable from this environment (HTTP 403 from the egress proxy for huggingface.co); "
         "the data comes from the public OXE bucket on storage.googleapis.com and was converted to a LeRobot-v2-style "
         "layout without synthesising anything (no timestamps were invented).", "",
         "| Dataset | Robot | Episodes | Frames | Download | PASS | REPAIR | REJECT | UNKNOWN | Baseline PASS/REJECT |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for n, d in rep["datasets"].items():
        v, b = d["verdicts"], d["baseline"]["verdicts"]
        L.append(f"| {n} | {d['robot_type']} | {d['episodes']} | {d['frames']} | {d['download_mb']} MB | {v['PASS']} | "
                 f"{v['REPAIR']} | {v['REJECT']} | {v['UNKNOWN']} | {b.get('PASS', 0)}/{b.get('REJECT', 0)} |")
    L += ["", "## Verdict shares per check family (% of episodes: PASS / REPAIR / REJECT / UNKNOWN; advisory episodes)", "",
          "| Family | kernel rule | " + " | ".join(rep["datasets"]) + " |", "|---|---|" + "---|" * len(rep["datasets"])]
    for f in FAMILIES:
        cells = []
        for d in rep["datasets"].values():
            t = d["family_table"][f]
            cells.append("UNKNOWN" if t["UNKNOWN"] == 100 else
                         f"{t['PASS']:.0f}/{t['REPAIR']:.0f}/{t['REJECT']:.0f}/{t['UNKNOWN']:.0f}" +
                         (f" (+{t['advisory_episodes']} adv.)" if t["advisory_episodes"] else ""))
        L.append(f"| {f} | {FAMILY_RULE.get(f, '-')} | " + " | ".join(cells) + " |")
    L += ["", "UNKNOWN reasons: " + "; ".join(sorted({f"{f}: {d['family_table'][f]['note']}" for d in rep["datasets"].values()
                                                       for f in FAMILIES if d["family_table"][f].get("note")
                                                       and d["family_table"][f]["UNKNOWN"] == 100})), ""]
    for n, d in rep["datasets"].items():
        L += [f"## {n}: findings (real)", ""]
        if d.get("max_fk_error_um") is not None:
            L.append(f"- R-KIN-01 ran on every frame: recorded Cartesian position vs Panda FK (flange) of the recorded "
                     f"joints, max error {d['max_fk_error_um']} micrometres over {d['frames']} frames (PASS; float32 precision).")
        for f in d["findings"]:
            L.append(f"- [{f['evidence']}] episode {f['episode']}{' (' + f['source'] + ')' if f.get('source') else ''}, "
                     f"frame {f['frame']}, {f['family']}: {f['what']}. Why: {f['why']}")
        if not d["findings"]:
            L.append("- none (all runnable checks passed)")
        bl = d["baseline"]
        L += ["", f"Structural baseline ({', '.join(bl['checks_run'])}): accept/reject agreement with the engine "
                  f"{bl['agreement_accept_reject']}; agreement on the shared checks {bl['agreement_on_shared_checks']}."]
        for x in bl["disagreements"]:
            L.append(f"- episode {x['episode']}: engine {x['engine']} ({'; '.join(x['engine_reasons'])[:200]}), "
                     f"baseline {x['baseline']} ({'; '.join(x['baseline_issues']) or 'no issue'})")
        L += ["", f"Passport `{d['passport']['file']}`: {d['accepted_episodes']} accepted episodes, verification "
                  f"{'VALID' if d['passport']['verify_ok'] else 'INVALID'}.", ""]
    L += ["## Timing-family self-test (SYNTHETIC timestamps on real episodes)", ""]
    for c in rep["timing_selftest"]["cases"]:
        L.append(f"- {c['case']}: {c['timing_verdict']} {('- ' + c['finding']) if c['finding'] else ''}")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
