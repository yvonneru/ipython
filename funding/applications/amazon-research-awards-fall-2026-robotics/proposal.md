# Verified Parthood: Automated Reasoning for Auditing and Constraining Part-Level Robot Manipulation Data

**Principal Investigator:** Prof. Michael Grüninger, Department of Mechanical and Industrial Engineering (Semantic Technologies Laboratory), University of Toronto
**Named postdoctoral researcher:** Dr. Yi Ru (PhD, Information Engineering, University of Toronto, 2025; [currently postdoctoral researcher, Harvard Medical School — confirm]; joining the PI's laboratory [June 2027 or later — confirm start])
**Call:** Amazon Research Awards, Fall 2026 — [Robotics (preferred) / Automated Reasoning — select once the call posts; keep the matching abstract sentence]
**Requested:** [USD cash, within the call's cash cap — see budget_and_timeline.md] cash gift plus [USD] AWS Promotional Credits; 12 months

*(Internal — delete before export. Page budget, cut order and template notes are in README.md, "Format and criteria". Every sentence in the PI's voice needs Prof. Grüninger's approval.)*

---

## Abstract

Robot-learning datasets — PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled and AgiBot World [confirm AgiBot World's part-level annotation fields] — describe objects as hierarchies of parts with kinematic, functional and visual labels, and manipulation policies are trained on them pooled. Each dataset defines "part" operationally; none is checked against the axioms of parthood, and labels are mapped across datasets by hand, so pooled training mixes incompatible part vocabularies. The resulting failures — poor transfer across vocabularies, brittle generalization to new categories — are reported but not measured, because there is no specification to measure against. We will supply one and enforce it by automated reasoning. **(O1)** Axiomatize a modular first-order ontology of object parts extending TUpper (ISO/IEC 21838-4) and the Process Specification Language, with every module proved consistent and non-trivial (Prover9/Mace4). **(O2)** Audit the five datasets against it on AWS with a two-tier checker — SMT/Datalog for the bulk, first-order proving for residual cases, timeouts reported as UNKNOWN — and publish per-dataset violation rates, corrected-annotation patches and cross-dataset label mappings proved meaning-preserving. **(O3)** In a SAPIEN pilot, test whether training a part-aware policy under the ontology improves success on held-out PartNet-Mobility categories, and whether its violation rate predicts failure. [Robotics: *The result is a cross-dataset part schema whose consistency is a theorem, and a failure signal computable before deployment.* / Automated Reasoning: *The result is an application of SMT and first-order proving to detecting inconsistency and vacuity in the informal specifications that annotation schemas are.*] Axioms, toolkit, patches and an AWS runbook will be released openly.

**Keywords:** automated reasoning; formal ontology; mereology; theorem proving; SMT; robot manipulation; articulated objects; dataset alignment; data quality; neuro-symbolic learning.

## 1. Significance of the research and prior work

Physical AI is being built on a handful of part-level datasets [5–9] whose schemas were designed independently: a "part" is a segmentation label in one, a movable link in another, an actionable region in a third. Warehouse manipulation meets far more object categories than these datasets cover (PartNet: 24 categories [verify]), so whether part representations transfer to unseen categories is decisive — and today it is judged by inspection.

**Prior work.** Label-error methods such as confident learning [18] flag labels that are statistically unlikely, but cannot say which labels contradict one another by definition. Robot knowledge bases (KnowRob [19]; IEEE 1872 CORA [20]) represent objects and parts for run-time reasoning, and semantic-loss methods [11, 17] add logical constraints to training. To our knowledge none has been used to audit the part hierarchies of training corpora against an axiomatized theory of parthood, or to test whether such a theory improves cross-category manipulation. Our prior work supplies the specification:

- **Verified first-order ontologies and COLORE (PI).** The PI's research axiomatizes ontologies as first-order theories and develops techniques for their design and verification [12, 13]. COLORE, an open repository in Common Logic [15], holds more than 2,580 first-order ontologies organized into hierarchies [13]. The PI's mereotopology, time, location and units-of-measure ontologies are modules of TUpper, published as ISO/IEC 21838-4 [1], each module verified; FOUnt, the units-of-measure module, received the Distinguished Paper Award at FOIS 2018 [14]. PSL [10] supplies the theory of activities and state change reused here. The PI's NSERC Discovery program [title — "Commonsense Cobotics"; confirm title and funding status] asks which mereotopologies the ShapeNet and PartNet decompositions presuppose. **This proposal funds what that grant does not: an audit of five robot-manipulation datasets at data scale on AWS, and the use of its result in policy training.**
- **A machine-checked theory of parthood under constitution (named postdoc, with the PI).** Dr. Ru's theory treats material constitution as a parthood-preserving mapping between distinct mereologies, with Prover9/Mace4 consistency and non-triviality proofs [2, 3; submitted to Synthese, 2026]. Given two part decompositions of one object, it states what must hold for them to be compatible — the question robot datasets pose when kinematic, functional and visual decompositions co-exist.
- **Ontology-governed systems in practice (named postdoc).** Dr. Ru's thesis [4] developed an architecture in which a verified ontology governs the data model, the learned models and the simulation layer; Dr. Ru is a core contributor to ISO/IEC 21838-4:2023 [confirm role wording and committee designation]. As co-founder and CEO of Uing Technologies, Dr. Ru builds ontology-based representations of objects and indoor environments for embodied AI and led nine invention patent applications.

**Impact at scale and relevance to Amazon.** The audit applies to any part-annotated corpus, including internal ones: adapters and checker are schema-driven, and the runbook reruns them in another AWS account. For robotics it yields a part schema whose consistency is proved and an ontology-violation rate computable before a policy is deployed; for automated reasoning it is SMT and first-order proving applied to data, with UNKNOWN as a first-class outcome.

**Readiness.** The constitution theory is written and under review [2, 3]; the verification toolchain is in daily use in the PI's laboratory; the datasets are public [confirm each licence]; the SMT tier compiles axioms already written. The award funds the audit at scale and the measured effect on learning.

## 2. Technical approach

Ontologies are designed with the PI's methodology [12, 13] and verified by characterizing the models of each module against its intended models. Competency questions come from the audit ("Is any part annotated both as contained in and disjoint from another?" "Which PartNet-Mobility links correspond to GAPartNet actionable parts?").

**Theme 1 — Parts (O1, M1–M4).** 1.1 axiomatizes rigid, articulated, functional and assembly parthood as Common Logic modules over the TUpper mereotopology; module relationships (conservative extension, definable equivalence) are proved or refuted by counter-model. 1.2 applies the constitution mappings of [2, 3] to kinematic, functional and visual decompositions, giving representation theorems for when two decompositions are compatible. 1.3 integrates PSL so that parthood change under manipulation (detach, insert, open) has axiomatized preconditions and effects. *Success measure:* every module has a Mace4 model and passes the non-triviality checks; each dataset's part vocabulary is shown definable in the ontology, or a counter-model is recorded.

**Theme 2 — Audit (O2, M3–M9).** 2.1 writes adapters from each native schema (and the LeRobot and RLDS formats of real-robot corpora) to ontology instances with per-part provenance. 2.2 builds the two-tier checker: the decidable fragment is compiled to Datalog and SMT (Z3 [16]) and run over every part instance and pairwise part relation on AWS; undecided instances go to Prover9/Mace4 under a time budget, and timeouts are reported as UNKNOWN, never as passed. 2.3 derives cross-dataset mappings from the Theme 1 theorems, proves each meaning-preserving, and releases corrected annotations as patches against the original releases. *Success measures:* per-dataset violation rates with confidence intervals, broken down by axiom family and category; the UNKNOWN rate; SMT–prover disagreement on a stratified sample of hierarchies; and audit precision — a random sample of each violation class is adjudicated by two annotators as a data error or an ontology error, and ontology errors revise the axioms before release (M6).

**Theme 3 — Learning pilot (O3, M8–M12).** 3.1 compiles the parthood axioms to differentiable relaxations (semantic-loss terms [11, 17]) as auxiliary losses on the part relations a policy infers. 3.2 uses Mace4-generated models to augment underrepresented categories in SAPIEN [6]. 3.3 reports, alongside task success, the rate at which a policy's inferred part structure violates the ontology. On one part-aware backbone [named by the Robotics Institute advisor], with metrics fixed before M8: **H1**, ontology-consistent training raises success on held-out PartNet-Mobility categories (matched comparison, [n] seeds, ablation by axiom family); **H2**, violation rate predicts task failure (AUROC); **H3**, ontology-aligned pooled data transfers across part vocabularies. H2 needs no retraining and is run first.

**Use of AWS.** The SMT/Datalog tier is embarrassingly parallel and runs on EC2 batch fleets with datasets in S3; the prover tier runs under explicit time budgets; Theme 3 uses GPU instances [types and hours sized with the advisor — see budget].

## 3. Milestones and timeline (12 months)

| Month | Milestone | Deliverable |
|---|---|---|
| M1–M4 | Parts modules axiomatized and verified; schema mappings for five datasets drafted | Ontology v0.9 in COLORE; technical report 1 (axioms, verification results) |
| M3–M9 | Adapters; SMT/Datalog and prover tiers; audit of five datasets; adjudicated precision sample | Audit toolkit v1 (open licence); violation reports and corrected-annotation patches; audit/data paper submitted |
| M8–M12 | Mappings proved; ontology-aligned index; H2, then H1 and H3, in SAPIEN | Mappings and index released; methods paper submitted; technical report 2 (AWS runbook); ontology v1.0 to COLORE and to ISO/IEC JTC 1 [committee — verify] |

**Decision points and risks.** M6: if the SMT fragment misses violations the prover finds, expand the prover tier and accept a smaller bulk set rather than weaken the audit. M10: if H1 fails on the first backbone, report it and switch to the advisor's alternative; H2 and H3 do not depend on H1. If Theme 2 runs late, Theme 3 is reduced to H2. If a licence forbids redistributing corrected annotations, release the violation reports and the patch generator instead. Themes 1 and 2 deliver the audit, the schema and the releases whatever Theme 3 shows.

## 4. Team and engagement

The PI [directs — confirm] the Semantic Technologies Laboratory, where the methodology and tools were developed, and supervises the verification work. Dr. Ru leads all three themes full-time; [a MASc student in the PI's laboratory — confirm funding source] takes the articulated-parthood module and the adapters; [Prof. name, University of Toronto Robotics Institute — confirm] advises on the policy backbone and simulator. We would welcome an Amazon research contact in robotics or automated reasoning to choose the object categories and violation classes most relevant to fulfilment manipulation.

---

## Appendix A. References

*(Internal — delete before export.)* Verify every entry. Entries 3, 4, 8, 9 and 14 need details from the applicant or PI. If references count toward the page limit, keep 1–7, 10, 12–14, 16, 18 and drop the rest.

1. ISO/IEC 21838-4:2023. Information technology — Top-level ontologies (TLO) — Part 4: TUpper. ISO/IEC, Geneva.
2. Ru, Y., and Grüninger, M. (2026, submitted). Material Constitution as a Parthood-Preserving Mapping between Mereologies. Synthese.
3. Ru, Y., and Grüninger, M. (2026, submitted). [Exact title of the mereological pluralism validation paper]. Synthese.
4. Ru, Y. (2025). [Thesis title]. PhD thesis, Department of Mechanical and Industrial Engineering, University of Toronto.
5. Mo, K., Zhu, S., Chang, A. X., Yi, L., Tripathi, S., Guibas, L. J., and Su, H. (2019). PartNet: A large-scale benchmark for fine-grained and hierarchical part-level 3D object understanding. Proc. IEEE/CVF CVPR 2019. [verify]
6. Xiang, F., Qin, Y., Mo, K., Xia, Y., Zhu, H., Liu, F., Liu, M., Jiang, H., Yuan, Y., Wang, H., Yi, L., Chang, A. X., Guibas, L. J., and Su, H. (2020). SAPIEN: A simulated part-based interactive environment. Proc. IEEE/CVF CVPR 2020. [verify]
7. Geng, H., Xu, H., Zhao, C., Xu, C., Yi, L., Huang, S., and Wang, H. (2023). GAPartNet: Cross-category domain-generalizable object perception and manipulation via generalizable and actionable parts. Proc. IEEE/CVF CVPR 2023. [verify]
8. [PartNet-Ensembled (PartNet-E) — confirm authors, title, venue, year; believed introduced with PartSLIP, Liu et al., CVPR 2023.]
9. [AgiBot World — confirm authors, title, identifier and year.]
10. Grüninger, M., and Menzel, C. (2003). The Process Specification Language (PSL) theory and applications. AI Magazine 24(3): 63–74. [verify]
11. Xu, J., Zhang, Z., Friedman, T., Liang, Y., and Van den Broeck, G. (2018). A semantic loss function for deep learning with symbolic knowledge. Proc. ICML 2018. [verify]
12. Grüninger, M., and Fox, M. S. (1995). Methodology for the design and evaluation of ontologies. IJCAI-95 Workshop on Basic Ontological Issues in Knowledge Sharing. [verify]
13. Grüninger, M., Hahmann, T., Hashemi, A., Ong, D., and Özgövde, A. (2012). Modular first-order ontologies via repositories. Applied Ontology 7(2): 169–209. [verify]
14. [FOUnt, FOIS 2018 (Distinguished Paper Award) — exact citation from Prof. Grüninger; he may add his mereotopology verification paper here.]
15. ISO/IEC 24707:2018. Information technology — Common Logic (CL): A framework for a family of logic-based languages. [verify edition]
16. de Moura, L., and Bjørner, N. (2008). Z3: An efficient SMT solver. Proc. TACAS 2008, LNCS 4963: 337–340. [verify]
17. Fischer, M., Balunovic, M., Drachsler-Cohen, D., Gehr, T., Zhang, C., and Vechev, M. (2019). DL2: Training and querying neural networks with logic. Proc. ICML 2019. [verify]
18. Northcutt, C. G., Jiang, L., and Chuang, I. L. (2021). Confident learning: Estimating uncertainty in dataset labels. Journal of Artificial Intelligence Research 70: 1373–1411. [verify]
19. Tenorth, M., and Beetz, M. (2013). KnowRob: A knowledge processing infrastructure for cognition-enabled robots. International Journal of Robotics Research 32(5): 566–590. [verify]
20. IEEE Std 1872-2015. IEEE Standard Ontologies for Robotics and Automation. IEEE. [verify]

## Appendix B. One-page PI CV

See statement.md, Part A (exported as the final page of the proposal PDF, per the ARA template).
