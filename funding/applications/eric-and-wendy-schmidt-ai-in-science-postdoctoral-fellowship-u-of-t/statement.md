# Statements — Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship (U of T)

Three texts. Part A is the required *statement of AI training needs* (target ≤ 1 page [verify limit]). Part B is a cover letter / personal statement for use only if the form has a free-text "personal statement" or "letter" field. Part C is a lay summary and impact statement: the U of T apply page reportedly asks for lay summaries of the PhD and proposed research and an impact statement [verify on the page; if not asked for, do not submit]. [Brackets] to confirm.

---

## Part A — Statement of AI training needs

**Where I stand.** My training is in formal methods for knowledge representation: first-order ontologies, automated theorem proving and model finding, and the engineering of data systems governed by those theories. I completed a PhD in Information Engineering at the University of Toronto in March 2025, contributed to the international standard ISO/IEC 21838-4:2023 (TUpper), and developed with Prof. Grüninger a formal theory of material constitution and mereological pluralism now under review at *Synthese*. I have used machine learning as a practitioner, not as a researcher: at MICAS I led machine-learning-driven marketing and order-risk systems in production; at Uing Technologies I built structured 3D datasets and shipped an application with mesh object recognition, spatial mapping and path planning; at Harvard Medical School I work on [one sentence — confirm]. What I have not had is formal training in the methods that Theme 3 of my proposal depends on: learning manipulation policies from demonstration and simulation, representation learning for 3D and articulated objects, differentiable programming for constraint relaxation, and uncertainty quantification for learned systems.

**What I need to learn, and why.** The proposal's third objective — using a verified ontology as an inductive bias inside policy training — requires me to (1) train and evaluate part-aware manipulation policies in SAPIEN and [second simulator], (2) design differentiable relaxations of first-order parthood constraints as auxiliary losses, (3) build constraint-guided data augmentation for under-represented object categories, and (4) calibrate abstention with conformal uncertainty inside a verification-in-the-loop evaluation protocol. Each maps to a training need:

| Need | How the fellowship meets it | Tied to |
|---|---|---|
| Deep robot learning: imitation learning, policy architectures for manipulation, simulation-to-real evaluation | Co-supervision by [name] at the U of T Robotics Institute / Vector; the cohort's AI training courses [verify programme content]; Robotics Institute seminars | Theme 3 (a), H1 |
| 3D and articulated-object representation learning (point clouds, part segmentation, kinematic prediction) | Cohort courses; reading group with the co-supervisor's students; reproduction of two baseline methods on PartNet-Mobility in Y1 | Theme 3 (a)–(b) |
| Differentiable programming and neuro-symbolic training (relaxing logical constraints into losses) | Cohort workshops; collaboration with [Vector faculty working on neuro-symbolic methods — name after confirming]; Y1 reading milestone | Theme 3 (a) |
| Uncertainty quantification and conformal prediction | Cohort statistics module [verify]; DSI methods training; applied first in the audit pipeline (Y1), then in policy evaluation (Y2) | Theme 2; Theme 3 (c) |
| Experimental design and statistical evaluation of learned policies (matched comparisons, confidence intervals, ablations) | DSI / Statistical Sciences training; co-supervisor's evaluation practice | H1–H3 |
| Scalable compute practice (distributed training, experiment tracking) | Vector Institute compute and engineering support [verify access] | Y2 experiments |

**How I will learn.** I learn by building: each need above has a Y1 deliverable (a reproduced baseline, an audit-pipeline component, a reading-group presentation) before it is used in a Y2 experiment. I will attend the full cohort programme, present the audit results to the cohort at the end of Y1, and offer the cohort a short workshop on specification-based data auditing in return. My aim is not to become a robot-learning specialist in place of a formal-methods researcher, but one of the few people who can carry a machine-checked specification all the way into a training loop and an evaluation protocol — the combination my long-term goal, a faculty position in knowledge representation for engineering systems, requires.

---

## Part B — Cover letter / personal statement

[Date]
Selection Committee, Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship
Data Sciences Institute, University of Toronto

Dear Committee,

