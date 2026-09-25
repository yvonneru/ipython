# Verified mereological ontologies for object–part representation in physical AI

UC President's Postdoctoral Fellowship Program 2027–28 — Research Proposal. Applicant: Yi Ru. Proposed mentor: [Prof. Hao Su, Computer Science and Engineering, UC San Diego — confirm agreement and tenured status] (alternative: [BAIR faculty member, UC Berkeley — name]). Funder limit: 700–1,000 words; references, citations, formulas and graphics are excluded from the count. Body below is about 985 words (headings and bracketed notes included); the header lines above are not part of the upload. Cut order if the exported text exceeds 1,000 words: the last sentence of §3, then the second open research question of Theme 2, then the CAD/BIM/medical sentence in §5.

## 1. Recent Progress

An ontology is a computer-interpretable specification of the terms an agent uses and what they mean [1]. My research axiomatizes ontologies of physical objects as theories in first-order logic and verifies them by automated reasoning. I was a core contributor to ISO/IEC 21838-4:2023, the international standard for the TUpper top-level ontology, each of whose modules is machine-verified [2]. With M. Grüninger I developed a theory of material constitution as a parthood-preserving mapping between mereologies, and a validation of mereological pluralism, in which consistency and non-triviality are established with Prover9 and Mace4 [3, 4]; together they state exactly when two part decompositions of one object are compatible. My doctoral thesis at the University of Toronto developed an architecture in which a verified ontology governs the data model, the learned models and the simulation layer of an AI system. I have carried the same discipline into production: ontology-governed data-integration systems at two companies I co-founded, and a structured 3D-dataset business serving embodied AI.

## 2. Objectives

Robot-learning datasets — PartNet [5], PartNet-Mobility and SAPIEN [6], GAPartNet [7], AgiBot World [8], Open X-Embodiment [9], DROID [10] — annotate objects as hierarchies of parts with kinematic, functional and visual labels. Each defines "part" operationally; no dataset or learned model is required to satisfy the axioms of parthood; there is no principled mapping between part vocabularies; pooled training silently mixes them. Poor transfer across vocabularies and brittle generalization to new categories are observed but unmeasured, because there has been no specification to measure against. The program is motivated by the following long-term challenge:

*Can the part-level representations that robot-learning systems learn be shown to satisfy the axioms of parthood that humans use, and does enforcing those axioms improve generalization?*

The proposed research has three primary objectives:

1. **Ontology as specification.** Axiomatize and verify a modular first-order ontology of physical object parts as an extension of TUpper integrated with the Process Specification Language (PSL) [11] for state change under manipulation.
2. **Ontology as audit.** Translate annotation hierarchies into ontology instances and check them, producing the first quantitative measurement of parthood consistency in robot datasets, corrected annotations and provably meaning-preserving cross-dataset mappings.
3. **Ontology as inductive bias.** Train part-aware manipulation policies under ontology constraints and measure the effect on generalization to unseen categories.

## 3. Literature Review

Mereology is extensively axiomatized [12], and the mereotopologies within TUpper are verified up to isomorphism [2], but no verified ontology covers rigid, articulated, functional and assembly parts together with state change under manipulation. Ontological analysis of vision datasets has asked which mereotopology is implicit in PartNet's decompositions [13]; no robot dataset has been checked against a formal specification. Neuro-symbolic methods impose logical constraints as losses, but for parthood the constraints have never been derived from a verified theory, so a violation could mean a bad model or a bad axiom.

## 4. Methodology

Ontologies are designed with the ontology lifecycle methodology of [1] and the COLORE repository techniques [14]: competency questions come from the application; every module is verified — its models are characterized up to isomorphism and compared with the intended models; and verification (models of the axioms versus intended models) is kept distinct from validation (whether the intended models are the right ones). Here the datasets' annotation schemas supply the competency questions.

**Theme 1: Parts (Objective 1).** *Which axioms of parthood do the part decompositions in robot datasets presuppose, and are they jointly satisfiable?*
Project 1.1, Parts ontology: modules for rigid, articulated (joint-linked), functional and assembly parts as TUpper extensions, with PSL fluents for attachment, detachment and articulation. Project 1.2, Representation theorems: for each dataset schema, a translation definition and a theorem that the schema's intended models are models of the ontology, proved in Prover9, with Mace4 counter-models where the theorem fails. Open research questions: Do kinematic, functional and visual decompositions require distinct parthood relations, or one relation with constraints? (Y1) Is constitution — a kinematic link versus its mesh — definable within the parts ontology? (Y1)

