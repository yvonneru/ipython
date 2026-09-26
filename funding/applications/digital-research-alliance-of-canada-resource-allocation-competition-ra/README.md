# Digital Research Alliance of Canada — Resource Allocation Competition (RAC) 2027, Resources for Research Groups (RRG) stream

**PI (applicant of record):** Prof. Michael Grüninger, Department of Mechanical and Industrial Engineering, University of Toronto — Semantic Technologies Laboratory · **Sponsored user / lead researcher:** Dr. Yi Ru (incoming postdoctoral fellow, [June 2027 or later]: never April, STRATEGY Addendum 6; sponsored external collaborator until then) · **Registry:** e1dfb65e5146, tier B, fit 74, verdict confirmed · **Package drafted:** 2026-09-25

This is an in-kind compute, storage and GPU request, not a grant. Nothing in it pays salary. It exists because the RAC allocation year (1 Apr 2027 – 31 Mar 2028) is exactly the period in which the O3 policy experiments and the O2 re-audit would run in Toronto, and RAC is the only route to *sustained* GPU time on Alliance systems. Dr. Ru cannot apply: postdocs cannot be PI, so the entire opportunity depends on Prof. Grüninger agreeing to submit and holding a current CCDB account. Everything below is written so that his effort is limited to reviewing, editing the "past usage" and HQP lines, updating his CCV, and pressing submit.

**Eligibility gate (review, 2026-09-26).** Search results attribute two rules to the Alliance. First, a RAC application needs a minimum request of **200 core-years CPU or 25 RGU-years GPU**. Second, a PI can obtain up to **40 TB project / 100 TB nearline** storage through the Rapid Access Service (RAS) without any RAC. Both come from the Alliance RAS page via search; the page was not opened [verify in the RAC 2027 Guide]. The honest request, which matches the compute bundle, is ≈ 9.7 RGU-years GPU, ≈ 1.4 core-years CPU and 20 TB project storage. As drafted, then, the RRG is **not eligible**, and its storage part belongs in RAS. The package therefore runs on two tracks. **(1) Now, whatever happens:** the sponsored CCDB role, plus a RAS storage request for 20 TB of project storage filed by the PI. **(2) Gate on 20 Oct:** submit the RRG only if the RAC 2027 Guide shows a threshold this request meets, or a measured per-run cost puts the same matrix at ≥ 25 RGU-years (break-even ≈ [61] H100-hours per run against the assumed [24]). The matrix is never enlarged to clear the bar. Otherwise, skip RAC 2027 and apply in RAC 2028 with a year of usage. Details: budget_and_timeline.md §0 and §7.

Files: `README.md` (this brief) · `proposal.md` (the RRG application text in the Alliance's sections, PI's voice) · `statement.md` (Dr. Ru's compute-justification memo to the PI, first person, and the sponsored-user role text for CCDB) · `referee_brief.md` (no referee letters exist in RAC — the file explains what the science and technical reviewers see and how the PI's inputs are scored) · `budget_and_timeline.md` (resource request in RGU / core-years / TB with derivations, and the allocation-year milestone timeline) · `emails.md` (to Prof. Grüninger ×3, to the HMS supervisor, to MIE research services / the U of T Alliance contact, to the AXIOMALITY CTO).

## Program

| Item | Detail | Status |
|---|---|---|
| Funder | Digital Research Alliance of Canada (national systems: SciNet/Compute Ontario Trillium; Vector-hosted Killarney; Fir, Rorqual, Nibi) | confirmed (registry) |
| Stream | Resources for Research Groups (RRG): "intended for individual faculty members from all disciplines, and their sponsored users"; for "projects whose primary purpose is to conduct research requiring compute, storage and cloud resources" | confirmed (web search 2026-09-25, alliancecan.ca) |
| What is awarded | GPU allocations in reference GPU units (RGU), CPU core-years, project/nearline storage, cloud; no cash | confirmed (registry) |
| Minimum request to apply | "A minimum of compute resources (currently set at 200 core-years for CPU and 25 RGU-years for GPUs) is required to be eligible to submit a RAC application"; RAS allows "a maximum of 40 TB of project storage and 100 TB of nearline storage in any General Purpose cluster without submitting a RAC application" | search 2026-09-26, attributed to https://www.alliancecan.ca/en/our-services/advanced-research-computing/accessing-resources/rapid-access-service (not opened) [verify for RAC 2027 and for AI compute] |
| Award basis | "appropriateness of the computational resources requested to achieve the project's objectives and the likelihood that these resources will be efficiently used, rather than on the evaluation of a complete research program"; in 2024, science score > 2.0/5 received an allocation; requests scaled by score, size and supply | search 2026-09-26, https://www.alliancecan.ca/en/2024-resource-allocations-competition-results |
| Allocation period | 1 April 2027 – 31 March 2028; renewable; Fast Track renewal for up to two further years if the prior science score exceeded 2.0/5 | confirmed (registry; Fast Track rule from alliancecan.ca Fast Track guidelines) |
| Official page | https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/resource-allocation-competition — the slug has also appeared as `…/resource-allocation-competitions`; both were returned by search, open whichever resolves | flag |
| Portal | Registry says alliance.smapply.ca; the 2025 alert says "online application form provided on the CCDB portal". The PI's CCDB login is needed either way | [verify which portal RAC 2027 uses] |

