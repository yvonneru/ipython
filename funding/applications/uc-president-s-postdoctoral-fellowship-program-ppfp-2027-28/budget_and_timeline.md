# Budget and timeline — UC President's Postdoctoral Fellowship 2027–28

## Budget
No budget is requested; PPFP is a fixed award. Figures found 2026-09-25 (ppfp.ucop.edu, 2026 award year; verify the 2027 figures when the call posts): salary starting at about **USD 69,209** per year depending on field and experience, plus **USD 5,000** for research and professional development, plus benefits; appointment of **one year with a possible second year** [confirm the renewal rule and the number of years on the terms-of-award page]. Compute and data: the mentor's group [SAPIEN / PartNet-Mobility infrastructure at UC San Diego — confirm]; campus GPU allocations [name]; NAIRR / ACCESS allocations transferred or re-applied from the compute bundle package [confirm portability]. The USD 5,000 is planned as: one robotics-venue conference (≈USD 2,500), one FOIS/JOWO or KR-venue conference (≈USD 2,000), and ISO/IEC JTC 1/SC 42 meeting participation (≈USD 500, remote where possible) [applicant to adjust].

AXIOMALITY is not part of this application. The CEO role must be disclosed to the host campus under its outside-activity policy and to PPFP if asked [decide the arrangement by 30 Nov 2026 per STRATEGY.md and disclose it identically everywhere].

## Milestone timeline (Sept 2027 start assumed; [confirm the start window])

| Month | Milestone | Objective | Output |
|---|---|---|---|
| M1–2 (Sept–Oct 2027) | Parts-ontology modules (rigid, articulated, functional, assembly) drafted as TUpper extensions; PSL fluents for attach/detach/articulation; competency questions extracted from the PartNet, PartNet-Mobility, GAPartNet, AgiBot World, Open X-Embodiment and DROID schemas | O1 | Common Logic modules in a public repository |
| M3–4 | Verification: consistency and non-triviality (Prover9/Mace4); representation theorems for at least PartNet and PartNet-Mobility schemas | O1 | Theorem obligations and counter-models checked in; first COLORE contribution |
| M4–6 | Two-tier audit pipeline (Datalog/SMT bulk; first-order proving for residuals); first audit of PartNet-Mobility with the maintainers [confirm mentor] | O2 | Violation rates and patterns by axiom family; audit toolkit v0 |
| M6–8 | Audit extended to the remaining datasets; cross-dataset mappings proved meaning-preserving; corrected annotations | O2 | Data release; audit/data paper submitted (robotics or ML venue) |
| M8–12 | Pooled ontology-aligned corpus; baseline policy training in SAPIEN; renewal case assembled | O2→O3 | Merged corpus; Year-1 report to PPFP and mentor |
| Y2 M13–18 (if renewed) | Parthood-constraint losses; constraint-guided augmentation; held-out-category experiments; ablations by axiom family | O3 | Methods paper (ML venue) |
| Y2 M18–24 | Verification-in-the-loop evaluation protocol; second simulator or benchmark suite [confirm]; SC 42 contribution; faculty applications | O3 | Robotics-venue paper; ISO/IEC JTC 1/SC 42 contribution; job-market package |

Twelve-month fallback (if only one year is awarded): the 12-month template from the research program — M1–4 ontology and schema mappings; M4–8 audit pipeline, results across the datasets, release; M8–12 pooling and policy experiments, methods paper, toolkit — with O3 reported as preliminary results rather than a full study.

## Dependencies and risks
- Mentor commitment by [10 Oct 2026] (gating; STRATEGY.md next action).
- Dataset licences: register at shapenet.org, partnet.cs.stanford.edu and sapien.ucsd.edu and save the accepted terms (already scheduled in STRATEGY.md).
- Audit at dataset scale: the Datalog/SMT tier is the mitigation; theorem proving is confined to residual cases and UNKNOWN/timeout is reported rather than hidden.
- Null result on O3: the audit and aligned corpus (O1–O2) are publishable on their own; O3 is written so that a null result is informative.