**Theme 2: Audit (Objective 2).** *What is the rate and pattern of parthood-axiom violations in the datasets physical-AI models are trained on?*
Project 2.1, Two-tier pipeline: Datalog/SMT rules for millions of part instances; first-order theorem proving for residual hard cases; UNKNOWN and timeout reported as first-class outcomes. Project 2.2, Alignment: cross-dataset label mappings made meaning-preserving by the theorems of 1.2; corrected annotations; a merged, ontology-aligned corpus. Open research questions: Which axiom families are violated most, and do violations concentrate in categories or in annotation sources? (Y1) Can a schema's violation pattern be predicted from the schema alone? (Y2)

**Theme 3: Learning (Objective 3).** *Does ontology-consistent training improve generalization of manipulation policies to unseen categories?*
Project 3.1: differentiable relaxations of parthood constraints as auxiliary losses on inferred part relations; constraint-guided augmentation that synthesizes ontology-consistent part configurations for underrepresented categories. Project 3.2, Verification-in-the-loop evaluation: ontology-violation rate reported alongside task success, in SAPIEN [6] [and a second simulator or benchmark suite — confirm with the mentor], with ablations by axiom family. Hypotheses: ontology-consistent training improves generalization to held-out PartNet-Mobility categories; violation rate predicts task failure; pooled, ontology-aligned data transfers across part vocabularies. (Y2)

## 5. Impact

Near term, the audit tells the field what its models are trained on and releases corrected, aligned data; the ontology-violation rate is an interpretable failure signal that can serve as machine-checkable evidence under the assurance regimes now arriving for robots (EU AI Act Annex I, from August 2028; NIST AI RMF). The audit method generalizes to CAD assemblies, building models and medical-image part labels. At [UC San Diego] the work would be done with the group that maintains SAPIEN and PartNet-Mobility [confirm], so corrections flow into the datasets themselves. Long term, the ontology will be contributed to COLORE and to ISO/IEC JTC 1/SC 42, giving physical AI a shared, verified vocabulary of parts, and the fellowship gives me the independent program on which I intend to build a faculty career in knowledge representation for engineering systems.

## Bibliography

(Not counted toward the word limit. [Verify each entry against the master reference list before upload.])

1. Grüninger, M., Fox, M. S. (1995). Methodology for the design and evaluation of ontologies. IJCAI-95 Workshop on Basic Ontological Issues in Knowledge Sharing.
2. ISO/IEC 21838-4:2023. Information technology — Top-level ontologies (TLO) — Part 4: TUpper. ISO/IEC JTC 1/SC 42.
3. Ru, Y., Grüninger, M. (2026, submitted). Material Constitution as a Parthood-Preserving Mapping between Mereologies. *Synthese*.
4. Ru, Y., Grüninger, M. (2026, submitted). [Exact title — mereological pluralism validation paper]. *Synthese*.
5. Mo, K., Zhu, S., Chang, A. X., Yi, L., Tripathi, S., Guibas, L. J., Su, H. (2019). PartNet: A large-scale benchmark for fine-grained and hierarchical part-level 3D object understanding. CVPR.
6. Xiang, F., Qin, Y., Mo, K., Xia, Y., Zhu, H., Liu, F., Liu, M., Jiang, H., Yuan, Y., Wang, H., Yi, L., Chang, A. X., Guibas, L. J., Su, H. (2020). SAPIEN: A SimulAted Part-based Interactive ENvironment. CVPR.
7. Geng, H., Xu, H., Zhao, C., Xu, C., Yi, L., Huang, S., Wang, H. (2023). GAPartNet: Cross-category domain-generalizable object perception and manipulation via generalizable and actionable parts. CVPR.
8. AgiBot World Colosseo team (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. arXiv:2503.06669. [verify author list]
9. Open X-Embodiment Collaboration (2023). Open X-Embodiment: Robotic learning datasets and RT-X models. arXiv:2310.08864.
10. Khazatsky, A., et al. (2024). DROID: A large-scale in-the-wild robot manipulation dataset. Robotics: Science and Systems.
11. ISO 18629-1:2004. Industrial automation systems and integration — Process specification language — Part 1: Overview and basic principles.
12. Varzi, A. C. (2019). Mereology. *Stanford Encyclopedia of Philosophy*.
13. Grüninger, M. Commonsense Cobotics. NSERC Discovery Grant proposal, Project 1.1 [cite the published form if one exists; otherwise cite as personal communication with the author's permission].
14. Grüninger, M., Hahmann, T., Hashemi, A., Ong, D., Özgövde, A. (2012). Modular first-order ontologies via repositories. *Applied Ontology*, 7(2), 169–209.
