#!/usr/bin/env python3
"""v2 end to end (v1 outputs are left untouched; run run_all.py for those):

  1. rule-encoding accounting (exact Z3 vs numeric counts) + Z3 self-check of the v2 tolerance profile
  2. REAL data: fetch OXE subsets (< 300 MB) -> LeRobot-v2-style layout -> real-data mode,
     structural baseline, signed passports (verified)
  3. SYNTHETIC v2: noisy data (3 variants, 3 classes) -> injection (20/class) -> calibration ->
     engine vs strong baseline vs structural baseline -> passport v2 (verified)
  4. v2 figures

    python run_v2.py              # everything (~2 min after the one-time ~280 MB download)
    python run_v2.py --skip-real  # synthetic v2 only (e.g. when storage.googleapis.com is unreachable)
"""
import argparse
import json
import time

from util import RESULTS_DIR, ROOT, write_json


def step(name, fn):
    t0 = time.perf_counter()
    print(f"\n== {name}")
    out = fn()
    print(f"   ({time.perf_counter() - t0:.1f}s)")
    return out


def selfcheck_v2():
    from kernel.profiles import rule_encoding_counts
    enc = rule_encoding_counts()
    write_json(RESULTS_DIR / "rule_encoding_counts.json", enc)
    print(f"[kernel] {enc['total_rules']} rules: {enc['z3_decides_per_episode']} decided per episode by Z3, "
          f"{enc['z3_selfcheck_only']} Z3-encoded in the self-check only, {enc['numeric_only']} numeric-only; "
          f"kind-label mismatch: {enc['rulebook_kind_label_disagrees_with_selfcheck']}")
    return enc


def selfcheck_calibrated_profile():
    """Re-run the Z3 rulebook self-check under the calibrated v2 tolerances (consistency of the widened rulebook)."""
    from kernel.axioms import self_check
    from kernel.profiles import phys_profile
    bench = json.loads((RESULTS_DIR / "benchmark_v2.json").read_text())
    ov = bench["calibration"]["engine_overrides"]
    with phys_profile(ov):
        rep = self_check(json.loads((ROOT / "data" / "seed_sample_109.json").read_text()))
    write_json(RESULTS_DIR / "rulebook_selfcheck_v2_profile.json", rep)
    print(f"[kernel] self-check under calibrated v2 tolerances: {rep['result']} | seed scene: "
          f"{rep['seed_scene_109']['result']} | implied-by-others: {rep['independence']['implied_by_others']}")
    return rep


def verify_all(names):
    from passport.passport import verify
    ok_all = True
    for n in names:
        ok, msgs = verify(RESULTS_DIR / n)
        ok_all &= ok
        print(f"  {n}: {'VALID' if ok else 'INVALID'}")
        for m in msgs:
            print("     " + m)
    if not ok_all:
        raise SystemExit("passport verification failed")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-real", action="store_true")
    a = ap.parse_args()
    t0 = time.perf_counter()
    RESULTS_DIR.mkdir(exist_ok=True)
    step("1. Rule-encoding accounting", selfcheck_v2)
    passports = []
    if not a.skip_real:
        from data import real_fetch
        import real_benchmark
        step("2a. REAL data: fetch + convert (OXE subsets)", real_fetch.main)
        rep = step("2b. REAL data: real-data mode + structural baseline + passports", real_benchmark.main)
        passports += [d["passport"]["file"] for d in rep["datasets"].values()]
    from data import generate_v2
    from inject import inject_v2
    import benchmark_v2
    step("3a. SYNTHETIC v2 data (noisy, 3 variants)", generate_v2.main)
    step("3b. Error injection v2", inject_v2.main)
    step("3c. Calibration + benchmark v2 (engine / strong / structural)", benchmark_v2.main)
    step("3d. Z3 self-check under the calibrated tolerances", selfcheck_calibrated_profile)
    passports.append(benchmark_v2.PASSPORT_V2.name)
    step("4. Verify all v2 passports offline", lambda: verify_all(passports))
    from figures import make_figures_v2
    step("5. Figures v2", make_figures_v2.main)
    print(f"\nDone in {time.perf_counter() - t0:.1f}s. See results/benchmark_v2.md, results/real_data.md, figures/.")


if __name__ == "__main__":
    main()
