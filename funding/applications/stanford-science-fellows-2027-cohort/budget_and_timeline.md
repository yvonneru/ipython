# Timeline and resources — Stanford Science Fellows (2027 cohort)

No budget is requested: the fellowship provides a stipend of USD 98,000 a year, research funds and professional development at amounts set by the program [research-fund amount: confirm on the FAQ]. This file is the 36-month milestone plan the research statement refers to (Y1–Y3 tags), followed by the resources the applicant will ask the host and the program for.

**Start date.** The program's earliest start is 1 July 2027 and the two-year cap on prior postdoctoral experience is measured at the fellowship start [per the FAQ; verify]. The plan therefore assumes **[1 July 2027]**. If the Harvard appointment began before July 2025, a July 2027 start is the only one that keeps the applicant under the cap [confirm the HMS start month; ask the program how partial months are counted — emails.md, email 1]. Shift every date below if the start moves.

## Milestone timeline (start [1 July 2027])

| Period | Theme / project | Milestone | Deliverable |
|---|---|---|---|
| Y1 M1–3 (Jul–Sep 2027) | 1.1 Parts ontology | Four parthood modules (rigid, articulated, functional, assembly) axiomatized in Common Logic; consistency and non-triviality verified with Prover9/Mace4 | Ontology v0.1 in COLORE (open licence) |
| Y1 M3–6 (Sep–Dec 2027) | 1.2 Constitution mappings | Compatibility conditions between kinematic, functional and visual decompositions proved from the parthood-preserving-mapping theory; PSL integration for parthood change under manipulation | Representation theorems; ontology v1.0 |
| Y1 M4–9 (Oct 2027–Mar 2028) | 2.1 Audit pipeline | Adapters for PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment, DROID; Datalog/SMT compilation; theorem-proving tier for residual cases | Audit toolkit v0.1; first violation-rate results on PartNet and DROID, discussed with their Stanford authors [confirm host] |
| Y1 M9–12 (Mar–Jun 2028) | 2.1 / 2.2 | Audit across all seven datasets; simulated vs real-robot comparison; first draft of the audit/data paper | Audit paper submitted [venue — a datasets-and-benchmarks track or a robotics venue; confirm with host] |
| Y2 M13–18 (Jul–Dec 2028) | 2.2 Alignment and release; 3.1 Constraint-based training | Provably meaning-preserving label mappings; corrected annotations; merged corpus released; differentiable relaxations of parthood constraints implemented in [host's policy architecture]; SAPIEN training on held-out PartNet-Mobility categories | Merged ontology-aligned corpus v1; toolkit v1.0; first generalization results |
| Y2 M18–24 (Jan–Jun 2029) | 3.1 / 3.2 | Constraint-guided augmentation; verification-in-the-loop evaluation; ablations by axiom family; violation rate vs task failure; pooled-data transfer experiments | Methods paper submitted [ML venue]; ontology and toolkit contributed to ISO/IEC JTC 1/SC 42 |
| Y3 M25–30 (Jul–Dec 2029) | 3.2 real-robot replication; 2.2 second domain | Replication on [host group's robot platform — confirm]; audit transferred to a second hierarchical-annotation domain (CAD assemblies or medical-imaging part labels, with [Stanford biomedical-ontology group — confirm]) | Real-robot results; second-domain audit released |
| Y3 M30–36 (Jan–Jun 2030) | Synthesis | Which axiom families account for generalization gains; cross-embodiment transfer; [second simulator — confirm] replication | Third paper [robotics venue]; final ontology release; faculty-application package |

## Resources to request (no dollar figures invented)

| Item | Why | Notes |
|---|---|---|
| GPU compute for policy training | Theme 3: training part-aware policies with ablations by axiom family across held-out categories | Scale to be sized with the host [confirm whether the program's research funds or the host's department supplies compute] |
| Robot platform access | Y3 real-robot replication | Host group's platform [confirm] |
| Research funds | Conference travel; open-data hosting; software licences if any | Amount set by the program [confirm] |
| Professional development | Faculty-preparation and cohort activities | Provided by the program [confirm scope] |
| Software | Prover9/Mace4, Z3, SAPIEN, Common Logic tooling — all open source | No cost |
| Access to COLORE and ISO/IEC JTC 1/SC 42 | Verification methodology and dissemination path | Through Prof. Grüninger (external collaborator on Theme 1) [confirm] |
| Dataset licences | PartNet/ShapeNet, SAPIEN, GAPartNet, AgiBot World, OXE, DROID under research (mostly non-commercial) licences | Corrected annotations released under compatible licences; no commercial reuse by AXIOMALITY without separate agreements |

## Risk register

| Risk | Mitigation |
|---|---|
| Two-year prior-postdoc cap at start (HMS appointment since [month year]) | Request the earliest start (1 July 2027); ask the program in writing how the cap is counted (email 1); keep the SGS letter and HMS appointment letter ready as evidence of dates |
| J-1 eligibility (program does not support H-1B; citizenship and current US status unknown) | Confirm current visa status now; if an F-1/OPT or J-1 history exists, check the two-year home-residency rule and J-1 bar-on-repeat rules with Stanford's Bechtel International Center before submitting [verify] |
| Scope: "fundamental research in a natural science discipline" | Ask the program office whether computer science / robotics / knowledge representation is in scope (email 1); the research statement is framed as a fundamental question about representation, tested empirically, and avoids compliance and commercial framing |
| Host not confirmed by 2 Oct | Approach two candidates in parallel (emails 3–4); a PartNet or DROID author is the strongest fit, a formal-methods host the second; the program awards only once a host has agreed |
| Start date July 2027 vs Toronto spring 2027 (NSERC CPRA) | Both applications proceed; decision when offers arrive [SSF notification date — verify; CPRA results date — verify] |
| Audit pipeline does not scale to millions of parts | SMT tier handles the bulk; prover tier is bounded with timeouts reported as UNKNOWN (first-class output) |
| Constraint-based training gives no generalization gain | The audit and the alignment are publishable independently; a null result on the inductive-bias hypothesis is itself a measurable claim about what policies represent |
| Non-commercial dataset licences vs the founder role | Fellowship work released openly; AXIOMALITY kept separate and disclosed under Stanford's outside-activity policy [verify] |