## Deadlines

| Date | What | Who |
|---|---|---|
| 23 Sep 2026 | RAC 2027 opened | — (confirmed: two independent university alerts and the Alliance page, searched 2026-09-25) |
| **by 2 Oct 2026** | Ask Prof. Grüninger for his CCDB status, CCRI and current RAS/RAC usage, a sponsored CCDB role for Dr. Ru now, a RAS storage request, and a conditional RRG | Dr. Ru (emails.md §1) |
| **by 9 Oct 2026** | Prof. Grüninger's yes/no on the sponsored role and the RAS storage request | Prof. Grüninger |
| by 10 Oct 2026 | Dr. Ru registered in CCDB as a sponsored user (external collaborator now; postdoc from June 2027 or later) | Dr. Ru; PI approves in CCDB |
| 10–19 Oct 2026 | [1–2] SAPIEN calibration runs on RAS opportunistic GPU (or an HMS O2 GPU partition, if the supervisor permits); RAC 2027 Guide read via research services (emails.md §5) | Dr. Ru |
| **20 Oct 2026** | **Gate decision** (budget_and_timeline.md §0), then emails.md §2 Variant A (skip) or B (full draft to the PI) | Dr. Ru + Prof. Grüninger |
| by 27 Oct 2026 | If go: PI's edits back; CCV in CCDB current; past-usage section written by the PI; HQP list complete | Prof. Grüninger |
| **by 30 Oct 2026** | If go: submit on the portal (three days of slack) | Prof. Grüninger |
| [Nov 2026] | RAS storage request (20 TB project) filed by the PI; independent of the gate [route — emails.md §5] | Prof. Grüninger |
| **3 Nov 2026** | Hard deadline (RAC 2027 closes) | — (confirmed) |
| [Fast Track deadline — not applicable] | Fast Track applies only to renewals of a previously scored RRG; the group has no prior allocation [confirm with the PI], so the full application route applies | — |
| Dec 2026 – Mar 2027 [verify] | Science and technical review; results announced before 1 Apr 2027 | Alliance |
| 1 Apr 2027 | Allocation active | — |

Referee deadlines: none — RAC has no reference letters. Internal institutional deadline: none known — RAC applications go from the PI directly to the Alliance without a research-office signature [confirm with MIE research services that U of T imposes no internal review; emails.md §5].

## Eligibility conditions

| Condition | Applies to | Status |
|---|---|---|
| PI is a faculty member eligible to hold research funding at a Canadian post-secondary institution | Prof. Grüninger | met (registry) |
| PI holds an active Alliance (CCDB) account with a current CCV | Prof. Grüninger | [unconfirmed — ask; emails.md §1] |
| Postdocs cannot be PI; Dr. Ru is a sponsored user | Dr. Ru | understood; Dr. Ru's citizenship and current Harvard status are irrelevant to eligibility (registry) |
| Sponsored-user role for Dr. Ru approved by the PI in CCDB before any allocation can be used | Dr. Ru + PI | [unconfirmed — whether an external collaborator at a US institution can be sponsored before the appointment starts] |
| Dr. Ru's U of T postdoctoral appointment begins [June 2027 or later]. The allocation is group-held, so the timing is not a bar, but the PI must justify GPU for a postdoc not yet in the group, and Q1 of the allocation year (Apr–Jun 2027) runs remotely under the external-collaborator role | PI | [appointment not yet confirmed — depends on CPRA (17 Oct 2026) or another salary source; remote use by a US-based sponsored user — verify] |
| Request meets the RAC minimum (≥ 200 core-years CPU or ≥ 25 RGU-years GPU) | PI | **not met as drafted** (≈ 9.7 RGU-years; ≈ 1.4 core-years); gate on 20 Oct |
| Whether AI compute (Killarney / PAICE) is requested inside the RRG form or via a separate AI-compute call | PI | [unresolved by search; read the RAC 2027 Application Guide] |
| Group has no known GPU-heavy RAC history; first-year GPU asks without history are routinely scaled back | PI | flag — and the honest ask is below the RAC minimum (next row), so "modest" is not an option: either the measured need clears 25 RGU-years or the group waits for RAC 2028 |

