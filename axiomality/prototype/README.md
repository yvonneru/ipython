# AXIOMALITY evidence-layer prototype

This is a small, working prototype of the AXIOMALITY verification engine. It checks
robot-episode data against a formal rulebook (the "knowledge kernel", written as Z3
axioms) plus kinematic and physics checks. For each episode it returns
**PASS / REPAIR / REJECT / UNKNOWN**, and each finding names a rule ID and a frame.
The engine then issues an **Ed25519-signed Data Passport** that anyone can verify
offline.

> **v1 (the sections up to "Limitations") uses SYNTHETIC episodes only.** The only real input is the scene geometry of
> AXIOMALITY sample 109 (`pointclouds/109.ply`: one mug and one laptop, with measured
> boxes). The episodes are simulated around that scene, the errors are injected by us,
> and the results are internal-prototype numbers. They are not field results.
>
> **Read the v2 section at the end before quoting the v1 numbers.** v2 adds real robot data
> (three public Open X-Embodiment subsets) and a noisy synthetic benchmark with a *strong*
> hand-written baseline. That baseline matches the engine's recall on both the v1 and the v2
> injected sets, so the v1 "90% vs 40%" comparison measures how the v1 baseline was
> specified, not an advantage of the rulebook.

## Run

```bash
pip install -r requirements.txt      # z3-solver, numpy, matplotlib, cryptography
python run_all.py                    # everything, ~20 s on a laptop-class CPU
```

`run_all.py` runs these steps in order: rulebook self-check, synthetic data generation,
error injection, the engine-vs-baseline benchmark, passport issuance, offline
verification, the tamper demo, and the figures. The individual entry points are
`python verify_passport.py` (exit 0 = valid, 1 = invalid) and `python tamper_demo.py`.
All randomness is seeded, so repeated runs give the same data, verdicts and content
hash. Only `issued_at` and the timings change.

## What is where

| Path | Contents |
|---|---|
| `kernel/rulebook.py` | Declarative rulebook: 7 object types × 5 properties + size ranges, 6 phase labels, declared 7-DoF arm (Panda-style DH, joint/speed limits, 0.14 m gripper), physical constants, 30 rules (`R-PROV/TIME/QTY/TYPE/JNT/KIN/GRIP/CONT/PERM/SUP/SPAT/PHASE/TASK`). Its hash goes into the passport. |
| `kernel/axioms.py` | Z3 encoding. It covers per-episode decisions (object type/size/affordance, phase grammar, contact events, with violated rules taken from unsat cores) and the **rulebook self-check**. |
| `kernel/arm.py`, `kernel/geometry.py` | Vectorised forward kinematics and DLS inverse kinematics; oriented-box separating-axis penetration test. |
| `data/generate.py` | Seeded simulator. It produces 200 pick-and-place episodes at 30 Hz: TCP pose, gripper command and width, 7 joints, object poses, phase labels, contact events, and metadata (robot id, calibration hash, consent id, `synthetic: true`). |
| `inject/inject.py` | Builds the held-out copy with 7 error classes × 10 episodes (35%) and 10 *valid failures*. Every change is documented in `data/generated/injection_key.json`. |
| `engine/verifier.py` | The verifier: inputs → repair of recording defects → kernel checks → verdict and reasons. |
| `baseline/rules_only.py` | A fair rules-only baseline (see below). |
| `benchmark.py` | Runs both checkers → `results/benchmark.{json,md}`, verdict files, and the accepted split. |
| `passport/passport.py`, `verify_passport.py`, `tamper_demo.py` | Passport issue and verify, plus the tamper demo. |
| `figures/` | `benchmark_recall.png`, `passport_card.png`, `verdict_example.png` (1600 px wide). |
| `keys/` | **Demo** Ed25519 keypair. See `keys/README.md`: the private key is unprotected and must not be used in production. |

## Rulebook self-check (Z3)

The self-check runs on every `run_all.py` and writes `results/rulebook_selfcheck.json`.

- **Result: SATISFIABLE (the rulebook is consistent).** The rulebook has 30 rules, 7 object types, 6 phase labels and 83 ground facts; the self-check instance contains 600 Z3 assertions.
- **Type layer.** Z3 finds a model with one object of every class plus a manipulated, graspable mug, under the property-coherence axiom (rigid ⇔ ¬deformable, container ⇒ rigid).
- **Seed scene 109 (verbatim) is consistent with the scene axioms.** Two measurement offsets fall inside the tolerances: the mug bottom sits 3.3 mm *below* the table and the laptop bottom sits 13.3 mm *above* it.
- **Episode layer.** This is a bounded 14-frame symbolic episode with 408 instantiated axioms. Z3 finds both a successful pick-and-place and a slip-failure episode.
- **Independence.** 18 of 19 symbolically encoded episode rules are not implied by the others. `R-TIME-01` (monotonic time) is implied by `R-TIME-02` (bounded sampling interval), and the report states this.
- **Not symbolically encoded.** Six rules are checked numerically only: `R-KIN-01` (nonlinear FK), `R-SUP-02`, `R-TYPE-01/03`, `R-CONT-03` and `R-PROV-01`. The symbolic episode is a 1-D horizontal + vertical abstraction.

