# Research proposal — Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship (U of T)

**Applicant:** Yi Ru, PhD (Information Engineering, University of Toronto, March 2025); Postdoctoral Researcher, Harvard Medical School [laboratory/department — confirm; the appointment is not on the current CV].
**Supervisor (domain):** Prof. Michael Grüninger, Department of Mechanical and Industrial Engineering, University of Toronto. **Co-supervisor (AI / robot learning):** [name — U of T Robotics Institute / Vector Institute affiliate; confirm. The U of T apply page reportedly requires at least two co-supervisors, one designated "Supervisor" — verify; if so this line is mandatory, not optional].
**Proposed start:** [1 May 2027 or later, within the 1 May 2027 – 1 January 2028 window].

*Format note (delete before submission): body below is about 1,290 words including headings — two pages at 11 pt with 2 cm margins, or just over two pages at 12 pt — plus a 15-entry reference list. The page limit is NOT established (see README); cut order if a 2-page limit at 12 pt applies: (1) the "Relation to the supervisor's programs" paragraph, (2) the last sentence of Recent progress bullet 3, (3) the open questions in Themes 1–2. If references count toward the limit, cite entries 6–12 in text as one grouped citation and drop entries 13–15. If the form prescribes headings (e.g. Background / Aims / Methods / AI component / Timeline), map: Summary → Background; Objectives → Aims; Methodology → Methods; Theme 3 + "AI methods and training" → AI component; month ranges → Timeline. If the form asks for a lay summary and impact statement, use statement.md Part C.*

## Title
**Verified part-level representations for robot manipulation: a machine-checked ontology to audit, align and constrain what physical-AI systems learn**

## Summary
**Domain:** engineering of physical-AI systems — robot-manipulation datasets, digital twins of articulated objects, and the data standards they rest on. **AI methods to be applied:** neuro-symbolic training, constraint-guided data generation, calibrated abstention. **AI methods I will be trained in:** deep robot learning, 3D representation learning, differentiable programming, uncertainty quantification.

Robot manipulation policies are trained on datasets that describe objects as hierarchies of parts [6–12]. Each dataset defines "part" operationally, none is required to satisfy the axioms of parthood, and pooled training mixes incompatible part vocabularies. Whether this costs generalization is unknown, because there is no formal specification to measure against. I will build that specification as a verified extension of the international-standard top-level ontology TUpper (ISO/IEC 21838-4) [1], audit and align the datasets the field trains on against it, and use it as an inductive bias inside the training and evaluation of part-aware manipulation policies. The engineering question: does verified structure improve generalization to unseen articulated objects? Verified mereology exists in COLORE [14] and TUpper is standardized [1]; neuro-symbolic constraint losses and knowledge-guided augmentation exist in vision and language [applicant to cite two works]; but no parts ontology has been integrated with a process ontology for manipulation, no robot dataset has been audited against one at scale, and no policy has been trained or evaluated against a formal specification of the structure it infers.

## 1. Recent progress
My research treats ontologies as first-order theories whose models are characterized and machine-checked, and carries such theories into deployed data systems.

- **Verified top-level ontology as an international standard.** I am a core contributor to ISO/IEC 21838-4:2023 (TUpper) [1], a top-level ontology adopted internationally with a complete first-order axiomatization and machine-checked verification. [Specify the modules and verification results I was responsible for.]
- **A formal theory of parts for objects with more than one decomposition.** With Prof. Grüninger I developed material constitution as a parthood-preserving mapping between distinct mereologies, and a validation of mereological pluralism (two papers submitted to *Synthese*, 2026; first author) [2, 3]. The theory states exactly what must hold for two part decompositions of one object — kinematic, functional, visual — to be compatible: the question robot datasets pose and do not answer.
- **Ontology-governed systems in production.** My thesis [4] developed an architecture in which a verified ontology governs the data model, learned models and simulation layer of an AI system. As co-founder of Uing Technologies I built structured 3D datasets and ontology-based object representations for embodied AI and shipped an Apple Vision Pro application with mesh object recognition, spatial mapping and path planning [5]; I am first inventor on patents in 3D recognition, indoor modelling and reconstruction [reconcile counts]; at MICAS I built machine-learning-driven marketing and order-risk systems in production. Distinguished Paper Award, FOIS 2018 [confirm role]. [One sentence on the Harvard Medical School work.]

## 2. Objectives
Long-term challenge: *can the part-level representations that robot-learning systems learn be shown to satisfy the axioms of parthood, and does enforcing those axioms improve generalization?* Three objectives, each with a measurable endpoint:

1. **O1 — Ontology as specification.** A verified, modular first-order ontology of physical object parts (rigid, articulated, functional, assembly) extending TUpper and integrated with the Process Specification Language (PSL) for state change under manipulation. *Endpoint:* consistency and non-triviality proofs for every module and representation theorems relating articulated-part models to kinematic trees, published in COLORE [14].
2. **O2 — Ontology as audit.** Translate the annotation hierarchies of PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled and AgiBot World [6–10] (Y1), and part-level subsets of Open X-Embodiment and DROID [11, 12] (Y2), into ontology instances and check them automatically. *Endpoint:* to my knowledge the first quantitative measurement of parthood-axiom violation rates in robot datasets, by axiom family and category with confidence intervals; corrected annotations; label mappings that are meaning-preserving by proof; a merged, ontology-aligned corpus.
3. **O3 — Ontology as inductive bias.** Training and evaluation methods that use the ontology to shape part-aware manipulation policies. *Endpoint:* a pre-registered comparison of task success on held-out PartNet-Mobility categories, ontology-constrained versus unconstrained, with a minimum effect size [to set with the co-supervisor], and a test of whether ontology-violation rate predicts task failure.

