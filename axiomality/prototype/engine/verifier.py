"""AXIOMALITY verification engine (prototype).

verify_episode(ep) -> {"verdict": PASS | REPAIR | REJECT | UNKNOWN, "findings": [...], ...}

Pipeline
  0. inputs      provenance + required channels present, else UNKNOWN (R-PROV-01)
  1. repair      only correctable *recording* defects: rows written out of
                 timestamp order (re-sort) and joint angles logged in degrees.
                 A repair is kept only if the repaired episode then passes every
                 rule; outcome labels are never modified.
  2. kernel      type / quantity axioms (Z3), arm + kinematics, gripper/contact
                 (Z3 per contact event), permanence, support, spatial relations,
                 phase grammar (Z3 with unsat-core rule attribution), task outcome.
Each finding names the rule ID and the first violating frame.
"""
from __future__ import annotations

import copy
import time

import numpy as np

from kernel import axioms
from kernel.arm import Q_HI, Q_LO, QD_MAX, fk
from kernel.geometry import box_penetration, footprint_overlap
from kernel.rulebook import (ARM, CLASSES, CONTACT_PHASES, CONTACT_REQUIRED_PHASES, PHASES, PHYS, REQUIRED_META,
                             VOCAB, horizontal_dims)

ENGINE_VERSION = "ax-engine-0.1.0-prototype"
FRAME_KEYS = ("t", "tcp_pose", "gripper_cmd", "gripper_width", "joints", "object_poses", "phase")
P = PHYS


def _first(mask) -> int | None:
    idx = np.flatnonzero(mask)
    return int(idx[0]) if idx.size else None


def _permute_frames(ep: dict, order: np.ndarray) -> dict:
    out = copy.deepcopy(ep)
    fr = out["frames"]
    for k in FRAME_KEYS:
        if k == "object_poses":
            fr[k] = {o: [v[i] for i in order] for o, v in fr[k].items()}
        else:
            fr[k] = [fr[k][i] for i in order]
    return out


def _dt_bad(dt: np.ndarray, hz: float) -> np.ndarray:
    """Sampling intervals violating R-TIME-02. v2 profile: up to P['max_single_drops'] isolated
    single dropped frames (interval ~2/hz) are tolerated; physics checks use the true dt."""
    r = dt * hz
    bad = np.abs(r - 1) > P["dt_rel_tol"]
    m = P.get("max_single_drops", 0)
    if m:
        drop = np.abs(r - 2) <= P["dt_rel_tol"]
        if drop.sum() <= m:
            bad = bad & ~drop
    return bad


def _rollmed(x: np.ndarray, w: int) -> np.ndarray:
    """Centred rolling median along axis 0 (edge-padded); v2 noise-robust geometry."""
    if not w or w < 3 or len(x) < w:
        return x
    h = w // 2
    xp = np.concatenate([np.repeat(x[:1], h, 0), x, np.repeat(x[-1:], h, 0)])
    win = np.lib.stride_tricks.sliding_window_view(xp, w, axis=0)
    return np.median(win, axis=-1)


def _sg_acc(pos: np.ndarray, t: np.ndarray, w: int) -> np.ndarray:
    """Second derivative from local quadratic least-squares fits (Savitzky-Golay style, true
    timestamps, windows truncated at the ends). Returns (n-2, d) aligned like the
    finite-difference acc (acc[i] is at frame i+1). Vectorised normal equations."""
    n, d = pos.shape
    if n < 3:
        return np.zeros((0, d))
    h = w // 2
    tp = np.pad(np.asarray(t, float), h, constant_values=np.nan)
    pp = np.pad(np.asarray(pos, float), ((h, h), (0, 0)), constant_values=np.nan)
    Wt = np.lib.stride_tricks.sliding_window_view(tp, w)                 # (n, w)
    Wp = np.lib.stride_tricks.sliding_window_view(pp, w, axis=0)         # (n, d, w)
    m = ~np.isnan(Wt)
    tt = np.where(m, Wt - np.asarray(t, float)[:, None], 0.0)
    S = [np.sum(m * tt ** k, 1) for k in range(5)]
    A = np.stack([np.stack([S[4], S[3], S[2]], -1), np.stack([S[3], S[2], S[1]], -1),
                  np.stack([S[2], S[1], S[0]], -1)], 1)                   # (n, 3, 3)
    y = np.where(m[:, None, :], Wp, 0.0)
    B = np.stack([np.sum(y * tt[:, None, :] ** k, -1) for k in (2, 1, 0)], 1)  # (n, 3, d)
    coef = np.linalg.solve(A[1:-1], B[1:-1])
    return 2 * coef[:, 0, :]


