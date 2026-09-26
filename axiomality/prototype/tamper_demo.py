#!/usr/bin/env python3
"""Tamper demo: modify the accepted data / passport and show verification fails,
then restore and show it passes again. Uses the real CLI (subprocess, exit codes)."""
import json
import shutil
import subprocess
import sys

from util import ACCEPTED_FILE, PASSPORT_FILE, ROOT, read_jsonl, write_jsonl


def run_verify(title: str) -> int:
    p = subprocess.run([sys.executable, str(ROOT / "verify_passport.py")], cwd=ROOT, capture_output=True, text=True)
    print(f"\n--- {title}\n{p.stdout.rstrip()}\n    exit code {p.returncode}")
    return p.returncode


def main() -> int:
    data_bak, pp_bak = ACCEPTED_FILE.with_suffix(".bak"), PASSPORT_FILE.with_suffix(".bak")
    shutil.copy(ACCEPTED_FILE, data_bak)
    shutil.copy(PASSPORT_FILE, pp_bak)
    results = []
    try:
        results.append(("untouched", run_verify("1. untouched data"), 0))

        eps = read_jsonl(data_bak)
        obj = eps[1]["scene"]["objects"][0]
        old = obj["label"]
        obj["label"] = "vase"
        write_jsonl(ACCEPTED_FILE, eps)
        results.append(("flip one label", run_verify(f"2. {eps[1]['episode_id']}: label '{old}' -> 'vase'"), 1))
        shutil.copy(data_bak, ACCEPTED_FILE)

        eps = read_jsonl(data_bak)
        eps[2]["frames"]["t"][10] = round(eps[2]["frames"]["t"][10] + 0.001, 6)
        write_jsonl(ACCEPTED_FILE, eps)
        results.append(("shift one timestamp", run_verify(f"3. {eps[2]['episode_id']}: frame 10 timestamp +1 ms"), 1))
        shutil.copy(data_bak, ACCEPTED_FILE)

        pp = json.loads(pp_bak.read_text())
        pp["verdict_counts"]["REJECT"] -= 5
        PASSPORT_FILE.write_text(json.dumps(pp, indent=2))
        results.append(("edit passport count", run_verify("4. passport REJECT count edited (-5)"), 1))
        shutil.copy(pp_bak, PASSPORT_FILE)

        results.append(("restored", run_verify("5. restored originals"), 0))
    finally:
        shutil.copy(data_bak, ACCEPTED_FILE)
        shutil.copy(pp_bak, PASSPORT_FILE)
        data_bak.unlink()
        pp_bak.unlink()
    print("\nTamper demo summary:")
    ok = True
    for name, code, want in results:
        good = code == want
        ok &= good
        print(f"  {name:<22} verify exit {code} (expected {want}) {'OK' if good else 'UNEXPECTED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