## Results (injected held-out copy, 200 SYNTHETIC episodes)

| Error class (n = 10 each) | Engine recall | Baseline recall |
|---|---|---|
| (a) wrong object label | 40% | 0% |
| (b) physically impossible relation | 90% | 0% |
| (c) reversed / illegal phase order | 100% | 0% |
| (d) object teleport | 100% | 80% |
| (e) 3-frame timestamp warp | 100% (all REPAIR) | 100% |
| (f) joint-limit violation | 100% | 100% |
| (g) gripper-state vs contact mismatch | 100% | 0% |

| Overall | Engine | Baseline |
|---|---|---|
| Precision | 1.00 | 1.00 |
| Recall | 0.90 (63/70) | 0.40 (28/70) |
| False-reject rate on 120 clean episodes | 0.0% | 0.0% |
| Valid failures (physically consistent slips) kept | 10/10 | 10/10 |
| Runtime per episode (single core, Python) | ~8 ms | ~0.5 ms |

Other results:

- The engine false-reject rate on all 200 pristine episodes is 0%.
- All 10 timestamp repairs are byte-identical to the original episode.
- Behaviour checks:
  - Missing object poses → UNKNOWN.
  - Joint angles logged in degrees → REPAIR.
  - A slip episode relabelled as "success" → REJECT, because the engine never turns a failure into a success.
  - A duplicate timestamp (cannot be re-sorted) → REJECT.

The full per-class breakdown, correct-action and rule-attribution rates, and the list of
misses are in `results/benchmark.md`.

**What the engine misses, and why.**

- **6 of the 10 wrong labels.** A mug relabelled *vase*, *fruit* or *earphone* has a bounding box that fits those classes' plausible size ranges. Box geometry alone cannot tell them apart; shape features from the point clouds would be needed.
- **One sunken laptop.** It was sunk 17 mm, and with the laptop's original 13 mm gap that leaves it only 4 mm below the table, inside the 10 mm tolerance.

These 7 missed episodes are in the accepted split, and the passport does not flag them.

**The baseline** gets everything a careful engineer would write in an afternoon:

- a schema check;
- NaN/Inf checks;
- monotonic timestamps;
- frame-drop detection;
- the same joint position and speed limits;
- gripper range and binary command;
- a speed-spike detector on TCP and object poses using the *same* v_max = 3 m/s;
- label vocabularies;
- dangling-event checks.

It has no object semantics, support or contact reasoning, phase grammar or kinematic
model. It catches teleports larger than about 0.1 m per frame, but not smaller ones.
A hand-written phase-order list would let the baseline catch (c) too. The point of the
kernel is to make rules like that declarative, consistency-checked and citable, not to
claim they cannot be written by hand. Both checkers keep the valid failures. The
engine's contribution there is that it keeps them *while* rejecting physically
impossible motion (floating, teleports) that the baseline also lets through.

## Data Passport

`results/passport_AX-DEMO-109.json` contains:

- the dataset id;
- the content hash: sha256 over the canonical JSON of the accepted split (137 PASS + 10 repaired episodes), with per-episode hashes included;
- the rulebook version and hash;
- verdict counts: 137 PASS, 10 REPAIR, 53 REJECT, 0 UNKNOWN;
- a findings summary by rule family and rule;
- the real/synthetic ratio (0 real / 147 synthetic);
- provenance (seed-sample hash, generator, robot ids, calibration hashes, consent ids);
- tool versions;
- `issued_at`;
- an Ed25519 signature.

`verify_passport.py` verifies the signature against the trusted public-key *file*, not
against the key embedded in the passport, and recomputes the content hash from the data.
`tamper_demo.py` runs four cases:

| Change | Verification result |
|---|---|
| Flip one label | Fails, and names the changed episode |
| Shift one timestamp by 1 ms | Fails |
| Edit one passport count | Fails (invalid signature) |
| Restore the originals | Passes |

## Limitations (read before quoting numbers)