class _Ctx:
    def __init__(self):
        self.findings, self.repairs = [], []

    def add(self, rule, frame, msg):
        self.findings.append({"rule": rule, "frame": None if frame is None else int(frame), "message": msg})


def _missing_inputs(ep: dict) -> list[str]:
    miss = [f"meta.{k}" for k in REQUIRED_META if ep.get("meta", {}).get(k) in (None, "")]
    fr = ep.get("frames") or {}
    miss += [f"frames.{k}" for k in FRAME_KEYS if not fr.get(k)]
    if not ep.get("scene", {}).get("objects"):
        miss.append("scene.objects")
    if ep.get("events") is None:
        miss.append("events")
    return miss


def _repair(ep: dict, ctx: _Ctx) -> dict | None:
    """Stage 1. Returns the (possibly repaired) episode, or None if unrecoverable."""
    t = np.asarray(ep["frames"]["t"], float)
    hz = float(ep["meta"]["hz"])
    if np.any(np.diff(t) <= 0):
        order = np.argsort(t, kind="stable")
        ts = t[order]
        dts = np.diff(ts)
        if np.all(dts > 0) and not np.any(_dt_bad(dts, hz)):
            moved = [int(i) for i in np.flatnonzero(order != np.arange(len(t)))]
            ep = _permute_frames(ep, order)
            ctx.repairs.append({"rule": "R-TIME-01", "frames": moved,
                                "action": f"re-sorted {len(moved)} rows written out of timestamp order"})
        else:
            k = _first(np.diff(t) <= 0) + 1
            ctx.add("R-TIME-01", k, f"Frame {k}: timestamp {t[k]:.4f}s <= previous {t[k - 1]:.4f}s and rows cannot be "
                                    "re-sorted into a regular time base")
            return None
    q = np.asarray(ep["frames"]["joints"], float)
    if np.nanmax(np.abs(q)) > 2 * np.pi + 0.5:
        qr = np.deg2rad(q)
        if np.all((qr >= Q_LO) & (qr <= Q_HI)):
            ep = copy.deepcopy(ep) if not ctx.repairs else ep
            ep["frames"]["joints"] = np.round(qr, 6).tolist()
            ctx.repairs.append({"rule": "R-JNT-01", "frames": "all", "action": "joint angles logged in degrees; converted to radians"})
    if ctx.repairs:
        ep["meta"]["ax_repairs"] = ctx.repairs
    return ep


def _runs_bool(mask) -> list[tuple[int, int]]:
    m = np.r_[False, np.asarray(mask, bool), False]
    d = np.diff(m.astype(int))
    return list(zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1)))


