# RAC 2027 — Resources for Research Groups (RRG) application

**PI:** Michael Grüninger, Department of Mechanical and Industrial Engineering, University of Toronto (CCRI [PI to supply]) · **Project title:** Verified mereological ontologies for object–part representation in physical AI · **Allocation year:** 1 April 2027 – 31 March 2028 · **Lead researcher (sponsored user):** Dr. Yi Ru, postdoctoral fellow from [April 2027 or later], CCDB username [after registration]

*Drafted 2026-09-25 by Dr. Ru for the PI to review, edit and submit. Voice: the PI's, following the structure of his NSERC proposals mapped onto the RRG form's sections. The RRG form's exact headings and length limits were not obtainable from the searches this session; the sections below use the headings that recur across RAC cycles and are sized so that the research description (§1–§6) runs to roughly three pages of 12-point text (≈1,900 words) and is written so that any section can be cut to fit a shorter limit. Re-fit to the RAC 2027 Application Guide before submission. Facts come only from the profile, the drafts and the registry; every unconfirmed item is in [brackets]. Resource quantities come from budget_and_timeline.md and inherit its bracketed assumptions.*

---

## Project summary (≈150 words; for the form's summary field)

Robot-learning datasets — PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment and DROID — annotate objects as hierarchies of parts with kinematic, functional and visual labels. Each dataset defines "part" operationally; no dataset or learned model is required to satisfy the axioms of parthood; there is no principled way to map labels across datasets; pooled training silently mixes incompatible part vocabularies. The consequences — poor transfer across part vocabularies, brittle generalization to new object categories — are observed but have never been measured, because there has been no formal specification to measure against. This project supplies the specification and the measurement: a verified first-order ontology of physical object parts extending TUpper (ISO/IEC 21838-4) and the Process Specification Language; a two-tier audit pipeline that produces the first quantitative measurement of parthood consistency in robot datasets; and training methods that use the ontology as an inductive bias for part-aware manipulation policies in SAPIEN [and Isaac Lab]. The allocation year carries the re-audit of all corpora with the released ontology and the full policy-training matrix.

---

## 1. Recent progress

An ontology is a computer-interpretable specification that is used by an agent, application, or other information resource to declare what terms it uses, and what the terms mean. My research has focussed on the axiomatization of ontologies as theories in first-order logic and the development of techniques for their design and verification.

- **COLORE and verified upper ontologies.** The Common Logic Ontology Repository (COLORE) is an open repository of first-order ontologies, currently 2,580 theories specified in Common Logic (ISO 24707), organized into hierarchies and serving as a testbed for ontology verification and integration [1]. My work on mereotopology, time, location and units of measure (FOUnt, Distinguished Paper Award, FOIS 2018 [2]) was integrated with the Process Specification Language ontology [3] to form the upper ontology TUpper, published as the International Standard ISO/IEC 21838-4 [4]. Each module of TUpper has been verified: we characterize the models of an ontology up to isomorphism and determine whether they are equivalent to the intended models.
- **Ontological analysis of AI benchmarks and robotic planning.** My recent work asks what minimal set of ontologies is needed to specify reasoning problems in robotic task and motion planning [5], and evaluates the ontological presuppositions implicit in AI benchmarking datasets (ShapeNet, PartNet, Visual Genome), which are riddled with logical and ontological errors that no prior work has analysed formally [6].
- **Material constitution and mereological pluralism (with Dr. Ru).** Dr. Yi Ru, who joins the laboratory as a postdoctoral fellow in [April 2027 or later], was a core contributor to ISO/IEC 21838-4 and has developed with me a theory of material constitution as a parthood-preserving mapping between mereologies, together with a machine-checked validation of mereological pluralism; both are under review at Synthese [7, 8]. The theory says exactly what must hold for two part decompositions of the same object to be compatible — the question posed, but never answered, by robot datasets in which kinematic, functional and visual decompositions of the same object co-exist.
- **Production-scale data integration.** Dr. Ru's doctoral work (MIE, 2025) developed an architecture in which a verified ontology governs the data model, learned models and simulation layer of an AI knowledge system [9], and Dr. Ru has shipped ontology-governed data-integration systems at production scale as a company founder — the engineering discipline (versioned axioms, regression tests on inferences, reproducible pipelines) that a dataset-scale audit requires.

## 2. Objectives

Manipulation policies for articulated objects are trained on part-level datasets whose annotations carry no formal semantics. Nothing requires the parts a model infers to form a consistent whole; nothing relates the part vocabularies of different datasets; nothing lets a policy report *why* an inferred decomposition is wrong. The research program is motivated by the following long-term challenge:

