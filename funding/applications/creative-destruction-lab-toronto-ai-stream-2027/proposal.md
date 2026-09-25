# AXIOMALITY — CDL-Toronto Artificial Intelligence stream, 2027/28 cohort: application narrative

Written as answers to the fields CDL's online application is known to cover (company, problem, technology, product and traction, market and business model, team, fundraising, IP, challenges, objectives, fit). CDL does not publish the field list or character limits; each answer is kept to 150–350 words so it fits a form box, and each carries a one-line version for short fields. When the 2027/28 form opens, map each section to its field and trim. Appendix A is the technical deep dive in the structure Prof. Grüninger's NSERC proposals use; it goes into the deck appendix or a mentor data room, **never into a form field** — CDL reviewers read hundreds of applications and score the form answers. Note that Appendix A overlaps with the founder's academic postdoctoral program (verified parts ontologies); the company narrative must keep the product (Engine, Passport, adapters, accumulated mappings) distinct from that program and from the Semantic Technologies Laboratory's methodology (see §11). CDL's FAQ asks applicants to show momentum: every section that carries a dated target must be refreshed with the actual at submission. [Brackets] mark facts the company must confirm before submission; nothing bracketed is to be submitted as-is.

---

## 1. One-line description

AXIOMALITY builds the evidence layer for robot-learning data: a verification Engine and a data Passport that check every episode against a machine-proven ontology and physics, so that data generators, robot OEMs and regulators can trust what a robot was trained on.

(Short field: "Robotics data verification, certification and exchange — machine-checkable evidence for embodied-AI training data.")

## 2. Company overview

AXIOMALITY is a [Canadian / US — confirm] company founded in 2026 [confirm date; state relationship to Uing Technologies, founded Aug 2022] by Dr. Yi Ru, with a CTO (McMaster University AI doctorate), a robotics lead (mechanical/electronic engineering doctorate, autonomous-system perception) and a senior 3D asset lead (more than ten years of production experience). We build a reusable verification and evaluation layer that every data-generation route — teleoperation, world models, simulation — and every robot deployment can use. Our first commercial unit is the offline Engine (ingestion → scene graph → formal and physical checks) and the data Passport, a reproducible per-release evidence pack whose audit-pack format has been reviewed with a Big Four accounting firm and an international law firm [names, if disclosable].

We start from three assets that took years to build: 100,000 measured 3D asset packages (JPG, USDZ, PLY, JSON oriented boxes) from room-level reconstruction and object-level annotation, with a consumer spatial app (an AR pet-interaction app) live on the Apple Vision Pro App Store; a knowledge kernel whose axioms are machine-proven consistent and aligned with ISO/IEC 21838-4, the international top-level-ontology standard to which I was a core contributor; and 13 granted patents and nine invention applications in 3D recognition, indoor modelling and automatic reconstruction. The minimum Engine is under development with internal testing planned for Q4 2026 [update with the result]; our next milestone is independent customer validation.

Stage: pre-seed [confirm]; revenue to date [confirm]; funds raised to date [confirm]; headcount [confirm].

## 3. The problem

Physical AI is data-bound in a way language models never were. About 500,000 hours of real-robot interaction data exist worldwide against an industry estimate of roughly 10 million hours needed; text is downloaded, motion data is collected in the physical world. Collection costs US$50–200 per effective hour with no learning curve — capacity is added by adding rigs and operators, and the ten-millionth hour costs what the first did. Repetition does not generalize: Lin et al. (2024) report about 90% success in unseen environments from 1,600 demonstrations spread over 32 environment–object pairs, where a thousand hours at one site fail in the first new environment [1]. And data is bound to the robot that collected it: action spaces, camera poses and contact modes do not transfer between a collaborative arm and a humanoid, so switching embodiment means re-collect, re-label, re-verify.

