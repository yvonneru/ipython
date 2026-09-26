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


def check_episode(ep: dict, policy: dict | None = None) -> dict:
    """policy (v2 only; None = v1 behaviour): max_single_drops (isolated ~2/hz intervals tolerated),
    qd_margin (joint-speed limit multiplier, calibrated on clean noisy data)."""
    t0 = time.perf_counter()
    pol = policy or {}
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
                drop = dt > 1.5 / hz
                single = drop & (dt < 2.5 / hz)
                if not (pol.get("max_single_drops") and np.all(single == drop) and drop.sum() <= pol["max_single_drops"]):
                    issues.append(f"frame drop at frame {int(np.argmax(dt > 1.5 / hz)) + 1}")
            q = chans["joints"]  # 4. joint limits and joint speed limits
            lo, hi = np.array(ARM["q_lower"]), np.array(ARM["q_upper"])
            if np.any((q < lo) | (q > hi)):
                issues.append(f"joint limit exceeded at frame {int(np.argmax(((q < lo) | (q > hi)).any(1)))}")
            if np.all(dt > 0):
                qd = np.abs(np.diff(q, axis=0)) / dt[:, None]
                if np.any(qd > np.array(ARM["qd_max"]) * pol.get("qd_margin", 1.0)):
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


def check_real_episode(df, info: dict) -> dict:
    """The same baseline applied to a REAL LeRobot-style episode, running only the checks
    whose inputs exist: minimum length, NaN/Inf, joint position and speed limits (only
    when limits are known for the robot, i.e. the same limits the engine used), and the
    TCP speed spike vs v_max (only for an EE position in metres with a declared fps).
    Not applicable on real data: timestamps (absent), gripper width range and binary
    command (continuous, normalised gripper), label vocabularies, events."""
    t0 = time.perf_counter()
    issues, ran = [], ["min_frames", "finite"]
    prof = info.get("axiomality_profile", {})
    n = len(df)
    if n < MIN_FRAMES:
        issues.append(f"episode too short ({n} frames)")
    mats = {}
    for c in df.columns:
        if df[c].dtype == object:
            mats[c] = np.stack([np.asarray(x, float) for x in df[c]]) if n else np.zeros((0, 1))
    for c, v in mats.items():
        if not np.all(np.isfinite(v)):
            issues.append(f"non-finite values in {c}")
    lim, fps, jidx = prof.get("limits"), info.get("fps"), prof.get("joint_idx")
    if lim and jidx and n:
        ran += ["joint_limits", "joint_speed"]
        q = mats["observation.state"][:, jidx]
        lo, hi = np.array(lim["q_lower"]), np.array(lim["q_upper"])
        if np.any((q < lo) | (q > hi)):
            issues.append(f"joint limit exceeded at frame {int(np.argmax(((q < lo) | (q > hi)).any(1)))}")
        if fps and n > 1:
            qd = np.abs(np.diff(q, axis=0)) * fps
            if np.any(qd > np.array(lim["qd_max"])):
                issues.append("joint speed limit exceeded")
    if prof.get("ee_units_m") and fps and n > 1:
        ran.append("tcp_speed_spike")
        e = mats[prof["ee_state_column"]][:, prof["ee_state_idx"]]
        sp = np.linalg.norm(np.diff(e, axis=0), axis=1) * fps
        if np.any(sp > PHYS["v_max"]):
            issues.append(f"tcp speed spike at frame {int(np.argmax(sp > PHYS['v_max'])) + 1}")
    return {"verdict": "REJECT" if issues else "PASS", "issues": issues, "checks_run": ran,
            "ms": (time.perf_counter() - t0) * 1e3}
