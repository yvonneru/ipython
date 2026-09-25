# Budget and timeline — ARIA Rolling Opportunity Seed (12 months; GBP 10,000–500,000 inclusive of VAT and all direct and indirect costs)

All figures are [to be entered]; none is invented here. The range — GBP 10,000 to 500,000 per project, "inclusive of VAT (where applicable) and all associated costs" — is quoted from the 29 May 2026 solicitation in registry record `208a4aa98de4`; the registry's own guide for this seed is GBP 150,000–300,000 [decide]. Because the ceiling is VAT-inclusive, every line below is entered gross and a VAT line is shown. ARIA's rules on eligible costs, overheads, equipment and subcontracting are not known from this draft [verify in the solicitation and applicant guidance]. The UK share must exceed 50% of the project; compute it on effort and on cost once the team is fixed, state the basis used on the form, and show the two shares in the last block of this file.

## Budget (GBP)

| Line | Who / where | Basis | Amount |
|---|---|---|---|
| Lead applicant salary and on-costs | Dr. Ru; [UK host, visiting appointment — FTE %; or a Toronto/Harvard share — confirm which is allowable] | 12 months × [FTE] | [GBP] |
| Research engineer / postdoc — audit pipeline and simulation | [UK host]; UK | 12 months × [FTE] | [GBP] |
| UK co-lead time | [UK host]; UK | [FTE %] | [GBP] |
| Toronto collaboration (verification, COLORE, SC 42) | U of T, Semantic Technologies Laboratory; subcontract or collaboration agreement [confirm ARIA rules on non-UK subawards] | [graduate student months / Grüninger time] | [GBP] |
| Compute | UK host cluster or cloud; policy training in SAPIEN and audit at scale (millions of part instances; SMT and prover runs) | [GPU-hours; storage TB] | [GBP] |
| AXIOMALITY contribution | In-kind: Engine, adapters, 100,000 asset packages, engineering time [role: in-kind / subcontract — decide; if subcontract, cost and conflict-of-interest declaration for the founder-applicant] | — | [GBP or in-kind value] |
| Travel | ARIA programme meetings (UK); one SC 42 meeting; one robotics venue for results | [trips] | [GBP] |
| Open release | Licensing review, data hosting, DOI minting, toolkit packaging | — | [GBP] |
| Host overheads / indirect costs | [UK host rate; ARIA policy — verify] | — | [GBP] |
| VAT (where applicable) | [UK host / subcontract lines — confirm which attract VAT] | — | [GBP] |
| **Total, inclusive of VAT and all costs** | | | **[GBP ≤ 500,000; guide 150,000–300,000]** |

**UK share (state on the form).** By effort: UK [x] person-months of [y] = [z]%. By cost: UK lines GBP [a] of GBP [b] = [c]%. Both must exceed 50% [or the Programme Director must have accepted a UK-benefit case in writing — see `emails.md` email 3].

**Justification.** The seed is people and compute. The ontology (O1) needs the applicant and the Toronto collaboration; the audit (O2) needs one engineer for adapters, the two-tier checker and the release; the learning experiments (O3) need the UK co-lead's group and GPU time. Datasets are public; the simulator (SAPIEN) is open; provers (Prover9/Mace4), the SMT solver (Z3) and the Datalog engine are open-source. Nothing is bought except compute and hosting.

## Milestones (12-month template from the research program)

| Month | Milestone | Deliverable / decision |
|---|---|---|
| M1 | Kick-off at [UK host]; datasets mirrored; AXIOMALITY adapters licensed for the project [confirm]; conflict-of-interest and IP ring-fence recorded in the collaboration agreement | Data-management and open-licence plan filed with ARIA |
| M3 | Parts ontology modules (rigid, articulated, functional, assembly) drafted; COLORE synonymy questions answered | Q1.1 answered: which existing mereotopologies match PartNet / PartNet-Mobility |
| M4 | Ontology verified: consistency, non-triviality, module relationships; representation theorems for the five annotation schemas | O1 complete; ontology v0.9 released to COLORE (open licence) |
| M6 | Two-tier audit pipeline running; soundness/completeness of the SMT tier checked against the prover on a held-out sample | Go/no-go on scaling the fast tier |
| M8 | Audit across PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World; violation rates by axiom family; provable cross-dataset mappings; corrected annotations | **Public release:** audit report, corrected annotations, merged corpus v1, toolkit v1 |
| M9 | Policy training set up in SAPIEN on raw / audited / pooled data; auxiliary losses and augmentation implemented | Pre-registered hypotheses and evaluation protocol shared with the Programme Director |
| M11 | Generalization results on unseen PartNet-Mobility categories; violation-rate-vs-failure analysis | O3 primary results |
| M12 | Ablations by axiom family; ontology v1.0 with SC 42 contribution filed [confirm route]; toolkit v1.1; stretch transfer to one non-robotics annotation set | Final report; methods paper and audit/data paper submitted; handover plan with an Activation Partner and AXIOMALITY's Passport |

## Risks and mitigations
- **UK-majority rule cannot be met** → the proposal is not submitted under this call; the concept paper is kept for a future programme call and the Toronto/Harvard routes in the registry carry the program instead.
- **Fast audit tier is not complete for some axiom families** → those families are audited by the prover on a sample and reported as estimated rates with intervals.
- **No generalization gain in O3** → the audit and corpus (O2) are the primary deliverables and stand alone; a null result on O3 with a verified violation signal is still a result ARIA values over papers.
- **Founder conflict of interest with AXIOMALITY** → declare it on the form; keep the company's role in-kind unless ARIA guidance permits a costed subcontract; ring-fence IP in the collaboration agreement.