The consequence is that value is moving from hours to evidence. Raw hours are approaching zero (free factory video in 2026); labs pay for semantics and coverage; exchanges and regulators pay for verification and certification, and vendors price passported data at two to three times raw hours. The compliance clock is set: the EU AI Act's Annex I obligations apply to AI embedded in machinery and robots from 2 August 2028, requiring traceable, auditable training data [2]; NIST's AI RMF and ANSI/A3 R15.06/R15.08 are the voluntary North American references. Today none of the existing evidence forms — self-declared quality documents, log sampling, one-off third-party audits, self-reported benchmarks — can be checked record by record by a machine.

Who feels it: model developers running heterogeneous data mixtures (π0.5), robot OEMs releasing autonomy updates, data suppliers proving acceptance, and industrial integrators producing application-specific test evidence. Each has a recurring data decision and a review bottleneck, and no shared, checkable format.

## 4. The technology (novel, defensible, scalable)

**What is new.** The Engine grounds robot data into a typed scene graph and checks it against a four-layer ontology kernel: TUpper (ISO/IEC 21838-4) as the foundation; a physical-world layer (parts, shape, measurement, materials, change, process); a robotics layer (embodiment, kinematic chains, contextual affordances, contacts, task phases, bounded safety conditions); and a dataset-instance layer (episodes, frames, sensors, transformations, source observations). Constraints are specified as Common Logic modules with explicit bridge axioms; theorem obligations are checked with Prover9 and counter-models searched with Mace4 [3]; the approved constraints are compiled into a supported SMT subset for per-record checking at dataset scale [4]. For a property P we search Φ ∧ observations ∧ ¬P; SAT and UNSAT are interpreted only within declared scope, and UNKNOWN, timeout, unsupported construct and missing input are first-class outputs — computation limits are never silently converted into a pass. Physical checks use a dynamics residual r_t = ‖M(q)q̈ + C(q,q̇) + g(q) − τ − J(q)ᵀf‖ under an observation contract that declares frames, units, load range and calibration; conformal prediction [5] calibrates uncertainty so that the system abstains and escalates rather than guesses. Adapters expose one checking interface over LeRobot, RLDS, ROS 2/MCAP, OpenUSD/USDZ, PLY and JSON without erasing source semantics.