## Format and criteria (verify on the official page)

What the three permitted searches established (2026-09-25):

- **Window:** "The Resource Allocation Competition (RAC) 2027 will open on September 23, 2026 and remain open until November 3, 2026." — https://www.uoguelph.ca/research/alerts/content/digital-research-alliance-canada-2025-resource-allocation-competition (2025 alert page carrying the 2027 dates); also https://library.viu.ca/blogs/datamanagement/RDMSCnews/digital-research-alliance-of-canada-2026-resource-allocation-competition-de (registry evidence).
- **RRG definition and submission route:** "Resources for Research Groups (RRG) is intended for individual faculty members from all disciplines, and their sponsored users"; "Applications must be submitted electronically using the online application form … An application template is available in the Resource Allocation Competition Application Guide." — https://www.alliancecan.ca/en/our-services/advanced-research-computing/accessing-advanced-research-computing-resources and https://www.alliancecan.ca/en/our-services/advanced-research-computing/accessing-resources
- **Fast Track rule (implies the science score scale):** "the previous RRG application must have received a science score greater than 2.0 points (out of 5) … no more than two consecutive years" — https://alliancecan.ca/resource-allocation-competitions/applying-to-the-rrg-competition-via-the-fast-track-application-process
- **RGU conversion (secondary source):** "an NVIDIA A100-40G counts as 4.0 RGUs, while an H100-80G counts as 12.15 RGUs" — https://docs.mila.quebec/technical_reference/clusters/drac/ [verify against the Alliance's own RGU table for RAC 2027].
- **Streams:** RRG (research groups) vs RPP (Research Platforms and Portals, persistent cloud services) — https://alliancecan.ca/en/services/advanced-research-computing/accessing-resources/resource-allocation-competitions/research-platforms-and-portals-rpp-competition. RRG is the correct stream here.

What the searches did **not** establish and must be read from the RAC 2027 Application Guide (PDF linked from the official page) before 20 Oct:

