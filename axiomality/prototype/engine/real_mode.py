"""AXIOMALITY real-data mode: run only the checks a real dataset can support.

Input: a LeRobot-v2-style dataset directory (meta/info.json, meta/episodes.jsonl,
meta/tasks.jsonl, data/chunk-000/episode_*.parquet). Nothing about object poses,
contacts or phases is assumed. Every check family reports, per episode, one of
    PASS     checked, nothing found
    REPAIR   a deterministic, lossless fix exists (applied to the accepted split)
    REJECT   a data-supported defect (hard evidence: bit-level, declared limits,
             datasheet limits or a physically unambiguous contradiction)
    UNKNOWN  the dataset does not contain what the check needs (reason given)
Heuristic findings (outlier-vs-robust-range, assumed semantics) are reported as
ADVISORY flags. They are listed with evidence but never change a verdict, because
their thresholds are not backed by a declaration.

Check families (rule ids in brackets map to the kernel rulebook where the physical
principle is the same):
  timing        timestamp monotonicity, gaps / jitter vs declared fps        [R-TIME-01/02]
  boundaries    frame_index / index continuity, is_first/is_last flags,
                zero-length and very short episodes
  numeric       NaN / Inf in any numeric channel                             [R-QTY-01]
  frames        duplicated frames (every channel bit-identical, non-idle)
  joint_limits  declared or datasheet limits (hard) / robust range (advisory) [R-JNT-01]
  motion        joint-speed limit (hard, needs fps + limits); teleport-like
                jumps and acceleration spikes vs robust range (advisory)      [R-JNT-02, R-PERM-01]
  kinematics    recorded EE pose vs forward kinematics of recorded joints
                (only when the kernel has the robot's kinematic model)       [R-KIN-01]
  action_state  commanded action vs observed next state
  gripper       gripper command vs gripper state                            [R-GRIP-01 analogue]
  duplicates    duplicate episodes (hash of the state sequence)
  task          task string present, constant within the episode, normalised
  outcome       outcome label vs reward signal, when both exist
  semantic      object type/size, support, contact, permanence, spatial,
                phase grammar, task-success geometry -> always UNKNOWN here:
                "no object state in dataset"      [R-TYPE, R-SUP, R-SPAT, R-PERM-02/03, R-CONT, R-PHASE, R-TASK]
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path

import numpy as np
import pandas as pd

from kernel.arm import _mdh
from kernel.rulebook import ARM, PHYS

REAL_MODE_VERSION = "ax-real-mode-0.1.0"
FAMILIES = ["timing", "boundaries", "numeric", "frames", "joint_limits", "motion", "kinematics", "action_state",
            "gripper", "duplicates", "task", "outcome", "semantic"]
FAMILY_RULE = {"timing": "R-TIME-01/02", "numeric": "R-QTY-01", "joint_limits": "R-JNT-01",
               "motion": "R-JNT-02 / R-PERM-01", "kinematics": "R-KIN-01", "gripper": "R-GRIP-01 (analogue)",
               "semantic": "R-TYPE/SUP/SPAT/PERM/CONT/PHASE/TASK"}
SEMANTIC_REASON = ("no object state in dataset: object poses, object classes/dimensions, contact events and phase "
                   "labels are not recorded, so type/size, support, contact, permanence, spatial, phase-grammar and "
                   "task-success rules cannot be evaluated")
KINEMATIC_MODELS = {"franka_panda": "kernel/arm.py Panda-style modified DH (flange frame, base at origin)"}
CATALOGUE = {  # hashed into the passport
    "version": REAL_MODE_VERSION, "families": FAMILIES,
    "thresholds": {"min_seconds_advisory": 2.0, "short_frames_no_fps": 20, "dup_run_reject": 3,
                   "stuck_cmd_rad": 0.02, "stuck_static_rad": 1e-4, "stuck_min_seconds": 1.0,
                   "lagged_div_rad": 0.10, "lagged_div_seconds": 2.0, "grip_lag_seconds": 1.0,
                   "grip_min_seconds": 1.5, "kin_tol_m": PHYS["fk_tol"], "spike_factor": 4.0, "range_factor": 0.5},
}


def catalogue_hash() -> str:
    return "sha256:" + hashlib.sha256(json.dumps(CATALOGUE, sort_keys=True).encode()).hexdigest()


# ------------------------------------------------------------------ loading
def load_dataset(path: Path) -> dict:
    path = Path(path)
    info = json.loads((path / "meta" / "info.json").read_text())
    eps_meta = [json.loads(line) for line in (path / "meta" / "episodes.jsonl").read_text().splitlines() if line.strip()]
    tasks = {}
    tp = path / "meta" / "tasks.jsonl"
    if tp.exists():
        for line in tp.read_text().splitlines():
            if line.strip():
                d = json.loads(line)
                tasks[d["task_index"]] = d["task"]
    frames = []
    for em in eps_meta:
        f = path / info["data_path"].format(episode_index=em["episode_index"])
        frames.append(pd.read_parquet(f) if f.exists() else None)
    return {"name": path.name, "path": path, "info": info, "episodes": eps_meta, "tasks": tasks, "frames": frames}


def _mat(df: pd.DataFrame, col: str) -> np.ndarray | None:
    if df is None or col not in df.columns:
        return None
    if len(df) == 0:
        return np.zeros((0, 0))
    v = df[col].to_numpy()
    if v.dtype == object:
        return np.stack([np.asarray(x, float) for x in v])
    return v.astype(float)[:, None]


def _runs(mask: np.ndarray) -> list[tuple[int, int]]:
    """[(start, end_exclusive)] of True runs."""
    m = np.r_[False, np.asarray(mask, bool), False]
    d = np.diff(m.astype(int))
    return list(zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1)))


class _Fam:
    def __init__(self):
        self.verdict, self.findings, self.advisories, self.reason = "PASS", [], [], None

    def reject(self, frame, what, why, check):
        self.verdict = "REJECT"
        self.findings.append({"frame": None if frame is None else int(frame), "what": what, "why": why,
                              "check": check, "evidence": "hard"})

    def repair(self, frame, what, why, check, action):
        if self.verdict == "PASS":
            self.verdict = "REPAIR"
        self.findings.append({"frame": None if frame is None else int(frame), "what": what, "why": why,
                              "check": check, "evidence": "hard", "repair": action})

    def advise(self, frame, what, why, check):
        self.advisories.append({"frame": None if frame is None else int(frame), "what": what, "why": why,
                                "check": check, "evidence": "heuristic"})

    def unknown(self, reason):
        self.verdict, self.reason = "UNKNOWN", reason

    def out(self):
        d = {"verdict": self.verdict, "findings": self.findings, "advisories": self.advisories}
        if self.reason:
            d["reason"] = self.reason
        return d


# ------------------------------------------------------------------ dataset-level statistics
def _dataset_stats(ds: dict) -> dict:
    prof = ds["info"].get("axiomality_profile", {})
    st = {}
    states = [_mat(df, "observation.state") for df in ds["frames"] if df is not None and len(df)]
    jidx = prof.get("joint_idx") or []
    if states and jidx:
        Q = np.concatenate([s[:, jidx] for s in states])
        lo, hi = np.percentile(Q, 0.5, axis=0), np.percentile(Q, 99.5, axis=0)
        st["robust_range"] = (lo, hi)
        dq = np.concatenate([np.abs(np.diff(s[:, jidx], axis=0)) for s in states if len(s) > 1])
        ddq = np.concatenate([np.abs(np.diff(s[:, jidx], 2, axis=0)) for s in states if len(s) > 2])
        st["dq_p999"], st["ddq_p999"] = np.percentile(dq, 99.9, axis=0), np.percentile(ddq, 99.9, axis=0)
    if states:
        S = np.concatenate(states)
        var = [j for j in range(S.shape[1]) if np.ptp(S[:, j]) > 0]
        uniq = [len(np.unique(S[:, j])) / len(S) for j in var]
        if var and np.median(uniq) < 0.2:
            st["quantized_state"] = (f"median {np.median(uniq):.0%} distinct values per non-constant state channel "
                                     f"over {len(S)} frames")
    ee_col, ee_idx = prof.get("ee_state_column"), prof.get("ee_state_idx")
    if ee_col and ee_idx:
        E = [(_mat(df, ee_col)[:, ee_idx]) for df in ds["frames"] if df is not None and len(df) > 2]
        de = np.concatenate([np.linalg.norm(np.diff(e, axis=0), axis=1) for e in E])
        dde = np.concatenate([np.linalg.norm(np.diff(e, 2, axis=0), axis=1) for e in E])
        st["ee_step_p999"], st["ee_acc_p999"] = np.percentile(de, 99.9), np.percentile(dde, 99.9)
        allE = np.concatenate(E)
        st["ee_extreme"] = (allE.min(0), allE.max(0))
        if prof.get("action_ee_idx"):
            A = np.concatenate([_mat(df, "action")[:, prof["action_ee_idx"]] for df in ds["frames"]
                                if df is not None and len(df)])
            st["ee_action_scale"] = np.abs(A).max(0)
    if prof.get("action_interface") == "absolute_joint_position":
        lags = []
        for df in ds["frames"]:
            if df is None or len(df) < 30:
                continue
            q, qa = _mat(df, "observation.state")[:, jidx], _mat(df, prof["action_joint_column"])
            if np.abs(np.diff(q, axis=0)).max() < 1e-3:
                continue
            err = [np.median(np.abs(qa[:len(q) - k] - q[k:]).max(1)) for k in range(0, 11)]
            lags.append(int(np.argmin(err)))
        st["lag"] = int(np.median(lags)) if lags else 0
        st["lag_per_episode"] = lags
    return st


def _column_aliases(ds: dict) -> list[dict]:
    """Dataset-level: numeric columns that are bit-identical to (a slice of) another column."""
    dfs = [df for df in ds["frames"] if df is not None and len(df)]
    if not dfs:
        return []
    cols = [c for c in dfs[0].columns if dfs[0][c].dtype == object]
    mats = {c: np.concatenate([_mat(df, c) for df in dfs]) for c in cols}
    feats = ds["info"].get("features", {})
    out = []
    for a in cols:
        for b in cols:
            if a == b:
                continue
            A, B = mats[a], mats[b]
            k = B.shape[1]
            if A.shape[1] > k and np.array_equal(A[:, :k], B):
                out.append({"column": a, "slice": f"[:{k}]", "equals": b,
                            "declared_as": feats.get(a, {}).get("source_description", ""),
                            "other_declared_as": feats.get(b, {}).get("source_description", "")})
            elif A.shape[1] == k and a < b and np.array_equal(A, B):
                out.append({"column": a, "slice": "", "equals": b,
                            "declared_as": feats.get(a, {}).get("source_description", ""),
                            "other_declared_as": feats.get(b, {}).get("source_description", "")})
    return out


# ------------------------------------------------------------------ per-episode checks
def _check_episode(ds: dict, i: int, st: dict, seen_hashes: dict) -> dict:
    info, prof, em, df = ds["info"], ds["info"].get("axiomality_profile", {}), ds["episodes"][i], ds["frames"][i]
    fps = info.get("fps")
    F = {f: _Fam() for f in FAMILIES}
    F["semantic"].unknown(SEMANTIC_REASON)
    n = 0 if df is None else len(df)

    # ---- boundaries
    B = F["boundaries"]
    if df is None:
        B.reject(None, "episode file missing", "meta/episodes.jsonl lists an episode with no data file", "file")
    elif n == 0:
        B.reject(None, "zero-length episode", "episode contains no frames", "zero_length")
    if n == 0:
        for f in FAMILIES:
            if f not in ("boundaries", "semantic"):
                F[f].unknown("no frames")
        return {f: F[f].out() for f in FAMILIES}
    fi = df["frame_index"].to_numpy()
    if not np.array_equal(fi, np.arange(n)):
        k = int(np.flatnonzero(fi != np.arange(n))[0])
        B.reject(k, f"frame_index breaks at row {k} (value {fi[k]})", "frame indices must run 0..n-1 without "
                 "gaps, repeats or resets", "frame_index")
    if not (df["episode_index"].to_numpy() == em["episode_index"]).all():
        B.reject(None, "episode_index column disagrees with episode metadata", "rows from another episode", "episode_index")
    if em.get("length") is not None and em["length"] != n:
        B.reject(None, f"declared length {em['length']} != {n} rows", "metadata/data mismatch", "length")
    if "is_first" in df:
        f1 = np.flatnonzero(df["is_first"].to_numpy())
        if list(f1) != [0]:
            B.reject(f1[1] if len(f1) > 1 else 0, f"is_first set at frames {list(f1)[:5]}", "exactly one is_first "
                     "flag at frame 0 is required; anything else means merged or split episodes", "is_first")
    if "next.is_last" in df:
        fl = np.flatnonzero(df["next.is_last"].to_numpy())
        if list(fl) != [n - 1]:
            B.reject(fl[0] if len(fl) else n - 1, f"is_last set at frames {list(fl)[:5]}", "exactly one is_last flag "
                     "at the final frame is required", "is_last")
    if "action.terminate_episode" in df:
        te = _mat(df, "action.terminate_episode")
        term = np.flatnonzero(te[:, 0] == 1)
        if len(term) and term[0] != n - 1:
            B.reject(term[0], f"terminate_episode flag at frame {term[0]} of {n}", "terminate action before the "
                     "final frame: the episode continues after it declared termination", "terminate")
    short = (n < CATALOGUE["thresholds"]["min_seconds_advisory"] * fps) if fps else (n < CATALOGUE["thresholds"]["short_frames_no_fps"])
    if short:
        B.advise(None, f"very short episode: {n} frames" + (f" ({n / fps:.1f} s)" if fps else ""),
                 "shorter than 2 s of data; often an aborted recording", "short")

    # ---- numeric
    num_cols = [c for c in df.columns if df[c].dtype == object or np.issubdtype(df[c].dtype, np.number)]
    for c in num_cols:
        try:
            m = _mat(df, c)
        except (TypeError, ValueError):
            continue
        bad = ~np.isfinite(m)
        if bad.any():
            k = int(np.flatnonzero(bad.any(1))[0])
            F["numeric"].reject(k, f"non-finite value in {c}", "NaN/Inf cannot be trained on or checked", "finite")
            break

    # ---- timing
    T = F["timing"]
    if "timestamp" not in df.columns:
        T.unknown("no per-frame timestamps in dataset" + (" (fps is declared externally only)" if fps else ""))
    else:
        t = df["timestamp"].to_numpy(float)
        dt = np.diff(t)
        if np.any(dt <= 0):
            ts = np.sort(t)
            if np.all(np.diff(ts) > 0):
                k = int(np.flatnonzero(dt <= 0)[0]) + 1
                T.repair(k, f"rows out of timestamp order at frame {k}", "rows can be re-sorted into a strictly "
                         "increasing time base", "monotonic", "re-sort rows by timestamp")
            else:
                k = int(np.flatnonzero(dt <= 0)[0]) + 1
                T.reject(k, f"duplicate/non-increasing timestamp at frame {k} ({t[k]:.4f} s)",
                         "time base cannot be restored by re-sorting", "monotonic")
        if fps:
            ts = np.sort(t)
            d = np.diff(ts) * fps
            gaps = np.flatnonzero(d > 1.5)
            if len(gaps):
                k = int(gaps[0]) + 1
                miss = int(np.round(d[gaps] - 1).sum())
                msg = f"{len(gaps)} gap(s) totalling ~{miss} dropped frame(s); first at frame {k} ({d[gaps[0]]:.1f}/fps)"
                if miss > 0.01 * n or d[gaps].max() > 5:
                    T.reject(k, msg, "more than 1% of frames missing or a gap > 5 frames", "gaps")
                else:
                    T.advise(k, msg, "isolated dropped frame(s) vs declared fps", "gaps")
            jit = np.flatnonzero(np.abs(d - 1) > 0.25)
            jit = [j for j in jit if d[j] <= 1.5]
            if jit:
                T.advise(int(jit[0]) + 1, f"{len(jit)} interval(s) deviate > 25% from 1/fps", "timing jitter", "jitter")

    state = _mat(df, "observation.state")
    action = _mat(df, "action")
    jidx = prof.get("joint_idx") or []
    q = state[:, jidx] if jidx else None

    # ---- frames: duplicated frames (all float channels bit-identical to the previous row)
    Fr = F["frames"]
    float_cols = [c for c in df.columns if df[c].dtype == object]
    full = np.concatenate([_mat(df, c) for c in float_cols], axis=1)
    same = np.all(full[1:] == full[:-1], axis=1)
    idle_action = np.all(action[1:] == 0, axis=1) if action is not None else np.zeros(n - 1, bool)
    dup = same & ~idle_action
    if st.get("quantized_state"):
        Fr.unknown(f"state is quantized ({st['quantized_state']}); bit-identical consecutive rows are expected and "
                   "are not evidence of a stale stream")
    elif dup.any():
        runs = _runs(dup)
        longest = max(e - s for s, e in runs)
        k = int(runs[0][0]) + 1
        if longest >= CATALOGUE["thresholds"]["dup_run_reject"]:
            Fr.reject(k, f"{int(dup.sum())} duplicated frame(s), longest run {longest} (from frame {k})",
                      "every channel incl. a non-zero action is bit-identical to the previous frame: a stale or "
                      "frozen data stream, not an idle robot", "duplicate_frames")
        elif dup.sum() <= 0.05 * n:
            Fr.repair(k, f"{int(dup.sum())} isolated duplicated frame(s), first at frame {k}",
                      "logging duplicate: bit-identical row", "duplicate_frames", "drop duplicated rows")
        else:
            Fr.reject(k, f"{int(dup.sum())} duplicated frames ({dup.mean():.0%})", "too many duplicates", "duplicate_frames")
    idle = same & idle_action
    if idle.any():
        runs = _runs(idle)
        s0, e0 = runs[-1]
        if e0 == n - 1 and e0 - s0 >= 5:
            Fr.advise(int(s0) + 1, f"idle tail: last {e0 - s0} frames have zero action and unchanged state",
                      "idle frames add no information; consider trimming", "idle_tail")

    # ---- joint limits
    J = F["joint_limits"]
    lim = prof.get("limits")
    if q is None:
        J.unknown("no joint angles in dataset")
    else:
        if lim:
            lo, hi = np.asarray(lim["q_lower"]), np.asarray(lim["q_upper"])
            bad = (q < lo) | (q > hi)
            if bad.any():
                k = int(np.flatnonzero(bad.any(1))[0])
                j = int(np.flatnonzero(bad[k])[0])
                over = np.maximum(q[:, j] - hi[j], lo[j] - q[:, j]).max()
                J.reject(k, f"joint {j + 1} = {q[k, j]:.4f} rad outside [{lo[j]:.4f}, {hi[j]:.4f}] on "
                            f"{int(bad[:, j].sum())} frame(s), max excess {over * 1e3:.1f} mrad",
                         f"limits from {lim['source'].split(';')[0]}", "limits")
        if "robust_range" in st:
            rlo, rhi = st["robust_range"]
            span = rhi - rlo
            f = CATALOGUE["thresholds"]["range_factor"]
            bad = (q < rlo - f * span) | (q > rhi + f * span)
            if bad.any():
                k = int(np.flatnonzero(bad.any(1))[0])
                j = int(np.flatnonzero(bad[k])[0])
                J.advise(k, f"joint {j + 1} = {q[k, j]:.3f} rad far outside the dataset's robust range "
                            f"[{rlo[j]:.3f}, {rhi[j]:.3f}]", "HEURISTIC outlier vs per-joint 0.5-99.5% range", "robust_range")
        if not lim:
            J.reason = "no joint limits declared in dataset metadata; only a heuristic robust-range check ran"

    # ---- motion: speed limits (hard) + spikes (advisory)
    M = F["motion"]
    ran = False
    if q is not None and len(q) > 2:
        ran = True
        dq = np.abs(np.diff(q, axis=0))
        if lim and lim.get("qd_max") and fps:
            qd = dq * fps
            bad = qd > np.asarray(lim["qd_max"])
            if bad.any():
                k = int(np.flatnonzero(bad.any(1))[0])
                j = int(np.argmax(qd[k] / np.asarray(lim["qd_max"])))
                M.reject(k + 1, f"joint {j + 1} speed {qd[k, j]:.2f} rad/s > datasheet {lim['qd_max'][j]} rad/s",
                         "joint moved further in one frame than the actuator can (teleport-like jump)", "speed_limit")
        if "dq_p999" in st:
            sf = CATALOGUE["thresholds"]["spike_factor"]
            bad = dq > sf * np.maximum(st["dq_p999"], 1e-6)
            if bad.any():
                k = int(np.flatnonzero(bad.any(1))[0])
                j = int(np.argmax(dq[k] / st["dq_p999"]))
                M.advise(k + 1, f"joint {j + 1} jumps {dq[k, j]:.3f} rad in one frame ({dq[k, j] / st['dq_p999'][j]:.1f}x "
                                f"the dataset 99.9th percentile)", "HEURISTIC teleport-like jump", "jump")
            ddq = np.abs(np.diff(q, 2, axis=0))
            bad = ddq > sf * np.maximum(st["ddq_p999"], 1e-6)
            if bad.any():
                k = int(np.flatnonzero(bad.any(1))[0])
                j = int(np.argmax(ddq[k] / st["ddq_p999"]))
                M.advise(k + 1, f"joint {j + 1} acceleration spike ({ddq[k, j]:.3f} rad/frame^2, "
                                f"{ddq[k, j] / st['ddq_p999'][j]:.1f}x p99.9)", "HEURISTIC acceleration spike", "accel")
    ee_col, ee_idx = prof.get("ee_state_column"), prof.get("ee_state_idx")
    if ee_col and ee_idx and "ee_step_p999" in st and n > 2:
        ran = True
        e = _mat(df, ee_col)[:, ee_idx]
        step = np.linalg.norm(np.diff(e, axis=0), axis=1)
        sf = CATALOGUE["thresholds"]["spike_factor"]
        bad = step > sf * max(st["ee_step_p999"], 1e-9)
        if bad.any():
            k = int(np.flatnonzero(bad)[0])
            M.advise(k + 1, f"end effector jumps {step[k]:.3f} (state units) in one frame "
                            f"({step[k] / st['ee_step_p999']:.1f}x p99.9)", "HEURISTIC teleport-like EE jump", "ee_jump")
        if fps and prof.get("ee_units_m"):  # only when the dataset declares metres
            v = step * fps
            if np.any(v > PHYS["v_max"]):
                k = int(np.argmax(v > PHYS["v_max"]))
                M.reject(k + 1, f"EE speed {v[k]:.1f} m/s > v_max {PHYS['v_max']} m/s", "teleport", "ee_speed")
    if not ran:
        M.unknown("no joint or end-effector trajectory in dataset")

    # ---- kinematics (R-KIN-01) where the kernel has the robot's kinematic model
    K = F["kinematics"]
    if info.get("robot_type") in KINEMATIC_MODELS and q is not None and "observation.cartesian_position" in df:
        c = _mat(df, "observation.cartesian_position")[:, :3]
        Tm = np.tile(np.eye(4), (n, 1, 1))
        for jj, (a, d, al) in enumerate(ARM["dh"]):
            Tm = Tm @ _mdh(a, d, al, q[:, jj])
        flange = Tm[:, :3, :3] @ np.array([0, 0, ARM["flange_d"]]) + Tm[:, :3, 3]
        err = np.linalg.norm(flange - c, axis=1)
        K.stat = float(err.max())
        if np.any(err > PHYS["fk_tol"]):
            k = int(np.argmax(err > PHYS["fk_tol"]))
            K.reject(k, f"recorded Cartesian position differs from FK(joints) by {err[k] * 1e3:.1f} mm",
                     f"recorded EE pose must equal forward kinematics of the recorded joints (tol {PHYS['fk_tol'] * 1e3:.0f} mm)",
                     "fk")
    else:
        K.unknown("kernel has no kinematic model for robot_type "
                  f"'{info.get('robot_type')}'" if q is not None else "no joint angles in dataset")

    # ---- action-state consistency
    A = F["action_state"]
    iface = prof.get("action_interface")
    th = CATALOGUE["thresholds"]
    if iface == "absolute_joint_position" and q is not None and prof.get("action_joint_column") in df:
        qa = _mat(df, prof["action_joint_column"])
        win = int(np.ceil(th["stuck_min_seconds"] * (fps or 10)))
        cmd_off = np.abs(qa[:-1] - q[:-1]).max(1) > th["stuck_cmd_rad"]
        static = np.abs(np.diff(q, axis=0)).max(1) < th["stuck_static_rad"]
        for s, e in _runs(cmd_off & static):
            if e - s >= win:
                gap = np.abs(qa[s:e] - q[s:e]).max(1)
                A.reject(s, f"commanded motion not executed for {e - s} frames ({(e - s) / (fps or 1):.1f} s): all joints "
                            f"static (|dq| < {th['stuck_static_rad']:.0e} rad/frame) while the commanded joint position "
                            f"differs by {np.median(gap):.3f} rad (median)",
                         "the recorded actions do not produce the recorded next states (stuck arm, controller not "
                         "engaged or stale state stream); a policy trained on these pairs learns that commands do "
                         "nothing", "stuck")
                break
        L = st.get("lag", 0)
        if n > L + 1:
            r = np.abs(qa[:n - L] - q[L:]).max(1)
            wl = int(np.ceil(th["lagged_div_seconds"] * (fps or 10)))
            for s, e in _runs(r > th["lagged_div_rad"]):
                if e - s >= wl:
                    A.advise(s, f"commanded vs observed joints (lag {L} frames) diverge by > {th['lagged_div_rad']} rad "
                                f"for {e - s} frames (max {r[s:e].max():.3f} rad)",
                             "HEURISTIC persistent tracking error", "lagged_divergence")
                    break
    elif iface == "ee_delta" and ee_col and ee_idx:
        e = _mat(df, ee_col)[:, ee_idx]
        a = action[:, prof["action_ee_idx"]]
        scale = st.get("ee_action_scale", np.abs(a).max(0))
        emin, emax = st.get("ee_extreme", (e.min(0), e.max(0)))
        noise = np.median(np.linalg.norm(np.diff(e, axis=0), axis=1)) + 1e-9
        for ax in range(a.shape[1]):
            sgn = np.sign(np.where(np.abs(a[:, ax]) >= 0.5 * scale[ax], a[:, ax], 0))
            for s, t_end in _runs(sgn[:-1] != 0):
                for s2, e2 in [(s, t_end)]:
                    if e2 - s2 < 2:
                        continue
                    sg = np.sign(a[s2, ax])
                    if not np.all(np.sign(a[s2:e2, ax]) == sg):
                        continue
                    end = min(e2 + 1, n - 1)
                    net = e[end, ax] - e[s2, ax]
                    at_bound = (e[s2:end + 1, ax] >= emax[ax]).any() if sg > 0 else (e[s2:end + 1, ax] <= emin[ax]).any()
                    if at_bound:
                        continue
                    if net == 0 and np.all(e[s2:end + 1, ax] == e[s2, ax]):
                        A.advise(s2, f"axis {'xyz'[ax]}: commanded {'+' if sg > 0 else '-'} for {e2 - s2} frames, EE "
                                     f"position unchanged (not at the dataset's workspace bound)",
                                 "HEURISTIC commanded motion not executed; a benign cause is contact with a surface "
                                 "(e.g. pressing on a board), which cannot be checked without object state", "no_motion")
                        break
                    if np.sign(net) == -sg and abs(net) > 3 * noise:
                        A.advise(s2, f"axis {'xyz'[ax]}: commanded {'+' if sg > 0 else '-'} for {e2 - s2} frames but the EE "
                                     f"moved {net:+.3f} (opposite)", "HEURISTIC delta-action sign disagreement (action "
                                     "scale/frame not declared)", "sign")
                        break
        A.reason = "ee-delta action interface: action-to-motion scale and frame are not declared; only a heuristic sign check ran"
    else:
        A.unknown("action interface not declared or required channels missing")

    # ---- gripper
    G = F["gripper"]
    gs_idx, gc_col, gc_aidx = prof.get("gripper_state_idx"), prof.get("gripper_cmd_column"), prof.get("gripper_cmd_action_idx")
    if gs_idx is not None and gc_col in df and fps:
        gs, gc = state[:, gs_idx], _mat(df, gc_col)[:, 0]
        lag = int(round(th["grip_lag_seconds"] * fps))
        win = int(round(th["grip_min_seconds"] * fps))
        for closing, cond, what, why in (
                (True, gc >= 0.5, "close commanded (cmd >= 0.5) but gripper state stays <= 0.02 (fully open)",
                 "fingers never moved although closing was commanded (a grasped object stops the fingers partly "
                 "closed, never fully open)"),
                (False, gc <= 0.1, "open commanded (cmd <= 0.1) but gripper state stays >= 0.5 (closed)",
                 "gripper never opened although opening was commanded")):
            for s, e in _runs(cond):
                if e - s >= win + lag:
                    obs = gs[s + lag:e]
                    bad = np.all(obs <= 0.02) if closing else np.all(obs >= 0.5)
                    if bad:
                        G.reject(s + lag, f"{what} for {e - s - lag} frames", why, "cmd_vs_state")
                        break
        mid = (gc > 0.1) & (gc < 0.5) & (gs == 0)
        for s, e in _runs(mid):
            if e - s >= win:
                G.advise(s, f"partial close command ({gc[s:e].max():.2f}) with gripper state exactly 0 for {e - s} frames",
                         "HEURISTIC: command below an unknown deadband or gripper not reporting", "partial_cmd")
                break
    elif prof.get("finger_state_idx") and gc_aidx is not None and fps:
        fs = state[:, prof["finger_state_idx"]].mean(1)
        gc = action[:, gc_aidx]
        lo_, hi_ = np.percentile(fs, 5), np.percentile(fs, 95)
        lag = int(round(th["grip_lag_seconds"] * fps))
        for s, e in _runs(gc != 0):
            sg = np.sign(gc[s])
            end = min(e + lag, n - 1)
            change = fs[end] - fs[s]
            already = fs[s] >= hi_ - 0.02 if sg > 0 else fs[s] <= lo_ + 0.02
            if not already and sg * change < 0.05:
                G.advise(s, f"gripper {'close' if sg > 0 else 'open'} command for {e - s} frames but finger joints "
                            f"change {change:+.3f} rad", "HEURISTIC (command semantics assumed, not declared)", "cmd_vs_state")
                break
        G.reason = "gripper command semantics not declared in the dataset; heuristic check only"
    else:
        G.unknown("gripper command semantics not documented or channels missing")

    # ---- duplicates (exact hash of state sequence; earlier episode keeps it)
    D = F["duplicates"]
    h = hashlib.sha256(np.ascontiguousarray(state.astype(np.float32)).tobytes()).hexdigest()
    if h in seen_hashes:
        D.reject(None, f"state sequence identical to episode {seen_hashes[h]}", "duplicate episode (sha256 of the "
                 "state sequence); the earlier copy is kept", "hash")
    else:
        seen_hashes[h] = em["episode_index"]
    src = em.get("source_file_path")
    if src:
        prev = seen_hashes.get(("src", src))
        if prev is not None:
            D.advise(None, f"same source_file_path as episode {prev} ({src[-60:]})", "possible re-export of one "
                     "recording", "source_path")
        else:
            seen_hashes[("src", src)] = em["episode_index"]

    # ---- task strings
    Tk = F["task"]
    if "task_index" in df and ds["tasks"]:
        tix = df["task_index"].to_numpy()
        if len(set(tix)) > 1:
            k = int(np.flatnonzero(tix != tix[0])[0])
            Tk.reject(k, f"task string changes within the episode at frame {k}", "one episode, one instruction", "constant")
        task = ds["tasks"].get(int(tix[0]))
        alts = [s for s in em.get("tasks", []) if s.strip()]
        if task is None:
            Tk.reject(0, f"task_index {tix[0]} not in meta/tasks.jsonl", "dangling task reference", "reference")
        elif not task.strip():
            if alts:
                Tk.repair(0, "primary instruction empty, alternate instruction present", "an alternate instruction "
                          "recorded for the same episode can be promoted", "empty", f"use alternate '{alts[0]}'")
            else:
                Tk.reject(0, "empty task / language instruction", "episode cannot be used for language-conditioned "
                          "training and its task is undocumented", "empty")
        elif re.sub(r"\s+", " ", task).strip() != task:
            Tk.repair(0, f"whitespace anomaly in task string {task!r}", "double/leading/trailing whitespace",
                      "whitespace", "collapse whitespace")
    else:
        Tk.unknown("no task strings in dataset")

    # ---- outcome label vs reward
    O = F["outcome"]
    src = em.get("source_file_path") or ""
    if "outcome_from" in prof and "next.reward" in df and ("/success/" in src or "/failure/" in src):
        lab_success = "/success/" in src
        r_last = float(df["next.reward"].to_numpy()[-1])
        if lab_success != (r_last == 1.0):
            O.reject(n - 1, f"recording labelled {'success' if lab_success else 'failure'} but final reward = {r_last}",
                     "outcome label and reward disagree", "label_vs_reward")
    else:
        O.unknown("no independent outcome label to compare the reward with")
    return {f: F[f].out() | ({"max_fk_error_m": F[f].stat} if hasattr(F[f], "stat") else {}) for f in FAMILIES}


def overall(fams: dict) -> str:
    vs = [v["verdict"] for f, v in fams.items()]
    if "REJECT" in vs:
        return "REJECT"
    if "REPAIR" in vs:
        return "REPAIR"
    return "PASS" if "PASS" in vs else "UNKNOWN"


def verify_real_dataset(path: Path) -> dict:
    t0 = time.perf_counter()
    ds = load_dataset(path)
    st = _dataset_stats(ds)
    seen = {}
    eps = []
    for i, em in enumerate(ds["episodes"]):
        t1 = time.perf_counter()
        fams = _check_episode(ds, i, st, seen)
        eps.append({"episode_index": em["episode_index"], "frames": em.get("length"), "verdict": overall(fams),
                    "families": fams, "ms": (time.perf_counter() - t1) * 1e3})
    n = len(eps)
    fam_table = {}
    for f in FAMILIES:
        vs = [e["families"][f]["verdict"] for e in eps]
        fam_table[f] = {v: round(100 * vs.count(v) / n, 1) for v in ("PASS", "REPAIR", "REJECT", "UNKNOWN")}
        fam_table[f]["advisory_episodes"] = sum(bool(e["families"][f]["advisories"]) for e in eps)
        reasons = {e["families"][f].get("reason") for e in eps if e["families"][f].get("reason")}
        if reasons:
            fam_table[f]["note"] = sorted(reasons)[0]
    return {"dataset": ds["name"], "real_mode": REAL_MODE_VERSION, "catalogue_hash": catalogue_hash(),
            "robot_type": ds["info"].get("robot_type"), "fps": ds["info"].get("fps"),
            "episodes": n, "frames": int(sum(e["frames"] or 0 for e in eps)),
            "verdicts": {v: sum(e["verdict"] == v for e in eps) for v in ("PASS", "REPAIR", "REJECT", "UNKNOWN")},
            "family_table": fam_table, "column_aliases": _column_aliases(ds),
            "dataset_stats": {"action_state_lag_frames": st.get("lag"), "lag_per_episode": st.get("lag_per_episode")},
            "episode_results": eps, "seconds": round(time.perf_counter() - t0, 3)}


def accepted_split(path: Path, result: dict) -> list[dict]:
    """PASS + REPAIR episodes (repairs applied) as JSON episodes for the passport content hash."""
    ds = load_dataset(path)
    out = []
    for er, em, df in zip(result["episode_results"], ds["episodes"], ds["frames"]):
        if er["verdict"] not in ("PASS", "REPAIR"):
            continue
        df = df.copy()
        repairs = [f["repair"] for fam in er["families"].values() for f in fam["findings"] if "repair" in f]
        task = ds["tasks"].get(int(df["task_index"].iloc[0]), "") if "task_index" in df else ""
        for r in repairs:
            if r.startswith("use alternate"):
                task = r.split("'", 1)[1].rstrip("'")
            elif r == "collapse whitespace":
                task = re.sub(r"\s+", " ", task).strip()
            elif r == "drop duplicated rows":
                cols = [c for c in df.columns if df[c].dtype == object]
                full = np.concatenate([_mat(df, c) for c in cols], axis=1)
                keep = np.r_[True, ~np.all(full[1:] == full[:-1], axis=1)]
                df = df[keep].reset_index(drop=True)
                df["frame_index"] = np.arange(len(df))
        frames = {c: (np.round(np.stack(df[c].to_numpy()).astype(float), 7).tolist() if df[c].dtype == object
                      else df[c].tolist()) for c in df.columns}
        out.append({"episode_id": f"{ds['name']}/episode_{em['episode_index']:06d}",
                    "meta": {"real": True, "synthetic": False, "robot_type": ds["info"]["robot_type"], "task": task,
                             "source_file_path": em.get("source_file_path"), "source_shard": em.get("source_shard"),
                             "ax_repairs": repairs},
                    "frames": frames})
    return out
