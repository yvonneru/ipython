# Budget and timeline — AXIOMALITY at the Harvard i-lab (Venture Program spring 2027; PIC 2027)

Neither program asks for a budget form. The Venture Program gives no cash (advisor, office hours, workspace, partner credits). The PIC awards prizes — in 2026, five grand prizes of USD 75,000 and five prizes of USD 25,000 across the tracks, plus Ingenuity Awards of up to USD 2,500 [2027 amounts unconfirmed; record from the official page] — and judges ask what a venture would do with the money. This file therefore has three parts: (1) the cost of applying, (2) a use-of-prize plan for the two prize sizes, written to match proposal.md §10, and (3) the milestone timeline that the written application and the deck reference. Every dollar figure other than the published prize amounts and the deck's price points is a placeholder in [brackets]; the arithmetic is complete so the totals follow once the inputs are filled. Currency: USD.

## 1. Cost of applying

| Item | Amount | Note |
|---|---|---|
| Application fee | 0 | Neither program charges a fee [confirm on the form]. |
| Team time — written answers, deck, video | [person-days: founder —, CTO —] | Registry estimate: 8 preparation days in total. |
| Video production | [0 if recorded in-house; otherwise quote] | Format and length unknown until the 2027 form opens. |
| Travel | 0 | Founder is in Boston; the i-lab is at 125 Western Ave, Allston [confirm]. |
| Legal — confirmation that the entity may receive prize funds; HMS outside-activity disclosure | [counsel time, if billed] | See emails.md, email 7. |
| Opportunity cost — Toronto start moved from April to [May–June] 2027 if option (a) in README is chosen | [none if the postdoctoral awards allow a later start; the CPRA/Vector/DSI drafts all state "April 2027 or later"] | Decision by 30 Oct 2026. |

## 2. Use of prize (PIC)

Prizes are equity-free. Who receives the funds (the company or the Team Lead personally), how they are paid and how they are taxed are [unconfirmed — ask the i-lab in email 1 and counsel in email 7]. The plan below assumes the company receives the funds; if the prize is paid to the Team Lead, [counsel] advises on the transfer.

### 2a. Grand prize case — USD 75,000

Funds the Q2 2027 gate (Passport v1 recognized by one assessment body or standards organization) and one engineer-quarter on the ROS 2/MCAP and OpenUSD adapters.

| Line | Amount | Justification |
|---|---|---|
| Passport v1 recognition: assessment-body or standards-organization evaluation fee, if any | [fee — 0 if the evaluation is done under a standards-committee process without a fee] | The Q2 2027 gate in the 18-month plan; the recognition is the moat described in proposal.md §7. |
| Passport v1 recognition: founder and CTO time to prepare the evidence pack, respond to the evaluator, and revise the Passport format (Project 2.2) | [person-months × loaded monthly cost] | Proposal Project 2.2 open question: which Passport fields does an assessment body require? |
| Legal review of the Passport's rights, consent and permitted-use fields | [quote from the international law firm named in the deck, if continuing] | Audit-pack design already reviewed with a Big Four firm and an international law firm [names]; this line covers the v1 revision only. |
| One engineer-quarter (ENG1, contract or new hire) on the ROS 2/MCAP and OpenUSD/USDZ adapters (Project 2.1) | [3 months × loaded monthly cost] | The adapters gate the first external dataset (proposal §10) and the throughput measurement in Project 2.1; the CTO cannot carry them beside the compiled-SMT work. |
| Compute for the two-tier checking runs on the first external datasets and the public-corpus audit | [cloud quote — episodes × cost per 1,000 episodes] | Throughput per 1,000 episodes is a Project 2.1 deliverable and needs a known allocation. |
| Reserve (unallocated) | [remainder to USD 75,000; target 5–10%] | Evaluator requests that cannot be scoped in advance. |
| **Total** | **75,000** | |

### 2b. Track prize case — USD 25,000

Funds the recognition work alone.

| Line | Amount | Justification |
|---|---|---|
| Assessment-body or standards-organization evaluation fee, if any | [fee] | As above. |
| Founder and CTO time on the evidence pack and Passport v1 revision | [person-months × loaded monthly cost] | As above. |
| Legal review of the Passport rights and consent fields | [quote] | As above. |
| Reserve | [remainder to USD 25,000] | |
| **Total** | **25,000** | |

