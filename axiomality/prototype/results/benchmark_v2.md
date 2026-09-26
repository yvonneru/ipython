# Benchmark v2: engine vs strong baseline vs structural baseline (SYNTHETIC, noisy)

300 SYNTHETIC episodes, 3 task variants (mug_to_target, mug_next_to_laptop, fruit_from_B), 3 object classes (mug, laptop, fruit). Sensor model: joint noise sigma 0.2-0.5 deg, object position noise 3 mm/axis, +-5 ms timestamp jitter, one dropped frame in ~30% of episodes. 20 episodes per error class, 20 valid failures, 140 clean. All tolerances calibrated on a disjoint calibration split (150 episodes (30 slips), disjoint seeds).

| Error class | n | Engine | Strong baseline | Structural baseline | Engine correct action | Engine rule attribution |
|---|---|---|---|---|---|---|
| (a) wrong object label | 20 | 55% | 55% | 0% | 55% | 55% |
| (b) impossible relation | 20 | 95% | 95% | 0% | 95% | 95% |
| (c) illegal phase order | 20 | 100% | 100% | 0% | 100% | 100% |
| (d) object teleport | 20 | 95% | 95% | 90% | 95% | 95% |
| (e) timestamp warp | 20 | 100% | 100% | 100% | 100% | 100% |
| (f) joint-limit violation | 20 | 100% | 100% | 100% | 100% | 100% |
| (g) gripper/contact mismatch | 20 | 100% | 100% | 0% | 100% | 100% |

| Overall | Engine | Strong | Structural |
|---|---|---|---|
| Recall | 0.92 (129/140) | 0.92 (129/140) | 0.41 (58/140) |
| Precision | 1.00 | 1.00 | 1.00 |
| False rejects, clean noisy episodes | 0/140 (0.0%) | 0/140 (0.0%) | 0/140 (0.0%) |
| Valid failures kept | 20/20 | 20/20 | 20/20 |
| Classes at 100% recall | 4/7 | 4/7 | 2/7 |
| ms / episode | 14.3 | 1.4 | 0.56 |

Engine with uncalibrated v1 tolerances on the same noisy data: false rejects on clean 140/140, valid failures kept 0/20 (v1 as shipped: 140/140 / 0/20).

Timestamp repairs byte-identical to the original noisy recording: 20/20.

## Calibrated tolerances

Engine overrides: `{"static_tol": 0.02384, "comove_tol": 0.059606, "pen_tol": 0.0125, "support_tol": 0.023438, "a_fragile": 10.0, "dt_rel_tol": 0.3125, "ballistic_az": [-1.875, -0.4], "max_single_drops": 2, "smooth_window": 5, "event_snap_s": 0.016666666666666666, "qd_margin": 1.953125}`

Strong baseline: `{"static_tol": 0.02384, "support_tol": 0.029298, "comove_tol": 0.030518, "pen_tol": 0.01, "grip_open_tol": 0.005, "grace_s": 0.5, "qd_margin": 1.953125, "max_single_drops": 2, "target_slack": 0.0}`

Structural baseline: `{"max_single_drops": 2, "qd_margin": 1.953125}`

## Where the two rule-based checkers differ

Engine-only catches by engine rule: `{}`


## The original v1 (noise-free) benchmark with the strong baseline added

| Error class (n = 10) | Engine (v1) | Strong baseline | Structural baseline (v1) |
|---|---|---|---|
| (a) wrong object label | 40% | 40% | 0% |
| (b) impossible relation | 90% | 90% | 0% |
| (c) illegal phase order | 100% | 100% | 0% |
| (d) object teleport | 100% | 100% | 80% |
| (e) timestamp warp | 100% | 100% | 100% |
| (f) joint-limit violation | 100% | 100% | 100% |
| (g) gripper/contact mismatch | 100% | 100% | 0% |
| **Overall recall** | 0.90 | 0.90 | 0.40 |
| Clean kept / valid failures kept | 100% / 100% | 100% / 100% | 100% / 100% |

## Sensitivity sweep (controlled magnitudes, 12 identical clean base episodes per point)

Detection rate per injected magnitude. Same error types as classes (b) and (d); same base episodes for all checkers.

