# Activate Fellowship — U.S. Cohort 2027 — application narrative

**Principal applicant:** Dr. Yi Ru, Founder/CEO, AXIOMALITY · **Co-applicant (optional):** [CTO name — decide] · **Cohort preference:** [Boston / Anywhere — decide by 2 Oct 2026] · **Venture:** AXIOMALITY [legal name, jurisdiction, incorporation date — confirm]

Activate does not publish headings or page limits; it says the application must "clearly demonstrate" nine things (activate.org/apply). The nine sections below answer those nine things in order, each sized for a form box (150–450 words). When the SMApply form is open, paste each section into the matching field and trim to its character limit. Citations are numbered; the bibliography is at the end. SMApply boxes will not carry a bibliography: when pasting, replace each [n] with a short inline reference (standard number, dataset name, "company deck, Sept 2026") or drop it. Nothing in [brackets] may be submitted unresolved.

---

## 1. Scientific and engineering basis of the technology

In plain terms: a robot learns from recordings of objects being handled, and every recording describes those objects as assemblies of parts — a drawer in a cabinet, a lid on a mug. Today nobody checks that those descriptions are internally consistent or that they mean the same thing from one dataset to the next. AXIOMALITY's technology is a checker that does this against a written specification of what "part", "contact" or "task phase" means — an ontology — where the specification itself has been machine-proven free of contradiction, and where every check on a dataset or a robot deployment returns a proof, a counter-example, or an explicit UNKNOWN.

The stack has four ontology layers. The foundational layer is TUpper, the top-level ontology standardized as ISO/IEC 21838-4:2023 [1], to which I was a core contributor. Above it sits a physical-world layer (parts, shape, measurement, materials, change, process), a robotics-domain layer (embodiment, kinematic chains, affordances, contacts, task phases, safety conditions), and a dataset-instance layer (episodes, frames, sensors). The theory of parts that governs the physical-world layer was developed by me with Prof. Michael Grüninger (University of Toronto): material constitution formalized as a parthood-preserving mapping between mereologies, and a validated mereological pluralism [2, 3]. That theory states exactly what must hold for two part decompositions of the same object — kinematic, functional, visual — to be compatible. It is the question every pooled robot dataset raises and none answers.

Verification follows the COLORE methodology developed in the Semantic Technologies Laboratory at the University of Toronto [4]: ontology modules are written in Common Logic (ISO 24707) [5]; consistency, non-triviality and the relationships between modules are established with the Prover9 theorem prover and the Mace4 model finder; representation theorems relate the ontology to each dataset's annotation schema so that cross-dataset label mappings are meaning-preserving by proof, not by convention. State change under manipulation is represented with the Process Specification Language ontology [6]. For dataset-scale checking, a compiled subset of the axioms runs as SMT and task-checking rules; the residual hard cases go to the theorem prover; timeouts are reported as UNKNOWN rather than silently passed.

The physical grounding is explicit. Each ingested episode is reconstructed as a scene graph and checked against physics residuals under an observation contract that states what the sensors could have seen; conformal, calibrated uncertainty controls when the Engine abstains. Adapters read the formats robot data arrives in (LeRobot, RLDS, ROS 2/MCAP, OpenUSD, PLY, JSON).

What is new is not any one component but the combination: robot-learning data checked against a machine-verified specification whose axioms are traceable to an international standard, with the check itself reproducible and auditable. [Insert one sentence on the principal theorem of [2] in plain language.]

## 2. The problem the technology addresses

Physical AI is being trained on a small number of large part-level datasets — PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, and real-robot corpora such as AgiBot World, Open X-Embodiment and DROID [7–12]. Each annotates objects as hierarchies of parts with kinematic, functional and visual labels, and each defines "part" operationally: a segmentation label in one, a movable link in another, an actionable region in a third. No dataset requires its annotations to satisfy the axioms of parthood, so a part may be recorded as both contained in and disjoint from another. No principled mapping exists between datasets, so pooled training silently mixes incompatible vocabularies. The consequences — poor transfer across part vocabularies, brittle generalization to new object categories — are observed throughout the field but have never been measured, because there has been no formal specification to measure against.