- **Synthetic episodes only.** One seed scene, one task, and one simulated arm. The errors were injected by the same team that wrote the engine, so blind spots may be shared. The error distributions and magnitudes were fixed before the benchmark was run and include near-threshold cases. The tolerances were set from physical reasoning and checked on clean and slip simulations; one fix (a landing-frame exemption) came from slip simulations, not from the injected set.
- **Small n.** There are 10 episodes per class, so one episode moves recall by 10 points.
- **Not a safety certification.** A passport attests which checks ran and what they found. It does not certify that the data is correct or safe to train on.
- **Kinematic physics only.** There is no force or torque data, no contact mechanics beyond the gripper-width model, no friction, and no tipping or bounce. Objects are axis-aligned-in-z boxes.
- **Demo key.** The key is unprotected, and there is no key rotation or revocation. The issuer identity is not established.

---

# v2 (2026-09-26): real data, noise, a strong baseline

Reproduce with `python run_v2.py` (or `python run_all.py --v2`); about 65 s after a one-time
~280 MB download; `--skip-real` runs the synthetic part only. v1 outputs are not touched.
New code: `engine/real_mode.py`, `data/rlds_reader.py`, `data/real_fetch.py`, `real_benchmark.py`,
`data/generate_v2.py`, `inject/inject_v2.py`, `baseline/strong_rules.py`, `kernel/profiles.py`,
`benchmark_v2.py`, `figures/make_figures_v2.py`, `run_v2.py`. Changes to v1 files are opt-in
switches whose defaults reproduce every saved v1 verdict and finding byte for byte (checked
for all 200 v1 episodes).

## What is real and what is synthetic

| Part | Data | Real? |
|---|---|---|
| Real-data mode (`results/real_data.md`) | DROID `droid_100` (Franka Panda, 14 episodes / 2,551 frames), `jaco_play` (Kinova Jaco 2, 13 / 879), `nyu_rot` (xArm, all 14 / 440) | **REAL** teleoperation recordings |
| Benchmark v2 (`results/benchmark_v2.md`) | 300 simulated noisy episodes + 150 calibration episodes | SYNTHETIC |
| Timing-family self-test | 3 real nyu_rot episodes with **synthetic** timestamps added | unit test only |

**Where the real data comes from.** The Hugging Face hub (LeRobot datasets) was **not
reachable**: the environment's egress policy answers HTTP 403 for `huggingface.co`, `hf.co`
and the LFS CDNs. The public Open X-Embodiment bucket (`storage.googleapis.com/gresearch/robotics`)
was reachable, so `data/real_fetch.py` downloads RLDS/TFRecord shards (283 MB in total, below the
300 MB cap), decodes them with a small pure-Python TFRecord reader (no TensorFlow), drops the
camera images and writes a LeRobot-v2-style layout (`meta/info.json`, `episodes.jsonl`,
`tasks.jsonl`, per-episode parquet). Nothing is synthesised during conversion; in particular
RLDS has no per-step timestamps and none were invented. Shards were chosen by size to meet
the budget, which may bias the sample toward shorter episodes. Shard SHA-256s are in each
`meta/info.json` and passport.

## Real-data mode

`engine/real_mode.py` runs only what the data supports, in 13 check families: timing,
boundaries, numeric, frames, joint limits, motion, kinematics, action-state, gripper,
duplicate episodes, task string, outcome label, and semantic. Verdicts are PASS / REPAIR /
REJECT / UNKNOWN. Hard evidence means bit-level facts, declared or datasheet limits, or a
direct contradiction. Heuristic findings (robust-range outliers, assumed command semantics)
are reported as advisories and never change a verdict. Everything that needs object state
returns **UNKNOWN: "no object state in dataset"**. **No Z3 query is made in real-data mode;**
all real-data checks are numeric.

| Dataset | Episodes | Frames | PASS | REPAIR | REJECT | UNKNOWN | Structural baseline PASS / REJECT |
|---|---|---|---|---|---|---|---|
| droid_100 | 14 | 2,551 | 5 | 1 | 8 | 0 | 12 / 2 |
| jaco_play | 13 | 879 | 13 | 0 | 0 | 0 | 13 / 0 |
| nyu_rot | 14 | 440 | 14 | 0 | 0 | 0 | 14 / 0 |

Families UNKNOWN for 100% of episodes:
- **semantic:** all 3 datasets.
- **timing:** all 3 datasets, because there are no timestamps.
- **kinematics:** jaco_play (the kernel has no Jaco model) and nyu_rot (no joints).
- **joint limits** and **gripper:** nyu_rot.
- **frames:** nyu_rot. Its state is quantised, so repeated rows are expected.
- **outcome:** jaco_play and nyu_rot.

The full per-family table is in `results/real_data.md` and `figures/real_data_summary.png`.

