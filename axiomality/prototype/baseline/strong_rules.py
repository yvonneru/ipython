"""STRONG rules baseline: what a good engineer writes in about a week.

Hand-coded Python checks with fixed (calibrated) tolerances. There is no formal
rulebook, no consistency checking, no cross-rule reasoning, no repair and no UNKNOWN:
every problem is REJECT, and missing inputs are REJECT too. On top of the structural
baseline (baseline/rules_only.py: schema, NaN/Inf, monotonic time, frame drops,
joint position/speed limits, gripper range and binary command, TCP/object speed
spikes vs v_max, label vocabularies, dangling events) it adds:

  S-PHASE    hand-coded phase order: approach > grasp > transport > place > release
             (success, all five, one contiguous block each) or approach > grasp >
             [transport] > abort (failure)
  S-EVENTS   contact events pair up begin/end on the manipulated object
  S-GRIP     gripper commanded closed and fingers not fully open while in contact
  S-SPEED    max object speed (v_max) and resting objects stay put when not held
  S-SUPPORT  table-support check with a fixed tolerance: every object not held is
             within +-support_tol of the table top (or of the top of an object it
             overlaps), except for a grace window after release (falls)
  S-SIZE     object dimensions inside the class size range of its label
  S-COMOVE   a held object keeps its distance to the TCP
  S-OVERLAP  object-object overlap of yaw-aware axis-aligned boxes
  S-OUTCOME  outcome=success -> manipulated object ends released inside the target

Not included (the things the engine does differently): forward-kinematics check,
TCP reach at contact begin, finger width vs object width, free-fall physics (a grace
window is used instead), fragile-object acceleration, phase/contact coupling
("transport requires contact"), graspability of the class, oriented-box SAT
penetration, UNKNOWN on missing inputs, repairs, Z3 rule attribution.
"""
from __future__ import annotations

import time

import numpy as np

from baseline.rules_only import check_episode as structural
from kernel.rulebook import ARM, CLASSES, PHYS

ORDER_SUCCESS = ["approach", "grasp", "transport", "place", "release"]
DEFAULT_TOL = {"static_tol": 0.005, "support_tol": 0.015, "comove_tol": 0.010, "pen_tol": 0.010,
               "grip_open_tol": 0.005, "grace_s": 0.5, "qd_margin": 1.0, "max_single_drops": 2,
               "target_slack": 0.0}
KNOB_OF = {"S-SPEED-static": "static_tol", "S-SUPPORT": "support_tol", "S-COMOVE": "comove_tol",
           "S-OVERLAP": "pen_tol", "S-GRIP-open": "grip_open_tol", "S-STRUCT-jointspeed": "qd_margin",
           "S-OUTCOME": "target_slack"}


def _extent(p, d):
    """Half extents in x, y of a yaw-rotated box (per frame)."""
    c, s = np.abs(np.cos(p[:, 3])), np.abs(np.sin(p[:, 3]))
    return np.stack([c * d[0] / 2 + s * d[1] / 2, s * d[0] / 2 + c * d[1] / 2], 1)


