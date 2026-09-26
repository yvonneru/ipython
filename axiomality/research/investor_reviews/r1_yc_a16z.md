# AXIOMALITY US seed deck: YC + a16z review (2026-09-26)

## 1. Scores
- **YC "fund at interview": 4/10 now, ~6/10 re-cut.** The founders are strong and the category is empty. But there are no users, the pitch is about an ontology when it should be about a job someone pays for, and YC already backs three neighbours (Instance, Shotwell, One Robot).
- **a16z "take to partner meeting": 2/10 now, ~4/10 re-cut.** The $12–60M sizing reads as a feature, Cosmos Evaluator is free, and the compliance-led why-now plus China touchpoints clash with American Dynamism. It becomes a meeting once a named vendor or buyer runs passports.

## 2. Direction: narrow
- **A. Acceptance testing for robot-data sales, the inspection layer between vendors (Scale, Mecka, Build AI, XDOF) and the labs buying from them. PICK.** This is real seller/buyer information asymmetry. It is the only setting where a signature matters, and it grows with data spend.
- **B. Evals and data-debugging for model teams.** Crowded (Instance, Shotwell, One Robot, Voxel51, Encord, Foxglove), and labs build it themselves. It becomes the report inside A.
- **C. Verifying synthetic / world-model data.** Cosmos Evaluator is free and NVIDIA owns the pipeline. Expansion in year 2 (synthetic suppliers are vendors too).
- **D. Compliance evidence for OEMs.** Obligations start in 2028 and are conditional, and it's the wrong tone for a16z. It becomes a free by-product of A, worth one line.

**Why A:** a lab's internal QA doesn't need a signature. A $500M vendor selling to an $11B lab does. A also changes the market story from "200 orgs × $200k" to a cut of robot-data transactions.

- **One-liner (14 words):** "We inspect robot training data before labs pay for it, and sign the result."
- **Analogy:** "**Vanta for robot data vendors.** The report that closes the data deal." It is seller-paid and buyer-trusted, and Vanta is a YC company. For a16z: "the inspection layer of the robot-data market." Avoid Foretellix: it just cut 18% of staff, citing slow demand for validation tools.

## 3. Slide plan (12 slides, no ask)
1. **"We inspect robot training data before labs pay for it."** The one-liner and a real prototype passport card. Move ISO and patents to slide 11.
2. **"Labs buy robot data blind; vendors can't prove what they sold."** Voxel51: 89% blame data. 58k LeRobot datasets, none validated. Teleop at $50–200/h with no usability record. Acceptance today means a video plus a spot check. Delete the unattributed quotes unless they come from real, dated interviews.
3. **"Robot data became a traded commodity in 2026, with no inspector."** Mecka (~$500M, in talks with Sequoia), XDOF $1.2B, Build AI (1M free hours), Scale (150k h, neutrality questioned post-Meta). Generators (Atlas, Cosmos) flood training. $18.6B Q2 physical-AI funding. EU 2028 as a footnote.
4. **"Drop in a dataset; get a per-episode verdict and a signed passport."** LeRobot/RLDS/MCAP in. Three plain checks: is the motion possible, does the story contradict itself, is the provenance intact. Accept/repair/reject with frame-level evidence. Valid failures are kept. Anyone can verify offline.
5. **DEMO: "Working prototype catches [N] error classes a rules-only baseline misses."** Fill in with prototype numbers only.
   - Per-class recall/precision, Engine vs. rules-only, across the 7 injected classes.
   - False-reject rate on clean episodes.
   - Valid-failure retention.
   - Z3 self-check catching a contradictory rule.
   - Verify ✓ → flip a byte → ✗.
   - Label: "Internal, synthetic: 200 episodes seeded from real scan geometry."
   - Show any ties honestly. If the engine wins on no class, the headline becomes "Signed, tamper-evident acceptance in one command."
