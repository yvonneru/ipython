# Research proposal — Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship (U of T)

**Applicant:** Yi Ru, PhD (Information Engineering, University of Toronto, 2025); Postdoctoral Researcher, Harvard Medical School [laboratory/department].
**Proposed supervisor:** Prof. Michael Grüninger, Department of Mechanical and Industrial Engineering, University of Toronto. **Proposed co-supervisor (AI/robotics):** [name, U of T Robotics Institute / Vector Institute affiliate — confirm].
**Proposed start:** [1 May 2027 or later, within the 1 May 2027 – 1 Jan 2028 window].

*Format note (delete before submission): written at about 2.5 pages of body text plus references. If the DSI limit is 2 pages, cut in this order: the last two Open Research Questions of Theme 1; the paragraph on cross-domain reuse in Impact; the sentence-level examples in the Literature Review. Headings are the Grüninger structure; re-map onto the funder's headings if the form prescribes them.*

## Title
**Verified part-level representations for robot manipulation: using a machine-checked ontology to audit, align and constrain what physical-AI systems learn**

## Summary
Robot manipulation policies are trained on large datasets that describe objects as hierarchies of parts. Each dataset defines "part" operationally, no dataset is required to satisfy the axioms of parthood, and pooled training silently mixes incompatible part vocabularies. The result — brittle transfer to new object categories — is observed but has never been measured, because there has been no formal specification to measure against. I will build that specification as a verified extension of the international standard top-level ontology TUpper (ISO/IEC 21838-4), use it to audit and align the datasets the field trains on, and then use it as an inductive bias inside the training and evaluation of part-aware manipulation policies. The engineering question is whether verified structure improves what learned policies do on articulated objects; the AI methods are neuro-symbolic training, constraint-guided data generation and calibrated abstention; the training I seek is in modern deep robot learning, which I have not yet been formally trained in.

## 1. Recent Progress
An ontology is a computer-interpretable specification that declares what terms a system uses and what they mean. My research has been on ontologies as theories in first-order logic whose models are characterized and machine-checked, and on carrying such theories into deployed data systems.

- **International standardization of a verified top-level ontology.** I am a core contributor to ISO/IEC 21838-4:2023, *Information technology — Top-level ontologies — Part 4: TUpper* (ISO/IEC JTC 1/SC 42) [1]. TUpper is the first top-level ontology adopted internationally with a complete first-order axiomatization and machine-checked verification: every claim about it is a theorem or a counter-model. [Specify the modules and verification results I was responsible for.]
- **A formal theory of parts for objects that have more than one decomposition.** With Prof. Grüninger I developed material constitution as a parthood-preserving mapping between distinct mereologies, and a validation of mereological pluralism, in two papers submitted to *Synthese* in 2026 [2, 3]. The axioms are first-order; consistency and non-triviality are established with automated provers and model finders; the mapping is proved to preserve the parthood structure it must preserve. The theory says exactly what must hold for two part decompositions of the same object — kinematic, functional, visual — to be compatible, which is the question robot datasets pose and do not answer.
- **Ontology-governed knowledge systems in production.** My doctoral thesis [4] developed an architecture in which a verified ontology governs the data model, the learned models and the simulation layer of an AI system; elements of it entered ISO/IEC 21838-4. As co-founder of Uing Technologies I built structured 3D physical-world datasets and ontology-based representations of objects, indoor environments and interactions for embodied AI, and shipped an AR application on the Apple Vision Pro with mesh object recognition, spatial mapping and autonomous path planning [5]; I am first inventor on patents in 3D recognition, indoor modelling and automatic reconstruction [reconcile counts and list numbers]. At MICAS I led machine-learning-driven marketing and order-risk systems at production scale. Distinguished Paper Award, FOIS 2018 [confirm role]. [One sentence on the Harvard Medical School work — ontology-driven integration of heterogeneous biomedical data / neuro-symbolic clinical AI.]

## 2. Objectives
Robot-learning datasets — PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment, DROID [6–12] — annotate objects as hierarchies of parts with kinematic, functional and visual labels. A "part" is a segmentation label in one, a movable link in another, an actionable region in a third. Nothing requires the parts a model infers to form a consistent whole; nothing relates the part vocabularies of different datasets; nothing lets a policy reason about why a part decomposition is wrong. The program is motivated by the following long-term challenge:

*Can the part-level representations that robot-learning systems learn be shown to satisfy the axioms of parthood that humans use, and does enforcing those axioms improve generalization?*

The proposed program has three objectives:

1. **Ontology as specification (O1).** Axiomatize and verify a modular first-order ontology of physical object parts — rigid, articulated, functional, assembly — as an extension of TUpper integrated with the Process Specification Language (PSL) for state change under manipulation.
2. **Ontology as audit (O2).** Translate the annotation hierarchies of the major datasets into ontology instances and check them automatically, producing the first quantitative measurement of parthood consistency in robot datasets, corrected annotations, provably meaning-preserving cross-dataset label mappings and a merged, ontology-aligned corpus.
3. **Ontology as inductive bias (O3).** Develop and evaluate training methods that use the ontology to shape part-aware manipulation policies, and measure the effect on generalization to unseen object categories in simulation.

