#!/usr/bin/env python3
"""Verify an AXIOMALITY Data Passport offline.

    python verify_passport.py [--passport results/passport_AX-DEMO-109.json]
                              [--pubkey keys/axiomality_demo_ed25519.pub.pem] [--data <accepted.jsonl>]

Checks the Ed25519 signature against a trusted public key file (not the key
embedded in the passport) and recomputes the content hash from the data files.
Exit code 0 = valid, 1 = invalid.
"""
import argparse
import sys

from passport.passport import PUB, verify
from util import PASSPORT_FILE


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--passport", default=str(PASSPORT_FILE))
    ap.add_argument("--pubkey", default=str(PUB))
    ap.add_argument("--data", default=None, help="accepted split JSONL (default: path recorded in the passport)")
    a = ap.parse_args()
    ok, msgs = verify(a.passport, a.pubkey, a.data)
    for m in msgs:
        print("  " + m)
    print("PASSPORT VALID" if ok else "PASSPORT INVALID")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