def verify_episode(ep: dict) -> dict:
    t_start = time.perf_counter()
    ctx = _Ctx()
    res = {"episode_id": ep.get("episode_id"), "engine": ENGINE_VERSION}
    miss = _missing_inputs(ep)
    if miss:
        res.update(verdict="UNKNOWN", findings=[{"rule": "R-PROV-01", "frame": None,
                                                 "message": "missing inputs: " + ", ".join(miss)}], repairs=[])
        res["reason"] = "R-PROV-01: cannot evaluate, missing " + ", ".join(miss)
        res["ms"] = (time.perf_counter() - t_start) * 1e3
        return res

    fr = ep["frames"]
    n = len(fr["t"])
    try:
        arrs = {k: np.asarray(fr[k], float) for k in ("t", "tcp_pose", "gripper_cmd", "gripper_width", "joints")}
        poses = {o: np.asarray(v, float) for o, v in fr["object_poses"].items()}
        shape_ok = all(len(a) == n for a in list(arrs.values()) + list(poses.values())) and len(fr["phase"]) == n \
            and all(p.shape == (n, 4) for p in poses.values()) and arrs["joints"].shape == (n, 7)
    except (ValueError, TypeError):
        shape_ok = False
    if not shape_ok:
        ctx.add("R-QTY-01", None, "per-frame channels have inconsistent lengths/shapes")
    elif not all(np.all(np.isfinite(a)) for a in list(arrs.values()) + list(poses.values())):
        ctx.add("R-QTY-01", None, "non-finite values (NaN/Inf) in recorded channels")
    else:
        ep2 = _repair(ep, ctx)
        if ep2 is not None:
            _kernel_checks(ep2, ctx)
            if ctx.repairs and not ctx.findings:
                res["repaired_episode"] = ep2
    verdict = "REJECT" if ctx.findings else ("REPAIR" if ctx.repairs else "PASS")
    ctx.findings.sort(key=lambda f: (f["frame"] if f["frame"] is not None else -1))
    res.update(verdict=verdict, findings=ctx.findings, repairs=ctx.repairs)
    f0 = ctx.findings[0] if ctx.findings else None
    res["reason"] = (f"{f0['message']}; rule {f0['rule']}" if f0 else
                     ("; ".join(r["action"] for r in ctx.repairs) if ctx.repairs else "all rules satisfied"))
    res["ms"] = (time.perf_counter() - t_start) * 1e3
    return res


