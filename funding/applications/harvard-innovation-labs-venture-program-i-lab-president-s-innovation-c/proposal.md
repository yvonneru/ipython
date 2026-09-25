# AXIOMALITY — Venture Program and President's Innovation Challenge 2027 application text

Written for the i-lab Venture Program form and the PIC written application. Neither form publishes its questions or character limits in advance [record them from the live form and trim each section to fit]. Sections §1–§10 are the venture application, written for a general audience with the evidence up front, as the i-lab's PIC guidance asks. The Technical Annex is for judges who want the mechanism and for the deck's appendix; it follows the Grüninger proposal structure. Track: **Open** [decision by 1 Nov 2026]. Items in [brackets] must be confirmed or supplied by the applicant; nothing in brackets may be submitted as written.

---

## 1. Venture summary

AXIOMALITY builds the evidence layer for robot-learning data. Robots are now trained on data — teleoperated demonstrations, simulation, world-model rollouts — and nobody can currently prove what that data says about the physical world: whether the parts of an object are labelled consistently, whether a contact or a joint motion is physically possible, whether two datasets mean the same thing by the same word. Our offline **Engine** ingests a dataset, builds a scene graph of objects, parts, contacts and task phases, and checks it against a machine-proven ontology with automated reasoning. Our **Data Passport** packages the result as a reproducible, per-release evidence pack that a customer, an auditor or a regulator can re-run. The company was founded in 2026 by Dr. Yi Ru (PhD, University of Toronto; core contributor to ISO/IEC 21838-4, the international standard for the TUpper top-level ontology; postdoctoral researcher at Harvard Medical School) [confirm legal entity, jurisdiction and date; relationship to Uing Technologies, founded August 2022]. We are pre-revenue [confirm], in internal test of the minimum Engine (Q4 2026), and in co-development discussions with humanoid-robot OEMs and data platforms [names and status — confirm]. We are applying to the Venture Program for the spring-2027 cohort and to the PIC Open track.

## 2. The problem

Physical AI is data-limited and the data cannot be trusted. Roughly 500,000 hours of real-robot data exist worldwide against an industry estimate of 10 million needed; teleoperated collection cost USD 50–200 per hour in 2024 and about USD 140 per hour at 2025 data-factory pricing [deck pp. 4–6, citing DreamVu (Aug 2026), SCSP / ISF Voices 2026 — confirm]. Every route to more data (teleoperation, simulation, world models) produces annotations — parts, joints, affordances, contacts, task phases — with no shared definition and no consistency requirement. In the public corpora that current models are trained on (PartNet, PartNet-Mobility, GAPartNet, Open X-Embodiment, DROID, AgiBot World), a "part" is a segmentation label in one dataset, a movable link in another, an actionable region in a third; a part can be annotated as both inside and disjoint from another; and pooled training silently mixes incompatible vocabularies. The consequences are visible to every model developer — poor transfer across part vocabularies, brittle generalization to new object categories, failures diagnosed by inspection rather than by principle — and were confirmed in our own field interviews with model developers, OEMs and data suppliers [number, dates; the deck cites "AXIOMALITY field interviews"]; but they have never been measured, because there has been no formal specification to measure against. The cost is paid three times: in data bought and discarded, in models retrained, and in deployments that cannot be certified. From 2 August 2028 the EU AI Act (Annex I, machinery and robots) will require documented evidence about training data for high-risk systems; NIST's AI Risk Management Framework and the ANSI/A3 R15.06 and R15.08 robot-safety standards point the same way. The buyers — model developers, robot OEMs, data suppliers, industrial integrators — have no tool that turns a dataset into evidence.

## 3. The solution

We turn a robot dataset into a machine-checkable claim about the world, and ship the proof with the data.