- [Section headings of the RRG form and the page/character limit of the research-description section — proposal.md uses the section names that recur across RAC cycles (Project title and summary; Research description; Resource justification: compute, GPU, storage, cloud; HQP; Past usage / progress; Publications) and is sized to fit a short limit; re-fit when the Guide is read.]
- [Review criteria and weights. RAC uses a science review by a discipline committee (score out of 5, confirmed above) and a technical review of feasibility and resource justification; whether HQP/productivity is scored separately or folded into the science score, and any weights, must be read from the Guide.]
- [Whether Killarney / PAICE AI compute is requested inside the RRG form for RAC 2027 or via a separate call.]
- [Storage categories, scratch quota and purge policy on the target cluster; the RAS storage-request route; whether the 200 core-year / 25 RGU-year minimum (found by search on 2026-09-26, above) applies unchanged to RAC 2027 and to AI compute.]
- [Whether the PI's CCV must be the Alliance/CCDB CCV variant.]

## What is submitted where and in what format

Submitted by the PI on the Alliance portal [alliance.smapply.ca or CCDB — verify]: the online RRG form with (1) project title and summary; (2) research description [length limit — verify]; (3) resource request and justification per resource type (GPU in RGU-years, CPU core-years, storage in TB by category, cloud if any), each with a technical justification and evidence of scaling; (4) HQP / team list with CCDB usernames; (5) past usage and progress report [not applicable for a first request — state RAS usage instead]; (6) publications enabled by prior allocations [none — state the group's relevant publications]; (7) the PI's CCV attached or linked from CCDB [verify variant]. Text is pasted into form fields; keep proposal.md sections self-contained so each can be pasted as a unit.

## Who must do what by when

| Who | What | By |
|---|---|---|
| Dr. Ru | Send emails.md §1 (fold into the consolidated 2 Oct Grüninger ask) | 2 Oct 2026 |
| Prof. Grüninger | Confirm CCDB account, CCRI, current RAS/RAC usage; approve Dr. Ru's sponsored role; agree to the RAS storage request | 9 Oct 2026 |
| Dr. Ru | Register in CCDB under the PI's CCRI; read the RAC 2027 Application Guide (thresholds, headings, limits, AI-compute route); run [1–2] calibration runs to measure the per-run GPU cost, stating the GPU model | 20 Oct 2026 |
| Dr. Ru + Prof. Grüninger | Gate decision; emails.md §2 Variant A or B | 20 Oct 2026 |
| Prof. Grüninger | If go: write "past usage" and the HQP list; update CCV; edit | 27 Oct 2026 |
| Prof. Grüninger | If go: submit | 30 Oct 2026 (hard: 3 Nov) |
| Prof. Grüninger | RAS storage request (20 TB project) | [Nov 2026; before 1 Mar 2027 at the latest] |
| MIE research services / U of T Alliance contact | Confirm no internal step is required; confirm U of T storage contribution rules if any | before 20 Oct (emails.md §5) |
| HMS supervisor | Nothing for RAC itself; informed that Alliance storage takes over the audit data by 1 Mar 2027 (emails.md §4) | Oct 2026 |
| AXIOMALITY CTO / company officer | Nothing to submit; acknowledge that no company workload will ever run on the allocation (emails.md §6) | Oct 2026 |

## Submission checklist

- [ ] Prof. Grüninger's written yes to the sponsored role and the RAS storage request (9 Oct)
- [ ] **Gate passed on 20 Oct** (RAC minimum met by the Guide's rule or by a measured per-run cost, with the matrix unchanged). If not: stop here; RAS storage request only
- [ ] PI's CCDB account active; CCRI known; CCV current [variant verified]
- [ ] Dr. Ru's CCDB sponsored role approved (username to enter in the HQP list)
- [ ] RAC 2027 Application Guide read; proposal.md re-fitted to its headings and limits; Killarney/PAICE route settled
- [ ] Every bracketed number in budget_and_timeline.md replaced by a measured value or an explicit stated assumption (reviewers accept stated assumptions; they do not accept blanks)
- [ ] RGU conversion for the target system taken from the Alliance's RAC 2027 table, not the Mila secondary source
- [ ] Storage: project storage via RAS (not in the RRG unless the total exceeds 40 TB); raw corpora on scratch; no nearline for active data
- [ ] Past usage section written by the PI (RAS usage from Oct 2026 if the sponsored role is active; otherwise "no prior allocation")
- [ ] HQP list: Dr. Ru + [lab graduate students on COLORE/PSL — PI to list]; MASc1/MASc2/PhD1 tags replaced or deleted
- [ ] Hardware: SAPIEN renderer (Vulkan) confirmed on the target GPU nodes; Isaac Lab placed on an RTX partition [Killarney L40S, if confirmed] or moved to the NVIDIA Academic Grant workstation (H100 has no RT cores)
- [ ] Data-management paragraph included (dataset terms; no frames re-hosted; no company use)
- [ ] Submitted by 30 Oct; confirmation email saved

## How this proposal meets the criteria

| Criterion (reconstructed 2026-09-26; weights [verify]) | How the package addresses it | Where |
|---|---|---|
| E. Eligibility screen: faculty PI with a CCDB account; minimum request ≥ 200 core-years or ≥ 25 RGU-years; format per the Guide | PI is faculty; the minimum is **not met as drafted** and is handled by the 20 Oct gate and the RAS track; headings and limits still unread | README gate; budget_and_timeline.md §0 |
| S1. Scientific excellence and significance (science score /5; > 2.0 funded in 2024) | A precise, unanswered question with three hypotheses; methodology the lab is known for (COLORE, PSL, TUpper/ISO 21838-4); allocation-year deliverables A1–A3 stated as measurable outputs; linked to the PI's NSERC program [status] | proposal.md §1–§4 |
| S2. Appropriateness of the resources to the objectives | Every quantity derived from the 138-run matrix and the 15-pass audit; arithmetic corrected; reconciled with the compute bundle; storage within RAS; cut order stated | budget_and_timeline.md §1–§4, §7; proposal.md §8 |
| S3. Likelihood of efficient use (technical feasibility) | Embarrassingly parallel array jobs; Tier-2 bounded by timeout; hardware matched to software (RTX for Isaac Lab); calibration before the gate; RAS usage from Oct 2026 | proposal.md §4, §7; budget_and_timeline.md §2 |
| S4. Team, HQP, productivity [whether scored separately — verify] | Dr. Ru named; concrete training on the allocation; trainee names still [PI to list]; three papers planned; open releases | proposal.md §5–§6 |
| S5. Fit with the RRG stream and data stewardship | Honest split between RAS (storage, CPU) and RRG (GPU above the minimum only); dataset licences respected; no company use | proposal.md §8–§9 |

## Items still needing the applicant or the PI

[RAC 2027 minimum request confirmed in the Guide, incl. for AI compute] · [measured GPU-hours per run and the GPU model it was measured on] · [RAS storage-request route; scratch quota and purge policy] · [RTX (L40S) partition on Killarney and its RGU factor] · [Commonsense Cobotics award status, number and term] · [PI's CCDB account status and CCRI] · [PI's yes/no by 9 Oct] · [which portal — alliance.smapply.ca or CCDB] · [RAC 2027 Application Guide: headings, page/character limits, criteria and weights] · [Killarney/PAICE inside RRG or separate call] · [Alliance RGU table for the target system] · [Alliance storage categories, quotas and RRG thresholds] · [CCV variant required] · [Dr. Ru's U of T appointment start date (June 2027 or later) and salary source] · [whether an external collaborator at a US institution can be sponsored in CCDB before the appointment] · [past usage of the group] · [HQP names and CCDB usernames] · [second simulator confirmed as Isaac Lab] · [SMT solver (Z3?) and Datalog engine (Soufflé?)] · [every numeric assumption in budget_and_timeline.md: instances per corpus, seconds per instance, ontology versions, axiom-family conditions, splits, seeds, GPU-hours per run, storage per corpus] · [pilot results from Harvard, once available, to cite] · [the 15 Jan 2027 public audit result, if the draft is updated after that date] · [PI's relevant publications list for the form] · [U of T internal review requirement, if any] · [HMS supervisor name] · [AXIOMALITY CTO name].

## Review log

**2026-09-26 — skeptical panel review (reviewer agent).** Inputs: this package, registry record e1dfb65e5146, funding/profile/*.md, funding/STRATEGY.md (Addendum overrides), compute-bundle README estimate and applications.md §F, Prof. Grüninger's NSERC proposals in funding/templates/. Three web searches (WebFetch blocked) yielded: the RAC minimum request (200 core-years / 25 RGU-years), the RAS storage ceilings (40 TB project / 100 TB nearline), and the award basis and 2024 score threshold. The RAC 2027 Application Guide itself was not reached.

### Scores (1–5, tough reviewer; criteria as reconstructed in "How this proposal meets the criteria")

| Criterion | Before | After | Why |
|---|---|---|---|
| E. Eligibility and format | 1 | 2 | Before: the request (≈ 9.7 RGU-years, ≈ 2–3 core-years, 20 TB) was below both RAC minimums, and the package did not know the minimums existed. After: the shortfall is stated, and a 20 Oct gate plus the RAS track route around it. It stays ineligible unless the gate passes. Guide headings and limits are still unread |
| S1. Scientific excellence | 3 | 4 | Clear question and hypotheses. Before: a grant proposal cited as literature (STRATEGY rule 4); planned NSERC work presented as completed; unsupported literature claims; no allocation-year deliverables. After: fixed, plus measurable deliverables A1–A3 |
| S2. Resource appropriateness | 2 | 4 | Before: the CPU total of [2] core-years contradicted its own lines (≈ 3.4); SAPIEN CPU "~1 core-year" should be 8 × 7,000 = 56,000 core-hours; the Tier-2 worst case (60,000) did not follow from its stated 5-pass derivation (≈ 20,800); a cut-order figure was wrong; nearline was used for active data; the claim that "RAS ~1 TB cannot carry this" was false. After: all corrected and reconciled with the bundle (budget_and_timeline.md §7) |
| S3. Likely efficient use | 2 | 3 | Before: Isaac Lab placed on H100 ("H100 nodes qualify"), though it needs RT-core GPUs; no usage history; the lead user was assumed onsite in April. After: RTX placement, calibration before the gate, remote Q1, and a June-or-later start. Still no measured costs and no RAC history |
| S4. Team / HQP | 2 | 2 | Training content is now concrete, but trainee names and usernames are placeholders only the PI can fill, and the collaborator is unnamed. Rises to 3 once the PI names real trainees |
| S5. Fit with the RRG stream | 2 | 3 | Before: asked RAC for storage and CPU that RAS covers. After: the honest RAS/RRG split. Data stewardship was already good |

### What changed

- **Eligibility gate added** (README, proposal note, budget_and_timeline.md §0, referee_brief.md, statement.md memo, emails.md §1/§2/§5). The default is now a sponsored role plus a RAS storage request; the RRG goes in only if the gate passes on 20 Oct; the matrix is not padded. The break-even (≈ 61 H100-hours per run) is computed and shown.
- **Numbers corrected and reconciled** with the compute bundle (budget_and_timeline.md §7): CPU 1.4 expected / 2 planned / 3.3 worst case; SAPIEN cores ≈ 6.4 core-years inside GPU jobs; Tier-2 worst case 20,800 (5 passes); cut order corrected; storage recategorized (project via RAS, raw corpora on scratch, no nearline).
- **Bundle errors to fix in the bundle as well** (not edited here): "~1 core-year" SAPIEN CPU; the Tier-2 worst case of 60,000 against a 5-pass derivation; "RAS default (~1 TB) cannot hold this"; "nearline/scratch" for active raw corpora.
- **Start date** changed from April to [June 2027 or later] in every file (STRATEGY Addendum 6), with remote Q1 use as an external collaborator [verify].
- **Hardware:** Isaac Lab moved to RTX-class GPUs [Killarney L40S, if confirmed] or the NVIDIA Academic Grant; SAPIEN Vulkan support flagged for verification.
- **Facts:** grant-proposal citation [6] removed (the NSERC program now appears as funding, status bracketed); "production scale" softened to what the profile supports (Uing Technologies, ontology-based representations); "core contributor" carries [confirm role wording]; the ISO 24707 year is bracketed (the PI's text says 2017); [18] and [19] are now cited; "the Alliance scores reuse" is bracketed. Every other number, date, title and award was traced to the profile, the registry, the PI's NSERC texts or the 2026-09-25 searches.
- **Deliverables A1–A3** added to proposal.md §2; §3 trimmed to what can be supported; §5 given concrete training on the allocation; a cut order for a short page limit added.

### Remaining risks

1. **Eligibility (decisive).** The minimums come from a search snippet, not the RAC 2027 Guide. If they hold, RAC 2027 is almost certainly a no-go: the 20 Oct gate requires a measured per-run cost about 2.5× the assumption, and the calibration depends on the sponsored role (or HMS GPU access) being live by ~10 Oct. STRATEGY §1.6 ("~50% for a scaled-back first-year award") should be revised.
2. **O3 GPU has no sustained route in 2027–28 without RAC.** RAS opportunistic GPU gives no guaranteed throughput; the NVIDIA Academic Grant, Vector compute and a collaborator's allocation are all unconfirmed. The matrix likely stretches into 2028.
3. **Unread Guide:** headings, page/character limits, criteria weights, portal, CCV variant, AI-compute route, RGU table.
4. **CCDB:** can a US-based external collaborator be sponsored now and use resources remotely until June 2027? Is the PI's account active?
5. **HQP placeholders, the unnamed collaborator, and the NSERC grant status**: only the PI can supply them.
6. **Hardware claims** (H100/A100 lacking RT cores for Isaac Lab; L40S on Killarney; Vulkan for SAPIEN) come from reviewer knowledge and must be verified on the vendor and cluster pages.
7. **Every count remains an assumption** (instances, seconds per instance, passes, splits, seeds, GPU-hours per run, storage).
8. **Profile gaps** that propagate here: the second Synthese title, the thesis title, the ISO role wording, the HMS appointment details.

2026-09-26: committee attribution corrected from SC 42 to SC 32 for ISO/IEC 21838 (see STRATEGY Addendum item 12).
