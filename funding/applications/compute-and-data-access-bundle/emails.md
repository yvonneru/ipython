# Emails — compute and data access bundle

Send order: **1** to Prof. Grüninger by 2 Oct 2026 (fold into, or send right after, the CPRA supervision email drafted for this week — he needs to decide on RAC 2027 by ~9 Oct); **2** to the HMS supervisor by 3 Oct 2026; **3** to the AXIOMALITY CTO by 2 Oct 2026 (entity facts gate every company application); **4** (RAC draft) to Prof. Grüninger by 20 Oct 2026; **5** to HMS Research Computing when the supervisor has agreed; **6** to a U of T Robotics Institute / Vector faculty member in January 2027. [Brackets] to fill in. Dataset-holder emails are in dataset_licences.md §4; the ManiSkill maintainers' email is applications.md §J.

---

## 1. To Prof. Michael Grüninger — by 2 Oct 2026

**Subject:** Compute for the postdoc program: a sponsored Alliance (CCDB) role now, and a RAC 2027 request by 3 November

Dear Michael,

Following the CPRA material [adjust: "and your reply of [date]"], one practical matter with a near deadline. The audit and simulation parts of the program need compute that I cannot obtain in my own name in Canada, and the only route to *sustained* GPU time from spring 2027 is the Digital Research Alliance of Canada's Resource Allocation Competition. RAC 2027 opened on 23 September and closes on **3 November 2026**, for allocations running 1 April 2027 – 31 March 2028 — which is exactly the period in which the SAPIEN policy experiments would run in your lab. Postdocs cannot apply; the PI must. May I ask four things?

1. **Do you hold an active CCDB (Alliance) account**, and does the group currently have any RAC allocation or default (Rapid Access) usage? If you have a CCRI, I will need it for the next point.
2. **Would you sponsor a CCDB role for me now** — as an external collaborator while I am at Harvard, converted to a postdoctoral role when the appointment starts? The default allocation costs nothing and needs no application; I would use it to prototype the audit pipeline on CPU nodes, run small ablations on the opportunistic GPU queues, and above all to hold the ontology instance store ([2–10 TB]) before my Harvard cluster access ends in spring 2027. Logged usage also strengthens a 2028 renewal.
3. **Would you submit an RRG request for RAC 2027 naming me as incoming postdoctoral fellow?** I would draft the whole thing — a one-page research description in Alliance format and the resource justification — and send it to you by **20 October** for review, so that your effort is limited to checking it, updating your CCV in CCDB if needed, and submitting via the portal. I propose a deliberately modest first-year ask, since first requests without RAC history are usually scaled back: on the order of [0.6–0.9] GPU-years on an H100-class system (Killarney or Trillium-GPU), [2] CPU core-years for the Datalog/SMT and Prover9/Mace4 audits, and [20 TB] project plus [50 TB] nearline storage for the seven corpora. The audit portion continues the lab's theorem-proving workflow; the GPU portion is new for the group, and I will bring pilot results from Harvard (ACCESS/NAIRR allocations I am requesting now) to make the per-run cost credible.
4. Two smaller questions for later: whether you would be PI on an **NVIDIA Academic Grant** application (in-kind GPU hardware or DGX Cloud credits; themed windows) once I am at U of T, ideally with a Robotics Institute or Vector co-PI whose group trains policies — an introduction to one such colleague would help; and whether a lab RTX-class workstation could be available from April 2027 so that the Isaac Lab simulator can move with me.

If the answer to (3) is no, or the timing is impossible this year, the fallback is the default allocation plus my US allocations while at Harvard, and a RAC 2028 request — so nothing is lost, but the spring-2027 GPU work would be thinner. I would need your decision on (3) by about 9 October to make the 3 November date comfortably.

Thank you — I know the timing is tight.

Best,
Yi

Yi Ru · Postdoctoral Researcher, Harvard Medical School · yi.ru@alumni.utoronto.ca

---

## 2. To the HMS postdoctoral supervisor — by 3 Oct 2026

**Subject:** Compute and data-access requests for my ontology-audit project — sponsorship and sign-offs I need from you

Dear [Dr./Prof. supervisor name],

Alongside the fellowship applications for the Toronto move [adjust if the supervisor is not yet aware], I am setting up the compute and data access that my dataset-audit project needs over the coming six months. Several requests require you as sponsoring PI, or your name as PI/co-PI so that the allocation survives my departure in [April 2027 or later]. None of them costs the lab money or, as far as I can tell, more than a few minutes of your time; I have drafted every text. May I ask for the following?

