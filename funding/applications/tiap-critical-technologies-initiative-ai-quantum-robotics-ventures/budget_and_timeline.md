# Budget and timeline — TIAP Critical Technologies Initiative, 12 months

**Envelope (from the official page as surfaced by search; verify):** up to CAD 200,000 = non-dilutive grant up to CAD 100,000 + dilutive match up to CAD 100,000 from TIAP or a third party, applied to technology development and/or executive advisory support. A third-party summary states the program covers up to 50% of eligible costs [confirm the rate and the eligible-cost rules with TIAP]; if so, the full grant requires at least CAD 200,000 of eligible project cost, with the balance from the match, company cash or other non-overlapping sources.

All salaries, quotes and cash figures are [bracketed] placeholders: the profile, the deck and the registry give none, and this package does not invent them. Percentages in §2 are a *proposed* allocation of the grant cap, to be replaced by the real lines once salaries and quotes are known; the arithmetic then follows. Currency: CAD. No cost incurred before the agreement is signed is assumed eligible [confirm].

## 1. Project envelope

| Item | Value |
|---|---|
| Project length | 12 months from agreement start [target March 2027] |
| Total eligible project cost | [CAD — sum of §2 and §3; ≥ 200,000 if the 50% rule applies] |
| CTI grant requested | CAD 100,000 [cap — confirm] |
| Match | CAD 100,000 [TIAP dilutive match — or third-party investor; instrument: SAFE / priced equity — confirm] |
| Company share / other sources | [CAD — cash on hand; pilot revenue; IRAP or SR&ED on non-overlapping costs] |

## 2. Use of the grant — technology development (CAD 100,000)

| Line | Proposed share | Amount | What it buys | Milestone |
|---|---|---|---|---|
| Engineering salary — ENG1, ontology/robotics software engineer [Ontario hire] | [~45%] | [CAD] | Two-tier checker bulk stage (Datalog/SMT), regression suite, adapters (LeRobot, RLDS, ROS 2/MCAP, OpenUSD/USDZ, PLY, JSON), the 10,000-episode audit run and its report by dataset and axiom family | M3, M6 |
| Founder / CTO / robotics-lead time on the project [fractions consistent with any other funded appointment; disclosed] | [~20%] | [CAD] | Kernel v1 modules and verification (Projects 1.1–1.3); grounding with abstention (2.2); regulated-health scoping (2.4); Passport v1 (3.1) | M3, M8, M9 |
| U of T Semantic Technologies Laboratory — research agreement [confirm; quote incl. overhead] | [~15%] | [CAD] | Verification of kernel modules with COLORE; representation theorems relating the parts module to PartNet-family schemas; mereological-pluralism check | M3 |
| Cloud / inference compute | [~10%] | [CAD] | Grounding models, SMT runs at scale, the pre-registered experiments (3.2), augmentation validation (3.3) | M6, M12 |
| Assessment body / standards organization — Passport v1 evaluation [fee, if any] | [~5%] | [CAD] | Written evaluation of Passport v1 | M9 |
| Legal — rights, consent and permitted-use fields for the health track; customer data-plane terms [firm] | [~5%] | [CAD] | Privacy scope and consent records for the regulated-health partner run | M8 |
| **Total grant** | 100% | **CAD 100,000** | | |

Justification. The CTI text ties the grant to technology development and executive advisory. Every line above retires a named uncertainty in proposal §4: completeness of the compiled check (M3), grounding accuracy and violation rates at scale (M6), transfer to a hospital setting (M8), external acceptance of the evidence format (M9), and measured value against simpler baselines (M12). ENG1 is the only new hire and carries the full-time engineering that the CTO cannot carry beside grounding and experiments. The U of T line buys the one capability the company does not hold in-house — tool-supported verification with the COLORE repository — and keeps the founder's academic and company roles separate under a written agreement.

## 3. Use of the match — commercial execution and advisory (CAD 100,000)

