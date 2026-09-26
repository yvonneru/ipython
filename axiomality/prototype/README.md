# AXIOMALITY evidence-layer prototype

This is a small, working prototype of the AXIOMALITY verification engine. It checks
robot-episode data against a formal rulebook (the "knowledge kernel", written as Z3
axioms) plus kinematic and physics checks. For each episode it returns
**PASS / REPAIR / REJECT / UNKNOWN**, and each finding names a rule ID and a frame.
The engine then issues an **Ed25519-signed Data Passport** that anyone can verify
offline.

> **All episode data here is SYNTHETIC.** The only real input is the scene geometry of
> AXIOMALITY sample 109 (`pointclouds/109.ply`: one mug and one laptop, with measured
> boxes). The episodes are simulated around that scene, the errors are injected by us,
> and the results are internal-prototype numbers. They are not field results.

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
