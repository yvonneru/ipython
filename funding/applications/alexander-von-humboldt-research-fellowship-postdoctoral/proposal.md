# Research outline — Humboldt Research Fellowship for postdoctoral researchers

**Applicant:** Dr. Yi Ru (PhD, Information Engineering, University of Toronto, 2025; currently postdoctoral researcher, Harvard Medical School [laboratory])
**Host:** Prof. [name], [institute], [University of Bremen / University of Osnabrück / TU Dresden — confirm]
**Title:** Verified mereological ontologies for object–part representation in physical AI
**Intended duration and division of visits:** 12 months, one continuous stay, [start month] 2027 [confirm sequencing; confirm whether the postdoctoral track permits division into stays]

Format note: the Foundation asks for approximately five pages in total including the bibliography, with the current state of research (about five relevant publications) taking at most one page, and for the outline to be agreed with the host before submission. This draft is written to that specification; the host's edits go in before it is uploaded.

## 1. Summary

Robot-learning systems are trained on datasets that describe objects as hierarchies of parts. No dataset, and no model trained on one, is required to satisfy the axioms of parthood, and no dataset states how its part vocabulary relates to any other's. I propose to supply the missing semantics: a formally verified first-order ontology of physical object parts, built as an extension of the ISO/IEC 21838-4 top-level ontology, and used first as a *specification*, then as an *audit* of the part-level datasets on which manipulation policies are trained, and then as an *inductive bias* on the policies themselves. The German stay is sized to the first two uses and to a first controlled experiment on the third, in collaboration with the host's knowledge-based robotics group. The outputs are a verified ontology deposited in an open repository, the first quantitative measurement of parthood consistency across robot datasets, a merged and ontology-aligned corpus, and an audit toolkit that the host's laboratory and the wider field can reuse.

## 2. Current state of research

An ontology is a computer-interpretable specification of what terms an agent uses and what they mean; when it is axiomatized in first-order logic, its consequences can be checked by a theorem prover and its unintended models found by a model finder. Four bodies of work define the starting point.

**Verified top-level and process ontologies.** ISO/IEC 21838-4:2023 standardizes TUpper, a top-level ontology whose modules for time, mereotopology, location, units of measure and process are each verified: the models of the axioms are characterized up to isomorphism and compared with the intended models [1]. TUpper is developed with the COLORE repository of first-order ontologies (2,580 theories in Common Logic, ISO 24707) and its methodology of competency questions, design by reuse and ontology merging [2, 3]. The Process Specification Language ontology (ISO 18629) supplies a verified theory of activities, occurrences and fluents for reasoning about state change [4]. I was a core contributor to the axiomatization and verification of TUpper within ISO/IEC JTC 1/SC 42 [confirm role wording].

**Mereology and material constitution.** Classical extensional mereology [5, 6] assumes a single parthood relation. Ordinary objects, and every annotated object in a robot dataset, carry several: a kinematic decomposition into links, a functional decomposition into handles and lids, a visual decomposition into segments. With M. Grüninger I have developed an account of material constitution as a parthood-preserving mapping between distinct mereologies and a validation of mereological pluralism by the same verification methods used for ontologies; two papers are under review at Synthese [7, 8]. The theory states, as first-order axioms, what must hold for two part decompositions of the same object to be compatible. That is exactly the question the datasets leave open.

**Part-level datasets for robot learning.** PartNet annotates 26,671 ShapeNet objects with fine-grained, hierarchical part decompositions [9]; PartNet-Mobility, released with the SAPIEN simulator, adds articulated links and joints for 2,346 objects [10]; GAPartNet defines nine classes of "generalizable and actionable parts" with pose annotations for manipulation [11]; real-robot corpora such as AgiBot World [12], Open X-Embodiment [13] and DROID [14] add episodes whose object structure is annotated inconsistently or not at all; PartNet-Ensembled [15, confirm citation] pools several of these. Each dataset defines "part" operationally; none states axioms; none maps its labels to another's. Pooled training silently mixes vocabularies. Poor transfer across part vocabularies and brittle generalization to new object categories are observed [11, 13] but have never been measured against a specification, because there has been none to measure against.

