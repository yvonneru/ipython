# Budget and timeline — Newton International Fellowship 2027

## Budget

The fellowship pays up to **GBP 280,000 over two years** (registry record, from the 2026 scheme notes) covering (i) basic salary at the host organisation's scale plus on-costs, (ii) research expenses, and (iii) relocation and visa costs for the fellow and dependents (2026 FAQ). Salary is set by the host, so the costing is done by the host research office; the applicant's job is to justify the research expenses and the relocation line. Every figure below is a placeholder to be replaced from the 2027 scheme notes and the host's costing [no amounts are confirmed; third-party summaries quoting GBP 8,000 p.a. research expenses and GBP 3,500 relocation appear to be older-round caps].

| Line | Year 1 | Year 2 | Justification |
|---|---|---|---|
| Salary and on-costs (host scale, postdoctoral grade [grade — host to confirm]) | [GBP] | [GBP] | Full-time fellow for 24 months; set by the host |
| Research expenses: compute | [GBP] | [GBP] | GPU hours for SAPIEN policy training and ablations by axiom family (WP3); Datalog/SMT audit runs over millions of part instances (WP2). Sizing method: [number of policy-training runs × hypotheses (3) × ablation arms × seeds] × [host GPU-hour rate] — fill with the sponsor. [State whether the host provides compute in kind; if so reduce this line and record the in-kind contribution for the HoD statement] |
| Research expenses: workstation and software | [GBP] | — | Workstation for theorem proving (Prover9/Mace4, SMT solvers) and simulation; open-source tools, no licence costs expected |
| Research expenses: open-access publication charges | [GBP] | [GBP] | Audit/data paper (Y1–Y2), methods paper (Y2), robotics-venue paper (Y2) |
| Research expenses: conferences and standards meetings | [GBP] | [GBP] | One AI or robotics conference per year (e.g., CoRL / ICRA / FOIS [choose]); ISO/IEC JTC 1/SC 32 plenary attendance [confirm whether SC 32 travel is an allowable cost] |
| Research expenses: collaboration visit to Toronto | [GBP] | [GBP] | One short visit per year to the Semantic Technologies Laboratory for COLORE integration and the Synthese follow-on work; within the scheme's limit on time outside the UK |
| Relocation and visa (fellow [+ dependents — confirm]) | [GBP] | — | Visa fees, immigration health surcharge, travel and removal; per the 2027 cap |
| **Total** | [GBP] | [GBP] | **≤ GBP 280,000** |

Data costs: none — PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled and AgiBot World are public. No fieldwork. No equipment beyond a workstation.

## Milestone timeline (24 months; from the research-program 24-month template)

| Month | Milestone | Work package | Deliverable |
|---|---|---|---|
| M1–M3 | Ontology design: competency questions extracted from the five datasets' annotation schemas; pilot audit of PartNet-Mobility to test the schema mapping; module structure fixed as a TUpper extension with PSL | WP1 (+WP2 pilot) | Design document; module signatures; pilot audit note (go/no-go per dataset) |
| M4–M8 | Verification: consistency, non-triviality, module relationships, representation theorems (Prover9/Mace4) | WP1 | **M8: verified ontology released (open licence) and submitted to COLORE** |
| M4–M10 | Schema mappings from each dataset to the ontology; Datalog/SMT tier of the audit pipeline; theorem-proving tier for residual cases | WP2 | Pipeline v1 |
| M10–M12 | Audit of five datasets; violation rates and patterns; corrected annotations | WP2 | **M12: audit results and corrected annotations published; audit/data paper submitted** |
| M12–M16 | Cross-dataset label mappings proved meaning-preserving; merged ontology-aligned corpus; toolkit packaging | WP2 | **M16: toolkit and merged corpus released** |
| M12–M18 | Pooled-data experiments; constraint-guided augmentation on the host's pipeline (SAPIEN [+ second simulator]) | WP3 | Interim results; first hypothesis tested |
| M18–M22 | Differentiable parthood-constraint losses; verification-in-the-loop evaluation protocol; ablations by axiom family | WP3 | Methods paper drafted |
| M22–M24 | Papers, standards contribution (SC 32 liaison), alumni-funding plan, faculty applications | all | **M24: methods paper and robotics-venue paper submitted; ontology proposed for SC 32 consideration** |

## Pre-award timeline (see README for the full table)

15 Oct 2026 decide UK track → 15 Nov 2026 sponsor secured → 15 Dec 2026 host internal EoI → Dec/Jan 2027 scheme notes read → 15 Jan 2027 proposal agreed with sponsor → 15 Feb 2027 referees, sponsor and HoD briefed → ≈4 Mar 2027 statements in Flexi-Grant → mid-March 2027 host approval and submission [exact date to confirm].
