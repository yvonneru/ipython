"""Shared helpers: paths, canonical JSON, hashing, JSONL I/O."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data" / "generated"
RESULTS_DIR = ROOT / "results"
FIG_DIR = ROOT / "figures"
KEYS_DIR = ROOT / "keys"

CLEAN_FILE = DATA_DIR / "clean_episodes.jsonl"
HELDOUT_FILE = DATA_DIR / "heldout_injected.jsonl"
KEY_FILE = DATA_DIR / "injection_key.json"
ACCEPTED_FILE = RESULTS_DIR / "accepted" / "accepted_episodes.jsonl"
PASSPORT_FILE = RESULTS_DIR / "passport_AX-DEMO-109.json"


def canonical_json(obj) -> bytes:
    """Deterministic JSON bytes: sorted keys, no whitespace, UTF-8."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path: Path, items) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, separators=(",", ":")) + "\n")


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)