*Can the part-level representations that robot-learning systems learn be shown to satisfy the axioms of parthood that humans use, and does enforcing those axioms improve generalization?*

To address this challenge, the program has three primary objectives:

1. **Ontology as specification (O1).** Axiomatize and verify a modular first-order ontology of physical object parts — rigid, articulated, functional and assembly parts — as an extension of TUpper integrated with PSL for state change under manipulation; verification of consistency, non-triviality, module relationships and representation theorems with Prover9 and Mace4 under the COLORE methodology.
2. **Ontology as audit (O2).** Translate the annotation hierarchies of the seven datasets into ontology instances and check them with a two-tier pipeline, yielding the first quantitative measurement of parthood consistency in robot datasets, corrected annotations, provably meaning-preserving cross-dataset label mappings, a merged ontology-aligned corpus [to the extent dataset terms permit] and a reusable audit toolkit.
3. **Ontology as inductive bias (O3).** Develop and evaluate training methods that use the ontology to shape part-aware manipulation policies — differentiable relaxations of parthood constraints as auxiliary losses, constraint-guided data augmentation for underrepresented categories, and verification-in-the-loop evaluation that reports ontology-violation rate alongside task success.

The allocation year covers the compute-intensive halves of O2 and O3. O1 and the first audit are completed before April 2027 on Dr. Ru's current allocations at Harvard [HMS O2 cluster; NSF ACCESS and NAIRR requests in progress]; a first public audit result on 2–3 datasets is targeted for [15 January 2027] and will be cited here once available.

## 3. Literature review

Very few representations of physical objects and their parts have been formalized to the extent suitable for automated reasoning. Classical mereology assumes a single parthood relation; the puzzles of material constitution arise because ordinary objects seem to demand more than one, and no prior work has stated machine-checkable conditions under which two decompositions are compatible [7, 8]. On the data side, PartNet [10] provides fine-grained hierarchical part segmentations; PartNet-Mobility, distributed with the SAPIEN simulator [11], adds articulation (2,347 models in 46 categories); GAPartNet [12] defines "generalizable actionable parts"; PartNet-Ensembled (PartNetE) was assembled from PartNet and PartNet-Mobility for PartSLIP [13]; the real-robot corpora AgiBot World [14], Open X-Embodiment [15] and DROID [16] carry sparse object and part labels attached to episodes. Each defines "part" by its own annotation protocol — a segmentation label, a movable link, an actionable region — and none states axioms that its annotations must satisfy. Existing work on dataset quality in robot learning measures label noise and coverage, not logical consistency; there has been no ontological analysis of these datasets and no formal specification against which their part hierarchies can be checked. Neuro-symbolic approaches that add constraints to learned models have not used a verified ontology as the source of constraints, and no evaluation protocol reports violation of parthood axioms alongside task success.

## 4. Methodology

The ontologies will be designed using my ontology lifecycle methodology [17] and verified — we characterize the models of an ontology up to isomorphism and determine whether they are equivalent to the intended models. Competency questions come from the datasets themselves: for every annotated object, which decompositions are compatible, which annotations violate which axiom, and which cross-dataset label mappings preserve parthood. The program is organized in three themes; the projects that consume the requested allocation are marked (**RAC**).

**Theme 1 — Parts (O1).** *Which axioms of parthood do rigid, articulated, functional and assembly parts require, and are they jointly consistent with TUpper and PSL?*

- Project 1.1 (before the allocation year): axiomatize the parts ontology as modules extending TUpper's mereotopology and PSL; verify with Prover9/Mace4; prove representation theorems relating each dataset's annotation schema to the ontology so that cross-dataset mappings are meaning-preserving by proof. Compute: hundreds of proof obligations × minutes — under 500 core-hours, met by the Rapid Access Service. Open questions: Does the axiomatization of articulated parts require the process ontology, or only the static mereotopology? Which annotation schemas are definably equivalent? (PDF: Dr. Ru; MASc1.)

**Theme 2 — Audit (O2).** *What fraction of the part annotations in each dataset violate the axioms, which axiom families are violated, and which cross-dataset mappings are provably meaning-preserving?*

- Project 2.1 (**RAC**, CPU): the two-tier audit. Tier 1 compiles an SMT/Datalog subset of the ontology and checks every annotated part instance in bulk; Tier 2 sends residual hard cases to Prover9 (proof obligations) and Mace4 (counter-models), with UNKNOWN/timeout as a first-class output so the worst case is bounded by the timeout. The audit is repeated across [3] ontology versions and [5] axiom-family conditions so that violation statistics can be attributed to individual axiom families. The workload is embarrassingly parallel array jobs on standard-memory nodes, with a few large-memory jobs for Datalog materialization of the largest corpus and for Mace4 counter-model search. The allocation year carries the re-audit of all seven corpora with the released ontology version; the first audit across five corpora is done at Harvard. Open questions: Does violation rate vary systematically by object category or annotation protocol? Are the violations that survive correction concentrated in a single axiom family? (PDF; MASc2.)
- Project 2.2 (**RAC**, storage): the ontology instance store (annotations, kinematics and episode metadata only — no frames), audit outputs, label mappings and corrected-annotation diffs; released publicly where dataset terms allow.

