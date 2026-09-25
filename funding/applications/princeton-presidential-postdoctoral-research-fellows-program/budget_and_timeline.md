# Budget and timeline — Princeton Presidential Postdoctoral Research Fellows Program

## Money
No budget is requested or scored. The fellowship provides (registry, deadline confidence low): a Princeton postdoctoral salary of **approximately USD 70,000–80,000 per year** plus benefits and **research funds** [amount not recorded — verify], for up to three years, starting September 2027. [Verify on the official page the exact salary, the research-fund amount, whether unspent funds roll over, and whether relocation is covered.] The plan below shows how a research allowance would be used; it is indicative and does not appear in the application unless the form asks.

| Year | Use of the research allowance (indicative; scale to the actual amount) | Priority order |
|---|---|---|
| Y1 | Cloud GPU/compute for the audit pipeline and first simulation runs [confirm whether the host group's cluster or a Princeton research-computing allocation is available; if so, reallocate to travel]; one ISO/IEC JTC 1/SC 42 plenary; one conference (FOIS or a robotics venue) | compute > SC 42 > conference |
| Y2 | Compute for policy-training experiments (SAPIEN + second simulator); two conferences (one ML/robotics — CoRL/ICRA/RSS class — and one KR/ontology venue); open-source release costs (DOI, hosting) | compute > conferences > release |
| Y3 | Real-robot replication consumables [confirm with host]; second-domain data access [confirm licence costs, if any]; job-market travel; SC 42 meeting | replication > job market > SC 42 > data |

No salary is requested for anyone other than the fellow. Undergraduate researchers, if any, are funded through Princeton's own independent-work and summer research programs [confirm what the host department offers].

## Milestone timeline (36 months, start September 2027 [or September 2028 under Scenario B])

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

Community milestones from the contributions statement run alongside: undergraduate independent-work projects each year (Y1–Y3); the parts-and-wholes reading group from month 3; the audit-tooling workshop in month 14 (after toolkit v1) and again in month 30 (toolkit v2).

## Internal deadlines for this application
| Date | Item |
|---|---|
| 26 Sept 2026 | Read the official page and application system; confirm whether the deadline is 13 Nov 2026 or the cycle has closed; confirm criteria wording, limits, referee mechanism, host-letter mechanics; email the program (emails.md, email 1) |
| 26 Sept – 2 Oct 2026 | Identify and contact candidate faculty hosts (emails.md, email 2); a host must agree before anything else is worth doing |
| **Scenario A — 13 Nov 2026 stands** | |
| 16 Oct 2026 | Complete draft (research statement, contributions statement, cover letter, CV) to the host and the three referees |
| 6 Nov 2026 | Referee letters in (internal date); host faculty letter submitted [verify who submits it] |
| 10 Nov 2026 | Submit the application (three days early) |
| 13 Nov 2026 | Program deadline [unconfirmed; verify time of day and time zone] |
| [winter/spring 2027] | Expected notification [verify] |
| Sept 2027 | Start |
| **Scenario B — 2026 cycle closed** | |
| Oct 2026 – Jun 2027 | Keep the host relationship active: share the first audit results as they appear from the Toronto or Harvard work; ask the host to confirm intent to sponsor in the 2027 cycle |
| [Jul–Aug 2027] | Portal opens [verify]; refresh all four documents; re-confirm referees |
| [Sept 2027] | Program deadline [verify]; confirm the years-since-PhD rule for a Sept 2028 start |
