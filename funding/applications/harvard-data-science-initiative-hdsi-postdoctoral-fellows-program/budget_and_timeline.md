# Timeline and resources — HDSI Postdoctoral Fellows Program (2026-27 call)

No budget is requested: the fellowship provides a salary and an annual research and travel allocation set by HDSI (2025-26: about USD 85,000 salary plus about USD 10,000 research/travel per year [confirm 2026-27 amounts on the call]). The program page now describes the fellowship as two to three years [confirm on the call; the plan below assumes two, with the imaging extension and Project 3.2 ablations the natural third-year continuation]. This file is the 24-month milestone plan the research statement refers to (Y1/Y2 tags), followed by how the research allocation would be used and the resources to arrange with mentors.

## Milestone timeline (start [September 2027 — confirm])

| Period | Theme / project | Milestone | Deliverable |
|---|---|---|---|
| Y1 M1–3 | 1.1 Parts ontology | Four parthood modules (rigid, articulated, functional, assembly) axiomatized in Common Logic as TUpper extensions; consistency and non-triviality verified with Prover9/Mace4 | Ontology v0.1 in COLORE (open licence) |
| Y1 M3–6 | 1.2 Constitution mappings | Compatibility conditions between kinematic, functional and visual decompositions proved from the parthood-preserving-mapping theory; PSL integration for parthood change under manipulation; representation theorems for each dataset schema | Ontology v1.0; theorems and counter-models filed |
| Y1 M2–8 | 2.1 Audit pipeline | Adapters in priority order: PartNet, PartNet-Mobility, GAPartNet (M2–5), then PartNet-Ensembled, AgiBot World, Open X-Embodiment, DROID (M5–8); Datalog/SMT compilation; theorem-proving tier with time budget; provenance store | Audit toolkit v0.1; first violation-rate results on two datasets |
| Y1 M5 | 2.2 Pre-registration | Analysis plan (hierarchical logistic model; bootstrap; multiplicity correction) and Theme 3 hypotheses pre-registered after the pilot | Registered plan (OSF or equivalent [confirm]) |
| Y1 M6–12 | 2.2 Measurement | Audit across all seven datasets (minimum at M12: the first three released); violation rates by axiom family with bootstrap intervals, stratified by category and depth; random-effects analysis of source disagreement with Mentor 1; corrections and mappings | Audit/data paper submitted [venue — e.g., a datasets-and-benchmarks track; confirm with mentors]; corrected annotations and mappings released |
| Y1 M9–Y2 M15 | 2.3 Health extension | Anatomical partonomy and segmentation dataset chosen with Mentor 3 [confirm; access approvals]; adapter written; audit run; divergence report | Imaging data-quality report; toolkit v1.0 with second-domain adapter |
| Y2 M13–18 | 3.1 Pooled data | Merged ontology-aligned corpus v1 released; part-aware policies trained in SAPIEN [+ second simulator] on native vs aligned pooled data; held-out PartNet-Mobility categories; matched comparisons with confidence intervals | Merged corpus; first generalization results |
| Y2 M16–22 | 3.2 Constraints and evaluation | Differentiable parthood-constraint losses; constraint-guided augmentation; verification-in-the-loop protocol; ablations by axiom family; violation rate vs task failure | Methods paper submitted [ML venue]; ontology and toolkit contributed to ISO/IEC JTC 1/SC 42 |
| Y2 M22–24 | Synthesis | Which axiom families account for gains; shared violation classes across robotics and imaging; final releases | Third paper [robotics or imaging venue]; final ontology release; faculty-application package |

## Use of the annual research and travel allocation (amount set by HDSI [confirm]; no figures invented)

| Item | Why | Notes |
|---|---|---|
| Conference travel | Present the audit paper and methods paper; attend one ISO/IEC JTC 1/SC 42 plenary as the laboratory's contributor [confirm] | Two to three trips per year |
| Cloud compute for the bulk audit | Tier-one Datalog/SMT checks over millions of part instances; theorem-proving tier with time budget | Sized after the M3 pilot; policy-training compute arranged with Mentor 2 (below) |
| Open-data hosting | Corrected annotations, mappings, merged corpus, audit logs | Prefer a Harvard-supported repository [confirm — e.g., Harvard Dataverse] |
| Workshop / cohort activity | Present the audit tooling at an HDSI event; the equity commitment in statement.md | Small |

## Resources to arrange with mentors and Harvard (no cost to HDSI unless noted)

| Item | Why | Source |
|---|---|---|
| GPU compute for policy training | Theme 3 experiments with ablations by axiom family | Mentor 2's group or Harvard research computing [confirm allocation process] |
| Policy architecture and second simulator | Project 3.1 | Mentor 2 [confirm] |
| Anatomical partonomy and segmentation dataset; any data-use approvals | Project 2.3 | Mentor 3 [confirm resource and approvals; no patient-identifiable data is required for a label-hierarchy audit, but confirm] |
| Software | Prover9/Mace4, Z3, SAPIEN, Common Logic tooling, LeRobot/RLDS adapters — all open source | No cost |
| COLORE access and SC 42 contribution path | Verification methodology and dissemination | Prof. Grüninger (external collaborator) [confirm] |

## Risk register

| Risk | Mitigation |
|---|---|
| The 2026-27 call does not run or the deadline passes before mentors are secured | Confirm by 3 Oct; if the call is dormant, redirect to the HDSI Postdoctoral Fellow Research Fund (separate registry entry) for an audit pilot while on the current HMS appointment |
| Internal candidates must name mentors outside the current laboratory | Mentor slots 1–3 are outside the current laboratory by design; the current supervisor is a referee, not a mentor |
| Tier-two theorem proving does not scale | Time budgets with UNKNOWN as a first-class result; report the decided fraction; restrict tier two to a stratified sample if needed |
| Alignment shows no generalization gain | The audit and the corpus are results in their own right; a null result on Theme 3 is reported with the violation-rate analysis |
| Imaging resource access delayed | Start Project 2.3 with a public partonomy and a public segmentation dataset [confirm]; no clinical data required |
| Founder role raises a conflict-of-interest question | Disclosed in statement.md; research outputs open-licensed and independent of the company; confirm Harvard rules before submission |
| Toronto track (CPRA/Vector/DSI) and HDSI both succeed | Only one can be accepted; decision at offer time (HDSI late Jan–early Feb 2027; CPRA ~31 Mar 2027); all outputs designed to carry over |