- **Engine (offline verification).** Reads the common robot-data formats (LeRobot, RLDS, ROS 2/MCAP, OpenUSD/USDZ, PLY, JSON), builds a scene graph — objects, parts, joints, contacts, task phases, safety conditions — and checks it against a library of rules about the physical world whose consistency has itself been machine-proven and which extends the international standard ISO/IEC 21838-4. Bulk checks run on an automated solver at the scale of millions of records; the hard residual cases go to a theorem prover, which returns a proof or a concrete counter-example. When the sensor evidence is too uncertain to decide, the Engine says so: "unknown" is a first-class result, and the Engine never claims more than it proved.
- **Data Passport.** A versioned evidence pack per data release: the rules applied, the checks run, the violations found and corrected, the counter-examples for anything rejected, and the residual uncertainty — all reproducible by re-running the pack. The audit-pack design has been reviewed with a Big Four accounting firm and an international law firm [names; confirm they may be cited].
- **Evidence loop.** Collect → Ground → Verify → Augment → Deliver → Learn: verified data feeds training and training failures feed back into the checks, for every data-generation route (teleoperation, simulation, world models).
- **Runtime semantic guardrails** — the same rules applied to a running robot — are a separately gated later product.

What is new is not the scene graph or the theorem prover; it is that the rules being checked are themselves proven consistent and aligned with an international standard, so a Passport is evidence in the ordinary sense: an independent party can re-derive it. The mechanism is in the Technical Annex.

## 4. Market and why now

Value in robot data is migrating from raw hours to semantics, verification and certification. Raw hours are trending toward zero as simulation and world models scale; the scarce good is knowing which hours are physically and semantically correct. Our bottom-up estimate is a focused pool of USD 12–60 million a year — 80–200 organizations paying USD 150–300k each — among model developers, OEMs, data suppliers and integrators in the US and Canada, with platform paths to USD 100 million ARR (200 customers at USD 500k, or 500 at USD 200k) as certified data exchange becomes the norm [deck pp. 43–45; source the organization count]. Vendors already price verified, certifiable data at 2–3× raw hours [deck market slide, citing State of Robotics 2026 and DreamVu (Aug 2026) — confirm]. Three forces make 2027 the year: (1) humanoid and mobile-manipulation programs have moved from research to procurement and are buying data at scale; (2) the EU AI Act Annex I compliance date of 2 August 2028 gives every OEM selling into Europe an 18-month clock to assemble training-data evidence; (3) the standards infrastructure for machine-checkable evidence now exists — ISO/IEC 21838 top-level ontologies (2021–2023), Common Logic (ISO/IEC 24707) — and we helped write it.

## 5. Traction and stage

[Every line to be confirmed and, where possible, backed by a document in the deck appendix; delete any line that cannot be evidenced by 15 Nov 2026.]