**Why it is defensible.** No collection, simulation, tooling or world-model vendor holds an ISO-lineage formal ontology, physics-plus-logic checks, measured room geometry, a consumer capture flywheel, a certification/audit pack and a cross-embodiment schema together; the direct alternatives (3Laws Supervisor, reasonX SafetyScope, NVIDIA's data-factory blueprint, internal pipelines, KnowRob-style ontologies) each cover one of these. The kernel's axiom set is machine-proven consistent; the standard it extends is one I helped write; and the assets that compound — validated task mappings, permitted failure taxonomies, adapters, regression cases — are company-authored background technology protected by 13 granted patents and nine applications. Public standards and solvers alone are not our IP; the verified kernel, the evidence schema and the accumulated mappings are.

**Why it scales.** The evidence loop (Collect → Ground → Verify → Augment → Deliver → Learn) is built to three criteria: every stage has an independently saleable output; each stage's output is the next stage's input with no manual conversion; and confirmed findings flow upstream as new rules, calibration updates and targeted collection, so round N+1 costs less per unit than round N. That is the opposite of collection, where unit cost is flat, and of marketplaces, where quality is unverifiable.

## 5. Product and stage of development

Achieved: 100,000 measured 3D packages inventoried by rights, source geography and unique count; the consumer spatial app on Apple Vision Pro; the knowledge kernel with machine-proven consistency; the audit-pack format reviewed with an accounting firm and a law firm; relationships in regulated industries (multinational medical-device and pharmaceutical companies, national standards bodies, a large hospital network) [names if disclosable].

In progress: the minimum verification Engine — ingestion → scene graph → SMT check → Passport — with internal testing in Q4 2026 [insert result: date, versions, known limits]; kernel v1 for home scenes; connectors for LeRobot, RLDS and OpenUSD; discussions with humanoid OEMs and platform/OS companies on co-development and channels.

The Passport is a portable evidence manifest: identity and rights (dataset/episode IDs, permitted use, content hashes); scope and method (robot, task, sensor and calibration context, kernel and software versions, thresholds, limitations); findings and reproducibility (per-check results, evidence pointers, repairs, reviewer decisions, runnable specifications); issuer and integrity (signature, signing policy, package hash). A Passport supports a specific review; it is not a blanket certificate of compliance or safety, and we say so on every page.

Runtime semantic guardrails — the same kernel checking task transitions live — are a separately gated product that needs a qualified partner, target hardware and latency and fallback tests; runtime revenue is outside the initial cohort model.

## 6. Traction and milestones

Dated targets from our September 2026 plan, to be replaced with actuals at application time [update every line]:
- Q4 2026: minimum Engine internal test — [result].
- Q1 2027: three co-development partners signed — [names/count]; 10,000 verified episodes from partner data and open datasets — [count].
- Q2 2027: Passport v1 recognized by one assessment body or standards organization — [body, status].
- Month 18: five cumulative paying customers and two renewals or expansions.

At least one named co-development partner moves from "in progress" to "achieved" before we present to investors; that partner is the traction we will lead with in the CDL interview [confirm].

## 7. Market and business model

We count eligible purchasing organizations, not robot shipments. First buyers own a recurring data decision: model developers (robot-learning lead; batch acceptance and diagnostics), robot OEMs (autonomy/quality lead; failure-linked regression evidence), data suppliers (data operations; repeatable customer acceptance) and industrial integrators (engineering/quality; application-specific test evidence), in the US and Canada.

Offer: an 8–12-week pilot at US$25k–50k on one task family with fixed data and acceptance criteria; an annual deployment at US$120k–240k covering supported integrations, recurring checks and support, implementation scoped separately. A sizing cohort of ten pilots and four annual conversions implies US$250k–500k in pilot bookings and US$480k–960k in annual recurring fees before credits (midpoint: US$1.04M combined bookings in the first contracted year).

Market: a focused pool of 80–200 organizations at US$150k–300k gives US$12M–60M a year; platform paths of 500 customers at US$200k or 200 at US$500k give US$100M ARR. The surrounding markets are moving: data annotation and training data US$4.9B (2025) → US$17.1B (2030); embodied AI US$4.4B → US$23.1B at 39% CAGR; physical AI ≈€430B by 2030 (PwC Strategy&). Customer ROI is measured against the whole operating cost: an illustrative 600 review hours a month at US$150 is US$1.08M of annual review capacity; a hypothesized 40% reduction releases US$432k against a stated US$180k first-year purchase, before the customer's own integration and compute costs.

Expansion is earned: task reuse must reduce second-deployment effort while preserving reliability, and renewals and new commitments — not more supported concepts — establish market scale.

## 8. Competition

The competitive map runs from raw collection to structured and verified, and from hand/tabletop to room/whole scene. Collection vendors (Build AI, Mecka, Human Archive, DreamVu, Config) sell hours whose price is heading to zero; tooling and labelling vendors (Scale AI, Encord, Foxglove, Rerun, Roboto) provide operations and inspection without integrated, actionable checks; simulation and world-model vendors (Isaac/Cosmos, Lightwheel, World Labs) generate data that nobody has verified for physical and logical consistency; 3Laws provides a real-time safety filter. NVIDIA Halos for Robotics occupies the functional-safety layer with accredited labs; we do not — semantic guardrails sit above it at the task level. Our position: structured, room-scale and certified; the wedge must beat the buyer's existing stack on less adaptation effort, better diagnostics and lower total cost, which we prove in the pilot against the customer's scripts, simple rules and a VLM-plus-rules baseline at fixed risk and cost.

## 9. Team

Founder/CEO — Dr. Yi Ru. PhD in Information Engineering, University of Toronto (2025); core contributor to ISO/IEC 21838-4:2023 (TUpper top-level ontology, ISO/IEC JTC 1/SC 42); 21 papers disclosed, Distinguished Paper Award at FOIS 2018 [confirm role], invited AAAI presentation [confirm], an English-language monograph [title]; first inventor on multiple patents. Founding team member of MICAS (Jul 2021–Aug 2022) [state title/role]: over US$5M in angel investment including Accel Partners, a cross-border DTC platform above US$50M annual revenue within a year, a 100+ person team, CRM/ERP/WMS built in-house and ML-driven marketing with KOL ROI above 4. Co-founder and CEO of Uing Technologies (Aug 2022–): structured 3D physical-world datasets, one of the first AR pet-interaction apps on the Apple Vision Pro App Store, nine invention patent applications. Co-founder of YourTable Inc. (2018–2021), incubated by U of T, Schulich and Imperial College London; Lo Family Social Venture Fund; represented Canadian startups at Collision 2019. Venture capital intern, IDG Capital (2018–2021). Currently postdoctoral researcher, Harvard Medical School [lab; confirm], returning to Toronto in spring 2027 [confirm].

CTO — [name]: McMaster University AI doctorate; applied AI leadership [prior roles].
Robotics lead — [name]: mechanical/electronic engineering doctorate; autonomous-system perception [prior roles].
Senior 3D asset lead — [name]: more than ten years of 3D production experience [prior roles].

Why this team: the kernel needs someone who has written a top-level ontology standard and proven axiom sets consistent; the Engine needs applied AI and robotics perception; the data foundation needs production 3D; and the company needs a founder who has been on the team that took a venture from zero to more than US$50M in annual revenue and a 100-person team within a year. Co-founder status, equity and full-time commitment: [confirm for each].

Founder commitment (CDL asks; answer plainly): the founder [is / is not yet] full-time on AXIOMALITY; current allocation is [x days per week] alongside a research appointment [Harvard Medical School now; U of T MIE postdoc from spring 2027 if awarded — state which]. [Name], CTO, is [full-time]. The founder will attend all five CDL sessions in person and owns the mentor objectives; the arrangement with the research host is disclosed in writing before Session 1. Our unfair advantage, in CDL's words: a founding team member who co-wrote the ISO top-level-ontology standard the kernel extends, 100,000 measured 3D packages no competitor holds, and [13] granted patents.

## 10. Fundraising

Raised to date for AXIOMALITY: [amount / none — confirm; the US$5M Accel figure belongs to MICAS and must not be presented as AXIOMALITY funding]. We are seeking, in this order: paid design partners, co-development partners, standards recognition, non-dilutive funding (NRC IRAP and Mitacs applications are in preparation on the company side), and a financing round sized to the 18-month operating plan [amount, timing, instrument — confirm; CDL's stated sweet spot is a US$500K–5M seed within 12 months of applying — verify on the FAQ]. Stated for the form: we plan to raise [US$X] as a [SAFE / priced seed] by [month 2028], within 12 months of this application, led by [investor type]; CDL mentor and associate investment is welcome on the same terms. Use of funds follows the plan's four gates: core product (kernel, mappings, connectors, evidence schema, customer-controlled execution); independent validation (customer-owned benchmarks, expert adjudication, real-robot tests, regression suites); commercial execution (a small paid-design-partner cohort, acceptance, collections, conversion); and cash discipline (a monthly model of headcount, contractors, cloud/inference, working capital and minimum reserve, with a buffer for delayed collection). Capital follows the remaining evidence requirements: we fund a repeatable offline business before broad platform expansion.

## 11. Intellectual property

13 granted patents and nine invention applications in 3D recognition, indoor modelling and automatic reconstruction [reconcile with the drafts' count of 3 Chinese invention patents and 9–10 German utility patents; list numbers; state assignment to the company]. Kernel specification, adapters and evidence schema are company-authored background technology. Customer datasets and confidential findings are separated from reusable adapters, task schemas and background technology by contract; the data plane stays in the customer's environment, the evidence plane is packaged per release. Standard alignment (ISO/IEC 21838-4) does not certify the reasoning engine, translator or robot safety, and we do not claim it does. Provenance: the verified-ontology methodology (COLORE, Prover9/Mace4 verification) and TUpper are public; the kernel, adapters, evidence schema and mappings were authored by the company [confirm dates and authorship; confirm no University of Toronto or Harvard inventions-policy claim, and that any work done during a university postdoctoral appointment is separated from the product by agreement].

## 12. Our biggest challenges (honest)

We pre-registered the ways this can fail and what we will do about each. (1) Simple rules may match the full kernel at equal cost on a customer's data; then we narrow to the error classes where formal checks pay and drop the rest. (2) Grounding may produce consistent graphs that are factually wrong; then perception and abstention, not the kernel, are the work. (3) Augmentation may raise internal scores without raising real outcomes; then we recalibrate the generator and mixture, and keep unsupported variants out of the approved split. (4) Each account may need extensive redesign; then we narrow and standardize the task domain before scaling sales. (5) A recipient may be unable to reproduce a stated check; then the Passport's artifacts and authorized access are the product until they can. (6) Runtime may fail latency or false-stop acceptance; then the module stays offline. Beyond the technical falsifiers: as of September 2026 we have no revenue, no paying customer and no independent customer validation [update]; the founder splits time with a research appointment [state the arrangement and the full-time date]; the team is small [headcount] and co-founder status is [confirm]; the patent count must be reconciled before we cite it (§11); and first-order checking is not universally decidable, so "no contradiction found" is never sold as a consistency proof.

## 13. Objectives we would set with CDL mentors

CDL runs on three objectives per session. Ours for Session 1, framed so that each is falsifiable by June 2028:
1. **Prove the wedge.** Two paid validation engagements completed with acceptance against a blinded customer baseline, with all implementation and review effort recorded (months 0–3 of the operating plan).
2. **Prove recurrence.** Three cumulative paying customers, positive delivery contribution on two, and one signed recurring commitment integrated into a customer's release decisions (months 4–9).
3. **Prove reusable infrastructure.** A second task or embodiment delivered with reusable mappings, adaptation hours and retained performance recorded, and a financing round closed that is sized to the 18-month plan (months 10–18).

## 14. Why CDL-Toronto and the AI stream

The AI stream asks for AI systems that autonomously interact with and learn from complex environments, including robotic control. The Engine is exactly that: it checks what a robot experienced, learns from confirmed failures (adapter fixes, rules, calibration updates, targeted collection) and decides what to collect next. Toronto is where the kernel's methodology comes from — the verified-ontology and COLORE work at the University of Toronto's Semantic Technologies Laboratory, and the ISO/IEC 21838-4 standard — and where the founder will be based from spring 2027. Sanctuary/Magna and Vention illustrate the Canadian OEM and integrator workflows our first buyers run, and CDL's mentors and Toronto's robotics and AI investors are the route to the financing round. The CDL-Toronto AI site page describes the stream as applying AI to scientific discovery [confirm the 2027/28 wording; email 1, question 2]; our claim to that description is that the Engine treats every dataset release as an experiment — pre-registered comparisons, falsifiers, negative results preserved — and that the kernel is contributed back to the standard. CDL takes no equity and we ask for no capital from CDL itself; we will raise the round within CDL's 12-month window, and what we want from the program is the objective-setting discipline and mentors who will tell us, at every session, whether the wedge is real.

---

## Appendix A — Technical deep dive (for mentors, interviewers and the deck appendix)

### A1. Recent progress

An ontology is a computer-interpretable specification that declares what terms a system uses and what they mean. My research axiomatizes ontologies as theories in first-order logic and verifies them by automated reasoning, and I have carried that method into a standard and into production systems.

- **TUpper and ISO/IEC 21838-4:2023.** As a core contributor within ISO/IEC JTC 1/SC 42 I worked on the axiomatization, modular organization and machine-checked verification of TUpper, the first internationally standardized top-level ontology with a complete first-order axiomatization [6]. The AXIOMALITY kernel is built as a verified modular extension of it.
- **Material constitution and mereological pluralism.** With M. Grüninger I developed a theory of material constitution as a parthood-preserving mapping between mereologies, and a validation of mereological pluralism, both stated in first-order logic with consistency and non-triviality established by Prover9 and Mace4 (two papers submitted to Synthese, 2026) [7], [8]. The theory says exactly when two part decompositions of the same object are compatible — the question a robot dataset poses whenever kinematic, functional and visual part labels co-exist.
- **Ontology-governed systems in production.** My doctoral architecture placed a verified ontology over the data, learned-model and simulation layers of an AI system; at Uing Technologies we built structured 3D datasets and the ontology-based representations behind a live Apple Vision Pro application; at MICAS the CRM/ERP and influencer-allocation systems I helped build used ontology-governed data models at production scale [state plainly what "ontology-governed" meant in that system].

### A2. Objectives

*Can every record a robot is trained on be checked, by machine and before release, against the axioms of the physical world that a human inspector would use — and does that evidence lower the cost of the next round of collection?*

1. **Kernel as specification** — a verified four-layer ontology (TUpper; physical world; robotics; dataset instances) with explicit module interfaces, bridge axioms and dependency tests.
2. **Kernel as audit** — a two-tier checking pipeline (compiled SMT for bulk records; theorem proving for residual hard cases) that returns localized findings, unknowns and review decisions, and preserves valid failures.
3. **Kernel as feedback** — a learning stage that turns confirmed findings into adapter fixes, rules, calibration updates and targeted collection, and measures net benefit at a fixed error tolerance.

### A3. Literature

Part-level datasets (PartNet [9], PartNet-Mobility/SAPIEN [10], GAPartNet [11]) and robot corpora (Open X-Embodiment [12], DROID [13], AgiBot World [14]) define "part", "contact" and "task phase" operationally; no dataset or learned model is required to satisfy the axioms of parthood, and no principled mapping relates their vocabularies, so pooled training silently mixes incompatible semantics. Existing process and spatial ontologies used in robotics (KnowRob-style) are expressed in description logics or informal schemas whose weak axiomatizations admit unintended models; conformal prediction [5] gives distribution-free coverage but says nothing about logical consistency; safety filters (3Laws) and safety-case tools operate at the control or documentation layer, not on the per-record semantics of training data. There has been no prior per-record ontological audit of robot training data.

### A4. Methodology — themes, projects, open questions

Ontologies are designed and verified with the ontology-lifecycle and COLORE methodology of the Semantic Technologies Laboratory: for each module we characterize the models of the axioms and determine whether they coincide with the intended models; competency questions come from customer acceptance tests.

**Theme 1 — Grounding and specification.** *Given episodes, scans and logs under a declared input contract, produce a typed scene graph in which every assertion links to an observation and missing evidence is flagged.*
- Project 1.1 Episode contract and adapters (LeRobot, RLDS, ROS 2/MCAP, OpenUSD). Open question: which checks can execute given each adapter's supported fields, and how is support reported by version? (Robotics lead; gate: Q4 2026 Engine test.)
- Project 1.2 Kernel v1 for home scenes. Open question: are the physical-world and robotics modules consistent in combination, and which bridge axioms are entailed rather than asserted? (Founder; Prover9/Mace4 obligations recorded with tool versions and resource limits.)

**Theme 2 — Verification.** *For each record and property P, decide Φ ∧ observations ∧ ¬P within declared scope, and expose UNKNOWN honestly.*
- Project 2.1 Compiled SMT subset. Open question: which fragment of the kernel compiles to a decidable checking subset without changing the conclusions of the first-order theory on prior datasets (regression)? (CTO.)
- Project 2.2 Physics residuals and calibrated abstention. Open question: at what held-out proxy error do PINN/neural-operator surrogates replace the analytic residual for a robot family, and how does conformal coverage behave under sensor, object, policy and embodiment shift? (Robotics lead; acceptance threshold agreed with the customer before delivery.)

**Theme 3 — Feedback and augmentation.** *Does confirmed evidence lower the cost and raise the coverage of the next batch?*
- Project 3.1 Learn stage. Open question: what fraction of confirmed findings need a new axiom versus an adapter fix, calibration or measurement request, and does net benefit — later-batch detection, review effort, maintenance cost, real task outcomes — rise across time-ordered customer batches? (CTO.)
- Project 3.2 Controlled variants. Open question: does a variant validated on held-out real views, measured contacts and unseen layouts improve real success and intervention rates when raw, conventionally filtered, Engine-checked and Engine-plus-augmentation mixtures are compared at fixed model, compute and data budget? (Robotics lead.)

Evaluation discipline throughout: hold out rooms, objects, sessions and time before tuning; distinguish natural defects from injected errors; audit passed samples as well as the review queue; report confidence intervals; pre-register comparisons and preserve negative results.

### A5. Impact

Near term: a machine-checkable evidence format for robot training data that maps to the requirement-to-evidence chain buyers already face (governance, traceability, conformity, benchmark testing), with the EU Annex I date of 2 August 2028 as the forcing function, and a measurable release of review capacity for model developers, OEMs, data suppliers and integrators. Longer term: the evidence format becomes the unit of measurement and of trade for embodied data — what exchanges price and regulators accept — and the verified kernel, contributed back through ISO/IEC JTC 1/SC 42 and the COLORE repository where it is generic, becomes shared infrastructure for physical AI rather than one company's middleware.

## Bibliography

[1] Lin, F., et al. (2024). Data Scaling Laws in Imitation Learning for Robotic Manipulation. arXiv preprint.
[2] Regulation (EU) 2024/1689 (Artificial Intelligence Act), as amended by Regulation (EU) 2026/1744; Annex I obligations for AI embedded in machinery and other regulated products apply from 2 August 2028.
[3] McCune, W. Prover9 and Mace4. https://www.cs.unm.edu/~mccune/prover9/
[4] de Moura, L., and Bjørner, N. (2008). Z3: An Efficient SMT Solver. TACAS.
[5] Angelopoulos, A. N., and Bates, S. (2021). A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification. arXiv:2107.07511.
[6] ISO/IEC 21838-4:2023. Information technology — Top-level ontologies (TLO) — Part 4: TUpper. ISO/IEC JTC 1/SC 42.
[7] Ru, Y., and Grüninger, M. (2026, submitted). Material Constitution as a Parthood-Preserving Mapping between Mereologies. Synthese.
[8] Ru, Y., and Grüninger, M. (2026, submitted). [Exact title — mereological pluralism validation]. Synthese.
[9] Mo, K., et al. (2019). PartNet: A Large-Scale Benchmark for Fine-Grained and Hierarchical Part-Level 3D Object Understanding. CVPR.
[10] Xiang, F., et al. (2020). SAPIEN: A SimulAted Part-based Interactive ENvironment. CVPR.
[11] Geng, H., et al. (2023). GAPartNet: Cross-Category Domain-Generalizable Object Perception and Manipulation via Generalizable and Actionable Parts. CVPR.
[12] Open X-Embodiment Collaboration (2023). Open X-Embodiment: Robotic Learning Datasets and RT-X Models. arXiv preprint.
[13] Khazatsky, A., et al. (2024). DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset. RSS.
[14] AgiBot World Colosseo (2025). [Full citation to confirm.]
[15] ISO/IEC 24707. Information technology — Common Logic (CL). 
[16] NIST (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0).
