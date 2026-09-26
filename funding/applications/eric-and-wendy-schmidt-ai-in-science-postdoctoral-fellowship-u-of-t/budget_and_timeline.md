# Budget and timeline — Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship (U of T)

## Budget
The fellowship's financial terms are fixed by the program and no budget is requested from the applicant: CAD 85,000 per year salary, plus a fixed CAD 11,000 per year paid towards the standard benefit rate and postdoctoral levy incurred by the supervisor's unit, for two years (confirmed from the DSI page via search on 2026-09-25) [verify whether the supervisor may top up; verify whether a research/travel allowance exists and its amount — none is mentioned in the snippet]. Research costs are therefore covered as follows (all to confirm with Prof. Grüninger and the co-supervisor):

| Item | Source | Note |
|---|---|---|
| Salary and benefits (2 years) | Fellowship | fixed |
| Verification tooling (Prover9/Mace4, COLORE, Common Logic tooling) | Semantic Technologies Laboratory | open-source; no cost |
| SMT/Datalog audit infrastructure | Open-source solvers; laboratory workstation | [solver choice — confirm] |
| Compute for policy training (Theme 3) | [Vector Institute allocation via co-supervisor / supervisor's allocation — confirm]; DSI cohort compute if offered [verify] | Y2 heavy |
| Datasets (PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment, DROID) | Public releases under their licences | licence terms to be checked for redistribution of corrected annotations |
| Conference travel (one AI/ML venue and one robotics venue per year) | [Fellowship allowance if any / supervisor's grant / DSI travel support — confirm] | [amount] |
| ISO/IEC JTC 1/SC 32 participation | [Standards Council of Canada mirror committee — confirm whether travel is needed or remote participation suffices] | |

Nothing in this package commits any dollar figure beyond the program's own terms.

## Milestone timeline (24 months from a 1 May 2027 start; shift by the actual start date)

| Months | Theme 1 — Parts (O1) | Theme 2 — Audit (O2) | Theme 3 — Learning (O3) | AI training programme | Outputs |
|---|---|---|---|---|---|
| 1–2 | Competency questions from annotator protocols and manipulation questions; rigid-part and articulated-part modules drafted | Schema mappings for PartNet and PartNet-Mobility | Onboarding with co-supervisor's group; set up SAPIEN | Cohort start; deep robot learning and 3D representation courses [verify programme] | Milestone M2: modules in COLORE with consistency proofs |
| 3–4 | Functional-part and assembly modules; constitution-mapping theorem carried over from [2] | Schema mappings for GAPartNet, PartNet-Ensembled, AgiBot World; SMT tier prototype | Reproduce two baseline part-aware manipulation methods on PartNet-Mobility (training deliverable) | Reading group; differentiable-programming workshop | M4: verified parts ontology v0.9 (consistency, non-triviality, module relationships) |
| 5–8 | Representation theorems (articulated parts ↔ kinematic trees); decidable fragment compiled | Two-tier pipeline complete; first audit across five datasets; violation rates by axiom family and category | Design of constraint losses (a); conformal calibration first used in audit abstention | Uncertainty quantification / statistics module | M8: first audit results; ontology v1.0 released; **audit/data paper submitted (Y1)** |
| 9–12 | Ontology contributed to ISO/IEC JTC 1/SC 32 as a working document [verify procedure] | Corrected annotations and provably meaning-preserving mappings released; merged ontology-aligned corpus v1 | Constraint-guided augmentation (b); pooled-data experiment (H3) begins | Present audit results to cohort; cohort workshop on specification-based auditing | M12: corpus and audit toolkit released; Y1 report to DSI |
| 13–16 | Extend to Open X-Embodiment and DROID part-level subsets | Audit of real-robot subsets; per-source coverage report | Constraint-loss training on held-out PartNet-Mobility categories (H1); ablations by axiom family | Vector compute onboarding [verify] | M16: **ML-venue paper 1 submitted** (constraint losses and augmentation) |
| 17–20 | Ontology maintenance; module additions from audit findings | Toolkit generalization test on one non-robotics hierarchical annotation set [CAD assemblies or medical-image part labels — choose] | Verification-in-the-loop evaluation protocol (c); violation rate vs. task failure (H2) | | M20: **robotics-venue paper submitted** (verification-in-the-loop evaluation) |
| 21–24 | Final COLORE and SC 32 contributions | Final corpus v2 release | Second simulator [confirm] replication; consolidation | Cohort close-out presentation | M24: **ML-venue paper 2 submitted** (pooled ontology-aligned data, cross-vocabulary transfer); final report |

## Dependencies and risks
- Theme 3 depends on a co-supervisor with a part-aware manipulation pipeline; if none is secured by M2, fall back to the open SAPIEN/ManiSkill-style baselines [verify names] and Vector collaborators.
- If the SMT tier cannot cover most obligations at dataset scale (Theme 2 first open question), the audit is reported on stratified samples with theorem-proving verification, and the full-scale run moves to Y2.
- If the apply page requires two co-supervisors and none is secured by 1 October, the application cannot be submitted as drafted; the proposal and timeline are then reused unchanged for the NSERC CPRA (17 October 2026) and the DSI Postdoctoral Fellowship (January 2027), which also needs a second co-supervisor.
- If DSI confirms that candidates with AI-adjacent doctorates are not the intended cohort, the same redirection applies.
- Timeline assumes a 1 May 2027 start; the milestones are relative to the start month and shift with it.
