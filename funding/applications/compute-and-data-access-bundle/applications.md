# Applications — ready-to-paste texts for every program in the compute and data access bundle

Drafted 2026-09-25 for Dr. Yi Ru. Each section gives the text for one program's form or proposal, sized to the length the registry records for that program (stated in the section header). Facts come only from `profile/*.md` and the registry records; every unconfirmed item is in [brackets]. Resource numbers come from the estimate in README.md §"Compute and storage requirement estimate" and inherit its bracketed assumptions — re-derive them if those change. Section letters match the references in README.md (§F = Alliance RAC, §G = NVIDIA Academic Grant).

Voice: first person "I" where Dr. Ru applies; "the PI" / "Dr. Ru" where Prof. Grüninger or the HMS supervisor submits. No pronouns are used for Dr. Ru anywhere [pronouns unknown].

## 0. Shared blocks (reuse, do not paste twice into one form)

### 0.1 Project summary (≈150 words)

Robot-learning datasets — PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment and DROID — annotate objects as hierarchies of parts with kinematic, functional and visual labels. Each dataset defines "part" operationally; no dataset or learned model is required to satisfy the axioms of parthood; there is no principled way to map labels across datasets; pooled training silently mixes incompatible part vocabularies. The consequences (poor transfer across part vocabularies, brittle generalization to new object categories) are observed but have never been measured, because there has been no formal specification to measure against. This project supplies the specification and the measurement: (O1) a verified first-order ontology of physical object parts extending TUpper (ISO/IEC 21838-4) with the Process Specification Language; (O2) a two-tier audit pipeline (Datalog/SMT bulk checks, first-order theorem proving for residual cases) that produces the first quantitative measurement of parthood consistency in robot datasets, corrected annotations and provably meaning-preserving cross-dataset label mappings; (O3) training methods that use the ontology as an inductive bias for part-aware manipulation policies, evaluated in SAPIEN [and Isaac Lab].

### 0.2 Technical justification (≈250 words)

**Why the audit needs CPU at scale.** Every annotated part instance in every corpus is translated into ontology instances and checked. Tier 1 compiles an SMT/Datalog subset of the ontology and checks every instance in bulk; Tier 2 sends the residual hard cases to Prover9 (proof obligations) and Mace4 (counter-models), with UNKNOWN/timeout as a first-class output so the worst case is bounded by the timeout. The audit is repeated across [3] ontology versions and [5] axiom-family conditions so that the violation statistics can be attributed to individual axiom families. The workload is embarrassingly parallel (one instance or one obligation per task), needs standard-memory nodes for most tasks and a few high-memory nodes for Datalog materialization of the largest corpus and for Mace4 counter-model search.

**Why the policy experiments need GPU.** O3 tests three hypotheses — ontology-consistent training improves generalization to unseen PartNet-Mobility categories; ontology-violation rate predicts task failure; pooled ontology-aligned data transfers across part vocabularies — with ablations by axiom family. The matrix is {no ontology loss, ontology loss} × {constraint-guided augmentation off, on} plus four single-family ablations (8 conditions) × [5] held-out category splits × [3] seeds, plus a pooled-data transfer block; every run is evaluated with verification-in-the-loop (violation rate alongside task success). SAPIEN physics and rendering run on CPU alongside each GPU.

**Why the storage is large.** The raw corpora are large (Open X-Embodiment ~9 TB in RLDS; DROID ~1.7 TB; AgiBot World tens of TB for the Beta release — registry figures, unverified) but only their part annotations, kinematics and episode metadata enter the ontology instance store, which is [10–20 %] of raw size. Raw frames are not copied into released artefacts.

### 0.3 Resource numbers (from README.md; all figures rest on bracketed assumptions)

| Quantity | Oct 2026 – Mar 2027 (Harvard period) | Apr 2027 – Mar 2028 (Toronto period) |
|---|---|---|
| CPU for the O2 audit and O1 verification | [~9,000 core-hours ≈ 1 core-year] | [~2.4 core-years planned (17,000 Tier-1 + 4,000 Tier-2 core-hours); up to ~9 worst case (Tier-2 at 62,500)] |
| GPU for O3 | pilot [500–1,000 GPU-hours, A100/H100-class] | main matrix [5,000–8,000 GPU-hours] + [~4.6–7.3 core-years] CPU for simulation (8 cores per GPU) |
| Memory | 64 GB standard; [2–4] jobs at 256 GB | same |
| Storage | [15–20 TB] raw + [2–10 TB] instance store/outputs | [20 TB] project + [50 TB] nearline/scratch (all seven corpora incl. AgiBot Beta); [2–5 TB] O3 scratch |
| Software | Prover9/Mace4, an SMT solver [Z3 — confirm], a Datalog engine [Soufflé — confirm], Python, SAPIEN, Isaac Lab, PyTorch, LeRobot/RLDS readers | same |

Non-duplication across the Harvard-period requests (state this in each "other support" field): HMS O2 carries pipeline development and the first Tier-1 passes [~4,000 core-hours]; ACCESS Explore carries the remaining CPU [~5,000 core-hours] and a first GPU pilot [~300 GPU-hours]; NAIRR carries the GPU pilot proper [500–700 GPU-hours] and project storage; Google Cloud research credits carry object storage for the GCS-hosted corpora (OXE, DROID) and batch ingest; AWS research credits carry S3 hosting for the released outputs and batch SMT checking. If every request is granted the overlap is roughly a third, which is deliberate because none of the programs could be verified as open.

### 0.4 Expected outcomes (≈120 words)

(1) A verified parts ontology released under an open licence and contributed to COLORE and ISO/IEC JTC 1/SC 32. (2) The first quantitative audit of parthood consistency in robot datasets — violation rates by dataset, object category and axiom family, with counter-models for representative failures — released publicly, first as a LeRobot-compatible validator plus an audit report on 2–3 public datasets [by 15 Jan 2027], then across five datasets [M4–8 of the 12-month plan]. (3) Provably meaning-preserving label mappings between the part vocabularies of the audited datasets, and corrected-annotation diffs where dataset terms allow. (4) An audit toolkit reusable for medical-image part labels, CAD assemblies and BIM. (5) Policy-training results in SAPIEN [and Isaac Lab] reporting ontology-violation rate alongside task success; two ML-venue papers and one robotics-venue paper (24-month plan).

### 0.5 Data-management statement (≈200 words)

