# Verified mereological ontologies for object–part representation in physical AI

UC President's Postdoctoral Fellowship Program 2027–28 — Research Proposal. Applicant: Yi Ru. Proposed mentor: [Prof. Hao Su, Computer Science and Engineering, UC San Diego — confirm he still holds a tenured UCSD appointment (an April 2026 press report suggested he might leave), and that he agrees] (alternative: [a tenured BAIR faculty member, UC Berkeley — name]). PDF header on every page: "Ru, Yi — Research Proposal" [confirm the header convention in the 2027–28 application instructions].

Funder limit: 700–1,000 words; references, citations, formulas and graphics are excluded, and "the review committee may not consider proposals that exceed the word limit." Count (2026-09-26, §1–§5 only): 1,014 whitespace tokens as drafted, of which 21 are citation numbers (excluded) and about 35 sit in [brackets] that shrink when filled — expected upload count ≈955 words. Recount the exported PDF. Cut order if over: the "Secondary hypothesis" sentence in Theme 3; the second open question of Theme 2; the "segmentation mask" sentence in §2. Never cut the success tests in §2 or the five-gaps sentence in §3.

---

## 1. Recent Progress

An ontology is a computer-interpretable specification of the terms an agent uses and what they mean [1]. I axiomatize ontologies of physical objects as first-order theories and verify them: every claim is a theorem or a counter-model. I was a core contributor to ISO/IEC 21838-4:2023, the international standard for the TUpper top-level ontology [2] [role wording to confirm with Prof. Grüninger]. With M. Grüninger I developed a theory of material constitution as a parthood-preserving mapping between mereologies, and a validation of mereological pluralism, checked with automated provers and model finders (two first-authored *Synthese* submissions [3, 4]); it states exactly when two part decompositions of one object are compatible. My Toronto doctoral thesis developed an architecture in which a verified ontology governs an AI system's data model, learned models and simulation layer. As a founding-team member of two companies I shipped ontology-governed data-integration systems, and I co-founded a 3D-dataset company for embodied AI.

## 2. Objectives

Robot-learning datasets — PartNet [5], PartNet-Mobility and SAPIEN [6], GAPartNet [7], AgiBot World [8], Open X-Embodiment [9], DROID [10] — annotate objects as part hierarchies with kinematic, functional and visual labels. Each defines "part" operationally: a segmentation mask in one, a movable link in another, an actionable region in a third. Nothing requires a dataset or learned model to satisfy the axioms of parthood, no principled mapping links the vocabularies, and pooled training silently mixes them. The costs — poor transfer across vocabularies, brittle generalization to new categories — are unmeasured because there has been no specification to measure against. The long-term challenge:

*Can the part-level representations that robot-learning systems learn be shown to satisfy the axioms of parthood that humans use, and does enforcing those axioms improve generalization?*

Three objectives, each with a test of success:

1. **Ontology as specification.** Axiomatize a modular first-order ontology of rigid, articulated, functional and assembly parts extending TUpper, with the Process Specification Language (PSL) [11] for state change under manipulation. Success: every module proved consistent, with representation theorems for at least the PartNet and PartNet-Mobility schemas (Year 1).
2. **Ontology as audit.** Check the six datasets' annotation hierarchies against the ontology. Success: the first quantitative measurement of parthood consistency in robot datasets (violation rates by axiom family), with corrected annotations and provably meaning-preserving cross-dataset mappings released openly (Year 1).
3. **Ontology as inductive bias.** Train part-aware manipulation policies under ontology constraints. Success: a measured effect, positive or null, on success in held-out PartNet-Mobility categories against the same policies trained without constraints (Year 2).

## 3. Literature Review

Mereology is extensively axiomatized [12] and COLORE's mereotopologies are verified first-order theories [13, 14], but no verified ontology separates the rigid, articulated, functional and assembly senses of "part" that coexist in robot data. The closest prior work, the ontological analysis of vision benchmarks in Prof. Grüninger's laboratory [14], asks which mereotopologies the static part decompositions of ShapeNet and PartNet presuppose; it does not treat articulated, functional or assembly parthood, parthood change under manipulation, real-robot corpora, dataset-scale audit or cross-dataset alignment. Those five gaps make this program mine, distinct from his and from my thesis. Neuro-symbolic methods impose logical constraints as losses [15], but for parthood the constraints were never derived from a verified theory, so a violation could mean a bad model or a bad axiom.

## 4. Methodology

Ontologies follow the lifecycle methodology of [1] and COLORE verification [13]: each module's models are characterized up to isomorphism and compared with the intended models, keeping verification (do the models match the intended ones?) distinct from validation (are the intended models right?). The annotation schemas supply the competency questions.

**Theme 1: Parts (O1).** *Which parthood axioms do dataset decompositions presuppose, and are they jointly satisfiable?* Project 1.1: the four part modules, with PSL fluents for attachment, detachment and articulation. Project 1.2: for each dataset schema, a translation definition and a Prover9 proof that its intended models are models of the ontology, or a Mace4 counter-model. Open questions: Do kinematic, functional and visual decompositions need distinct parthood relations, or one relation with constraints? (Y1) Is constitution — a kinematic link versus its mesh — definable in the parts ontology? (Y1)

