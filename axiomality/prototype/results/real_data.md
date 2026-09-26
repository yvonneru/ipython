# Real-data mode results (REAL robot data, Open X-Embodiment RLDS subsets)

Hugging Face (LeRobot) was unreachable from this environment (HTTP 403 from the egress proxy for huggingface.co); the data comes from the public OXE bucket on storage.googleapis.com and was converted to a LeRobot-v2-style layout without synthesising anything (no timestamps were invented).

| Dataset | Robot | Episodes | Frames | Download | PASS | REPAIR | REJECT | UNKNOWN | Baseline PASS/REJECT |
|---|---|---|---|---|---|---|---|---|---|
| droid_100 | franka_panda | 14 | 2551 | 165.3 MB | 5 | 1 | 8 | 0 | 12/2 |
| jaco_play | kinova_jaco2 | 13 | 879 | 112.4 MB | 13 | 0 | 0 | 0 | 13/0 |
| nyu_rot | xarm | 14 | 440 | 5.6 MB | 14 | 0 | 0 | 0 | 14/0 |

## Verdict shares per check family (% of episodes: PASS / REPAIR / REJECT / UNKNOWN; advisory episodes)

| Family | kernel rule | droid_100 | jaco_play | nyu_rot |
|---|---|---|---|---|
| timing | R-TIME-01/02 | UNKNOWN | UNKNOWN | UNKNOWN |
| boundaries | - | 100/0/0/0 (+1 adv.) | 100/0/0/0 | 100/0/0/0 |
| numeric | R-QTY-01 | 100/0/0/0 | 100/0/0/0 | 100/0/0/0 |
| frames | - | 93/0/7/0 | 100/0/0/0 | UNKNOWN |
| joint_limits | R-JNT-01 | 93/0/7/0 | 100/0/0/0 | UNKNOWN |
| motion | R-JNT-02 / R-PERM-01 | 100/0/0/0 | 100/0/0/0 | 100/0/0/0 |
| kinematics | R-KIN-01 | 100/0/0/0 | UNKNOWN | UNKNOWN |
| action_state | - | 93/0/7/0 | 100/0/0/0 | 100/0/0/0 (+13 adv.) |
| gripper | R-GRIP-01 (analogue) | 100/0/0/0 (+1 adv.) | 100/0/0/0 | UNKNOWN |
| duplicates | - | 100/0/0/0 | 100/0/0/0 | 100/0/0/0 |
| task | - | 36/7/57/0 | 100/0/0/0 | 100/0/0/0 |
| outcome | - | 100/0/0/0 | UNKNOWN | UNKNOWN |
| semantic | R-TYPE/SUP/SPAT/PERM/CONT/PHASE/TASK | UNKNOWN | UNKNOWN | UNKNOWN |

UNKNOWN reasons: frames: state is quantized (median 2% distinct values per non-constant state channel over 440 frames); bit-identical consecutive rows are expected and are not evidence of a stale stream; gripper: gripper command semantics not documented or channels missing; joint_limits: no joint angles in dataset; kinematics: kernel has no kinematic model for robot_type 'kinova_jaco2'; kinematics: no joint angles in dataset; outcome: no independent outcome label to compare the reward with; semantic: no object state in dataset: object poses, object classes/dimensions, contact events and phase labels are not recorded, so type/size, support, contact, permanence, spatial, phase-grammar and task-success rules cannot be evaluated; timing: no per-frame timestamps in dataset; timing: no per-frame timestamps in dataset (fps is declared externally only)

## droid_100: findings (real)

- R-KIN-01 ran on every frame: recorded Cartesian position vs Panda FK (flange) of the recorded joints, max error 0.04 micrometres over 2551 frames (PASS; float32 precision).
- [hard] episode all, frame None, schema: column 'action[:6]' is bit-identical to 'action.cartesian_position' in all 2551 frames. Why: documented as "Robot action, consists of [6x joint velocities, 1x gripper position]." but it holds "Commanded Cartesian position"
- [hard] episode 3 (AUTOLab/failure/2023-11-09), frame 19, action_state: commanded motion not executed for 15 frames (1.0 s): all joints static (|dq| < 1e-04 rad/frame) while the commanded joint position differs by 0.133 rad (median). Why: the recorded actions do not produce the recorded next states (stuck arm, controller not engaged or stale state stream); a policy trained on these pairs learns that commands do nothing
- [hard] episode 1 (TRI/failure/2023-10-18), frame 141, joint_limits: joint 6 = 3.7626 rad outside [-0.0175, 3.7525] on 32 frame(s), max excess 207.0 mrad. Why: limits from external: Franka Emika Panda datasheet (robot_type franka_panda)
- [hard] episode 3 (AUTOLab/failure/2023-11-09), frame 43, frames: 7 duplicated frame(s), longest run 7 (from frame 43). Why: every channel incl. a non-zero action is bit-identical to the previous frame: a stale or frozen data stream, not an idle robot
- [hard] episode 8/14 episodes, frame 0, task: no language instruction in any instruction field (episodes [1, 3, 4, 5, 6, 7, 12, 13]; 5 of them recorded as success). Why: unusable for language-conditioned training; task undocumented
- [hard] episode 0 (AUTOLab/success/2023-10-15), frame 0, task: whitespace anomaly in task string 'Put the  cable in the storage box'. Why: double/leading/trailing whitespace
- [heuristic] episode 6 (WEIRD/success/2024-01-09), frame 143, gripper: partial close command (0.25) with gripper state exactly 0 for 34 frames. Why: HEURISTIC: command below an unknown deadband or gripper not reporting
- [heuristic] episode 7 (TRI/failure/2023-08-22), frame None, boundaries: very short episode: 13 frames (0.9 s). Why: shorter than 2 s of data; often an aborted recording

