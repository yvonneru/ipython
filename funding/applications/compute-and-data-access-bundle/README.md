# Compute and data access bundle — compute, storage and dataset access for O2 (dataset audit) and O3 (SAPIEN policy experiments)

**Applicant:** Dr. Yi Ru · **Sponsors:** Prof. Michael Grüninger (MIE, U of T — Canadian PI from spring 2027), the HMS postdoctoral supervisor [name] (US PI/co-PI while at Harvard), AXIOMALITY CTO [name] (company-side applications) · **Bundle of 13 program families / 16 registry records, tiers A–B** · package drafted 2026-09-25

This is one package for every in-kind resource the research program needs — compute, storage, simulators, dataset licences and a public-release channel — rather than one package per program, because none of them pays salary, all are rolling or near-rolling, and they only matter in combination: O2 needs data plus CPU and storage by winter 2026–27, O3 needs sustained GPU from spring 2027. Files: this README (table, order, requirement estimate, bracket list), `applications.md` (paste-ready texts), `dataset_licences.md` (licence table and request emails), `emails.md` (sponsor emails).

## Verification caveat

The WebSearch budget of the session that built the registry was exhausted and funder pages could not be fetched, so **every record in this bundle carries verdict `unverifiable`**: amounts, caps, review cadences and eligibility wordings below are the registry's prior-knowledge paraphrases, not fresh snippets. Open the official URL in the table before relying on any figure. Where the registry gives no figure, this package says "[confirm on program page]" rather than guessing.

## The two dates that drive the order

| Milestone | What must be in place | Source |
|---|---|---|
| **17 Oct 2026** (CPRA deadline) | Registrations for all audit corpora complete so the proposal can state the data is in hand | dataset-licences record: "complete registrations before the CPRA submission" |
| **15 Jan 2027** (self-imposed) | A public LeRobot-compatible parthood validator plus an audit report on 2–3 public datasets, citable in the DSI (Jan 2027) and Vector (28 Feb 2027) applications — needs CPU, storage and data from Oct 2026 | LeRobot record |
| **1 Apr 2027** | Alliance RAC 2027 allocation period begins (1 Apr 2027 – 31 Mar 2028) if Prof. Grüninger applies by the early-November deadline [reported 3 Nov 2026 — confirm]; this is the only route to *sustained* GPU for O3 in Toronto | RAC record |
| **Spring 2027** (Harvard → U of T move) | Every US-held allocation (HMS O2, ACCESS, NAIRR, AWS/Google research credits) either ends or must have the Harvard supervisor as PI; data must be mirrored to Alliance storage by 1 Mar 2027 | HMS O2, ACCESS, NAIRR records |

The research program (profile/research_program.md) places the audit pipeline and first audit in M1–8 (24-month plan) or M4–8 (12-month plan) and the policy experiments in M8–24 / M8–12, so the practical requirement is: **data + CPU + ~15 TB by Nov 2026; pilot GPU (hundreds of GPU-hours) by Jan 2027; sustained GPU (thousands of GPU-hours) and ~50 TB from April 2027.**

## Program table

Legend for "Who applies": **Ru** = Dr. Ru as an individual researcher; **MG** = Prof. Grüninger as Canadian faculty PI; **HMS** = the Harvard supervisor as US PI/co-PI; **AX** = AXIOMALITY as a company. "Unconfirmed" lists eligibility conditions the registry could not verify. "Order" is the sequence position in the next section.