Real findings (all in droid_100; figure `real_finding_example.png`):

1. **Commanded motion not executed.** Episode 3 (AUTOLab, labelled failure), frames 19-33:
   all 7 joints are bit-identical while the commanded joint position moves (median offset
   0.133 rad, commanded velocity up to about 0.6 rad/s). Frames 43-49 are fully duplicated
   rows. REJECT.
2. **Joint 6 beyond the Panda datasheet limit.** Episode 1 (TRI, labelled failure), frames
   141-172: joint 6 is above the Panda limit of 3.7525 rad, peaking at 3.959 rad (+207 mrad).
   The limit is an *external* datasheet value, not dataset metadata. A Franka FR3 allows
   4.52 rad, so this may be an arm-model mismatch rather than bad data. REJECT.
3. **Mis-documented action column.** The `action` field is documented as "[6x joint
   velocities, 1x gripper position]", but its first 6 values are bit-identical to the
   commanded **Cartesian position** in all 2,551 frames. This is a dataset-level schema
   finding.
4. **Missing language instructions.** 8 of 14 episodes have no instruction in any of the
   three instruction fields; 5 of them are labelled success. REJECT under the policy "no
   instruction, no language-conditioned use". Six of the eight droid_100 rejects are
   caused **only** by this policy. With that family set to advisory, droid_100 would have
   12 accepted and 2 rejected episodes.
5. **Whitespace anomaly.** "Put the  cable ..." has a double space. REPAIR (normalise).

Plus two positive checks:
- R-KIN-01 ran on every droid_100 frame. The recorded Cartesian position equals the kernel's
  Panda forward kinematics (flange) within 0.04 µm, which is float32 precision. This shows
  internal consistency of a derived channel, not physical truth.
- Outcome labels (recording folder vs final reward) agree in 14/14 episodes.

jaco_play and nyu_rot produced no hard findings. nyu_rot has advisories: idle tails
(14/14) and "commanded but no motion" steps (13/14), where a benign cause is contact with a
surface, which cannot be checked without object state. The structural baseline, run where
applicable, agrees with the engine on all shared checks (41/41). It disagrees on 6
accept/reject decisions, all in droid_100: the engine's rejects for missing tasks (5) and
the stuck-arm episode (1). The baseline has no such checks. Signed passports
`results/passport_real_<name>.json` cover each accepted split (6 / 13 / 14 episodes) and
verify offline. Each lists `checks_not_run` and `known_limitations`.

## Benchmark v2 (SYNTHETIC, noisy)

The sensor model has:
- joint encoder noise with σ ~ U(0.2°, 0.5°);
- TCP recorded as FK(noisy joints);
- 3 mm per-axis object-pose noise and 0.01 rad yaw noise;
- 0.5 mm gripper-width noise;
- ±5 ms timestamp jitter;
- one dropped frame in ~30% of episodes.

The data covers 3 task variants: mug to target (the v1 task), mug placed next to the laptop,
and an apple (class `fruit`) picked from a different start region. There are 3 object
classes per scene. The set has 20 episodes per error class (140), 20 valid failures and 140
clean. The error classes and magnitude ranges are the same as v1. **Strong baseline**
(`baseline/strong_rules.py`, what a good engineer writes in a week) = the structural checks
plus:
- a hand-coded phase order;
- contact-event pairing;
- gripper closed while in contact;
- max object speed, and resting objects stay put;
- table support with a fixed tolerance and a post-release grace window;
- class size ranges;
- held object keeps its distance to the TCP;
- yaw-aware box overlap;
- success means the object ends in the target.

It has no formal rulebook, no cross-rule reasoning, no REPAIR and no UNKNOWN. **Fair
calibration:** every checker's noise-sensitive tolerances start at their v1 values and are
widened ×1.25, rule by rule, until a disjoint calibration split (120 clean + 30 slip
episodes) has zero false rejects.

| Error class (n = 20) | Engine | Strong baseline | Structural baseline |
|---|---|---|---|
| (a) wrong object label | 55% | 55% | 0% |
| (b) impossible relation | 95% | 95% | 0% |
| (c) illegal phase order | 100% | 100% | 0% |
| (d) object teleport | 95% | 95% | 90% |
| (e) timestamp warp | 100% (all REPAIR, 20/20 byte-identical) | 100% (REJECT) | 100% (REJECT) |
| (f) joint-limit violation | 100% | 100% | 100% |
| (g) gripper/contact mismatch | 100% | 100% | 0% |
| **Recall** | **0.92 (129/140)** | **0.92 (129/140)** | 0.41 (58/140) |
| Precision | 1.00 | 1.00 | 1.00 |
| False rejects, 140 clean noisy episodes | 0% | 0% | 0% |
| Valid failures kept | 20/20 | 20/20 | 20/20 |
| ms / episode | ~14 | ~1.5 | ~0.6 |