The economics make the problem urgent. Real-robot data available worldwide is on the order of 500,000 hours against an estimated need of 10 million; teleoperated collection costs USD 50–200 per hour [13]. As synthetic and world-model routes drive the price of raw hours toward zero, the value of a dataset migrates to what can be proven about it: its semantics, its consistency, its provenance. Buyers — model developers, robot OEMs, data suppliers and industrial integrators — have no instrument for that proof today; passported data is expected to command a 2–3× premium [13].

Regulation sets a clock. The EU AI Act's Annex I applies to AI in machinery and robots from 2 August 2028; in North America the NIST AI Risk Management Framework and the ANSI/A3 R15.06 and R15.08 robot-safety standards are the voluntary references buyers already use for risk records and application tests [14–16]. Every robot deployment will need a machine-checkable account of the data it learned from. AXIOMALITY builds that account.

## 3. Current development stage

The company is at the pre-product, pre-revenue stage that Activate targets [confirm: no product on general sale; revenue to date; total non-governmental funding raised < USD 2M].

Built and verified. The knowledge kernel — the four-layer ontology described in Section 1 — has its axioms machine-proven consistent and is aligned with ISO/IEC 21838-4. Kernel v1 is scoped to home scenes.

In test. The minimum offline verification Engine (ingestion → scene graph → SMT check → Passport) enters internal test in Q4 2026; physics residuals and conformal calibration follow in later gates. Connectors for LeRobot, RLDS and OpenUSD are under development; ROS 2/MCAP, PLY and JSON adapters are specified. [By 23 Oct 2026: insert the first internal-test result — dataset, number of episodes ingested, proportion flagged, proportion UNKNOWN, wall-clock per episode — or state that the test is scheduled for [date].]

Designed. The data Passport — a reproducible per-release evidence pack — whose audit-pack structure has been reviewed with a Big Four accounting firm and an international law firm [confirm that these engagements may be described; names only with permission]. Runtime semantic guardrails for deployed robots are specified as a separately gated product.

Assets. 100,000 measured 3D asset packages (JPG, USDZ, PLY, JSON oriented boxes) from room-level reconstruction and object-level annotation, which serve as ground truth for the physical-world layer; a consumer spatial application built on the same reconstruction pipeline is live on the Apple Vision Pro App Store (Uing Technologies) [confirm relationship of Uing's assets to AXIOMALITY's ownership].

Commercial discussions. Humanoid OEM and platform discussions in progress [confirm; do not name without permission]; relationships with multinational medical-device and pharma companies, national standards bodies and a large hospital network from prior work [confirm which may be referenced].

## 4. Evidence that the technology works

The evidence is of three kinds, in decreasing order of formality.

Theorems. The kernel's consistency and module relationships are established by Prover9 proofs and Mace4 models under the COLORE methodology of the laboratory in which TUpper (ISO/IEC 21838-4:2023) was developed [1, 4]. The theory of parts underlying the physical-world layer is under peer review at Synthese [2, 3]; its central results are stated as first-order theorems [confirm whether the proofs in [2, 3] are machine-checked or hand proofs, and say which].

Production. The spatial-computing stack (room-level reconstruction, object-level 3D annotation) behind the 100,000 measured asset packages also powers a shipped consumer application on Apple Vision Pro (mesh object recognition, 3D spatial mapping, autonomous path planning). Before that, at MICAS, I built the CRM/ERP/WMS and ML-driven marketing systems of a cross-border platform that reached more than USD 50M in annual revenue and one million followers and customers in more than 100 countries within a year of launch; at YourTable I built a personalized recommendation system.

Engine runs. [Insert internal-test numbers when available (see Section 3). If none are available by submission, state: "The first internal test on [dataset] is scheduled for [date]; results will be available before interviews."]

What is not yet shown. The Engine has not yet run on a customer's data against an independent baseline. That is the company's next evidence gate — first paid design partners, with acceptance judged against a blind baseline — and the Q4-2026 internal test is its precondition. I state this plainly because the fellowship's first months are where that gate is passed.