| # | Program (registry id) | What it gives | Who applies | Eligibility conditions still unconfirmed | How / where to apply | Expected turnaround | Order |
|---|---|---|---|---|---|---|---|
| 1 | **Dataset access licences** — ShapeNet, PartNet, PartNet-Mobility/SAPIEN, GAPartNet, AgiBot World, Open X-Embodiment, DROID (6981053de7aa) | The corpora O2 audits and O3 pools; zero cost; licence split: ShapeNet/PartNet/SAPIEN/GAPartNet/AgiBot World non-commercial; OXE mostly CC BY 4.0 / Apache-2.0 per sub-dataset; DROID CC BY 4.0 (data) + MIT (code) — all "as best known, unverified" | Ru (institutional email: harvard.edu now; utoronto.ca from spring 2027). AX is excluded from the non-commercial sets without separate agreements | Current terms text of each dataset; whether derived annotations (corrected labels, mappings) may be published; whether registration binds to the registering institution; whether alumni.utoronto.ca is accepted; licence of AgiBot World Beta releases; PartNet-Ensembled terms [not in the registry at all] | shapenet.org and partnet.cs.stanford.edu registration; sapien.ucsd.edu account + terms; GAPartNet request form via github.com/PKU-EPIC/GAPartNet; Hugging Face gated acceptance at huggingface.co/agibot-world; OXE table at robotics-transformer-x.github.io; DROID at droid-dataset.github.io | Registrations: [turnaround not recorded — confirm]; OXE/DROID/AgiBot World need no approval (HF account for AgiBot) | 1 |
| 2 | **Harvard institutional compute — HMS O2 cluster** (Cannon and Kempner only via faculty collaborators) (24dcc2eb2b71) | Shared CPU and GPU partitions (e.g. gpu, gpu_quad) and a base storage quota for HMS labs at no direct cost; extra storage and some services charged to the lab. No cash; ends with the Harvard appointment; academic use only | Ru, sponsored by HMS | Whether the HMS appointment is Quad-based (O2) or hospital-based (then the hospital cluster, e.g. MGB ERIS); supervisor's written agreement that robotics-dataset audit work may run under the lab; current account-request route, GPU partition names, storage quota and charges; HMS outside-activity/COI reporting for AXIOMALITY | HMS Research Computing account-request form with sponsoring-PI approval; wiki: harvardmed.atlassian.net/wiki/spaces/O2/overview | Rolling; requests processed continuously [days — confirm] | 2 |
| 3 | **Digital Research Alliance of Canada — Rapid Access Service (RAS)** via a sponsored CCDB role (6c92ea507e9e) | Per-PI-group default allocation: opportunistic CPU and GPU queues (GPU at low priority behind RAC groups), default project storage (typically ~1 TB project, larger scratch), small default cloud/AI-compute quotas where offered. No cash; continuous; renewed with the annual CCDB role renewal | MG sponsors; Ru registers (external collaborator now, postdoc from the U of T start) | Whether Prof. Grüninger has an active CCDB account; whether an external collaborator at a US institution can be sponsored before the appointment starts; current default GPU/storage quotas; whether Killarney/PAICE (AI compute) is inside RAS defaults | ccdb.alliancecan.ca: register with name, institutional email, position, sponsor's CCRI; sponsor approves in CCDB; sign the Alliance user agreement | Available as soon as the PI approves the role (1 day of prep) | 3 |
| 3b | **Digital Research Alliance of Canada — Resource Allocation Competition (RAC) 2027, RRG stream** (e1dfb65e5146; added because it is the only sustained-GPU route for O3 from April 2027) | GPU allocations in reference GPU units (RGU) on H100-class systems (Killarney, Trillium-GPU, Fir, Rorqual, Nibi), CPU core-years, storage, cloud; allocation 1 Apr 2027 – 31 Mar 2028, renewable (fast-track if unchanged). First-year GPU asks without RAC history are routinely scaled back | MG as PI (postdocs cannot be PI); Ru as sponsored user | RAC 2027 window (scout report: opened 23 Sep 2026, closes 3 Nov 2026 — not re-verified; fast-track ~2 weeks earlier); whether AI compute (Killarney/PAICE) is requested inside the RRG form or in a separate call; PI eligibility wording; the URL slug (…/resource-allocation-competition vs …-competitions); Prof. Grüninger's CCV current in CCDB; his group's GPU history | Alliance application portal (alliance.smapply.ca), submitted by the PI: research description, resource justification, HQP/team list, PI CCV | Decision → allocation effective 1 Apr 2027 | 4 |
| 4 | **NSF ACCESS allocations** — Explore / Discover / Accelerate (Maximize >3M) (5dca99a0213e) | In-kind ACCESS credits exchanged for time on Delta/DeltaAI, Bridges-2, Anvil, Expanse, Jetstream2 etc.: Explore up to 400,000, Discover up to 1,500,000, Accelerate up to 3,000,000, Maximize above 3M [caps from prior knowledge — confirm on allocations.access-ci.org/project-types]; GPU nodes are expensive at the exchange rate; 12 months, renewable, supplements possible | Ru as PI (postdoc-as-PI rule [confirm]) with HMS as co-PI or PI so the allocation survives the move | Postdoc-as-PI wording; current caps and GPU exchange rates; export-control restrictions on some resources (citizenship [UNKNOWN]); research use only — not for AXIOMALITY | allocations.access-ci.org: ACCESS ID; Explore = one-paragraph abstract + CV + resource selection; Accelerate = 3-page proposal with justification | Explore: rolling, "typically within ~2 weeks"; Accelerate: rolling with panel review; Maximize: semi-annual (mid-Dec / mid-June) | 5 |
| 5 | **Google Cloud Research Credits** (c4f8773a6f7f) | Typically up to ~USD 5,000 in Google Cloud credits per application [unverified — confirm]; expire ~12 months after issue; per-project awards, so a second application from utoronto.ca in 2027 is possible; non-commercial only | Ru (self-application [confirm] with institutional email); HMS informed beforehand | Whether a postdoc may apply in their own name or needs a faculty PI; whether Harvard/HMS (now) and U of T (2027) are on the eligible list; maximum amount and expiry; whether HMS IT / Harvard HUIT requires credits to sit in a Harvard-managed GCP billing account | cloud.google.com/edu/researchers online form: 200–500-word abstract, institutional email, resource estimate | Reviewed continuously [confirm] | 6 |
| 6 | **AWS Cloud Credit for Research** (e54329a0465e) | AWS promotional credits sized to the requested 12-month budget (typical grants "in the low tens of thousands USD" [unverified — confirm]); credits expire ~12 months after issue [unverified]; in-kind only; must build cloud-based tools, workflows or publicly shared datasets. Not for AXIOMALITY | Ru with institutional email, naming the PI/lab AWS account (HMS now; MG after spring 2027) | Whether the program is still accepting applications in its recalled form; current form fields and review cadence; postdoc in own name vs faculty PI; credit expiry term; whether HMS research computing must sign off on cloud credits | Online proposal form: project description, AWS services, timeline, sharing plan, 12-month credit budget by service; program URL in the registry; AWS Open Data Sponsorship Program for hosting the released corpus [read terms] | Periodic review batches, roughly quarterly [unverified] | 7 |
| 7 | **NAIRR Pilot compute and data resource allocations** (313549ff9e88) | In-kind: GPU hours on NSF systems (Delta/DeltaAI, Bridges-2, Anvil, Expanse) and DOE systems (Perlmutter, Polaris), cloud credits (Microsoft/AWS/Google), model-API credits, curated datasets; typically 12 months; no cash | Ru (US-based researcher at HMS) with HMS as PI or co-PI | Whether requests are still open (NAIRR Operations Center transition under NSF 25-546); whether a postdoc may be PI; current review cadence; which resources are US-persons-only or need DOE foreign-national review — citizenship [UNKNOWN], so prefer NSF systems and cloud/API credits | nairrpilot.org/opportunities/allocations: ACCESS ID; 1–2-page project description, resource justification (GPU-hours, storage, software), data-use statement, team list, expected outcomes and open-release plan | Smaller requests reviewed roughly monthly, larger in periodic cycles [confirm]; DOE user agreement + foreign-national review 4–12 weeks after award | 8 |
| 8 | **NVIDIA Isaac Sim / Isaac Lab / Omniverse free access** (+ Jetson education discount) (90e29ae17a69) | Free software: Isaac Sim (open-sourced 2025, Apache-2.0), Isaac Lab (BSD-3), Omniverse Kit SDK / USD tooling via GitHub/NGC (Launcher deprecated 2025). Jetson Orin Nano dev kit retail ~USD 249 with an education discount for verified students/educators [postdoc eligibility unverified]. No grant, no compute — needs an RTX-class GPU (~8 GB+ VRAM minimum, 16 GB+ recommended, Ubuntu 22.04/24.04 or Windows) or a cloud GPU from another row | Ru (NVIDIA Developer Program account); AX may use under the permissive licences (SimReady/asset packs and enterprise components have their own terms) | Current Isaac Sim 5.x / Isaac Lab system requirements; Jetson discount eligibility for postdocs and which email domains verify (harvard.edu likely; alumni.utoronto.ca probably not); which Omniverse components remain free | Download from developer.nvidia.com/isaac/sim, github.com/isaac-sim/IsaacSim, isaac-sim.github.io/IsaacLab — no application | None | 9 |
| 9 | **Hugging Face LeRobot community** — dataset contributions, LeRobot Worldwide Hackathon (b08ecff54fe8) | No cash; free Hub hosting for public datasets/models; adoption, visibility, a citable public artifact; hackathon prizes are hardware/credits at HF's discretion (2025 edition 14–15 June 2025; 2027 dates unconfirmed) | Ru personally, or an AXIOMALITY Hub organisation | Current LeRobotDataset format (v3), CONTRIBUTING.md and licence (Apache-2.0 — anything merged must be open source); which part of the audit engine can be released (validator, not the Passport); source-dataset licences may forbid re-hosting a merged corpus | PR to github.com/huggingface/lerobot with tests; Hub dataset card(s) with audit statistics and licence statement; optional Space demo; hackathon city registration ~4–6 weeks before the June event | Engineering task (15 prep days), not an application; self-imposed public date 15 Jan 2027 | 10 |
| 10 | **NVIDIA Academic Grant Program** — Simulation & Digital Twins / Physical AI track (6982d408a17b) | In-kind GPU hardware (workstation/data-centre class) and/or DGX Cloud credits plus software and technical support; per-award value not published; cloud credits for ~12 months [unverified]; hardware is donated to the institution | MG as faculty PI (from spring 2027), ideally with a GPU-oriented U of T Robotics Institute / Vector co-PI [name]; optional earlier route: HMS as PI under a currently open theme | Whether calls are rolling or themed windows, and which themes are open with what close dates; the eligibility wording on postdocs (historically: apply through the faculty PI); hardware vs credits for the Physical AI/Simulation theme; institutional acceptance/export rules for hardware | Online form at nvidia.com/en-us/industries/higher-education-research/academic-grant-program/: project description, expected outcomes, compute plan, PI CV / lab information | [Not recorded — confirm]; institutional acceptance of hardware 2–4 weeks after award | 11 |
| 11 | **NVIDIA Inception** — startup program (f624847b7f86; second record b82c4ffa6b14 adds the Physical AI Open Dataset / GR00T outreach route) | No cash, no equity: partner cloud-credit offers (historically AWS Activate, Microsoft for Startups/Azure, Google Cloud, OCI, CoreWeave/Lambda) unlocked by membership, each with its own application and cap; DGX Cloud and software trials/discounts (Isaac Sim, Omniverse, NIM); hardware purchase discounts; DLI credits; GTC exposure; VC and OEM introductions. Physical AI Open Dataset: NVIDIA-curated Hugging Face releases, no verified third-party submission call — treat as outreach via the Inception partner manager | AX (CTO/CEO); individuals cannot join | Legal entity name, country and incorporation date (Uing Technologies, Aug 2022, vs a new AXIOMALITY entity); a live company website and company-domain email; current eligibility text (historically incorporated, privately held, <10 years old, not a subsidiary, uses GPU acceleration); current partner-credit list; a China-incorporated entity can join but some partner credits and export-controlled hardware offers would not apply | nvidia.com/en-us/startups online application: company profile, stage, product description, use of NVIDIA technology; the Sept 2026 US/Canada deck is adequate | Acceptance "typically within weeks" [confirm] | C1 |
| 12 | **Google for Startups Cloud Program** — Start / Scale / AI-startup tiers (55bea54c0a16) | Start: ~USD 2,000 (pre-funded/bootstrapped); Scale: up to USD 200,000 over 2 years (equity funding from a recognized investor/accelerator, Series A or earlier); AI-first: up to USD 350,000 over 2 years plus Gemini/Vertex credits and technical support [all unverified — confirm]; one award per company; a Google for Startups Accelerator: AI First (North America) 2027 cohort is expected to open in Q1 2027 [unconfirmed] | AX | Legal entity, incorporation country/date; company website and domain email; whether Uing Technologies already consumed Google Cloud startup credits (one-award rule); whether a Start award blocks a later Scale/AI upgrade; the "recognized investor/accelerator" definition; no financing round yet → only Start reachable now | cloud.google.com/startup online application; incorporation details; funding evidence for Scale/AI tiers | [Not recorded — confirm] | C2 |
| 13 | **AWS Activate** (bc48b23e314b; second record 0a576098038a adds the AWS Generative AI Accelerator) | Activate Founders: ~USD 1,000 in credits, self-serve; Activate Portfolio: up to ~USD 100,000 via an Activate Provider organization ID; layered generative-AI credit offers; credits valid ~1–2 years [all unverified after AWS's 2024–25 changes — confirm]. Generative AI Accelerator: historically up to USD 1M in credits, 10 weeks, ~40 companies/year; 2026 window very likely closed, next expected ~May–Jun 2027 [unconfirmed] | AX | Legal entity, incorporation country/date, whether it is Uing Technologies and whether that entity already received Activate credits (lifetime caps); company AWS account and website; current tier names, caps, company-age rule and Provider requirement; an Activate Provider relationship (CDL-Toronto, UTEST, MaRS, a US accelerator) not yet in place | aws.amazon.com/startups/credits with the company AWS account and website; Portfolio with the Provider org ID; accelerator: online application, deck, demo video, team bios | Founders: self-serve (~30 minutes to request; decision time [not recorded — confirm]); Portfolio follows the accelerator's intake calendar; accelerator historically closes ~mid-June for a September cohort | C3 |

## Order of application

Academic and company tracks run in parallel and must never share an account, a billing profile or a storage bucket (every academic record says institutional or research credits may not be used for AXIOMALITY). Dates are the registry's next-action targets; anything in brackets is unconfirmed.

**Academic track (Dr. Ru; sponsors MG and HMS)**

| When | Step | Row |
|---|---|---|
| 25 Sep – 3 Oct 2026 | Confirm the HMS lab/department and whether it is Quad- or hospital-based (by 30 Sep). Register at shapenet.org, partnet.cs.stanford.edu and sapien.ucsd.edu with harvard.edu; save the accepted terms as PDF (by 3 Oct). Ask the HMS supervisor to sponsor an O2 account and give written OK for the audit workload (email 2; by 3 Oct). Send email 1 to Prof. Grüninger asking for a sponsored CCDB role now and a RAC 2027 RRG submission (by 2 Oct). Open the official RAS, RAC, ACCESS and NAIRR pages and record current quotas, caps and rules (by 3 Oct) | 1, 2, 3, 3b, 4, 7 |
| by 10 Oct 2026 | GAPartNet request form; AgiBot World terms on Hugging Face; pull the OXE per-dataset licence table and the DROID licence and flag the commercially reusable subsets. Create an ACCESS ID (used by both ACCESS and NAIRR). HMS supervisor agrees to be PI/co-PI on ACCESS and NAIRR and names the lab AWS account. Check the Google research-credits form (postdoc self-application? faculty PI?) and ask HMS IT / HUIT about GCP billing governance. Prof. Grüninger's RAC decision needed by ~9 Oct | 1, 4, 5, 6, 7, 3b |
| by 15 Oct 2026 | Submit **ACCESS Explore** (one-paragraph abstract, CV, Delta/DeltaAI GPU + Bridges-2 or Anvil CPU). Read the NVIDIA Academic Grant page for windows/themes/postdoc wording. Confirm HMS outside-activity/COI reporting for AXIOMALITY | 4, 10, 2 |
| 17 Oct 2026 | CPRA deadline — all registrations done so the proposal can say the corpora are in hand | — |
| by 20 Oct 2026 | Draft the RAC RRG technical justification and 1-page research description in Alliance format for Prof. Grüninger (text in applications.md §F) | 3b |
| by 24 Oct 2026 | Submit **Google Cloud Research Credits** (200–300-word O2 abstract, GCS + Cloud Batch estimate) after informing the HMS supervisor | 5 |
| by 31 Oct 2026 | Read Isaac Sim / Isaac Lab requirements and licence terms. Write the 1-page AWS Cloud Credit for Research description with the 12-month budget. Decide with the CTO which part of the audit engine is released under Apache-2.0 for LeRobot | 8, 6, 9 |
| [3 Nov 2026 — confirm] | Prof. Grüninger submits the **RAC 2027 RRG** request (fast-track renewals ~2 weeks earlier do not apply to a first request) | 3b |
| by 15 Nov 2026 | Submit **AWS Cloud Credit for Research** from the Harvard affiliation (or re-apply under U of T in April 2027) | 6 |
| by 30 Nov 2026 | Submit the **NAIRR Pilot** request (1–2 pages) with HMS as PI/co-PI. If Explore pilot runs show sustained GPU need, submit **ACCESS Accelerate** (3-page proposal, preliminary results) | 7, 4 |
| by 15 Dec 2026 | Check each source-dataset licence before re-hosting any frames; release reports and mappings only where redistribution is barred | 1, 9 |
| by 31 Dec 2026 | Install Isaac Lab on an RTX machine (HMS lab workstation with consent, or a cloud GPU) and reproduce one articulated-object task | 8 |
| by 15 Jan 2027 | **LeRobot validator + audit report on 2–3 public datasets public on the Hub** (citable in DSI and Vector applications). Identify a GPU-oriented U of T Robotics Institute / Vector co-sponsor for the NVIDIA Academic Grant | 9, 10 |
| Feb 2027 | Draft the 1–2-page NVIDIA Academic Grant compute plan (applications.md §G) | 10 |
| by 1 Mar 2027 | Mirror audit data, instance store and code to Alliance storage (RAS default now; RAC storage from 1 Apr 2027) before O2 access ends | 2, 3 |
| before leaving Harvard | File the ACCESS PI change to the HMS supervisor (or final report); NAIRR continues only if the PI stays at Harvard | 4, 7 |
| 1 Apr 2027 onward | RAC allocation active [if awarded]; sustained O3 training on Killarney/Trillium-GPU. Re-apply for Google research credits as a new O3 project from utoronto.ca under Prof. Grüninger; AWS Cloud Credit under U of T if the Harvard round was declined. Submit the NVIDIA Academic Grant in the first open Physical AI / Simulation window after the appointment starts. Ask about a lab RTX workstation so the simulator moves with the postdoc | 3b, 5, 6, 10, 8 |
| June 2027 [unconfirmed] | Register a Toronto or Boston team for the LeRobot Worldwide Hackathon once dates are announced | 9 |

**Company track (AXIOMALITY; CTO with Dr. Ru)**

| When | Step | Row |
|---|---|---|
| by 2–10 Oct 2026 | Confirm legal entity name, country/province of incorporation, incorporation date, EIN / CRA business number, whether it is Uing Technologies, and whether that entity ever received AWS Activate or Google Cloud startup credits (email 3) | 11, 12, 13 |
| by 9–15 Oct 2026 | Read the current Inception eligibility text and partner-credit list; read the Google for Startups FAQ for tier amounts, the recognized-investor definition and whether Start blocks a later upgrade | 11, 12 |
| 16–31 Oct 2026 | Submit **NVIDIA Inception** (after the CPRA crunch; the two registry records give 16 Oct and 31 Oct as targets). Stand up the company website, company-domain email and a company AWS Organizations account — never the Harvard account. If the upgrade path is confirmed, apply for the Google **Start** tier to cover Q4 2026 Engine internal testing | 11, 13, 12 |
| after Inception acceptance | Apply through the Inception portal for each partner cloud-credit offer (AWS Activate / Azure / OCI / GCP) separately | 11 |
| by 15 Nov 2026 | Request **AWS Activate Founders** (~30 minutes) and check for any stackable generative-AI credit offer | 13 |
| by 31 Jan 2027 | Choose an Activate Provider / Google-recognized accelerator route (CDL-Toronto, UTEST, MaRS, Techstars, Y Combinator, Robotics Factory Accelerate) and apply | 13, 12 |
| Q1 2027 | AXIOMALITY counsel's written position on which datasets may appear in commercial Passport evidence packs (only OXE CC BY subsets and DROID without separate agreements); seek data agreements with AgiBot and Stanford (PartNet) if commercial use is needed. CTO sizes the Q1 2027 compute budget (SMT/Datalog checks on 10,000 episodes; hosting of 100k asset packages) so credit requests are quantified. Decide which O2-audited subset, if any, could be released under CC-BY/Apache and raise it with NVIDIA's Isaac/robotics team via the Inception partner manager | 1, 13, 11 |
| 1 May 2027 | Calendar check of the AWS Generative AI Accelerator 2027 window; deck and 3-minute demo ready ("evidence layer for physical-AI training data") | 13 |
| by 30 Jun 2027 | Request **Activate Portfolio** with the Provider org ID; target Google **Scale / AI-first** immediately after the financing round or accelerator admission | 13, 12 |

## Compute and storage requirement estimate

Derived from profile/research_program.md (objectives O1–O3, the two timeline templates, "results across five datasets", "experiments in SAPIEN [+ second simulator], ablations by axiom family") and the storage figures in the dataset-licences record. **The research program gives no counts; every number below rests on the bracketed assumptions and must be re-derived when the applicant replaces them.** Dataset sizes marked "registry" come from the dataset-licences record and are themselves unverified.

### 1. What O2 has to audit

| Corpus | Audit unit | Count [assumption] | Where the number comes from |
|---|---|---|---|
| PartNet | fine-grained part instances in object hierarchies | [~26.7k models / ~574k part instances — from the PartNet paper; confirm] | not in registry |
| PartNet-Mobility (SAPIEN) | articulated models / movable parts with joints | [~2.3k models / ~14k movable parts — from the SAPIEN paper; confirm] | not in registry |
| GAPartNet | generalizable actionable parts | [~1.2k objects / ~8.5k part instances — from the GAPartNet paper; confirm] | not in registry |
| PartNet-Ensembled | [unknown; assume PartNet-Mobility scale, ~2k objects; confirm — the release page and licence were not found by the registry] | not in registry |
| AgiBot World | episodes; audit unit = labelled object × labelled part per episode | [~1M episodes (Alpha); ~15 part instances per episode → ~15M] | registry: Alpha subset; Beta "far larger" |
| Open X-Embodiment | same, sparse part labels | [~1M episodes across ~60 sub-datasets; ~4 per episode → ~4M] | not in registry |
| DROID | same | [~76k episodes; ~4 per episode → ~0.3M] | not in registry |

Minimum scope (12-month plan, "five datasets"): PartNet, PartNet-Mobility, GAPartNet, AgiBot World and one of OXE/DROID ≈ [~16M] episode-derived instances plus [~0.6M] hierarchy instances. Stretch: all seven ≈ [~20M]. After de-duplication by object category × part vocabulary the number of *distinct* hierarchies to prove things about is far smaller: [assume ~50k].

### 2. SMT / prover runs (CPU)

- **Tier 1 — Datalog/SMT bulk check** of every instance against the compiled SMT subset: [0.05–0.5 s per instance on one core; assume 0.2 s]. Passes: [3 ontology versions] × [5 axiom-family conditions (4 families dropped one at a time + full)] = 15 passes. 20M × 0.2 s × 15 ≈ 60M core-seconds ≈ **17,000 core-hours ≈ 2 core-years** [range 1–4 core-years].
- **Tier 2 — Prover9 / Mace4 on residual hard cases**: [1–5 % of the ~50k distinct hierarchies → 0.5k–2.5k obligations per pass, but budget 50k to allow per-instance escalation] × [timeout 300 s, median well below] × [5 passes]. Expected **~4,000 core-hours (0.5 core-year)**; worst case with full escalation and timeouts **~60,000 core-hours (7 core-years)**. UNKNOWN/timeout is a first-class output, so the worst case is bounded by the timeout, not open-ended.
- **O1 verification** of the ontology itself (consistency, non-triviality, module relationships, representation theorems with Prover9/Mace4; COLORE methodology): [hundreds of obligations × minutes] → **< 500 core-hours**.
- Memory: Datalog materialization of the largest corpus and Mace4 counter-model search [assume 64 GB standard nodes; 2–4 jobs needing 256 GB high-memory nodes].
- **O2 CPU total: ~3 core-years planned, up to ~10 core-years worst case.** Split: [~1 core-year] on HMS O2 / ACCESS / NAIRR / cloud batch between Oct 2026 and Mar 2027 (pipeline + first audit across five datasets), the rest on Alliance systems from April 2027 (re-audits with the released ontology, the merged corpus, the seven-dataset stretch).

### 3. Storage

| Item | Size | Basis |
|---|---|---|
| Open X-Embodiment (RLDS) | ~9 TB (elsewhere ">8 TB") | registry |
| AgiBot World | Alpha [size not recorded — assume ≤10 TB; confirm on the dataset card]; Beta "tens of TB (>40 TB)" | registry |
| DROID | ~1.7 TB RLDS (raw larger) | registry |
| ShapeNet + PartNet | [~2 TB — confirm] | not in registry |
| PartNet-Mobility, GAPartNet, PartNet-Ensembled | [tens of GB each — confirm] | not in registry |
| Ontology instance store + audit outputs (metadata only, no frames copied) | [10–20 % of raw → 2–10 TB] | assumption |
| Merged ontology-aligned corpus (mappings, corrected-annotation diffs, audit reports — not re-hosted frames) | [< 1 TB] | assumption; licence-driven (see dataset_licences.md) |
| SAPIEN / Isaac Lab rollouts, checkpoints, evaluation logs (O3) | [2–5 TB scratch] | assumption |
| **Total** | **~15 TB floor (five datasets, Alpha/subsets) to ~50–70 TB (all seven incl. AgiBot Beta)** | registry: "secure ~15–50 TB" |

The RAS default (~1 TB project) cannot hold this; the RAC request must include storage [~20 TB project + ~50 TB nearline/scratch — confirm the Alliance storage categories]. Before O2 access ends (spring 2027) the instance store, outputs and code [2–10 TB] must be mirrored to Alliance storage; raw corpora can be re-downloaded in Toronto rather than transferred.

### 4. Policy-training GPU-hours in SAPIEN (O3)

Experimental matrix from the three O3 hypotheses (generalization to unseen PartNet-Mobility categories; violation rate predicts task failure; pooled ontology-aligned data transfers across vocabularies) and "ablations by axiom family":

- Conditions: {no ontology loss, ontology loss} × {constraint-guided augmentation off, on} = 4; plus 4 axiom-family ablations (drop one family) = **8 conditions**.
- Held-out category splits: [5]; seeds: [3] → 8 × 5 × 3 = **120 training runs**.
- Pooled-data transfer: {raw pooled, ontology-aligned pooled} × [3 target vocabularies] × [3 seeds] = **18 runs**.
- Cost per run: [24 GPU-hours on one A100/H100-class GPU — SAPIEN rendering + policy training of ~1M environment steps; confirm with a pilot run]. Training: 138 × 24 ≈ **3,300 GPU-hours**.
- Verification-in-the-loop evaluation (ontology-violation rate alongside task success, every run): [+25 %] → **+800 GPU-hours**.
- Second simulator [Isaac Lab, half the matrix]: **+2,000 GPU-hours**. Development, debugging, failed runs: [+30 % of training] → **+1,000 GPU-hours**.
- **O3 GPU total: ~7,000 GPU-hours ≈ 0.8 GPU-years [range 4,000–10,000 GPU-hours]**, plus [~8 CPU cores per GPU for SAPIEN physics/rendering → ~1 core-year] and [2–5 TB] scratch.
- Phasing: pilot [500–1,000 GPU-hours] on ACCESS Explore / NAIRR while at Harvard (Oct 2026 – Mar 2027) to calibrate the per-run cost and produce preliminary results for an Accelerate request; main matrix [5,000–8,000 GPU-hours] on the RAC 2027 allocation (Apr 2027 – Mar 2028) — expressed in RGU [confirm the H100 RGU conversion on the Alliance page]; an NVIDIA Academic Grant workstation or DGX Cloud credits for interactive development.

### 5. Where each workload lands

| Workload | Oct 2026 – Mar 2027 (Harvard) | Apr 2027 – Mar 2028 (Toronto) |
|---|---|---|
| Dataset download + raw storage [15 TB floor] | HMS O2 lab quota [if sufficient — confirm] or S3/GCS via AWS / Google research credits | Alliance RAS scratch → RAC storage |
| Tier-1 Datalog/SMT bulk audit [~1 core-year now] | HMS O2 CPU partitions; ACCESS Explore (Bridges-2/Anvil); Google Cloud Batch / AWS Batch | Alliance CPU (RAS opportunistic → RAC core-years) |
| Tier-2 Prover9/Mace4 + O1 verification | HMS O2; laptop/workstation for small obligations | Alliance CPU; Semantic Technologies Lab machines |
| O3 pilot [500–1,000 GPU-hours] | ACCESS Explore/Accelerate (DeltaAI); NAIRR (NSF systems, cloud credits); HMS O2 GPU partitions if permitted | — |
| O3 main matrix [5,000–8,000 GPU-hours] | — | RAC 2027 (Killarney / Trillium-GPU) [if awarded]; NVIDIA Academic Grant hardware/DGX Cloud; Vector compute [affiliation and allocation to confirm] |
| Isaac Lab second simulator | HMS lab RTX workstation with consent, or a cloud GPU | Lab RTX workstation [to ask]; NVIDIA Academic Grant |
| Public release (validator, audit reports, mappings) | Hugging Face Hub (free) | Hugging Face Hub; AWS Open Data Sponsorship [read terms] |
| AXIOMALITY Engine tests (10,000 verified episodes by Q1 2027; 100k asset packages) | Company AWS/GCP accounts via Inception partner credits, Activate Founders, Google Start — **never** academic resources | Same; Activate Portfolio / Google Scale-AI after a Provider or financing round |

## Who does what

| Who | What |
|---|---|
| Dr. Ru | All dataset registrations; O2 account request; ACCESS and NAIRR submissions (as PI if allowed, else as lead user); Google and AWS research-credit applications; RAC justification draft for Prof. Grüninger; Isaac Lab install and pilot; LeRobot validator and audit report; keeps academic and company accounts separate |
| Prof. Grüninger | Confirms CCDB account; approves the sponsored role; decides on and submits RAC 2027 RRG by [3 Nov 2026]; later serves as PI on the NVIDIA Academic Grant and on the U of T re-applications for Google/AWS research credits |
| HMS supervisor [name] | Sponsors the O2 account; written OK for the workload; PI or co-PI on ACCESS and NAIRR; acknowledges the AWS research-credit application and names the lab AWS account; consent for Isaac Lab on lab hardware; advises on HMS COI reporting |
| U of T Robotics Institute / Vector faculty [name] | Co-PI on the NVIDIA Academic Grant; possible RTX workstation and Vector compute |
| AXIOMALITY CTO [name] | Entity facts; website and domain email; company AWS/GCP accounts; Inception, Activate and Google for Startups submissions; Q1 2027 compute budget; decides the Apache-2.0 validator boundary |
| AXIOMALITY counsel | Written position on commercial use of each dataset before Q1 2027 partner pilots |

## Facts the applicant must supply (every [bracket] in this package)

Applicant and appointment
- [HMS laboratory / department; start month/year; whether the appointment is Quad-based or hospital-based] — decides O2 vs a hospital cluster and NAIRR/ACCESS PI arrangements
- [HMS supervisor's name] and their agreement to sponsor O2, be PI/co-PI on ACCESS and NAIRR, and hold the AWS research credits
- [Citizenship / immigration status] — irrelevant to eligibility for every row, but decisive for DOE resources under NAIRR and export-controlled ACCESS resources; choose NSF/cloud resources if not a US person
- [ORCID]; [thesis title]; [PhD supervisor name] — for CVs attached to ACCESS/NAIRR/RAC
- [Pronouns] — application texts use first person and "Dr. Ru" to avoid assuming any

Canadian sponsor
- [Whether Prof. Grüninger has an active CCDB account and any current RRG/fast-track allocation; his CCRI; his CCV current in CCDB]
- [His decision to submit RAC 2027 RRG by ~9 Oct 2026; his agreement to sponsor a CCDB role now]
- [RAC 2027 open/close dates (reported 23 Sep – 3 Nov 2026); whether Killarney/PAICE is inside the RRG form; the correct URL slug; the H100 RGU conversion; Alliance storage categories]
- [Name of a GPU-oriented U of T Robotics Institute / Vector co-PI]; [whether a lab RTX workstation is available from April 2027]; [Vector affiliation and compute allocation]

Program pages to re-read (all "unverifiable" in the registry)
- ACCESS: [current caps; postdoc-as-PI wording; GPU exchange rates; Explore decision time]
- NAIRR: [requests still open; postdoc-as-PI; cadence; US-persons-only resources; continuation under NSF 25-546]
- Google Cloud Research Credits: [postdoc self-application vs faculty PI; eligible-institution list; maximum amount and expiry; HUIT/HMS billing-account rule]
- AWS Cloud Credit for Research: [still open in recalled form; form fields; cadence; postdoc vs PI; expiry; HMS research-computing sign-off]
- NVIDIA Academic Grant: [rolling vs windowed; open themes and close dates; postdoc wording; hardware vs credits]
- Isaac Sim/Lab: [current system requirements; Jetson education-discount eligibility for postdocs; free Omniverse components]
- LeRobot: [dataset format version; CONTRIBUTING.md; licence; 2027 hackathon dates]
- Alliance RAS: [default quotas; external-collaborator rule for a US-based researcher; Killarney in RAS]
- HMS O2: [account-request route; GPU partition names; storage quota and charges]

Datasets (see dataset_licences.md)
- [Current terms text of ShapeNet, PartNet, SAPIEN, GAPartNet, AgiBot World (incl. Beta), each OXE sub-dataset, DROID]; [whether derived annotations may be published]; [whether registration binds to the institution]; [PartNet-Ensembled release page and licence]; [exact instance/episode counts and download sizes used in the estimate]

Company
- [Legal entity name; country and province/state of incorporation; incorporation date; EIN / CRA business number; employee count; revenue to date; whether it is Uing Technologies; founder residency; cap table]
- [Live company website and company-domain email]; [company AWS account ID; GCP billing account]
- [Whether Uing Technologies ever received AWS Activate or Google Cloud startup credits]
- [CTO's name]; [counsel]; [Activate Provider / Google-recognized accelerator chosen]; [Q1 2027 compute budget in instance-hours and TB-months]
- [Which components of the audit engine may be released under Apache-2.0]; [which O2-audited subset, if any, may be released under CC-BY/Apache]

Estimate assumptions to replace
- [Per-dataset instance and episode counts; per-instance SMT time; residual fraction; prover timeout; number of ontology versions and axiom families; number of category splits, seeds and target vocabularies; GPU-hours per training run; second-simulator share; storage sizes not in the registry]
