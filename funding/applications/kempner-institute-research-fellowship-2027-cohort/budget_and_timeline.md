# Timeline and resources — Kempner Institute Research Fellowship (2027 cohort)

No budget is requested: the fellowship provides salary (about USD 100k reported [confirm]), research support, office space, compute and engineering support at amounts set by the Institute [confirm amounts on the official page or from the program office]. This file is the 36-month milestone plan the proposal refers to (Y1–Y3 tags), followed by the resources the applicant will ask the Institute for.

## Milestone timeline (start September 2027)

| Period | Theme / project | Milestone | Deliverable |
|---|---|---|---|
| Y1 M1–3 (Sept–Nov 2027) | 1.1 Parts ontology | Four parthood modules (rigid, articulated, functional, assembly) axiomatized in Common Logic; consistency and non-triviality verified with Prover9/Mace4 | Ontology v0.1 in COLORE (open licence) |
| Y1 M3–6 (Dec 2027–Feb 2028) | 1.2 Constitution mappings | Compatibility conditions between kinematic, functional and visual decompositions proved from the parthood-preserving-mapping theory; PSL integration for parthood change under manipulation | Representation theorems; ontology v1.0 |
| Y1 M4–9 (Dec 2027–May 2028) | 2.1 Audit pipeline | Adapters for PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment, DROID; Datalog/SMT compilation; theorem-proving tier for residual cases | Audit toolkit v0.1; first violation-rate results on two datasets |
| Y1 M9–12 (June–Aug 2028) | 2.1 / 2.2 | Audit across all seven datasets; simulated vs real-robot comparison; first draft of the audit/data paper | Audit paper submitted [venue — e.g., a NeurIPS Datasets & Benchmarks track or a robotics venue; confirm with mentors] |
| Y2 M13–18 (Sept 2028–Feb 2029) | 2.2 Alignment and release; 3.1 Constraint-based training | Provably meaning-preserving label mappings; corrected annotations; merged corpus released; differentiable relaxations of parthood constraints implemented in [Mentor 1's policy architecture]; SAPIEN training on held-out PartNet-Mobility categories | Merged ontology-aligned corpus v1; toolkit v1.0; first generalization results |
| Y2 M18–24 (Mar–Aug 2029) | 3.1 / 3.2; 3.3 pilot | Constraint-guided augmentation; verification-in-the-loop evaluation; ablations by axiom family; violation rate vs task failure; pooled-data transfer experiments; human-comparison protocol drafted and ethics application submitted with Mentor 2, small pilot run | Methods paper submitted [ML venue]; ontology and toolkit contributed to ISO/IEC JTC 1/SC 42; pilot protocol |
| Y3 M25–30 (Sept 2029–Feb 2030) | 3.3 Human comparison | Full elicitation of human part decompositions for a sample of PartNet-Mobility objects (approval obtained in Y2); agreement measured under the constitution theory | Human–policy comparison dataset released |
| Y3 M30–36 (Mar–Aug 2030) | 3.2 / 3.3; synthesis | Which axiom families account for generalization gains; whether humans and ontology-trained policies violate the same axioms; second simulator [confirm] replication | Third paper [cognitive science or robotics venue]; final ontology release; faculty-application package |

## Resources to request from the Institute (no dollar figures invented)

| Item | Why | Notes |
|---|---|---|
| GPU compute for policy training | Theme 3: training part-aware policies with ablations by axiom family across held-out categories | Scale to be sized with Mentor 1 [confirm the Institute's compute allocation process] |
| Engineering support | Dataset adapters (LeRobot, RLDS, ROS 2/MCAP, OpenUSD formats) and the two-tier audit pipeline — all written fresh under the fellowship and released under an open licence; no AXIOMALITY code or data is used (the company's product overlaps with Theme 2, so this separation must be explicit and kept) | The Institute lists engineering support as part of the fellowship [confirm scope] |
| Research support funds | Human-participant compensation for Project 3.3; conference travel; open-data hosting | Amount set by the Institute [confirm] |
| Software | Prover9/Mace4, Z3, SAPIEN, Common Logic tooling — all open source | No cost |
| Access to COLORE and ISO/IEC JTC 1/SC 42 | Verification methodology and dissemination path | Through Prof. Grüninger (external collaborator) [confirm] |

## Risk register

| Risk | Mitigation |
|---|---|
| Mentors not confirmed by 27 Sept | Submit with two confirmed mentors; a third is optional |
| Start date Sept 2027 vs Toronto spring 2027 | Both applications proceed; decision in Jan 2027 when Kempner offers arrive, before CPRA results (31 Mar 2027) |
| Audit pipeline does not scale to millions of parts | SMT tier handles the bulk; prover tier is bounded with timeouts reported as UNKNOWN (first-class output) |
| Constraint-based training gives no generalization gain | The audit and the human comparison are publishable independently; a null result on the inductive-bias hypothesis is itself a measurable claim about what policies represent |
| Human study delayed by ethics approval | Protocol and ethics application in Y2 with a pilot; full study in Y3; Mentor 2's group holds the approval route |
| Conflict of interest: AXIOMALITY sells data verification that overlaps with Theme 2 | Disclose in the statement (done); confirm outside-activity policy with the program office (email 6); keep fellowship code and data open and separate; no company data in any experiment |