All datasets are obtained under their own terms by Dr. Ru as an individual academic researcher with an institutional email (harvard.edu now; utoronto.ca from the U of T appointment). ShapeNet, PartNet, PartNet-Mobility/SAPIEN, GAPartNet and AgiBot World are non-commercial licences [terms to be re-read at registration]; Open X-Embodiment sub-datasets are mostly CC BY 4.0 / Apache-2.0 and DROID is CC BY 4.0 (data) and MIT (code) [registry, unverified]. Raw data are stored only on the allocated institutional or research-cloud systems, never on company systems, and are deleted or mirrored to the successor academic allocation when an allocation ends. The ontology instance store holds annotations, kinematics and episode metadata only — no frames. Public releases consist of the ontology, audit reports, label mappings, corrected-annotation diffs [where the dataset terms permit derived annotations] and the validator code (Apache-2.0); any re-hosted merged corpus is limited to subsets whose licence permits redistribution (CC BY / Apache sub-datasets of Open X-Embodiment, DROID) and carries each source's attribution. No personal data are processed [confirm for DROID/AgiBot World teleoperation footage: operators may be visible; the audit does not use frames]. The applicant's company, AXIOMALITY, does not use any resource requested here; company workloads run on separately funded company accounts.

---

## A. HMS O2 cluster — account request and sponsoring-PI approval (registry 24dcc2eb2b71)

*Route: HMS Research Computing account-request form with the sponsoring PI's approval [confirm current form on the O2 wiki]; if the appointment is hospital-based, the same text serves for the hospital cluster [e.g. MGB ERIS — confirm]. Length: form fields; keep each under ~150 words.*

**Sponsoring PI:** [HMS supervisor name], [department/laboratory], Harvard Medical School.
**User:** Yi Ru, Postdoctoral Researcher, [laboratory], since [month year]; harvard.edu email [address].

**Intended use (paste into "research description / justification"):**
Formal verification and data-quality auditing of hierarchical part annotations. The workload is CPU-bound batch computing: Datalog/SMT bulk checks of annotation hierarchies against a first-order ontology, and Prover9/Mace4 theorem-proving jobs for residual cases, run as array jobs of independent short tasks. Datasets are public research datasets (PartNet, PartNet-Mobility, GAPartNet, Open X-Embodiment, DROID, AgiBot World) obtained under their academic terms; the same audit toolkit applies to part labels in medical imaging, which is its relevance to the laboratory [adjust to the supervisor's wording]. Estimated need over Oct 2026 – Mar 2027: [~4,000 core-hours] on standard CPU partitions, [2–4] high-memory jobs (256 GB), and [15–20 TB] of scratch or lab storage for raw corpora [confirm the base quota and per-TB charges before requesting; raw corpora can instead live on cloud storage if the quota is small]. No GPU is required for this workload [request the GPU partition only if the supervisor agrees to the O3 pilot; ~300 GPU-hours]. No human-subjects or PHI data are involved.

**Supervisor's written agreement (for the supervisor to send to HMS RC or to keep on file):**
I sponsor an O2 account for Dr. Yi Ru, a postdoctoral researcher in my laboratory. Dr. Ru's project — a formal audit of part annotations in public robotics datasets using an ontology and automated theorem proving — is an academic research activity conducted under my supervision; its toolkit is intended to generalize to hierarchical labels in [medical imaging / the laboratory's domain]. I agree that the workload described in the request may run under the laboratory's allocation, and I confirm that no commercial work will be performed on O2. — [Name, title, date]

---

## B. Digital Research Alliance of Canada — Rapid Access Service via a sponsored CCDB role (registry 6c92ea507e9e)

*Route: ccdb.alliancecan.ca registration; sponsor approves in CCDB. Length: form fields.*

**Position type:** [external collaborator until the U of T appointment starts; then postdoctoral fellow — confirm CCDB offers both].
**Sponsor:** Prof. Michael Grüninger, Department of Mechanical and Industrial Engineering, University of Toronto; CCRI [Prof. Grüninger to supply].
**Institution / email:** [University of Toronto, MIE — with yi.ru@alumni.utoronto.ca now; switch to the utoronto.ca staff address on appointment — confirm CCDB accepts the alumni address].

**Role description (paste into "research description"):**
Verified mereological ontologies for object–part representation in physical AI — a joint project with Prof. Grüninger's Semantic Technologies Laboratory extending TUpper (ISO/IEC 21838-4) and PSL to physical object parts, auditing public robot-learning datasets against the ontology with Datalog/SMT and Prover9/Mace4, and testing the ontology as an inductive bias for manipulation policies in SAPIEN. Under the default allocation I will prototype the audit pipeline on CPU nodes, run small policy ablations on opportunistic GPU queues, and hold the ontology instance store [2–10 TB — confirm default project/scratch quotas] so that the audit data survive the end of my Harvard allocation in spring 2027. Usage under RAS will be logged to support the group's RAC 2028 renewal.

---

## C. NSF ACCESS — Explore (now) and Accelerate (if pilots show sustained need) (registry 5dca99a0213e)

*Route: allocations.access-ci.org with an ACCESS ID. PI: Dr. Ru [postdoc-as-PI rule — confirm on project-types page] with the HMS supervisor as co-PI so the allocation survives the spring-2027 move; if the rule has changed, swap the roles. Research use only.*

### C.1 Explore ACCESS — abstract (one paragraph; ≈240 words) and resource selection

**Title:** Formal audit of part annotations in robot-learning datasets and pilot ontology-constrained policy training

**Abstract:**
Robot-learning datasets (PartNet, PartNet-Mobility, GAPartNet, Open X-Embodiment, DROID, AgiBot World) annotate objects as part hierarchies, but no dataset is required to satisfy the axioms of parthood and there is no principled mapping between their part vocabularies; the resulting transfer and generalization failures have never been measured because there has been no specification to measure against. This project (a) verifies a modular first-order ontology of physical object parts extending TUpper (ISO/IEC 21838-4) with the Process Specification Language, using Prover9/Mace4 under the COLORE methodology; (b) audits the datasets against it with a two-tier pipeline — Datalog/SMT bulk checking of every part instance, first-order theorem proving for residual cases — producing the first quantitative measurement of parthood consistency in robot data, corrected annotations and provably meaning-preserving cross-dataset label mappings; and (c) pilots ontology-constrained training of part-aware manipulation policies in SAPIEN, reporting ontology-violation rate alongside task success. The audit is an embarrassingly parallel CPU workload ([~5,000 core-hours] on Bridges-2 or Anvil regular-memory nodes, with [2–4] extreme-memory jobs for Datalog materialization); the pilot needs [~300 GPU-hours] on DeltaAI to calibrate per-run cost for an Accelerate request. Storage: [10 TB] project scratch for annotation shards (no frames). Outputs — the ontology, audit reports, mappings and a LeRobot-compatible validator — will be released publicly. PI: Yi Ru (postdoctoral researcher, Harvard Medical School; core contributor to ISO/IEC 21838-4); co-PI: [HMS supervisor].