- With its **uncalibrated v1 tolerances** the engine rejects 140/140 clean noisy episodes
  and 0/20 valid failures are kept. The v1 tolerances were only valid for noise-free data.
  Calibration widened them considerably (static 5 → 24 mm, co-move 10 → 60 mm, joint-speed
  margin ×1.95; see `results/benchmark_v2.md`).
- **On the original v1 noise-free set the strong baseline also reaches 0.90 recall**, the
  same as the engine, per class.
- The engine and the strong baseline catch *exactly the same* 129 episodes.

**Where the engine still wins, and why:**

- **Smaller detectable errors in a controlled magnitude sweep.** This uses the same error
  types, identical base episodes, and `figures/benchmark_v2_sensitivity.png`:
  - Laptop sinks: engine detects from 25 mm, strong baseline from 40 mm.
  - Post-release teleports: 30 mm (92%) vs 60 mm.
  - Post-release hovering: at 20 mm, 42% vs 17%.
  - Floating laptops and interpenetration: equal.

  Two causes:
  - **(i) The engine replaces a fixed post-release grace window with support and free-fall
    reasoning.** The strong baseline must stop checking a released object for 0.5 s to
    tolerate real falls. The engine knows whether the object is supported, and so whether it
    must be static. This is a genuine cross-rule effect.
  - **(ii) Rolling-median geometry lets the engine keep a tighter sink tolerance under
    noise.** A baseline could copy this.
- **Correct action.** The engine repairs the 20 timestamp warps back to the byte-identical
  recording; both baselines discard them. The engine returns UNKNOWN (not REJECT) when inputs
  are missing, and REPAIR for joint angles logged in degrees.
- **Traceability.** Every finding cites a rule id and frame. The rulebook is hashed into the
  passport. The calibrated rulebook still passes the Z3 self-check
  (`results/rulebook_selfcheck_v2_profile.json`). The strong baseline's checks also name a
  check and a frame, but they are not versioned or consistency-checked.

**Where it does not win:**
- Recall on the seven injected classes: tie.
- Wrong labels whose boxes fit the wrong class: both miss 9/20.
- Runtime: the engine is ~10× slower than the strong baseline.

## Claims fixed

- **Z3 vs numeric (exact, `results/rule_encoding_counts.json`).** 30 rules in total:
  - **9 are decided per episode by a Z3 query:** R-QTY-01/02, R-TYPE-02, R-PHASE-01..04,
    R-CONT-01/02.
  - **15 more are Z3-encoded only in the rulebook self-check.** They are evaluated per
    episode with numpy against the same constants.
  - **6 are numeric-only:** R-PROV-01, R-TYPE-01, R-TYPE-03, R-KIN-01, R-CONT-03, R-SUP-02.

  So 24 rules are Z3-encoded in total. The rulebook's `kind` column says 23/7 because
  R-TIME-01 is labelled "numeric" but is encoded in the self-check. The label is left
  unchanged so that the v1 rulebook hash and passport stay valid.
- **Passport `known_limitations`.** The v2 and real passports carry a `known_limitations`
  field; real passports also carry `checks_not_run`.
- **Undetected errors in the accepted split.** The engine accepts 191 of the 300 v2
  episodes. **Evaluation-only:** 11 of them are known from the injection key to contain an
  undetected injected error:
  - 9 wrong labels;
  - 1 hover of 11 mm;
  - 1 teleport of 34 mm.

  (The 20 repaired timestamp warps are accepted in repaired, byte-identical form.) The
  passport cannot know this number and does not contain it.

## v2 limitations

- **Real data is small and partial:** 41 episodes from 3 datasets. Only low-level checks
  can run. Semantic checks, which are the reason the rulebook exists, returned UNKNOWN on
  100% of real episodes, and timing checks could not run because of missing timestamps.
- The real-data REJECT policy for empty instructions is a choice. Several thresholds (stuck
  arm: > 0.02 rad commanded, < 1e-4 rad/frame observed, ≥ 1 s) and the Panda datasheet
  limits are ours, not the datasets'.
- The v2 benchmark is still SYNTHETIC, still one simulated arm, and still injected by the
  team that wrote the engine and the strong baseline. The strong baseline was also written
  by us, after the engine; a different engineer might write a weaker or stronger one.
- Calibration to zero false rejects on 150 episodes does not bound the false-reject rate
  on other data. The resulting tolerances are wide: co-move is 60 mm.