The objectives cluster around three themes: Parts, Audit, Learning.

## 3. Literature Review
Part-level datasets for physical AI have grown from segmentation hierarchies of static shapes (PartNet [6]) to articulated assets with kinematic joints (PartNet-Mobility in SAPIEN [7]), actionable parts (GAPartNet [8]), ensembled corpora (PartNet-Ensembled [9]) and real-robot episode collections (AgiBot World [10], Open X-Embodiment [11], DROID [12]). Their annotation schemas were designed independently and are combined freely in training pipelines; a part may be annotated as both contained in and disjoint from another within one dataset, and no dataset provides a definition of "part" against which its own labels could be checked. Learned manipulation policies inherit these presuppositions: as Grüninger's Commonsense Cobotics program observes, the performance of machine-learning implementations is heavily influenced by the ontological presuppositions implicit in training data [13]. On the formal side, first-order mereology and mereotopology are mature and verified within the COLORE repository (2,580+ ontologies) [14, 15], TUpper is standardized [1], and the Grüninger lifecycle methodology gives a verification standard — characterize the models of an ontology up to isomorphism and compare them with the intended models [16]. What is missing is the bridge: no verified ontology of object parts exists that is integrated with a process ontology for manipulation, no robot dataset has been subjected to ontological analysis, and no manipulation policy has been trained or evaluated against a formal specification of the structure it infers. Neuro-symbolic work on constraint losses and knowledge-guided augmentation exists in vision and language [17 — cite two representative works]; it has not been applied to parthood in manipulation.

## 4. Methodology
The ontologies will be designed with the ontology lifecycle methodology of [16] and the design-by-reuse, merging and transfer techniques of the Semantic Technologies Laboratory [18]. All ontologies will be verified: we characterize the models of each module up to isomorphism and determine whether they are equivalent to the intended models. Competency questions come from the application: the labels and relations that annotators actually use, and the questions a policy must answer about an object before and after manipulation ("which parts move together when this handle is pulled?").

### Theme 1: Parts (O1)
*Given an object with kinematic, functional and visual part decompositions, specify a first-order theory under which these decompositions are provably compatible or provably not.*

