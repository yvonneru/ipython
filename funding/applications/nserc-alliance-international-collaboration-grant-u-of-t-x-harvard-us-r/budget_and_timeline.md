# Budget and timeline — Alliance International Collaboration grant

Constraints (registry and Form 101 instructions as read from search summaries on 2026-09-25; verify on the official page): annual request up to CAD 100,000; duration up to three years; the grant funds the Canadian component of a project newly funded by the international collaborator's national agency (award letter dated no earlier than 120 days before submission; copy of the international proposal and award letter attached); each side's budget must be at least 25% of the total project budget; the international team's annual support, converted to CAD, is stated in the budget justification. No Canadian cash match. All figures below are [bracketed] placeholders: no dollar amount in this file is confirmed except the CAD 100,000 ceiling and the registry's note that a postdoctoral salary of about CAD 70,000 plus benefits fits inside it — which means the postdoctoral line will take most of the ceiling. **The draft therefore funds the postdoc and one MASc student from the grant and lists PhD1 and the undergraduates as other support; a budget that promises a postdoc, a PhD, a MASc, two undergraduates, travel and compute out of CAD 100,000 would not be believed.**

## 1. Requested budget (CAD, per year)

| Line | Year 1 | Year 2 | Year 3 | Justification |
|---|---|---|---|---|
| Postdoctoral fellow salary — Dr. Ru | [MIE scale] | [ ] | [ ] | Leads O1–O3 day to day; co-supervises graduate students; link to the Harvard team. Registry note: ~CAD 70,000 fits the ceiling but leaves little else |
| Benefits on the postdoctoral salary | [U of T rate × salary] | [ ] | [ ] | Mandatory employer costs |
| PhD student stipend (PhD1) | [other support] | [other support] | [other support] | Theme 1 articulation axioms; Theme 3 failure prediction; exchange visit; funded from [Prof. Grüninger's Discovery Grant / departmental award — confirm]; listed as other support, not requested |
| MASc student stipend (MASc1) | [ ] | [ ] | — | Theme 1 translation definitions; Theme 2 audit tiers |
| Undergraduate summer students (2 × 16 weeks) | [other support] | [other support] | [other support] | Data adapters (LeRobot, RLDS, ROS 2), audit runs; one position reserved for an equity-deserving-group applicant; funded from [NSERC USRA / MIE summer research program — confirm] |
| Travel — Toronto–Boston exchanges | [ ] | [ ] | [ ] | [2–4] weeks per graduate student per year in the international team's group; Dr. Ru [two] short visits per year |
| Travel — conferences | [ ] | [ ] | [ ] | Two presentations per year (one ML/robotics venue, one applied-ontology venue) |
| Compute and storage | [ ] | [ ] | [ ] | GPU time for policy training beyond Vector / Digital Research Alliance allocations; storage for the merged corpus |
| Dissemination and standards | [ ] | [ ] | [ ] | Open-access charges; one ISO/IEC JTC 1/SC 42 meeting per year for the PhD student or Dr. Ru |
| **Total** | **≤ 100,000** | **≤ 100,000** | **≤ 100,000** | |

Sizing rule: set the total to the lesser of CAD 100,000 and [the international team's annual support in CAD], and check that both sides are ≥ 25% of the total project budget. The lines must sum to the request. If the postdoctoral line leaves less than [amount] for the rest, move the MASc stipend to [Discovery Grant] support and keep travel and compute. If both CPRA and this grant succeed, the postdoctoral salary line moves to CPRA and this budget shifts to graduate students, travel and compute [check NSERC rules on holding a CPRA alongside Alliance-funded stipend top-ups].

## 2. International collaborator's contribution (stated in the budget justification, CAD)

| Item | Amount per year | Source |
|---|---|---|
| Personnel time on the joint project | [ ] | [agency, grant title, number, end date] |
| Robot platform / laboratory access | [ ] | [in-kind] |
| Datasets and compute | [ ] | [ ] |
| Hosting of visiting Toronto students | [ ] | [in-kind] |
| **Total (each side ≥ 25% of the total project budget; request ≤ this total)** | [ ] | [agency award letter dated no earlier than 120 days before submission] |

Convert at [Bank of Canada rate on the date of the letter]; state the rate and date.

## 3. In-kind and other support (Canadian side)

- Semantic Technologies Laboratory: verification infrastructure (COLORE tooling, Prover9/Mace4, SMT), laboratory space.
- Vector Institute: HQP affiliations and compute [confirm that affiliations are available to MIE trainees and whether Prof. Grüninger needs a Vector faculty affiliate as co-sponsor].
- University of Toronto Robotics Institute: simulation environments and seminar community [confirm with co-applicant, if named].
- Prof. Grüninger's Discovery Grant [confirm it is active and can co-fund graduate students].

## 4. Milestone timeline (36 months from [1 June 2027 — STRATEGY §1.8 rule 3: May–June 2027 or later, never April])

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

- Decision timing: if NSERC's decision arrives after [June 2027], Dr. Ru's appointment start slips or is bridged by [CPRA / departmental funds]; state the intended start as "on award" if the research office advises.
- The 120-day rule: the international team's award letter must post-date [28 July 2026] for a 25 November submission. If the collaborator's award comes later, target the next deadline ([February/March 2027 — confirm]) rather than force this one.
- Collaborator funding below the ceiling: reduce request (see sizing rule).
- Postdoctoral salary consumes most of the ceiling: PhD1 and the undergraduates are other support; only the MASc stipend is requested, and it is the first line to drop.
- Real-robot validation depends on the Harvard platform; the simulation results in SAPIEN stand on their own if access is delayed.
