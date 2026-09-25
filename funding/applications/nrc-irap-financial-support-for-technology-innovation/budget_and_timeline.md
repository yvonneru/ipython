# Budget and timeline — NRC IRAP project, 12 months

All dollar figures are placeholders in [brackets]: the profile, the deck and the registry give no salaries, no cash position and no contractor quotes, and this package does not invent them. The structure, the cost-share rates and the arithmetic are complete, so the applicant fills in the bracketed inputs and the totals follow. **Cost-share rates below are the registry's (up to 80% of R&D salaries, up to 50% of contractor costs); the ITA confirms the rates, the eligible-cost rules and the claim cycle, and they govern.** No cost incurred before the contribution agreement is signed is eligible. Currency: CAD.

## 1. Project envelope

| Item | Value |
|---|---|
| Project length | 12 months from agreement start [target 1 April 2027; earlier on signature if FY 2026-27 funds are available] |
| Target total project cost | [CAD — sum of Tables 2–4] |
| Requested IRAP contribution | [CAD — 0.8 × eligible salaries + 0.5 × eligible contractor costs, capped at the amount the ITA indicates; registry range for early projects CAD 50k–500k] |
| Company share | [CAD — total project cost minus IRAP contribution; includes all non-eligible costs] |
| Source of company share | [cash on hand / committed financing / pilot revenue — reference the financial statements] |

## 2. Eligible R&D salaries (IRAP up to 80%)

Only employees on the Canadian payroll performing the R&D in Canada. FTE fraction is the share of the person's time on this project.

| Role | Person | Annual salary | FTE on project | Months | Project cost | IRAP share (80%) | Company share (20%) |
|---|---|---|---|---|---|---|---|
| Founder/CEO — kernel (Theme 1), Passport (3.1), audit (2.3), feedback (3.3) | Yi Ru [Canadian payroll from — date; if also a U of T postdoc, the FTE here must be consistent with the university appointment and disclosed] | [salary] | [0.4–0.6] | [12] | [=] | [=] | [=] |
| CTO — compilation (1.3), adapters (2.1), grounding (2.2), experiments (3.2), training interface (3.3) | [name] | [salary] | [0.6–0.8] | 12 | [=] | [=] | [=] |
| Robotics lead — robotics module (1.2), physics residuals (2.4), second-robot and detection experiments (3.2) | [name] | [salary] | [0.5–0.8] | 12 | [=] | [=] | [=] |
| Senior 3D asset lead — asset audit, OpenUSD/PLY adapters (2.1), augmentation variants (3.3) | [name] | [salary] | [0.3–0.5] | 12 | [=] | [=] | [=] |
| ENG1 — ontology/robotics software engineer (new Canadian hire; two-tier checker, regression suite, audit runs) | [to hire; job description attached; IRAP YEP if eligible] | [salary] | 1.0 | [10–12] | [=] | [=] | [=] |
| **Subtotal salaries** | | | | | **[S]** | **[0.8 S]** | **[0.2 S]** |

Justification. The Engine's four workstreams map one-to-one onto the four existing roles; ENG1 is the only addition and is needed because the 10,000-episode audit (M6) and the regression suite (M3) are full-time engineering that the CTO cannot carry beside the grounding and experiment work. The founder's fraction is set by the kernel and Passport work, which no one else on the team can do.

## 3. Eligible contractor costs (IRAP up to 50%)

| Contractor | Work | Quote | IRAP share (50%) | Company share (50%) |
|---|---|---|---|---|
| University of Toronto, Semantic Technologies Laboratory (Prof. M. Grüninger) — research agreement | Verification of kernel modules (Project 1.1: representation theorems relating the parts module to PartNet-family schemas; mereological-pluralism check); COLORE contribution | [quote; typically a graduate research assistant for — months plus faculty time; U of T overhead rate to confirm] | [=] | [=] |
| [Cloud / inference provider] | Compute for grounding models, SMT runs at scale, augmentation and the Theme 3 experiments in SAPIEN [+ second simulator] | [quote] | [=] | [=] |
| [Law firm — the international firm named in the deck, if continuing] | Rights, consent and permitted-use fields of the Passport; customer data-plane terms | [quote] | [=] | [=] |
| [Assessment body / standards organization] | Written evaluation of Passport v1 (M9) | [fee, if any] | [=] | [=] |
| **Subtotal contractors** | | **[C]** | **[0.5 C]** | **[0.5 C]** |

