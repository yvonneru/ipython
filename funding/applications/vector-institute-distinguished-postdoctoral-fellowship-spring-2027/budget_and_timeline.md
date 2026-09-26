# Timeline and resources — Vector Institute Distinguished Postdoctoral Fellowship, Spring 2027 cohort

## Budget

No budget is requested from the applicant. The fellowship pays the fellow's salary and benefits (amount set by Vector; third-party listings and Glassdoor show roughly CAD 49–65k base [confirm on the live posting]) and provides Vector compute and a research environment. The standard term is 1–2 years with a possible extension to 3 (Vector posting, checked 2026-09-25); the plan below is written for 24 months and does not assume the extension. The only resource statements the application may need are the compute and data-access notes below, to be sized with the sponsor.

| Resource | Need | Source | Status |
|---|---|---|---|
| Theorem proving and model finding (Prover9, Mace4, SMT) for Themes 1–2 | CPU-bound; modest | Semantic Technologies Laboratory (MIE) workstations; Vector CPU nodes | Available [confirm access to the STL verification pipeline from spring 2027] |
| Bulk audit of five part-level datasets (millions of part instances) | Storage for PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World; CPU for Datalog/SMT | Vector storage and CPU; public dataset licences | [Confirm dataset licences permit release of corrected annotations and a merged corpus] |
| Policy training and evaluation in SAPIEN and [second simulator] (Theme 3) | GPU-hours [estimate to be sized with the sponsor — do not guess in the application] | Vector GPU cluster | [Sponsor to advise] |
| Open release (ontology, mappings, corpus, toolkit) | Repository hosting; COLORE contribution | COLORE [confirm current repository URL]; GitHub | Available |

## Pre-award timeline (2026–27)

| When | Milestone |
|---|---|
| 2 Oct 2026 | Emails 1 (Grüninger) and 3 (Vector office) sent alongside the CPRA follow-up |
| 15 Oct 2026 | Grüninger reply: co-sponsorship, Vector affiliate status, sponsor candidates |
| Nov–Dec 2026 | Meetings with 2–3 candidate sponsors (email 2); agree policy backbone and second simulator for Theme 3 |
| 15 Jan 2027 | Vector sponsor agreed in writing |
| 31 Jan 2027 | Full draft to sponsor, co-sponsor and referees (email 6) |
| 14 Feb 2027 | Reference letters in hand (or sent to Vector) |
| 21 Feb 2027 | Single PDF assembled and submitted |
| 28 Feb 2027, 23:59 EST | Vector deadline — application and all three letters received in full; late applications roll to the Autumn cohort |
| March 2027 | Committee review; [decision date unknown] |
| 31 Aug 2027 | Fallback: Autumn 2027 cohort |

## Fellowship timeline (24 months, from [April 2027 or later])

| Months | Theme | Milestone | Output |
|---|---|---|---|
| 1–4 | 1 Parts | Rigid, articulated, functional and assembly parthood modules axiomatized in Common Logic; consistency and non-triviality verified (Prover9/Mace4); representation theorems drafted | Ontology v0.9 in COLORE |
| 3–8 | 1 Parts / 2 Audit | Constitution mappings applied to kinematic, functional and visual decompositions; PSL integration for parthood change under manipulation; dataset adapters (PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World); Datalog/SMT compilation of the axioms | Audit pipeline v1; first audit results (Y1 open questions answered) |
| 6–12 | 2 Audit | Cross-dataset label mappings proved meaning-preserving; corrected annotations; merged, ontology-aligned corpus | Public data release; audit/data paper submitted (ML or robotics venue) |
| 8–16 | 3 Learning | Part-aware policy backbone agreed with sponsor; axioms compiled to semantic-loss / fuzzy-logic terms; constraint-guided augmentation from Mace4 models instantiated in SAPIEN; pooled-data experiments (H3) | Methods paper draft; toolkit v1 |
| 12–20 | 3 Learning | Constraint-based training on held-out PartNet-Mobility categories (H1); verification-in-the-loop evaluation, violation rate vs task success (H2); ablations by axiom family | ML-venue paper submitted |
| 16–24 | 2–3 | Extension to real-robot corpora (AgiBot World, DROID; Open X-Embodiment if licences permit); second simulator; toolkit release; ontology contributed to ISO/IEC JTC 1/SC 32 | Robotics-venue paper; toolkit v2; standards contribution |
| 20–24 | — | Consolidation; talks at Vector and the U of T Robotics Institute; faculty applications | — |

## Decision points

- Month 8: if the SMT-compiled fragment misses violations the prover finds, expand the prover tier and accept a smaller bulk set rather than weaken the audit.
- Month 14: if H1 fails on the first backbone, switch backbone (agreed alternative with sponsor) before month 16; H2 and H3 do not depend on H1.
- Concurrency: if CPRA (results 31 Mar 2027) or DSI is also awarded, seek Vector's approval to hold them together before accepting either [policy unconfirmed].
