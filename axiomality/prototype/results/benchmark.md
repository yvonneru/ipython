# Benchmark: AXIOMALITY engine vs rules-only baseline

Dataset: AX-DEMO-109 injected held-out copy (SYNTHETIC), 200 episodes (10 per error class, 10 valid failures, 120 clean). All data SYNTHETIC; errors injected by `inject/inject.py`.

| Error class | n | Engine recall | Baseline recall | Engine correct action | Engine rule attribution |
|---|---|---|---|---|---|
| a_wrong_label | 10 | 40% | 0% | 40% | 40% |
| b_impossible_relation | 10 | 90% | 0% | 90% | 90% |
| c_phase_order | 10 | 100% | 0% | 100% | 100% |
| d_teleport | 10 | 100% | 80% | 100% | 100% |
| e_timestamp_warp | 10 | 100% | 100% | 100% | 100% |
| f_joint_limit | 10 | 100% | 100% | 100% | 100% |
| g_gripper_contact_mismatch | 10 | 100% | 0% | 100% | 100% |

| Overall | Engine | Baseline |
|---|---|---|
| Precision (flagged episodes that were corrupted) | 1.00 | 1.00 |
| Recall (corrupted episodes flagged) | 0.90 (63/70) | 0.40 (28/70) |
| False-reject rate, clean episodes in held-out set | 0.0% | 0.0% |
| Valid failures (physically consistent slips) kept | 10/10 | 10/10 |
| Error classes with 100% recall | 5/7 | 2/7 |
| Runtime per episode | 7.7 ms | 0.48 ms |

Engine false-reject rate on the 200 pristine episodes: 0.0%. Timestamp repairs byte-identical to the original episode: 10/10.

Recall = verdict other than PASS. Correct action = REPAIR for timestamp warps, REJECT otherwise. Rule attribution = at least one finding cites a rule from the expected family.

## Engine misses

- `ep_0002` a_wrong_label: object=obj0, from=mug, to=vase
- `ep_0016` a_wrong_label: object=obj0, from=mug, to=vase
- `ep_0047` a_wrong_label: object=obj0, from=mug, to=earphone
- `ep_0119` a_wrong_label: object=obj0, from=mug, to=fruit
- `ep_0182` a_wrong_label: object=obj0, from=mug, to=fruit
- `ep_0198` a_wrong_label: object=obj0, from=mug, to=vase
- `ep_0087` b_impossible_relation: subtype=laptop_sunk, sink_m=0.0171

## Behaviour checks

| Case | Expected | Engine | Baseline |
|---|---|---|---|
| object poses missing | UNKNOWN | UNKNOWN | REJECT |
| joint angles logged in degrees | REPAIR | REPAIR | REJECT |
| slip episode relabelled as success | REJECT | REJECT | PASS |
| duplicate timestamp (not re-sortable) | REJECT | REJECT | REJECT |