Justification. The U of T contract buys the one capability the company does not hold in-house — tool-supported ontology verification with the COLORE repository — and keeps the founder's academic and company roles separate under a written agreement. Compute is scoped to the experiments in Project 3.2, which hold model, compute and data budget fixed across conditions and therefore need a known allocation. [If the Big Four audit-pack review continues, list it here or as a non-eligible cost, as the ITA advises.]

## 4. Non-eligible costs (company-funded, listed for the ITA's view of total project cost)

| Item | Amount |
|---|---|
| Equipment (workstations, sensors, [robot access for second-robot experiment — or partner-supplied]) | [CAD] |
| Overhead, rent, travel to design partners and standards meetings | [CAD] |
| Sales and pilot delivery not part of R&D | [CAD] |
| **Subtotal non-eligible** | **[N]** |

## 5. Totals

| | Amount |
|---|---|
| Total project cost | [S + C + N] |
| IRAP contribution requested | [0.8 S + 0.5 C] |
| Company share | [0.2 S + 0.5 C + N] |
| Company share as % of total | [=] |

Cash-flow note. IRAP reimburses eligible costs after they are incurred, on [quarterly] claims. The company must carry [one quarter] of salaries and contractor costs before each reimbursement; the monthly cash model should show the peak pre-reimbursement exposure and the reserve that covers it.

## 6. Timeline and milestones (months from agreement start)

| Month | Theme 1 Kernel | Theme 2 Engine | Theme 3 Passport / validation | Milestone and acceptance |
|---|---|---|---|---|
| 1 | 1.1 parts module axioms; 1.2 robotics module scoping | Episode contract frozen; adapter gap list | Partner data agreements signed [two partners] | Kick-off; ENG1 hired |
| 2 | 1.1 verification (Prover9/Mace4); U of T contract starts | 2.1 LeRobot and RLDS adapters | — | — |
| 3 | 1.3 compilation to SMT subset; regression suite | Vertical slice on one task and connector | Evidence package v0 | **M3** — kernel v1 frozen; blind-baseline vertical slice reproduced by a partner |
| 4 | Representation theorems vs PartNet-family schemas (U of T) | 2.1 ROS 2/MCAP, OpenUSD adapters; 2.2 grounding v1 | — | Adapters for [four] formats |
| 5 | Pluralism check; module docs | 2.3 two-tier checking at scale; dispositions and repairs | Passport schema draft | — |
| 6 | Kernel v1.1 (fixes from audit) | 10,000 episodes verified; audit report by dataset and axiom family | — | **M6** — Engine v1; audit report; passed-sample audit |
| 7 | — | 2.4 physics residuals: observation contract, geometry and kinematics checks | 3.1 Passport v1 build; issuer signature | — |
| 8 | — | 2.4 dynamics residual where signals exist; calibration on held-out data | Passport v1 to [assessment body] | Physics gate decision |
| 9 | COLORE contribution of verified modules | Robustness experiments (shift, missing fields, corruption, timeout) | Written evaluation received | **M9** — Passport v1 recognized |
| 10 | — | 3.2 detection and ablation experiments with partner baselines | 3.3 feedback classification; augmentation variants | — |
| 11 | — | 3.2 second-robot experiment (adaptation hours recorded) | 3.3 training-interface experiment in SAPIEN [+ second simulator] | — |
| 12 | Kernel v1.2 | Experiment report with confidence intervals | Gate decisions: uncertainty, augmentation, runtime | **M12** — [two] design-partner acceptances; roadmap for months 13–18; final claim and report |

Alignment with the company's dated targets (deck): three co-development partners and 10,000 verified episodes by Q1 2027; Passport v1 recognized by Q2 2027; five paying customers and two renewals by month 18. If the agreement starts on 1 April 2027 the Q1 2027 targets are reached with company funds before the project and are treated as background; M6 then extends the verified corpus to partner data under the project. [Re-date the milestone table once the ITA fixes the start date.]

## 7. Reporting

[Quarterly] claims with timesheets, payroll records and contractor invoices; [quarterly] progress reports against M3/M6/M9/M12; final report at month 12 with the experiment results and the gate decisions [confirm the schedule in the contribution agreement].
