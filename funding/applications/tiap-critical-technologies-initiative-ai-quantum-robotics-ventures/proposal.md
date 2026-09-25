# Passport v1 for regulated robotics: a verified evidence layer for robot and medical-device AI data

**TIAP Critical Technologies Initiative — project proposal · AXIOMALITY [legal name; business number]** · 12 months from agreement start · Prepared by Dr. Yi Ru, Founder/CEO · Draft 2026-09-25

*Format note: TIAP publishes no template, page limit or rubric for the CTI; the official text says applicants submit a project proposal with budget and milestones for an investment committee, and the registry lists a technology and IP summary, a business plan / use of funds, and team bios as the components. This draft is about eight pages plus a bibliography, written so that §1–§2 can be lifted as the 2-page technology/IP summary for the interview, §3–§5 form the project proposal with milestones, §6–§7 the business plan and use of funds, and §8 the team. Citations are numbered; the bibliography is on the last page. Items in [brackets] are unconfirmed and must be supplied before submission. Sector framing: TIAP's own descriptions centre on health-science commercialization; the regulated-health track (Project 2.4 and §6) is written to lead if TIAP requires it, and the technology and business are unchanged either way.*

## 1. Summary

AXIOMALITY builds the verification and evaluation layer for embodied-AI data: an offline **Engine** that checks robot-learning episodes record by record against a knowledge kernel whose axioms have been machine-proven consistent, and a **Passport**, a reproducible per-release evidence pack that a customer, an assessor or a regulator can rerun. The kernel descends from my doctoral work at the University of Toronto with Prof. Michael Grüninger and from ISO/IEC 21838-4:2023 (TUpper), the international standard for a top-level ontology to which I was a core contributor [1]. The company holds 100,000 measured 3D asset packages, 13 granted patents and nine invention applications in 3D recognition, indoor modelling and automatic reconstruction [assignee to confirm], a consumer spatial-capture application live on the Apple Vision Pro, and working relationships with multinational medical-device and pharmaceutical companies, national standards bodies and a large hospital network.

The CTI funds would take the Engine from its Q4 2026 internal test to a product whose checks run on partner data, whose results a third party can reproduce, and whose value over simpler alternatives has been measured — with one of the design-partner tracks placed in a regulated-health setting, where robots and AI systems are medical devices or operate around patients and where the evidence requirement is strictest. The non-dilutive grant (up to CAD 100K) is applied to technology development; the matched investment (up to CAD 100K, from TIAP or a third party) to commercial execution and executive advisory. Twelve-month deliverables: kernel v1 verified and compiled (M3); 10,000 verified episodes with an audit report (M6); Passport v1 evaluated in writing by one assessment body or standards organization (M9); two design-partner acceptances against independent baselines, one of them in a health setting (M12).

## 2. Technology and IP summary

An ontology is a computer-interpretable specification that an application uses to declare what terms it uses and what the terms mean. My research, and the company's technical core, is the axiomatization of such specifications as theories in first-order logic and their verification by automated reasoning: every claim about the ontology is a theorem or a counter-model, not an informal gloss. The background we bring:

- **A verified knowledge kernel with Ontario origin.** Four ontology layers — TUpper (ISO/IEC 21838-4:2023 [1]) as foundation; a physical-world layer (parts, shape, measurement, materials, change, process); a robotics layer (embodiment, kinematic chains, contextual affordances, contacts, task phases, bounded safety conditions); and a dataset-instance layer (episodes, frames, sensors, transformations). Axioms are written as Common Logic modules (ISO/IEC 24707 [2]); theorem obligations are checked with Prover9 and counter-models searched with Mace4 [3]; approved constraints are compiled into a supported SMT subset checked with Z3 [4]. The axioms have been machine-proven consistent. The theory of parts that the kernel rests on — material constitution as a parthood-preserving mapping between mereologies, and the validation of mereological pluralism — was developed with Prof. Grüninger at the University of Toronto and is in two papers submitted to Synthese (2026) [5], [6]. It fixes exactly when two part decompositions of the same object are compatible, which is the question every robot dataset poses when kinematic, functional and visual part labels co-exist without any statement of how they relate. [The IPO determination of which elements are U of T-created IP under the Inventions Policy, and the licence terms, to be recorded here.]
- **Measured spatial data at scale.** 100,000 measured 3D asset packages (JPG, USDZ, PLY, JSON oriented boxes: centroid, dimensions, rotation in metres and radians) from room-level reconstruction and object-level annotation; a consumer spatial-capture application on the Apple Vision Pro App Store; nine invention applications from that stack. The inventory is documented by rights, source geography and unique count.
- **Patents and background technology.** 13 granted patents and nine invention applications in 3D recognition, indoor modelling and automatic reconstruction [numbers, titles and assignee to list; the drafts elsewhere count 3 Chinese invention patents and 9–10 German utility patents — reconcile]. The kernel specification, adapters and evidence schema are company-authored background technology.
- **Evidence loop in progress.** A minimum verification Engine (ingestion → scene graph → SMT check → Passport) is scheduled for internal test in Q4 2026, with a kernel v1 for home scenes and connectors for LeRobot [7], RLDS [8] and OpenUSD. An international law firm has mapped regulatory clauses to evidence fields and a Big Four accounting firm has reviewed the audit-pack design [firms to name if they consent].
- **Standards position.** The kernel's ISO/IEC 21838-4 lineage and my participation in ISO/IEC JTC 1/SC 42 [working-group designation to confirm] give the company a route to have the Passport format recognized where the evidence format becomes the unit of measurement and of trade.

What is *not* yet established, and what this project establishes, is stated in §4.

## 3. The problem and why now

Real-robot interaction data is scarce — about 500,000 hours worldwide against an industry estimate of roughly 10 million hours needed — costs USD 50–200 per hour to collect with no learning curve, and is bound to the embodiment that collected it [9]–[13]. Generalization is set by the number of environment–object pairs covered, not by hours at one site [14], so targeted collection and provenance, not volume, are the binding constraint. As raw hours approach zero price, value migrates to semantics, verification and certification: vendors price passported data at two to three times raw hours.

The compliance clock is set. The EU AI Act's Annex I obligations apply to AI embedded in machinery and other regulated products — robots and, under the medical-devices regulation, medical devices [confirm scope with counsel] — from 2 August 2028 [15], requiring traceable, auditable training data. None of today's evidence forms — documents and self-declaration, log sampling, one-off third-party audit reports, self-reported benchmarks — can be checked record by record by a machine. In North America, NIST AI RMF [16], ANSI/A3 R15.06/R15.08 and OSHA are the references buyers already cite, and hospital and medical-device buyers add their own quality-system and validation duties. Buyers in the United States and Canada already gate their own data through acceptance and regression workflows; every deployment adds a stream of failures, interventions and release decisions that needs a versioned, checkable record.

Existing tooling divides into collection vendors, simulation and world-model vendors, and inspection or labelling tools (Foxglove, Rerun, Roboto, Encord, Scale); runtime safety filters (3Laws) and safety-case tools (reasonX SafetyScope) sit beside them; NVIDIA's data-factory blueprint and Halos for Robotics address production and functional safety. None applies an axiom set that has been machine-proven consistent to per-record data, and none produces evidence that re-verifies offline. Research ontologies for robotics such as KnowRob [17] provide vocabularies without the verification standard of ISO/IEC 21838-4; neuro-symbolic training interfaces — Logic Tensor Networks [18], DeepProbLog [19] — supply soft constraints whose relationship to hard logical satisfaction is not established. Part-level corpora (PartNet [20], PartNet-Mobility/SAPIEN [21], GAPartNet [22]) and robot corpora (Open X-Embodiment [11], DROID [12], AgiBot World [13]) define "part", "contact" and "task" operationally and independently; no dataset or model is required to satisfy the axioms of parthood, and pooled training silently mixes incompatible vocabularies. The consequences are observed but have never been measured, because there has been no formal specification to measure against.

## 4. Project objectives

The project is motivated by the following long-term challenge:

*Can the physical and logical consistency of a robot-learning dataset be checked record by record against a machine-proven specification, at dataset scale, so that a training or release decision carries evidence that a customer, an assessor or a regulator can reproduce?*

