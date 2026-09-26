# Budget and timeline — Princeton Presidential Postdoctoral Research Fellows Program

## Money
No budget is requested or scored. The fellowship provides an annual salary of **[USD 75,000 — figure from a Princeton laboratory's page for a prior cycle; the registry estimated USD 70,000–80,000; verify on the current call]** plus benefits and **support for computing, professional development and research** [amounts not published in the sources found — verify], for a **one-year appointment renewable for a second year** (full salary for up to two years), starting [1 July – 1 September] 2027. [Verify whether unspent funds roll over and whether relocation is covered.] The plan below shows how the research/computing support would be used; it is indicative and does not appear in the nomination unless the call asks for it.

| Year | Use of the research and computing support (indicative; scale to the actual amount) | Priority order |
|---|---|---|
| Y1 | Compute for the audit pipeline and first simulation runs [confirm whether the sponsor group's cluster or a Princeton research-computing allocation is available; if so, reallocate to travel]; one ISO/IEC JTC 1/SC 32 meeting; one conference (FOIS or a robotics venue) | compute > SC 32 > conference |
| Y2 | Compute for policy-training experiments (SAPIEN + second simulator); two conferences (one ML/robotics — CoRL/ICRA/RSS class — and one KR/ontology venue); open-source release costs (DOI, hosting); job-market travel | compute > conferences > release > job market |

No salary is requested for anyone other than the fellow. Undergraduate researchers, if any, are funded through Princeton's own independent-work and summer research programs [confirm what the sponsor's department offers].

## Milestone timeline (24 months, start September 2027)

| Months | Theme | Milestone | Deliverable / evidence |
|---|---|---|---|
| 1–3 | 1 | Competency questions extracted from the annotation schemas of PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment and DROID | Competency-question set; dataset adapters (LeRobot, RLDS, ROS 2/MCAP, USD/PLY/JSON) [reuse; confirm which are already built] |
| 1–8 | 1 | Parts ontology: rigid, articulated, functional and assembly modules in Common Logic, verified (consistency, non-triviality, representation theorems) with Prover9/Mace4 | Modules released to COLORE; verification log |
| 4–8 | 1 | Constitution mappings between the four modules; PSL integration for parthood change under manipulation | Theorems on compatibility of decompositions; **Y1 question: is every dataset hierarchy a model of at least one module?** |
| 6–12 | 2 | Two-tier audit pipeline (Datalog/SMT bulk tier, first-order prover tier); first audit of all seven datasets | **First quantitative measurement of parthood consistency in robot datasets**; audit/data paper submitted (end of Y1 — the renewal case) |
| 10–16 | 2 | Cross-dataset label mappings proven meaning-preserving; corrected annotations; merged ontology-aligned corpus | Public data release with DOI; audit toolkit v1; Y2 workshop for students (month 12–14) |
| 12–18 | 3 | Differentiable relaxations of parthood constraints as auxiliary losses; constraint-guided augmentation | Training code; pilot results on held-out PartNet-Mobility categories in SAPIEN |
| 16–24 | 3 | Verification-in-the-loop evaluation protocol; full simulation study with confidence intervals and ablations by axiom family; real-robot replication on [sponsor group's platform] if available in months 20–24 | **Y2 questions: does ontology-consistent training improve generalization? does violation rate predict failure?**; methods paper submitted to an ML or robotics venue |
| 18–24 | 1–3 | Contribution of the parts ontology to ISO/IEC JTC 1/SC 32 [confirm mechanism — new work item or amendment]; consolidated open release; faculty job market | SC 32 contribution document; final release; job applications |
| beyond | 2–3 | Second hierarchical-annotation domain (CAD assemblies); cross-embodiment transfer on pooled, aligned data | Continued with the sponsor's group or from the fellow's next position |

Community milestones from the contributions text run alongside: undergraduate independent-work projects each year; the parts-and-wholes reading group from month 3; the audit-tooling workshop after toolkit v1 (month 12–14).

## Internal deadlines for this nomination
| Date | Item |
|---|---|
| 26 Sept 2026 | Read the DOF page and the September call; confirm the deadline (13 Nov 2026), materials, whether a candidate contributions statement is required, letter mechanism; email the program (emails.md, email 1) |
| 26 Sept – 2 Oct 2026 | Contact candidate sponsors (emails.md, email 2) — ask whether they would *nominate*; each sponsor may nominate only one candidate |
| 16 Oct 2026 | Sponsor committed (STRATEGY.md go/no-go); complete draft (research statement, contributions text, CV, nominator brief) to the sponsor and the three referees |
| 6 Nov 2026 | Referee letters in (internal date); sponsor's nomination letter drafted |
| 10 Nov 2026 | Sponsor submits the nomination with all materials (three days early) |
| 13 Nov 2026 | Program deadline — all nominations and materials received [verify time of day and time zone on the call] |
| [winter/spring 2027] | Expected notification [verify; prior cohorts were announced publicly in September/October of the start year] |
| [1 Jul – 1 Sept] 2027 | Start |
| **If no sponsor commits by 16 Oct 2026** | Drop this cycle; keep the relationship warm; re-check the DOF page on 1 Sept 2027 for the 2028 cohort (requirements-met March 2025 ≈ 3.5 years at a Sept 2028 start, inside a 4-year window [confirm the rule still reads "within 4 years of the start date"]) |