**Resource selection:** Bridges-2 Regular Memory (RM) [~5,000 core-hours] + Bridges-2 Extreme Memory [2–4 jobs] or Anvil CPU; DeltaAI GPU [~300 GPU-hours]; Bridges-2 or Delta project storage [10 TB]. Credits: [convert with the ACCESS exchange calculator; if the GPU line pushes the total over the Explore cap of 400,000 credits [confirm], drop the GPU line to the NAIRR request].
**Supporting grant:** none required for Explore; list "pending: NSERC CPRA (submitted 17 Oct 2026)" [if submitted].
**CV:** Dr. Ru's CV [PDF]; co-PI CV [PDF].

### C.2 Accelerate ACCESS — proposal (3 pages; ≈1,000 words below plus tables; submit only with pilot results, target 30 Nov 2026)

**1. Research objectives.** [Paste 0.1 Project summary.] The Accelerate request covers the O3 experimental matrix in full and the re-audit of all seven corpora with the released ontology (O2), which the Explore allocation and pilot runs have shown to require sustained GPU time beyond the Explore cap.

**2. Computational methods and software.** [Paste 0.2 Technical justification.] Software stack: Prover9/Mace4; [Z3] via Python bindings; [Soufflé] Datalog; SAPIEN with PartNet-Mobility assets; Isaac Lab [second simulator]; PyTorch; LeRobot and RLDS readers. All components are open source and already run on the Explore allocation.

**3. Preliminary results (from the Explore allocation).** [Insert after the pilot: Tier-1 throughput per core-hour and per instance; residual fraction sent to Tier 2; median and timeout rates for Prover9/Mace4; GPU-hours per SAPIEN training run measured over [n] runs; first violation statistics on [datasets]. These replace the assumptions in §4.]

**4. Justification of the resource request.**

| Component | Basis | Request |
|---|---|---|
| O3 training runs | 8 conditions × [5] held-out category splits × [3] seeds = 120 runs + 18 pooled-transfer runs; [24] GPU-hours per run measured in the pilot | [3,300] GPU-hours DeltaAI |
| Verification-in-the-loop evaluation | [+25 %] of training | [800] GPU-hours |
| Second simulator (Isaac Lab, half matrix) | | [2,000] GPU-hours |
| Development, failed runs | [+30 % of training] | [1,000] GPU-hours |
| SAPIEN physics/rendering CPU | [8 cores per GPU] × [7,100] GPU-hours | [~57,000 core-hours ≈ 6.5 core-years] Bridges-2/Anvil |
| Re-audit, seven corpora, [3] ontology versions × [5] axiom conditions | Tier-1 [0.2 s/instance] × [20M] instances × 15 passes; Tier-2 [50k] obligations × [300 s] timeout × 15 | [17,000] + [4,000] core-hours (Tier-2 worst case [62,500]) |
| Storage | annotation shards for seven corpora, instance store, checkpoints | [30 TB] project + [5 TB] scratch |

Total: [~7,000] GPU-hours and [~9] core-years (21,000 audit + ~57,000 simulation core-hours) → [credits per the exchange calculator; must be ≤ 3,000,000 for Accelerate — confirm cap]. Note that the Toronto share of this work (from April 2027) is requested in parallel from the Digital Research Alliance of Canada RAC 2027; if that allocation is awarded, the ACCESS allocation will be closed early or transferred to the co-PI, and any unused credits returned.

**5. Data management.** [Paste 0.5.]

**6. Team and continuity.** PI Yi Ru (HMS postdoctoral researcher; PhD U of T 2025; ISO/IEC 21838-4 core contributor; two journal papers on parthood-preserving mappings under review at Synthese with M. Grüninger). Co-PI [HMS supervisor]. Collaborator Prof. Michael Grüninger (U of T, Semantic Technologies Laboratory; COLORE, PSL, TUpper). Dr. Ru moves to U of T in [April 2027 or later]; the co-PI will hold the allocation from that date and Dr. Ru will continue as a user [confirm ACCESS allows non-US users on a US-held allocation].

---

## D. Google Cloud Research Credits (registry c4f8773a6f7f)

*Route: cloud.google.com/edu/researchers online form. Applicant: Dr. Ru with harvard.edu [postdoc self-application vs faculty PI — confirm; if a PI is required, name the HMS supervisor]. Length: 200–500-word abstract; the text below is ≈280 words. Inform the supervisor first; check HUIT/HMS billing-account rules.*

**Project title:** Auditing part annotations in public robot-learning datasets against a verified ontology

**Abstract (≈280 words):**
Robot manipulation policies are trained on datasets that annotate objects as hierarchies of parts — PartNet, PartNet-Mobility, GAPartNet, Open X-Embodiment, DROID and AgiBot World — yet no dataset requires its annotations to satisfy the axioms of parthood, and no principled mapping exists between their part vocabularies. Models trained on pooled data therefore mix incompatible vocabularies, and the resulting transfer and generalization failures have never been measured because there has been no formal specification to measure against. I am building that specification — a verified first-order ontology of physical object parts extending ISO/IEC 21838-4 (TUpper), which I helped author — and an audit pipeline that translates every annotated part instance into ontology instances and checks them: a Datalog/SMT tier for bulk checking and an automated-theorem-proving tier (Prover9/Mace4) for residual cases. The output is the first quantitative measurement of parthood consistency in robot data, corrected annotations, and provably meaning-preserving label mappings across datasets, released publicly with a LeRobot-compatible validator.

