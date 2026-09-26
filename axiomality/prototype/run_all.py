#!/usr/bin/env python3
"""One command end to end:
rulebook self-check -> synthetic data -> error injection -> engine + baseline benchmark
-> Data Passport -> offline verification -> tamper demo -> figures."""
import json
import subprocess
import sys
import time

import benchmark
from data import generate
from figures import make_figures
from inject import inject
from kernel.axioms import self_check
from passport import passport
from util import RESULTS_DIR, ROOT, write_json


def step(name, fn):
    t0 = time.perf_counter()
    print(f"\n== {name}")
    out = fn()
    print(f"   ({time.perf_counter() - t0:.1f}s)")
    return out


def selfcheck():
    rep = self_check(json.loads((ROOT / "data" / "seed_sample_109.json").read_text()))
    write_json(RESULTS_DIR / "rulebook_selfcheck.json", rep)
    ep = rep["episode_layer"]
    print(f"[kernel] rulebook self-check: {rep['result']} | {rep['rulebook_rules']} rules, {rep['object_types']} object "
          f"types, {rep['ground_facts']} ground facts, {rep['total_z3_assertions']} Z3 assertions | seed scene 109: "
          f"{rep['seed_scene_109']['result']} | symbolic success episode: {ep['success']['result']}, slip failure: "
          f"{ep['slip_failure']['result']} | implied-by-others: {rep['independence']['implied_by_others']}")
    return rep


def cli(name, script):
    p = subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT, capture_output=True, text=True)
    print(p.stdout.rstrip())
    if p.returncode != 0:
        print(p.stderr)
        raise SystemExit(f"{name} failed with exit code {p.returncode}")


def main():
    if "--v2" in sys.argv:  # v2 (real data + noisy synthetic benchmark); v1 outputs are not touched
        raise SystemExit(subprocess.run([sys.executable, str(ROOT / "run_v2.py"),
                                         *[a for a in sys.argv[1:] if a != "--v2"]], cwd=ROOT).returncode)
    t0 = time.perf_counter()
    RESULTS_DIR.mkdir(exist_ok=True)
    rep = step("1. Knowledge kernel: rulebook self-check (Z3)", selfcheck)
    if not rep["result"].startswith("SATISFIABLE"):
        raise SystemExit("rulebook self-check failed")
    step("2. Synthetic dataset from sample 109", generate.main)
    step("3. Error injection into held-out copy", inject.main)
    step("4. Benchmark: engine vs rules-only baseline", benchmark.main)
    step("5. Data Passport (Ed25519)", passport.issue)
    step("6. Offline verification", lambda: cli("verify_passport", "verify_passport.py"))
    step("7. Tamper demo", lambda: cli("tamper_demo", "tamper_demo.py"))
    step("8. Figures", make_figures.main)
    print(f"\nDone in {time.perf_counter() - t0:.1f}s. See results/benchmark.md, results/passport_AX-DEMO-109.json, figures/.")


if __name__ == "__main__":
    main()