Structural baseline (min_frames, finite, joint_limits, joint_speed, tcp_speed_spike): accept/reject agreement with the engine 8/14; agreement on the shared checks 14/14.
- episode 3: engine REJECT (action_state: commanded motion not executed for 15 frames (1.0 s): all joints static (|dq| < 1e-04 rad/f; frames: 7 duplicated frame(s), longest run 7 (from frame 43); task: empty task / language inst), baseline PASS (no issue)
- episode 4: engine REJECT (task: empty task / language instruction), baseline PASS (no issue)
- episode 5: engine REJECT (task: empty task / language instruction), baseline PASS (no issue)
- episode 6: engine REJECT (task: empty task / language instruction), baseline PASS (no issue)
- episode 12: engine REJECT (task: empty task / language instruction), baseline PASS (no issue)
- episode 13: engine REJECT (task: empty task / language instruction), baseline PASS (no issue)

Passport `passport_real_droid_100.json`: 6 accepted episodes, verification VALID.

## jaco_play: findings (real)

- none (all runnable checks passed)

Structural baseline (min_frames, finite): accept/reject agreement with the engine 13/13; agreement on the shared checks 13/13.

Passport `passport_real_jaco_play.json`: 13 accepted episodes, verification VALID.

## nyu_rot: findings (real)

- [heuristic] episode 0 (data/train/episode_4.npy), frame 0, action_state: axis z: commanded - for 2 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 1 (data/train/episode_3.npy), frame 6, action_state: axis y: commanded + for 2 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 2 (data/train/episode_10.npy), frame 14, action_state: axis z: commanded - for 4 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 3 (data/train/episode_12.npy), frame 7, action_state: axis y: commanded - for 6 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 4 (data/train/episode_1.npy), frame 17, action_state: axis z: commanded - for 3 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 5 (data/train/episode_5.npy), frame 13, action_state: axis z: commanded - for 3 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 7 (data/train/episode_0.npy), frame 15, action_state: axis z: commanded - for 3 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 8 (data/train/episode_13.npy), frame 14, action_state: axis x: commanded - for 2 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 9 (data/train/episode_8.npy), frame 18, action_state: axis z: commanded - for 5 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 10 (data/train/episode_6.npy), frame 16, action_state: axis z: commanded - for 3 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 11 (data/train/episode_9.npy), frame 22, action_state: axis x: commanded - for 2 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 11 (data/train/episode_9.npy), frame 9, action_state: axis z: commanded - for 4 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 12 (data/train/episode_7.npy), frame 15, action_state: axis z: commanded - for 3 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 13 (data/train/episode_2.npy), frame 20, action_state: axis z: commanded - for 3 frames, EE position unchanged (not at the dataset's workspace bound). Why: HEURISTIC commanded motion not executed; a benign cause is contact with a surface (e.g. pressing on a board), which cannot be checked without object state
- [heuristic] episode 0 (data/train/episode_4.npy), frame 29, frames: idle tail: last 11 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 1 (data/train/episode_3.npy), frame 20, frames: idle tail: last 10 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 2 (data/train/episode_10.npy), frame 19, frames: idle tail: last 11 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 3 (data/train/episode_12.npy), frame 20, frames: idle tail: last 10 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 4 (data/train/episode_1.npy), frame 21, frames: idle tail: last 9 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 5 (data/train/episode_5.npy), frame 25, frames: idle tail: last 5 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 6 (data/train/episode_11.npy), frame 21, frames: idle tail: last 9 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 7 (data/train/episode_0.npy), frame 20, frames: idle tail: last 10 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 8 (data/train/episode_13.npy), frame 21, frames: idle tail: last 9 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 9 (data/train/episode_8.npy), frame 25, frames: idle tail: last 5 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 10 (data/train/episode_6.npy), frame 21, frames: idle tail: last 9 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 11 (data/train/episode_9.npy), frame 25, frames: idle tail: last 15 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 12 (data/train/episode_7.npy), frame 20, frames: idle tail: last 10 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming
- [heuristic] episode 13 (data/train/episode_2.npy), frame 25, frames: idle tail: last 5 frames have zero action and unchanged state. Why: idle frames add no information; consider trimming

Structural baseline (min_frames, finite): accept/reject agreement with the engine 14/14; agreement on the shared checks 14/14.

Passport `passport_real_nyu_rot.json`: 14 accepted episodes, verification VALID.

## Timing-family self-test (SYNTHETIC timestamps on real episodes)

- clean clock: PASS 
- two missing frames (gap of 3 periods): REJECT - 1 gap(s) totalling ~2 dropped frame(s); first at frame 10 (3.0/fps)
- two rows swapped: REPAIR - rows out of timestamp order at frame 6
