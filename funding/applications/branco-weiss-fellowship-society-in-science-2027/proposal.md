# Research proposal — The Branco Weiss Fellowship – Society in Science (2027 round)

**Applicant:** Yi Ru, PhD (University of Toronto, 2025); postdoctoral researcher, Harvard Medical School
**Proposed main host:** Semantic Technologies Laboratory, Department of Mechanical and Industrial Engineering, University of Toronto (Prof. Michael Grüninger) [confirm; see README on whether the PhD-granting institution may host]
**Format limit:** maximum 5 pages including abstract, timelines, tentative milestones and references (official application page). This draft is written to fit 5 pages at 11–12 pt; the bibliography is part of the count. [Confirm any font/margin rule in the portal when it opens in October 2026.]

---

## Title

**Proof before deployment: a public, machine-checkable audit of the data that teaches robots what objects are**

## Abstract

Robots that manipulate objects are now trained on a few large datasets that describe objects as hierarchies of parts. No dataset, and no model trained on one, is required to satisfy the axioms of parthood that people use without thinking: a part is not disjoint from the whole it belongs to; parts of parts are parts; two decompositions of the same object must agree on what is inside what. The field measures task success, not whether the learned structure of an object is coherent, and it pools datasets whose notions of "part" were never reconciled. I propose to put a formally verified theory of parts between the data and the policy: to specify parthood as first-order axioms verified with automated provers, to audit the major robot-learning corpora against those axioms and publish the results, and to test whether training under the axioms makes manipulation policies generalize. The project departs from the mainstream of both of its parent fields, which treat scale (robot learning) and description (applied ontology) as the answer; it treats proof as the answer. It also departs from my doctoral work on knowledge-system architecture and top-level ontology. Its society-facing aim is concrete: from 2 August 2028 the EU AI Act applies to AI in machinery and robots, and regulators, standards bodies and the public will need evidence about training data that is checkable rather than asserted. I will produce that evidence in the open and take it into the standards process (ISO/IEC JTC 1/SC 42) and into public dialogue about who gets to say that a robot's training is trustworthy.

## 1. Why this project departs from the mainstream

An ontology is a computer-interpretable specification that declares what terms a system uses and what they mean [1]. My research axiomatizes ontologies as theories in first-order logic and verifies them: every claim about the theory is a theorem or a counter-model, established with automated tools (Prover9, Mace4, SMT solvers) under the COLORE methodology [2]. Three results of that work bear on this proposal.

- **A verified top-level ontology as an international standard.** I was a core contributor to ISO/IEC 21838-4:2023, the TUpper top-level ontology [3], within ISO/IEC JTC 1/SC 42 [confirm exact role wording and working-group designation]. TUpper is a modular first-order theory in which each module is verified, and it is the reference against which domain ontologies can be proven, not merely asserted, to be consistent extensions.
- **A theory of parts that admits more than one parthood relation.** With M. Grüninger I developed a formal account of material constitution as a parthood-preserving mapping between distinct mereologies, and a validation of mereological pluralism, both submitted to Synthese in 2026 [4, 5]. The theory says exactly what must hold for two part decompositions of the same object to be compatible, and it is machine-checkable. That is the question robot datasets pose and do not answer.
- **Ontology-first systems in production.** My doctoral thesis [title] developed an architecture in which a verified ontology governs the data model, the learned models and the simulation layer of an AI system. As founding team member of MICAS and co-founder of YourTable Inc. and Uing Technologies I shipped ontology-governed data-integration, recommendation and 3D-scene systems, including one of the first AR object-interaction applications on the Apple Vision Pro, and I am first inventor on [number — confirm] granted patents in 3D recognition and indoor modelling.

The mainstream of robot learning holds that the route to general manipulation is more data and larger models; datasets such as PartNet [6], PartNet-Mobility [7], GAPartNet [8], Open X-Embodiment [9], DROID [10] and AgiBot World [11] are built and pooled on that assumption. The mainstream of applied ontology holds that its job is to describe domains; it has not audited the training data of learned systems against its own axioms. This project stands outside both. It claims that the coherence of what a robot learns about objects can be specified, checked and published, and that doing so is a precondition for trusting the robot, whatever its scale. It is a departure from my thesis as well: the thesis was about architecture and top-level categories; nothing in it concerned physical object parts, robot datasets or learned policies, and none of its datasets, methods or experiments recurs here.