1. **O2 cluster account.** Would you sponsor an O2 account for me through the HMS Research Computing form, and confirm in writing (a two-sentence note is enough; draft attached) that the audit workload — CPU-bound batch checking of public robotics-dataset annotations against a formal ontology, with the toolkit generalizing to hierarchical labels in medical imaging — may run under the lab's allocation? Estimated need: [~4,000] core-hours and [15–20 TB] of scratch or lab storage between now and March; [please tell me if the lab's storage quota or per-TB charges make the storage part impractical, in which case I will put the raw data on cloud research credits instead]. [If our appointment is hospital-based rather than Quad-based, please point me to the right cluster — I will adapt the request.]
2. **NSF ACCESS and NAIRR Pilot.** I intend to request a small ACCESS "Explore" allocation (one-paragraph abstract; CPU on Bridges-2/Anvil plus a few hundred GPU-hours on DeltaAI) by 15 October, and a NAIRR Pilot allocation (1–2 pages; GPU pilot for the simulation experiments plus storage) by 30 November. Both are tied to a US institution. Would you agree to be named **co-PI (ACCESS) and PI (NAIRR)** — or PI on both if the postdoc-as-PI rule has changed — so that the allocations continue under the lab after I leave, with me as a user? I would write and manage everything; your part is agreement and a CV.
3. **Cloud research credits.** I plan to apply for Google Cloud research credits (by 24 October) and AWS Cloud Credit for Research (by 15 November) for object storage and batch checking. The AWS form asks for the PI/lab AWS account that will hold the credits — could you tell me whether the lab has an AWS account you would allow for this, or whether I should ask HMS Research Computing to set one up? For Google, I only need to let you know before I apply, and to confirm with HMS IT whether the credits must sit in a Harvard-managed billing account.
4. **Simulator on lab hardware.** If the lab has an RTX-class GPU workstation that is not fully used, may I install Isaac Lab (open source) on it to reproduce one articulated-object task before the end of December? A cloud GPU is the alternative.
5. **Conflict-of-interest reporting.** I founded a company (AXIOMALITY) that works on robotics-data verification. No company work will run on O2 or on any research allocation, and the datasets I register for academically will not be used by the company. Could you point me to the HMS outside-activity / COI reporting route so that this is on record by mid-October?
6. **Data hand-off.** Before I leave I will mirror the audit outputs and code to University of Toronto / Alliance storage and close or transfer the allocations; I will send you a short plan by 1 March 2027.

