# Stipend plan and milestone timeline — CRA Trustworthy AI Research Fellowship (2027–28 cohort)

## Money

No budget is requested. The fellowship pays a fixed **USD 17,000 stipend** (cohort 2; [verify for cohort 3]) and separately covers travel, lodging and meals for the four-day Field School. Whether the stipend is restricted to research use or paid to the fellow personally was not recorded [verify]. The allocation below is the applicant's own plan for the stipend if it is unrestricted; every figure is [proposed] and sums to USD 17,000.

| Use | [Proposed] USD | Justification |
|---|---|---|
| Compute for the dataset audit (cloud CPU hours for Datalog/SMT bulk checking; theorem-proving residuals) | [5,000] | Project 2.1 checks millions of part instances across five datasets; host-institution compute [confirm availability] may reduce this |
| Interview compensation and transcription for dataset maintainers and annotation workers | [2,500] | Project 2.3; [number] participants at [rate]; consent and compensation per host IRB [confirm whether review is required] |
| Travel to one ISO/IEC JTC 1/SC 42 meeting to present the parts ontology for contribution | [3,500] | Impact: the ontology is offered to the AI standards committee where the applicant already participates |
| Travel to one AI or robotics venue to present the audit results | [3,000] | Dissemination of the O2 audit paper |
| Open-data hosting, DOIs and evidence-pack archiving | [1,000] | All axioms, mappings, corrected annotations and evidence packs released openly |
| Contingency (licences, books, second-simulator costs) | [2,000] | [Second simulator] licence if not open source |
| **Total** | **17,000** | |

No salary is charged: the fellowship is held alongside the Harvard (or other US) appointment, which continues to pay salary and benefits [confirm]. No company funds or AXIOMALITY resources are used for the research outputs, which are released under an open licence.

## Milestone timeline (fellowship year; months numbered from the cohort start date [date unknown])

| Month | Milestone | Objective / project | Deliverable |
|---|---|---|---|
| M1 | Cohort start; mentor matched; Project 2.3 protocol drafted and submitted for ethics review if required | — | Mentoring plan; ethics submission [if required] |
| M1–M4 | Parts module axiomatized as a TUpper extension; consistency and module relationships verified with Prover9/Mace4; representation theorems for three dataset schemas | 1.1 | Ontology v0.1 in Common Logic; proofs and counter-models |
| M3–M5 | PSL integration for state change under manipulation (detachment, assembly) | 1.2 | Ontology v0.2 |
| M4–M8 | Two-tier audit pipeline (Datalog/SMT + first-order residuals) built and validated on sampled hard cases | 2.1 | Audit toolkit v1; agreement study between SMT subset and full checking |
| [Field School dates] | Four-day in-person Trustworthy AI Field School | — | Revised Project 2.3 design incorporating cohort and mentor input |
| M7 | First audit results across five datasets: violation rate by axiom family and by source | 2.1, 2.3 | Internal report; draft audit paper |
| M5–M10 | Maintainer and annotator interviews; coverage-by-source analysis | 2.3 | Qualitative findings; coverage tables |
| M6–M9 | Corrected annotations, proved label mappings, merged ontology-aligned corpus, evidence packs mapped to NIST AI RMF Map/Measure and EU AI Act Article 10 | 2.2 | Public data release with DOIs |
| M8–M12 | Constraint-based training and augmentation experiments in SAPIEN and [second simulator]; ablations by axiom family | 3.1 | Methods results with confidence intervals |
| M9–M12 | Verification-in-the-loop evaluation; violation rate as failure signal; model-card reporting format | 3.2 | Protocol and reference implementation |
| M10 | Ontology offered to ISO/IEC JTC 1/SC 42 and deposited in COLORE | Impact | Committee contribution; repository entry |
| M12 | Audit/data paper submitted to an AI or robotics venue; methods paper drafted; fellowship report to CRA | 2, 3 | Two manuscripts; report |

## Dependencies and risks

- The timeline assumes the fellowship year coincides with a continuing US appointment; if the appointment ends in spring 2027, the plan is not executable under this program (see README decision tree).
- Project 2.3 depends on access to dataset maintainers and annotation workers; if access is refused, the coverage-by-source analysis proceeds from published documentation alone and the interview component is reported as attempted.
- Compute for Project 2.1 may exceed the proposed allocation on real-robot corpora; the five-dataset scope is ordered so that the three synthetic datasets (PartNet, PartNet-Mobility, GAPartNet) are audited first.