To address this challenge, the project has four objectives, each tied to a dated milestone:

1. **Kernel v1 as a verified, compiled specification.** Complete and verify the physical-world and robotics modules of the kernel as extensions of TUpper integrated with the Process Specification Language (PSL) [23] for state change under manipulation, and compile the approved constraints into the SMT subset with regression tests (M3).
2. **Engine v1 running on partner data.** Extend adapters (LeRobot, RLDS, ROS 2/MCAP, OpenUSD/USDZ, PLY, JSON), grounding with abstention, and the two-tier checker so that 10,000 episodes from partner and open datasets are verified with localized findings, unknowns and review decisions (M6).
3. **Passport v1 recognized.** Ship the portable evidence manifest — identity and rights, scope and method, findings and reproducibility, issuer and integrity — and obtain a written evaluation from one assessment body or standards organization (M9).
4. **Measured value with two design partners, one in a regulated-health setting.** Run the pre-registered experiments (detection, ablation, second robot, feedback cycles, robustness) against independent baselines, and decide on the evidence whether physics residuals, calibrated uncertainty and augmentation enter the product (M12).

The technological uncertainties these objectives resolve are what make the project de-risking rather than engineering. (a) General quantified first-order logic is not decidable: "no contradiction found" is not a consistency proof, so the compiled SMT subset must be shown to preserve the meaning of the approved first-order constraints, and UNKNOWN, timeout, unsupported construct and missing input must be first-class outputs rather than silent passes. (b) A physical residual such as r_t = ‖M(q)q̈ + C(q,q̇) + g(q) − τ − Jᵀf‖ needs synchronized states, torque and contact signals, calibration and declared units; whether PINN or neural-operator proxies [24] reduce cost without hiding out-of-domain error is untested. (c) Conformal prediction [25] gives population coverage under stated assumptions, not a safety probability for one trajectory; the right target, grouping by episode and abstention policy are open. (d) A generator and its checker may share blind spots, so augmentation must be validated on held-out real views, measured contacts and unseen layouts. (e) Whether semantic checks detect error classes that simple rules miss at equal cost, and whether task mappings transfer across accounts and across a hospital-floor and a factory-floor setting without redesign, are commercial questions only pre-registered experiments can answer. Each is kept as a falsifier: a negative result narrows scope before further capital is committed.

## 5. Work plan: themes, projects and milestones

