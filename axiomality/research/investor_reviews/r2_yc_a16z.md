# AXIOMALITY deck v2: YC + a16z review (2026-09-26)

## 1. Scores
- **YC, fund at interview: 5/10.** Strong, honest founders and a real prototype, but zero users. YC already backs Shotwell and Instance next door.
- **a16z, take to partner meeting: 3/10.** Empty category and a real neutrality argument. But no design partner, a $5M pool today, and free Cosmos Evaluator in the slot.

## 2. Prototype credibility: PARTLY
**What holds up.** The code runs, is seeded and reproduces. Neither checker reads the injection key. The baseline gets the same limits and v_max. The README discloses misses and limits.

**Why it is not yet evidence:**
- One team wrote simulator, injector, engine and tolerances.
- Trajectories are noise-free: TCP is exact FK of the joints; the only noise is ±1 ms timestamp jitter.
- The engine reads ground-truth object poses, box sizes, contact events and phase labels. Most real LeRobot/DROID data lacks these, so it would get UNKNOWN.
- 4 of 7 error classes are semantic, and the baseline was specified not to check them, so 90 vs 40 is largely by construction.
- One scene, one task, one arm.
- The baseline also keeps 10/10 valid failures.
- The passport signs over 7 missed corrupted episodes, which the deck never mentions.

**Overstatements** (replacement copy in §4):
- Slide 4 "Drop in a dataset" (#1)
- Slide 12 "Bring a dataset; watch a real passport get issued" (#2)
- Slides 1/5 "rules alone catch 40%": the engine is also rules (#4)
- Slide 10 "0 false rejects; every valid failure kept" (#5)
- Slide 10 "30-rule rulebook, self-checked contradiction-free with Z3": only 24 are in Z3 (#8)
- Slide 6 "The next customer's identical error is caught on day one": not built (#9)
- Slide 1 "flip one byte" (#10)
- Slide 10 "run engine and baseline blind" (#12)

## 3. Top 3 pass reasons
**1. No pull.** No users, pilots or LOIs, and no proof vendors will pay to be graded.
- *Copy now:* #6.
- *90 days:* one paid pilot or two unpaid bake-offs on real vendor batches, plus one lab procurement lead who agrees in writing to accept passports at intake.

**2. Real-data gap.** The engine needs scene state that real data lacks. The video-to-state perception layer is unbuilt. Real-data false-reject rate and policy impact are unknown.
- *Copy now:* #1, #2, #5.
- *90 days:* DROID/LeRobot rerun with published UNKNOWN rate, false-reject rate and review hours; one filter-vs-no-filter policy run; hire the robot-learning lead.

**3. Market and moat.** $5M pool today, an unproven 5–8% take, free Cosmos, and Applied Intuition could add this.
- *Copy now:* #11; label slide 8's take rate "hypothesis the pilots test".
- *90 days:* a price a vendor has actually quoted, and a head-to-head against Cosmos with a third party holding the key.

## 4. Edits (highest impact first)
| # | Slide | Current | New |
|---|---|---|---|
| 1 | 4 | Drop in a dataset; get a verdict per episode and a signed passport | Give us episodes with object poses, contact events and phase labels; get a verdict per episode and a signed passport. Missing inputs return UNKNOWN. |
| 2 | 12 | Bring a dataset; watch a real passport get issued, then tampered with and rejected | Corrupt any of our 200 episodes yourself; watch the verdict, then the passport, change |
| 3 | 5 | …53 were rejected. | …53 were rejected. 7 accepted episodes hold an injected error we missed; a passport records which checks ran, not that data is correct. |
| 4 | 5 | …rules alone catch 40% / seeded from real scan geometry | …structural checks alone catch 40% / one real scanned scene (mug, laptop), one task, one simulated arm, noise-free trajectories |
| 5 | 10 | 90% of injected errors caught vs 40% for rules alone; 0 false rejects; every valid failure kept | Synthetic, noise-free: 90% vs 40% for structural checks; 0 false rejects. Real-data false-reject rate is the Dec 31 test. |
| 6 | 9 | Accounts are targets… none is a customer or partner today. | Add, true numbers only: "Conversations to date: [n] vendors, [m] labs; [k] agreed to a bake-off." If k = 0, say so. |
| 7 | 2 | ≈ 0 direct reuse of action data across robot embodiments | 48% of teams cite data-quality problems (Voxel51, 2026). (OXE showed positive transfer; current stat invites attack.) |
| 8 | 6 | 30 rules… Z3 finds a model satisfying every rule | 30 rules; 24 encoded in Z3, and a bounded 14-frame model satisfies all 24 (success and slip); 6 checked numerically |
| 9 | 6 | Rejects are clustered… caught on day one. | Planned, not in prototype: rejects cluster into candidate rules, each proven consistent before release. |
| 10 | 1 | flip one byte and verification fails | change one label or shift one timestamp 1 ms and verification fails |
| 11 | 6 | Re-checkable by a third party: No | Re-runnable with the same weights; no rule-level reason |
| 12 | 10 | run engine and baseline blind | run engine and baseline; neither reads the injection key |

## 5. After edits
- **YC: 6/10.** No diligence traps left; the prototype reads as unusually honest. Getting to 7+ needs a real vendor yes.
- **a16z: 4/10.** Credibility is up, but pull and market size are unchanged. A partner meeting needs two named design partners and a real-data rerun.