Google Cloud is the natural home for the audit because two of the largest corpora (Open X-Embodiment, ~9 TB in RLDS; DROID, ~1.7 TB) are distributed from Google Cloud Storage, so annotation shards can be extracted in-region without egress. Planned use over 12 months: Cloud Storage for annotation shards and the ontology instance store [15 TB average]; Cloud Batch on standard machine types for the embarrassingly parallel SMT/Datalog checks [~3,000 vCPU-hours]; [2–4] high-memory VM jobs for Datalog materialization; BigQuery [optional] for violation statistics. No GPU is requested. All data are public research datasets used under their academic terms; no frames are re-hosted, and all released artefacts are metadata, reports and code. Requested credits: [sized to the estimate above at list prices — enter the figure the form asks for; do not exceed the program's stated maximum, confirm on the program page].

**Institution / role:** Harvard Medical School, Postdoctoral Researcher [lab]; institutional email [address]; billing account [personal-research or lab-managed GCP billing account — per HUIT/HMS guidance].
**Re-application from U of T (April 2027 or later):** same abstract with O3 replaced in the second paragraph: "Vertex AI / GPU VMs for [N] SAPIEN policy-training runs [~1,000 GPU-hours]" — under Prof. Grüninger, utoronto.ca email; a separate project, as awards are per project [confirm].

---

## E. AWS Cloud Credit for Research (registry e54329a0465e)

*Route: online proposal form [confirm the program is still accepting applications in its recalled form]. Applicant: Dr. Ru, harvard.edu, naming the HMS supervisor's lab AWS account [account ID]; re-apply under U of T MIE (Prof. Grüninger's account) in April 2027 if declined. Length: one-page project description (≈450 words) plus a 12-month budget by service. Must build cloud-based tools, workflows or publicly shared datasets — the framing below is the open audit toolkit and the public release.*

**Project title:** An open, cloud-hosted audit toolkit and public release of ontology-aligned part annotations for robot-learning datasets

**Project description (≈450 words):**
*Problem.* Robot-learning datasets (PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment, DROID) annotate objects as part hierarchies with kinematic, functional and visual labels. Each defines "part" operationally; none is required to satisfy the axioms of parthood; there is no principled mapping between their vocabularies; pooled training silently mixes incompatible vocabularies. The transfer and generalization failures this causes are observed but unmeasured, because there has been no formal specification to measure against.

*What will be built on AWS.* (1) A cloud-native audit workflow: annotation hierarchies from each dataset are converted by open adapters (LeRobot, RLDS) into ontology instances stored as partitioned Parquet on S3; AWS Batch runs the two-tier check — a compiled SMT/Datalog subset of the ontology for bulk checking of every instance, and Prover9/Mace4 theorem-proving tasks for residual hard cases, with UNKNOWN/timeout recorded as a first-class result. (2) A public release on S3 [and, once released, the AWS Open Data Sponsorship Program — read terms]: the verified ontology (open licence), per-dataset audit reports with violation rates by category and axiom family, provably meaning-preserving cross-dataset label mappings, corrected-annotation diffs where the dataset terms permit, and the validator code under Apache-2.0. (3) A reproducible container image of the toolkit so other groups can audit their own datasets — the same toolkit applies to hierarchical labels in medical imaging, CAD assemblies and BIM.

*Why AWS.* The audit is an embarrassingly parallel batch workload with a large, cold object-storage footprint and a small hot working set — a fit for S3 storage classes plus Batch on Spot instances. Hosting the released artefacts on S3 gives the robotics community a single durable location; the AWS Open Data Sponsorship Program is the intended long-term home for the released mappings and reports.

*Timeline (12 months from credit issue).* Months 1–2: adapters, S3 layout, Batch job definitions; first Tier-1 pass on PartNet and PartNet-Mobility. Months 3–6: all five core datasets audited; Tier-2 proving; first public release (validator + audit report on 2–3 datasets, target 15 Jan 2027). Months 7–12: re-audit with the released ontology version, label mappings and corrected-annotation diffs released; container image and documentation; Open Data Sponsorship application.

*Sharing plan.* Code on GitHub (Apache-2.0); reports and mappings on S3 and the Hugging Face Hub; ontology contributed to COLORE and ISO/IEC JTC 1/SC 32; audit/data paper at a robotics or ML venue.

*Team.* Yi Ru, Postdoctoral Researcher, Harvard Medical School (PhD U of T 2025; core contributor to ISO/IEC 21838-4); [HMS supervisor], PI of the lab account; Prof. Michael Grüninger, U of T, collaborator on the ontology.

**12-month credit budget by service** [quantities from README.md; dollar values from the AWS Pricing Calculator at the time of submission — do not enter a total until computed]:

| Service | Quantity | Purpose |
|---|---|---|
| S3 Standard → Standard-IA | [15–20 TB] average over 12 months | annotation shards, instance store, released artefacts |
| AWS Batch on EC2 Spot (compute-optimized, 64 GB) | [~3,000 vCPU-hours] | Tier-1 SMT/Datalog checks |
| EC2 memory-optimized (256 GB) | [2–4 jobs × ~24 h] | Datalog materialization, Mace4 |
| EC2 GPU (optional) | [≤ 300 GPU-hours] | O3 pilot only if not covered by ACCESS/NAIRR |
| Data transfer out | [~5 TB] | public downloads of released artefacts |
| ECR, CloudWatch, misc. | [small] | container image, logs |
| **Total requested** | **[USD — compute at list price]** | |

---

## F. Digital Research Alliance of Canada — RAC 2027, RRG stream (registry e1dfb65e5146) — draft for Prof. Grüninger to submit

*Route: Alliance application portal, submitted by the PI (Prof. Grüninger) by 3 Nov 2026 (RAC 2027 window 23 Sep – 3 Nov 2026 — confirmed by web search 2026-09-25 against an arc.ubc.ca announcement and the alliancecan.ca RRG page; re-check on the official page). Postdocs cannot be PI. Allocation period 1 Apr 2027 – 31 Mar 2028. Length: research description ≈1 page (≈500 words below); resource justification per the form's sections. Keep the first-year ask modest: first-year GPU requests without RAC history are routinely scaled back.*

**Project title:** Verified mereological ontologies for object–part representation in physical AI

**Research description (≈500 words):**
The Semantic Technologies Laboratory develops and verifies first-order ontologies (the COLORE repository, the Process Specification Language, TUpper / ISO/IEC 21838-4) and uses them as specifications for engineering and AI systems. This project, led in the group by Dr. Yi Ru (incoming postdoctoral fellow, [April 2027 or later]; PhD MIE 2025; core contributor to ISO/IEC 21838-4; two journal papers with the PI under review at Synthese on material constitution as a parthood-preserving mapping between mereologies and on mereological pluralism), carries that methodology into robot learning.