**Theme 2: Audit (O2).** *How often, and where, is parthood violated in the data physical-AI models learn from?* Project 2.1: Datalog/SMT rules compiled from the axioms check millions of part instances; theorem proving handles residual hard cases; UNKNOWN and timeout are reported, not hidden. Project 2.2: cross-dataset mappings made meaning-preserving by the theorems of 1.2; corrected annotations; a merged, ontology-aligned corpus. Open questions: Which axiom families fail most, and do failures concentrate by category or by annotation source? (Y1) Do simulated (PartNet-Mobility) and real-robot (AgiBot World, DROID) corpora differ? (Y1)

**Theme 3: Learning (O3).** *Does ontology-consistent training improve generalization to unseen categories?* Project 3.1: differentiable relaxations of parthood constraints as auxiliary losses [15]; constraint-guided augmentation for underrepresented categories. Project 3.2: ontology-violation rate reported alongside task success, using the released baselines of [6, 7], in SAPIEN [and a second simulator — confirm with the mentor], with confidence intervals and ablations by axiom family. Secondary hypothesis: violation rate predicts failure. If only one year is funded, 3.2 evaluates existing policies and 3.1 covers one axiom family. (Y2)

## 5. Impact

For knowledge representation, the program tests at dataset scale whether a verified ontology can govern learned systems. For robotics, it releases corrected, aligned data and an interpretable failure signal of the kind robot-assurance regimes will require (EU AI Act Annex I [2 Aug 2027 per Article 113 vs 2 Aug 2028 per the company deck — resolve before use]; NIST AI RMF). At [UC San Diego] the work sits with the group that maintains SAPIEN and PartNet-Mobility [confirm]: I bring the specification and audit method; the group brings data, simulator and robotics community; corrections flow back into the datasets. I will co-supervise [number — agree with the mentor] undergraduate researchers on Theme 2. The ontology goes to COLORE and ISO/IEC JTC 1/SC 32, and the fellowship gives me the independent program on which to build a faculty career in knowledge representation for engineering systems.

## Bibliography

(Not counted toward the word limit. [Verify each entry against the source before upload.])

1. Grüninger, M., Fox, M. S. (1995). Methodology for the design and evaluation of ontologies. IJCAI-95 Workshop on Basic Ontological Issues in Knowledge Sharing.
2. ISO/IEC 21838-4:2023. Information technology — Top-level ontologies (TLO) — Part 4: TUpper. ISO/IEC JTC 1/SC 32.
3. Ru, Y., Grüninger, M. (2026, submitted). Material Constitution as a Parthood-Preserving Mapping between Mereologies. *Synthese*.
4. Ru, Y., Grüninger, M. (2026, submitted). [Exact title — mereological pluralism validation paper]. *Synthese*.
5. Mo, K., Zhu, S., Chang, A. X., Yi, L., Tripathi, S., Guibas, L. J., Su, H. (2019). PartNet: A large-scale benchmark for fine-grained and hierarchical part-level 3D object understanding. CVPR.
6. Xiang, F., Qin, Y., Mo, K., Xia, Y., Zhu, H., Liu, F., Liu, M., Jiang, H., Yuan, Y., Wang, H., Yi, L., Chang, A. X., Guibas, L. J., Su, H. (2020). SAPIEN: A SimulAted Part-based Interactive ENvironment. CVPR.
7. Geng, H., Xu, H., Zhao, C., Xu, C., Yi, L., Huang, S., Wang, H. (2023). GAPartNet: Cross-category domain-generalizable object perception and manipulation via generalizable and actionable parts. CVPR.
8. AgiBot World Colosseo team (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. arXiv:2503.06669. [verify author list and identifier]
9. Open X-Embodiment Collaboration (2024). Open X-Embodiment: Robotic learning datasets and RT-X models. IEEE ICRA.
10. Khazatsky, A., et al. (2024). DROID: A large-scale in-the-wild robot manipulation dataset. Robotics: Science and Systems.
11. ISO 18629-1:2004. Industrial automation systems and integration — Process specification language — Part 1: Overview and basic principles.
12. Varzi, A. C. (2019). Mereology. *Stanford Encyclopedia of Philosophy*.
13. Grüninger, M., Hahmann, T., Hashemi, A., Ong, D., Özgövde, A. (2012). Modular first-order ontologies via repositories. *Applied Ontology*, 7(2), 169–209.
14. [Published Semantic Technologies Laboratory papers on (a) verification of the COLORE mereotopologies and (b) ontological analysis of vision benchmarks (ShapeNet, PartNet) — exact citations from Prof. Grüninger. Never cite his NSERC Discovery Grant proposals (STRATEGY.md §4, rule 4). If (b) is unpublished, change the §3 sentence to "ongoing work in Prof. Grüninger's laboratory" and cite only (a).]
15. Xu, J., Zhang, Z., Friedman, T., Liang, Y., Van den Broeck, G. (2018). A semantic loss function for deep learning with symbolic knowledge. ICML.
