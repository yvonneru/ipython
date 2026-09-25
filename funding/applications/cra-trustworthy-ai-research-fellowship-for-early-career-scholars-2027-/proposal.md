# Research plan — Machine-checkable evidence for the part-level data that trains physical AI

**Yi Ru** · Postdoctoral Researcher [confirm title as HR states it], Harvard Medical School, [laboratory/department] · yi.ru@alumni.utoronto.ca

*Note on use. The cohort-2 CRA application asked for a form, a CV and short written responses, not a research proposal. This plan is the source for response 2 in statement.md and for conversations with CRA mentors; at about 2,100 words plus bibliography it runs to three to four pages, so cut Section 3 and the bullets under each project if the cohort-3 call asks for a shorter research statement. [Verify on the live form.]*

## 1. Recent Progress

An ontology is a computer-interpretable specification that declares what terms a system uses and what the terms mean. My research has focussed on first-order ontologies of physical objects and their parts, on the verification of those ontologies with automated reasoning, and on carrying them out of the laboratory into an international standard, patents and production systems.

- **Top-level ontology as an international standard.** I was a core contributor to ISO/IEC 21838-4:2023, the TUpper top-level ontology [1], developed within ISO/IEC JTC 1/SC 42, the committee responsible for artificial-intelligence standards [confirm exact role wording and working-group designation]. TUpper is a modular first-order theory whose consistency and module relationships are established by theorem proving and model finding rather than asserted in prose; every claim about it is a theorem or a counter-model. That is the standard of rigour the present plan applies to robot data.
- **A verified theory of parts and constitution.** With Michael Grüninger (University of Toronto) I developed an account of material constitution as a parthood-preserving mapping between distinct mereologies, and a validation of mereological pluralism, both submitted to *Synthese* in 2026 [2, 3]. The theory states, as first-order axioms checked with Prover9 and Mace4 [6], exactly what must hold for two part decompositions of the same object to be compatible. [Insert one plain-language sentence stating the central theorem.] Robot datasets pose precisely that question: kinematic, functional and visual decompositions of the same object coexist without any statement of how they relate.
- **Ontology-governed systems in production.** My doctoral thesis at the University of Toronto [title] developed an architecture in which a verified ontology governs the data model, the learned models and the simulation layer of an AI system [insert principal quantitative result]. As co-founder and CEO of Uing Technologies I built structured 3D physical-world datasets and ontology-based representations of objects, indoor environments and interactions for embodied AI, and led nine invention patent applications; as a founding team member of MICAS I built internal CRM, ERP and WMS systems and machine-learning-driven marketing for a 100-plus-person organization. I hold [reconcile: 13 granted patents and 9 applications per the AXIOMALITY deck; 3 Chinese invention patents and 9–10 German utility patents per the drafts].
- **Current work.** Since [month year] I have been a postdoctoral researcher at Harvard Medical School, [laboratory/department], working on [one sentence]. [If applicable: one line on how ontology-driven integration of heterogeneous biomedical data relates to the audit method below.]

## 2. Objectives

Robot manipulation policies are trained on datasets that annotate objects as hierarchies of parts with kinematic, functional and visual labels: PartNet [8], PartNet-Mobility in SAPIEN [9], GAPartNet [10], PartNet-Ensembled [citation to verify], and real-robot corpora such as Open X-Embodiment [11], DROID [12] and AgiBot World [13]. Those policies are meant to open drawers and hand over objects in homes, clinics and workplaces; whether the data behind them is internally consistent, and whose notion of an object it encodes, is a question about the people those robots will act around as much as about the robots. Each dataset defines "part" operationally. No dataset or learned model is required to satisfy the axioms of parthood; there is no principled way to map labels across datasets; pooled training silently mixes incompatible part vocabularies. The consequences, poor transfer across part vocabularies and brittle generalization to new object categories, are observed but have never been measured, because there has been no formal specification to measure against. For trustworthy AI this is a data-governance gap with a specific shape: the frameworks that regulators and practitioners now rely on, the NIST AI Risk Management Framework [14] and the EU AI Act's data-governance obligations for high-risk systems, which extend to robots under Annex I from 2 August 2028 [15], ask for documented, examined training data, but supply no machine-checkable notion of what it means for annotated object data to be internally consistent.