Robot-learning datasets (PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment, DROID) annotate objects as hierarchies of parts. Each defines "part" operationally; none is required to satisfy the axioms of parthood; there is no principled way to map labels across datasets; pooled training mixes incompatible part vocabularies. The consequences — poor transfer across vocabularies, brittle generalization to new categories — have never been measured because there has been no formal specification to measure against.

Three objectives. **O1 — Ontology as specification.** Axiomatize and verify a modular first-order ontology of physical object parts (rigid, articulated, functional, assembly) extending TUpper and integrated with PSL for state change under manipulation; verification of consistency, non-triviality, module relationships and representation theorems with Prover9/Mace4 under the COLORE methodology. **O2 — Ontology as audit.** A two-tier pipeline (Datalog/SMT for bulk checks; first-order theorem proving for residual cases) translates annotation hierarchies into ontology instances and checks them, yielding the first quantitative measurement of parthood consistency in robot datasets, corrected annotations, provably meaning-preserving cross-dataset label mappings, a merged ontology-aligned corpus [to the extent dataset terms permit] and a reusable audit toolkit. **O3 — Ontology as inductive bias.** Differentiable relaxations of parthood constraints as auxiliary losses, constraint-guided data augmentation for underrepresented categories, and verification-in-the-loop evaluation reporting ontology-violation rate alongside task success; experiments in SAPIEN [and Isaac Lab] with ablations by axiom family, testing whether ontology-consistent training improves generalization to unseen PartNet-Mobility categories, whether violation rate predicts task failure, and whether pooled ontology-aligned data transfers across part vocabularies.

During the allocation year (1 Apr 2027 – 31 Mar 2028) the project runs the re-audit of all corpora with the released ontology (O2) and the full O3 experimental matrix; O1 and the first audit are completed before April 2027 on the applicant's current allocations at Harvard, whose results (audit report on 2–3 public datasets, [15 Jan 2027]) will be cited in the application [insert once available]. The GPU work is new for the group; the CPU work continues the group's established theorem-proving workflow.

Outcomes: an open-licence verified ontology contributed to COLORE and ISO/IEC JTC 1/SC 32; public audit reports and mappings; two ML-venue papers and one robotics-venue paper; a toolkit reusable for CAD assemblies, BIM and medical-image part labels. HQP: Dr. Yi Ru (PDF); [graduate students in the lab working on COLORE/PSL — PI to list].

**Resource justification (form sections):**

| Resource | Request (allocation year) | Justification |
|---|---|---|
| GPU (RGU) on an H100-class system [Killarney or Trillium-GPU — confirm whether AI compute is inside the RRG form] | [5,000–8,000] GPU-hours ≈ [0.6–0.9] GPU-years → [convert to RGU with the Alliance H100 factor] | 120 O3 training runs (8 conditions × [5] splits × [3] seeds) + 18 pooled-transfer runs at [24] GPU-hours each, plus verification-in-the-loop evaluation [+25 %], Isaac Lab half-matrix [+2,000 GPU-hours] and development [+30 %]. Per-run cost is calibrated by pilot runs at Harvard in [Oct 2026 – Mar 2027]. |
| CPU core-years | [~9] core-years (Tier-1 [17,000] core-hours; Tier-2 Prover9/Mace4 [4,000] core-hours, worst case [62,500]; SAPIEN physics/rendering [~56,000] core-hours ≈ 6.4 core-years at 8 cores per GPU) — still far below the RAC floor of 200 core-years; see the RAC package's go/no-go gate | Embarrassingly parallel array jobs; [3] ontology versions × [5] axiom-family conditions over [~20M] annotated part instances; Prover9/Mace4 obligations with a [300 s] timeout. |
| Large-memory nodes | [2–4] jobs at 256 GB | Datalog materialization of the largest corpus; Mace4 counter-model search. |
| Project storage | [20 TB] | Annotation shards and ontology instance store for seven corpora (no frames); audit outputs; mappings. |
| Nearline / scratch storage | [50 TB] | Raw corpora during extraction (OXE ~9 TB; AgiBot World Beta tens of TB; DROID ~1.7 TB — registry figures) and O3 rollouts/checkpoints [2–5 TB]. [Confirm Alliance storage categories and default quotas.] |
| Cloud | none | |
| Software | Prover9/Mace4, [Z3], [Soufflé], Python, PyTorch, SAPIEN, Isaac Lab, LeRobot/RLDS | All open source; SAPIEN and Isaac Lab need RTX/CUDA-capable GPUs — confirm on the target system. |

**Past usage:** [PI to complete: current RAS/RAC usage of the group; if none, state that RAS usage from Oct 2026 will be reported]. **Fast-track:** not applicable to a first request.

---

## G. NVIDIA Academic Grant Program — Simulation & Digital Twins / Physical AI track (registry 6982d408a17b) — draft for the faculty PI

*Route: online form. PI: Prof. Grüninger from April 2027, ideally with a GPU-oriented U of T Robotics Institute / Vector co-PI [name]; optional earlier route with the HMS supervisor as PI under a currently open theme. Submit in the first open Physical AI / Simulation window after the appointment starts [windows and themes unknown — read the page]. Length: 1–2 pages; ≈600 words below.*

**Project title:** Ontology-verified articulated-object data and part-aware policy training in SAPIEN and Isaac Lab

**Project description (≈300 words):**
Simulation-based training of manipulation policies for articulated objects depends on part-level assets and annotations — PartNet-Mobility in SAPIEN, and the OpenUSD scene graphs consumed by Isaac Sim / Isaac Lab — whose part hierarchies carry no formal semantics: nothing requires the parts of an asset to form a consistent whole, and nothing relates the part vocabularies of different asset libraries or real-robot datasets. This project supplies the missing specification and uses it in three ways. First, a modular first-order ontology of physical object parts, extending the ISO/IEC 21838-4 top-level ontology (which the lead researcher co-authored) and verified with automated theorem provers, defines what a consistent part hierarchy is. Second, an audit pipeline checks every annotated part instance of PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment and DROID against the ontology — the first quantitative measurement of parthood consistency in robot data — and produces provably meaning-preserving label mappings and corrected annotations. Third, the ontology becomes an inductive bias for policy training: differentiable relaxations of parthood constraints as auxiliary losses, constraint-guided data augmentation for underrepresented categories, and verification-in-the-loop evaluation reporting ontology-violation rate alongside task success. Experiments run in SAPIEN and, as the second simulator, Isaac Lab, with ablations by axiom family, testing whether ontology-consistent training improves generalization to unseen articulated-object categories and whether violation rate predicts task failure.

