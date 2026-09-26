# Research outline — Humboldt Research Fellowship for postdoctoral researchers

**Applicant:** Dr. Yi Ru — PhD, Information Engineering, University of Toronto (all requirements completed March 2025 [confirm conferral date]); postdoctoral researcher, Harvard Medical School [laboratory/department; since month year]
**Host:** Prof. [name], [institute], [University of Bremen / University of Osnabrück / TU Dresden — confirm]
**Title:** Verified mereological ontologies for object–part representation in physical AI
**Intended duration and division of visits:** 12 months in one continuous stay, from [start month — 2027 or 2028, per the sequencing decision]. [The postdoctoral track is understood to require a single stay; confirm on the programme information before submission.]

## 1. Summary

Robot-learning systems are trained on datasets that describe objects as hierarchies of parts. No dataset, and no model trained on one, is required to satisfy the axioms of parthood, and no dataset states how its part vocabulary relates to any other's. I propose to supply the missing semantics: a formally verified first-order ontology of physical object parts, extending the ISO/IEC 21838-4 top-level ontology, used first as a *specification*, then as an *audit* of the part-level datasets on which manipulation policies are trained, and then as an *inductive bias* on the policies themselves. The 12-month stay is sized to the first two uses and to one controlled experiment on the third, with the host's knowledge-based robotics group. Outputs: a verified ontology in an open repository, the first quantitative measurement of parthood consistency across robot datasets, a merged and ontology-aligned corpus, and a reusable audit toolkit.

## 2. Current state of research

An ontology axiomatized in first-order logic can be checked by a theorem prover and its unintended models found by a model finder. Four bodies of work define the starting point.

**Verified top-level and process ontologies.** ISO/IEC 21838-4:2023 standardizes TUpper, a top-level ontology whose modules for time, mereotopology, location, units and process are verified: the models of the axioms are characterized up to isomorphism and compared with the intended models [1]. TUpper is developed with the COLORE repository of first-order ontologies (2,580 theories in Common Logic) and its methodology of competency questions, reuse and merging [2, 3]; the Process Specification Language (ISO 18629) supplies a verified theory of activities, occurrences and fluents [4]. I was a core contributor to ISO/IEC 21838-4 [confirm role wording].

**Mereology and material constitution.** Classical extensional mereology [5, 6] assumes a single parthood relation. Every annotated object in a robot dataset carries several: kinematic (links), functional (handles, lids), visual (segments). With M. Grüninger I have developed an account of material constitution as a parthood-preserving mapping between distinct mereologies, and a validation of mereological pluralism by the verification methods used for ontologies; two papers are under review at Synthese [7, 8]. The theory states, as first-order axioms, when two part decompositions of one object are compatible — exactly the question the datasets leave open.

**Part-level datasets for robot learning.** PartNet annotates 26,671 objects with hierarchical part decompositions [9]; PartNet-Mobility (SAPIEN) adds articulated links and joints for 2,346 objects [10]; GAPartNet defines nine classes of actionable parts with pose annotations [11]; real-robot corpora such as AgiBot World [12], Open X-Embodiment [13] and DROID [14] annotate object structure inconsistently or not at all; PartNet-Ensembled [15, confirm citation] pools several. Each defines "part" operationally; none states axioms; none maps its labels to another's. Poor transfer across part vocabularies and brittle generalization to new categories are observed [11, 13] but have never been measured against a specification, because there has been none.

**Knowledge-based robotics.** The KnowRob knowledge-processing system and the CRC EASE programme at Bremen [16, 17] represent objects, parts, affordances and actions in a robot's knowledge base and query them during task execution. That part structure is, to my knowledge, asserted rather than verified against a mereology, and it has not been aligned with the learning datasets above. [Extend with the host's own recent work once the host is confirmed.]

**The gap.** Verified mereological theory, large part-level datasets and knowledge-based robot architectures all exist; nothing connects them. There is no verified ontology of object parts extending a standardized top-level ontology, no audit of any robot dataset against one, and no measurement of whether enforcing parthood axioms changes what a policy learns.

## 3. Objectives

