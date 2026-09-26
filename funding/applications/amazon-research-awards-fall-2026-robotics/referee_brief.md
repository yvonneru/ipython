# Brief for the PI and the Theme 3 advisor — Amazon Research Awards, Fall 2026

**ARA takes no reference letters.** There is no referee component in this program; the people whose input decides the application are the PI (Prof. Grüninger), who submits it and whose one-page CV is scored, and the U of T Robotics Institute faculty member who advises on Theme 3. This brief is for them. [Brackets] to confirm.

## What the program is

Amazon Research Awards give a **one-time unrestricted cash gift to the PI's institution plus AWS Promotional Credits** for a 12-month project on a topic named in a call for proposals. The Fall 2025 call advertised up to USD 100,000; the Spring 2026 Robotics call split this as up to USD 50,000 cash plus up to USD 50,000 credits [third-party listing — verify]; the Fall 2026 caps will be stated in the call text [confirm ~1 Oct 2026]. A USD 50,000 cash cap does not cover a full postdoc year plus a MASc student, so the budget offers two options (budget_and_timeline.md). The FAQ says the cash is "generally anticipated to support one to two graduate students or a post-doctoral researcher for one year, plus some conference travel and equipment." Amazon has historically claimed no IP and expected open publication [confirm 2026 terms]. Decisions come about three months after the close.

Only a full-time faculty member can be PI. Dr. Ru, as a postdoctoral researcher, is named as the funded researcher on the PI's proposal; the research program is Dr. Ru's own (verified mereological ontologies for object–part representation in physical AI), complementary to and drawing on the laboratory's COLORE, TUpper and PSL infrastructure.

## What the form asks

A proposal of at most 3 pages (per the general template; some 2026 calls allow 4 — [confirm]) with the headings *Abstract and Keywords; Significance of the research and prior work; Technical approach; Milestones with timeline estimates (datasets, code releases, technical reports)*, plus a **one-page PI CV** listing only the 5–6 most relevant papers. Budget (cash and credits) is entered in the portal. The PI submits.

What is needed from the PI (STRATEGY.md lists this call as skip-by-default in favour of Spring 2027; the asks below apply only if the PI opts in, and none falls in the CPRA week or the 30 Oct – 3 Nov RAC week):
1. Yes/no in principle to being PI and to hosting Dr. Ru from [June 2027 or later] — by Fri 9 Oct 2026 (with the RAC decision). No answer means Spring 2027.
2. The one-page CV (statement.md, Part A): rank and appointments, 5–6 papers, exact citations for FOUnt (FOIS 2018; bibliography entry 14) and the mereotopology and TAMP papers — by Wed 21 Oct 2026.
3. Approval, sentence by sentence, of everything the proposal says in the PI's voice (§1 first bullet, including the Discovery-grant distinction; §2 methodology sentence; §4) — by Wed 21 Oct.
4. Choice of call topic once posted and of the matching abstract sentence (Robotics is the better fit; see below).
5. Name of the Robotics Institute advisor, and whether the laboratory funds the MASc student (budget Option A) or the award does (Option B).

What is needed from the Theme 3 advisor:
1. Agreement to be named; policy backbone (part-aware manipulation policy) and second simulator alongside SAPIEN.
2. GPU instance types and hours for the H1–H3 experiments, to size the AWS-credit request.

## What reviewers score

ARA publishes no weighted rubric. The Spring 2026 call text (confirmed by search 2026-09-26) states that proposals are reviewed for **scientific quality and novelty, technical feasibility, creativity, potential for real-world impact at scale, and readiness to deliver meaningful outcomes** [verify the Fall 2026 wording]. Reviewers also read for fit to the call's listed topics, PI track record (the one-page CV), and open outputs with sensible use of AWS credits.

**Topic fit.** The Spring 2026 Robotics call listed AI for Robotics and HRI, Manipulation in Cluttered and Unstructured Environments, and Perception and Computer Vision for Robotics among its topics — this proposal fits the first three at the level of data and evaluation, not new manipulation hardware or control. The Fall 2025 Automated Reasoning call was about reasoning over computing systems (LLM–solver interfaces, auto-formalization of system specifications including detecting ambiguity, vacuity and inconsistency, SAT/SMT quantifier reasoning, static analysis, Lean foundations); a data-quality audit fits only through the inconsistency/vacuity and quantifier-reasoning topics and would be read as peripheral. Prefer Robotics; submit to Automated Reasoning only if its Fall 2026 text names specification consistency or data.

## The four points that help most

1. **The audit has not, to our knowledge, been done.** We know of no part-level robot dataset — PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World — checked against an axiomatized theory of parthood; §1 now contrasts this with statistical label-error auditing (confident learning), robot knowledge bases (KnowRob, IEEE 1872) and semantic-loss training, so the novelty claim is argued rather than asserted. The proposal measures violation rates, adjudicates a sample for audit precision, and releases corrected annotations (as licence-safe patches) and proved cross-dataset mappings. The PI's Discovery program poses the ShapeNet/PartNet mereotopology question as open work, not as a published result, and the proposal says so; **the PI should confirm that the distinction drawn in §1 (Discovery asks the question; ARA funds the audit at data scale and the learning experiments) is one he is comfortable stating**, because a reviewer who sees the two as the same project will read the ARA request as double funding.
2. **Automated reasoning at data scale, honestly.** The two-tier checker (Datalog/SMT bulk tier; Prover9/Mace4 residual tier) reports UNKNOWN and timeout as first-class outputs, and the M6 decision point tests whether the compiled fragment misses what the prover finds. This is the sentence an Automated Reasoning reviewer wants to see.
3. **A theorem, not a convention, behind the cross-dataset schema.** Dr. Ru's constitution-mapping theory (two Synthese submissions with the PI) states exactly when two part decompositions are compatible; cross-dataset label mappings are proved meaning-preserving. A Robotics reviewer sees a cross-embodiment part schema with a consistency guarantee and a deployable failure signal (ontology-violation rate).
4. **Feasibility.** The verification tools exist in the PI's laboratory today; Dr. Ru builds ontology-based representations of objects and indoor environments at Uing Technologies; the 12-month plan has releases at M4, M9 and M12, two decision points, success measures for each theme, and Theme 3 scoped as a months-8–12 pilot that shrinks to H2 (no retraining) if the audit runs late. The remaining feasibility questions a reviewer will ask — dataset licences, GPU sizing, a measured SMT check time, and whether one postdoc plus one MASc can carry three themes — need the advisor's numbers, a licence check and a one-category pilot before submission.

## Deadline

Expected Fall 2026 close **~Thu 12 Nov 2026, 11:59 PM PT [confirm on the call page ~1 Oct]**. Internal targets: PI yes/no 9 Oct; PI CV and approvals 21 Oct; package to Research Services 26 Oct; institutional sign-off (if U of T requires one) ~29 Oct; PI submits ~5–9 Nov. If the Fall 2026 topics do not fit, the same package goes to the Spring 2027 call (~25 Mar – mid-May 2027).
