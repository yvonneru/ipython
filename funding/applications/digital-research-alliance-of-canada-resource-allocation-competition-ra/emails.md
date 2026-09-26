# Emails — RAC 2027 RRG

*Send order: §1 to Prof. Grüninger by 2 Oct 2026 (fold into, or send immediately after, the CPRA supervision email in source_drafts/emails_gruninger_sgs_referees.md; it supersedes §1 of the compute-bundle emails for the RAC part); §5 to MIE research services by 10 Oct; §2 to Prof. Grüninger by 20 Oct, choosing the variant that matches the gate result (budget_and_timeline.md §0); §3 to Prof. Grüninger on 28 Oct as the final nudge; §4 to the HMS supervisor in October; §6 to the AXIOMALITY CTO in October. No referee emails exist for this program. [Brackets] to fill in.*

---

## 1. To Prof. Michael Grüninger — by 2 Oct 2026

**Subject:** Alliance compute for the postdoc program: a sponsored CCDB role, a RAS storage request, and possibly a RAC 2027 request (closes 3 Nov)

Dear Michael,

Following the CPRA material, one practical matter with a near deadline. The audit and simulation parts of the program need Alliance compute and storage that I cannot request in my own name. RAC 2027 opened on 23 September and closes on **3 November 2026**, for allocations running 1 April 2027 – 31 March 2028. Postdocs cannot apply; the PI must. One complication first. Search results attribute to the Alliance a minimum RAC request of 200 core-years of CPU or 25 RGU-years of GPU, and say a PI can get up to 40 TB of project storage through the Rapid Access Service without any RAC [I could not open the page to verify]. My honest estimate is about [7,000] GPU-hours (≈ [10] RGU-years on H100), ≈ [1.4] CPU core-years and [20 TB] of project storage. That is below the RAC minimum and inside RAS. So the ask is in three parts:

1. **Do you hold an active CCDB (Alliance) account**, and does the group currently have any RAC allocation or Rapid Access usage? If you have a CCRI, I will need it for the next point.
2. **Would you sponsor a CCDB role for me now** (external collaborator while I am at Harvard, converted to a postdoctoral role when the appointment starts, in June 2027 or later), **and request 20 TB of RAS project storage for the group?** Neither needs a competition. I would use them to prototype the audit pipeline, run [1–2] GPU calibration runs on the opportunistic queues, and hold the ontology instance store before my Harvard access ends. The logged usage is what a later RAC request needs.
3. **Would you be willing to submit an RRG request for RAC 2027, but only if it clears the minimum honestly?** The deciding numbers are the per-run GPU cost (the break-even is about [61] H100-hours per run, against my assumed [24]) and the RAC 2027 Guide's rules for AI compute. I will have both by **20 October**. If the answer is go, the draft is ready: research description in your NSERC structure, resource justification with every number derived, HQP line, data-management paragraph. Your part would be checking it, writing the past-usage lines, listing any students, updating your CCV in CCDB, and submitting by 30 October. If the answer is no-go, we skip RAC this year and apply in RAC 2028 with a year of usage.
4. Do you know whether U of T requires any internal step for RAC, and whether Killarney (AI compute) is requested inside the RRG form this year or in a separate call? I will also ask MIE research services.

I would need your answer on (1)–(2) by about **9 October**; (3) is decided together on 20 October.

Thank you — I know the timing is tight.

Best,
Yi

Yi Ru · Postdoctoral Researcher, Harvard Medical School · yi.ru@alumni.utoronto.ca

---

## 2. To Prof. Grüninger — gate result, 20 Oct 2026

**Variant A — gate not passed (default).** **Subject:** RAC 2027: recommend we skip this year; RAS storage instead

Dear Michael,

The RAC 2027 Guide [states / does not change] the minimum of 25 RGU-years GPU and 200 core-years CPU. The calibration run gave [N GPU-hours per run / no result yet], which puts the matrix at [X] RGU-years, below the minimum. I recommend we do not submit the RRG this year. The RAS storage request [filed / still to file] covers the instance store, and the audit runs on RAS CPU. I will prepare a RAC 2028 request with a year of logged usage behind it. Nothing further is needed from you for 3 November.

Best,
Yi

**Variant B — gate passed.** **Subject:** RAC 2027 RRG draft — research description, resource justification and my compute memo, for your review

Dear Michael,

