# Budget and timeline — Amazon Research Awards, Fall 2026

## Budget

ARA awards have two components entered in the portal: a **cash gift** (one-time, unrestricted, paid to the University of Toronto; "may not be used for indirect expenses which are not allocable, reasonable, adequately documented, and consistent with established policies") and **AWS Promotional Credits**. The FAQ sizes a typical cash budget at one postdoctoral researcher or one to two graduate students for one year plus some conference travel and equipment.

**Caps are call-specific and the cash cap binds.** Fall 2025 (all calls): up to USD 100,000. Spring 2026 Robotics: up to USD 50,000 cash plus up to USD 50,000 AWS credits (third-party listing seen 2026-09-26 — verify on the call page). Fall 2025 Automated Reasoning: cash reportedly about USD 70–80k, with larger credit allowances (search snippet — verify). [Record the Fall 2026 cash cap and credit cap on 1 Oct.] **No dollar figure below is set; every amount comes from MIE finance and the call text.** A request that lists a full postdoc year, a MASc stipend, travel and storage will exceed a USD 50,000 cash cap; choose one of the two options below with MIE finance and request only what the justified lines reach.

| Line | Option A — no salary award held at acceptance | Option B — CPRA / Vector / DSI salary held | Justification | Amount |
|---|---|---|---|---|
| Postdoctoral researcher (Dr. Ru), salary and benefits | [N] months, as many as fit under the cash cap after travel | — (salary from the fellowship) | Leads Themes 1–3 full-time for 12 months | [USD — months × MIE postdoc rate incl. benefits, at MIE finance's exchange rate] |
| MASc student, stipend | — (PI's laboratory funds the student [confirm]) | 12 months | Articulated-parthood module (Theme 1) and adapters (Theme 2) | [USD — MIE MASc stipend rate] |
| Conference travel | 1–2 trips | 2–3 trips | Audit/data paper and methods paper (one AI/robotics venue, one applied-ontology venue such as FOIS); one ISO/IEC JTC 1 [committee — verify] meeting | [USD at U of T rates] |
| Storage | as needed | as needed | Local copies of the five datasets and prover logs; no other equipment | [USD] |
| **Cash total** | ≤ cash cap | ≤ cash cap | No non-allocable indirect costs [confirm U of T's overhead position on corporate gifts] | [USD] |
| **AWS Promotional Credits** | same | same | See sizing below | [USD credits, ≤ credit cap] |

**AWS-credit sizing (state the assumptions in the justification; a reviewer discounts an unexplained round number).** Bulk tier: (part instances and pairwise relations × mean SMT check time) ÷ vCPU-hours per instance → [instance type, hours]. Prover tier: (residual jobs × time budget) → [hours]. Storage: five datasets plus logs in S3 → [TB-months]. Theme 3: (backbones × held-out categories × ablations × seeds × GPU-hours per run) → [instance type, hours], sized with the Robotics Institute advisor. Pilot the SMT check time on one PartNet category before 21 Oct so the bulk-tier number is measured, not guessed.

Justification text for the portal (≤120 words, adjust to the chosen option and numbers): *The cash gift supports [the named postdoctoral researcher for [N] months / one MASc student for twelve months], travel to present the audit/data and methods papers and to contribute the ontology to the relevant ISO/IEC JTC 1 committee, and local storage for staged datasets. AWS credits fund the compute-heavy audit — an embarrassingly parallel SMT/Datalog tier over [N] part instances and their pairwise relations on EC2 ([instance type], [hours]; measured check time [x] ms) with datasets in S3 ([TB]), a theorem-proving tier with explicit time budgets ([hours]) — and the GPU training and simulation runs for the generalization pilot ([instance type], [hours]). Code, axioms, corrected-annotation patches and an AWS runbook will be released.*

**Concurrency rule.** If CPRA, Vector or DSI is awarded before the ARA decision (~Feb–Mar 2027), switch to Option B before acceptance, not after; ARA gifts are one-time and the portal budget is what Amazon funds. [Confirm with U of T whether a gift budget can be re-lined after submission, or whether a fixed budget is required.]

## Pre-award timeline (2026)

The ARA ask must not compete with CPRA (hard stop Sat 17 Oct, planned submission 13–14 Oct) or with Prof. Grüninger's RAC 2027 submission (3 Nov). STRATEGY.md lists this call as **skip by default** (target Spring 2027); the dates below apply only if the go/no-go gate in README.md passes.

| When | Milestone |
|---|---|
| Thu 1 – Fri 2 Oct 2026 | Fall 2026 call checked; topics, caps, template, deadline recorded. Gate 1: a Robotics topic (or an Automated Reasoning topic naming specification inconsistency or solver quantifier reasoning) exists. |
| Fri 2 Oct 2026 | ARA ask added as the last item of the single 2 Oct message to Prof. Grüninger (CPRA first, per STRATEGY Addendum 5); emails 2 and 5 sent |
| Fri 9 Oct 2026 | Gate 2: Prof. Grüninger's yes/no in principle (same day as his RAC decision). No answer = Spring 2027 |
| Mon 19 Oct 2026 | After the CPRA hard stop: U of T handling confirmed; MIE salary/stipend rates received; budget option chosen |
| Wed 21 Oct 2026 | PI CV and sentence approvals; advisor named; GPU sizing and SMT check-time pilot done |
| Mon 26 Oct 2026 | Full package to U of T Research Services |
| ~Thu 29 Oct 2026 | Institutional sign-off if required (registry: ~2 weeks before the close). No ARA asks of the PI 30 Oct – 3 Nov (RAC) |
| ~Thu 5 – Mon 9 Nov 2026 | PI submits in the ARA portal |
| ~Thu 12 Nov 2026, 11:59 PM PT [confirm] | Expected close |
| ~Feb–Mar 2027 | Decision (≈3 months after close) |
| [June 2027 or later — never April, STRATEGY Addendum 6] | Dr. Ru starts at MIE; project month 1 |

## Project timeline (12 months, from Dr. Ru's start)

| Months | Theme | Milestone | Output |
|---|---|---|---|
| 1–4 | 1 Parts | Rigid, articulated, functional and assembly parthood modules in Common Logic; consistency and non-triviality (Prover9/Mace4); module relationships proved or refuted; constitution mappings applied to kinematic/functional/visual decompositions; PSL integration; schema mappings for five datasets drafted | Ontology v0.9 in COLORE; technical report 1 |
| 3–9 | 2 Audit | Adapters (PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World; LeRobot/RLDS); SMT/Datalog tier on EC2; prover tier with time budgets; violation rates by dataset, axiom family and category; adjudicated precision sample | Audit toolkit v1 (open licence); violation reports and corrected-annotation patches; audit/data paper submitted |
| 6 | — | **Decision point:** if the SMT fragment misses violations the prover finds, expand the prover tier and accept a smaller bulk set; ontology errors found by adjudication revise the axioms before release | — |
| 8–12 | 2–3 Audit / Learning | Cross-dataset mappings proved meaning-preserving; ontology-aligned index; H2 (no retraining) first, then H1 and H3 on one backbone with ablations by axiom family; metrics fixed before M8 | Mappings and index released; methods paper submitted; technical report 2 (AWS runbook); ontology v1.0 to COLORE and ISO/IEC JTC 1 [committee — verify] |
| 10 | — | **Decision point:** if H1 fails on the first backbone, report it and switch to the advisor's alternative; if Theme 2 is late, Theme 3 is reduced to H2 | — |
| 12 | — | Final report to Amazon; talks at the U of T Robotics Institute and [Amazon research contact's group, if offered] | — |

## Resources not requested from Amazon

| Resource | Source | Status |
|---|---|---|
| Verification pipeline (COLORE, Common Logic tooling, Prover9/Mace4) | Semantic Technologies Laboratory, MIE | Available [confirm access from the start date] |
| Dataset licences permitting release of corrected annotations (as patches) and an ontology-aligned index | Public licences of the five datasets | [Confirm each licence before submission; see compute-and-data-access-bundle/dataset_licences.md. The proposal promises patches and mappings, not a redistributed merged corpus, and names the fallback (violation reports plus patch generator).] |
| MASc student (Option A) | PI's laboratory | [PI to confirm] |
| Policy backbone and second simulator | Robotics Institute advisor | [Advisor to confirm] |
| Postdoc salary if a fellowship is awarded | CPRA / Vector / DSI | [Pending; switch to Option B if awarded] |