6. **"Our rulebook is checked for contradictions before it checks your data."** One episode with the three checks overlaid. Contrast: a VLM judge gives a plausibility score, we give a re-checkable trail. Cut the cost curve and "compiled twice."
7. **"Everyone scores data; nobody signs a neutral per-episode verdict."** A 2×2 (neutral vs. self/vendor; signed evidence vs. score) placing Cosmos Evaluator, Dana, Instance/Shotwell, Pebblous and Foxglove/LeRobot (rails we plug into). Delete the ● matrix.
8. **"Vendors pay per certified dataset; buyers verify for free."** Per-hour or per-episode pricing. Paid pilot $25–50k. A sourced take-rate model, labelled as a model. Drop the royalty and guardrail lines.
9. **"Start with challenger vendors who need to beat Scale on trust."** 10 named targets, marked as targets. The buyer is the vendor's head of data ops. Blind bake-off on their batch against their own scripts. Then one lab accepts passports at intake.
10. **"What's built, and three things you can check by Dec 31."** Built: prototype, machine-checked kernel, 100k measured 3D packages (as capture capability), 13 patents. By Dec 31: (a) passports on one vendor's real data under NDA; (b) public spec + verifier + a passport for an open dataset; (c) the benchmark on DROID/LeRobot data, with Cosmos Evaluator added as a baseline and a third party holding the injection key.
11. **"People who write machine-checked rulebooks, plus people who've shipped at scale."** CEO: the documented ISO/IEC 21838-4 role and >$50M year-one revenue. CTO: AI PhD, chief scientist. Perception lead: ex-XPeng. Say plainly that a VLA-trained robot-learning lead is being hired now, and name an advisor if one exists.
12. **"Every robot dataset that changes hands ships with a passport."** Path: vendors → buyer intake → synthetic suppliers → OEM evidence. Ask for introductions to one vendor and one lab procurement lead, and offer a 12-minute session on the investor's own data.

## 4. Five likely pass reasons
1. **"Nobody uses it."** Answer with the Slide 5 demo and the dated, checkable Dec-31 commitments. Report pipeline as counts ("N vendor calls, M samples received"), never "partners."
2. **"NVIDIA or Applied will ship it as a feature."** Neutrality plus the signature is something a stack vendor can't credibly offer. Show error classes that learned judges miss. Add Cosmos Evaluator as a baseline and treat it as an upstream input.
3. **"Labs build QA in-house; vendors won't be graded."** Sell into the asymmetry: challenger vendors want an edge on Scale, and buyers get leverage for free. Aim for one vendor live within 90 days.
4. **"Can we trust the signer?"** For a16z American Dynamism, remove the Beijing data-exchange licence, GB/Z and the China humanoid forecast. State the entity and where data resides, and note the verifier runs inside the customer's environment. Name the robot-learning hiring gap.
5. **"Too small or compliance-driven."** Size the market on data-transaction volume and put compliance in a footnote.

## 5. Phrase fixes
- "train on evidence instead of assumptions" → "know what they bought before they train on it."
- "Value is moving from hours to evidence; the evidence format becomes the unit of trade" → "Robot data is now bought and sold; nobody inspects it."
- The sample passport values (96.4%, 99.1%, 0.94, "ISO 13482-derived · 0 violations", "EU Art. 10/12") look like results and overclaim conformity → show the real prototype passport, labelled synthetic.
- "One rulebook, compiled twice…" → cut (it is not a theorem).
- "competitors cannot download" → "every confirmed failure becomes a checked rule we keep."
- "$60 → $12 / h", "< $5 / h" → cut until real batch economics exist.
- "Nobody sells…" / "0 vendors selling a certificate" is false (Pebblous and CertifiedData exist) → "No one signs per-episode physics + logic checks for robot data."
- A ● in every cell of our column → show only what the prototype demonstrates.
- "Separate bookings, commitments, credits and cash…", "Renewal is the proof, not the model" → "Vendors pay per certified dataset."
- "the pilot is designed to be falsifiable; we pre-register…" → "Blind bake-off on your data against your current scripts."
- "What exists today is assets and relationships" → "What's built, and what you can check by Dec 31."
- The unnamed law firm / Big Four / pharma relationships → cut.
- "we co-wrote the standard, we proved it consistent" → state the documented role exactly. The public TUpper axioms are credited to the Toronto lab under CC BY-SA, so clear the licence.
