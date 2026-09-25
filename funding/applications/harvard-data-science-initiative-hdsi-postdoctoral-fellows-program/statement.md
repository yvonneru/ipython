# Cover letter and personal statement — HDSI Postdoctoral Fellows Program (2026-27 call)

**Use.** The portal's component list is unconfirmed [verify]. If it asks for a cover letter, send Part A alone. If it asks for a personal or research statement separate from the proposal, send Part B (about 900 words; trim to any stated limit). If it asks for neither, fold the second and third paragraphs of Part B into the top of the research statement. [Brackets] to confirm.

---

## Part A — Cover letter

[Date]

Harvard Data Science Initiative
Postdoctoral Fellows Program Selection Committee

Dear Committee,

I am applying to the Harvard Data Science Postdoctoral Fellows Program for the [2027–2029] term, naming [Mentor 1, Statistics / Computer Science], [Mentor 2, SEAS] and [Mentor 3, Harvard Medical School / Biomedical Informatics] as the Harvard faculty with whom I would like to work. My research is on data quality for hierarchically annotated data: I build formally verified ontologies of physical objects and their parts and use them as specifications against which large annotated datasets are audited, aligned and, in the case of learned models, constrained.

I completed my PhD in Information Engineering at the University of Toronto in 2025 and am currently a postdoctoral researcher at Harvard Medical School, in [laboratory/department]. I am a core contributor to ISO/IEC 21838-4:2023, the international standard for the TUpper top-level ontology; I co-authored, with Prof. Michael Grüninger, a formal theory of material constitution now under review at Synthese; and I have built and shipped production data-integration and recommendation systems as a founder of two technology companies. The combination — formal theory that is machine-checked, and data systems that run at scale — is what I bring to HDSI.

The attached research statement proposes a program in three parts: a verified ontology of object parts; a scalable audit of the part-level datasets that current physical-AI models are trained on, which no one has yet checked against any formal specification, extended to anatomical part labels in medical imaging; and measured experiments on whether ontology-aligned data and ontology-derived constraints improve what learned policies generalize. The second part is the data-science core and will produce public data and a reusable toolkit; the first and third give it a specification and an outcome measure.

I would be glad to present this work to the committee or to interested faculty. Thank you for your consideration.

Sincerely,
Yi Ru
Postdoctoral Researcher, Harvard Medical School · yi.ru@alumni.utoronto.ca

---

## Part B — Personal statement

**Research trajectory.** I came to data science through the question of what a data model means. As an industrial engineering undergraduate and then a doctoral student at the University of Toronto, I worked on formal ontology — theories in first-order logic whose consistency and intended models are established by automated theorem provers and model finders — and became a core contributor to ISO/IEC 21838-4:2023, the standard for the TUpper top-level ontology [confirm role wording]. My doctoral thesis developed an architecture for AI knowledge systems in which a verified ontology governs the data model, the learned models and the simulation layer [add one sentence naming the application domain and the principal quantitative result]. With Prof. Michael Grüninger I then developed a theory of material constitution as a parthood-preserving mapping between mereologies and a validation of mereological pluralism, two papers now under review at Synthese, which give a machine-checkable answer to a question that data integration asks constantly: when are two decompositions of the same thing compatible? Since [month year] I have been a postdoctoral researcher at Harvard Medical School, in [laboratory/department], working on [one sentence]. That appointment has given me a second data regime and an applied community that judges formal methods by whether they work.

**Why the proposed program, and why HDSI.** Physical AI is being built on a handful of large part-level datasets whose annotation schemas were designed independently and whose part relations carry no stated semantics; the same is true of anatomical segmentation datasets in medicine. The consequences are visible — poor transfer across part vocabularies, silent errors when datasets are pooled — but have never been measured, because there has been no formal specification to measure against. My program supplies the specification, the scalable audit, and the measurement of what the audit changes. It is data science in HDSI's own terms: data systems design and modeling of structured data at the methodological end, and applications in robotics and the health sciences at the other. It needs what HDSI is built to provide — faculty across Statistics, Engineering and Medicine, and a cohort of fellows who will scrutinize claims about data quality and generalization — and it gives HDSI in return a public audit of widely used datasets, a reusable toolkit and an ontology-aligned corpus.

**Independence.** The program is my own. My thesis did not address object parts, robot datasets or learned policies; the Synthese papers provide the theory and the datasets released over the past three years provide, for the first time, data at a scale where the theory can be tested. The Harvard faculty I have named would each supervise one component — measurement design, the policy experiments, the imaging extension — and Prof. Grüninger would be an external collaborator for the verification methodology; none of them owns the program. [If HDSI requires mentors outside the current laboratory: My current supervisor is not among the named faculty; the proposed work is distinct from the laboratory's research.]

**From theory to practice.** I have founded or co-founded technology companies in which ontology-governed data systems were built and shipped at production scale — a cross-border commerce platform serving customers in over a hundred countries, and a spatial-data company whose consumer application runs on the Apple Vision Pro — and I hold [number] patents from applied 3D-recognition and indoor-modelling work. I am also the founder of AXIOMALITY, a company developing a verification layer for robotics data; I disclose this here and will comply with Harvard's outside-activity and conflict-of-interest rules [confirm the rules for HDSI fellows]. The fellowship research will be released under open licences and contributed to the COLORE repository and to ISO/IEC JTC 1/SC 42; the company does not fund, own or restrict it. What the company experience contributes to the fellowship is engineering discipline — versioned axioms, regression tests on inferences, reproducible pipelines — practised, not proposed.

**Open science and equity.** All axioms, mappings, code, audit logs and corrected annotations will be released so that groups without access to proprietary robot or clinical data can build on the work. The datasets to be audited come from a small number of laboratories and depict objects, homes and workplaces from a narrow range of regions; the ontology separates structural parthood from culturally specific object categories, and the audit will report coverage by source so that these gaps are documented rather than hidden. At Toronto I served as Vice President of the graduate students' association of my department, as departmental representative to the Graduate Student Union and as a CUPE 3902 steward, and was a teaching assistant in database systems and knowledge modelling; at Harvard I will [describe a concrete commitment — e.g., mentor a first-generation graduate student through the fellowship's cohort activities and present the audit tooling at an HDSI workshop].

**Career goal.** A faculty position in knowledge representation for engineering and biomedical data systems. Two years at HDSI, with the audit results, the corpus and the toolkit as public outputs and three papers as the record, is the step that goal requires.