[Optional: 7. NVIDIA's Academic Grant Program offers in-kind GPUs/credits under themed calls and requires a faculty PI; if a Physical AI or Simulation theme is open this autumn, would you consider submitting with me as lead researcher? Otherwise I will do this from Toronto.]

I attach: the O2 justification and your draft note; the ACCESS and NAIRR abstracts; a one-page summary of the project. Could we take ten minutes at [next meeting] to go through them?

Thank you very much.

Yi Ru · Postdoctoral Researcher, [laboratory], Harvard Medical School · [harvard.edu address]

---

## 3. To the AXIOMALITY CTO — by 2 Oct 2026

**Subject:** Company-side credit applications (NVIDIA Inception, Google for Startups, AWS Activate) — facts I need from you and a split of tasks

Hi [CTO name],

Three no-cash, no-equity programs would cover the Q4 2026 Engine internal test and the Q1 2027 batch verification of 10,000 episodes: NVIDIA Inception (partner cloud credits, DGX Cloud and Isaac/Omniverse enterprise access, OEM introductions), the Google for Startups Cloud Program (Start tier now; Scale/AI-first only after a financing round or a recognized accelerator), and AWS Activate (Founders tier now; Portfolio up to a much larger cap only with an Activate Provider such as CDL, UTEST, MaRS or a US accelerator). I have drafted all the texts. What I need from you, in order:

1. **Entity facts, by 10 October:** legal entity name; country and province/state of incorporation; incorporation date; CRA business number / EIN; employee count; revenue to date; whether the entity is Uing Technologies (Aug 2022) or a new AXIOMALITY entity; founder residency; cap table summary. Every form asks for these, and a China-incorporated entity would lose some partner credits and hardware offers — if that is the case we should decide whether to apply from a US or Canadian entity.
2. **Prior credits:** has Uing Technologies ever received AWS Activate or Google Cloud startup credits? Both programs have one-award-per-company rules or lifetime caps.
3. **Website and domain email, by 31 October:** Inception, Google and AWS all require a live company website and a company-domain address. [Status of the site?]
4. **Accounts:** a company AWS Organizations account and a company GCP billing account in the entity's name. These must never touch my Harvard or University of Toronto accounts, and nothing from the company may run on academic allocations — I am reporting the company to HMS under their COI route, so the separation has to be clean in both directions.
5. **Submissions (you as submitter; I review):** Inception between 16 and 31 October (the September deck is adequate; texts attached); Google Start by 31 October *only if* the FAQ confirms that a Start award does not block a later Scale/AI-first upgrade; AWS Activate Founders by 15 November (about 30 minutes) and any stackable generative-AI offer. After Inception acceptance, each partner credit (AWS, Azure, OCI, GCP) is a separate application through their portal.
6. **Q1 2027 compute budget, by 31 October:** instance-hours and TB-months for the 10,000-episode SMT/Datalog checks and hosting of the 100k asset packages, so that every credit request is quantified rather than guessed.
7. **Open-source boundary, by 31 October:** I want to release a LeRobot-compatible parthood validator under Apache-2.0 by 15 January 2027 (it is the public deliverable the fellowship applications need). Proposal: the solver-free axiom checks and the report format go out; the Passport, the physics residuals, the conformal abstention and the SMT compilation stay in. Please confirm or redraw the line.
8. **Datasets and counsel, Q1 2027:** ShapeNet, PartNet, PartNet-Mobility, GAPartNet and AgiBot World are non-commercial; only DROID and the CC BY subsets of Open X-Embodiment can appear in commercial evidence packs without agreements. Before any partner pilot we need counsel's written position, including whether internal Engine validation on a non-commercial dataset counts as commercial use, and whether to approach Stanford, UCSD and AgiBot for data agreements (enquiry template attached).
9. **Accelerator route, by 31 January 2027:** pick the Activate Provider / Google-recognized accelerator we actually want (CDL-Toronto, UTEST, MaRS, Techstars, YC, Robotics Factory) — it unlocks the Portfolio and Scale tiers. And a calendar note for 1 May 2027 to check the AWS Generative AI Accelerator window.

Attached: the Inception, Google Start and Activate texts; the counsel enquiry template; the dataset licence table.

Thanks,
Yi

---

## 4. To Prof. Grüninger — RAC draft, by 20 Oct 2026 (only if he said yes)

**Subject:** RAC 2027 RRG draft — research description and resource justification for your review

Dear Michael,

Attached is the RAC 2027 RRG draft: a one-page research description in the Alliance format and the resource justification table (GPU in RGU [conversion per the Alliance page], CPU core-years, large-memory jobs, project and nearline storage, software), plus the HQP line with my name — please add any students whose COLORE/PSL work should appear. Three things for you to check: (1) the "past usage" section, which I have left for you; (2) whether the AI-compute request (Killarney) belongs inside this form or in a separate call this year — I could not confirm it; (3) your CCV in CCDB. I have kept the ask modest and cited the pilot allocations at Harvard as the basis for the per-run cost. The deadline is 3 November; I am available to make any edits the same day.

Thank you,
Yi

---

## 5. To HMS Research Computing — with the account request, after email 2 is answered

**Subject:** O2 account request — [Yi Ru], sponsored by [supervisor], [laboratory]

Dear HMS Research Computing,

I have submitted the O2 account-request form [ticket/date] with [supervisor name] as sponsoring PI. The workload is CPU-bound batch computing (array jobs of short SMT/Datalog checks and theorem-proving tasks; [2–4] jobs needing ~256 GB memory) on public research datasets, with [15–20 TB] of scratch needed for about six months. Could you confirm (1) the base storage quota for the lab and the charge for additional scratch, (2) the partitions and any per-user limits I should target for array jobs, and (3) whether any additional approval is needed for GPU partitions should the PI later permit a small number of GPU jobs? Thank you.

Yi Ru · Postdoctoral Researcher, [laboratory], Harvard Medical School · [harvard.edu address]

---

## 6. To a U of T Robotics Institute / Vector faculty member — January 2027, after Prof. Grüninger names them

**Subject:** NVIDIA Academic Grant co-PI and simulation compute for an ontology-verified articulated-object project (from April 2027)

Dear Prof. [name],

Prof. Michael Grüninger suggested I write to you. I join his Semantic Technologies Laboratory as a postdoctoral fellow in [April 2027 or later], after a postdoc at Harvard Medical School and a PhD in MIE (2025). My program audits the part annotations of robot-learning datasets (PartNet-Mobility, GAPartNet, AgiBot World, Open X-Embodiment, DROID) against a machine-verified ontology of object parts, and then uses the ontology as an inductive bias for part-aware manipulation policies in SAPIEN and Isaac Lab, reporting ontology-violation rate alongside task success. A first public audit result is at [link, 15 Jan 2027].

Two asks. First, NVIDIA's Academic Grant Program offers in-kind GPU hardware or DGX Cloud credits under themed calls (Simulation / Physical AI), and a submission from a group that already trains policies would be far stronger than one from a knowledge-representation lab alone: would you consider being co-PI with Prof. Grüninger, with your group receiving [the workstation / a share of the credits] and co-authorship on the policy-training papers? I have a draft compute plan ready. Second, if your group has an RTX-class workstation or an allocation on which an Isaac Lab installation could live from April, that would let the simulator move with me.

Could we speak for twenty minutes in the coming weeks? I am in Boston until [date] and can meet online at any time.

Best regards,
Yi Ru · Postdoctoral Researcher, Harvard Medical School · yi.ru@alumni.utoronto.ca
