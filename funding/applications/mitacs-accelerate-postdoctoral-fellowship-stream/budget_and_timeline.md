# Budget and timeline — Mitacs Accelerate, six units over 24 months

All Mitacs figures come from the registry entry (CAD 20,000 per 4–6 month unit; partner contributes roughly half; up to 3 units per year, up to 9 units in total). [Confirm on the official page: current unit value; partner share and whether it is subject to tax; reduced partner share for start-ups under Accelerate Entrepreneur; minimum stipend payable to a postdoctoral intern per unit; allowable research costs; U of T overhead treatment of Mitacs funds.]

## Funding summary

| Item | Per unit | Year 1 (units 1–3) | Year 2 (units 4–6) | Total (6 units) |
|---|---|---|---|---|
| Partner cash contribution | CAD 10,000 [confirm] | CAD 30,000 | CAD 30,000 | CAD 60,000 |
| Mitacs contribution | CAD 10,000 [confirm] | CAD 30,000 | CAD 30,000 | CAD 60,000 |
| **Total award** | **CAD 20,000** | **CAD 60,000** | **CAD 60,000** | **CAD 120,000** |

The award is paid to a research account at the University of Toronto administered by Prof. Grüninger and disbursed as below.

## Disbursement and justification

| Line | Per unit | 6 units | Justification |
|---|---|---|---|
| Intern stipend / salary (paid through U of T payroll, with benefits as MIE requires) | [CAD — at or above the Mitacs minimum for postdoctoral interns; confirm] | [CAD] | The intern is the sole person executing O1–O3; the stipend is the primary purpose of the award. If a salary award (CPRA, Vector, DSI, CIRTA) is held concurrently, the stipend line is reduced and the research line increased, subject to Mitacs and the paying institution's stacking rules [confirm]. |
| Compute for O3 (policy training in SAPIEN and [second simulator]; ablations by axiom family) | [CAD] (units 4–6 only) | [CAD] | GPU time for matched comparisons over held-out PartNet-Mobility categories with confidence intervals. [Source to be chosen: partner's infrastructure, Vector Institute allocation if a Vector affiliation is granted, or U of T/Compute Canada; estimate to be sized with the supervisor.] |
| Data storage and hosting for the aligned public corpus and toolkit releases | [CAD] | [CAD] | Five public datasets plus the merged corpus; releases hosted for the life of the project. |
| Open-access publication fees (audit/data paper; methods paper; robotics paper) | — | [CAD] | Three papers over 24 months per the research program's 24-month plan. |
| Travel: partner site visits; one ISO/IEC JTC 1/SC 42 meeting; one conference presentation per year | [CAD] | [CAD] | On-site time each unit (§7 of the proposal) and contribution of the ontology to SC 42. |
| **Total disbursed** | **CAD 20,000** | **CAD 120,000** | |

Notes. (1) No equipment is requested; verification runs on laboratory workstations (Prover9/Mace4, SMT solvers) and existing servers. (2) No funds go to the partner or to AXIOMALITY in either route. (3) [Route B: state the reduced partner contribution and the incubator's in-kind support, if any.] (4) [If the template requires Mitacs's own budget categories, re-map the lines above onto them.]

## Timeline (Gantt by unit; each unit is four months)

| Activity | U1 Apr–Jul 2027 | U2 Aug–Nov 2027 | U3 Dec 2027–Mar 2028 | U4 Apr–Jul 2028 | U5 Aug–Nov 2028 | U6 Dec 2028–Mar 2029 |
|---|---|---|---|---|---|---|
| Partner schema analysis; competency questions | ██ | | | | | |
| Parts ontology (four modules); verification | ██ | ██ | | | | |
| Representation theorems for public and partner schemas | | ██ | | | | |
| Audit pipeline: Datalog/SMT tier | | ██ | ██ | | | |
| Audit pipeline: first-order tier; adapters | | | ██ | | | |
| Audits: partner datasets | | ██ | ██ | ██ | | |
| Audits: five public datasets | | ██ | ██ | | | |
| Toolkit v1 at partner | | | ██ | | | |
| Merged ontology-aligned corpus; public release | | | | ██ | | |
| COLORE contribution; SC 42 proposal | | | | ██ | ██ | |
| Pooled-data experiments | | | | ██ | ██ | |
| Constraint-guided augmentation | | | | | ██ | |
| Constrained training (auxiliary losses) | | | | | ██ | ██ |
| Verification-in-the-loop evaluation protocol | | | | | | ██ |
| Papers: audit/data (U3), methods (U5), robotics (U6) | | | ██ | | ██ | ██ |
| Unit reports to partner and Mitacs | ▲ | ▲ | ▲ | ▲ | ▲ | ▲ |

## Milestones

| End of | Milestone | Verifiable by |
|---|---|---|
| Unit 1 | Parts ontology v0.1: four modules proved consistent and non-trivial (Prover9/Mace4); competency-question document agreed with the partner | Proof scripts and models in the repository; signed-off competency questions |
| Unit 2 | Representation theorems for the public schemas and the partner schema; first audit report on [partner dataset 1] and on PartNet / PartNet-Mobility | Theorem files; violation-rate tables |
| Unit 3 | Audit pipeline v1 (both tiers; adapters for LeRobot, RLDS, ROS 2/MCAP, OpenUSD/USDZ, PLY, JSON [+ partner formats]); audits of all five public datasets; audit/data paper submitted; toolkit v1 installed at the partner | Release tag; submission receipt; partner acceptance |
| Unit 4 | Merged ontology-aligned public corpus released; private aligned release of the partner's data; ontology in COLORE and proposed to SC 42; pooled-data results | Release DOI; SC 42 document number; results tables |
| Unit 5 | Augmentation and constrained-training methods; methods paper submitted | Code release; submission receipt |
| Unit 6 | Verification-in-the-loop evaluation protocol; robotics paper; toolkit v2; evidence pack for the partner [route B: Passport integration] | Protocol document; submission receipt; partner acceptance |

## Pre-award timeline

| Date | Step |
|---|---|
| 2 Oct 2026 | Supervisor asked (email 1) |
| 15 Oct 2026 | Mitacs BD representative asked to confirm format and figures (email 2) |
| 31 Oct 2026 | Route chosen; partner approached (email 3 or 4) |
| 30 Nov 2026 | Partner commitment letter, CVs, COI declarations, [incubator letter] in hand; BD review done |
| ~11 Dec 2026 | Application submitted (16 weeks before 1 Apr 2027) |
| Dec 2026–Feb 2027 | Peer review; responses |
| 1 Apr 2027 | Unit 1 starts, subject to the U of T postdoctoral appointment |