**Knowledge-based robotics in Germany.** The host's community has built the most complete knowledge infrastructure for everyday manipulation: the KnowRob knowledge-processing system and the CRC EASE programme on everyday activity science [16, 17], which represent objects, parts, affordances and actions in a robot's knowledge base and query them during task execution. Those knowledge bases encode part structure that is, to my knowledge, asserted rather than verified against a mereology, and that has not been aligned with the part vocabularies of the learning datasets above. [Replace or extend this paragraph with the host's own recent work once the host is confirmed.]

**The gap.** Verified mereological theory exists; large part-level datasets exist; knowledge-based robot architectures that consume part structure exist. Nothing connects them: there is no verified ontology of object parts that extends a standardized top-level ontology, no audit of any robot dataset against one, and no measurement of whether enforcing parthood axioms changes what a policy learns.

## 3. Objectives

The programme is motivated by the following long-term challenge:

*Can the part-level representations that robot-learning systems learn be shown to satisfy the axioms of parthood that humans use, and does enforcing those axioms improve generalization?*

The fellowship addresses three objectives; the German stay completes O1 and O2 and delivers the first experiment of O3.

1. **Ontology as specification (O1).** Axiomatize and verify a modular first-order ontology of physical object parts (rigid, articulated, functional, assembly) as an extension of TUpper integrated with PSL for state change under manipulation, with representation theorems relating it to the annotation schemas of the major datasets and to the host's knowledge base.
2. **Ontology as audit (O2).** Build a two-tier audit pipeline (Datalog/SMT for bulk instances; first-order theorem proving for residual cases) and produce the first quantitative measurement of parthood consistency in PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled and AgiBot World, with corrected annotations, provably meaning-preserving cross-dataset mappings and a merged corpus.
3. **Ontology as inductive bias (O3).** Test, in the host's simulation and robot environment, whether ontology-consistent training data and parthood constraints expressed as auxiliary losses improve generalization of part-aware manipulation policies to unseen object categories, and whether the rate of ontology violations in a policy's inferred object structure predicts task failure.

## 4. Methodology

All ontologies are designed with the ontology lifecycle methodology of competency questions, verification and validation practised in COLORE [2, 3]: I characterize the models of each module up to isomorphism, prove consistency and non-triviality with Prover9 and Mace4, and establish the relationships between modules (extension, conservative extension, definable equivalence) as theorems. Verification asks whether the models of the axioms are the intended models; validation asks whether the intended models are the right ones, and here the validation instrument is the data: every competency question is a question that a dataset either answers consistently or does not. The work is organized in three themes; each project lists open research questions that will be answered by a theorem, a counter-model or a measurement, tagged with the quarter of the stay in which they are due.

### Theme 1 — Parts (O1)

*Given an object annotated under several part decompositions, state as first-order axioms when the decompositions are compatible and what follows for the object under manipulation.*

**Project 1.1 — Parts ontology.** A modular ontology with separate mereologies for rigid parts, articulated parts (links and joints, with PSL activities for joint motion), functional parts (affordance-bearing regions in the sense of GAPartNet) and assemblies, each an extension of TUpper's mereotopology, related to one another by the constitution mappings of [7, 8]. Every module is verified; the ontology is written in Common Logic and deposited in COLORE and in the host's repository.
- Open research questions: Are the kinematic, functional and visual part relations in the datasets three mereologies related by parthood-preserving mappings, or does one of them fail to be a mereology at all? (Q1) Which axioms of extensional mereology must be weakened for articulated objects whose parts move relative to one another? (Q1) Is material constitution definable from parthood plus PSL fluents, or does it require a primitive? (Q2)

**Project 1.2 — Representation theorems for annotation schemas.** For each dataset schema, and for the host's knowledge base, a translation definition into the ontology's signature and a theorem stating which axioms the schema entails and which it violates by construction.
- Open research questions: Which dataset schemas are definably equivalent to a fragment of the parts ontology, and which are strictly weaker? (Q2) Does the host's knowledge base [KnowRob / confirm] entail the parthood axioms, and if not, which counter-models does Mace4 return? (Q2)

### Theme 2 — Audit (O2)

*Translate every part instance in a dataset into the ontology and report, at scale, where the data violate the axioms and which cross-dataset label mappings preserve meaning.*

**Project 2.1 — Two-tier audit pipeline.** Bulk checking by Datalog rules and an SMT encoding (Z3 [18]) of the decidable fragment, handling millions of part instances; first-order theorem proving for the residual cases; UNKNOWN and timeout reported as first-class outcomes rather than silently dropped. The pipeline is engineered as a versioned toolkit with adapters for the dataset formats (PartNet JSON hierarchies, SAPIEN URDF, GAPartNet annotations, LeRobot/RLDS episodes).
- Open research questions: What fraction of parthood violations in each dataset is decidable in the SMT fragment, and what remains for the prover? (Q2) Does violation density differ systematically by object category, by annotator source or by dataset? (Q3)

**Project 2.2 — Cross-dataset alignment and merged corpus.** Label mappings between datasets are accepted only when the mapping is proved parthood-preserving under the constitution theory; the aligned corpus and the corrected annotations are released with the proofs. This is the first quantitative audit of parthood consistency in robot datasets.
- Open research questions: Which pairs of part vocabularies admit a meaning-preserving mapping at all, and where does pooling necessarily introduce inconsistency? (Q3) Does the audit generalize without change to the host's own robot logs [confirm data available at the host]? (Q3)

### Theme 3 — Learning (O3)

*Does a policy trained on ontology-consistent data, or constrained by the ontology, generalize better to unseen object categories, and does its violation rate predict failure?*

**Project 3.1 — Ontology-consistent training and verification-in-the-loop evaluation.** Three interventions on a part-aware manipulation policy in SAPIEN [10] and the host's platform [confirm second simulator or robot]: (a) training on the audited and aligned corpus versus the raw pooled corpus; (b) differentiable relaxations of parthood constraints as auxiliary losses on inferred part relations; (c) an evaluation protocol that reports ontology-violation rate alongside task success, with ablations by axiom family. Matched comparisons on held-out PartNet-Mobility categories with confidence intervals.
- Open research questions: Does training on the aligned corpus improve success on held-out categories relative to raw pooling? (Q4) Is a policy's ontology-violation rate a predictor of task failure, and therefore an interpretable failure signal? (Q4) Which axiom families carry the effect? (Q4, and continued after the stay)

## 5. Work and time schedule (12 months, [start month] 2027 – [end month] 2028)

| Quarter | Work | Deliverable |
|---|---|---|
| Q1 (months 1–3) | Parts ontology modules; verification; first representation theorems for PartNet and PartNet-Mobility schemas; alignment with the host's knowledge base | Verified ontology v0.9 in COLORE and the host's repository; technical report |
| Q2 (months 4–6) | Remaining schema theorems (GAPartNet, AgiBot World, host data); audit pipeline v1; first audit of two datasets | Audit pipeline released; audit results for two datasets; ontology v1.0 |
| Q3 (months 7–9) | Audit of all five datasets; cross-dataset mappings with proofs; merged corpus | Audit and data paper submitted [venue: robotics or AI data track — agree with host]; public data release |
| Q4 (months 10–12) | Policy experiments in SAPIEN and the host's platform; verification-in-the-loop evaluation; write-up; plan for continuation | Methods paper draft; ontology contributed to ISO/IEC JTC 1/SC 42 as a liaison document [confirm process]; joint follow-on proposal with the host |

Contingencies: if the SMT fragment covers less of the data than expected, Q2 shifts effort to the prover tier and the audit is reported on a sampled subset with stated coverage; if the host's platform is unavailable, Q4 runs entirely in SAPIEN. The theory work of Theme 1 has no external dependencies and starts on day one.

## 6. Expected results, impact and the choice of host

**Results.** A verified parts ontology under an open licence, deposited in COLORE and offered to the host's repository and to ISO/IEC JTC 1/SC 42; the first measured account of parthood consistency in the datasets that current robot-learning models are trained on; a merged, ontology-aligned corpus with corrected annotations and proved mappings; a reusable audit toolkit applicable to any hierarchical annotation (CAD assemblies, building information models, medical image part labels); two papers, one on the audit and data and one on the methods, both co-authored with the host.

**Impact.** For robotics, benchmark quality and an interpretable failure signal for learned policies. For AI assurance, machine-checkable evidence about training data of the kind that the EU AI Act's Annex I obligations for AI in machinery and robots (applicable from 2 August 2028) will require and that the NIST AI Risk Management Framework describes; a German host places this work inside the jurisdiction where that evidence will first be demanded. For knowledge representation, an empirical validation of mereological pluralism at a scale the philosophical literature has never had.

**Why this host and why Germany.** The verification methodology I use was developed in Toronto; the knowledge-based robot architectures that would consume a verified parts ontology, and the everyday-manipulation science that gives it its competency questions, are concentrated in Germany, in the host's group [and the CRC EASE programme — confirm]. Germany is also the European centre of applied formal ontology and of the standards work (ISO/IEC JTC 1/SC 42, DIN) that the ontology will feed. Working in the host's laboratory gives O1 its validation instrument (a deployed knowledge base and robots that act on it), O2 a second body of real robot data, and O3 a platform; it gives the host a verified ontology aligned with their own representations and an audit of the datasets their systems are trained on. The stay is not a continuation of my doctoral work, which was on knowledge-system architecture, and it is in a new academic environment; it is the empirical continuation of my own theoretical work on constitution and pluralism. After the stay I intend to maintain the collaboration through joint supervision of the follow-on experiments of Theme 3 and through a joint proposal [DFG / Humboldt alumni return fellowship — confirm], and to carry the toolkit into my planned position in Toronto.

## Bibliography

1. ISO/IEC 21838-4:2023. *Information technology — Top-level ontologies (TLO) — Part 4: TUpper.* ISO/IEC JTC 1/SC 42.
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
