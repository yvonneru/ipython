"""Minimal pure-Python reader for TFDS/RLDS TFRecord shards (no TensorFlow needed).

A TFRecord file is a sequence of records:
    uint64 length | uint32 masked-crc32c(length) | bytes[length] data | uint32 masked-crc32c(data)
Each RLDS record is one episode serialised as a ``tf.train.Example`` whose feature keys are
flattened paths such as ``steps/observation/joint_position``; per-step tensors are
concatenated over all steps. TFDS stores every floating tensor (also float64) as a
``float_list`` of float32, integers/bools as ``int64_list`` and strings/images as
``bytes_list``.

Only the protobuf wire format needed for ``tf.train.Example`` is implemented. Features
whose key is not requested (e.g. camera images) are skipped without decoding.
"""
from __future__ import annotations

import struct
from pathlib import Path

import numpy as np


def _varint(buf: bytes, i: int) -> tuple[int, int]:
    shift = result = 0
    while True:
        b = buf[i]
        i += 1
        result |= (b & 0x7F) << shift
        if not b & 0x80:
            return result, i
        shift += 7


def _fields(buf: bytes, start: int = 0, end: int | None = None):
    """Yield (field_number, wire_type, value_or_(start,end)) for one protobuf message."""
    i, end = start, len(buf) if end is None else end
    while i < end:
        tag, i = _varint(buf, i)
        fn, wt = tag >> 3, tag & 7
        if wt == 0:
            v, i = _varint(buf, i)
            yield fn, wt, v
        elif wt == 2:
            ln, i = _varint(buf, i)
            yield fn, wt, (i, i + ln)
            i += ln
        elif wt == 5:
            yield fn, wt, buf[i:i + 4]
            i += 4
        elif wt == 1:
            yield fn, wt, buf[i:i + 8]
            i += 8
        else:
            raise ValueError(f"unsupported wire type {wt}")


def _decode_feature(buf: bytes, s: int, e: int):
    for fn, wt, v in _fields(buf, s, e):  # Feature: oneof 1 bytes_list, 2 float_list, 3 int64_list
        ls, le = v
        if fn == 1:
            return [buf[a:b] for f2, _, (a, b) in _fields(buf, ls, le) if f2 == 1]
        if fn == 2:
            out = []
            for f2, wt2, v2 in _fields(buf, ls, le):
                if wt2 == 2:  # packed
                    out.append(np.frombuffer(buf[v2[0]:v2[1]], dtype="<f4"))
                else:
                    out.append(np.frombuffer(v2, dtype="<f4"))
            return np.concatenate(out) if out else np.zeros(0, np.float32)
        if fn == 3:
            out = []
            for f2, wt2, v2 in _fields(buf, ls, le):
                if wt2 == 2:
                    j = v2[0]
                    while j < v2[1]:
                        x, j = _varint(buf, j)
                        out.append(x - (1 << 64) if x >= 1 << 63 else x)
                else:
                    out.append(v2 - (1 << 64) if v2 >= 1 << 63 else v2)
            return np.asarray(out, dtype=np.int64)
    return None


def parse_example(buf: bytes, keys: set[str] | None = None) -> dict:
    out = {}
    for fn, _, (s, e) in _fields(buf):  # Example.features = 1
        if fn != 1:
            continue
        for fn2, _, (s2, e2) in _fields(buf, s, e):  # Features.feature map entries = 1
            if fn2 != 1:
                continue
            key, val = None, None
            for fn3, _, (s3, e3) in _fields(buf, s2, e2):
                if fn3 == 1:
                    key = buf[s3:e3].decode("utf-8")
                elif fn3 == 2:
                    val = (s3, e3)
            if key is not None and val is not None and (keys is None or key in keys):
                out[key] = _decode_feature(buf, *val)
    return out


def iter_records(path: Path):
    with open(path, "rb") as f:
        while True:
            hdr = f.read(12)
            if not hdr:
                return
            if len(hdr) < 12:
                raise ValueError(f"{path}: truncated record header")
            (n,) = struct.unpack("<Q", hdr[:8])
            data = f.read(n)
            if len(data) < n or len(f.read(4)) < 4:
                raise ValueError(f"{path}: truncated record")
            yield data


def list_keys(path: Path) -> dict:
    """Keys and value counts of the first record (for inspection)."""
    rec = next(iter_records(path))
    d = parse_example(rec)
    return {k: (type(v).__name__, len(v)) for k, v in d.items()}
