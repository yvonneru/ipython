"""Fetch small REAL-robot datasets and convert them to a LeRobot-v2-style layout.

Why not the Hugging Face hub: in this environment the egress policy answers 403 to
CONNECT for huggingface.co / hf.co / cdn-lfs.* (checked 2026-09-26), so LeRobot
datasets such as lerobot/svla_so100_pickplace could not be downloaded. The Open
X-Embodiment (OXE) release on storage.googleapis.com/gresearch/robotics *is*
reachable. It contains real-robot teleoperation data in RLDS/TFRecord form. We
download a few shards (total < 300 MB, no videos are needed but RLDS embeds camera
frames in the records, which we discard) and convert the low-dimensional channels to
    data/real/<name>/meta/info.json, meta/episodes.jsonl, meta/tasks.jsonl
    data/real/<name>/data/chunk-000/episode_XXXXXX.parquet
so that ``engine/real_mode.py`` reads the same layout a LeRobot dataset has.

Nothing is synthesised during conversion. In particular RLDS has no per-step
timestamps, so the parquet files have NO ``timestamp`` column (LeRobot's own OXE ports
fill ``timestamp = frame_index / fps``; we deliberately do not, so that timing checks
report UNKNOWN instead of checking a fabricated clock).

Everything in ``axiomality_profile`` is taken from the source's own feature
descriptions (features.json) or, where marked ``external``, from a public datasheet.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from data.rlds_reader import iter_records, parse_example  # noqa: E402
from util import ROOT  # noqa: E402

REAL_DIR = ROOT / "data" / "real"
RAW_DIR = REAL_DIR / "raw"
GCS = "https://storage.googleapis.com/gresearch/robotics"
BUDGET_BYTES = 300_000_000

# Franka Emika Panda datasheet limits (public; same numbers as the declared arm in kernel/rulebook.py).
PANDA_Q_LO = [-2.8973, -1.7628, -2.8973, -3.0718, -2.8973, -0.0175, -2.8973]
PANDA_Q_HI = [2.8973, 1.7628, 2.8973, -0.0698, 2.8973, 3.7525, 2.8973]
PANDA_QD_MAX = [2.175, 2.175, 2.175, 2.175, 2.61, 2.61, 2.61]

DATASETS = {
    "droid_100": {
        "source": "droid_100", "version": "1.0.0",
        # the six smallest of 31 shards plus shards 0 and 5 (size-ordered selection to respect the budget)
        "shards": ["r2d2_faceblur-train.tfrecord-000%02d-of-00031" % i for i in (9, 6, 19, 29, 24, 17, 0, 5)],
        "robot_type": "franka_panda", "fps": 15.0,
        "fps_source": "DROID paper / OXE overview table (15 Hz control); not stored in the RLDS files",
        "state": [("steps/observation/joint_position", 7, [f"joint{j}" for j in range(1, 8)]),
                  ("steps/observation/gripper_position", 1, ["gripper"])],
        "action": [("steps/action", 7, None)],
        "extra": {"observation.cartesian_position": "steps/observation/cartesian_position",
                  "action.joint_position": "steps/action_dict/joint_position",
                  "action.joint_velocity": "steps/action_dict/joint_velocity",
                  "action.gripper_position": "steps/action_dict/gripper_position",
                  "action.cartesian_position": "steps/action_dict/cartesian_position",
                  "action.cartesian_velocity": "steps/action_dict/cartesian_velocity"},
        "tasks": ["steps/language_instruction", "steps/language_instruction_2", "steps/language_instruction_3"],
        "profile": {"joint_idx": list(range(7)), "joint_units": "rad", "gripper_state_idx": 7,
                    "ee_state_column": "observation.cartesian_position", "ee_state_idx": [0, 1, 2],
                    "ee_units_m": True,  # metres: the column equals Panda FK of the joints in metres (R-KIN-01)
                    "gripper_state_semantics": "0 = open, 1 = closed (continuous)",
                    "action_interface": "absolute_joint_position", "action_joint_column": "action.joint_position",
                    "action_joint_velocity_column": "action.joint_velocity",
                    "gripper_cmd_column": "action.gripper_position", "gripper_cmd_semantics": "0 = open, 1 = closed",
                    "limits": {"q_lower": PANDA_Q_LO, "q_upper": PANDA_Q_HI, "qd_max": PANDA_QD_MAX,
                               "source": "external: Franka Emika Panda datasheet (robot_type franka_panda); "
                                         "NOT declared in the dataset's own metadata"},
                    "outcome_from": "episode_metadata/file_path contains /success/ or /failure/; reward=1 on "
                                    "final step for successful demos (features.json)"},
    },
    "jaco_play": {
        "source": "jaco_play", "version": "0.1.0",
        "shards": ["jaco_play-train.tfrecord-00%03d-of-00128" % i for i in (108, 102, 72, 15, 76, 63)],
        "robot_type": "kinova_jaco2", "fps": 10.0,
        "fps_source": "OXE overview table (10 Hz); not stored in the RLDS files",
        "state": [("steps/observation/joint_pos", 8, [f"joint{j}" for j in range(1, 7)] + ["finger1", "finger2"])],
        "action": [("steps/action/world_vector", 3, ["dx", "dy", "dz"]),
                   ("steps/action/gripper_closedness_action", 1, ["gripper_closedness"])],
        "extra": {"observation.ee_pose": "steps/observation/end_effector_cartesian_pos",
                  "observation.ee_velocity": "steps/observation/end_effector_cartesian_velocity",
                  "action.terminate_episode": "steps/action/terminate_episode"},
        "tasks": ["steps/observation/natural_language_instruction"],
        "profile": {"joint_idx": list(range(6)), "joint_units": "rad (6 arm joints; 2 finger joints)",
                    "finger_state_idx": [6, 7], "action_interface": "ee_delta", "ee_state_column": "observation.ee_pose",
                    "ee_state_idx": [0, 1, 2], "action_ee_idx": [0, 1, 2], "gripper_cmd_action_idx": 3,
                    "gripper_cmd_semantics": "assumed RT-1/OXE convention 1 = close, -1 = open, 0 = no change "
                                             "(jaco_play features.json has no description) -> heuristic",
                    "limits": None},
    },
    "nyu_rot": {
        "source": "nyu_rot_dataset_converted_externally_to_rlds", "version": "0.1.0",
        "shards": ["nyu_rot_dataset_converted_externally_to_rlds-train.tfrecord-00000-of-00001"],
        "robot_type": "xarm", "fps": None,
        "fps_source": "not stored in the RLDS files and not used",
        "state": [("steps/observation/state", 7, ["ee_x", "ee_y", "ee_z", "ee_r1", "ee_r2", "ee_r3", "gripper"])],
        "action": [("steps/action", 7, ["d_x", "d_y", "d_z", "d_r1", "d_r2", "d_r3", "gripper"])],
        "extra": {},
        "tasks": ["steps/language_instruction"],
        "profile": {"joint_idx": [], "joint_units": "no joint angles recorded (end-effector state only)",
                    "gripper_state_idx": 6, "action_interface": "ee_delta", "ee_state_column": "observation.state",
                    "ee_state_idx": [0, 1, 2], "action_ee_idx": [0, 1, 2], "gripper_cmd_action_idx": 6,
                    "gripper_cmd_semantics": "not documented", "limits": None},
    },
}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(name: str, cfg: dict) -> list[Path]:
    d = RAW_DIR / cfg["source"]
    d.mkdir(parents=True, exist_ok=True)
    out = []
    for meta in ("features.json", "dataset_info.json"):
        p = d / meta
        if not p.exists():
            subprocess.run(["curl", "-sS", "--fail", "--retry", "3", "-o", str(p),
                            f"{GCS}/{cfg['source']}/{cfg['version']}/{meta}"], check=True)
    for s in cfg["shards"]:
        p = d / s
        if not p.exists():
            print(f"[real] downloading {cfg['source']}/{s}")
            subprocess.run(["curl", "-sS", "--fail", "--retry", "3", "--max-time", "900", "-o", str(p),
                            f"{GCS}/{cfg['source']}/{cfg['version']}/{s}"], check=True)
        out.append(p)
    return out


def _txt(v) -> str:
    return v.decode("utf-8", "replace") if isinstance(v, bytes) else str(v)


def convert(name: str, cfg: dict, shards: list[Path]) -> dict:
    out = REAL_DIR / name
    (out / "meta").mkdir(parents=True, exist_ok=True)
    (out / "data" / "chunk-000").mkdir(parents=True, exist_ok=True)
    keys = {k for k, _, _ in cfg["state"] + cfg["action"]} | set(cfg["extra"].values()) | set(cfg["tasks"]) | {
        "steps/is_first", "steps/is_last", "steps/is_terminal", "steps/reward", "episode_metadata/file_path"}
    tasks: dict[str, int] = {}
    episodes, gidx, ep_idx = [], 0, 0
    for shard in shards:
        for rec_i, rec in enumerate(iter_records(shard)):
            ex = parse_example(rec, keys)
            n = len(ex["steps/is_first"])

            def mat(key, dim):
                v = np.asarray(ex[key], np.float32)
                if v.size != n * dim:
                    raise ValueError(f"{name}: {key} has {v.size} values for {n} steps x {dim}")
                return v.reshape(n, dim)
            state = np.concatenate([mat(k, d) for k, d, _ in cfg["state"]], axis=1) if n else np.zeros((0, 1))
            action = np.concatenate([mat(k, d) for k, d, _ in cfg["action"]], axis=1) if n else np.zeros((0, 1))
            cols = {"index": np.arange(gidx, gidx + n), "episode_index": np.full(n, ep_idx),
                    "frame_index": np.arange(n), "observation.state": list(state), "action": list(action)}
            for col, key in cfg["extra"].items():
                v = np.asarray(ex[key])
                cols[col] = list(v.reshape(n, -1).astype(np.float32))
            strs = [[_txt(x) for x in ex[k]] for k in cfg["tasks"]]
            tidx = []
            for i in range(n):
                t = strs[0][i]
                tidx.append(tasks.setdefault(t, len(tasks)))
            cols["task_index"] = np.asarray(tidx, np.int64)
            for k in ("is_first", "is_last", "is_terminal"):
                cols[f"next.{k}" if k != "is_first" else k] = np.asarray(ex[f"steps/{k}"], bool)
            cols["next.reward"] = np.asarray(ex["steps/reward"], np.float32)
            df = pd.DataFrame(cols)
            pq.write_table(pa.Table.from_pandas(df, preserve_index=False),
                           out / "data" / "chunk-000" / f"episode_{ep_idx:06d}.parquet")
            fp = ex.get("episode_metadata/file_path")
            episodes.append({"episode_index": ep_idx, "length": n,
                             "tasks": sorted({s for col in strs for s in col}, key=lambda s: (s == "", s)),
                             "task_columns": {k.split("/")[-1]: sorted(set(c)) for k, c in zip(cfg["tasks"], strs)},
                             "source_file_path": _txt(fp[0]) if fp else None,
                             "source_shard": shard.name, "source_record": rec_i})
            gidx += n
            ep_idx += 1
    feats = {"observation.state": {"dtype": "float32", "shape": [sum(d for _, d, _ in cfg["state"])],
                                   "names": sum([nm or [f"{k.split('/')[-1]}_{i}" for i in range(d)]
                                                 for k, d, nm in cfg["state"]], [])},
             "action": {"dtype": "float32", "shape": [sum(d for _, d, _ in cfg["action"])],
                        "names": sum([nm or [f"{k.split('/')[-1]}_{i}" for i in range(d)]
                                      for k, d, nm in cfg["action"]], [])}}
    src_feats = json.loads((RAW_DIR / cfg["source"] / "features.json").read_text())

    def desc(path):
        node = src_feats
        for part in path.split("/"):
            if part == "steps":
                node = node["featuresDict"]["features"]["steps"]["sequence"]["feature"]
            else:
                node = node["featuresDict"]["features"][part]
        return node.get("description", "")
    for col, key in list(cfg["extra"].items()) + [(k, k) for k, _, _ in cfg["state"] + cfg["action"]]:
        try:
            feats.setdefault(col, {})["source_description"] = desc(key)
        except KeyError:
            pass
    feats["action"]["source_description"] = " | ".join(desc(k) for k, _, _ in cfg["action"])
    feats["observation.state"]["source_description"] = " | ".join(desc(k) for k, _, _ in cfg["state"])
    total_bytes = sum(p.stat().st_size for p in shards)
    info = {
        "codebase_version": "v2.0 (AXIOMALITY conversion of an OXE RLDS source; LeRobot-v2-style layout)",
        "robot_type": cfg["robot_type"], "fps": cfg["fps"], "fps_source": cfg["fps_source"],
        "total_episodes": len(episodes), "total_frames": gidx, "total_tasks": len(tasks),
        "has_timestamps": False,
        "timestamps_note": "the RLDS source has no per-step timestamps; none were synthesised",
        "data_path": "data/chunk-000/episode_{episode_index:06d}.parquet", "features": feats,
        "real": True, "synthetic": False,
        "source": {"collection": "Open X-Embodiment (RLDS)", "url": f"{GCS}/{cfg['source']}/{cfg['version']}/",
                   "dataset": cfg["source"], "version": cfg["version"], "download_bytes": total_bytes,
                   "shards": [{"file": p.name, "bytes": p.stat().st_size, "sha256": sha256_file(p)} for p in shards],
                   "selection": "subset of shards chosen by file size to keep the total download < 300 MB; "
                                "may be biased toward shorter episodes",
                   "why_not_huggingface": "huggingface.co blocked by this environment's egress policy (HTTP 403 on CONNECT)"},
        "axiomality_profile": cfg["profile"],
    }
    (out / "meta" / "info.json").write_text(json.dumps(info, indent=2))
    with open(out / "meta" / "episodes.jsonl", "w") as f:
        for e in episodes:
            f.write(json.dumps(e) + "\n")
    with open(out / "meta" / "tasks.jsonl", "w") as f:
        for t, i in sorted(tasks.items(), key=lambda x: x[1]):
            f.write(json.dumps({"task_index": i, "task": t}) + "\n")
    print(f"[real] {name}: {len(episodes)} REAL episodes, {gidx} frames from {len(shards)} shard(s) "
          f"({total_bytes / 1e6:.0f} MB) -> {out.relative_to(ROOT)}")
    return info


def main(names=None) -> dict:
    names = names or list(DATASETS)
    shards = {n: download(n, DATASETS[n]) for n in names}
    total = sum(p.stat().st_size for v in shards.values() for p in v)
    if total > BUDGET_BYTES:
        raise SystemExit(f"download budget exceeded: {total / 1e6:.0f} MB")
    return {n: convert(n, DATASETS[n], shards[n]) for n in names}


if __name__ == "__main__":
    main()
