# US partner score: AXIOMALITY v3 (2026-09-26)

## 1. Scores
- **YC: 5/10.** Honest deck, strong formal-methods founder, working prototype. But nobody has asked for it yet, YC already backs Shotwell and Instance here, and the team has no robot-learning operator.
- **a16z infra: 3/10.** By the deck's own evidence the moat is not visible: recall ties our own baseline, real-data mode runs no Z3 (`z3_in_loop: false`), and the largest pool on slide 9 is $120M.

## 2. Overstatements diligence would catch
1. **S1/S11** "change one label or one timestamp and verification fails" / "change any field". The real data has no timestamps, video is not covered and the key is a demo key. → "Change any covered value and verification fails (video not yet covered; demo key)."
2. **S5** "the prototype found three real problems". The joint-limit finding may be an FR3 arm, not bad data. → "Numeric checks flagged a stuck arm, a mis-documented field and a possible arm mismatch."
3. **S4** "Three checks run on every episode". The semantic family was UNKNOWN on 100% of real episodes. → "Three check families; on today's public data only the first can run."
4. **S7** "Our rulebook is checked for contradictions before it checks your data". The proof covers a bounded 14-frame 1-D abstraction, and Z3 decides 9 rules per episode on synthetic data only. → "24 rules proven jointly consistent on a bounded model; 9 decided by Z3 on synthetic data."
5. **S6** "a week of hand-written rules" and "Every verdict cites a rule". We wrote the baseline after the engine, and it also cites a check ID and frame. → "our own strong baseline, written after the engine"; "cites a *versioned, hash-bound* rule".
6. **S3** "PI, Skild, Generalist, Figure all buy data" / "need a neutral referee". Several collect in-house and no buyer is quoted. → "spend heavily on data"; "Our hypothesis: buyers want a neutral referee." On S2, label the Voxel51 stats as visual-AI teams.

## 3. Highest-impact edits
| Slide | Current | New |
|---|---|---|
| 1 | "…the inspection report that closes the data deal." | "The inspection record a lab accepts at intake. Prototype on public data; no customers yet." |
| 4 | Three families shown as equally live | Add "Next: derive object state from video (perception lead) so families 2–3 run on real data." |
| 5 | Findings only | Add "Could a script find these? Yes. We add doing it on every batch, signing it, and listing what we couldn't check." |
| 6 | "equal recall, finer detection, exact repair" | "Checks are copyable; a neutral signed record is not." Halve the slide. |
| 7 | ISO ontology stack | Move to appendix. Replace with "Versioned, hash-bound, consistency-checked rules: anyone can re-derive a verdict." |
| 8 | "A lab's own QA needs no signature." | This conflicts with slide 9. Choose: cross-party trades only (small market), or the intake gate for *all* training data. |
| 9 | Pool table topping at $120M | Add "Third-party inspection alone is $5–120M; venture scale needs intake-gating of in-house and synthetic data, which the lab bake-off tests." |
| 11/13 | "Passports on one vendor's real data under NDA" | "By Dec 31: one paid pilot or LOI, and one lab's written intake requirement." State the discovery calls made so far, even if zero. |

## 4. Ceiling and path to yes
**Ceiling without new facts: YC 6, a16z 4.** Missing: evidence of demand, and a moat visible on real data.

**YC (90 days)**
1. Hold 30+ calls with vendor data-ops and lab intake leads, and convert them into 1 paid pilot ($25k+) or 2 LOIs.
2. Run the blind bake-off on one vendor's real batch and publish it, ties included.
3. Put the founders full-time in the US and close the robot-learning lead.

**a16z (90 days)**
1. Get one lab to state in writing that it will accept or require passports at intake. That buyer pull is what makes it Vanta-like.
2. Get the semantic checks running on real DROID video. Beat the strong baseline and Cosmos Evaluator by at least 10 points on a set whose key a third party holds.
3. Measure the defect rate and cost on a real paid batch, publish the verifier, and get one host (LeRobot, Foxglove or Rerun) to show the badge.