- Product: minimum verification Engine in internal test, Q4 2026 (ingestion → scene graph → SMT check → Passport); knowledge kernel v1 for home scenes; Engine connectors for LeRobot, RLDS and OpenUSD in the test build (ROS 2/MCAP, PLY and JSON adapters follow [status]). Internal-test numbers — episodes processed, violation rate by axiom family, throughput per 1,000 episodes — [insert by 15 Nov 2026 or omit].
- Customer discovery: field interviews with model developers, OEMs and data suppliers [number, dates, roles — the deck cites "AXIOMALITY field interviews"].
- Partners: co-development discussions with [humanoid OEM(s)] and [data platform(s)]; target of three signed co-development partners and 10,000 verified episodes by Q1 2027.
- Assets: 100,000 measured 3D asset packages (JPG, USDZ, PLY, JSON oriented boxes) from room-level reconstruction and object-level annotation; a consumer spatial application live on the Apple Vision Pro App Store (one of the first AR pet-interaction apps: mesh object recognition, 3D spatial mapping, autonomous path planning).
- IP: 13 granted patents and 9 invention applications in 3D recognition, indoor modelling and automatic reconstruction [numbers; reconcile with the CPRA draft's counts]; knowledge kernel of axioms machine-proven consistent and aligned with ISO/IEC 21838-4.
- Assurance: audit-pack design reviewed with a Big Four accounting firm and an international law firm [names].
- Relationships: multinational medical-device and pharma companies, national standards bodies, a large hospital network [names; nature of each relationship].
- Funding: [funds raised to date; instrument; investors — confirm; if none, state "bootstrapped" and the planned round].
- Revenue: [revenue to date — confirm; if pre-revenue, say so and give pilot pipeline value].

## 6. Business model

We sell verification, then certification, then exchange.

- **Pilot:** USD 25,000–50,000 for an 8–12-week engagement — one customer dataset through the Engine, a Passport, and a written findings report.
- **Annual deployment:** USD 120,000–240,000 per year for continuous verification of a customer's data releases, with Passports per release; implementation scoped separately. A sizing cohort of 10 pilots with four annual conversions implies USD 250–500k in pilot bookings.
- **Passported data premium:** suppliers who ship data with a Passport price it at 2–3× raw hours; we take [share — confirm] on exchange transactions in the later platform phase.
- **Gates (18-month operating plan):** Q1 2027 — three co-development partners, 10,000 verified episodes; Q2 2027 — Passport v1 recognized by one assessment body or standards organization; month 18 — five paying customers, two renewals. Capital is sized to this plan [amount — confirm].
- **Unit economics:** [gross margin on a pilot; Engine compute cost per 1,000 episodes; sales cycle length — to add from the operating model].

## 7. Competition and defensibility

Alternatives are (a) in-house data QA scripts at model developers, which check format and statistics but not meaning; (b) data-labelling vendors, who produce annotations but do not verify them against any specification; (c) simulation vendors, whose data is consistent by construction with their own simulator but not with anyone else's; and (d) emerging AI-assurance consultancies, which audit processes rather than data. Named alternatives in our competitive map are 3Laws Supervisor (a real-time safety filter), reasonX SafetyScope (safety-case evidence management), NVIDIA's data-factory blueprint, and KnowRob-style robot ontologies; NVIDIA Halos for Robotics is a functional-safety layer beneath ours, not a competitor. None produces reproducible, machine-checkable evidence that a third party can re-derive. Our defensibility rests on three things that take years to build: the verified ontology kernel and its lineage in an international standard the founder helped write; the adapter and physics-residual layer that makes checking work on real robot formats at scale; and the Passport as a recognized artifact — the Q2 2027 gate of recognition by an assessment body or standards organization is the moat we are building toward. Patents (13 granted, 9 pending [confirm]) cover the 3D reconstruction and recognition pipeline that produces our own asset library.

## 8. Team

- **Yi Ru, Founder/CEO, Team Lead.** PhD in Information Engineering, University of Toronto (2025); postdoctoral researcher, Harvard Medical School [lab]. Core contributor to ISO/IEC 21838-4:2023 (TUpper); 21 papers; FOIS 2018 Distinguished Paper Award [role]; invited AAAI presentation [confirm]; English-language monograph [title]; first inventor on multiple patents. Founding team at MICAS (>USD 5M angel round including Accel Partners; >USD 50M revenue in year one; led a 100+ person team; built CRM/ERP/WMS and ML-driven marketing); co-founder of YourTable Inc. (incubated by U of T, Schulich and Imperial College London; Collision 2019); co-founder and CEO of Uing Technologies (2022–), which shipped the Vision Pro application and filed nine invention patent applications.
- **CTO [name].** AI doctorate, McMaster University; applied-AI leadership [prior roles].
- **Robotics lead [name].** Mechanical/electronic engineering doctorate; autonomous-system perception.
- **Senior 3D asset lead [name].** 10+ years of production experience.
- **Advisors:** [none listed — add i-lab staff advisor once assigned; consider asking Prof. Michael Grüninger (U of T, editor lineage of TUpper) whether he will be named as a scientific advisor — see emails.md].
- **Commitments:** the founder is full-time at HMS through [date] and leads the company outside those hours [confirm HMS outside-activity disclosure]; a postdoctoral appointment at the University of Toronto is planned from [April/May 2027 or later], after which the company's Canadian presence [is/is not] the primary base [decision].

## 9. Impact

The economic impact is measured in data not wasted and deployments not blocked. If verification removes even 10% of unusable hours from a 10-million-hour global requirement at USD 50–200 per hour, the avoided collection cost is USD 50–200 million — illustrative arithmetic on the deck's figures, not a forecast; the first measured number will be the violation rate on the first external dataset [insert the internal-test rate once available, 15 Nov 2026]. For an OEM selling into Europe, a Passport is the training-data component of the Annex I technical documentation due by 2 August 2028; without it, certification is a bespoke consulting exercise per model release. The safety impact is that a robot trained on data whose part structure and contacts have been proven consistent has fewer failure modes that arise from mislabelled data, and the same ontology can later run as a guardrail at deployment. The scientific impact is the first quantitative measurement of annotation consistency in the datasets the field trains on, released as a public audit with corrected annotations and cross-dataset mappings, and contributed back to the COLORE repository and ISO/IEC JTC 1/SC 42. Beyond robotics, the same audit toolkit applies to any hierarchical annotation — part labels in medical imaging, CAD assemblies, building information models — which is how the founder's Harvard Medical School work and the company's medical-device and hospital relationships connect [one sentence on the HMS work — confirm].

## 10. Milestones and what the i-lab and the prize enable

During the spring-2027 Venture Program (12 weeks) we will: convert [two] of the co-development discussions into signed pilots at the USD 25–50k price point; run the first external dataset through Engine v1 and issue Passport v0.9; and use i-lab advisors and the HBS network to test the certification thesis with three Boston-area robotics and medical-device buyers [names]. A PIC grand prize (USD 75,000 in 2026) funds the Q2 2027 gate — recognition of Passport v1 by one assessment body or standards organization — and one engineer-quarter on the ROS 2/MCAP and OpenUSD adapters; a USD 25,000 prize funds the recognition work alone (see budget_and_timeline.md). Both are non-dilutive and precede the financing round sized to the 18-month plan.

---

## Technical Annex — "A verified evidence layer for robot-learning data"

### Recent Progress

An ontology is a computer-interpretable specification that declares what terms a system uses and what the terms mean. The founder's research has been the axiomatization of ontologies as first-order theories and their verification, carried into standards, patents and production systems.

- **TUpper and ISO/IEC 21838-4:2023.** As a core contributor within ISO/IEC JTC 1/SC 42, the founder worked on the axiomatization of the TUpper top-level ontology, its modular organization, and the verification of consistency and of the relationships between modules [1]. TUpper is an internationally standardized top-level ontology with a complete first-order axiomatization and machine-checked verification [confirm the wording of the founder's role and of this characterization with Prof. Grüninger]; every claim is a theorem or a counter-model. The company's kernel is built as a verified extension of it.
- **Material constitution and mereological pluralism.** With M. Grüninger, the founder developed a theory of material constitution as a parthood-preserving mapping between mereologies, and a validation of mereological pluralism, as first-order theories whose consistency and non-triviality are established by automated provers and model finders [2, 3]. The theory states exactly when two part decompositions of the same object are compatible — the question every robot dataset poses when kinematic, functional and visual part decompositions co-exist.
- **Knowledge-system architecture and deployment.** The founder's doctoral thesis developed an architecture in which a verified ontology governs the data model, the learned models and the simulation layer of an AI system; elements contributed to ISO/IEC 21838-4 [4]. At MICAS and YourTable, ontology-governed data-integration and recommendation systems ran in production; at Uing Technologies, ontology-based representations of objects, indoor environments and spatial relationships underlie a 100,000-package 3D asset library and a shipped Vision Pro application, with 13 granted patents and 9 applications [5].
- **AXIOMALITY kernel and Engine (2026).** Common Logic modules (ISO/IEC 24707) [6]; Prover9 theorem obligations and Mace4 counter-models [7]; a compiled SMT subset ([Z3 — confirm the solver actually used] [8]) for bulk checking; adapters for LeRobot, RLDS, ROS 2/MCAP, OpenUSD/USDZ, PLY and JSON; conformal calibration of physics residuals for abstention [9]. Internal test Q4 2026.

### Objectives

Robot-learning datasets annotate objects as hierarchies of parts with kinematic, functional and visual labels, but each dataset defines "part" operationally; no dataset or learned model is required to satisfy the axioms of parthood; there is no principled way to map labels across datasets. The company's technical program is motivated by the following long-term challenge:

*Can the part-level and contact-level structure recorded in robot-learning data be shown, by machine-checkable proof, to satisfy the axioms of physical objects that humans use, and can that proof be delivered as reproducible evidence at the scale and in the formats of commercial robot data?*

The program has three objectives:

1. **Ontology as specification (Kernel).** Axiomatize and verify the four-layer kernel — TUpper; physical world (parts, shape, measurement, materials, change, process); robotics (embodiment, kinematic chains, affordances, contacts, task phases, safety conditions); dataset instances — as modular first-order theories with consistency, non-triviality, module relationships and representation theorems established by Prover9/Mace4 under the COLORE methodology [10].
2. **Ontology as audit (Engine and Passport).** Translate annotation hierarchies and trajectories into kernel instances and check them by a two-tier pipeline (SMT for bulk; theorem proving for residual cases), producing per-release Passports and the first quantitative measurement of parthood and contact consistency across PartNet, PartNet-Mobility, GAPartNet, Open X-Embodiment, DROID and AgiBot World [11–16].
3. **Ontology as feedback (Augment and Learn).** Use violation rates and counter-models to drive correction, constraint-guided augmentation of underrepresented categories, and verification-in-the-loop evaluation of policies trained on passported versus raw data, in SAPIEN [17] [+ second simulator].

### Literature Review

Part-level datasets for physical AI — PartNet [11], PartNet-Mobility/SAPIEN [17], GAPartNet [12] — and real-robot corpora — Open X-Embodiment [13], DROID [14], AgiBot World [15] — are manually or semi-automatically annotated with no formal semantics: nothing requires the parts a model infers to form a consistent whole, nothing relates the part vocabularies of different datasets, and no prior work has subjected these datasets to ontological analysis. Existing data-quality tooling checks schema conformance and statistics, not meaning. Within applied ontology, the standardized top-level ontologies — BFO, DOLCE and TUpper, all parts of ISO/IEC 21838 [1, 18] — have been verified, but none has been used as a specification against which large annotation corpora are audited. Formal mereology supplies the axioms [19] but classical mereology assumes a single parthood relation; the founder's pluralist account [2, 3] is what allows kinematic, functional and visual decompositions to be checked against each other rather than collapsed. Assurance frameworks — the EU AI Act [20], NIST AI RMF [21] — require evidence about training data but do not say how evidence about physical-world semantics is to be produced or reproduced. That gap is the product.

### Methodology

The kernel is designed with the ontology lifecycle methodology of Grüninger and Fox [22] and the COLORE design-by-reuse and verification techniques [10]: competency questions come from the customer's acceptance tests (what must be true of every episode in this release?), and every module is verified — its models characterized up to isomorphism and compared with the intended models — before it is used to check data. Verification (models of the axioms versus intended models) is kept distinct from validation (whether the intended models are the ones the customer's data actually requires); Passports report both.

**Theme 1: Kernel (Objective 1).** *Given the annotation schema and format of a customer dataset, which verified modules of the kernel are required to specify it, and are they jointly consistent?*
- Project 1.1 — Parts and constitution module: rigid, articulated, functional and assembly parts as an extension of TUpper mereotopology with PSL [23] for state change under manipulation. Open questions: Do the kinematic (link/joint) and functional (actionable-region) decompositions in PartNet-Mobility and GAPartNet satisfy a common mereology, or do they require distinct parthood relations related by a constitution mapping? [Founder] Which axiom families produce counter-models on real annotations, and are those counter-models annotation errors or genuine pluralism? [Founder, CTO]
- Project 1.2 — Contacts, task phases and safety conditions: axiomatize contact, support and grasp phases so that a trajectory's phase labels are entailed rather than asserted. Open question: Can the safety conditions of ANSI/A3 R15.06 and R15.08 [24] be stated as fluents over the robotics layer so that a violation is a theorem? [Robotics lead]

**Theme 2: Engine and Passport (Objective 2).** *Can consistency be decided at the scale of commercial datasets, and can the decision be reproduced by a third party?*
- Project 2.1 — Two-tier checking: compile the decidable fragment of each module to SMT; route residual obligations to Prover9 with Mace4 for counter-models; UNKNOWN and timeout reported explicitly. Open questions: What fraction of obligations on each public corpus falls in the compiled fragment, and what is the throughput per 1,000 episodes? [CTO] Does the physics-residual observation contract, with conformal calibration, bound the abstention rate at the level a customer will accept? [Robotics lead]
- Project 2.2 — Passport format: axioms, checks, violations, corrections, counter-models and uncertainty as a versioned pack re-runnable by the recipient; aligned to the documentation expectations of EU AI Act Annex I and NIST AI RMF [20, 21]; reviewed with [accounting firm] and [law firm]. Open question: Which Passport fields does an assessment body require to recognize it as evidence? [Founder; Q2 2027 gate]

**Theme 3: Augment and Learn (Objective 3).** *Does passported data train better policies?*
- Project 3.1 — Correction and augmentation: constraint-guided synthesis of ontology-consistent part configurations for underrepresented categories. Open question: Does augmentation from counter-models improve coverage of unseen PartNet-Mobility categories more than random augmentation? [CTO]
- Project 3.2 — Verification-in-the-loop evaluation: report ontology-violation rate alongside task success for policies trained on raw versus passported data in SAPIEN. Open questions: Does violation rate predict task failure? Does pooled, ontology-aligned data transfer across part vocabularies? [Founder, robotics lead; ablations by axiom family.]

### Impact

Near term, the Engine and Passport give model developers, OEMs and data suppliers a way to buy, sell and certify robot data on evidence rather than on trust, and give regulators and assessment bodies a reproducible artifact for the training-data portion of technical documentation due under the EU AI Act from 2 August 2028. The public audit of the field's benchmark datasets improves the data that every model in the field is trained on and is contributed back to COLORE and ISO/IEC JTC 1/SC 42. Longer term, the same kernel, running at deployment as a semantic guardrail, extends machine-checkable evidence from what a robot learned to what it is doing; and the audit toolkit generalizes to any hierarchical annotation — medical-image part labels, CAD assemblies, building information models — connecting the company to the biomedical data problems of the founder's Harvard environment.

### Bibliography

[Verify every entry against the source before submission; entries marked † need venue/year confirmation.]

1. ISO/IEC 21838-4:2023. Information technology — Top-level ontologies (TLO) — Part 4: TUpper. ISO/IEC JTC 1/SC 42.
2. Ru, Y., Grüninger, M. (2026, submitted). Material Constitution as a Parthood-Preserving Mapping between Mereologies. Synthese.
3. Ru, Y., Grüninger, M. (2026, submitted). [Exact title — mereological pluralism validation paper]. Synthese.
4. Ru, Y. (2025). [Thesis title]. PhD thesis, Department of Mechanical and Industrial Engineering, University of Toronto.
5. [Patent list — numbers, jurisdictions, dates — for the 13 granted patents and 9 applications.]
6. ISO/IEC 24707:2018. Information technology — Common Logic (CL): a framework for a family of logic-based languages.
7. McCune, W. Prover9 and Mace4. https://www.cs.unm.edu/~mccune/prover9/ †
8. de Moura, L., Bjørner, N. (2008). Z3: An efficient SMT solver. TACAS. †
9. [Conformal prediction reference used for residual calibration — e.g., Vovk, Gammerman & Shafer, Algorithmic Learning in a Random World (2005) — confirm the method actually implemented.]
10. Grüninger, M., et al. COLORE: Common Logic Ontology Repository. colore.oor.net. † [confirm citation]
11. Mo, K., et al. (2019). PartNet: A large-scale benchmark for fine-grained and hierarchical part-level 3D object understanding. CVPR. †
12. Geng, H., et al. (2023). GAPartNet: Cross-category domain-generalizable object perception and manipulation via generalizable and actionable parts. CVPR. †
13. Open X-Embodiment Collaboration (2023). Open X-Embodiment: Robotic learning datasets and RT-X models. arXiv:2310.08864. †
14. Khazatsky, A., et al. (2024). DROID: A large-scale in-the-wild robot manipulation dataset. RSS. †
15. AgiBot World Colosseo team (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. arXiv. †
16. PartNet-Ensembled [citation — confirm source].
17. Xiang, F., et al. (2020). SAPIEN: A simulated part-based interactive environment. CVPR. †
18. ISO/IEC 21838-1:2021 (requirements), 21838-2:2021 (BFO), 21838-3:2023 (DOLCE). †
19. Casati, R., Varzi, A. (1999). Parts and Places: The Structures of Spatial Representation. MIT Press. †
20. Regulation (EU) 2024/1689 (Artificial Intelligence Act), Annex I and the application date of 2 August 2028 for AI systems covered by the listed product legislation. †
21. NIST (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. †
22. Grüninger, M., Fox, M. S. (1995). Methodology for the design and evaluation of ontologies. IJCAI-95 Workshop on Basic Ontological Issues in Knowledge Sharing. †
23. ISO 18629 (Process Specification Language). †
24. ANSI/RIA R15.06 and ANSI/A3 R15.08 (industrial and industrial mobile robot safety). †