*Given a robot-learning dataset and a policy trained on it, produce machine-checkable evidence of what the data asserts about objects and their parts, of where the data contradicts itself or other datasets, and of whether the policy's inferred object structure respects the axioms of parthood that people rely on.*

The plan has three objectives:

1. **Ontology as specification (O1).** Axiomatize and verify a modular first-order ontology of physical object parts (rigid, articulated, functional, assembly) as an extension of TUpper integrated with the Process Specification Language (PSL) [5] for state change under manipulation.
2. **Ontology as audit (O2).** Build a scalable pipeline that translates annotation hierarchies into ontology instances and checks them, producing the first quantitative measurement of parthood consistency in robot datasets, provably meaning-preserving cross-dataset label mappings, and public evidence packs.
3. **Ontology as inductive bias (O3).** Use the ontology to shape and evaluate part-aware manipulation policies, reporting an ontology-violation rate alongside task success as an interpretable failure signal.

## 3. Literature Review

Part-level robot datasets [8–13] document their annotation guidelines informally; none states axioms for its part relation, and none has been the subject of an ontological analysis. Documentation practices for trustworthy AI, datasheets for datasets [19] and model cards [20], record provenance and intended use but do not verify the content of annotations; a datasheet cannot say whether a dataset asserts that a drawer is both part of and disjoint from its cabinet. Policy frameworks [14, 15] require data governance and examination for errors but leave "consistency" undefined. Formal mereology [16, 17] provides a mature axiomatic literature on parts and wholes, and the COLORE repository methodology [4] provides tool-supported verification of first-order ontologies in Common Logic [18], but neither has been connected to learned part representations. Neuro-symbolic work on robot learning uses symbolic structure as scaffolding for policies, but the symbolic layer is typically hand-written and unverified, so an inconsistent specification propagates into training unnoticed. The gaps are therefore: no formal specification of "part" for robot data; no measurement of annotation consistency against any specification; no meaning-preserving alignment across datasets; and no evaluation protocol in which a policy's object model is checked against verified commonsense axioms.

## 4. Methodology

The ontology is designed with the lifecycle methodology of the COLORE repository [4]: axioms in Common Logic [18], organized into modules by signature, with competency questions drawn from the audit tasks and verification by characterizing the models of each module up to isomorphism where possible, and by consistency and non-triviality checks with Prover9 and Mace4 [6] otherwise. I distinguish verification (do the models of the axioms match the intended models?) from validation (are the intended models the right ones for robot data?), and treat the second as an empirical question answered in Theme 2. Milestones are tagged by fellowship month (M1–M12, with M1 the cohort kickoff; cohort 2 ran June 2026 – August 2027 with the Field School in late July, so cohort 3 is assumed to run June 2027 – August 2028 [unconfirmed]); the plan is the 12-month template of my wider program, leaves the final two months of the cohort for the fellowship report, and continues in my host appointment beyond the fellowship year.

### Theme 1 — Parts: a verified specification (O1)

*Which axioms of parthood, articulation and function must an annotated object satisfy, and can they be stated as a consistent modular extension of TUpper and PSL?*

**Project 1.1 — Mereology of rigid and articulated parts.** Extend TUpper with a parts module distinguishing rigid parthood, kinematic connection (joint types and limits as in PartNet-Mobility) and assembly membership; prove consistency and the relationships between modules; state representation theorems relating the module to the annotation schemas of PartNet, PartNet-Mobility and GAPartNet so that cross-dataset mappings are meaning-preserving by proof. M1–M4.
- Is the parts module a conservative extension of TUpper, and is each dataset schema definably interpretable in it? (theorem or counter-model) M3
- Which schema relations have no meaning-preserving image in the ontology, and are they errors or genuine differences in intended models? M4

