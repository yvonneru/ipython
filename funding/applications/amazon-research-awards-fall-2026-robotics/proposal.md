# Verified Parthood: Automated Reasoning for Auditing and Constraining Part-Level Robot Manipulation Data

**Principal Investigator:** Prof. Michael Grüninger, Department of Mechanical and Industrial Engineering (Semantic Technologies Laboratory), University of Toronto
**Named postdoctoral researcher:** Dr. Yi Ru (PhD Information Engineering, University of Toronto, 2025; currently postdoctoral researcher, Harvard Medical School; joining MIE [April 2027 or later — confirm start])
**Call:** Amazon Research Awards, Fall 2026 — [Robotics / Automated Reasoning — select the topic once the call posts; the abstract has one alternate sentence for each]
**Requested:** [USD cash — see budget_and_timeline.md] cash gift plus [USD] AWS Promotional Credits; 12 months

**Format note (internal — delete before export).** The ARA proposal template (03.19.2025 version, checked 2026-09-25) prescribes: Abstract and Keywords; Significance of the research and prior work; Technical approach; Milestones with timeline estimates (datasets, code releases, technical reports); a one-page PI CV; maximum 3 pages excluding appendices. Some Spring 2026 calls allowed 4 pages. The body below is about 1,850 words including one table, roughly 3 pages at 10.5–11 pt single-spaced with 0.75 in margins; the bibliography is Appendix A and the PI CV (statement.md, Part A) is Appendix B. **Re-download the Fall 2026 template on 1 Oct 2026 and re-fit the headings.** If a 3-page limit binds, cut in this order: the "Relevance to Amazon" paragraph's last sentence; the *Open questions* lines in Themes 1 and 3; the decision-points sentence in §3; the third bullet of §1. The proposal is written in the PI's voice ("we"); Prof. Grüninger must approve every sentence attributed to his laboratory before submission.

---

## Abstract

Robot-learning datasets — PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment, DROID — annotate objects as hierarchies of parts with kinematic, functional and visual labels, and manipulation policies are trained on them in pooled form. Each dataset defines "part" operationally; none is required to satisfy the axioms of parthood; and there is no principled way to map labels across datasets, so pooled training silently mixes incompatible part vocabularies. The consequences — poor transfer across part vocabularies and brittle generalization to new object categories — are observed but have never been measured, because there has been no formal specification to measure against. We propose to supply that specification and to enforce it by automated reasoning. (1) We will axiomatize and verify a modular first-order ontology of physical object parts as an extension of TUpper (ISO/IEC 21838-4) integrated with the Process Specification Language, establishing consistency, non-triviality and representation theorems with Prover9, Mace4 and SMT. (2) A two-tier audit pipeline — Datalog/SMT for the bulk of the data, first-order theorem proving for residual hard cases — will translate annotation hierarchies into ontology instances and check them, yielding the first quantitative measurement of parthood consistency in robot datasets, corrected annotations, provably meaning-preserving cross-dataset mappings and a merged corpus. (3) We will use the ontology as an inductive bias on part-aware manipulation policies and test in SAPIEN whether ontology-consistent training improves generalization to unseen categories. [Robotics call: *The result is a cross-embodiment part schema whose consistency is a theorem.* / Automated Reasoning call: *The result is a deployed application of SMT and theorem proving to a data-quality problem at the scale of millions of part instances.*] All axioms, mappings, code and corrected annotations will be released under an open licence; the audit will run on AWS.

**Keywords:** automated reasoning; formal ontology; mereology; theorem proving; SMT; robot manipulation; articulated objects; dataset alignment; neuro-symbolic learning; data quality; ISO/IEC 21838.

## 1. Significance of the research and prior work

An ontology is a computer-interpretable specification that an agent, application or information resource uses to declare what terms it uses and what the terms mean. Physical AI is being built on a handful of large part-level datasets [5–11] whose annotation schemas were designed independently: a "part" is a segmentation label in one, a movable link in another, an actionable region in a third. Nothing requires the parts a model infers to form a consistent whole, nothing relates the part vocabularies of different datasets, and nothing lets a policy reason about why a part decomposition is wrong. Manipulation at fulfilment scale encounters far more object categories than any of these datasets contains, so whether a part representation transfers to an unseen category decides whether a policy trained on one catalogue can handle the next. Today that is settled by inspection. We propose to settle it by proof.

