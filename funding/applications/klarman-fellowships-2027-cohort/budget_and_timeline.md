# Budget and timeline — Klarman Fellowships, 2027 cohort

## Money
No budget is requested or scored. The fellowship provides (registry, deadline confidence high): a stipend of **USD 80,000 per year** plus benefits, and **USD 12,000 per year in research funds**, for up to three years, start between 1 July and 1 September 2027. [Verify on the official page whether the research funds are a flat allowance, whether unspent funds roll over, and whether relocation is covered separately.] The plan below shows how the research allowance would be used; it is indicative and does not appear in the application unless the portal asks.

| Year | Use of the USD 12,000 research allowance (indicative) | Approx. |
|---|---|---|
| Y1 | Cloud GPU/compute for the audit pipeline and first simulation runs [confirm whether the host group's cluster is available; if so, reallocate to travel]; ISO/IEC JTC 1/SC 42 plenary attendance (one meeting); one conference (FOIS or a robotics venue) | 6,000 / 2,500 / 3,500 |
| Y2 | Compute for policy-training experiments (SAPIEN + second simulator); two conferences (one ML/robotics — CoRL/ICRA/RSS class — and one KR/ontology venue); open-source release costs (DOI, hosting) | 6,500 / 5,000 / 500 |
| Y3 | Real-robot replication consumables [confirm with host]; second-domain data access [confirm licence costs, if any]; job-market travel; SC 42 meeting | 4,000 / 2,000 / 3,500 / 2,500 |

No salary is requested for anyone other than the fellow. Undergraduate research assistants, if any, are funded through Cornell's own programs [confirm what the host department offers].

## Milestone timeline (36 months, start [1 July – 1 September 2027])

| Months | Theme | Milestone | Deliverable / evidence |
|---|---|---|---|
| 1–3 | 1 | Competency questions extracted from the annotation schemas of PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment and DROID | Competency-question set; dataset adapters (LeRobot, RLDS, ROS 2/MCAP, USD/PLY/JSON) [reuse; confirm which are already built] |
| 1–8 | 1 | Parts ontology: rigid, articulated, functional and assembly modules in Common Logic, verified (consistency, non-triviality, representation theorems) with Prover9/Mace4 | Modules released to COLORE; verification log |
| 4–8 | 1 | Constitution mappings between the four modules; PSL integration for parthood change under manipulation | Theorems on compatibility of decompositions; **Y1 milestone: is every dataset hierarchy a model of at least one module?** |
| 6–12 | 2 | Two-tier audit pipeline (Datalog/SMT bulk tier, first-order prover tier); first audit of all seven datasets | **First quantitative measurement of parthood consistency in robot datasets**; audit/data paper submitted |
| 10–16 | 2 | Cross-dataset label mappings proven meaning-preserving; corrected annotations; merged ontology-aligned corpus | Public data release with DOI; audit toolkit v1 |
| 12–18 | 3 | Differentiable relaxations of parthood constraints as auxiliary losses; constraint-guided augmentation | Training code; pilot results on held-out PartNet-Mobility categories in SAPIEN |
| 18–24 | 3 | Verification-in-the-loop evaluation protocol; full simulation study with confidence intervals and ablations by axiom family | **Y2 milestones: does ontology-consistent training improve generalization? does violation rate predict failure?**; methods paper submitted to an ML or robotics venue |
| 24–30 | 3 | Replication on [host group's robot platform — confirm]; cross-embodiment transfer on pooled, aligned data | Robotics-venue paper |
| 24–32 | 2 | Audit method applied to a second hierarchical-annotation domain (CAD assemblies or medical-imaging part labels) [choose with host] | Toolkit v2; second-domain paper or report |
| 30–36 | 1–3 | Contribution of the parts ontology to ISO/IEC JTC 1/SC 42 [confirm mechanism — new work item or amendment]; consolidated open release; faculty job market | SC 42 contribution document; final release; job applications |

## Internal deadlines for this application
| Date | Item |
|---|---|
| 26 Sept 2026 | Read the official page and portal; confirm page/word limits, referee mechanism, host form; email the program about the PhD-date rule (emails.md, email 1) |
| 26–29 Sept 2026 | Identify and contact candidate faculty hosts (emails.md, email 2); a host must agree before anything else is worth doing |
| 2 Oct 2026 | Complete draft (proposal, statement, CV) to the host and the three referees |
| 9 Oct 2026 | Referee letters in (internal date); host sponsorship form submitted [verify who submits it] |
| 13 Oct 2026 | Submit the application (two days early) |
| 15 Oct 2026 | Program deadline (registry; verify time of day and time zone) |
| [Jan–Mar 2027] | Expected notification [verify] |
| 1 Jul – 1 Sep 2027 | Start window |