**Relevance to NVIDIA's simulation and physical-AI ecosystem (≈100 words):**
The audit toolkit reads OpenUSD/USDZ scene graphs directly, so the same consistency checks apply to SimReady-style asset libraries and to Isaac Lab task assets; the ontology-violation metric is a candidate data-quality signal for synthetic-data pipelines. Isaac Sim (Apache-2.0) and Isaac Lab (BSD-3) are already the planned second simulator [registry: open-sourced 2025 — confirm current licences]. Results, mappings and the validator are released openly.

**Compute plan (≈200 words):**
Requested: [one RTX-class workstation (48 GB-class GPU) or DGX Cloud credits — choose per the theme's offer; hardware is preferred because Isaac Sim requires an RTX GPU with 16 GB+ VRAM and interactive development is continuous] plus DGX Cloud credits for the batch matrix if offered. Workload: [138] SAPIEN training runs at [24] GPU-hours each ≈ [3,300] GPU-hours, verification-in-the-loop evaluation [+800], Isaac Lab half-matrix [+2,000], development [+1,000]: [~7,000] GPU-hours over 12 months, of which the workstation carries development, Isaac Lab installation and rendering-heavy debugging [~1,500 GPU-hours] and the batch matrix runs on DGX Cloud credits [if offered] or on the group's Digital Research Alliance of Canada RAC 2027 allocation [if awarded]. Storage needs are met by the Alliance allocation. Software: Isaac Sim 5.x, Isaac Lab, SAPIEN, PyTorch, Prover9/Mace4, [Z3].

**Expected outcomes:** an open-licence verified parts ontology; public audit reports and label mappings covering the main articulated-object datasets; an Isaac Lab-compatible validator and violation metric; two ML-venue papers and one robotics-venue paper; a graduate-course module in the PI's knowledge-modelling course [confirm].

**PI and lab:** Prof. Michael Grüninger, MIE, University of Toronto — Semantic Technologies Laboratory (COLORE, PSL, TUpper); co-PI [U of T Robotics Institute / Vector faculty, name, GPU lab]; lead researcher Dr. Yi Ru (PDF). Institutional acceptance of hardware: [U of T procurement/legal contact].

---

## H. NAIRR Pilot — compute resource request (registry 313549ff9e88)

*Route: nairrpilot.org/opportunities/allocations with an ACCESS ID [confirm requests are open under the NAIRR Operations Center transition]. PI: [HMS supervisor] with Dr. Ru as lead researcher (so the allocation survives the spring-2027 move) [or Dr. Ru as PI if the rules allow]. Prefer NSF systems and cloud credits over DOE systems [citizenship UNKNOWN]. Length: 1–2 pages; ≈700 words below. Target submission 30 Nov 2026.*

**Project title:** Ontology-verified part annotations for robot learning: audit at scale and ontology-constrained policy training

**1. Project description (≈250 words).** [Paste 0.1 Project summary, then add:] This request covers the Harvard-period share of the work: completion of the first audit across five datasets (O2) and the pilot of the O3 experiments in SAPIEN that calibrates the per-run cost for the full matrix. It complements an ACCESS Explore allocation (CPU on Bridges-2/Anvil, [~300] GPU-hours on DeltaAI) and institutional CPU time on the HMS O2 cluster; there is no duplication — the NAIRR request carries the GPU pilot proper and the project storage.

**2. Resource justification.**

| Resource | Request | Justification |
|---|---|---|
| GPU-hours, NSF systems (DeltaAI preferred; Bridges-2 GPU or Anvil GPU acceptable) | [500–700] A100/H100-class GPU-hours | Pilot of the O3 matrix: [2] conditions × [2] held-out splits × [3] seeds = 12 runs at [24] GPU-hours, plus verification-in-the-loop evaluation and development; per-run cost measured here sizes the RAC 2027 and ACCESS Accelerate requests. |
| CPU core-hours (same system) | [~2,000] | SAPIEN physics/rendering [8 cores per GPU]; Tier-2 Prover9/Mace4 obligations not covered by Explore. |
| Storage | [20 TB] project/scratch for the allocation period | Annotation shards and ontology instance store for five datasets (no frames); rollouts and checkpoints [2–5 TB]. |
| Cloud credits [optional, if offered] | [small; for GCS-side extraction of OXE/DROID shards] | Two corpora are hosted on Google Cloud Storage. |
| Software | SAPIEN, Isaac Lab, PyTorch, Prover9/Mace4, [Z3], [Soufflé], LeRobot/RLDS readers | All open source; containerized. |

DOE resources are not requested [pending confirmation of citizenship/visa status; if a US person, Perlmutter GPU is an alternative].

**3. Data-use statement.** [Paste 0.5 Data-management statement.] No NAIRR-curated datasets are requested at this time [add if the NAIRR catalogue lists a relevant robotics dataset].

**4. Team.** PI [HMS supervisor, title, department]; lead researcher Yi Ru (Postdoctoral Researcher, HMS; PhD U of T 2025; ISO/IEC 21838-4 core contributor); collaborator Prof. Michael Grüninger (U of T). Dr. Ru will move to U of T in [April 2027 or later]; the PI remains at Harvard for the allocation period and Dr. Ru continues as a user [confirm permitted].

**5. Expected outcomes and open-release plan.** [Paste 0.4 Expected outcomes.] Release channels: GitHub (Apache-2.0 validator), Hugging Face Hub (LeRobot-compatible audit reports and mappings), COLORE (ontology), a data/audit paper. A short final report with usage statistics will be provided to NAIRR.

---

## I. Hugging Face LeRobot community — validator PR, Hub dataset card, hackathon blurb (registry b08ecff54fe8)

*Not an application: an engineering deliverable with a self-imposed public date of 15 Jan 2027. Everything merged into huggingface/lerobot is Apache-2.0; the validator, not the Passport, is released [CTO to confirm the boundary by 31 Oct 2026]. Check the current LeRobotDataset format [v3 — confirm] and CONTRIBUTING.md before opening the PR.*

**PR title:** Add a part-hierarchy consistency validator for LeRobotDataset part/object annotations

**PR description (≈200 words):**
This PR adds `lerobot/validators/parthood.py` [path per the repo's current layout], a validator that checks object–part annotations attached to a LeRobotDataset (object ids, part ids, part-of relations, joint/kinematic labels) against a small, machine-verified set of parthood axioms: acyclicity and antisymmetry of part-of, transitivity closure, disjointness of sibling parts where declared, and consistency of a part's kinematic role with its declared parent. Violations are reported per episode and per object category with a stable violation code, so that datasets can publish a consistency statistic on their card. The axioms are a compiled subset of a first-order ontology of physical object parts extending ISO/IEC 21838-4 (paper in preparation; full ontology released separately under an open licence); the validator is pure Python, has no solver dependency, and runs in [O(n)] per episode. Tests cover synthetic hierarchies and a public sample [DROID subset — CC BY 4.0]. Datasets without part annotations are skipped with a notice. Licence: Apache-2.0, consistent with the repository. Follow-ups: an optional SMT back end for the full ontology, and an example notebook producing the audit report format used in [Hub org/dataset].

**Hub dataset card — audit report (≈150 words; one card per audited dataset):**
*[Dataset] — parthood-consistency audit, v[0.1], [date].* This repository holds audit results and label mappings for [dataset] produced with the LeRobot parthood validator and the [ontology name] ontology. Contents: violation statistics by episode, object category and axiom family; counter-model summaries for representative failures; a mapping table from [dataset]'s part vocabulary to the ontology's part types with the proof-of-preservation reference. It contains no frames or other raw data from [dataset]; use of the results is subject to [dataset]'s own licence [CC BY 4.0 for DROID and the CC BY sub-datasets of Open X-Embodiment; non-commercial for AgiBot World — state the source licence]. Licence of this repository: [CC BY 4.0 for reports and mappings — confirm compatible with the source licence]. Citation: [audit/data paper or Zenodo DOI]. Maintainer: Yi Ru [affiliation, ORCID].

**Hackathon team registration blurb (≈60 words; June 2027, dates unconfirmed):**
Team [name], [Toronto/Boston]: we bring an open validator that measures whether a dataset's part annotations are consistent with a verified ontology of parthood, and we will collect and release an SO-101 [confirm hardware] articulated-object dataset that passes it, with a part-aware policy evaluated by violation rate alongside task success.

---

## J. ManiSkill / SAPIEN / PartNet-Mobility maintainers — collaboration proposal (registry 98854105be32)

*Not an application: a proposal to the UCSD Hao Su lab / ManiSkill maintainers, sent as an individual academic researcher (SAPIEN terms are non-commercial; AXIOMALITY is not the contributing entity). Send with a first audit result on 3–5 PartNet-Mobility categories in hand [target Feb–Mar 2027]; cc Prof. Grüninger. Check whether a 2027 ManiSkill challenge is announced [Dec 2026 – Jan 2027]. Clarify IP expectations with Hillbot before sharing toolkit code.*

**Subject:** Ontology audit of PartNet-Mobility part hierarchies — corrected annotations and a violation metric for ManiSkill

Dear [ManiSkill lead developer / Prof. Su],

I am a postdoctoral researcher [at Harvard Medical School / at the University of Toronto, with Prof. Michael Grüninger's Semantic Technologies Laboratory], working on formally verified ontologies of physical object parts (I was a core contributor to ISO/IEC 21838-4). I have audited the part hierarchies of [N] PartNet-Mobility categories ([list]) against a machine-verified parthood ontology and would like to offer the results to the SAPIEN/ManiSkill community.

What I found: [x %] of part instances in [category] violate [axiom family — e.g., a movable part whose declared parent is not its kinematic parent]; the attached report lists each violation with a counter-model, and a corrected-annotation diff that resolves [y %] of them without changing the URDFs. I would like to ask three things. (1) Would you host, or link to, the corrected-annotation diff and the mapping from PartNet-Mobility's part vocabulary to the ontology, under the SAPIEN terms [confirm whether the terms allow publication of derived annotations]? (2) Would an `ontology_violation_rate` metric — computed by an open, solver-free validator on a policy's predicted part decompositions — be a welcome addition to ManiSkill's evaluation utilities? I can open a PR. (3) If a ManiSkill challenge runs in 2027, would a track that scores consistency alongside task success be of interest?

Everything on my side is open-licensed (validator: Apache-2.0; ontology: [open licence]); I keep this separate from a company I founded, which does not use PartNet-Mobility. I would be glad to present the audit to the group in a short call.

Best regards,
Yi Ru — [affiliation], yi.ru@alumni.utoronto.ca [ORCID]; cc Prof. Michael Grüninger

---

## K. NVIDIA Isaac Sim / Isaac Lab / Omniverse — no application (registry 90e29ae17a69)

Free downloads (Isaac Sim: Apache-2.0, GitHub; Isaac Lab: BSD-3; Omniverse Kit SDK / USD tooling via GitHub/NGC) under an NVIDIA Developer Program account; no text to submit. Requirements to confirm before the 31 Dec 2026 installation target: [RTX-class GPU, 8 GB+ VRAM minimum / 16 GB+ recommended, Ubuntu 22.04/24.04 or Windows — current Isaac Sim 5.x page]. Developer-profile "area of interest" field (if asked): "Robot learning — formal verification and auditing of part-level annotations; ontology-constrained policy training in Isaac Lab and SAPIEN." Jetson education discount [postdoc eligibility and verifying email domains unconfirmed]: verify with the harvard.edu address; the intended use is an on-device runtime-guardrail demonstration.

---

## L. NVIDIA Inception — company application (registry f624847b7f86 / b82c4ffa6b14) — for the AXIOMALITY CTO/CEO to submit

*Route: nvidia.com/en-us/startups online application. Prerequisites: [legal entity name, country, incorporation date; live company website; company-domain email]. The Sept 2026 US/Canada deck is adequate as the deck. Company-track only: never mention academic allocations. Length: form fields; ≈120–200 words each.*

**Company name / website / stage:** [legal entity] · [website] · pre-seed [confirm; no financing round closed]; founded [date]; [n] employees.

**Company description (≈120 words):**
AXIOMALITY engineers the evidence layer for embodied-AI data: a verification, certification and exchange mechanism that every data-generation route (teleoperation, world models, simulation) and every robot deployment can use. Its first commercial unit is the offline Engine — ingestion → scene graph → SMT check — and the data Passport, a reproducible per-release evidence pack whose audit format is being reviewed with a Big Four accounting firm and an international law firm. The technical core is a four-layer ontology stack (TUpper / ISO/IEC 21838-4 foundational; physical world; robotics domain; dataset instances) with Prover9 proof obligations, Mace4 counter-models and a compiled SMT checking subset, physics residuals under an observation contract, and conformal calibrated uncertainty controlling abstention. Founded by Yi Ru (U of T AI doctorate; ISO/IEC 21838-4 core contributor; prior founder of MICAS and Uing Technologies).

**Product description (≈180 words):**
Real-robot data is scarce (roughly 500k hours worldwide against ~10M needed) and raw hours are trending toward zero value; value migrates to semantics, verification and certification, where passported data commands a 2–3× premium. AXIOMALITY's Engine ingests episodes through adapters for LeRobot, RLDS, ROS 2/MCAP, OpenUSD/USDZ, PLY and JSON, builds a scene graph aligned to the ontology, and checks it — parthood and kinematic-chain consistency, contact and task-phase conditions, safety conditions — with UNKNOWN/timeout as first-class outputs. The Passport packages the result as a versioned evidence pack per data release for model developers, robot OEMs, data suppliers and industrial integrators (pilot USD 25–50k over 8–12 weeks; annual deployment USD 120–240k), against the compliance clock of the EU AI Act Annex I (machinery/robots from 2 Aug 2028), NIST AI RMF and ANSI/A3 R15.06/R15.08. Assets: 100,000 measured 3D asset packages (JPG, USDZ, PLY, JSON oriented boxes), a live consumer spatial app on Apple Vision Pro, 13 granted patents and 9 applications. Status: Engine internal test Q4 2026; three co-development partners and 10,000 verified episodes targeted for Q1 2027; Passport v1 recognition by an assessment body targeted Q2 2027.

**Use of NVIDIA technology (≈120 words):**
The Engine's OpenUSD/USDZ adapter targets the scene-graph conventions used by Isaac Sim and Omniverse; our 100k USDZ asset packages are candidates for SimReady-style conversion, and Isaac Lab is one of the two simulators in which we validate ontology-consistent training. GPU acceleration is used for scene-graph construction from sensor streams, physics-residual estimation and batch SMT checking of episodes [confirm the CTO's stack: CUDA, TensorRT, NIM]. From Inception we seek: Isaac Sim / Omniverse enterprise-component access, DGX Cloud or partner cloud credits for the Q1 2027 batch checks (10,000 episodes) and asset hosting (100k packages), hardware discounts for an RTX workstation, and introductions to humanoid OEMs and NVIDIA's robotics-data partners; in return we can contribute an ontology-aligned, permissively licensed audited subset [Q1 2027 decision] to NVIDIA's physical-AI open datasets.

**Team (≈60 words):** CEO Yi Ru (see above); CTO [name] (McMaster University AI doctorate; applied AI leadership); robotics lead [name] (mechanical/electronic engineering doctorate; autonomous-system perception); senior 3D asset lead [name] (10+ years production). Prior execution: MICAS (USD 5M incl. Accel; >USD 50M revenue in year one; 100+ team), YourTable (Toronto/Imperial incubation).

---

## M. Google for Startups Cloud Program — Start tier (registry 55bea54c0a16) — for the CTO to submit

*Route: cloud.google.com/startup. Prerequisites: [entity facts; website; domain email; confirmation that Uing Technologies never received Google Cloud startup credits (one award per company); FAQ confirmation that a Start award does not block a later Scale/AI-first upgrade]. Only the Start tier is reachable before a financing round. Length: form fields; ≈150 words each.*

**Company description:** [Paste L "Company description".]

**What you are building and how you will use Google Cloud (≈150 words):**
AXIOMALITY is building the offline verification Engine and data Passport for embodied-AI training data (see company description). In Q4 2026 we run the Engine's internal test and in Q1 2027 we deliver 10,000 verified episodes to three co-development partners. On Google Cloud we will (1) store and serve our 100,000 measured 3D asset packages (USDZ, PLY, JSON) and partner episode data in Cloud Storage with per-partner buckets and audit logging, (2) run the batch SMT/Datalog checks on Cloud Batch and Cloud Run jobs, (3) build scene graphs from partner sensor streams on GPU VMs, and (4) [Vertex AI / Gemini API for the natural-language layer of the Passport evidence pack — confirm with the CTO]. Two of the public corpora our adapters target (Open X-Embodiment, DROID) are distributed from Google Cloud Storage, which makes GCP the lowest-egress location for cross-dataset validation. Expected Start-tier usage: [TB-months of storage, vCPU-hours, GPU-hours — CTO's Q1 2027 budget].

**Funding status:** bootstrapped / pre-seed; no equity round closed [confirm]; seeking a financing round sized to an 18-month operating plan. **Accelerator affiliation:** none yet [CDL-Toronto / UTEST / MaRS / Techstars / YC candidates].

---

## N. AWS Activate — Founders tier (registry bc48b23e314b / 0a576098038a) — for the CTO to submit

*Route: aws.amazon.com/startups/credits with the company AWS account (never the Harvard account) and website. Prerequisites: [entity facts; whether Uing Technologies already received Activate credits; current tier names and caps]. Portfolio tier later with an Activate Provider organization ID [CDL-Toronto, UTEST, MaRS, Robotics Factory Accelerate, or a VC]. Length: short form; ≈120 words.*

**Company description:** [Paste L "Company description", trimmed to the field limit.]

**How you will use AWS (≈120 words):**
AXIOMALITY's offline Engine verifies embodied-AI training data (ingestion → scene graph → SMT check) and issues a per-release evidence pack, the Passport. On AWS we will run the Q1 2027 batch verification of 10,000 partner episodes on AWS Batch with Spot instances, store partner data and our 100,000 measured 3D asset packages in S3 with per-partner isolation and object-lock audit trails, build scene graphs from sensor streams on GPU instances, and host the Passport delivery API [confirm the CTO's architecture]. Adapters for LeRobot, RLDS, ROS 2/MCAP and OpenUSD/USDZ already exist. Estimated first-year usage: [S3 TB-months; Batch vCPU-hours; GPU-hours — from the CTO's Q1 2027 budget]. Target customers include robot OEMs and data suppliers in the US and Canada; AWS Robotics and Amazon industrial contacts are relevant partners.

**Stage / funding:** pre-seed, bootstrapped [confirm]; founded [date]; website [URL]; AWS account ID [company account].