The long-term question is: *can the part-level representations that robot-learning systems learn be shown to satisfy the axioms of parthood, and does enforcing those axioms improve generalization?* The fellowship addresses three objectives; the stay completes O1 and O2 and delivers the first experiment of O3.

1. **Ontology as specification (O1).** Axiomatize and verify a modular first-order ontology of physical object parts (rigid, articulated, functional, assembly) as an extension of TUpper integrated with PSL for state change under manipulation, with representation theorems relating it to the annotation schemas of the major datasets and to the host's knowledge base. *Success criterion:* every module verified (consistency, non-triviality, module relationships as theorems) and deposited in COLORE; theorems for at least four dataset schemas and the host's knowledge base.
2. **Ontology as audit (O2).** Build a two-tier audit pipeline (Datalog/SMT for bulk instances; first-order theorem proving for residual cases) and produce the first quantitative measurement of parthood consistency in PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled and AgiBot World, with corrected annotations, proved meaning-preserving cross-dataset mappings and a merged corpus. *Success criterion:* all five datasets audited with stated coverage; corpus, corrections and proofs publicly released; audit/data paper submitted.
3. **Ontology as inductive bias (O3).** Test, in SAPIEN and the host's environment, whether ontology-consistent training data and parthood constraints expressed as auxiliary losses improve generalization of part-aware manipulation policies to unseen object categories, and whether a policy's ontology-violation rate predicts task failure. *Success criterion:* one matched comparison on held-out PartNet-Mobility categories with confidence intervals and an ablation by axiom family; methods paper drafted.

## 4. Methodology

All ontologies follow the lifecycle methodology of competency questions, verification and validation practised in COLORE [2, 3]: I characterize the models of each module up to isomorphism, prove consistency and non-triviality with Prover9 and Mace4 [19], and establish the relationships between modules (extension, conservative extension, definable equivalence) as theorems. Verification asks whether the models of the axioms are the intended models; validation asks whether the intended models are the right ones, and here the validation instrument is the data: every competency question is one that a dataset either answers consistently or does not. Each project lists the open questions it answers by a theorem, a counter-model or a measurement, with the quarter in which they are due.

### Theme 1 — Parts (O1)

**Project 1.1 — Parts ontology.** Separate mereologies for rigid parts, articulated parts (links and joints, with PSL activities for joint motion), functional parts (affordance-bearing regions in the sense of GAPartNet) and assemblies, each extending TUpper's mereotopology and related to one another by the constitution mappings of [7, 8]. Every module is verified, written in Common Logic, and deposited in COLORE and the host's repository.
- Open questions: Are the kinematic, functional and visual part relations in the datasets three mereologies related by parthood-preserving mappings, or does one fail to be a mereology at all? (Q1) Which axioms of extensional mereology must be weakened for articulated objects whose parts move relative to one another? (Q1) Is material constitution definable from parthood plus PSL fluents, or does it need a primitive? (Q2)

**Project 1.2 — Representation theorems for annotation schemas.** For each dataset schema, and for the host's knowledge base, a translation definition into the ontology's signature and a theorem stating which axioms the schema entails and which it violates by construction.
- Open questions: Which schemas are definably equivalent to a fragment of the parts ontology, and which are strictly weaker? (Q2) Does the host's knowledge base [KnowRob — confirm] entail the parthood axioms, and if not, which counter-models does Mace4 return? (Q2)

### Theme 2 — Audit (O2)

**Project 2.1 — Two-tier audit pipeline.** Bulk checking by Datalog rules and an SMT encoding (Z3 [18]) of the decidable fragment, handling millions of part instances; first-order theorem proving for the residual cases; UNKNOWN and timeout reported as first-class outcomes. The pipeline is a versioned toolkit with adapters for the dataset formats (PartNet JSON hierarchies, SAPIEN URDF, GAPartNet annotations, LeRobot/RLDS episodes).
- Open questions: What fraction of parthood violations in each dataset is decidable in the SMT fragment, and what remains for the prover? (Q2) Does violation density differ systematically by object category, annotator source or dataset? (Q3)