**Project 1.1 — Parts ontology as a TUpper/PSL extension.** Modules for rigid parts (mereotopology), articulated parts (joints as fluents whose change is a PSL activity), functional parts (affordance-bearing regions) and assemblies (parthood-preserving mappings between the three). Verification with Prover9 and Mace4 [19]; modules and translation definitions contributed to COLORE. Theorems to be proved: consistency of each module; non-triviality (existence of non-degenerate models); representation theorems relating articulated-part models to kinematic trees; that the constitution mapping of [2] preserves parthood between the functional and rigid mereologies.
- Are the parthood relations implicit in PartNet's segmentation hierarchy and PartNet-Mobility's link hierarchy the same relation, or distinct relations each with its own axiomatization? — Y1 milestone
- Does the axiomatization of articulated parts require the full PSL Ontology or a definable fragment? — Y1 milestone
- Which classes of partial orders and graphs are needed to verify the assembly module up to isomorphism? — Y1
- Can affordance-bearing regions (GAPartNet's actionable parts) be defined from the rigid and articulated modules, or do they require new primitives? — Y1

### Theme 2: Audit (O2)
*Given a dataset's annotation hierarchy, measure the rate and pattern of parthood-axiom violations and compute label mappings across datasets that are meaning-preserving by proof.*

**Project 2.1 — Two-tier audit pipeline.** Schema mappings translate each dataset's annotation hierarchy into instances of the parts ontology. A Datalog/SMT tier [solver — confirm] checks the bulk of the data (millions of part instances) against the compiled decidable fragment of the ontology; a first-order theorem-proving tier handles the residual hard cases; UNKNOWN and timeout are first-class outputs rather than silent passes. Output per dataset: violation rate by axiom family and by object category; corrected annotations; per-source coverage. Output across datasets: the set of label mappings that are provably meaning-preserving, and a merged, ontology-aligned corpus. Datasets audited: PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World (Y1); Open X-Embodiment and DROID part-level subsets (Y2).
- What fraction of the ontology's obligations is decidable in the SMT tier, and does the residue fit within a theorem-proving budget at dataset scale? — Y1 milestone
- Do violation rates cluster by object category, by annotator protocol or by dataset — that is, are the errors ontological (a wrong definition of part) or clerical? — Y1
- Which cross-dataset mappings are meaning-preserving only under the constitution mapping of [2] rather than under identity of parthood? — Y2

### Theme 3: Learning (O3) — the AI core
*Does training and evaluating a part-aware manipulation policy against the verified ontology improve generalization to unseen object categories?*

**Project 3.1 — Ontology as inductive bias.** Three methods, developed with [co-supervisor]'s group: (a) differentiable relaxations of parthood constraints as auxiliary losses on the part relations a policy infers; (b) constraint-guided data augmentation that synthesizes ontology-consistent part configurations for under-represented categories; (c) a verification-in-the-loop evaluation protocol that reports, alongside task success, the rate at which a policy's inferred object structure violates the ontology, with conformal calibrated uncertainty controlling when the policy abstains. Experiments on articulated-object manipulation in SAPIEN [7] and [second simulator — confirm], with held-out PartNet-Mobility categories, matched comparisons with confidence intervals, and ablations by axiom family. Hypotheses: H1, ontology-consistent training improves generalization to unseen categories; H2, violation rate predicts task failure and serves as an interpretable failure signal; H3, pooled ontology-aligned data trains policies that transfer across part vocabularies.
- Which axiom families, when relaxed into losses, change policy behaviour, and which are already satisfied by the data? — Y2 milestone
- Is the ontology-violation rate a better predictor of failure on held-out categories than task-success on seen categories? — Y2 milestone
- Does the merged corpus of Theme 2 outperform any single source at equal size? — Y2

**AI methods and training link.** Methods (a)–(c) are where the fellowship's AI training programme is load-bearing: I bring the formal specification and the data-engineering discipline; the fellowship and the co-supervisor supply training in deep policy learning, 3D representation learning, differentiable programming and uncertainty quantification (see the statement of AI training needs).

## 5. Impact
Near term, the program delivers to the physical-AI community a verified parts ontology under an open licence (contributed to COLORE and to ISO/IEC JTC 1/SC 42), the first quantitative audit of parthood consistency in the datasets much of the field trains on, a merged ontology-aligned corpus, an audit toolkit, and an interpretable failure signal for manipulation policies. It gives engineering science a measured answer to whether formal structure improves learning on articulated objects. It also addresses a compliance clock: the EU AI Act Annex I applies to AI in machinery and robots from 2 August 2028, and NIST's AI RMF asks for evidence about training data; specification-based audits are machine-checkable evidence [20]. The toolkit generalizes to other hierarchical annotations — CAD assemblies and digital twins in manufacturing, part labels in medical imaging (my Harvard context), building information models. Longer term, the ontologies join the open knowledge network that COLORE supports and give the robotics community a testbed in which the correctness of perception and action can be evaluated against the ontologies humans use.

**Publications and releases (24 months):** audit/data paper at a leading AI or robotics venue (Y1); two machine-learning-venue papers on methods (a)–(c) (Y2); one robotics-venue paper on verification-in-the-loop evaluation (Y2); ontology, corpus and toolkit released with the papers.

## Bibliography
All entries flagged [verify citation] must be completed from the applicant's own bibliography before submission; no title has been invented.
1. ISO/IEC 21838-4:2023. *Information technology — Top-level ontologies (TLO) — Part 4: TUpper.* ISO/IEC JTC 1/SC 42. [verify citation]
2. Ru, Y., Grüninger, M. (2026, submitted). Material Constitution as a Parthood-Preserving Mapping between Mereologies. *Synthese.*
3. Ru, Y., Grüninger, M. (2026, submitted). [Exact title — mereological pluralism validation]. *Synthese.*
4. Ru, Y. (2025). [Thesis title]. PhD thesis, Department of Mechanical and Industrial Engineering, University of Toronto.
5. Uing Technologies. [App name], Apple Vision Pro App Store [year]. [verify citation]
6. PartNet (Mo et al., CVPR 2019). [verify citation]
7. SAPIEN / PartNet-Mobility (Xiang et al., CVPR 2020). [verify citation]
8. GAPartNet (Geng et al., CVPR 2023). [verify citation]
9. PartNet-Ensembled. [verify citation]
10. AgiBot World (2025). [verify citation]
11. Open X-Embodiment (2023). [verify citation]
12. DROID (Khazatsky et al., 2024). [verify citation]
13. Grüninger, M. *Commonsense Cobotics.* NSERC Discovery Grant proposal (unpublished) — cite the published PRAxIS/robotics work instead. [verify citation]
14. COLORE, Common Logic Ontology Repository, colore.oor.net. [verify citation]
15. ISO/IEC 24707:2018. *Common Logic.* [verify citation]
16. Grüninger, M., Fox, M. S. (1995). Methodology for the design and evaluation of ontologies. [verify citation]
17. [Two representative neuro-symbolic works on constraint losses / knowledge-guided augmentation — applicant to select.]
18. [Grüninger et al. — design by reuse / ontology merging / ontology transfer papers, as cited in the NSERC proposals as [18], [19], [2], [12], [6].] [verify citation]
19. McCune, W. Prover9 and Mace4. [verify citation]
20. Regulation (EU) 2024/1689 (AI Act), Annex I; NIST AI Risk Management Framework 1.0. [verify citation]