I am applying for the Schmidt AI in Science Postdoctoral Fellowship to be held in the Department of Mechanical and Industrial Engineering at the University of Toronto under Prof. Michael Grüninger, with [name] as co-supervisor for the machine-learning component, starting [1 May 2027 or later].

My research is on knowledge-grounded representation for physical AI: I build formally verified ontologies of physical objects and their parts and use them as specifications, audits and inductive biases for learned manipulation policies. I completed my PhD in Information Engineering at the University of Toronto in March 2025 and am currently a postdoctoral researcher at Harvard Medical School. I am a core contributor to ISO/IEC 21838-4:2023, the international standard for the TUpper top-level ontology; I co-authored, with Prof. Grüninger, a formal theory of material constitution now under review at *Synthese*; and I have built and shipped production data systems as a founder of two technology companies. The combination — formal theory that is machine-checked, and systems that run — is what I bring.

The proposal addresses an engineering problem that the robotics community has observed but never measured. Manipulation policies are trained on part-level datasets whose annotations carry no formal semantics; pooled training mixes incompatible part vocabularies; transfer to new object categories is brittle. I will supply the missing specification as a verified extension of TUpper, audit the datasets the field trains on against it, and then use it inside policy training and evaluation. The first two parts are where my existing skills lie. The third is where AI methods change what the domain can do — and it is exactly where I need the training this fellowship provides. My statement of AI training needs is specific about that: deep robot learning, 3D representation learning, differentiable constraint relaxation and uncertainty quantification, each tied to a milestone.

Why Toronto: the verified-ontology methodology with tool support exists only in the Semantic Technologies Laboratory; the Robotics Institute and the Vector Institute supply the robotics community and the compute; the DSI cohort supplies the training. I will be resident in Toronto for the full term and will participate fully in the cohort programme.

Thank you for your consideration. I would be glad to present the work to the committee or to interested faculty.

Sincerely,
Yi Ru
yi.ru@alumni.utoronto.ca

---

## Part C — Lay summary and impact statement [submit only if the form asks for them; verify]

**Lay summary of my PhD research (about 120 words).** Computer systems that reason about the world need a precise, shared vocabulary for what things are and how they relate: an ontology. My doctoral research at the University of Toronto developed a way of building artificial-intelligence systems in which such a vocabulary is written as mathematical axioms, checked by computer for consistency, and then used to govern the system's data, its learned models and its simulations, so that every part of the system means the same thing by the same word. [One sentence naming the application domain and the main result of the thesis — confirm.] Parts of this work were adopted in an international standard, ISO/IEC 21838-4, which gives engineers worldwide a common, machine-checked foundation for building ontologies.

**Lay summary of the proposed research (about 150 words).** Robots learn to handle objects — open a drawer, turn a handle — from large collections of examples in which objects are labelled as assemblies of parts. But each collection labels parts in its own way, nobody checks whether the labels obey the basic logic of parts and wholes, and robot-training pipelines mix these collections freely. Nobody knows how much this costs, because there has been no exact standard to check against. I will write that standard as a set of computer-verified axioms, extending an international standard I helped create; use it to audit the major robot datasets and report, for the first time, how often their labels contradict the logic of parthood; and then build the axioms into the training of robot policies to test whether robots that respect the logic of parts generalize better to objects they have never seen. The fellowship's AI training programme will teach me the modern robot-learning methods this last step requires.

**Impact statement (about 120 words).** The immediate beneficiaries are the researchers and companies that train robots on public part-level datasets: they receive a verified vocabulary of parts, an audit of the data they already use, corrected labels, a merged corpus and a tool that reports when a robot's understanding of an object is logically inconsistent — an interpretable warning signal. Because the audit is machine-checkable, it is also the kind of evidence that emerging safety regulation for AI in machinery and robots asks for, so it helps make deployed robots safer and more accountable. The same tool applies to any hierarchical labelling problem — CAD assemblies, digital twins of buildings [and part labels in medical images — confirm]. All axioms, mappings, code and corrected annotations will be released openly and contributed to ISO/IEC JTC 1/SC 32.