**Project 1.2 — Parts under manipulation.** Integrate the parts module with PSL so that opening a drawer, detaching a lid or breaking an object are state changes with axiomatized preconditions and effects on the part structure. M3–M5.
- Can "part that becomes a separate object" (detachment) and "objects that become one" (assembly) be axiomatized without inconsistency with material constitution [2]? M5

### Theme 2 — Audit: evidence about the data (O2)

*What do current robot datasets actually assert about parts, where do they contradict themselves and each other, and whose object vocabulary do they encode?*

**Project 2.1 — Two-tier audit pipeline.** Translate annotation hierarchies into ontology instances; check the bulk with Datalog rules and SMT (Z3 [7]) compiled from the axioms, and route residual hard cases to first-order theorem proving; report UNKNOWN and timeout as first-class outcomes rather than silently passing them. M4–M8.
- What fraction of part instances in each of five datasets violates a parthood, articulation or assembly axiom, and which axiom families account for the violations? (measured) M7
- Does the compiled SMT subset agree with full first-order checking on a sampled set of hard cases? (measured) M8

**Project 2.2 — Aligned corpus and evidence packs.** Release corrected annotations, proved label mappings and a merged, ontology-aligned corpus, each with a reproducible evidence pack that records the axioms, tool versions, obligations discharged and residual unknowns, structured so that it can be cited under NIST AI RMF "Map" and "Measure" functions [14] and under the EU AI Act's data-governance article [15]. M6–M9.
- Can pooled, ontology-aligned data be built across datasets without loss of the relations each dataset intended? (theorem for mappings; measured for coverage) M9

**Project 2.3 — Whose parts? Provenance, coverage and the people who annotate.** Report coverage by source laboratory, region and object category; document where annotation guidelines disagree and where the ontology had to choose; and conduct semi-structured interviews with dataset maintainers and annotation workers [number; recruitment route; consent and compensation per host IRB — confirm whether review is required] about how "part" was operationalized, whether reported violations are errors or deliberate choices, and what the audit misses. The interview protocol is drafted at M1, revised after the Field School (M2) with cohort and mentor input, and fielded from M5; findings are returned to participants before publication. This is the community-based component of the plan and the one on which I most want CRA mentorship: I can measure disagreement, but deciding whose decomposition counts as correct is not a computing question. M5–M10.
- Do violation rates differ systematically by annotation source or guideline, and do maintainers and annotators recognize the reported violations as errors or as deliberate choices? (measured; qualitative) M10

### Theme 3 — Learning: the ontology as inductive bias and as evaluation (O3)

*Does training on ontology-consistent data, or against ontology-derived constraints, improve generalization to unseen object categories, and does a policy's ontology-violation rate predict its failures?*

**Project 3.1 — Constraint-based training.** Differentiable relaxations of parthood constraints as auxiliary losses on inferred part relations; constraint-guided data augmentation that synthesizes ontology-consistent part configurations for underrepresented categories. Experiments in SAPIEN [9] and [second simulator], with ablations by axiom family. M8–M12.
- Does ontology-consistent training improve success on held-out PartNet-Mobility categories relative to matched baselines, with confidence intervals? (measured) M12

**Project 3.2 — Verification-in-the-loop evaluation.** A protocol that reports, alongside task success, the rate at which a policy's inferred object structure violates the ontology, and tests whether that rate predicts failure. M9–M12.
- Is the violation rate an interpretable, pre-deployment failure signal, and can it be reported in a model card [20] without releasing the policy? (measured) M12

## 5. Impact