**Relation to the supervisor's programs.** Prof. Grüninger's NSERC programs ask which mereotopologies are implicit in ShapeNet and PartNet [13]. This program takes those results as input and is distinct in object (articulated, functional and assembly parts under manipulation), data (real-robot episode corpora), method (scalable audit; ontology as a training-time inductive bias) and question (whether enforcing the axioms changes what a learned policy does).

## 3. Methodology
Ontologies are designed with the lifecycle methodology of [15] and the Semantic Technologies Laboratory's reuse, merging and transfer techniques, verified with Prover9 and Mace4, and contributed to COLORE. Competency questions come from the relations annotators actually use and the questions a policy must answer under manipulation ("which parts move together when this handle is pulled?").

**Theme 1 — Parts (O1; months 1–8).** Modules for rigid parts (mereotopology), articulated parts (joints as fluents changed by PSL activities), functional parts (affordance-bearing regions) and assemblies (parthood-preserving mappings between the three). Open questions: Does articulated parthood need the full PSL ontology or a definable fragment? Can GAPartNet's actionable parts be defined from the rigid and articulated modules?

**Theme 2 — Audit (O2; months 3–16).** Schema mappings translate each dataset's hierarchy into ontology instances. A Datalog/SMT tier [solver — confirm] checks millions of part instances against a compiled decidable fragment; a theorem-proving tier handles residual cases; UNKNOWN and timeout are first-class outputs, never silent passes. Open questions: What fraction of the ontology's obligations is decidable in the SMT tier? Do violations cluster by category, annotator protocol or dataset — ontological errors or clerical ones?

**Theme 3 — Learning (O3; pilot months 5–8, full months 9–24) — the AI core.** With [co-supervisor]'s group: (a) differentiable relaxations of parthood constraints as auxiliary losses on the part relations a policy infers; (b) constraint-guided augmentation that synthesizes ontology-consistent part configurations for under-represented categories; (c) verification-in-the-loop evaluation reporting, beside task success, the rate at which a policy's inferred object structure violates the ontology, with conformal uncertainty controlling abstention. Experiments in SAPIEN [7] and [second simulator — confirm] on held-out PartNet-Mobility categories: matched comparisons with confidence intervals, ablations by axiom family. Hypotheses: H1, ontology-consistent training improves held-out generalization; H2, violation rate predicts task failure; H3, the merged corpus of Theme 2 beats any single source at equal size. A Y1 pilot (two baselines reproduced; loss (a) on two held-out categories) de-risks Y2. Open question: which axiom families, relaxed into losses, change policy behaviour?

**AI methods and training.** Methods (a)–(c) are where the fellowship's AI training is load-bearing: I bring the formal specification and data-engineering discipline; the cohort programme and the co-supervisor supply training in deep policy learning, 3D representation learning, differentiable programming and uncertainty quantification, each tied to a Y1 deliverable (see statement of AI training needs).

## 4. Impact and outputs
The program gives engineering science a measured answer to whether formal structure improves learning on articulated objects, and gives the physical-AI community a verified parts ontology under an open licence (contributed to COLORE and ISO/IEC JTC 1/SC 42), the first audit of parthood consistency in the datasets much of the field trains on, a merged corpus, an audit toolkit and an interpretable failure signal for policies. Such audits are machine-checkable evidence of the kind AI regulation for machinery and robots (EU AI Act, Annex I) and the NIST AI Risk Management Framework ask for, and the toolkit generalizes to CAD assemblies, digital twins and building information models. Outputs in 24 months: an audit/data paper (Y1); a methods paper on (a)–(b) and a robotics-venue paper on (c) (Y2); ontology, corpus and toolkit released with the papers; results presented to the cohort.

## References
Entries flagged [verify citation] must be completed from the applicant's own bibliography; no title has been invented.
1. ISO/IEC 21838-4:2023. *Information technology — Top-level ontologies (TLO) — Part 4: TUpper.* [verify citation]
2. Ru, Y., Grüninger, M. (2026, submitted). Material Constitution as a Parthood-Preserving Mapping between Mereologies. *Synthese.*
3. Ru, Y., Grüninger, M. (2026, submitted). [Exact title — mereological pluralism validation]. *Synthese.*
4. Ru, Y. (2025). [Thesis title]. PhD thesis, Department of Mechanical and Industrial Engineering, University of Toronto.
5. Uing Technologies. [App name], Apple Vision Pro App Store, [year]. [verify citation]
6. PartNet [Mo et al., CVPR 2019 — verify citation]
7. SAPIEN / PartNet-Mobility [Xiang et al., CVPR 2020 — verify citation]
8. GAPartNet [Geng et al., CVPR 2023 — verify citation]
9. PartNet-Ensembled [verify citation]
10. AgiBot World [2025 — verify citation]
11. Open X-Embodiment [2023 — verify citation]
12. DROID [Khazatsky et al., 2024 — verify citation]
13. [Grüninger, M. — a published paper on ontological analysis of benchmarking datasets / PRAxIS ontologies; applicant to select. Do not cite the unpublished NSERC proposals.]
14. COLORE, Common Logic Ontology Repository. [verify citation]
15. Grüninger, M., Fox, M. S. (1995). Methodology for the design and evaluation of ontologies. [verify citation]
