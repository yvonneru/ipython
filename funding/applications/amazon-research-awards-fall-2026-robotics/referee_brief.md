# Brief for the PI and the Theme 3 advisor — Amazon Research Awards, Fall 2026

**ARA takes no reference letters.** There is no referee component in this program; the people whose input decides the application are the PI (Prof. Grüninger), who submits it and whose one-page CV is scored, and the U of T Robotics Institute faculty member who advises on Theme 3. This brief is for them. [Brackets] to confirm.

## What the program is

Amazon Research Awards give a **one-time unrestricted cash gift to the PI's institution plus AWS Promotional Credits** for a 12-month project on a topic named in a call for proposals. The Fall 2025 call advertised up to USD 100,000; the Fall 2026 ceiling and cash/credit split will be stated in the call text [confirm ~1 Oct 2026]. The FAQ says the cash is "generally anticipated to support one to two graduate students or a post-doctoral researcher for one year, plus some conference travel and equipment." Amazon has historically claimed no IP and expected open publication [confirm 2026 terms]. Decisions come about three months after the close.

Only a full-time faculty member can be PI. Dr. Ru, as a postdoctoral researcher, is named as the funded researcher on the PI's proposal; the research program is Dr. Ru's own (verified mereological ontologies for object–part representation in physical AI), complementary to and drawing on the laboratory's COLORE, TUpper and PSL infrastructure.

## What the form asks

A proposal of at most 3 pages (per the general template; some 2026 calls allow 4 — [confirm]) with the headings *Abstract and Keywords; Significance of the research and prior work; Technical approach; Milestones with timeline estimates (datasets, code releases, technical reports)*, plus a **one-page PI CV** listing only the 5–6 most relevant papers. Budget (cash and credits) is entered in the portal. The PI submits.

What is needed from the PI:
1. Agreement to be PI and to host Dr. Ru from [April 2027 or later] — by 10 Oct 2026.
2. The one-page CV (statement.md, Part A): rank and appointments, 5–6 papers, exact citations for FOUnt (FOIS 2018) and the mereotopology and TAMP papers, and the published lab papers to replace bibliography entry 14 — by 24 Oct 2026.
3. Approval, sentence by sentence, of everything the proposal says in the PI's voice (§1 first bullet; §2 methodology sentence; §4).
4. Choice of call topic once posted (Robotics vs Automated Reasoning) and of the matching abstract sentence.
5. Name of the Robotics Institute advisor, and of the MASc student slot (MASc1) if one is to be funded.

What is needed from the Theme 3 advisor:
1. Agreement to be named; policy backbone (part-aware manipulation policy) and second simulator alongside SAPIEN.
2. GPU instance types and hours for the H1–H3 experiments, to size the AWS-credit request.

## What reviewers score

ARA publishes no rubric. From the template and past calls, reviewers read for: significance and novelty against prior work; a technical approach that is sound and completable in 12 months; **relevance to the call topic and to Amazon** (each call lists research areas of interest — the abstract should echo two or three phrases from the Fall 2026 list); PI track record; and open outputs (datasets, code, technical reports) with sensible use of AWS credits.

## The four points that help most

1. **The audit has never been done.** No part-level robot dataset — PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World — has been checked against any formal specification of parthood; the proposal produces the first quantitative measurement and releases corrected annotations and a merged corpus. If the PI's CV or team text can say that the laboratory's ontological analysis of ShapeNet/PartNet is the direct precursor, the novelty claim is anchored.
2. **Automated reasoning at data scale, honestly.** The two-tier checker (Datalog/SMT bulk tier; Prover9/Mace4 residual tier) reports UNKNOWN and timeout as first-class outputs, and the M6 decision point tests whether the compiled fragment misses what the prover finds. This is the sentence an Automated Reasoning reviewer wants to see.
3. **A theorem, not a convention, behind the cross-dataset schema.** Dr. Ru's constitution-mapping theory (two Synthese submissions with the PI) states exactly when two part decompositions are compatible; cross-dataset label mappings are proved meaning-preserving. A Robotics reviewer sees a cross-embodiment part schema with a consistency guarantee and a deployable failure signal (ontology-violation rate).
4. **Feasibility.** The verification tools exist in the PI's laboratory today; Dr. Ru has shipped ontology-governed data pipelines in production; the 12-month plan has releases at M4, M8 and M12 and two decision points.

## Deadline

Expected Fall 2026 close **~12 Nov 2026, 11:59 PM PT [confirm on the call page ~1 Oct]**. Internal targets: PI agreement 10 Oct; PI CV and approvals 24 Oct; institutional sign-off (if U of T requires one) ~30 Oct; PI submits ~5–9 Nov. If the Fall 2026 topics do not fit, the same package goes to the Spring 2027 call (~25 Mar – mid-May 2027).
