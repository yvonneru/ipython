"""SYNTHETIC pick-and-place episode generator seeded from sample 109.

Every episode is SYNTHETIC. The scene geometry (mug + laptop boxes, poses,
dimensions) is taken verbatim from AXIOMALITY sample 109 (pointclouds/109.ply)
and perturbed by small, seeded measurement noise. A declared 7-DoF arm picks the
mug from the table and places it in a target region; joint trajectories are
min-jerk interpolations between IK waypoints, and the TCP pose is the forward
kinematics of the recorded joints. With ``slip=True`` the mug physically slips
out of the gripper during transport and falls ballistically onto the table (a
*valid failure*: physically consistent, labelled failure_slip).
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kernel.arm import Q_READY, fk, ik, rot_to_quat, tcp_yaw, topdown_rotation  # noqa: E402
from kernel.rulebook import ARM, PHYS  # noqa: E402
from util import CLEAN_FILE, ROOT, canonical_json, sha256_hex, write_jsonl  # noqa: E402

SEED = 109
N_EPISODES = 200
HZ = 30.0
TARGET_CENTER, TARGET_RADIUS = (-0.10, 0.38), 0.05
HOME = (-0.35, 0.20, 0.38)
GRASP_ABOVE = 0.02      # TCP sits 2 cm above the mug centroid when grasping
FINGER_SPEED = 0.10     # m/s
OPEN_W = ARM["gripper_aperture"]
ROBOTS = ("AX-SIM-ARM7-01", "AX-SIM-ARM7-02", "AX-SIM-ARM7-03")
GENERATOR = "axiomality-prototype/data/generate.py v0.1"
SEED_FILE = ROOT / "data" / "seed_sample_109.json"


def load_seed() -> dict:
    return json.loads(SEED_FILE.read_text())


def calibration_hash(robot_id: str) -> str:
    return "sha256:" + sha256_hex(canonical_json({"robot": robot_id, "arm": ARM}))


def _mj(tau):
    tau = np.clip(tau, 0.0, 1.0)
    return 10 * tau**3 - 15 * tau**4 + 6 * tau**5


def _mj_d(tau):
    tau = np.clip(tau, 0.0, 1.0)
    return 30 * tau**2 - 60 * tau**3 + 30 * tau**4


def _wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def simulate_episode(idx: int, slip: bool = False) -> dict:
    rng = np.random.default_rng([SEED, idx])
    seed = load_seed()
    mug_s, lap_s = seed["objects"]

    # ---- scene: sample 109 + seeded measurement noise
    def noisy_dims(d):
        return {k: round(v * (1 + rng.uniform(-0.02, 0.02)), 6) for k, v in d.items()}
    mug_d, lap_d = noisy_dims(mug_s["dimensions"]), noisy_dims(lap_s["dimensions"])
    mug_p = np.array([mug_s["centroid"]["x"] + rng.uniform(-0.04, 0.04), mug_s["centroid"]["y"] + rng.uniform(-0.04, 0.04),
                      mug_s["centroid"]["z"] + (mug_d["height"] - mug_s["dimensions"]["height"]) / 2,
                      mug_s["rotations"]["z"] + rng.uniform(-0.35, 0.35)])
    lap_p = np.array([lap_s["centroid"]["x"] + rng.uniform(-0.01, 0.01), lap_s["centroid"]["y"] + rng.uniform(-0.01, 0.01),
                      lap_s["centroid"]["z"] + (lap_d["height"] - lap_s["dimensions"]["height"]) / 2,
                      lap_s["rotations"]["z"] + rng.uniform(-0.03, 0.03)])
    gw = min(mug_d["length"], mug_d["width"])  # grasp across the narrower side
    place_xy = np.array(TARGET_CENTER) + rng.uniform(-0.02, 0.02, 2)
    grasp_z = mug_p[2] + GRASP_ABOVE
    place_z = mug_d["height"] / 2 + GRASP_ABOVE + rng.uniform(-0.002, 0.004)
    lift = rng.uniform(0.12, 0.20)
    yaw_g = float(_wrap(mug_p[3] + np.pi))

    # ---- IK waypoints
    wps = {"home": HOME, "pre": (*mug_p[:2], grasp_z + 0.12), "grasp": (*mug_p[:2], grasp_z),
           "lift": (*mug_p[:2], grasp_z + lift), "preplace": (*place_xy, place_z + lift),
           "place": (*place_xy, place_z), "retreat": (*place_xy, place_z + 0.10)}
    Rg, q, Q = topdown_rotation(yaw_g), Q_READY, {}
    for name, p in wps.items():
        q, err = ik(np.array(p), Rg, q)
        if err > 1e-3:
            raise RuntimeError(f"IK failed for episode {idx} waypoint {name}: {err:.2e}")
        Q[name] = q

    # ---- timeline (phase, q_from, q_to, duration)
    U = rng.uniform
    segs = [("approach", "home", "pre", U(1.0, 1.4)), ("approach", "pre", "grasp", U(0.5, 0.7)),
            ("grasp", "grasp", "grasp", U(0.45, 0.6)), ("transport", "grasp", "lift", U(0.5, 0.7)),
            ("transport", "lift", "preplace", U(1.1, 1.5)), ("place", "preplace", "place", U(0.5, 0.7)),
            ("release", "place", "place", U(0.3, 0.4)), ("release", "place", "retreat", U(0.4, 0.6))]
    starts = np.cumsum([0.0] + [s[3] for s in segs])
    t_close, t_open = starts[2] + 0.1, starts[6]
    t_slip = starts[4] + U(0.2, 0.5) * segs[4][3] if slip else np.inf
    T_end = t_slip + U(1.0, 1.4) if slip else starts[-1]
    n = int(np.floor(T_end * HZ)) + 1
    t = np.arange(n) / HZ + np.r_[0.0, rng.uniform(-0.001, 0.001, n - 1)]
    t = t[t <= T_end]
    n = len(t)

    def plan(tt):
        qq, qd, ph = np.zeros((len(tt), 7)), np.zeros((len(tt), 7)), np.empty(len(tt), dtype=object)
        for i, (phase, a, b, dur) in enumerate(segs):
            m = (tt >= starts[i]) & ((tt < starts[i + 1]) | (i == len(segs) - 1))
            tau = (tt[m] - starts[i]) / dur
            qq[m] = Q[a] + np.outer(_mj(tau), Q[b] - Q[a])
            qd[m] = np.outer(_mj_d(tau), Q[b] - Q[a]) / dur
            ph[m] = phase
        return qq, qd, ph

    qs, _, phase = plan(t)
    if slip:  # robot does not react instantly: joint velocity decays exponentially
        s = int(np.argmax(t >= t_slip))
        q_s, qd_s = (x[0] for x in plan(np.array([t_slip]))[:2])
        tau_d = 0.12
        dt_after = t[s:] - t_slip
        qs[s:] = q_s + np.outer(1 - np.exp(-dt_after / tau_d), qd_s * tau_d)
        phase[s:] = "abort"
    T = fk(qs)
    tcp = T[:, :3, 3]

    # ---- gripper
    cmd = ((t >= t_close) & (t < t_open)).astype(int)
    width = np.where(t < t_close, OPEN_W, np.maximum(gw, OPEN_W - FINGER_SPEED * (t - t_close)))
    width = np.where(t >= t_open, np.minimum(OPEN_W, gw + FINGER_SPEED * (t - t_open)), width)
    b = int(np.argmax(t >= t_close + (OPEN_W - gw) / FINGER_SPEED))
    e = int(np.argmax(t >= t_slip)) if slip else int(np.argmax(t >= t_open))
    if slip:
        width[e:] = np.maximum(0.0, gw - FINGER_SPEED * (t[e:] - t_slip))

    # ---- object poses
    mug = np.tile(mug_p, (n, 1))
    rel = np.linalg.inv(T[b]) @ np.r_[mug_p[:3], 1.0]
    yaw_t = tcp_yaw(T)
    for k in range(b, e):
        mug[k, :3] = (T[k] @ rel)[:3]
        mug[k, 3] = _wrap(mug_p[3] + yaw_t[k] - yaw_t[b])
    if slip:
        p0, v = mug[e - 1, :3], (mug[e - 1, :3] - mug[e - 2, :3]) / (t[e - 1] - t[e - 2])
        zb0, g = p0[2] - mug_d["height"] / 2, PHYS["g"]
        t_land = (v[2] + np.sqrt(v[2] ** 2 + 2 * g * zb0)) / g
        for k in range(e, n):
            tau = min(t[k] - t[e - 1], t_land)
            mug[k, :2] = p0[:2] + v[:2] * tau
            mug[k, 2] = p0[2] + v[2] * tau - 0.5 * g * tau**2
            mug[k, 3] = mug[e - 1, 3]
    else:
        mug[e:] = mug[e - 1]
    lap = np.tile(lap_p, (n, 1))

    robot = ROBOTS[idx % len(ROBOTS)]
    r6 = lambda a: np.round(np.asarray(a, dtype=float), 6).tolist()  # noqa: E731
    return {
        "episode_id": f"ep_{idx:04d}",
        "schema": "ax-episode/0.1",
        "meta": {
            "synthetic": True, "real": False,
            "provenance": "SYNTHETIC - generated from sample 109 geometry (pointclouds/109.ply); not recorded on hardware",
            "derived_from": {"folder": seed["folder"], "filename": seed["filename"]},
            "generator": GENERATOR, "rng_seed": [SEED, idx],
            "robot_id": robot, "arm_model": ARM["name"], "calibration_hash": calibration_hash(robot),
            "consent_id": f"SYN-NO-HUMAN-SUBJECT-{idx:04d}", "hz": HZ, "task": "pick_and_place",
            "manipulated_object": "obj0",
            "target_region": {"center": list(TARGET_CENTER), "radius": TARGET_RADIUS},
            "outcome": "failure_slip" if slip else "success",
        },
        "scene": {"table_z": PHYS["table_z"], "objects": [
            {"id": "obj0", "label": mug_s["name"], "dimensions": mug_d},
            {"id": "obj1", "label": lap_s["name"], "dimensions": lap_d}]},
        "frames": {
            "t": r6(t),
            "tcp_pose": r6(np.c_[tcp, rot_to_quat(T[:, :3, :3])]),
            "gripper_cmd": cmd.tolist(),
            "gripper_width": r6(width),
            "joints": r6(qs),
            "object_poses": {"obj0": r6(mug), "obj1": r6(lap)},
            "phase": phase.tolist(),
        },
        "events": [{"t": round(float(t[b]), 6), "type": "contact_begin", "object": "obj0"},
                   {"t": round(float(t[e]), 6), "type": "contact_end", "object": "obj0"}],
    }


def main() -> list[dict]:
    t0 = time.perf_counter()
    eps = [simulate_episode(i) for i in range(N_EPISODES)]
    write_jsonl(CLEAN_FILE, eps)
    frames = sum(len(e["frames"]["t"]) for e in eps)
    print(f"[data] {len(eps)} SYNTHETIC episodes, {frames} frames @ {HZ:.0f} Hz -> {CLEAN_FILE.relative_to(ROOT)} "
          f"({time.perf_counter() - t0:.1f}s)")
    return eps


if __name__ == "__main__":
    main()