In the near term the plan gives the field its first measurement of what part-level robot datasets actually assert, a merged corpus that can be pooled without silent vocabulary mixing, and an evidence-pack format that turns "we examined our training data" into a checkable claim under the NIST AI RMF and the EU AI Act. The ontology is contributed to the COLORE repository and offered to ISO/IEC JTC 1/SC 42, the committee in which ISO/IEC 21838-4 was developed [confirm current participation], so that the specification outlives the project. The violation-rate protocol gives practitioners and regulators an interpretable failure signal for manipulation policies that does not require access to model weights. Project 2.3 makes the audit accountable to the people whose labour produced the data.

In the longer term the same method, specification-based auditing of hierarchical annotations, transfers to part labels in medical imaging, CAD assemblies and building information models, and supports an open knowledge network in which the commonsense structure of physical objects is stated once, verified, and reused by learning systems that can be asked to show their evidence. I disclose that I am founder of AXIOMALITY [confirm entity], a company building robotics-data verification tooling; all ontologies, mappings, audit code and corrected annotations from this plan are released under an open licence, and the company holds no exclusive rights to them.

## Bibliography

1. ISO/IEC 21838-4:2023. *Information technology — Top-level ontologies (TLO) — Part 4: TUpper.* ISO/IEC JTC 1/SC 42.
2. Ru, Y., and Grüninger, M. (2026, submitted). Material constitution as a parthood-preserving mapping between mereologies. *Synthese.*
3. Ru, Y., and Grüninger, M. (2026, submitted). [Exact title — mereological pluralism validation]. *Synthese.*
4. Grüninger, M., Hahmann, T., Hashemi, A., Ong, D., and Özgövde, A. (2012). Modular first-order ontologies via repositories. *Applied Ontology* 7(2), 169–209.
5. Grüninger, M., and Menzel, C. (2003). The Process Specification Language (PSL) theory and applications. *AI Magazine* 24(3), 63–74.
6. McCune, W. (2005–2010). Prover9 and Mace4. https://www.cs.unm.edu/~mccune/prover9/
7. de Moura, L., and Bjørner, N. (2008). Z3: an efficient SMT solver. *TACAS 2008*, LNCS 4963, 337–340.
8. Mo, K., Zhu, S., Chang, A. X., Yi, L., Tripathi, S., Guibas, L. J., and Su, H. (2019). PartNet: a large-scale benchmark for fine-grained and hierarchical part-level 3D object understanding. *CVPR 2019.*
9. Xiang, F., Qin, Y., Mo, K., et al. (2020). SAPIEN: a SimulAted Part-based Interactive ENvironment. *CVPR 2020.*
10. Geng, H., Xu, H., Zhao, C., Xu, C., Yi, L., Huang, S., and Wang, H. (2023). GAPartNet: cross-category domain-generalizable object perception and manipulation via generalizable and actionable parts. *CVPR 2023.*
11. Open X-Embodiment Collaboration (2024). Open X-Embodiment: robotic learning datasets and RT-X models. *ICRA 2024.*
12. Khazatsky, A., et al. (2024). DROID: a large-scale in-the-wild robot manipulation dataset. *RSS 2024.*
13. AgiBot World Colosseo Team (2025). AgiBot World Colosseo: a large-scale manipulation platform for scalable and intelligent embodied systems. arXiv:2503.06669. [verify]
14. National Institute of Standards and Technology (2023). *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* NIST AI 100-1.
15. Regulation (EU) 2024/1689 of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), Article 10 and Annex I.
16. Simons, P. (1987). *Parts: A Study in Ontology.* Oxford University Press.
17. Casati, R., and Varzi, A. C. (1999). *Parts and Places: The Structures of Spatial Representation.* MIT Press.
18. ISO/IEC 24707:2018. *Information technology — Common Logic (CL): a framework for a family of logic-based languages.*
19. Gebru, T., Morgenstern, J., Vecchione, B., Vaughan, J. W., Wallach, H., Daumé III, H., and Crawford, K. (2021). Datasheets for datasets. *Communications of the ACM* 64(12), 86–92.
20. Mitchell, M., Wu, S., Zaldivar, A., et al. (2019). Model cards for model reporting. *Proceedings of FAT\* 2019*, 220–229.