**Theme 3 — Learning (O3).** *Does ontology-consistent training improve generalization to unseen object categories, does violation rate predict task failure, and does pooled ontology-aligned data transfer across part vocabularies?*

- Project 3.1 (**RAC**, GPU): the experimental matrix. Conditions {no ontology loss, ontology loss} × {constraint-guided augmentation off, on} plus four single-axiom-family ablations (8 conditions) × [5] held-out PartNet-Mobility category splits × [3] seeds = 120 training runs, plus a pooled-data transfer block of {raw pooled, ontology-aligned pooled} × [3] target vocabularies × [3] seeds = 18 runs, in SAPIEN; a half-matrix replication in [Isaac Lab]. Every run is evaluated with verification-in-the-loop (violation rate alongside task success). SAPIEN physics and rendering run on CPU alongside each GPU. Per-run cost ([24] GPU-hours per run of ~[1M] environment steps) is calibrated by pilot runs at Harvard in [Oct 2026 – Mar 2027] and will be replaced by the measured figure. Open questions: Is the effect of the ontology loss larger on categories with high audit violation rates? Which axiom family's relaxation carries the generalization gain? (PDF; PhD1.)

## 5. Team and HQP

Dr. Yi Ru (postdoctoral fellow from [April 2027 or later]; PhD MIE 2025; core contributor to ISO/IEC 21838-4; first author of [7, 8]) leads all three themes and runs the allocation. [Lab graduate students working on COLORE/PSL — PI to list with CCDB usernames: MASc1, MASc2, PhD1 above are placeholders for the trainees who will own the tagged open questions.] Collaboration on the simulation component: [U of T Robotics Institute / Vector Institute faculty member — name after introduction]. HQP training outcomes: graduate students learn ontology verification at dataset scale and GPU policy training with formal evaluation; Dr. Ru gains the independent program required for a faculty career.

## 6. Expected outcomes and impact

(1) A verified parts ontology released under an open licence and contributed to COLORE and to ISO/IEC JTC 1/SC 42. (2) The first quantitative audit of parthood consistency in robot datasets — violation rates by dataset, category and axiom family, with counter-models for representative failures — released publicly. (3) Provably meaning-preserving label mappings across the seven datasets and corrected-annotation diffs where terms allow. (4) An audit toolkit reusable for hierarchical annotations beyond robotics: CAD assemblies and product-lifecycle data in manufacturing, building information models, and part labels in medical imaging. (5) Policy-training results reporting ontology-violation rate alongside task success; two ML-venue papers and one robotics-venue paper. Near term, the work improves the quality of the datasets on which robot-learning systems are trained and tested and supplies an interpretable failure signal for manipulation policies; longer term, the ontologies reside in COLORE and support an open knowledge network of commonsense knowledge about the physical world and testbeds for how robotic systems encounter it.

## 7. Past usage and progress

This is the group's first RRG request [PI to confirm]. The laboratory's theorem-proving workflow (Prover9/Mace4 verification of COLORE ontologies) has run on [departmental machines / the Rapid Access Service — PI to state]. From October 2026, Dr. Ru's sponsored role under the Rapid Access Service is used to prototype the audit pipeline and hold the instance store, and that usage is reported here [insert RAS usage figures at submission]. Pilot results from Dr. Ru's Harvard-period allocations [ACCESS / NAIRR / HMS O2 — insert measured Tier-1 throughput, Tier-2 residual fraction and GPU-hours per training run when available] are the basis for the per-unit costs in the resource justification. Fast Track is not applicable.

## 8. Resource request (summary; full derivation in budget_and_timeline.md)