- **Verified first-order ontologies and COLORE (PI).** The PI's research has focussed on the axiomatization of ontologies as theories in first-order logic and on techniques for their design and verification [16, 17]. COLORE, an open repository of ontologies specified in Common Logic (ISO/IEC 24707) [19], holds 2,580 ontologies organized into hierarchies and is the testbed for design by reuse, merging and transfer. Every ontology is verified: its models are characterized up to isomorphism and compared with the intended models. The PI's work on mereotopology, time, location and units of measure (FOUnt, Distinguished Paper Award, FOIS 2018 [confirm citation]) is integrated into the upper ontology TUpper, published as ISO/IEC 21838-4:2023 [1]; the PSL ontology [12] supplies the verified theory of activities and state change reused here. The PI's current NSERC work applies ontological analysis to robotics — the minimal ontologies needed to specify task and motion planning problems, and the parthood relations implicit in ShapeNet and PartNet [14].
- **A machine-checked theory of parthood under constitution (named postdoc, with the PI).** Classical mereology assumes one parthood relation; ordinary objects seem to demand more. Dr. Ru's theory treats material constitution as a parthood-preserving mapping between distinct mereologies and validates the resulting pluralism with the techniques of ontology verification: first-order axioms, consistency and non-triviality by Prover9 and Mace4, and a proof that the mapping preserves the structure it must (two papers submitted to Synthese, 2026 [2, 3]). Given two part decompositions of one object, the theory says exactly what must hold for them to be compatible — the question robot datasets pose, where kinematic, functional and visual decompositions co-exist with no statement of how they relate.
- **Ontology-governed systems in production (named postdoc).** Dr. Ru's thesis [4] developed an architecture in which a verified ontology governs the data model, the learned models and the simulation layer; elements contributed to ISO/IEC 21838-4:2023, on which Dr. Ru is a core contributor within ISO/IEC JTC 1/SC 42 [confirm role wording]. As a founder of two technology companies Dr. Ru shipped ontology-governed data-integration systems and holds [number — confirm] patents in 3D recognition and reconstruction.

**Relevance to Amazon.** For automated reasoning, the audit is an industrial-scale application of SMT and theorem proving in which UNKNOWN and timeout are first-class outputs and the compiled fragment must be shown not to miss what the prover finds. For robotics, the deliverable is a cross-embodiment part schema whose consistency is a theorem, plus a failure signal — ontology-violation rate — computable before a policy is deployed. Machine-checkable evidence about training data is also what regulators are beginning to require (EU AI Act Annex I covers AI in machinery and robots from 2 August 2028).

## 2. Technical approach

The program is motivated by the following long-term challenge:

*Can the part-level representations that robot-learning systems learn be shown to satisfy the axioms of parthood that humans use, and does enforcing those axioms improve generalization?*

It has three primary objectives:

1. **Ontology as specification** — axiomatize and verify a modular first-order ontology of physical object parts (rigid, articulated, functional, assembly) as an extension of TUpper integrated with PSL for state change under manipulation.
2. **Ontology as audit** — translate the annotation hierarchies of PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled and AgiBot World into ontology instances, check them automatically, and derive cross-dataset mappings that are meaning-preserving by proof.
3. **Ontology as inductive bias** — use the verified ontology to shape part-aware manipulation policies and measure the effect on generalization to unseen object categories.

Ontologies are designed with the PI's lifecycle methodology [16] and the COLORE techniques [17], and verified: we characterize the models of each module up to isomorphism and decide whether they are the intended models. Competency questions come from the application — the queries an audit must answer ("Is any part annotated both as contained in and disjoint from another?" "Which PartNet-Mobility links correspond to GAPartNet actionable parts?") are the semantic requirements on the ontology.

**Theme 1 — Parts (Objective 1).** *Given the part vocabularies of the major robot datasets, specify a verified theory of which each vocabulary is a definable extension.* Project 1.1 axiomatizes rigid, articulated, functional and assembly parthood as Common Logic modules over the TUpper mereotopology; consistency and non-triviality are established by Prover9/Mace4, and module relationships (conservative extension, definable equivalence) are proved or refuted by counter-model. Project 1.2 applies the constitution mappings of [2, 3] to relate kinematic, functional and visual decompositions, yielding representation theorems that state when two decompositions are compatible. Project 1.3 integrates PSL so that parthood change under manipulation (detach, insert, open) is an activity occurrence with axiomatized preconditions and effects. *Open questions:* Are the parthood relations implicit in PartNet, PartNet-Mobility and GAPartNet definable in one mereology, or do they require distinct mereologies related by constitution mappings? (Ru, M3) Which classes of lattices and partial orderings characterize the models of the articulated-parthood module? (MASc1, M6)