**Project 2.2 — Cross-dataset alignment and merged corpus.** Label mappings between datasets are accepted only when proved parthood-preserving under the constitution theory; the aligned corpus and corrected annotations are released with the proofs.
- Open questions: Which pairs of part vocabularies admit a meaning-preserving mapping at all, and where does pooling necessarily introduce inconsistency? (Q3) Does the audit run unchanged on the host's own robot logs [confirm data available]? (Q3)

### Theme 3 — Learning (O3)

**Project 3.1 — Ontology-consistent training and verification-in-the-loop evaluation.** Three interventions on a part-aware manipulation policy in SAPIEN [10] and the host's platform [confirm second simulator or robot]: (a) training on the audited, aligned corpus versus the raw pooled corpus; (b) differentiable relaxations of parthood constraints as auxiliary losses on inferred part relations; (c) an evaluation protocol reporting ontology-violation rate alongside task success, with ablations by axiom family. Matched comparisons on held-out PartNet-Mobility categories with confidence intervals.
- Open questions: Does training on the aligned corpus improve success on held-out categories relative to raw pooling? (Q4) Is a policy's ontology-violation rate a predictor of task failure? (Q4) Which axiom families carry the effect? (Q4, continued after the stay)

## 5. Work and time schedule (12 months, [start month] – [end month])

| Quarter | Work | Deliverable |
|---|---|---|
| Q1 (months 1–3) | Parts ontology modules; verification; representation theorems for PartNet and PartNet-Mobility schemas; alignment with the host's knowledge base | Verified ontology v0.9 in COLORE and the host's repository; technical report |
| Q2 (months 4–6) | Remaining schema theorems (GAPartNet, AgiBot World, host data); audit pipeline v1; first audit of two datasets | Audit pipeline released; audit results for two datasets; ontology v1.0 |
| Q3 (months 7–9) | Audit of all five datasets; cross-dataset mappings with proofs; merged corpus | Audit/data paper submitted [venue — agree with host]; public data release |
| Q4 (months 10–12) | Policy experiments in SAPIEN and the host's platform; verification-in-the-loop evaluation; write-up; continuation plan | Methods paper draft; ontology offered to ISO/IEC JTC 1/SC 32 as a liaison contribution [confirm process]; joint follow-on proposal with the host |

Contingencies: if the SMT fragment covers less of the data than expected, Q2 shifts effort to the prover tier and the audit is reported on a sampled subset with stated coverage; if the host's platform is unavailable, Q4 runs in SAPIEN alone; if Q3 overruns, Theme 3 is reduced to intervention (a) plus the evaluation protocol, and (b) continues after the stay. Theme 1 has no external dependencies and starts on day one.

## 6. Expected results, impact, independence and the choice of host

**Results.** A verified parts ontology under an open licence in COLORE and the host's repository, offered to ISO/IEC JTC 1/SC 32; the first measured account of parthood consistency in the datasets robot-learning models are trained on; a merged, ontology-aligned corpus with corrected annotations and proved mappings; a reusable audit toolkit applicable to any hierarchical annotation (CAD assemblies, building information models, medical image part labels); two papers co-authored with the host.

**Impact.** For robotics, benchmark quality and an interpretable failure signal for learned policies. For AI assurance, machine-checkable evidence about training data of the kind the EU AI Act's Annex I obligations for AI in machinery and robots (from 2 August 2028 [confirm current date]) and the NIST AI Risk Management Framework describe [20]; a German host places the work where such evidence will first be demanded. For knowledge representation, an empirical validation of mereological pluralism at a scale the philosophical literature has never had.