## 2. Objectives

Part-level datasets annotate objects as hierarchies with kinematic, functional and visual labels. Each defines "part" operationally: a segmentation label in one, a movable link in another, an actionable region in a third. There is no shared definition, no consistency requirement inside a dataset (a part may be annotated as both contained in and disjoint from another), and no principled way to map labels across datasets. The consequences — poor transfer across part vocabularies, brittle generalization to new object categories, silent errors when data are pooled — are observed but have never been measured, because there has been no specification to measure against. The programme is motivated by the following long-term challenge:

*Can the part-level representations that robot-learning systems acquire be shown to satisfy the axioms of parthood that humans use, can that evidence be produced in public and at the scale of the datasets themselves, and does enforcing the axioms make the systems generalize?*

The programme has four primary objectives:

1. **Ontology as specification (O1).** Axiomatize and verify a modular first-order ontology of physical object parts (rigid, articulated, functional, assembly) as an extension of TUpper integrated with the Process Specification Language (PSL) for state change under manipulation.
2. **Ontology as audit (O2).** Build a two-tier audit pipeline (Datalog/SMT for bulk data; first-order theorem proving for residual cases), audit the major robot-learning corpora, and publish the first quantitative measurement of parthood consistency in robot datasets, with corrected annotations and provably meaning-preserving cross-dataset mappings.
3. **Ontology as inductive bias (O3).** Develop and test training methods that use the ontology to shape part-aware manipulation policies, and an evaluation protocol that reports ontology-violation rate alongside task success.
4. **Ontology as public evidence (O4).** Turn the audit into an open evidence format for training data, take it into ISO/IEC JTC 1/SC 42 and into dialogue with regulators, robot manufacturers and the public ahead of the 2028 application of the EU AI Act to machinery.

## 3. State of the art and gaps