| Error type | magnitude (mm) | Engine | Strong | Structural |
|---|---|---|---|---|
| laptop sunk | 5 | 0% | 0% | 0% |
| laptop sunk | 10 | 0% | 0% | 0% |
| laptop sunk | 15 | 0% | 0% | 0% |
| laptop sunk | 20 | 8% | 0% | 0% |
| laptop sunk | 25 | 100% | 0% | 0% |
| laptop sunk | 30 | 100% | 0% | 0% |
| laptop sunk | 40 | 100% | 100% | 0% |
| laptop floating | 5 | 0% | 8% | 0% |
| laptop floating | 10 | 100% | 92% | 0% |
| laptop floating | 15 | 100% | 100% | 0% |
| laptop floating | 20 | 100% | 100% | 0% |
| laptop floating | 25 | 100% | 100% | 0% |
| laptop floating | 30 | 100% | 100% | 0% |
| laptop floating | 40 | 100% | 100% | 0% |
| persistent teleport | 10 | 0% | 0% | 0% |
| persistent teleport | 20 | 8% | 0% | 0% |
| persistent teleport | 30 | 92% | 0% | 0% |
| persistent teleport | 40 | 100% | 42% | 0% |
| persistent teleport | 60 | 100% | 100% | 0% |
| persistent teleport | 80 | 100% | 100% | 0% |
| floating after release | 5 | 0% | 0% | 0% |
| floating after release | 10 | 0% | 0% | 0% |
| floating after release | 20 | 42% | 17% | 0% |
| floating after release | 30 | 100% | 100% | 0% |
| floating after release | 40 | 100% | 100% | 0% |
| interpenetration | 5 | 100% | 100% | 0% |
| interpenetration | 10 | 100% | 100% | 0% |
| interpenetration | 15 | 100% | 100% | 0% |
| interpenetration | 20 | 100% | 100% | 0% |
| interpenetration | 30 | 100% | 100% | 0% |

## Engine misses

- `v2_0020` a_wrong_label: variant=fruit_from_B, object=obj1, from=mug, to=vase
- `v2_0060` a_wrong_label: variant=mug_to_target, object=obj2, from=fruit, to=earphone
- `v2_0092` a_wrong_label: variant=fruit_from_B, object=obj0, from=fruit, to=mug
- `v2_0103` a_wrong_label: variant=mug_next_to_laptop, object=obj0, from=mug, to=earphone
- `v2_0172` a_wrong_label: variant=mug_next_to_laptop, object=obj2, from=fruit, to=earphone
- `v2_0174` a_wrong_label: variant=mug_to_target, object=obj2, from=fruit, to=mug
- `v2_0206` a_wrong_label: variant=fruit_from_B, object=obj0, from=fruit, to=mug
- `v2_0217` a_wrong_label: variant=mug_next_to_laptop, object=obj2, from=fruit, to=mug
- `v2_0237` a_wrong_label: variant=mug_to_target, object=obj0, from=mug, to=vase
- `v2_0209` b_impossible_relation: variant=fruit_from_B, subtype=manipulated_floating_after_release, raise_m=0.0108, from_frame=158
- `v2_0239` d_teleport: variant=fruit_from_B, frame=151, magnitude_m=0.0338, mode=persistent, frames=[151, 177]

## Accepted split and passport

Accepted split: 191 episodes; passport `passport_AX-DEMO-109-v2.json`. **Evaluation-only:** 11 accepted episodes are known from the injection key to contain an injected error that the engine did not detect. The passport cannot know this and does not contain the number.

## Behaviour checks

| Case | Expected | Engine | Strong baseline |
|---|---|---|---|
| object poses missing | UNKNOWN | UNKNOWN | REJECT |
| joint angles logged in degrees | REPAIR | REPAIR | REJECT |
| slip relabelled as success (phases relabelled too) | REJECT | REJECT | REJECT |
| duplicate timestamp (not re-sortable) | REJECT | REJECT | REJECT |
| contact ends mid-transport, gripper still closed (cross-rule) | REJECT | REJECT | REJECT |

## Rule encoding (exact)

30 rules: 9 are decided per episode by a Z3 query, 15 more are Z3-encoded only in the rulebook self-check (evaluated per episode with numpy), 6 are numeric-only (R-CONT-03, R-KIN-01, R-PROV-01, R-SUP-02, R-TYPE-01, R-TYPE-03). The rulebook's own kind labels say 23 z3 / 7 numeric; they disagree with the self-check for R-TIME-01.