def _kernel_checks(ep: dict, ctx: _Ctx) -> None:
    meta, fr, scene = ep["meta"], ep["frames"], ep["scene"]
    hz, table = float(meta["hz"]), float(scene.get("table_z", P["table_z"]))
    t = np.asarray(fr["t"], float)
    n, dt = len(t), np.diff(np.asarray(fr["t"], float))
    tcp = np.asarray(fr["tcp_pose"], float)[:, :3]
    cmd = np.asarray(fr["gripper_cmd"], int)
    width = np.asarray(fr["gripper_width"], float)
    q = np.asarray(fr["joints"], float)
    phase = list(fr["phase"])
    objs = {o["id"]: o for o in scene["objects"]}
    poses = {o: np.asarray(v, float) for o, v in fr["object_poses"].items()}
    manip = meta["manipulated_object"]
    success = meta["outcome"] == "success"
    add = ctx.add

    # --- time base
    k = _first(_dt_bad(dt, hz))
    if k is not None:
        add("R-TIME-02", k + 1, f"Frame {k + 1}: sampling interval {dt[k] * 1e3:.1f} ms vs nominal {1e3 / hz:.1f} ms")

    # --- type / quantity layer (Z3)
    labels = {}
    for oid, o in objs.items():
        lab = o.get("label")
        if lab not in VOCAB:
            add("R-TYPE-01", 0, f"{oid} label '{lab}' is not in the kernel vocabulary")
            continue
        labels[oid] = lab
        for rid in axioms.check_object(lab, o["dimensions"], manipulated=(oid == manip)):
            hx, hn, h = horizontal_dims(o["dimensions"])
            c = CLASSES[lab]
            detail = {"R-QTY-02": f"box {hx:.3f} x {hn:.3f} x {h:.3f} m is outside the '{lab}' range "
                                  f"({c['hmax'][0]}-{c['hmax'][1]} x {c['hmin'][0]}-{c['hmin'][1]} x "
                                  f"{c['height'][0]}-{c['height'][1]} m)",
                      "R-TYPE-02": f"a '{lab}' of width {hn:.3f} m is not parallel-graspable "
                                   f"(aperture {ARM['gripper_aperture']} m)",
                      "R-QTY-01": "non-positive or inconsistent dimensions"}.get(rid, rid)
            add(rid, 0, f"Scene: {oid} labelled '{lab}': {detail}")

    # --- arm
    bad = (q < Q_LO) | (q > Q_HI)
    k = _first(bad.any(1))
    if k is not None:
        j = int(np.flatnonzero(bad[k])[0])
        add("R-JNT-01", k, f"Frame {k}: joint {j + 1} = {q[k, j]:.3f} rad outside [{Q_LO[j]:.3f}, {Q_HI[j]:.3f}]")
    qd = np.abs(np.diff(q, axis=0)) / dt[:, None]
    qd_lim = QD_MAX * P.get("qd_margin", 1.0)  # v2: finite-difference noise margin (calibrated)
    k = _first((qd > qd_lim).any(1))
    if k is not None:
        j = int(np.argmax(qd[k] / qd_lim))
        add("R-JNT-02", k + 1, f"Frame {k + 1}: joint {j + 1} speed {qd[k, j]:.2f} rad/s > {qd_lim[j]:g} rad/s")
    fk_err = np.linalg.norm(fk(q)[:, :3, 3] - tcp, axis=1)
    k = _first(fk_err > P["fk_tol"])
    if k is not None:
        add("R-KIN-01", k, f"Frame {k}: recorded TCP differs from FK(joints) by {fk_err[k] * 1e3:.1f} mm")
    k = _first((width < 0) | (width > ARM["gripper_aperture"] + 1e-6))
    if k is not None:
        add("R-GRIP-02", k, f"Frame {k}: finger width {width[k]:.3f} m outside [0, {ARM['gripper_aperture']}]")

    # --- contact events -> attached intervals
    attached = {o: np.zeros(n, bool) for o in poses}
    open_at, event_frames = {}, []
    for ev in sorted(ep["events"], key=lambda e: e.get("t", -1)):
        o, et = ev.get("object"), float(ev.get("t", -1))
        k = int(np.searchsorted(t, et - 1e-9))
        snap = P.get("event_snap_s")
        if snap:  # v2: events snap to the nearest frame within half a period (dropped frames / jitter)
            k = int(np.argmin(np.abs(t - et)))
            if abs(t[k] - et) <= snap:
                et = t[k]
        if o not in poses or k >= n or abs(t[k] - et) > 1e-6 or ev.get("type") not in ("contact_begin", "contact_end"):
            add("R-CONT-03", min(k, n - 1), f"event {ev} does not reference a known object/frame/type")
            continue
        if ev["type"] == "contact_begin":
            if o in open_at:
                add("R-CONT-03", k, f"Frame {k}: second contact_begin on {o} without contact_end")
                continue
            open_at[o] = k
        else:
            if o not in open_at:
                add("R-CONT-03", k, f"Frame {k}: contact_end on {o} without contact_begin")
                continue
            attached[o][open_at.pop(o):k] = True
        event_frames.append((ev["type"], o, k))
    for o, b in open_at.items():
        attached[o][b:] = True

    # --- per-object physics
    airborne_all = {}
    sw = P.get("smooth_window", 0)
    geo = {o: (_rollmed(v, sw) if sw else v) for o, v in poses.items()}  # v2: geometry on rolling medians
    for oid, Pz in poses.items():
        Pg = geo[oid]
        dims = objs[oid]["dimensions"]
        d3 = (dims["length"], dims["width"], dims["height"])
        h = d3[2]
        lab = labels.get(oid)
        gap = Pg[:, 2] - h / 2 - table
        supported = gap <= P["support_tol"]
        for o2, P2 in geo.items():
            if o2 != oid:
                d2 = objs[o2]["dimensions"]
                top2 = P2[:, 2] + d2["height"] / 2
                on_top = (np.abs(Pg[:, 2] - h / 2 - top2) <= P["support_tol"]) & \
                    (footprint_overlap(Pg, d3, P2, (d2["length"], d2["width"])) > 0)
                supported |= on_top
        att = attached[oid]
        free = ~att
        airborne = free & ~supported
        airborne_all[oid] = airborne
        step = np.diff(Pz[:, :3], axis=0)
        disp = np.linalg.norm(step, axis=1)

        k = _first(gap < -P["pen_tol"])
        if k is not None:
            add("R-SPAT-01", k, f"Frame {k}: {oid} bottom {gap[k] * 1e3:.0f} mm below the table surface")
        k = _first(disp / dt > P["v_max"])
        if k is not None:
            add("R-PERM-01", k + 1, f"Frame {k + 1}: {oid} moved {disp[k]:.2f} m in {dt[k] * 1e3:.0f} ms "
                                    f"({disp[k] / dt[k]:.1f} m/s > v_max {P['v_max']} m/s)")
        # landing exemption: the frame pair right after a flight may still carry the impact motion
        just_landed = np.r_[False, airborne[:-2]]
        k = _first(free[:-1] & free[1:] & supported[:-1] & supported[1:] & ~just_landed & (disp > P["static_tol"]))
        if k is not None:
            add("R-PERM-02", k + 1, f"Frame {k + 1}: {oid} rests with no contact yet moved {disp[k] * 1e3:.0f} mm")
        dev = np.linalg.norm(step - np.diff(tcp, axis=0), axis=1)
        k = _first(att[:-1] & att[1:] & (dev > P["comove_tol"]))
        if k is not None:
            add("R-PERM-03", k + 1, f"Frame {k + 1}: attached {oid} deviates {dev[k] * 1e3:.0f} mm from the gripper motion")
        gw = min(dims["length"], dims["width"])
        k = _first(att & ((cmd != 1) | (np.abs(width - gw) > P["grip_width_tol"])))
        if k is not None:
            add("R-GRIP-01", k, f"Frame {k}: {oid} in contact but gripper cmd={'closed' if cmd[k] else 'open'}, "
                                f"width {width[k]:.3f} m vs object {gw:.3f} m")
        vel = step / dt[:, None]
        acc = np.diff(vel, axis=0) / ((dt[:-1] + dt[1:]) / 2)[:, None]  # acc[i] is at frame i+1
        if sw:
            acc = _sg_acc(Pz[:, :3], t, sw)
        if lab and CLASSES[lab]["fragile"]:
            m = att[:-2] & att[1:-1] & att[2:] & (np.linalg.norm(acc, axis=1) > P["a_fragile"])
            k = _first(m)
            if k is not None:
                add("R-TYPE-03", k + 1, f"Frame {k + 1}: fragile '{lab}' accelerated at "
                                        f"{np.linalg.norm(acc[k]):.1f} m/s^2 > {P['a_fragile']}")
        g = P["g"]
        lo, hi = P["ballistic_az"]
        az = acc[:, 2]
        m = airborne[:-2] & airborne[1:-1] & airborne[2:] & ((az > hi * g) | (az < lo * g))
        if sw:  # v2: one quadratic fit per airborne run (>= 4 frames) instead of 3-frame differences
            m = np.zeros(max(n - 2, 0), bool)
            for s0, e0 in _runs_bool(airborne):
                if e0 - s0 >= 4:
                    tt = t[s0:e0] - t[s0]
                    a_fit = 2 * np.polyfit(tt, Pz[s0:e0, 2], 2)[0]
                    if a_fit > hi * g or a_fit < lo * g:
                        m[max(s0 - 1, 0)] = True
                        az = az.copy()
                        az[max(s0 - 1, 0)] = a_fit
        k = _first(m)
        if k is not None:
            add("R-SUP-01", k + 1, f"Frame {k + 1}: {oid} unsupported ({gap[k + 1] * 1e3:.0f} mm above support, no "
                                   f"contact) but vertical accel {az[k]:.1f} m/s^2 is not free fall")
        # flight-time bound on each airborne run
        k = 0
        while k < n:
            if not airborne[k]:
                k += 1
                continue
            j = k
            while j + 1 < n and airborne[j + 1]:
                j += 1
            ref = k - 1 if k > 0 else k
            u = max((Pz[k, 2] - Pz[k - 1, 2]) / dt[k - 1], 0.0) if k > 0 else 0.0
            t_max = (u + np.sqrt(u * u + 2 * g * max(gap[ref], 0.0))) / g + P["flight_slack_frames"] / hz
            over = np.flatnonzero(t[k:j + 1] - t[ref] > t_max)
            if over.size:
                f = k + int(over[0])
                add("R-SUP-02", f, f"Frame {f}: {oid} airborne for {t[f] - t[ref]:.2f} s from "
                                   f"{max(gap[ref], 0) * 1e3:.0f} mm; free fall would land within {t_max:.2f} s")
            k = j + 1

    # --- rigid-box interpenetration
    ids = list(poses)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            if not (labels.get(a) and labels.get(b) and CLASSES[labels[a]]["rigid"] and CLASSES[labels[b]]["rigid"]):
                continue
            da, db = objs[a]["dimensions"], objs[b]["dimensions"]
            depth = box_penetration(geo[a], (da["length"], da["width"], da["height"]),
                                    geo[b], (db["length"], db["width"], db["height"]))
            k = _first(depth > P["pen_tol"])
            if k is not None:
                add("R-SPAT-02", k, f"Frame {k}: rigid {a} ('{labels[a]}') and {b} ('{labels[b]}') interpenetrate "
                                    f"by {depth[k] * 1e3:.0f} mm")

    # --- contact events (Z3 per event)
    for kind, o, k in event_frames:
        dist = float(np.linalg.norm(tcp[k] - poses[o][k, :3]))
        for rid in axioms.check_contact_event(kind, closed=bool(cmd[k] == 1), dist=dist, opened=bool(cmd[k] == 0),
                                              free_after=bool(airborne_all[o][k])):
            msg = (f"Frame {k}: contact_begin on {o} with gripper {'closed' if cmd[k] else 'open'} and TCP "
                   f"{dist * 1e3:.0f} mm from object (reach {P['reach'] * 1e3:.0f} mm)" if kind == "contact_begin" else
                   f"Frame {k}: contact_end on {o} while gripper stays closed and object is not in free flight")
            add(rid, k, msg)

    # --- phase grammar (Z3) + phase/contact coupling
    unknown = [i for i, p in enumerate(phase) if p not in PHASES]
    if unknown:
        add("R-PHASE-01", unknown[0], f"Frame {unknown[0]}: unknown phase label '{phase[unknown[0]]}'")
    else:
        segs = [0] + [i for i in range(1, n) if phase[i] != phase[i - 1]]
        labels_seq = [phase[s] for s in segs]
        for rid, si in axioms.check_phases(labels_seq, success):
            add(rid, segs[si], f"Frame {segs[si]}: phase sequence {' > '.join(labels_seq)} (outcome "
                               f"{meta['outcome']}) violates the task grammar at segment '{labels_seq[si]}'")
        ph = np.array(phase)
        any_att = np.any(np.stack(list(attached.values())), axis=0)
        k = _first(any_att & ~np.isin(ph, CONTACT_PHASES))
        if k is not None:
            add("R-PHASE-05", k, f"Frame {k}: object in contact during phase '{ph[k]}'")
        if manip in attached:
            k = _first(np.isin(ph, CONTACT_REQUIRED_PHASES) & ~attached[manip])
            if k is not None:
                add("R-PHASE-05", k, f"Frame {k}: phase '{ph[k]}' but {manip} is not held")

    # --- task outcome
    if success and manip in poses:
        c, r = np.array(meta["target_region"]["center"]), float(meta["target_region"]["radius"])
        d = float(np.linalg.norm(poses[manip][-1, :2] - c))
        if attached[manip][-1] or airborne_all[manip][-1] or d > r:
            add("R-TASK-01", n - 1, f"Frame {n - 1}: outcome 'success' but {manip} ends {d * 1e3:.0f} mm from target "
                                    f"centre (radius {r * 1e3:.0f} mm), held={bool(attached[manip][-1])}")


def verify_dataset(episodes: list[dict]) -> list[dict]:
    return [verify_episode(e) for e in episodes]