The intellectual-property position is 13 granted patents and 9 pending invention applications in 3D recognition, indoor modelling, automatic reconstruction, emotion sensing and adaptive feedback [confirm assignee; reconcile with the CV's count of 3 Chinese invention patents and 9–10 German utility patents; list numbers on the CV].

## 5. Potential impact

For robotics. A data Passport turns a robot dataset from a file into an auditable object: each release carries a reproducible evidence pack stating which axioms it satisfies, which it violates, and where the Engine abstained. Model developers can pool data across vocabularies with proven mappings; OEMs can show deployers what their robots learned from; data suppliers can sell verified hours at a premium instead of raw hours at a discount. The first quantitative audit of parthood consistency across the major public datasets — a by-product of building the Engine — will be released publicly, and the parts ontology itself will be contributed under an open licence to the COLORE repository and to ISO/IEC JTC 1/SC 42, so that the specification the industry is measured against is not proprietary.

For safety and assurance. Verification-in-the-loop evaluation reports an ontology-violation rate alongside task success; a rising violation rate is an interpretable failure signal that a learned policy is losing its grip on object structure. That is the kind of evidence the EU AI Act's Annex I regime, NIST AI RMF and the ANSI/A3 robot-safety standards will require from 2028 [14–16].

Beyond robotics. Specification-based auditing of hierarchical annotations is a general method. The same toolkit applies to part labels in medical imaging, to CAD assemblies in manufacturing, and to building information models — domains in which I already have relationships through my Harvard Medical School appointment and through the company's medical-device and pharma contacts [confirm].

For the field of knowledge representation. AXIOMALITY is a demonstration that a verified ontology can be a product, not only a paper: the standard I helped write becomes the specification a market is measured against.

## 6. My technical expertise and experience

I hold a PhD in Information Engineering from the University of Toronto (Department of Mechanical and Industrial Engineering; all requirements completed March 2025, Fast Track PhD) and a BASc in Industrial Engineering from the same university (2015; President Scholarship; Dean's Honours List). My thesis developed an architecture for AI knowledge systems in which a verified formal ontology governs the data model, the learned models and the simulation layer; elements of it contributed to ISO/IEC 21838-4:2023 [1]. I am currently a postdoctoral researcher at Harvard Medical School [laboratory/department; one sentence on the work].

Formal methods. Core contributor to ISO/IEC 21838-4:2023 (TUpper) within ISO/IEC JTC 1/SC 42 [confirm role wording]. First author of two papers submitted to Synthese in 2026 with Prof. Michael Grüninger on material constitution and mereological pluralism [2, 3], for which I developed the theory and the proofs. 21 papers [confirm list]; Distinguished Paper Award, FOIS 2018 [confirm role]; invited AAAI presentation [confirm]; an English-language monograph [confirm title, publisher].

Systems. Co-founder and CEO of Uing Technologies (2022–present): structured 3D datasets and ontology-based representations of objects, indoor environments and interactions for embodied AI and AR; launched one of the first AR pet-interaction apps on the Apple Vision Pro App Store; led nine invention patent applications. Founding team, MICAS (2021–22): built CRM/ERP/WMS and ML-driven marketing systems for a cross-border platform that reached more than USD 50M in annual revenue with a 100+ person team and USD 5M of angel investment including Accel Partners. Co-founder, YourTable Inc. (2018–21): personalized recommendation; incubated by U of T, Schulich and Imperial College London. Named inventor on 13 granted patents [confirm first-inventor status and assignees; reconcile with the CV's counts].

Standards and community. Session Chair, IISE Annual Conference 2017; teaching assistant in Knowledge Modeling and Management and Database Systems at U of T; graduate-student leadership (Vice President, AMIGAS; MIE representative, Graduate Student Union).

## 7. My leadership role in the project

I founded AXIOMALITY and serve as its CEO [confirm title, start date, equity]. I conceived the product — the evidence loop Collect → Ground → Verify → Augment → Deliver → Learn — and I own three things personally: the knowledge kernel and its verification (I wrote the axioms and run their verification); the standards strategy (recognition of the Passport by an assessment body or standards organization, and contribution of the ontology to ISO/IEC JTC 1/SC 42, the committee to which I contributed 21838-4 [confirm current membership or liaison status]); and the first customers (design-partner and OEM conversations).

The team I lead: a CTO with an AI doctorate from McMaster University and applied-AI leadership experience [name; confirm as co-applicant]; a robotics lead with a doctorate in mechanical/electronic engineering and autonomous-system perception experience [name]; a senior 3D asset lead with more than ten years of production experience [name]. I have led teams of more than a hundred people before (MICAS) and know the difference between a research prototype and a product that survives its first customer.

Focus. I currently hold a postdoctoral appointment at Harvard Medical School and lead Uing Technologies (co-founded 2022). AXIOMALITY is [the same legal entity as Uing, renamed / a new entity that holds or licenses Uing's 3D assets and patents — confirm and state plainly]. If awarded, I commit full-time to AXIOMALITY for the fellowship's duration: the postdoctoral appointment ends before the cohort starts, and Uing's remaining activity [is folded into AXIOMALITY / is run day-to-day by [name] — confirm].

## 8. Plan for commercial development

Product sequence. (1) Offline Engine plus data Passport — the first commercial unit: a customer's dataset is ingested, reconstructed as scene graphs, checked, and returned with a versioned evidence pack. (2) Augment and Deliver — corrected annotations and provably meaning-preserving cross-dataset mappings, sold as ontology-aligned data releases. (3) Runtime semantic guardrails for deployed robots — a separately gated product, opened only after the offline Engine has paying customers.

Customers and pricing. Model developers, robot OEMs, data suppliers and industrial integrators in the U.S. and Canada. Entry is a paid pilot at USD 25–50k over 8–12 weeks — one task family, fixed data, one supported connector, acceptance against an independent blind baseline, a reproducible evidence package; conversion is to an annual deployment at USD 120–240k [13]. The bottom-up focused pool is estimated at USD 12–60M, with platform paths to USD 100M ARR [13].

Milestones (company plan, September 2026). Q4 2026: minimum Engine internal test; kernel v1 (home scenes); connectors. Q1 2027: three co-development partners signed; 10,000 verified episodes. Q2 2027: Passport v1 recognized by one assessment body or standards organization. Month 18: five paying customers, two renewals. The cohort starts mid-2027, after the Q4-2026 and Q1–Q2-2027 gates; those become the evidence base at interview, and the fellowship's 24 months carry the plan from first Passports to renewals (budget_and_timeline.md, part B).

Competition and defensibility. Direct alternatives are real-time safety filters (3Laws Supervisor), safety-case evidence management (reasonX SafetyScope), NVIDIA's data-factory blueprint, buyers' internal pipelines and KnowRob-style robot ontologies [13]. None checks per-record data against an axiom set machine-proven consistent, re-verifies offline, and uses one kernel for both evidence and guardrails. Collection vendors and world-model companies are channels, not competitors: their output needs the same verification. The kernel is anchored to a standard I helped write; 13 granted patents and 9 applications cover the reconstruction and recognition pipeline; 100,000 measured assets are ground truth competitors lack; and a Passport recognized by an assessment body becomes the reference other suppliers must meet.

Financing. An 18-month operating plan with capital sized to it; the company is seeking paid design partners, co-development partners, standards recognition, non-dilutive funding and a financing round [amount, instrument, timing — confirm]. Non-governmental funding raised to date: [amount — must be below USD 2M].

Regulatory and standards route. The Passport is designed to the evidence demands of EU AI Act Annex I (robots, from 2 Aug 2028), NIST AI RMF and ANSI/A3 R15.06/R15.08 [14–16]; recognition by one assessment body or standards organization is a Q2-2027 milestone.

## 9. Why the Activate Fellowship would significantly accelerate the project

Time. The fellowship's living stipend lets me work on AXIOMALITY full-time for two years without raising equity capital before the Engine has customers. Today the company's progress is gated by my time, which is split between a postdoctoral appointment and the venture; the plan's Q1–Q2 2027 milestones (three co-development partners, Passport recognition) are customer- and standards-facing work that only the founder can do.

Money with a purpose. The USD 100,000 in R&D support goes to the three things the technology needs that the team cannot supply from its own hands: robot time to validate physics residuals and the observation contract against real sensor streams rather than logged ones; compute for dataset-scale checking of the public corpora; and the assessment-body process for Passport recognition [see budget_and_timeline.md for the proposed allocation].

A host lab. In Boston, Activate's host-lab arrangement with its Harvard/MIT partners would give AXIOMALITY access to instrumented robot cells without owning them, at the moment when the Engine moves from logged data to live validation. [If Anywhere: name the facility already under the company's control and why it suffices.]

The network. AXIOMALITY's customers are robot OEMs and model developers, its validators are standards bodies, and its financing will come from investors who understand deep-tech timelines. Activate's fellows, mentors and investor community are exactly those people, and Activate's non-dilutive positioning matches the company's plan to reach five paying customers before a priced round.

Without the fellowship. The company would raise a priced round in 2027 before the Engine has customers, on a founder who is still part-time; the live-robot validation would wait for a customer to lend a cell. With it, the technical de-risking happens in the first six months on a host-lab robot, under my hands, before any raise.

What Activate gets. A founder who has already carried formal methods into an international standard and into shipped products, a technology whose correctness claims are theorems, and a company whose product is the evidence layer that every other physical-AI company in the portfolio will eventually need.

## Cohort preference and host-lab plan

[Decide by 2 Oct 2026. Boston: continuity with the Harvard appointment, host lab via Activate's Harvard/MIT partners, proximity to Boston-area robotics OEMs. Anywhere: requires a facility the founder already controls (name it) and still requires U.S. work authorization; whether an Anywhere fellow may reside outside the U.S. is unconfirmed — ask Activate (email 1). Berkeley / New York: not preferred; state why if the form asks.]

---

## Bibliography

[1] ISO/IEC 21838-4:2023. Information technology — Top-level ontologies (TLO) — Part 4: TUpper. ISO/IEC JTC 1/SC 42.
[2] Ru, Y., and Grüninger, M. (2026, submitted). Material Constitution as a Parthood-Preserving Mapping between Mereologies. Synthese.
[3] Ru, Y., and Grüninger, M. (2026, submitted). [Exact title of the mereological pluralism validation paper]. Synthese.
[4] Grüninger, M., et al. COLORE — Common Logic Ontology Repository, colore.oor.net (2,580+ first-order ontologies). [Insert the canonical citation Prof. Grüninger uses.]
[5] ISO/IEC 24707 (2017 edition, as cited in Prof. Grüninger's proposals). Information technology — Common Logic (CL). [Confirm edition and full title.]
[6] Grüninger, M. The Process Specification Language (PSL) ontology. [Insert canonical citation; ISO 18629 — confirm.]
[7] PartNet. [Insert full citation.]
[8] PartNet-Mobility / SAPIEN. [Insert full citation.]
[9] GAPartNet. [Insert full citation.]
[10] AgiBot World. [Insert full citation.]
[11] Open X-Embodiment. [Insert full citation.]
[12] DROID. [Insert full citation.]
[13] AXIOMALITY. Engineering the Evidence Layer — U.S./Canada company deck, September 2026 (market sizing, pricing and data-supply estimates; internal).
[14] EU Artificial Intelligence Act, Annex I — application to AI in machinery and robots from 2 August 2028 (company brief). [Insert regulation number and article reference — confirm.]
[15] NIST AI 100-1. Artificial Intelligence Risk Management Framework (AI RMF 1.0). [Confirm.]
[16] ANSI/A3 R15.06 and R15.08 (industrial robot and mobile robot safety). [Confirm editions.]
[17] McCune, W. Prover9 and Mace4. [Insert citation.]