**Theme 2 — Audit (Objective 2).** *Given an annotation hierarchy and the ontology, decide which axioms it violates, at dataset scale, with an explicit UNKNOWN.* Project 2.1 writes adapters from each native schema (and the LeRobot and RLDS formats of real-robot corpora) to ontology instances with per-part provenance. Project 2.2 builds the two-tier checker: the decidable fragment is compiled to Datalog and SMT (Z3 [20]) and run over millions of part instances on AWS; undecided instances go to Prover9/Mace4 under a time budget, and timeouts are reported as UNKNOWN rather than passed. Project 2.3 derives cross-dataset mappings from the Theme 1 theorems, proves each meaning-preserving, and assembles a merged, ontology-aligned corpus with corrected annotations. *Open questions:* Does the compiled SMT fragment miss violations the prover finds, and on which axiom families? (Ru, M6) What is each dataset's violation rate, and is it concentrated in particular categories or annotation sources? (Ru, M7)

**Theme 3 — Learning (Objective 3).** *Does a policy trained under the ontology generalize better, and does its violation rate predict its failures?* Project 3.1 compiles the parthood axioms to differentiable relaxations (semantic-loss and fuzzy-logic terms in the style of [15, 21, 22]) as auxiliary losses on the part relations a policy infers. Project 3.2 uses Mace4-generated models as constraint-guided augmentation, instantiating ontology-consistent part configurations for underrepresented categories in SAPIEN [6]. Project 3.3 defines a verification-in-the-loop protocol that reports, alongside task success, the rate at which a policy's inferred object structure violates the ontology. Hypotheses, tested with matched comparisons across held-out PartNet-Mobility categories and ablations by axiom family: H1, ontology-consistent training improves generalization to unseen categories; H2, violation rate predicts task failure; H3, pooled, ontology-aligned data transfers across part vocabularies. *Open questions:* Which axiom families carry the gain? (Ru, M11)

**Use of AWS.** The Datalog/SMT tier is embarrassingly parallel over part instances and will run on EC2 batch fleets with datasets staged in S3; Theme 3 training and SAPIEN evaluation will use GPU instances [types and hours to be sized with the collaborator — see budget]. The toolkit will be packaged so that any dataset holder can rerun the audit in their own AWS account.

## 3. Milestones and timeline (12 months)

| Month | Milestone | Deliverable |
|---|---|---|
| M1–M4 | Parts ontology modules axiomatized; consistency, non-triviality and module relationships verified; schema mappings for five datasets drafted | Ontology v0.9 in COLORE; technical report 1 (axioms and verification results) |
| M4–M8 | Audit pipeline v1 (adapters, Datalog/SMT tier, prover tier); first audit across PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World | Code release (audit toolkit v1, open licence); dataset release (corrected annotations, violation reports); audit/data paper submitted |
| M8–M12 | Cross-dataset mappings proved; merged ontology-aligned corpus; H1–H3 experiments in SAPIEN; verification-in-the-loop protocol | Merged corpus release; methods paper submitted; technical report 2 (AWS runbook); ontology contributed to ISO/IEC JTC 1/SC 42 |

Decision points: at M6, if the SMT fragment misses violations the prover finds, expand the prover tier and accept a smaller bulk set rather than weaken the audit; at M10, if H1 fails on the first policy backbone, switch to the agreed alternative — H2 and H3 do not depend on H1.

## 4. Team, dissemination and engagement

The PI directs the Semantic Technologies Laboratory, where the verified-ontology methodology and its tools were developed. Dr. Ru leads all three themes as the named postdoctoral researcher; one MASc student (MASc1) owns the lattice-characterization question; [Prof. name, University of Toronto Robotics Institute — confirm] advises on the policy backbone and simulator. All outputs are released openly and contributed to COLORE, to AI, robotics and applied-ontology venues, and to ISO/IEC JTC 1/SC 42. We would welcome a research contact at Amazon Robotics or in AWS automated reasoning to select the object categories and violation classes most relevant to fulfilment manipulation; the toolkit and AWS runbook will let the audit be rerun on internal data.

---

