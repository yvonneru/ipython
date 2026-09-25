# Budget and timeline — Alliance International Collaboration grant

Constraints (registry and Form 101 instructions): annual request up to CAD 100,000; duration up to three years; the international collaborator's own annual support for the joint work, converted to CAD, must be at least equal to the NSERC request and is stated in the budget justification. No Canadian cash match. All figures below are [bracketed] placeholders: no dollar amount in this file is confirmed except the CAD 100,000 ceiling and the registry's note that a postdoctoral salary of about CAD 70,000 plus benefits fits inside it.

## 1. Requested budget (CAD, per year)

| Line | Year 1 | Year 2 | Year 3 | Justification |
|---|---|---|---|---|
| Postdoctoral fellow salary — Dr. Ru | [MIE scale] | [ ] | [ ] | Leads O1–O3 day to day; co-supervises graduate students; link to the Harvard team. Registry note: ~CAD 70,000 fits the ceiling but leaves little else |
| Benefits on the postdoctoral salary | [U of T rate × salary] | [ ] | [ ] | Mandatory employer costs |
| PhD student stipend (PhD1) | [ ] | [ ] | [ ] | Theme 1 articulation axioms; Theme 3 failure prediction; exchange visit to Harvard; net of departmental and external awards |
| MASc student stipend (MASc1) | [ ] | [ ] | — | Theme 1 translation definitions; Theme 2 audit tiers |
| Undergraduate summer students (2 × 16 weeks) | [ ] | [ ] | [ ] | Data adapters (LeRobot, RLDS, ROS 2), audit runs; one position reserved for an equity-deserving-group applicant |
| Travel — Toronto–Boston exchanges | [ ] | [ ] | [ ] | [4–8] weeks per graduate student per year in the Harvard group; Dr. Ru [two] short visits per year |
| Travel — conferences | [ ] | [ ] | [ ] | Two presentations per year (one ML/robotics venue, one applied-ontology venue) |
| Compute and storage | [ ] | [ ] | [ ] | GPU time for policy training beyond Vector / Digital Research Alliance allocations; storage for the merged corpus |
| Dissemination and standards | [ ] | [ ] | [ ] | Open-access charges; one ISO/IEC JTC 1/SC 42 meeting per year for the PhD student or Dr. Ru |
| **Total** | **≤ 100,000** | **≤ 100,000** | **≤ 100,000** | |

Sizing rule: set the total to the lesser of CAD 100,000 and the collaborator's annual contribution in CAD. If the collaborator's committed support is below the salary line, either reduce the request to match (and fund the difference from [Prof. Grüninger's Discovery Grant / a CPRA award, if won]) or drop the graduate stipends. If both CPRA and this grant succeed, the postdoctoral salary line moves to CPRA and this budget shifts to graduate students, travel and compute [check NSERC rules on holding a CPRA alongside Alliance-funded stipend top-ups].

## 2. International collaborator's contribution (stated in the budget justification, CAD)

| Item | Amount per year | Source |
|---|---|---|
| Personnel time on the joint project | [ ] | [agency, grant title, number, end date] |
| Robot platform / laboratory access | [ ] | [in-kind] |
| Datasets and compute | [ ] | [ ] |
| Hosting of visiting Toronto students | [ ] | [in-kind] |
| **Total (must be ≥ NSERC request)** | [ ] | |

Convert at [Bank of Canada rate on the date of the letter]; state the rate and date.

## 3. In-kind and other support (Canadian side)

- Semantic Technologies Laboratory: verification infrastructure (COLORE tooling, Prover9/Mace4, SMT), laboratory space.
- Vector Institute: HQP affiliations and compute [confirm that affiliations are available to MIE trainees and whether Prof. Grüninger needs a Vector faculty affiliate as co-sponsor].
- University of Toronto Robotics Institute: simulation environments and seminar community [confirm with co-applicant, if named].
- Prof. Grüninger's Discovery Grant [confirm it is active and can co-fund graduate students].

## 4. Milestone timeline (36 months from [1 April 2027])

| Months | Toronto (Grüninger, Ru, PhD1, MASc1) | Harvard ([collaborator]) | Joint deliverable |
|---|---|---|---|
| 1–4 | Parts ontology axiomatized as a TUpper extension with PSL; consistency and non-triviality proved; annotation schemas of PartNet, PartNet-Mobility and GAPartNet analysed | Kick-off; data-sharing agreement; [datasets] transferred | Ontology v0.1 in a shared repository |
| 4–8 | Representation theorems for the three schemas; Datalog/SMT tier of the audit pipeline; first audit results | [Second-domain schema] analysed with Dr. Ru | M8: first quantitative audit; ontology submitted to COLORE |
| 8–12 | Prover tier for hard cases; ablations by axiom family; workshop paper | PhD1 exchange visit 1; toolkit trial on [Harvard domain] | M12: open release of ontology v1 and audit toolkit |
| 12–18 | Audit extended to AgiBot World, Open X-Embodiment, DROID; corrected annotations and proved mappings | [Real-robot data] audited | M18: merged ontology-aligned corpus released; data/audit paper submitted |
| 18–24 | Pooled-data and constraint-guided augmentation experiments in SAPIEN [and second simulator] | Evaluation design; MASc1 exchange visit | M24: methods paper submitted; MASc1 thesis |
| 24–30 | Auxiliary-loss training; verification-in-the-loop evaluation | [Real-robot validation] of trained policies | M30: robotics-venue paper submitted |
| 30–36 | Contribution of the parts module to ISO/IEC JTC 1/SC 42; applied-ontology paper; PhD1 candidacy/thesis progress | Joint workshop or tutorial proposal | M36: final report; standard contribution filed; Dr. Ru's faculty applications supported by three years of joint output |

## 5. Risks to the budget and schedule

- Decision timing: if NSERC's decision arrives after [April 2027], Dr. Ru's appointment start slips or is bridged by [CPRA / departmental funds]; state the intended start as "on award" if the research office advises.
- Collaborator funding below the ceiling: reduce request (see sizing rule).
- Postdoctoral salary consumes most of the ceiling: the graduate student lines depend on [Discovery Grant] co-funding.
- Real-robot validation depends on the Harvard platform; the simulation results in SAPIEN stand on their own if access is delayed.
