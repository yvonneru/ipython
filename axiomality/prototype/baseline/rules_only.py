"""Rules-only baseline: what a careful engineer writes in an afternoon.

Structural, per-channel checks in the spirit of dataset "doctor" tools. It gets
the same declared joint limits, joint speed limits, gripper stroke, class
vocabulary and the same global object speed bound (v_max) as the engine, but no
relational semantics (no object types/affordances, no support or contact
reasoning, no phase grammar, no kinematic model). Verdicts: PASS or REJECT.
"""
from __future__ import annotations

import time

import numpy as np

from kernel.rulebook import ARM, PHASES, PHYS, VOCAB

REQ_META = ("robot_id", "calibration_hash", "consent_id", "synthetic", "hz")
REQ_FRAMES = ("t", "tcp_pose", "gripper_cmd", "gripper_width", "joints", "object_poses", "phase")
MIN_FRAMES = 30


def check_episode(ep: dict) -> dict:
    t0 = time.perf_counter()
    issues = []
    meta, fr = ep.get("meta", {}), ep.get("frames", {})
    issues += [f"missing meta.{k}" for k in REQ_META if meta.get(k) in (None, "")]
    issues += [f"missing frames.{k}" for k in REQ_FRAMES if not fr.get(k)]
    if not issues:
        n = len(fr["t"])
        chans = {k: np.asarray(fr[k], float) for k in ("t", "tcp_pose", "gripper_cmd", "gripper_width", "joints")}
        chans.update({f"obj:{o}": np.asarray(v, float) for o, v in fr["object_poses"].items()})
        if any(len(v) != n for v in chans.values()) or len(fr["phase"]) != n:
            issues.append("channel length mismatch")
        elif n < MIN_FRAMES:
            issues.append(f"episode too short ({n} frames)")
        else:
            for k, v in chans.items():  # 1. NaN / Inf
                if not np.all(np.isfinite(v)):
                    issues.append(f"non-finite values in {k}")
            t, hz = chans["t"], float(meta["hz"])
            dt = np.diff(t)
            if np.any(dt <= 0):  # 2. monotonic timestamps
                issues.append(f"non-monotonic timestamp at frame {int(np.argmax(dt <= 0)) + 1}")
            elif np.any(dt > 1.5 / hz):  # 3. frame drops
                issues.append(f"frame drop at frame {int(np.argmax(dt > 1.5 / hz)) + 1}")
            q = chans["joints"]  # 4. joint limits and joint speed limits
            lo, hi = np.array(ARM["q_lower"]), np.array(ARM["q_upper"])
            if np.any((q < lo) | (q > hi)):
                issues.append(f"joint limit exceeded at frame {int(np.argmax(((q < lo) | (q > hi)).any(1)))}")
            if np.all(dt > 0):
                qd = np.abs(np.diff(q, axis=0)) / dt[:, None]
                if np.any(qd > np.array(ARM["qd_max"])):
                    issues.append("joint speed limit exceeded")
            w = chans["gripper_width"]  # 5. gripper range and binary command
            if np.any((w < 0) | (w > ARM["gripper_aperture"] + 1e-6)):
                issues.append("gripper width out of range")
            if not set(np.unique(chans["gripper_cmd"])).issubset({0.0, 1.0}):
                issues.append("gripper command not binary")
            if np.all(dt > 0):  # 6. spike detector: TCP and object speeds vs v_max
                for k, v in chans.items():
                    if k == "tcp_pose" or k.startswith("obj:"):
                        sp = np.linalg.norm(np.diff(v[:, :3], axis=0), axis=1) / dt
                        if np.any(sp > PHYS["v_max"]):
                            issues.append(f"{k} speed spike at frame {int(np.argmax(sp > PHYS['v_max'])) + 1}")
            if any(p not in PHASES for p in fr["phase"]):  # 7. label vocabularies
                issues.append("unknown phase label")
            for o in ep.get("scene", {}).get("objects", []):
                if o.get("label") not in VOCAB:
                    issues.append(f"unknown object label {o.get('label')}")
                if any(float(v) <= 0 for v in o.get("dimensions", {}).values()):
                    issues.append("non-positive object dimension")
            for e in ep.get("events", []):  # 8. events reference known objects / time range
                if e.get("object") not in fr["object_poses"] or not (t[0] <= e.get("t", -1) <= t[-1]):
                    issues.append("dangling event")
    return {"episode_id": ep.get("episode_id"), "verdict": "REJECT" if issues else "PASS", "issues": issues,
            "ms": (time.perf_counter() - t0) * 1e3}