Formal mereology has a mature literature [12, 13], and first-order mereotopologies have been verified and standardized within TUpper [3]. Robot-learning datasets, by contrast, carry no formal semantics: PartNet [6] provides hierarchical segmentation; PartNet-Mobility and SAPIEN [7] add articulation; GAPartNet [8] defines "generalizable and actionable" parts across categories; real-robot corpora [9, 10, 11] add trajectories without a part schema. Each is internally useful; jointly they are inconsistent by construction, and no prior work has performed an ontological analysis of any of them (Grüninger's "Commonsense Cobotics" programme proposes it for vision benchmarks; this proposal does it for manipulation data, at dataset scale, and publicly). Neuro-symbolic learning has used constraints as losses and as data-generation rules, but the constraints have been hand-written rather than derived from a verified theory, so nothing certifies that satisfying the loss means satisfying the intended models. On the policy side, the emerging AI-assurance regime — the EU AI Act (Regulation (EU) 2024/1689) [14], which applies to AI in machinery from 2 August 2028, and the NIST AI Risk Management Framework [15] — asks for evidence about data governance and quality but does not say what checkable evidence about training data looks like. Nobody has yet supplied a definition.

## 4. Methodology

Ontologies will be designed with the ontology lifecycle methodology of the Semantic Technologies Laboratory [16] and verified in the strict sense: I will characterize the models of each module up to isomorphism and determine whether they are equivalent to the intended models. Verification (do the axioms have exactly the intended models?) is distinguished throughout from validation (are the intended models the right ones?); dataset annotations serve as the source of competency questions for validation. The work is organized in three themes, each with projects and open research questions; each question is answerable by a theorem, a counter-model or a measured effect, and each is tagged with the phase in which it is answered (P = pioneer phase, years 1–2.5; E = exploitation phase, years 2.5–5).

### Theme 1 — Parts (O1)

*Which mereologies are implicit in the part decompositions robots are trained on, and can one verified theory relate them?*

**Project 1.1 — Verified parts ontology.** Extend TUpper with modules for rigid parts, articulated parts (joints as PSL fluents), functional parts (affordance-bearing regions) and assemblies, using design by reuse and ontology merging from COLORE. Verify consistency, non-triviality and inter-module relationships with Prover9 and Mace4; prove representation theorems that characterize the models.
- Are the kinematic, functional and visual decompositions of a single object in PartNet-Mobility models of one mereology or of several? (P)
- Does the material-constitution mapping of [4] extend to a mapping between the articulated and the functional decomposition of the same object? (P)

**Project 1.2 — Schema theorems.** For each dataset schema, state its implicit axioms and prove (or refute by counter-model) that its labels can be interpreted in the ontology without loss.
- Which dataset relations are not definable in the ontology, and do they mark genuine ontological commitments or annotation artefacts? (P)
- Can cross-dataset label mappings be proved parthood-preserving, and which pairs of datasets admit no such mapping? (P/E)

### Theme 2 — Audit (O2, O4)

*What is the rate and pattern of parthood violations in the data that trains physical AI, and how should that evidence be published?*

**Project 2.1 — Audit pipeline.** Translate annotation hierarchies into ontology instances; check bulk data (millions of part instances) with Datalog/SMT rules compiled from the axioms; send residual hard cases to a first-order prover. UNKNOWN and timeout are first-class outcomes and are reported, not hidden. Targets: PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, and the part-relevant slices of AgiBot World, Open X-Embodiment and DROID [confirm final list with host].
- Which axiom families are violated most often, and are violations concentrated in particular object categories or annotation sources? (P)
- Does the violation rate of a category predict the failure rate of policies trained on it? (E, with Theme 3)

**Project 2.2 — Open evidence format.** Publish, per dataset release, a reproducible evidence pack: axioms, mappings, violation statistics, corrected annotations, and the proof or counter-model behind every mapping claim; release the toolkit under an open licence so that groups without proprietary robot data can run it, including on medical image part labels, CAD assemblies and building models.
- What minimum evidence about training data would let an independent party re-derive an audit claim without trusting the auditor? (P)
- Can the evidence pack be expressed in the terms of ISO/IEC JTC 1/SC 42 data-quality and AI-management standards so that it is usable in conformity assessment? (E)

### Theme 3 — Learning (O3)

*Does training under verified axioms make part-aware manipulation policies generalize, and is violation rate a usable failure signal?*

**Project 3.1 — Ontology-constrained training.** Differentiable relaxations of parthood constraints as auxiliary losses on inferred part relations; constraint-guided augmentation that synthesizes ontology-consistent part configurations for underrepresented categories. Experiments in SAPIEN [7] and [second simulator — confirm], with ablations by axiom family. Hypotheses: ontology-consistent training improves generalization to unseen PartNet-Mobility categories; pooled, ontology-aligned data transfers across part vocabularies.
- Which axiom families carry the generalization effect, and does the effect survive when constraints are enforced only at evaluation? (E)

**Project 3.2 — Verification-in-the-loop evaluation.** Report ontology-violation rate alongside task success; test whether it predicts failure and can serve as an interpretable failure signal for humans supervising a robot.
- Is violation rate a better predictor of out-of-category failure than in-distribution success? (E)

## 5. Society in Science: the dialogue this project commits to

The fellowship asks for willingness to engage beyond the discipline. This project's society-facing question is: *who gets to say that the data a robot was trained on is trustworthy, and on what evidence?* Today the answer is the data's producer. I will work to make the answer "anyone who can run the check". Concretely: (a) every audit result and evidence pack is public and reproducible; (b) I will bring the evidence format into ISO/IEC JTC 1/SC 42, where I already contribute, so that it can be referenced by conformity-assessment bodies preparing for the EU AI Act's 2028 machinery provisions [14] and by NIST AI RMF profiles [15]; (c) I will convene one open workshop per year, alternating between a technical audience (robot-learning and applied-ontology researchers, robot manufacturers) and a public/policy audience (regulators, standards bodies, labour and consumer representatives) [host and venue to confirm]; (d) I will write for non-specialist audiences on what "verified" can and cannot mean for a learned system, with the audit as the worked example. The economic dimension is also open for discussion: I founded a company, AXIOMALITY, that pursues a commercial verification product for robot data; the fellowship project is independent academic research whose outputs are open, and my role in the company during the fellowship will be [state the arrangement decided with the host: e.g., non-executive/advisory role, with a written conflict-of-interest plan approved by the host institution]. I raise this openly because the question of whether data assurance for physical AI should be a public good or a paid service is exactly the kind of question the fellowship exists to have argued out in the open.

## 6. Timeline and tentative milestones (5 years; pioneer phase then exploitation phase)

| Period | Milestone |
|---|---|
| Months 1–8 | Parts ontology modules axiomatized and verified (P1.1); schema theorems for PartNet and PartNet-Mobility (P1.2); audit pipeline prototype (P2.1). |
| Months 6–16 | First public audit across five datasets with evidence packs (P2.1, P2.2); corrected annotations and mappings released; audit/data paper submitted; first open workshop. |
| Months 12–24 | Pooled-data and augmentation experiments in SAPIEN (P3.1); toolkit v1 released; SC 42 contribution drafted; methods paper on specification-based annotation auditing. |
| Month ~24 | **Site visit and review (end of pioneer phase).** Deliverables in hand: verified ontology in COLORE; public audit of five datasets; toolkit; two papers; SC 42 draft. |
| Years 3–4 | Extension to real-robot corpora (AgiBot World, Open X-Embodiment, DROID slices); ontology-constrained training and verification-in-the-loop evaluation (P3.1, P3.2); robotics-venue paper; evidence format aligned with conformity-assessment practice; public/policy workshop ahead of August 2028. |
| Year 5 | Second application domain for the audit toolkit (medical image part labels or CAD assemblies) [choose with host]; consolidation into a standard proposal or technical specification within SC 42; synthesis publication and third-party funding secured for continuation. |

## 7. Impact

Near term, the project gives the physical-AI community its first measured account of what its models are trained on, a corrected and aligned public corpus, and a failure signal that humans can read. It gives standards bodies and regulators a definition of checkable evidence about training data before the 2028 deadline makes one necessary. Long term, it establishes proof — rather than scale or description — as a third route to trustworthy embodied AI, contributes verified ontologies to the open COLORE repository and to ISO/IEC 21838, and trains the people (students at the host, standards delegates, workshop participants) who will carry the practice into manufacturing, health and the built environment.

## References

[Bibliographic details marked [verify] must be completed from the applicant's reference manager before submission; no item may be cited without a checked reference.]

1. Grüninger, M. "Ontologies for the Physical Turing Test", NSERC Discovery Grant proposal (opening definition of ontology). [cite the published source of this definition instead, e.g., Gruber or the ISO/IEC 21838-1 definition — verify]
2. COLORE — Common Logic Ontology Repository, colore.oor.net; and the associated verification papers [complete citation — verify].
3. ISO/IEC 21838-4:2023. Information technology — Top-level ontologies (TLO) — Part 4: TUpper. ISO/IEC, Geneva.
4. Ru, Y., Grüninger, M. (2026, submitted). Material Constitution as a Parthood-Preserving Mapping between Mereologies. Synthese.
5. Ru, Y., Grüninger, M. (2026, submitted). [exact title of the mereological pluralism validation paper]. Synthese.
6. Mo, K. et al. (2019). PartNet: a large-scale benchmark for fine-grained and hierarchical part-level 3D object understanding. CVPR. [verify]
7. Xiang, F. et al. (2020). SAPIEN: a simulated part-based interactive environment (includes PartNet-Mobility). CVPR. [verify]
8. Geng, H. et al. (2023). GAPartNet: cross-category domain-generalizable object perception and manipulation via generalizable and actionable parts. CVPR. [verify]
9. Open X-Embodiment Collaboration (2023). Open X-Embodiment: robotic learning datasets and RT-X models. [verify venue/year]
10. Khazatsky, A. et al. (2024). DROID: a large-scale in-the-wild robot manipulation dataset. [verify venue]
11. AgiBot World Colosseo (2025). [verify authors, title, venue]
12. Simons, P. (1987). Parts: A Study in Ontology. Oxford University Press. [verify]
13. Casati, R., Varzi, A. (1999). Parts and Places. MIT Press. [verify]
14. Regulation (EU) 2024/1689 (Artificial Intelligence Act), Annex I; application to machinery from 2 August 2028. [verify article/annex references]
15. NIST (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). [verify]
16. Grüninger, M., Fox, M. S. Methodology for the design and evaluation of ontologies. [complete citation — verify]
17. ISO 18629 (Process Specification Language). [verify parts and years]
18. PartNet-Ensembled [verify citation]; McCune, W. Prover9 and Mace4 [verify].