| Line | Amount | What it buys |
|---|---|---|
| Design-partner delivery (two pilots incl. the health-setting run): adapters for partner formats, acceptance runs, evidence packages | [CAD] | Two acceptances against independent baselines (M12) |
| Executive advisory [TIAP-provided or scoped: regulated-B2B sales, quality-system and validation evidence, board practice] | [CAD] | Founder transition from consumer ventures to regulated B2B software |
| IP management: IPO licence, patent assignment/licence from Uing Technologies, IP-ownership map [counsel] | [CAD] | Clean IP position for the round |
| Working capital for pre-reimbursement exposure and delayed collections | [CAD] | Cash discipline per the operating plan |
| **Total match** | **CAD 100,000** | |

## 4. Stacking and non-duplication

The grant is government assistance (FedDev-backed): it counts toward the overall cap on assistance for any project it co-funds and reduces the SR&ED base for the same expenditures; it must not overlap NRC IRAP-claimed costs (the IRAP package proposes the Engine and adapters over a 12-month agreement targeted for April 2027 — keep a scope map or claim net). Mitacs- or Alliance-funded U of T work is university research, not company R&D, and the same scope must not be claimed under both. The founder's possible U of T postdoctoral appointment (April 2027 or later) is disclosed; time fractions here must be consistent with it. [Confirm each with TIAP, the ITA, the SR&ED preparer and counsel.]

## 5. Timeline and milestones (months from agreement start; target month 1 = March 2027)

| Month | Theme 1 Kernel | Theme 2 Engine | Theme 3 Passport / validation | Milestone and acceptance |
|---|---|---|---|---|
| 1 | 1.1 parts module axioms; 1.2 robotics module scoping | Episode contract frozen; adapter gap list | Partner data agreements signed [robot OEM / model developer; health partner] | Kick-off; ENG1 hired |
| 2 | 1.1 verification (Prover9/Mace4); U of T agreement starts | 2.1 LeRobot and RLDS adapters | — | — |
| 3 | 1.3 compilation to SMT subset; regression suite | Vertical slice on one task and connector | Evidence package v0 | **M3** — kernel v1 frozen; blind-baseline vertical slice reproduced by a partner |
| 4 | Representation theorems vs PartNet-family schemas (U of T) | 2.1 ROS 2/MCAP, OpenUSD adapters; 2.2 grounding v1 | — | Adapters for [four] formats |
| 5 | Pluralism check; module docs | 2.3 two-tier checking at scale; dispositions and repairs | Passport schema draft | — |
| 6 | Kernel v1.1 (fixes from audit) | 10,000 episodes verified; audit report by dataset and axiom family | — | **M6** — Engine v1; audit report; passed-sample audit |
| 7 | — | 2.4 health-partner input contract, rights and consent fields; 2.5 physics residuals: geometry and kinematics checks | 3.1 Passport v1 build; issuer signature | — |
| 8 | — | 2.4 health-partner run under the partner's acceptance test; 2.5 dynamics residual where signals exist | Passport v1 to [assessment body] | **M8** — health-track acceptance run; physics gate decision |
| 9 | COLORE contribution of verified modules | Robustness experiments (shift, missing fields, corruption, timeout) | Written evaluation received | **M9** — Passport v1 recognized |
| 10 | — | 3.2 detection and ablation experiments with partner baselines | 3.3 feedback classification; augmentation variants | — |
| 11 | — | 3.2 second-robot experiment (adaptation hours recorded) | 3.3 training-interface experiment in SAPIEN [+ second simulator] | — |
| 12 | Kernel v1.2 | Experiment report with confidence intervals | Gate decisions: uncertainty, augmentation, runtime | **M12** — two design-partner acceptances (one health); roadmap for months 13–18; final report |

Alignment with the company's dated targets (deck): three co-development partners and 10,000 verified episodes by Q1 2027; Passport v1 recognized by Q2 2027; five paying customers and two renewals by month 18. If the agreement starts in March 2027, the Q1 2027 targets are reached with company funds before the project and are treated as background; M6 then extends the verified corpus to partner data under the project. [Re-date the table once TIAP fixes the start date.]

## 6. Reporting

[Quarterly] progress reports against M3/M6/M8/M9/M12 and [quarterly] expenditure reports with payroll records and invoices; final report at month 12 with the experiment results and the gate decisions [confirm TIAP's reporting schedule and claim mechanics — advance vs reimbursement — in the agreement].
