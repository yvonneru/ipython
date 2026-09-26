"""SYNTHETIC benchmark v2: noisy recordings, three task variants, a third object.

Everything here is SYNTHETIC. Scene geometry of the mug and laptop comes from
AXIOMALITY sample 109 as in v1; v2 adds an apple (class ``fruit``, 0.075-0.085 m)
and three task variants:

  V1 mug_to_target        pick the mug (sample-109 position), place in target region A (v1 task)
  V2 mug_next_to_laptop   pick the mug, place it in a region right next to the laptop
  V3 fruit_from_B         pick the apple from a different start region B, place in region A

The ground-truth motion is simulated as in v1 (IK waypoints, min-jerk joint
trajectories, rigid carry, ballistic slip). A sensor model (kernel/profiles.SENSOR_MODEL)
is then applied to the *recording*:
  * joint encoders: Gaussian noise, sigma ~ U(0.2, 0.5) deg per episode
  * TCP pose: recomputed as FK(noisy joints) (what a real arm logs)
  * object poses: 3 mm per-axis position noise, 0.01 rad yaw noise (vision/mocap tracker)
  * gripper width: 0.5 mm noise
  * timestamps: uniform +-5 ms jitter on every row
  * with probability 0.3 one interior frame is dropped (all channels)
Contact events keep their original (noisy) frame timestamps; if that frame was dropped
the event time no longer matches a row.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from data.generate import (FINGER_SPEED, GRASP_ABOVE, HOME, HZ, OPEN_W, ROBOTS, _mj, _mj_d, _wrap,  # noqa: E402
                           calibration_hash, load_seed)
from kernel.arm import Q_READY, fk, ik, rot_to_quat, tcp_yaw, topdown_rotation  # noqa: E402
from kernel.profiles import SENSOR_MODEL  # noqa: E402
from kernel.rulebook import ARM, PHYS  # noqa: E402
from util import ROOT, write_jsonl  # noqa: E402

SEED_V2 = 2109
CAL_SEED = 7109             # calibration split (disjoint seeds) used only to set tolerances
GENERATOR_V2 = "axiomality-prototype/data/generate_v2.py v0.2"
DATA_V2 = ROOT / "data" / "generated_v2"
CLEAN_V2 = DATA_V2 / "clean_noisy_episodes.jsonl"
CAL_V2 = DATA_V2 / "calibration_noisy_episodes.jsonl"
N_BENCH = 300
N_CAL = 120

TARGET_A = ((-0.10, 0.38), 0.05)
TARGET_NEXT_TO_LAPTOP = ((-0.09, -0.12), 0.04)
REGION_B = (-0.40, 0.42)
VARIANTS = ("mug_to_target", "mug_next_to_laptop", "fruit_from_B")
FRUIT_DIMS = (0.075, 0.085)


def simulate_v2(idx: int, variant: str, slip: bool = False, seed: int = SEED_V2) -> dict:
    """Noise-free ground-truth episode (before the sensor model)."""
    rng = np.random.default_rng([seed, idx, VARIANTS.index(variant)])
    sd = load_seed()
    mug_s, lap_s = sd["objects"]

    def noisy_dims(d):
        return {k: round(v * (1 + rng.uniform(-0.02, 0.02)), 6) for k, v in d.items()}
    mug_d, lap_d = noisy_dims(mug_s["dimensions"]), noisy_dims(lap_s["dimensions"])
    fd = rng.uniform(*FRUIT_DIMS)
    fruit_d = {"length": round(fd * rng.uniform(0.97, 1.03), 6), "width": round(fd * rng.uniform(0.97, 1.03), 6),
               "height": round(fd * rng.uniform(0.92, 1.0), 6)}
    mug_p = np.array([mug_s["centroid"]["x"] + rng.uniform(-0.04, 0.04), mug_s["centroid"]["y"] + rng.uniform(-0.04, 0.04),
                      mug_s["centroid"]["z"] + (mug_d["height"] - mug_s["dimensions"]["height"]) / 2,
                      mug_s["rotations"]["z"] + rng.uniform(-0.35, 0.35)])
    lap_p = np.array([lap_s["centroid"]["x"] + rng.uniform(-0.01, 0.01), lap_s["centroid"]["y"] + rng.uniform(-0.01, 0.01),
                      lap_s["centroid"]["z"] + (lap_d["height"] - lap_s["dimensions"]["height"]) / 2,
                      lap_s["rotations"]["z"] + rng.uniform(-0.03, 0.03)])
    fruit_p = np.array([REGION_B[0] + rng.uniform(-0.03, 0.03), REGION_B[1] + rng.uniform(-0.03, 0.03),
                        fruit_d["height"] / 2 + rng.uniform(-0.002, 0.002), -np.pi / 2 + rng.uniform(-0.35, 0.35)])

    if variant == "fruit_from_B":
        man_lab, man_d, man_p = "fruit", fruit_d, fruit_p
        others = [("mug", mug_d, mug_p), ("laptop", lap_d, lap_p)]
        (tc, tr) = TARGET_A
    else:
        man_lab, man_d, man_p = "mug", mug_d, mug_p
        others = [("laptop", lap_d, lap_p), ("fruit", fruit_d, fruit_p)]
        (tc, tr) = TARGET_A if variant == "mug_to_target" else TARGET_NEXT_TO_LAPTOP
    gw = min(man_d["length"], man_d["width"])
    place_xy = np.array(tc) + rng.uniform(-0.015, 0.015, 2)
    grasp_z = man_p[2] + GRASP_ABOVE
    place_z = man_d["height"] / 2 + GRASP_ABOVE + rng.uniform(-0.002, 0.004)
    lift = rng.uniform(0.14, 0.20)
    yaw_g = float(_wrap(man_p[3] + np.pi))

    wps = {"home": HOME, "pre": (*man_p[:2], grasp_z + 0.12), "grasp": (*man_p[:2], grasp_z),
           "lift": (*man_p[:2], grasp_z + lift), "preplace": (*place_xy, place_z + lift),
           "place": (*place_xy, place_z), "retreat": (*place_xy, place_z + 0.10)}
    Rg, q, Q = topdown_rotation(yaw_g), Q_READY, {}
    for name, p in wps.items():
        q, err = ik(np.array(p), Rg, q)
        if err > 1e-3:
            raise RuntimeError(f"IK failed for v2 episode {idx} ({variant}) waypoint {name}: {err:.2e}")
        Q[name] = q

    U = rng.uniform
    close_time = 0.1 + (OPEN_W - gw) / FINGER_SPEED  # the fingers must reach the object before transport
    slow = 1.3 if variant == "mug_next_to_laptop" else 1.0  # longer path: keep joint speeds inside limits
    segs = [("approach", "home", "pre", U(1.0, 1.4)), ("approach", "pre", "grasp", U(0.5, 0.7)),
            ("grasp", "grasp", "grasp", max(U(0.45, 0.6), close_time + U(0.08, 0.15))),
            ("transport", "grasp", "lift", U(0.5, 0.7)),
            ("transport", "lift", "preplace", slow * U(1.1, 1.5)), ("place", "preplace", "place", U(0.5, 0.7)),
            ("release", "place", "place", U(0.3, 0.4)), ("release", "place", "retreat", U(0.4, 0.6))]
    starts = np.cumsum([0.0] + [s[3] for s in segs])
    t_close, t_open = starts[2] + 0.1, starts[6]
    t_slip = starts[4] + U(0.2, 0.5) * segs[4][3] if slip else np.inf
    T_end = t_slip + U(1.0, 1.4) if slip else starts[-1]
    n = int(np.floor(T_end * HZ)) + 1
    t = np.arange(n) / HZ
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
    if slip:
        s = int(np.argmax(t >= t_slip))
        q_s, qd_s = (x[0] for x in plan(np.array([t_slip]))[:2])
        tau_d = 0.12
        qs[s:] = q_s + np.outer(1 - np.exp(-(t[s:] - t_slip) / tau_d), qd_s * tau_d)
        phase[s:] = "abort"
    T = fk(qs)
    cmd = ((t >= t_close) & (t < t_open)).astype(int)
    width = np.where(t < t_close, OPEN_W, np.maximum(gw, OPEN_W - FINGER_SPEED * (t - t_close)))
    width = np.where(t >= t_open, np.minimum(OPEN_W, gw + FINGER_SPEED * (t - t_open)), width)
    b = int(np.argmax(t >= t_close + (OPEN_W - gw) / FINGER_SPEED))
    e = int(np.argmax(t >= t_slip)) if slip else int(np.argmax(t >= t_open))
    if slip:
        width[e:] = np.maximum(0.0, gw - FINGER_SPEED * (t[e:] - t_slip))
    man = np.tile(man_p, (n, 1))
    rel = np.linalg.inv(T[b]) @ np.r_[man_p[:3], 1.0]
    yaw_t = tcp_yaw(T)
    for k in range(b, e):
        man[k, :3] = (T[k] @ rel)[:3]
        man[k, 3] = _wrap(man_p[3] + yaw_t[k] - yaw_t[b])
    if slip:
        p0, v = man[e - 1, :3], (man[e - 1, :3] - man[e - 2, :3]) / (t[e - 1] - t[e - 2])
        zb0, g = p0[2] - man_d["height"] / 2, PHYS["g"]
        t_land = (v[2] + np.sqrt(v[2] ** 2 + 2 * g * zb0)) / g
        for k in range(e, n):
            tau = min(t[k] - t[e - 1], t_land)
            man[k, :2] = p0[:2] + v[:2] * tau
            man[k, 2] = p0[2] + v[2] * tau - 0.5 * g * tau ** 2
            man[k, 3] = man[e - 1, 3]
    else:
        man[e:] = man[e - 1]
    robot = ROBOTS[idx % len(ROBOTS)]
    objs = [{"id": "obj0", "label": man_lab, "dimensions": man_d}] + \
        [{"id": f"obj{i + 1}", "label": lab, "dimensions": d} for i, (lab, d, _) in enumerate(others)]
    poses = {"obj0": man, **{f"obj{i + 1}": np.tile(p, (n, 1)) for i, (_, _, p) in enumerate(others)}}
    return {
        "episode_id": f"v2_{idx:04d}",
        "schema": "ax-episode/0.2",
        "meta": {
            "synthetic": True, "real": False,
            "provenance": "SYNTHETIC - generated from sample 109 geometry (+ apple); noisy sensor model; not recorded on hardware",
            "generator": GENERATOR_V2, "rng_seed": [seed, idx], "variant": variant,
            "robot_id": robot, "arm_model": ARM["name"], "calibration_hash": calibration_hash(robot),
            "consent_id": f"SYN-NO-HUMAN-SUBJECT-V2-{idx:04d}", "hz": HZ, "task": f"pick_and_place/{variant}",
            "manipulated_object": "obj0",
            "target_region": {"center": list(tc), "radius": tr},
            "outcome": "failure_slip" if slip else "success",
        },
        "scene": {"table_z": PHYS["table_z"], "objects": objs},
        "frames": {"t": t, "q": qs, "gripper_cmd": cmd, "gripper_width": width, "object_poses": poses,
                   "phase": phase.tolist()},
        "events": [("contact_begin", b), ("contact_end", e)],
    }


def record(ep: dict, rng: np.random.Generator) -> dict:
    """Apply the sensor model and serialise to the ax-episode JSON layout."""
    fr = ep["frames"]
    n = len(fr["t"])
    sm = SENSOR_MODEL
    sig_q = np.deg2rad(rng.uniform(*sm["joint_noise_deg"]))
    q = fr["q"] + rng.normal(0, sig_q, fr["q"].shape)
    T = fk(q)
    tcp = np.c_[T[:, :3, 3], rot_to_quat(T[:, :3, :3])]
    t = fr["t"] + np.r_[0.0, rng.uniform(-sm["timestamp_jitter_s"], sm["timestamp_jitter_s"], n - 1)]
    width = np.clip(fr["gripper_width"] + rng.normal(0, sm["gripper_width_noise_m"], n), 0.0, ARM["gripper_aperture"])
    poses = {}
    for o, P in fr["object_poses"].items():
        P = P.copy()
        P[:, :3] += rng.normal(0, sm["object_pos_noise_m"], (n, 3))
        P[:, 3] = _wrap(P[:, 3] + rng.normal(0, sm["object_yaw_noise_rad"], n))
        poses[o] = P
    keep = np.ones(n, bool)
    dropped = None
    if rng.random() < sm["dropped_frame_prob"]:
        dropped = int(rng.integers(3, n - 3))
        keep[dropped] = False
    ev_t = {name: float(t[k]) for name, k in ep["events"]}
    r6 = lambda a: np.round(np.asarray(a, dtype=float), 6).tolist()  # noqa: E731
    out = {k: v for k, v in ep.items() if k not in ("frames", "events")}
    out["meta"] = dict(ep["meta"], sensor={"joint_sigma_deg": round(float(np.rad2deg(sig_q)), 3),
                                           "dropped_frame": dropped})
    out["frames"] = {"t": r6(t[keep]), "tcp_pose": r6(tcp[keep]), "gripper_cmd": fr["gripper_cmd"][keep].tolist(),
                     "gripper_width": r6(width[keep]), "joints": r6(q[keep]),
                     "object_poses": {o: r6(P[keep]) for o, P in poses.items()},
                     "phase": [p for p, k in zip(fr["phase"], keep) if k]}
    out["events"] = [{"t": round(ev_t[name], 6), "type": name, "object": "obj0"} for name, _ in ep["events"]]
    return out


def make_episode(idx: int, slip: bool = False, seed: int = SEED_V2) -> dict:
    variant = VARIANTS[idx % len(VARIANTS)]
    gt = simulate_v2(idx, variant, slip=slip, seed=seed)
    return record(gt, np.random.default_rng([seed, idx, 99, int(slip)]))


def main() -> dict:
    t0 = time.perf_counter()
    bench = [make_episode(i) for i in range(N_BENCH)]
    cal = [make_episode(i, seed=CAL_SEED) for i in range(N_CAL)] + \
          [make_episode(N_CAL + i, slip=True, seed=CAL_SEED) for i in range(N_CAL // 4)]
    for e in cal:
        e["episode_id"] = "cal_" + e["episode_id"]
    write_jsonl(CLEAN_V2, bench)
    write_jsonl(CAL_V2, cal)
    drops = sum(e["meta"]["sensor"]["dropped_frame"] is not None for e in bench)
    print(f"[data v2] {len(bench)} SYNTHETIC noisy benchmark episodes ({', '.join(VARIANTS)}; {drops} with a dropped "
          f"frame) + {len(cal)} calibration episodes (disjoint seeds) ({time.perf_counter() - t0:.1f}s)")
    return {"bench": bench, "cal": cal}


if __name__ == "__main__":
    main()
