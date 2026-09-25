# Reviewer brief — RAC 2027 RRG (there are no referees; this is what the reviewers see)

*RAC has no reference letters and no nominator: the PI submits a form and it is scored by an Alliance science committee in the PI's discipline and by a technical review. This file is (A) the brief for Prof. Grüninger on what the reviewers score, so that his edits and his "past usage" section land where they count, and (B) a one-paragraph note for anyone the PI names as a collaborator on the form (e.g. a Robotics Institute faculty member), who may be asked to confirm their role but writes no letter. Criteria and weights below are as best known from prior cycles and the Fast Track rule; verify against the RAC 2027 Application Guide [not obtainable by search this session].*

## A. For the PI

**What the program is.** The Alliance's annual competition for compute, GPU, storage and cloud on the national systems beyond the Rapid Access Service defaults. RRG is the stream for individual faculty PIs and their sponsored users. Allocation year 1 Apr 2027 – 31 Mar 2028; renewable; Fast Track renewal for up to two further years if the science score exceeds 2.0 out of 5 (confirmed on alliancecan.ca). RAC 2027 closes **3 November 2026** (confirmed).

**What the form asks.** Project title and summary; research description [length limit — verify]; resource request by type with technical justification and evidence of scaling; HQP list with CCDB usernames; past usage and progress (first request: state RAS usage or "none"); publications from prior allocations; the PI's CCV [variant — verify]. Text fields; the draft in proposal.md is sized to be pasted section by section.

**What reviewers score (as best known).**
- *Science review* (score out of 5 — the scale is confirmed by the Fast Track threshold): quality and significance of the research, feasibility, HQP training and productivity. Committees are discipline-based; the project sits in computing science / AI with an engineering PI [choose the discipline committee on the form consistently with the CPRA subject-code decision].
- *Technical review*: whether the requested resources are justified by the described workload, whether the software runs on the target system, whether the storage categories are used correctly, and whether the group has demonstrated it can use what it asks for. First-year GPU requests from groups without RAC history are routinely scaled back; a derivation that can be cut line by line survives better than a round number.
- [Weights, and whether HQP/productivity is scored separately — read the Guide.]

**The four points that help most.**
1. The research description reads as the PI's program, not a postdoc's side project: it opens with COLORE, TUpper/ISO 21838-4 and the lab's dataset-evaluation work, and places Dr. Ru's theory (the two Synthese submissions) inside it. Keep that framing; edit the voice to your own.
2. Every number is derived from the experimental matrix and the audit pass count, with a stated worst case (budget_and_timeline.md). If the pilot at Harvard yields a measured GPU-hours-per-run figure before 30 Oct, it replaces the [24] and the request is recomputed.
3. The "past usage" section is honest and non-empty: RAS usage from Dr. Ru's sponsored role (Oct 2026 onward) plus the Harvard pilot results, and the statement that the CPU half continues the lab's existing theorem-proving workflow.
4. The outputs are public and cross-disciplinary (ontology to COLORE and SC 42; audit reports, mappings and an Apache-2.0 validator; toolkit reusable for CAD, BIM and medical-image labels) — the Alliance is a national, multi-disciplinary facility and scores reuse.

**What to avoid.** A GPU ask above ~[10] RGU-years in year one; unnamed storage categories; software that has not been shown to run on H100 nodes (SAPIEN and Isaac Lab need CUDA/RTX-capable GPUs — state that Killarney/Trillium-GPU qualify [verify]); any mention of company use.

**Deadline for your part.** Edits, past usage, HQP list and CCV by 27 Oct; submit by 30 Oct; hard close 3 Nov 2026.

## B. For a named collaborator (no letter required)

Prof. Grüninger is submitting a RAC 2027 RRG request (Alliance compute, closes 3 Nov 2026) for a program led by Dr. Yi Ru, who joins his laboratory as a postdoctoral fellow in [April 2027 or later]: a verified ontology of object parts, an audit of the part annotations of PartNet, PartNet-Mobility, GAPartNet, AgiBot World, Open X-Embodiment and DROID against it, and policy-training experiments in SAPIEN [and Isaac Lab] that use the ontology as an inductive bias and report ontology-violation rate alongside task success. Your name appears as a collaborator on the simulation component [confirm wording with you first]. Nothing is required from you for the submission; if the Alliance asks you to confirm the collaboration, a one-line reply suffices. The allocation is group-held and would run 1 Apr 2027 – 31 Mar 2028.