**Independence.** The outline is my own. Its basis is the constitution and pluralism theory of which I am first author [7, 8]; its objectives, datasets and experiments appear neither in my doctoral thesis (knowledge-system architecture), nor in my current Harvard work, nor in [the Toronto laboratory's programmes on ontologies for the Physical Turing Test and commonsense cobotics — confirm against current grants], which do not audit robot-learning datasets or train policies. The stay is in a new academic environment and continues my own post-doctoral theory.

**Why this host and why Germany.** The verification methodology I use was developed in Toronto and I bring it with me. What I cannot bring is the validation instrument: a deployed knowledge base that represents object parts for real robots, a group that generates and consumes part-level robot data, and the everyday-manipulation science that gives the ontology its competency questions. These are concentrated in the host's group [and the CRC EASE programme — confirm]; Germany also hosts a strong applied-ontology community and the DIN mirror committee to ISO/IEC JTC 1/SC 32 [confirm]. The host's laboratory gives O1 its validation instrument, O2 a second body of real robot data and O3 a platform; the host receives a verified ontology aligned with its own representations, an audit of the datasets its systems train on, the toolkit and co-authorship. After the stay I intend to maintain the collaboration through joint supervision of the Theme 3 follow-on experiments and a joint proposal [DFG / Humboldt alumni instrument — confirm], and to carry the toolkit into [my next position — per the sequencing decision].

## Bibliography

1. ISO/IEC 21838-4:2023. *Information technology — Top-level ontologies (TLO) — Part 4: TUpper.* ISO/IEC JTC 1/SC 32.
2. Grüninger, M., Hahmann, T., Hashemi, A., Ong, D., Özgövde, A. (2012). Modular first-order ontologies via repositories. *Applied Ontology* 7(2), 169–209.
3. Grüninger, M., Fox, M. S. (1995). Methodology for the design and evaluation of ontologies. *IJCAI-95 Workshop on Basic Ontological Issues in Knowledge Sharing.*
4. Grüninger, M. (2004). Ontology of the Process Specification Language. In Staab, S., Studer, R. (eds), *Handbook on Ontologies*, Springer, 575–592. See also ISO 18629.
5. Simons, P. (1987). *Parts: A Study in Ontology.* Oxford University Press.
6. Casati, R., Varzi, A. C. (1999). *Parts and Places: The Structures of Spatial Representation.* MIT Press.
7. Ru, Y., Grüninger, M. (2026, submitted). Material constitution as a parthood-preserving mapping between mereologies. *Synthese.*
8. Ru, Y., Grüninger, M. (2026, submitted). [Exact title — mereological pluralism validation]. *Synthese.*
9. Mo, K., Zhu, S., Chang, A. X., Yi, L., Tripathi, S., Guibas, L. J., Su, H. (2019). PartNet: A large-scale benchmark for fine-grained and hierarchical part-level 3D object understanding. *CVPR 2019.*
10. Xiang, F., Qin, Y., Mo, K., et al. (2020). SAPIEN: A simulated part-based interactive environment. *CVPR 2020.*
11. Geng, H., Xu, H., Zhao, C., et al. (2023). GAPartNet: Cross-category domain-generalizable object perception and manipulation via generalizable and actionable parts. *CVPR 2023.*
12. AgiBot World Contributors (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. *arXiv preprint* [confirm final venue].
13. Open X-Embodiment Collaboration (2024). Open X-Embodiment: Robotic learning datasets and RT-X models. *ICRA 2024.*
14. Khazatsky, A., et al. (2024). DROID: A large-scale in-the-wild robot manipulation dataset. *RSS 2024.*
15. [PartNet-Ensembled — confirm citation and venue.]
16. Beetz, M., Beßler, D., Haidu, A., Pomarlan, M., Bozcuoğlu, A. K., Bartels, G. (2018). KnowRob 2.0 — A 2nd generation knowledge processing framework for cognition-enabled robotic agents. *ICRA 2018.*
17. Collaborative Research Centre EASE — Everyday Activity Science and Engineering, University of Bremen (DFG CRC 1320) [cite the host's most relevant recent paper here once the host is confirmed].
18. de Moura, L., Bjørner, N. (2008). Z3: An efficient SMT solver. *TACAS 2008*, LNCS 4963, 337–340.
19. McCune, W. (2005–2010). Prover9 and Mace4. https://www.cs.unm.edu/~mccune/prover9/
20. Regulation (EU) 2024/1689 (Artificial Intelligence Act), Annex I; NIST AI 100-1, *AI Risk Management Framework* (2023).