The gate passed: [the Guide's rule for AI compute / the measured per-run cost of N GPU-hours puts the request at X RGU-years]. Attached: (1) the RRG application text in the Alliance's sections, written in your voice and your NSERC structure — recent progress, objectives with the long-term challenge, literature review, methodology as themes and projects with open questions tagged to trainee slots, team, outcomes, past usage, resource summary, data management, bibliography; (2) the resource request with the full derivation in RGU, core-years and TB, and a stated cut order; (3) a memo from me explaining every number so you can defend the request if the technical reviewers ask; (4) the CCDB role text I used to register [confirm you have approved the role].

Five things for you: (a) the **past usage** section, which I have left for you — RAS usage from my role since [date] is [figures]; (b) the **HQP list** — please add any students whose COLORE/PSL work should appear, with CCDB usernames, and replace my MASc1/MASc2/PhD1 placeholders (or delete them); (c) your **CCV in CCDB** [verify the required variant]; (d) the bibliography entries marked [complete], which are your references; (e) the award status, number and term of the *Commonsense Cobotics* NSERC grant, which §1 now names as the program's funding rather than citing the proposal. Two open format points I could not settle by search: the exact section headings and length limits in the RAC 2027 Application Guide, and whether Killarney is requested inside this form — I have sized the description to about three pages and will re-fit it the same day once you or research services confirm. The pilot at Harvard has [measured GPU-hours per run: N / not yet completed]; I have [replaced / left bracketed] the per-run figure accordingly.

The deadline is 3 November; submitting by 30 October leaves slack. I am available for same-day edits.

Best,
Yi

---

## 3. To Prof. Grüninger — final nudge, 28 Oct 2026 (only if Variant B was sent)

**Subject:** RAC 2027 — submission by Friday 30 Oct?

Dear Michael,

A short reminder that RAC 2027 closes on Tuesday 3 November; submitting by Friday 30 October leaves room for portal problems. Everything on my side is final [with the measured per-run figure from the pilot: N GPU-hours]. If anything in the form does not accept the text as drafted (character limits, section names), send me the field names and I will re-fit within the hour. Please forward the confirmation email when it goes in.

Thank you,
Yi

---

## 4. To the HMS postdoctoral supervisor — October 2026

**Subject:** Heads-up: Alliance (Canada) compute request for the Toronto period, and the data hand-off plan

Dear [Dr./Prof. supervisor name],

A brief note so nothing surprises you. Prof. Grüninger at the University of Toronto is arranging compute and storage at Canada's Digital Research Alliance, from now and possibly through 31 March 2028, for the ontology-audit and policy-training program I would run in his lab after leaving here. Nothing in it involves this lab or Harvard resources, and it does not overlap with the ACCESS/NAIRR/O2 requests for the current period, which end with my appointment. What it does mean is that the audit instance store and code produced here ([2–10 TB], no raw frames) would be mirrored to Alliance storage before I leave; I will send you a one-page hand-off plan by 1 March 2027 and will make sure the lab retains a copy of anything it wants.

Thank you,
Yi

---

## 5. To MIE research services / the U of T Alliance (SciNet / Compute Ontario) contact — by 10 Oct 2026

**Subject:** RAC 2027 RRG application from Prof. Grüninger (MIE) — internal requirements and two format questions

Dear [name],

Prof. Michael Grüninger (MIE) intends to submit a Resources for Research Groups request in the Digital Research Alliance of Canada's RAC 2027 (closes 3 November 2026) for a postdoctoral program I will lead in his laboratory from [June 2027 or later]; I am drafting the application. Four questions: (1) Does the University of Toronto require any internal review, signature or notification for RAC applications, and if so by when? (2) Can you point me to the RAC 2027 Application Guide (section headings, length limits, review criteria) and to the current RGU conversion table and storage categories? I have not been able to reach the PDFs from here. (3) Is AI compute on Killarney requested inside the RRG form this year, or through a separate call, and does the minimum request of 25 RGU-years GPU / 200 core-years CPU apply to it? (4) How does a PI request RAS project storage above the default (up to 40 TB), and what are the scratch quota and purge policy on the likely target cluster? I am also registering as a sponsored user under Prof. Grüninger's CCRI; if U of T has guidance for external collaborators registering before an appointment starts, I would be grateful for it.

Thank you,
Yi Ru · Postdoctoral Researcher, Harvard Medical School · yi.ru@alumni.utoronto.ca

---

## 6. To the AXIOMALITY CTO — October 2026

**Subject:** Academic compute allocation in Canada — firewall between company work and the U of T allocation

Hi [CTO name],

For the record: Prof. Grüninger is arranging academic compute and storage (Digital Research Alliance of Canada, a Rapid Access storage request now and possibly a RAC allocation for 1 Apr 2027 – 31 Mar 2028) for my postdoctoral program. The application states that AXIOMALITY does not use any resource requested and that company workloads run on separately funded company accounts. Please make sure nothing in our Q4 2026 – 2027 compute plan assumes access to it, and that no company data or code is ever placed on an academic account of mine — the same rule as for the Harvard cluster. The academic outputs that are open-licensed (the validator, the ontology, audit reports) can be consumed by the company like any other public artefact; the non-commercial datasets cannot. Shout if anything in the Q1 2027 plan conflicts with this.

Thanks,
Yi