The adapter engineer-quarter and compute are then funded from [the financing round sized to the 18-month plan / pilot revenue — confirm].

### 2c. Ingenuity Award (up to USD 2,500) — not planned

The Ingenuity Awards are for early-stage student ideas. AXIOMALITY applies as a venture with a product in internal test; the award is not pursued unless the i-lab advises otherwise.

## 3. What the Venture Program provides (in kind)

| Resource | Planned use during the 12-week cohort |
|---|---|
| Staff advisor (regular meetings) | Weekly: converting co-development discussions into signed pilots at USD 25–50k; certification go-to-market, which is new to a founder whose earlier companies sold to consumers. |
| Expert office hours (legal, finance, sales, fundraising) | Prize-receipt and entity questions; pilot contract template; pricing test for the 2–3× passported-data premium [basis to confirm]; preparation of the financing round. |
| Workspace at the i-lab | Founder's working base for the cohort; team visits for the demo build. |
| Partner credits [cloud, software — record from the admission materials] | Compute for Engine runs on the first external datasets; offsets the compute line in §2a. |
| Community and HBS network | Three Boston-area robotics and medical-device buyer conversations to test the certification thesis (proposal §10) [names]. |

## 4. Milestone timeline

Dates in brackets are expected, not confirmed. Program dates are re-set once the 2027 pages are read (README, 2 Oct 2026).

| When | Company milestone | Program milestone | Evidence produced for the application or the judges |
|---|---|---|---|
| Oct 2026 | Engine internal test begins (minimum Engine; kernel v1 for home scenes; six adapters) | Official pages read; eligibility confirmed in writing; Student i-lab membership; PIC tips workshop attended | Internal-test plan; eligibility email trail |
| 23 Oct 2026 | Co-development LOIs or signed agreements requested from [humanoid OEM(s)] and [data platform(s)] | — | LOIs for the deck appendix (the semifinalist filter is traction) |
| 30 Oct 2026 | — | Venture Program application drafted; deck v1 | Form answers from proposal.md §1–§10 |
| 15 Nov 2026 | Engine internal-test results: episodes processed, violation rates, throughput per 1,000 episodes [once available] | PIC written application complete; deck v2; video script | Test results are the product-traction line in proposal §5 |
| 1 Dec 2026 | — | **PIC application submitted (internal deadline)**; official deadline expected early December [unconfirmed] | Confirmation email saved |
| Dec 2026 – Jan 2027 [expected] | Kernel v1 frozen; first partner dataset ingested | **Venture Program application submitted on opening day** | — |
| Mid-Jan 2027 [expected] | — | PIC semifinalists announced; if selected, application goes to external judges | — |
| Jan – Apr 2027 [expected] | Q1 2027 gate: three co-development partners signed; 10,000 verified episodes; first external dataset through Engine v1; Passport v0.9 issued | 12-week Venture Program cohort; Team Lead present at the i-lab; weekly advisor meetings; three buyer conversations | Signed pilots and Passport v0.9 are the finalist-stage evidence |
| Mar 2027 [expected] | — | PIC finalists announced; pitch coaching; live pitch to judges | Pitch deck v3; demo of scene graph and check output |
| Late Apr / May 2027 [expected] | — | PIC awards ceremony | — |
| Q2 2027 | Passport v1 recognized by one assessment body or standards organization (funded by the prize under §2, or otherwise by [round / revenue]) | — | — |
| [May–June 2027, or later — decision by 30 Oct 2026] | Founder's U of T postdoctoral appointment begins if the CPRA / Vector / DSI route succeeds; company roles and postdoctoral work kept separate under a written arrangement | — | — |
| Month 18 of the operating plan | Five paying customers; two renewals | — | — |

## 5. Consistency checks before submission

- Every number in this file matches the deck and proposal.md (prize amounts; pilot USD 25–50k; annual deployment USD 120–240k; Q1/Q2/month-18 gates).
- The prize-use plan sums to the prize amount exactly, and no line names a supplier, evaluator or hire that cannot be evidenced.
- The Toronto start date in row "[May–June 2027]" agrees with the date entered in the CPRA, Vector and DSI applications.
- If the 2027 prize amounts differ from 2026, §2a and §2b are re-cut to the new totals.
