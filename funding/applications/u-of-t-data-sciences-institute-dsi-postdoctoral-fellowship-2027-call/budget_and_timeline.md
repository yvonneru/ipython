# Budget and timeline — DSI Postdoctoral Fellowship, 2027 call

## Budget

No budget is requested or submitted. The fellowship is a fixed-value award: CAD 60,000 per year plus benefits (registry figure, not re-verified), for up to two years [confirm on the 2027 page the value, the payment route, whether a research or travel allowance is included, and whether the co-supervisors are expected to top up the salary or cover benefits]. Costs not covered by the fellowship and how they are met:

| Need | Source | Note |
|---|---|---|
| Verification infrastructure (COLORE, Prover9/Mace4, Common Logic tooling) | Semantic Technologies Laboratory (Prof. Grüninger) | in place |
| Compute for the audit pipeline (Datalog/SMT over millions of part instances) | Laboratory workstation / [U of T or Compute Ontario allocation — confirm] | Y1 |
| Compute for policy training and simulation (Theme 3; SAPIEN and [second simulator]) | [Second co-supervisor's allocation / Vector Institute affiliation — confirm]. Fallback if unavailable: audit already-released policies for violation rate (no training) | Y2-heavy |
| Conference travel (one AI/ML or robotics venue per year) | [Fellowship allowance if any / co-supervisors' grants / DSI travel support — confirm] | [amount] |
| Data hosting for the released corpus and toolkit | [U of T Dataverse / GitHub / Zenodo — free tiers] | Y1–Y2 |

## Award window and concurrency

- Start: between 1 May and 1 December of the award year (DSI page, per search summary; verify for 2027). Planned start 1 May 2027 (the applicant's earliest Toronto start is April 2027). Decisions: [verify; previous calls decided in the spring].
- May not be held concurrently with another major fellowship (Vector Distinguished Postdoctoral Fellowship, Schmidt AI in Science; NSERC CPRA [verify]). If more than one succeeds, the applicant chooses at offer stage; see README.md.

## Milestone timeline (24 months; Y1 is a complete 12-month program on its own)

| Months | Theme / Project | Milestone | Output |
|---|---|---|---|
| 1–3 | 1.1 Parts ontology | Four parthood modules (rigid, articulated, functional, assembly) axiomatized in Common Logic; consistency and non-triviality established with Prover9/Mace4 | Ontology v0.1 in COLORE (internal) |
| 3–5 | 1.2 Constitution mappings | Parthood-preserving mappings between the modules proved; PSL integration for parthood change under manipulation; representation theorems for at least two modules; annotation schema mappings for the five core datasets | Ontology v1.0; theory note; schema-mapping document |
| 4–8 | 2.1 Audit pipeline | Adapters for PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World [Open X-Embodiment, DROID if time]; SMT compilation of the decidable fragment; prover fallback; coverage reporting by source, category and region; first audit across five datasets | Audit results v1 (violation rate and pattern per dataset) |
| 8–12 | 2.2 Cross-dataset alignment | Meaning-preserving label mappings derived and proved; corrected annotations; merged ontology-aligned corpus assembled and documented (datasheet) | Public data release; audit toolkit v1; audit/data paper submitted; **Y1 report to DSI** |
| 10–14 | 3.1 (pooling track) | Policies trained on ontology-aligned vs unaligned pooled data; transfer across part vocabularies measured in SAPIEN with confidence intervals | Interim results; methods paper on specification-based auditing submitted |
| 13–18 | 3.1 Constraint-based training | Differentiable parthood-constraint losses; constraint-guided augmentation for underrepresented categories; ablations by axiom family | Second methods paper draft |
| 17–22 | 3.2 Verification-in-the-loop evaluation | Violation-rate metric in the evaluation loop; held-out PartNet-Mobility category experiments in SAPIEN and [second simulator]; violation rate vs task failure analysis | Robotics-venue paper submitted |
| 20–24 | Dissemination | Ontology contributed to ISO/IEC JTC 1/SC 32 as a working document [verify procedure] and released under an open licence in COLORE; toolkit v2; non-robotics demonstration of the audit method (medical-image part labels or CAD assemblies) [choose with second co-supervisor]; final report | Final deliverables; faculty-application materials |

Throughout: monthly meetings with both co-supervisors; DSI community events, seminars and [workshop/tutorial contribution — verify what DSI offers fellows]; Robotics Institute seminar series; SC 32 meetings as the laboratory's representative; co-supervision of [number] graduate students on the ontology and audit components [confirm with co-supervisors].

## Pre-submission timeline (September 2026 – January 2027)

| Date | Action | Owner |
|---|---|---|
| 30 Sep 2026 | Send DSI-specific request to Prof. Grüninger (email 1); ask him to propose the second co-supervisor | Applicant |
| by 10 Oct 2026 | Send deadline/label/format/reference/concurrency questions to DSI (email 5, awards.dsi@utoronto.ca) | Applicant |
| by 15 Oct 2026 | First contact with prospective second co-supervisor(s) (email 2); send proposal and co-supervisor note | Applicant |
| by 1 Nov 2026 | Second co-supervisor confirmed; concurrency position agreed with both | Applicant / co-supervisors |
| Oct–Nov 2026 | Watch the DSI page for the next call; register for the information session | Applicant |
| early Dec 2026 | Attend information session | Applicant |
| by 15 Dec 2026 | Re-fit proposal and statement to the posted form; update CV; PhD-completion evidence in hand; full draft to both co-supervisors and any referees (emails 3, 4) | Applicant |
| 4 Jan 2027 | Co-supervisor comments incorporated | Applicant |
| 6 Jan 2027 | Additional references, if required, confirmed | Referees |
| 8 Jan 2027 | Submit | Applicant |
| 12 Jan 2027 (plan) – ~22 Jan | Applicant deadline [confirm; SGS listing shows 12 Jan, the 2026 call closed 23 Jan] | — |
| ~1 week later | Co-supervisor structured forms due [confirm] | Prof. Grüninger / second co-supervisor |
| [spring 2027] | Decisions [confirm] | DSI |