Kernel modules are designed with the ontology lifecycle methodology of Grüninger and Fox [26] and the COLORE repository techniques [27]: competency questions come from the checks customers need; every module is verified — its models characterized and compared with the intended models — before it is compiled. Verification (do the axioms have the intended models?) is kept distinct from validation (are the intended models the right ones for the customer's task?). Roles: **CEO** (founder, ontology and product), **CTO** (AI and engineering), **RL** (robotics lead), **AL** (3D asset lead), **ENG1** [Ontario engineering hire], **UofT** [Semantic Technologies Laboratory as contractor under a research agreement — to confirm].

### Theme 1 — Kernel: the specification (months 1–4)

*Given a robot episode, which assertions about objects, parts, contacts and task phases must hold, and which axioms decide it?*

**Project 1.1 Parts and articulation module.** Axiomatize rigid, articulated, functional and assembly parts as a modular extension of TUpper's mereotopology, with PSL fluents for state change under manipulation (open, close, grasp, place). Verify consistency and non-triviality with Prover9/Mace4; prove representation theorems relating the module to the annotation schemas of PartNet, PartNet-Mobility and GAPartNet so that cross-dataset label mappings are meaning-preserving by proof, using the constitution-mapping result of [5].
- Open question: Which parthood relations are implicit in PartNet-style decompositions, and do they require distinct axiomatizations (mereological pluralism [6])? **CEO, UofT** — M3.
- Open question: Does the axiomatization of articulated objects require the process module, or can it be stated in a static mereotopology? **CEO** — M3.

**Project 1.2 Robotics domain module.** Embodiment, kinematic chains, contextual affordances (a graspability claim depends on gripper, pose, load and environment), contact events and bounded safety conditions, with declared units, frames, handedness and rotation order bound before any spatial relation is derived.
- Open question: Which affordance claims are definable from geometry plus embodiment alone, and which need observed contact evidence? **RL** — M3.

**Project 1.3 Compilation and regression.** Compile approved constraints to the SMT subset; validate translation and combined modules; regression-test changed conclusions on prior datasets; save exact inputs, outputs, tool versions and resource limits with every run.
- Open question: For which constraint families is the compiled check complete with respect to the first-order module, and where must UNKNOWN be returned? **CTO, ENG1** — M3 (kernel v1 tagged and frozen).

### Theme 2 — Engine: checking at dataset scale (months 3–8)

*Can 10,000 heterogeneous episodes be grounded and checked with localized findings, unknowns and review decisions, without inventing a physical fact where evidence is missing?*

**Project 2.1 Adapters and the episode contract.** Extend the connectors to a common episode contract — episode_id, asset_ids, robot configuration, sensor references, timestamps, frame tree, calibration, state/action schema, task phases, contact events, outcome, interventions, rights, real/synthetic lineage. Original recordings stay immutable; conversion is an explicit, versioned operation; support is reported by adapter version. **CTO, ENG1, AL** — M4.

**Project 2.2 Grounding with abstention.** Vision-language and graph models propose identities, affordances and relations with per-candidate confidence; type, timing, geometry and task checks constrain them; a contradiction creates a localized finding and missing friction or contact evidence produces an unknown. Confirmed corrections become regression cases.
- Open question: What fraction of frames can be grounded automatically at a fixed audited accuracy, and which unknown types dominate the residual? **CTO** — M6.

**Project 2.3 Two-tier checking and dispositions.** Bulk checks in the compiled subset; residual hard cases to first-order proving. Every record receives a disposition — valid success, valid failure (retained with its failure phase), correctable defect (new derived version, original retained), unresolved (review with exact missing evidence), unsupported synthetic (excluded from the approved split). A sample of passed records is audited as well as the review queue, so that systematic false accepts cannot stay invisible.
- Open question: What is the parthood- and contact-consistency violation rate in the open corpora and in partner data, by dataset and by axiom family? **CEO, ENG1** — M6 (10,000 verified episodes).

**Project 2.4 Regulated-health design-partner track.** With [the hospital network / a medical-device company from the company's existing relationships — name and confirm], scope one bounded task family in a health setting (for example, a hospital logistics or service robot's episodes, or a device-mounted manipulation task [to be agreed with the partner]), agree the input contract, rights and consent fields (privacy scope: PIPEDA and provincial health-information rules [counsel to confirm]), and run the Engine on the partner's data under the partner's own acceptance test. The checks are the same kernel; what changes is the evidence interface — quality-system records, validation evidence and per-record lineage — and the severity taxonomy. This track makes the Passport's "requirements-to-evidence mapping" concrete for a regulated product before Annex I applies.
- Open question: Does a task mapping built on home and factory scenes transfer to a hospital floor without redesign, and which unknown types are new there? **CEO, RL** — M8.

**Project 2.5 Physics residuals (expansion gate).** Observation contract and layered checks (geometry: scale, extent, penetration, transforms, reachability; kinematics: position, velocity, acceleration, timing; dynamics where torque and contact signals exist), calibrated on held-out measurements with proxy error and out-of-domain behaviour reported.
- Open question: Does a calibrated surrogate reduce checking cost at the same false-accept rate as the analytic residual? **RL** — M8.

### Theme 3 — Passport, validation and feedback (months 6–12)

*Can a conclusion travel with the data, method, version and review history so that a recipient reruns the check, and does the loop lower the cost of the next batch?*

**Project 3.1 Passport v1.** Identity and rights (dataset/episode IDs, source type, permitted use, content hashes, versions); scope and method (robot, task, calibration context, kernel, software, thresholds, limitations); findings and reproducibility (per-check results, evidence pointers, repairs, reviewer decisions, runnable specifications or proof/model artifacts); issuer and integrity (signature, signing policy, package hash). Every percentage carries a denominator, record counts and calibration provenance. A Passport supports a specific review; it is not a blanket certificate of compliance or safety. Submit Passport v1 to [assessment body / standards organization] for written evaluation. **CEO, CTO** — M9.

**Project 3.2 Pre-registered validation experiments.** With the two design partners and against customer scripts, simple rules, VLM-plus-rules and the existing stack at matched model, compute and data budget: detection (false accepts/rejects, review time); ablation (remove ontology, physics, uncertainty separately); training (raw, conventional filter, Engine, Engine plus augmentation → real success, interventions, failures); second robot (all adaptation hours recorded, retained performance); robustness (shift, missing fields, corruption, timeout → coverage and correct abstention). Rooms, objects, sessions and time are held out before tuning; confidence intervals are reported; negative results are preserved.
- Open question: Which error classes do semantic checks detect that simple rules miss, and at what cost? **CTO, RL** — M12.
- Open question: Does a second embodiment reuse task mappings with materially fewer adaptation hours? **RL** — M12.

**Project 3.3 Feedback, augmentation and the training interface.** Classify confirmed findings (observation error, missing metadata, task-definition error, model limit, real robot failure) and route each to an adapter fix, calibration, rule, concept or measurement request; generate controlled variants around coverage gaps with generator version, seed and real/synthetic proportion recorded, validated on independent real evidence; expose the kernel's named vocabulary through a soft-constraint interface L = L_task + λ·L_logic and validate the soft/hard bridge separately.
- Open question: Does later-batch detection improve at a fixed error tolerance, net of rule-maintenance cost? **CEO, ENG1** — M12.
- Open question: Does ontology-consistent augmentation improve generalization to unseen object categories in SAPIEN [21] [and a second simulator] under a fixed budget? **CTO** — M12 (research option; enters the product only on measured benefit).

### Milestones

| Milestone | Month | Deliverable and acceptance |
|---|---|---|
| M3 | 3 | Kernel v1 frozen: verified modules, compiled subset, regression suite; vertical slice on one supported task and connector with a blind baseline and a reproducible evidence package |
| M6 | 6 | Engine v1: 10,000 verified episodes across partner data and open datasets; audit report with violation rates by dataset and axiom family; adapters for [four] formats |
| M8 | 8 | Regulated-health track: partner data run under the partner's acceptance test; physics-residual gate decision |
| M9 | 9 | Passport v1 shipped; written evaluation from [assessment body / standards organization] |
| M12 | 12 | Validation experiments reported; two design-partner acceptances (one health setting) against independent baselines; augmentation and uncertainty gate decisions; roadmap for months 13–18 |

## 6. Business plan

**Buyers and offer.** First buyers own a recurring data decision: model developers (robot-learning lead: batch acceptance and diagnostics), robot OEMs (autonomy/quality lead: failure-linked regression evidence), data suppliers (data operations: repeatable customer acceptance) and industrial integrators (engineering/quality: application-specific test evidence). In the regulated-health segment the same offer is bought by [medical-device and hospital-robotics teams — confirm with the existing relationships] for validation evidence and per-record lineage. Qualified entry requires a named task family, a next training or release date, recurring batches and a measurable review bottleneck. The commercial offer is a pilot at USD 25–50K for 8–12 weeks on one task family with fixed data and acceptance, converting to an annual deployment at USD 120–240K with supported integrations, recurring checks and support. A sizing cohort of ten pilots and four annual conversions implies USD 250–500K in pilot bookings and USD 480–960K in annual recurring fees before credits. Customer ROI is stated conservatively: an illustrative 600 review-hours-per-month baseline at USD 150/hour with a hypothesized 40% reduction releases USD 432K of annual capacity against a USD 180K first-year purchase, before the customer's own integration and compute costs.

**Market.** Counting eligible purchasing organizations rather than robot shipments, a focused pool of 80–200 US and Canadian organizations at USD 150–300K gives USD 12–60M annually, with platform paths to USD 100M ARR (500 customers at USD 200K or 200 at USD 500K). External budgets are committed: the data-annotation and training-data market is forecast to grow from USD 4.9B (2025) to USD 17.1B (2030); world-model companies and field deployments each add streams of data that nobody has verified for physical and logical consistency.

**Competitive position.** Complementary to collection, simulation and tooling vendors; the direct alternatives — runtime safety filters, safety-case evidence tools, internal pipelines and KnowRob-style ontologies — lack an axiom set machine-proven consistent, per-record evidence that re-verifies offline, and one kernel for guardrails and evidence. The wedge is cross-stack task semantics, localized check results and reproducible evidence inside the buyer's existing workflow; defensibility accumulates in validated task mappings, permitted failure taxonomies, adapters, regression cases and recurring release integration, not in public standards or solvers alone. Functional-safety layers (NVIDIA Halos and accredited labs) sit below; semantic guardrails sit above them at the task level and remain a separately gated product.

**Plan and gates (18 months, from the operating plan).** Months 0–3: vertical slice, two paid validation engagements. Months 4–9: repeat delivery, three cumulative paying customers, positive delivery contribution on two. Months 10–18: second task or embodiment, reusable mappings, five cumulative customers and two renewals or expansions. Dated targets already set: three co-development partners signed and 10,000 verified episodes by Q1 2027; Passport v1 recognized by one assessment body or standards organization by Q2 2027; five paying customers and two renewals by month 18. Decision rule: pre-register the comparison, preserve negative results, and prefer the simpler method that achieves the customer outcome.

**Capital.** Financing is sized to the 18-month plan with a buffer for delayed collection [round size and status to state]. The CTI match — from TIAP or a third-party investor — is the natural first instrument of that round [cap-table review with existing shareholders to record]. Non-dilutive routes pursued in parallel and kept non-overlapping in scope: NRC IRAP (Engine and adapters), SR&ED (net of assistance), Mitacs (U of T-side kernel verification) [each to confirm].

## 7. Use of funds and what TIAP support de-risks

The CTI text names three things the grant supports: IP management, company creation and technology de-risking. Each applies here.

- **Technology de-risking (grant, up to CAD 100K).** Engine hardening after the Q4 2026 internal test; adapters; the 10,000-episode audit; Passport v1 and its external evaluation; the regulated-health partner run. The funded milestones retire the stated uncertainties in order (M3 completeness of the compiled check; M6 grounding accuracy and violation rates; M8 transfer to a hospital setting; M9 external acceptance of the evidence format; M12 measured value over simpler baselines). Detailed lines are in budget_and_timeline.md.
- **IP management.** The IPO determination and licence for U of T-derived elements of the kernel; the assignment or licence of the Uing-held patents to the applicant entity; a written IP-ownership map that separates customer datasets and confidential findings from reusable adapters, task schemas and background technology. TIAP's IP and venture-building services are the reason to bring this to TIAP rather than only to a grant agency.
- **Company creation.** [If the Ontario entity is new: incorporation, shareholder agreements, the match instrument, and executive-advisory support for a founder whose prior ventures were in consumer commerce rather than regulated B2B software.]
- **Commercial execution (match, up to CAD 100K).** Design-partner delivery cost, acceptance and collections for the first paid cohort, and the executive-advisory line.

## 8. Team

Founder/CEO — Dr. Yi Ru: PhD in Information Engineering, University of Toronto (requirements completed March 2025), on an architecture in which a verified ontology governs the data, model and simulation layers of an AI system; core contributor to ISO/IEC 21838-4:2023; 21 papers disclosed, FOIS outstanding-paper award, invited AAAI presentation, an English-language monograph [titles and roles to confirm]; currently a postdoctoral researcher at Harvard Medical School [laboratory; one sentence on the work]; founding team member of MICAS (USD 5M raised including Accel Partners; >USD 50M annual revenue in year one; 100+ team; built CRM/ERP/WMS and ML-driven marketing) and co-founder of YourTable Inc. (U of T, Schulich and Imperial College incubation); co-founder and CEO of Uing Technologies (2022–), whose spatial stack produced the 100,000 asset packages and nine invention applications. CTO — McMaster University AI doctorate; applied AI leadership. Robotics lead — mechanical/electronic engineering doctorate; autonomous-system perception. Senior 3D asset lead — more than ten years of production experience. Academic linkage — Prof. Michael Grüninger, Semantic Technologies Laboratory, U of T MIE (COLORE, PSL, TUpper) [role: letter of support; contractor under a research agreement — to confirm]. Full bios are in statement.md.

## 9. Impact for Ontario and for the member institution

The project places the company's core IP development (kernel, adapters, evidence schema) in Ontario with [N] R&D positions including ENG1; gives Canadian robotics and manufacturing companies (the deck cites Sanctuary/Magna and Vention as deployment contexts) and Canadian data suppliers a repeatable acceptance product to sell into US and EU markets ahead of the Annex I date; and returns to the University of Toronto a commercial application of a standard and a theory developed there, with verified modules contributed to the open COLORE repository and a standards route through ISO/IEC JTC 1/SC 42. The audit methodology generalizes beyond robotics to medical-image part labels, CAD assemblies and building information models — the first of which is the bridge to TIAP's health-science portfolio and to the hospital and medical-device relationships the company already holds.

---

## Bibliography

[1] ISO/IEC 21838-4:2023. Information technology — Top-level ontologies (TLO) — Part 4: TUpper. ISO/IEC JTC 1/SC 42.
[2] ISO/IEC 24707:2018. Information technology — Common Logic (CL): a framework for a family of logic-based languages.
[3] W. McCune. Prover9 and Mace4. Software and documentation, 2005–2010.
[4] L. de Moura and N. Bjørner. Z3: An efficient SMT solver. TACAS 2008.
[5] Y. Ru and M. Grüninger. Material constitution as a parthood-preserving mapping between mereologies. Submitted to Synthese, 2026.
[6] Y. Ru and M. Grüninger. [Exact title — mereological pluralism validation]. Submitted to Synthese, 2026.
[7] LeRobot dataset format v3. Hugging Face, documentation.
[8] RLDS: Reinforcement Learning Datasets. Google DeepMind, documentation.
[9] DreamVu. Robot Training Data Companies: The 2026 Landscape. August 2026.
[10] SCSP / ISF Voices 2026. The Robotics Data Gap.
[11] Open X-Embodiment Collaboration. Open X-Embodiment: Robotic learning datasets and RT-X models. 2023.
[12] A. Khazatsky et al. DROID: A large-scale in-the-wild robot manipulation dataset. 2024.
[13] AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. 2025.
[14] F. Lin et al. Data scaling laws in imitation learning for robotic manipulation. 2024.
[15] Regulation (EU) 2024/1689 (Artificial Intelligence Act), as amended by Regulation (EU) 2026/1744; Annex I obligations for AI in machinery and other regulated products apply from 2 August 2028.
[16] NIST. Artificial Intelligence Risk Management Framework (AI RMF 1.0), January 2023.
[17] M. Beetz et al. KnowRob 2.0 — A 2nd generation knowledge processing framework for cognition-enabled robotic agents. ICRA 2018.
[18] S. Badreddine, A. d'Avila Garcez, L. Serafini, M. Spranger. Logic Tensor Networks. Artificial Intelligence 303, 2022.
[19] R. Manhaeve et al. DeepProbLog: Neural probabilistic logic programming. NeurIPS 2018.
[20] K. Mo et al. PartNet: A large-scale benchmark for fine-grained and hierarchical part-level 3D object understanding. CVPR 2019.
[21] F. Xiang et al. SAPIEN: A simulated part-based interactive environment. CVPR 2020.
[22] H. Geng et al. GAPartNet: Cross-category domain-generalizable object perception and manipulation via generalizable and actionable parts. CVPR 2023.
[23] ISO 18629 (parts 1, 11–14, 41–44). Industrial automation systems and integration — Process specification language.
[24] Z. Li et al. Fourier neural operator for parametric partial differential equations. arXiv:2010.08895, 2020.
[25] A. N. Angelopoulos and S. Bates. A gentle introduction to conformal prediction and distribution-free uncertainty quantification. arXiv:2107.07511, 2021.
[26] M. Grüninger and M. S. Fox. Methodology for the design and evaluation of ontologies. IJCAI-95 Workshop on Basic Ontological Issues in Knowledge Sharing, 1995.
[27] M. Grüninger, T. Hahmann, A. Hashemi, D. Ong, A. Özgövde. Modular first-order ontologies via repositories. Applied Ontology 7(2), 2012.