| Resource | Request (allocation year) | Justification |
|---|---|---|
| GPU, H100-class ([Killarney or Trillium-GPU — confirm system and whether AI compute is requested inside this form]) | [5,000–8,000] GPU-hours ≈ [7–11] RGU-years at 12.15 RGU per H100-80G [verify factor on the Alliance table] | 138 training runs at [24] GPU-hours + verification-in-the-loop [+25 %] + [Isaac Lab] half-matrix [+2,000] + development [+30 %] |
| CPU | [2] core-years | Tier-1 [17,000] core-hours; Tier-2 [4,000] core-hours (worst case [60,000], bounded by timeout); SAPIEN physics/rendering [~1 core-year] |
| Large-memory nodes | [2–4] jobs at 256 GB | Datalog materialization; Mace4 counter-model search |
| Project storage | [20 TB] | Annotation shards and instance store for seven corpora (no frames); audit outputs; mappings |
| Nearline / scratch | [50 TB] | Raw corpora during extraction (OXE ~9 TB; AgiBot World Beta tens of TB; DROID ~1.7 TB — registry figures); rollouts and checkpoints [2–5 TB] |
| Cloud | none | |
| Software | Prover9/Mace4; [Z3]; [Soufflé]; Python; PyTorch; SAPIEN; [Isaac Lab]; LeRobot/RLDS readers | All open source; SAPIEN and Isaac Lab require CUDA/RTX-capable GPUs |

## 9. Data management

All datasets are obtained under their own terms by Dr. Ru as an individual academic researcher with an institutional email. ShapeNet, PartNet, PartNet-Mobility/SAPIEN, GAPartNet and AgiBot World are non-commercial licences [terms re-read at registration]; Open X-Embodiment sub-datasets are mostly CC BY 4.0 / Apache-2.0 and DROID is CC BY 4.0 (data) and MIT (code) [registry, unverified]. Raw data are stored only on the allocated systems and deleted or mirrored when the allocation ends. The instance store holds annotations, kinematics and episode metadata only. Public releases consist of the ontology, audit reports, label mappings, corrected-annotation diffs [where terms permit] and the validator code (Apache-2.0); any re-hosted merged corpus is limited to subsets whose licence permits redistribution. No personal data are processed [confirm for teleoperation footage: the audit does not use frames]. Dr. Ru's company, AXIOMALITY, does not use any resource requested here; company workloads run on separately funded company accounts.

---

## Bibliography

*Numbering as cited above. Entries marked [complete] need full bibliographic details from the PI's or Dr. Ru's reference lists; no details are invented here.*

1. Grüninger, M. et al. COLORE — Common Logic Ontology Repository, colore.oor.net (2,580 first-order ontologies). [complete reference as used in the PI's NSERC proposal, ref. 13]
2. Grüninger, M. et al. FOUnt — first-order ontologies for units of measure. Proc. FOIS 2018, Distinguished Paper Award. [complete]
3. Grüninger, M. The Process Specification Language (PSL) ontology. [complete; ISO 18629 lineage]
4. ISO/IEC 21838-4:2023. Information technology — Top-level ontologies (TLO) — Part 4: TUpper. ISO/IEC JTC 1/SC 42.
5. Grüninger, M. et al. Ontological analysis of robotic task and motion planning (path planning requires ontologies for spatiotemporal regions, location and motion activities). [complete; ref. 4 of "Commonsense Cobotics"]
6. Grüninger, M. Commonsense Cobotics, NSERC Discovery Grant proposal (evaluation of AI benchmarking datasets). [internal; cite the published version if any]
7. Ru, Y. and Grüninger, M. (2026, submitted). Material Constitution as a Parthood-Preserving Mapping between Mereologies. Synthese.
8. Ru, Y. and Grüninger, M. (2026, submitted). [Exact title — mereological pluralism validation]. Synthese.
9. Ru, Y. (2025). [Thesis title]. PhD thesis, Information Engineering, Department of Mechanical and Industrial Engineering, University of Toronto.
10. Mo, K. et al. PartNet: a large-scale benchmark for fine-grained and hierarchical part-level 3D object understanding. [complete]
11. Xiang, F. et al. SAPIEN: a simulated part-based interactive environment (PartNet-Mobility). [complete]
12. Geng, H. et al. GAPartNet: cross-category domain-generalizable object perception and manipulation via generalizable and actionable parts. [complete]
13. Liu, M. et al. PartSLIP: low-shot part segmentation for 3D point clouds via pretrained image-language models (PartNet-Ensembled). CVPR 2023. [complete]
14. AgiBot World Colosseo. [complete; dataset card]
15. Open X-Embodiment Collaboration. Open X-Embodiment: robotic learning datasets and RT-X models. [complete]
16. Khazatsky, A. et al. DROID: a large-scale in-the-wild robot manipulation dataset. [complete]
17. Grüninger, M. and Fox, M. S. Methodology for the design and evaluation of ontologies (the ontology lifecycle methodology cited as [17] in the PI's NSERC proposals). [complete]
18. McCune, W. Prover9 and Mace4. [complete]
19. ISO/IEC 24707:2018. Information technology — Common Logic (CL).
