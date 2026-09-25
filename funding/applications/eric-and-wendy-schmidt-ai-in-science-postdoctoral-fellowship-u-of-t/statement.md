# Statements — Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship (U of T)

Two texts. Part A is the required *statement of AI training needs* (target ≤ 1 page [verify limit]). Part B is a cover letter / personal statement for use if the form has a free-text "personal statement" or "letter" field; if it does not, Part B is not submitted. [Brackets] to confirm.

---

## Part A — Statement of AI training needs

**Where I stand.** My training is in formal methods for knowledge representation: first-order ontologies, automated theorem proving and model finding, and the engineering of data systems governed by those theories. I completed a PhD in Information Engineering at the University of Toronto in 2025, contributed to the international standard ISO/IEC 21838-4:2023 (TUpper), and developed with Prof. Grüninger a formal theory of material constitution and mereological pluralism now under review at *Synthese*. I have used machine learning as a practitioner rather than as a researcher: at MICAS I led machine-learning-driven marketing and order-risk systems in production; at Uing Technologies I built structured 3D datasets and shipped an application with mesh object recognition, spatial mapping and path planning; and at Harvard Medical School I work on [one sentence — ontology-driven integration of heterogeneous biomedical data / neuro-symbolic clinical AI]. What I have not had is formal training in the methods that Theme 3 of my proposal depends on: learning manipulation policies from demonstration and simulation, representation learning for 3D and articulated objects, differentiable programming for constraint relaxation, and uncertainty quantification for learned systems.

**What I need to learn, and why.** The proposal's third objective — using a verified ontology as an inductive bias inside policy training — requires me to (1) train and evaluate part-aware manipulation policies in SAPIEN and [second simulator], (2) design differentiable relaxations of first-order parthood constraints as auxiliary losses, (3) build constraint-guided data augmentation for under-represented object categories, and (4) calibrate abstention with conformal uncertainty inside a verification-in-the-loop evaluation protocol. Each of these maps to a training need:

| Need | How the fellowship meets it | Tied to |
|---|---|---|
| Deep robot learning: imitation learning, policy architectures for manipulation, simulation-to-real evaluation | Co-supervision by [name] at the U of T Robotics Institute / Vector; the cohort's AI training courses [verify programme content]; Robotics Institute seminar series | Project 3.1 (a), H1 |
| 3D and articulated-object representation learning (point clouds, part segmentation, kinematic prediction) | Cohort courses; reading group with the co-supervisor's students; reproduction of two baseline methods on PartNet-Mobility in Y1 | Project 3.1 (a)–(b) |
| Differentiable programming and neuro-symbolic training (relaxing logical constraints into losses) | Cohort workshops; collaboration with [Vector faculty working on neuro-symbolic methods — name after confirming]; Y1 reading milestone | Project 3.1 (a) |
| Uncertainty quantification and conformal prediction | Cohort statistics module [verify]; DSI methods training; applied first in the audit pipeline (Y1), then in policy evaluation (Y2) | Project 2.1, 3.1 (c) |
| Experimental design and statistical evaluation of learned policies (matched comparisons, confidence intervals, ablations) | DSI/Statistical Sciences training; co-supervisor's evaluation practice | H1–H3 |
| Scalable compute practice (distributed training, experiment tracking) | Vector Institute compute and engineering support [verify access] | Y2 experiments |

**How I will learn.** I learn by building: each training need above has a Y1 deliverable (a reproduced baseline, an audit-pipeline component, a reading-group presentation) before it is used in a Y2 experiment. I will attend the full cohort programme, present the audit results to the cohort at the end of Y1, and offer the cohort a short workshop on specification-based data auditing in return. My aim is not to become a robot-learning specialist in place of a formal-methods researcher but to become one of the few people who can carry a machine-checked specification all the way into a training loop and an evaluation protocol — the combination my long-term goal, a faculty position in knowledge representation for engineering systems, requires.

---

## Part B — Cover letter / personal statement

[Date]
Selection Committee, Eric and Wendy Schmidt AI in Science Postdoctoral Fellowship
Data Sciences Institute, University of Toronto

Dear Committee,

I am applying for the Schmidt AI in Science Postdoctoral Fellowship to be held in the Department of Mechanical and Industrial Engineering at the University of Toronto under Prof. Michael Grüninger, with [name] as co-supervisor for the machine-learning component, starting [1 May 2027 or later].

My research is on knowledge-grounded representation for physical AI: I build formally verified ontologies of physical objects and their parts and use them as specifications, audits and inductive biases for learned manipulation policies. I completed my PhD in Information Engineering at the University of Toronto in 2025 and am currently a postdoctoral researcher at Harvard Medical School. I am a core contributor to ISO/IEC 21838-4:2023, the international standard for the TUpper top-level ontology; I co-authored, with Prof. Grüninger, a formal theory of material constitution now under review at *Synthese*; and I have built and shipped production data systems as a founder of two technology companies. The combination — formal theory that is machine-checked, and systems that run — is what I bring.

The proposal addresses an engineering problem that the robotics community has observed but never measured. Manipulation policies are trained on part-level datasets whose annotations carry no formal semantics; pooled training mixes incompatible part vocabularies; transfer to new object categories is brittle. I will supply the missing specification as a verified extension of TUpper, audit the datasets the field trains on against it, and then use it inside policy training and evaluation. The first two parts are where my existing skills lie. The third is where AI methods change what the domain can do — and it is exactly where I need the training this fellowship provides. I have written the statement of AI training needs to be specific about that: deep robot learning, 3D representation learning, differentiable constraint relaxation and uncertainty quantification, each tied to a milestone.

Why Toronto: the verified-ontology methodology with tool support exists only in the Semantic Technologies Laboratory; the Robotics Institute and the Vector Institute supply the robotics community and the compute; the DSI cohort supplies the training. I will be resident in Toronto for the full term and will participate fully in the cohort programme.

Thank you for your consideration. I would be glad to present the work to the committee or to interested faculty.

Sincerely,
Yi Ru
yi.ru@alumni.utoronto.ca
