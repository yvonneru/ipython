# Timeline and resources — Stanford Science Fellows (2027 cohort)

No budget is requested: the fellowship provides a stipend (USD 98,000/yr per the registry [verify; the tracker records 85,000–95,000]), research funds and professional development at amounts set by the program [confirm on the official page or from the program office]. This file is the 36-month milestone plan the proposal refers to (Y1–Y3 tags), followed by the resources the applicant will ask the host and the program for. If the 2026 cycle has closed (Plan B in README.md), shift every date by twelve months.

## Milestone timeline (start [1 September 2027])

| Period | Theme / project | Milestone | Deliverable |
|---|---|---|---|
| Y1 M1–3 (Sept–Nov 2027) | 1.1 Parts ontology | Four parthood modules (rigid, articulated, functional, assembly) axiomatized in Common Logic; consistency and non-triviality verified with Prover9/Mace4 | Ontology v0.1 in COLORE (open licence) |
| Y1 M3–6 (Dec 2027–Feb 2028) | 1.2 Constitution mappings | Compatibility conditions between kinematic, functional and visual decompositions proved from the parthood-preserving-mapping theory; PSL integration for parthood change under manipulation | Representation theorems; ontology v1.0 |
| Y1 M4–9 (Dec 2027–May 2028) | 2.1 Audit pipeline | Adapters for PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment, DROID; Datalog/SMT compilation; theorem-proving tier for residual cases | Audit toolkit v0.1; first violation-rate results on PartNet and DROID, discussed with their Stanford authors [confirm host] |
| Y1 M9–12 (June–Aug 2028) | 2.1 / 2.2 | Audit across all seven datasets; simulated vs real-robot comparison; first draft of the audit/data paper | Audit paper submitted [venue — e.g., a NeurIPS Datasets & Benchmarks track or a robotics venue; confirm with host] |
| Y2 M13–18 (Sept 2028–Feb 2029) | 2.2 Alignment and release; 3.1 Constraint-based training | Provably meaning-preserving label mappings; corrected annotations; merged corpus released; differentiable relaxations of parthood constraints implemented in [host's policy architecture]; SAPIEN training on held-out PartNet-Mobility categories | Merged ontology-aligned corpus v1; toolkit v1.0; first generalization results |
| Y2 M18–24 (Mar–Aug 2029) | 3.1 / 3.2 | Constraint-guided augmentation; verification-in-the-loop evaluation; ablations by axiom family; violation rate vs task failure; pooled-data transfer experiments | Methods paper submitted [ML venue]; ontology and toolkit contributed to ISO/IEC JTC 1/SC 42 |
| Y3 M25–30 (Sept 2029–Feb 2030) | 3.2 real-robot replication; 2.2 second domain | Replication on [host group's robot platform — confirm]; audit transferred to a second hierarchical-annotation domain (CAD assemblies or medical-imaging part labels, with [Stanford biomedical-ontology group — confirm]) | Real-robot results; second-domain audit released |
| Y3 M30–36 (Mar–Aug 2030) | Synthesis | Which axiom families account for generalization gains; cross-embodiment transfer; [second simulator — confirm] replication | Third paper [robotics venue]; final ontology release; faculty-application package |

## Resources to request (no dollar figures invented)

| Item | Why | Notes |
|---|---|---|
| GPU compute for policy training | Theme 3: training part-aware policies with ablations by axiom family across held-out categories | Scale to be sized with the host [confirm whether the program or the host's department supplies compute] |
| Robot platform access | Y3 real-robot replication | Host group's platform [confirm] |
| Research funds | Conference travel; open-data hosting; software licences if any | Amount set by the program [confirm] |
| Professional development | Faculty-preparation and cohort activities | Provided by the program [confirm scope] |
| Software | Prover9/Mace4, Z3, SAPIEN, Common Logic tooling — all open source | No cost |
| Access to COLORE and ISO/IEC JTC 1/SC 42 | Verification methodology and dissemination path | Through Prof. Grüninger (external collaborator and co-author on Theme 1) [confirm] |
| Dataset licences | PartNet/ShapeNet, SAPIEN, GAPartNet, AgiBot World, OXE, DROID under research (mostly non-commercial) licences | Registry notes non-commercial terms; corrected annotations released under compatible licences; no commercial reuse by AXIOMALITY without separate agreements |

## Risk register

| Risk | Mitigation |
|---|---|
| Deadline already passed (mid-Sept 2026) | Plan B: the same package for the September 2027 cycle; ask the program now whether a 2028 start satisfies the post-PhD window |
| Host not confirmed by 2 Oct (Plan A) | Approach two candidates in parallel (emails 3–4); a PartNet or DROID author is the strongest fit, a formal-methods host the second |
| Start date Sept 2027 vs Toronto spring 2027 (CPRA) | Both applications proceed; decision when offers arrive [notification date — verify], before CPRA results (31 Mar 2027) |
| Audit pipeline does not scale to millions of parts | SMT tier handles the bulk; prover tier is bounded with timeouts reported as UNKNOWN (first-class output) |
| Constraint-based training gives no generalization gain | The audit and the alignment are publishable independently; a null result on the inductive-bias hypothesis is itself a measurable claim about what policies represent |
| Non-commercial dataset licences vs the founder role | Fellowship work released openly; AXIOMALITY kept separate and disclosed under the outside-activity policy [verify] |