def check_episode(ep: dict, tol: dict | None = None) -> dict:
    t0 = time.perf_counter()
    T = dict(DEFAULT_TOL, **(tol or {}))
    base = structural(ep, policy={"max_single_drops": T["max_single_drops"], "qd_margin": T["qd_margin"]})
    issues = [("S-STRUCT-jointspeed" if "joint speed" in i else "S-STRUCT", i) for i in base["issues"]]
    if any(i.startswith("missing") or "mismatch" in i for i in base["issues"]):
        return {"episode_id": ep.get("episode_id"), "verdict": "REJECT", "issues": issues,
                "ms": (time.perf_counter() - t0) * 1e3}
    meta, fr, scene = ep["meta"], ep["frames"], ep["scene"]
    t = np.asarray(fr["t"], float)
    order = np.argsort(t, kind="stable")  # the checks below need a time-ordered view
    t = t[order]
    n, hz = len(t), float(meta["hz"])
    dt = np.maximum(np.diff(t), 1e-6)
    tcp = np.asarray(fr["tcp_pose"], float)[order, :3]
    cmd = np.asarray(fr["gripper_cmd"], float)[order]
    width = np.asarray(fr["gripper_width"], float)[order]
    phase = [fr["phase"][i] for i in order]
    poses = {o: np.asarray(v, float)[order] for o, v in fr["object_poses"].items()}
    objs = {o["id"]: o for o in scene["objects"]}
    manip = meta.get("manipulated_object")
    table = float(scene.get("table_z", 0.0))

    # S-PHASE
    segs = [phase[0]] + [phase[i] for i in range(1, n) if phase[i] != phase[i - 1]]
    success = meta.get("outcome") == "success"
    ok = segs == ORDER_SUCCESS if success else (
        len(segs) >= 3 and segs[0] == "approach" and segs[1] == "grasp" and segs[-1] == "abort"
        and segs[2:-1] in ([], ["transport"]))
    if not ok:
        issues.append(("S-PHASE", f"illegal phase sequence {' > '.join(segs)} for outcome {meta.get('outcome')}"))

    # S-EVENTS -> held interval of each object
    held = {o: np.zeros(n, bool) for o in poses}
    open_at = {}
    for ev in sorted(ep.get("events", []), key=lambda e: e.get("t", -1)):
        o = ev.get("object")
        k = int(np.argmin(np.abs(t - ev.get("t", -1))))
        if o not in poses or abs(t[k] - ev.get("t", -1)) > 0.5 / hz:
            issues.append(("S-EVENTS", f"event {ev} does not match a frame"))
            continue
        if ev["type"] == "contact_begin":
            if o in open_at:
                issues.append(("S-EVENTS", f"double contact_begin on {o}"))
            open_at[o] = k
        elif ev["type"] == "contact_end":
            if o not in open_at:
                issues.append(("S-EVENTS", f"contact_end on {o} without begin"))
                continue
            held[o][open_at.pop(o):k] = True
    for o, b in open_at.items():
        held[o][b:] = True

    # S-GRIP: closed while in contact
    for o, h in held.items():
        bad = h & ((cmd != 1) | (width > ARM["gripper_aperture"] - T["grip_open_tol"]))
        if bad.any():
            k = int(np.argmax(bad))
            issues.append(("S-GRIP-open", f"frame {k}: {o} held but gripper open (cmd {cmd[k]:.0f}, width {width[k]:.3f})"))

    # S-SIZE
    for oid, o in objs.items():
        c = CLASSES.get(o.get("label"))
        if c is None:
            continue
        d = o["dimensions"]
        hx, hn, hh = max(d["length"], d["width"]), min(d["length"], d["width"]), d["height"]
        if not (c["hmax"][0] <= hx <= c["hmax"][1] and c["hmin"][0] <= hn <= c["hmin"][1]
                and c["height"][0] <= hh <= c["height"][1]):
            issues.append(("S-SIZE", f"{oid} '{o['label']}' size {hx:.3f}x{hn:.3f}x{hh:.3f} outside class range"))

    # per-object motion / support
    release_end = {}
    for o, h in held.items():
        ends = np.flatnonzero(h[:-1] & ~h[1:])
        release_end[o] = [int(e) + 1 for e in ends]
    ext = {o: _extent(p, (objs[o]["dimensions"]["length"], objs[o]["dimensions"]["width"])) for o, p in poses.items()}
    for o, p in poses.items():
        dims = objs[o]["dimensions"]
        h = held[o]
        disp = np.linalg.norm(np.diff(p[:, :3], axis=0), axis=1)
        if np.any(disp / dt > PHYS["v_max"]):
            k = int(np.argmax(disp / dt > PHYS["v_max"])) + 1
            issues.append(("S-SPEED", f"frame {k}: {o} faster than v_max"))
        grace = np.zeros(n, bool)
        for e in release_end[o]:
            grace[e:e + int(np.ceil(T["grace_s"] * hz))] = True
        gap = p[:, 2] - dims["height"] / 2 - table
        on_other = np.zeros(n, bool)
        for o2, p2 in poses.items():
            if o2 == o:
                continue
            top2 = p2[:, 2] + objs[o2]["dimensions"]["height"] / 2
            ov = np.all(np.abs(p[:, :2] - p2[:, :2]) < ext[o] + ext[o2], axis=1)
            on_other |= ov & (np.abs(p[:, 2] - dims["height"] / 2 - top2) <= T["support_tol"])
        unsupported = ~h & ~grace & ~on_other & (np.abs(gap) > T["support_tol"])
        if unsupported.any():
            k = int(np.argmax(unsupported))
            issues.append(("S-SUPPORT", f"frame {k}: {o} not held and {gap[k] * 1e3:.0f} mm from the table top"))
        resting = ~h[:-1] & ~h[1:] & ~grace[:-1] & ~grace[1:]
        if np.any(resting & (disp > T["static_tol"])):
            k = int(np.argmax(resting & (disp > T["static_tol"]))) + 1
            issues.append(("S-SPEED-static", f"frame {k}: resting {o} moved {disp[k - 1] * 1e3:.0f} mm"))
        if h.any():
            b = int(np.argmax(h))
            d0 = np.linalg.norm(tcp[b] - p[b, :3])
            dd = np.abs(np.linalg.norm(tcp - p[:, :3], axis=1) - d0)
            if np.any(h & (dd > T["comove_tol"])):
                k = int(np.argmax(h & (dd > T["comove_tol"])))
                issues.append(("S-COMOVE", f"frame {k}: held {o} distance to TCP changed by {dd[k] * 1e3:.0f} mm"))

    # S-OVERLAP (yaw-aware AABB)
    ids = list(poses)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = ids[i], ids[j]
            pa, pb = poses[a], poses[b]
            ha, hb = objs[a]["dimensions"]["height"] / 2, objs[b]["dimensions"]["height"] / 2
            ox = np.min(ext[a] + ext[b] - np.abs(pa[:, :2] - pb[:, :2]), axis=1)
            oz = np.minimum(pa[:, 2] + ha, pb[:, 2] + hb) - np.maximum(pa[:, 2] - ha, pb[:, 2] - hb)
            depth = np.minimum(ox, oz)
            if np.any(depth > T["pen_tol"]):
                k = int(np.argmax(depth > T["pen_tol"]))
                issues.append(("S-OVERLAP", f"frame {k}: {a} and {b} overlap by {depth[k] * 1e3:.0f} mm"))

    # S-OUTCOME
    if success and manip in poses:
        c, r = np.array(meta["target_region"]["center"]), float(meta["target_region"]["radius"])
        d = float(np.linalg.norm(poses[manip][-1, :2] - c))
        if held[manip][-1] or d > r + T["target_slack"]:
            issues.append(("S-OUTCOME", f"success but {manip} ends {d * 1e3:.0f} mm from target, held={held[manip][-1]}"))
    return {"episode_id": ep.get("episode_id"), "verdict": "REJECT" if issues else "PASS",
            "issues": [f"{c}: {m}" for c, m in issues], "codes": sorted({c for c, _ in issues}),
            "ms": (time.perf_counter() - t0) * 1e3}
