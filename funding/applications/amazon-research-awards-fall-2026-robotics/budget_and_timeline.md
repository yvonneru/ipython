# Budget and timeline — Amazon Research Awards, Fall 2026

## Budget

ARA awards have two components entered in the portal: a **cash gift** (one-time, unrestricted, paid to the University of Toronto for distribution; "may not be used for indirect expenses which are not allocable, reasonable, adequately documented, and consistent with established policies") and **AWS Promotional Credits**. The FAQ sizes a typical cash budget at one postdoctoral researcher or one to two graduate students for one year plus some conference travel and equipment. The Fall 2025 ceiling was USD 100,000 [confirm the Fall 2026 ceiling and whether it is cash + credits combined or cash alone]. **No dollar figure below is set; every amount must come from MIE finance and the call text.** Request the ceiling only if the justified lines reach it.

| Line | Justification | Amount |
|---|---|---|
| Postdoctoral researcher (Dr. Ru), partial salary and benefits | Leads Themes 1–3 full-time for 12 months. If a salary award (CPRA, Vector, DSI) is held concurrently, this line drops and shifts to the MASc, compute and travel lines [confirm concurrency with U of T]. | [USD — months × MIE postdoc rate incl. benefits, converted at the rate MIE finance uses] |
| MASc student (MASc1), stipend | Owns the lattice-characterization question (Theme 1) and the audit adapters (Theme 2) for 12 months. | [USD — MIE MASc stipend rate] |
| Conference travel | Presentation of the audit/data paper and the methods paper (one AI/robotics venue, one applied-ontology venue, e.g., FOIS); one ISO/IEC JTC 1/SC 42 meeting to contribute the ontology. | [USD — 2–3 trips at U of T rates] |
| Equipment / storage | Local workstation storage for staged copies of the five datasets and prover logs; no other equipment. | [USD] |
| **Cash subtotal** | Within ceiling; no non-allocable indirect costs [confirm U of T's overhead position on corporate gifts]. | [USD] |
| **AWS Promotional Credits** | Theme 2: Datalog/SMT tier over millions of part instances on EC2 batch fleets, datasets in S3, prover-tier jobs with time budgets; Theme 3: GPU instances for policy training and SAPIEN evaluation across held-out PartNet-Mobility categories with ablations by axiom family. [Size with the Robotics Institute advisor: instance types, hours, storage volume; state the assumptions in the justification.] | [USD credits] |

Justification text for the portal (≤120 words, adjust to the numbers): *The cash gift supports the named postdoctoral researcher [and one MASc student] for twelve months, travel to present the audit/data and methods papers and to contribute the ontology to ISO/IEC JTC 1/SC 42, and local storage for staged datasets. AWS credits fund the compute-heavy audit — an embarrassingly parallel SMT/Datalog tier over millions of part instances on EC2 with datasets staged in S3, and a theorem-proving tier with explicit time budgets — and the GPU training and simulation runs for the generalization experiments. All code, axioms, corrected annotations and an AWS runbook will be released so the audit can be rerun on other accounts.*

## Pre-award timeline (2026)

| When | Milestone |
|---|---|
| 1–2 Oct 2026 | Fall 2026 call checked; topics, ceiling, template, deadline recorded; emails 1, 2, 5 sent |
| 10 Oct 2026 | Prof. Grüninger agrees to be PI |
| 17 Oct 2026 | U of T handling (gift vs award; MRA; overhead; contacts) confirmed |
| 24 Oct 2026 | Full draft to PI and Theme 3 advisor; PI CV received; budget lines set with MIE finance; GPU sizing received |
| ~30 Oct 2026 | Institutional sign-off if required |
| ~5–9 Nov 2026 | PI submits in the ARA portal |
| ~12 Nov 2026, 11:59 PM PT [confirm] | Expected close |
| ~Feb–Mar 2027 | Decision (≈3 months after close) |
| Apr 2027 or later | Dr. Ru starts at MIE; project month 1 |

## Project timeline (12 months, from Dr. Ru's start)

| Months | Theme | Milestone | Output |
|---|---|---|---|
| 1–4 | 1 Parts | Rigid, articulated, functional and assembly parthood modules in Common Logic; consistency and non-triviality (Prover9/Mace4); module relationships proved or refuted; constitution mappings applied to kinematic/functional/visual decompositions; PSL integration for parthood change; schema mappings for five datasets drafted | Ontology v0.9 in COLORE; technical report 1 |
| 4–8 | 2 Audit | Adapters (PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World; LeRobot/RLDS); Datalog/SMT tier on EC2; prover tier with time budgets; first audit results and violation rates by dataset, category and source | Audit toolkit v1 (open licence); corrected annotations and violation reports released; audit/data paper submitted |
| 6 | — | **Decision point:** if the SMT fragment misses violations the prover finds, expand the prover tier and accept a smaller bulk set | — |
| 8–12 | 2–3 Audit / Learning | Cross-dataset mappings proved meaning-preserving; merged ontology-aligned corpus; parthood axioms compiled to auxiliary losses; Mace4-model augmentation in SAPIEN; H1–H3 experiments with ablations by axiom family; verification-in-the-loop protocol | Merged corpus release; methods paper submitted; technical report 2 (AWS runbook); ontology contributed to ISO/IEC JTC 1/SC 42 |
| 10 | — | **Decision point:** if H1 fails on the first backbone, switch to the agreed alternative; H2 and H3 do not depend on H1 | — |
| 12 | — | Final report to Amazon; talks at the U of T Robotics Institute and [Amazon research contact's group, if offered] | — |

## Resources not requested from Amazon

| Resource | Source | Status |
|---|---|---|
| Verification pipeline (COLORE, Common Logic tooling, Prover9/Mace4) | Semantic Technologies Laboratory, MIE | Available [confirm access from spring 2027] |
| Dataset licences permitting release of corrected annotations and a merged corpus | Public licences of the five datasets | [Confirm each licence; see compute-and-data-access-bundle/dataset_licences.md] |
| Policy backbone and second simulator | Robotics Institute advisor | [Advisor to confirm] |
| Postdoc salary if a fellowship is awarded | CPRA / Vector / DSI | [Pending; re-line the ARA budget if awarded] |