## Appendix A. Bibliography

*(Internal note — delete before export.)* Verify every entry against the source before submission; entries marked [confirm] have details the applicant or PI must supply. Entry 14 must be replaced with the laboratory's published papers; a grant proposal cannot be cited.

1. ISO/IEC 21838-4:2023. Information technology — Top-level ontologies (TLO) — Part 4: TUpper. ISO/IEC, Geneva.
2. Ru, Y., and Grüninger, M. (2026, submitted). Material Constitution as a Parthood-Preserving Mapping between Mereologies. Synthese.
3. Ru, Y., and Grüninger, M. (2026, submitted). [Exact title of the mereological pluralism validation paper]. Synthese.
4. Ru, Y. (2025). [Thesis title]. PhD thesis, Department of Mechanical and Industrial Engineering, University of Toronto. [confirm title]
5. Mo, K., Zhu, S., Chang, A. X., Yi, L., Tripathi, S., Guibas, L. J., and Su, H. (2019). PartNet: A large-scale benchmark for fine-grained and hierarchical part-level 3D object understanding. Proc. IEEE/CVF CVPR 2019.
6. Xiang, F., Qin, Y., Mo, K., Xia, Y., Zhu, H., Liu, F., Liu, M., Jiang, H., Yuan, Y., Wang, H., Yi, L., Chang, A. X., Guibas, L. J., and Su, H. (2020). SAPIEN: A simulated part-based interactive environment. Proc. IEEE/CVF CVPR 2020.
7. Geng, H., Xu, H., Zhao, C., Xu, C., Yi, L., Huang, S., and Wang, H. (2023). GAPartNet: Cross-category domain-generalizable object perception and manipulation via generalizable and actionable parts. Proc. IEEE/CVF CVPR 2023.
8. [PartNet-Ensembled (PartNet-E) — confirm authors, title, venue and year; believed to have been introduced with PartSLIP, Liu et al., CVPR 2023 — verify.]
9. AgiBot World Colosseo team (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. arXiv preprint. [confirm author list and identifier]
10. Open X-Embodiment Collaboration (2024). Open X-Embodiment: Robotic learning datasets and RT-X models. Proc. IEEE ICRA 2024.
11. Khazatsky, A., et al. (2024). DROID: A large-scale in-the-wild robot manipulation dataset. Proc. Robotics: Science and Systems (RSS) 2024.
12. Grüninger, M., and Menzel, C. (2003). The Process Specification Language (PSL) theory and applications. AI Magazine 24(3): 63–74.
13. Simons, P. (1987). Parts: A Study in Ontology. Oxford University Press.
14. [REPLACE before submission: the Semantic Technologies Laboratory's published papers on mereotopology verification, on ontological analysis of robotic task and motion planning, and on the ontological analysis of ShapeNet and PartNet — obtain exact references from Prof. Grüninger.]
15. Xu, J., Zhang, Z., Friedman, T., Liang, Y., and Van den Broeck, G. (2018). A semantic loss function for deep learning with symbolic knowledge. Proc. ICML 2018.
16. Grüninger, M., and Fox, M. S. (1995). Methodology for the design and evaluation of ontologies. IJCAI-95 Workshop on Basic Ontological Issues in Knowledge Sharing.
17. Grüninger, M., Hahmann, T., Hashemi, A., Ong, D., and Özgövde, A. (2012). Modular first-order ontologies via repositories. Applied Ontology 7(2): 169–209.
18. McCune, W. (2005–2010). Prover9 and Mace4. https://www.cs.unm.edu/~mccune/prover9/
19. ISO/IEC 24707:2018. Information technology — Common Logic (CL): A framework for a family of logic-based languages.
20. de Moura, L., and Bjørner, N. (2008). Z3: An efficient SMT solver. Proc. TACAS 2008, LNCS 4963: 337–340.
21. Fischer, M., Balunovic, M., Drachsler-Cohen, D., Gehr, T., Zhang, C., and Vechev, M. (2019). DL2: Training and querying neural networks with logic. Proc. ICML 2019. [verify]
22. Manhaeve, R., Dumančić, S., Kimmig, A., Demeester, T., and De Raedt, L. (2018). DeepProbLog: Neural probabilistic logic programming. Proc. NeurIPS 2018. [verify]

## Appendix B. One-page PI CV

See statement.md, Part A (to be exported as the final page of the proposal PDF, per the ARA template).
