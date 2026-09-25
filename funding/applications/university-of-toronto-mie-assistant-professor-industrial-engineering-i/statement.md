# Cover letter, teaching statement, EDI statement, CV outline and job-talk plan

Yi Ru · Tenure-stream Assistant Professor search, Information Engineering / Applied Machine Learning, Department of Mechanical and Industrial Engineering, University of Toronto. Items in [brackets] to confirm. Upload plan (from recent MIE postings): the cover letter and CV go into dedicated fields on jobs.utoronto.ca; the research statement (proposal.md) with the three representative publications form combined PDF 1; the teaching dossier (§2 plus evaluations and syllabi) and the EDI statement (§3) form combined PDF 2.

---

## 1. Cover letter (1.5–2 pages)

[Date]

Professor [name], Chair, Search Committee
Department of Mechanical and Industrial Engineering
University of Toronto
[Posting title and job number]

Dear Professor [name] and members of the search committee,

I am applying for the tenure-stream Assistant Professor position in [Information Engineering / Applied Machine Learning] advertised by the Department of Mechanical and Industrial Engineering. My research is on knowledge representation for engineering systems: I build formally verified first-order ontologies of physical objects and their parts and use them as specifications, audits and inductive biases for the datasets and learned policies of physical AI. I completed my PhD in Information Engineering in this department in March 2025 [confirm], hold a BASc in Industrial Engineering from the University of Toronto (2015), and am currently a postdoctoral researcher at Harvard Medical School [laboratory/department].

Three lines of work define my record. I was a core contributor to ISO/IEC 21838-4:2023, the international standard for the TUpper top-level ontology, the first top-level ontology adopted internationally with a complete first-order axiomatization in which every module has been machine-verified [confirm role wording]. With Michael Grüninger I developed a formal theory of material constitution as a parthood-preserving mapping between mereologies, and a validation of mereological pluralism; the two first-author papers are under review at Synthese. And I have carried formal methods into production: as co-founder and CEO of Uing Technologies I built ontology-governed 3D datasets of objects, indoor environments and interactions for embodied AI, shipped one of the first AR applications on the Apple Vision Pro App Store, and am first inventor on multiple patents [reconcile counts]; earlier, as a founding team member of MICAS and co-founder of YourTable Inc., I designed CRM/ERP, recommendation and ML-driven allocation systems that ran at production scale. My work has been recognized with a Distinguished Paper Award at FOIS 2018 [confirm role] and an invited presentation at AAAI [confirm].

The research statement proposes a five-year program with a single long-term question: can the part-level representations that robot-learning systems learn be shown to satisfy the axioms of parthood that humans use, and does enforcing those axioms improve generalization? The program treats a verified ontology of object parts in three roles — as a specification (a TUpper–PSL extension with representation theorems for the annotation schemas of PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled and AgiBot World), as an audit (the first quantitative measurement of parthood consistency in robot datasets, with corrected annotations and provably meaning-preserving cross-dataset mappings released publicly), and as an inductive bias (parthood constraints as auxiliary losses and a verification-in-the-loop evaluation that reports ontology-violation rate alongside task success). In years three to five the same ontology and toolkit extend to CAD assemblies and digital twins in manufacturing and to part labels in medical imaging. The outputs are engineering data quality, an ISO/IEC contribution, and a new evaluation metric for manipulation policies. I will apply for an NSERC Discovery Grant in my first cycle, a CFI JELF for a simulation and verification workstation, an NSERC Alliance grant with a robot-data or manufacturing partner, and Vector Institute affiliation.

I address directly the fact that I trained in this department. The verified-ontology methodology on which the program rests — modular first-order theories with machine-checked consistency, representation theorems and the COLORE repository — was developed in the Semantic Technologies Laboratory and has working tool support nowhere else; I expect to collaborate with Professor Grüninger, and my program is my own. His NSERC programs design perception, process and spatial ontologies and evaluate vision and reasoning benchmarks; none of my three objectives, none of the robot corpora I audit, and none of the learning experiments appears in them. My doctoral thesis was on knowledge-system architecture and top-level ontology; the proposed program is on physical object parts in robot data. Since finishing my doctorate I have worked in a different intellectual community and on a different data regime at Harvard, and I return with a research agenda, an industrial verification stack and a standards role that I built independently.

I would contribute to teaching across the Information Engineering curriculum. As a teaching assistant in this Faculty I taught in Engineering Economics and Accounting, Database Systems, Knowledge Modeling and Management, and Resource and Production Modeling. I propose an undergraduate course on data modelling and verification for engineering information systems and a graduate course on verified ontologies for engineering data, both described in the teaching statement. My commitment to equity, diversity and inclusion is set out in the enclosed statement; my graduate-student service in this department — Vice President of the MIE graduate students' association, MIE representative on the Graduate Student Union, steward for CUPE 3902 — is where it began.

[Citizenship sentence — choose one after confirming status: "I am a Canadian citizen / permanent resident of Canada." or "I am a citizen of [country] and would require a work permit; I understand Canadians and permanent residents will be given priority."] [P.Eng. sentence — choose one: "I am registered as a Professional Engineer in Ontario (licence [number])." or "I am eligible for registration as a Professional Engineer in Ontario on the basis of my accredited BASc in Industrial Engineering and [have applied / will apply] to Professional Engineers Ontario."] I disclose that I am founder and CEO of AXIOMALITY [confirm legal entity and relationship to Uing Technologies], a robotics-data verification company; on appointment I would [state the arrangement — e.g. transfer executive duties and hold a non-executive role within the University's outside-activity and conflict-of-interest policies]. My earliest start date is [1 July 2027 / negotiated date; confirm Harvard commitments].

Enclosed are my curriculum vitae, research statement, three representative publications, teaching dossier and EDI statement. My referees are Professor Michael Grüninger (University of Toronto), [Harvard supervisor, title, institution] and [external referee, title, institution]; each has agreed to write when the University requests a letter. Thank you for your consideration.

Sincerely,
Yi Ru
yi.ru@alumni.utoronto.ca · [phone] · ORCID [id]

---

## 2. Teaching statement (for the teaching dossier; 2 pages)

**Summary of teaching experience.** Teaching Assistant, Faculty of Applied Science and Engineering, University of Toronto, in four upper-year and graduate courses of the Industrial Engineering curriculum: Engineering Economics and Accounting; Database Systems; Knowledge Modeling and Management; Resource and Production Modeling [course codes and terms — verify against MIE records; obtain evaluations]. Responsibilities included [tutorials, laboratories, marking, office hours — confirm]. I have supervised or co-supervised [number] undergraduate and master's project students [confirm], and have led technical teams of engineers and data scientists in industry, including a 100+ person technology and operations team at MICAS, where onboarding and skills development were my responsibility.

**How I teach.** An engineer who can state precisely what a data model means, and check it, is worth more than one who can only build it. Everything I teach is organized around that claim, and around three habits. First, *specify before you compute*: in Database Systems I taught students to write the integrity constraints of a schema before the queries, and to treat a query result that violates a constraint as a bug in the model, not in the data; in the proposed courses, students state the axioms a dataset must satisfy and then run the check. Second, *make every claim falsifiable*: a knowledge model is not "reasonable", it is consistent or it has a counter-model, and I put model finders in students' hands early so that abstract definitions become things that break. Third, *build the whole pipeline*: in Knowledge Modeling and Management and in Resource and Production Modeling, the students who learned most were those who took a model from specification through implementation to a result they had to defend. My industry years taught me that this is also how engineers are judged.

**Proposed courses.** (1) *Data modelling and verification for engineering information systems* (undergraduate, Information Engineering stream): conceptual and logical data models; integrity constraints as logic; schema mapping and integration; consistency checking with SMT and Datalog; a term project auditing a public engineering dataset against a written specification. It complements the existing database and knowledge-modelling courses and can take over material from either [coordinate with the current instructors]. (2) *Verified ontologies for engineering data* (graduate): first-order ontologies and Common Logic; the ontology lifecycle methodology; verification with Prover9/Mace4 and the COLORE repository; ISO/IEC 21838 top-level ontologies; specification-based data auditing; case studies from robot datasets, CAD assemblies and building information models. I am also prepared to teach Engineering Economics and Accounting, Database Systems and the Faculty's design courses [P.Eng. status permitting].

**Assessment and mentoring.** I assess with projects that produce an artifact a reviewer can run — a schema with its constraints, an ontology with its verification log, an audit report — and with short in-class exercises that check the reasoning, not the recall. Graduate students in my group own an open research question stated as a theorem to prove or a measurement to make (the research statement tags each one), publish their software with their results, and present at the U of T Robotics Institute and Vector Institute seminars from their first year. I will take on undergraduate summer research students each year through [the MIE summer research program — confirm name] and will co-supervise capstone projects with industrial partners.

**Evidence.** Teaching evaluations for the four TA assignments [attach; obtain from MIE]; sample syllabi for the two proposed courses [write; attach]; [any teaching awards or training — e.g. TATP certificates — confirm].

---

## 3. Equity, diversity and inclusion statement (1 page)

I have three concrete commitments, each of which I have already practised in some form.

*In the research.* The datasets my program audits come from a small number of laboratories and depict objects, homes and workplaces from a narrow range of regions, and assume users with a narrow range of physical abilities. The ontology separates structural parthood from culturally specific object categories, and every audit report will state coverage by source so that these gaps are documented rather than hidden. All axioms, mappings, code and corrected annotations will be released under an open licence, so that groups without access to proprietary robot data — and universities without a robotics laboratory — can build on the work.

*In the group.* I will recruit deliberately from equity-deserving groups, advertise every position through the Faculty's and the University's EDI channels [name the programs after confirming], and structure supervision so that a student's first result is a verification or a measurement they own, published under their name. I will mentor [an undergraduate research student from an equity-deserving group each year — confirm the program and the commitment], and I will teach in a way that makes formal methods usable by students who did not arrive with a logic background, because in my experience that is most of them.

*In the department.* As a graduate student here I served as Vice President of the MIE graduate students' association (AMIGAS), as the MIE representative on the Graduate Student Union, and as a steward and representative for CUPE 3902, where the work was the representation of teaching assistants and the fair application of collective-agreement terms across a diverse graduate body. I am bilingual in English and Mandarin and have presented this research to academic and industrial audiences in North America and Asia; I will use that reach to recruit international students and to connect them with the Faculty's support services. [Add any equity-focused activities at Harvard or in industry — confirm.]

I recognize that the University of Toronto welcomes applications from racialized persons, women, Indigenous peoples, persons with disabilities, LGBTQ2S+ persons and others who contribute to the diversification of ideas, and I will apply the same standard to my own hiring and supervision. [Self-identification, if the applicant wishes, is made in the University's confidential survey, not here.]

---

## 4. CV outline (for the dedicated CV field; populate from the master CV)

1. Personal: Yi Ru (茹意); yi.ru@alumni.utoronto.ca; [phone]; ORCID [id]; languages English, Mandarin Chinese. [Citizenship/PR status — optional.] [P.Eng. status.]
2. Education: PhD, Information Engineering, U of T MIE, requirements completed March 2025 (Fast Track PhD; GPA A); thesis [title]; supervisor [name]. BASc, Industrial Engineering (Minor: Engineering Business), U of T, June 2015; President Scholarship; Dean's Honours List; 5T3 Alumni Scholarship.
3. Positions: Postdoctoral Researcher, Harvard Medical School, [lab], [start]–present. Co-Founder and CEO, Uing Technologies, Aug 2022–present [and AXIOMALITY, 2026 — confirm entity]. Founding Team, MICAS, Jul 2021–Aug 2022. Venture Capital Intern, IDG Capital, Mar 2018–Jun 2021. Co-Founder, YourTable Inc., Mar 2018–Jun 2021.
4. Awards: Distinguished Paper Award, FOIS 2018 [role]; invited AAAI presentation [confirm]; Lo Family Social Venture Fund; Collision 2019 Canadian startup representative; [doctoral scholarships — list].
5. Standards: ISO/IEC 21838-4:2023 (TUpper), core contributor, ISO/IEC JTC 1/SC 42 [working-group designation; current activity].
6. Patents: [13 granted; 9 applications — numbers, titles, jurisdictions, dates; reconcile with "3 Chinese invention patents; 9–10 German utility patents"].
7. Publications: refereed journal articles [list; 20+ SCI-indexed to confirm]; submitted: Ru & Grüninger ×2 (Synthese, 2026); refereed conference papers [FOIS, JOWO, ICBO, IEEE/ACM — list]; monograph [title, publisher — confirm]; technical reports and software.
8. Presentations: invited talks; conference presentations; standards-committee presentations [list].
9. Teaching: the four TA assignments with codes and terms; guest lectures; students supervised.
10. Service and leadership: AMIGAS VP; GSU MIE representative; CUPE 3902 steward; Session Chair, IISE 2017; reviewing [list].
11. Industry outcomes (one block, factual): Apple Vision Pro App Store launch; nine invention patent applications led at Uing; MICAS: >USD 5M angel investment incl. Accel, >USD 50M annual revenue, 100+ team, KOL ROI >4; YourTable: incubated by U of T, Schulich, Imperial College London; Tim Hortons Canada collaboration.
12. Referees: Prof. Michael Grüninger (MIE, U of T); [Harvard supervisor]; [external expert].

---

## 5. Job-talk plan (research seminar, 45 minutes + questions)

Title: *Do robots learn parts? Verified ontologies as specification, audit and inductive bias for physical AI.*

| Minutes | Segment | Content and evidence |
|---|---|---|
| 0–5 | The question | A drawer, a lid, a handle: three datasets, three incompatible definitions of "part". The long-term challenge in one sentence. Why a search committee in Information Engineering should care: data integration is the department's problem, and this is data integration with proofs |
| 5–15 | What an ontology can prove | TUpper and ISO/IEC 21838-4 in two slides; verification vs. validation; the constitution mapping from the Synthese papers and the theorem in plain language [insert]; a live Mace4 counter-model for a naive parthood schema |
| 15–27 | Audit: what the field is training on | Pipeline (Datalog/SMT tier, prover tier, UNKNOWN as an output); first results on [PartNet / PartNet-Mobility — whichever the applicant has run by the talk; otherwise the pipeline design and a worked example from the Uing 3D corpus]; violation profile by axiom family; the cross-dataset mapping theorem |
| 27–37 | Learning: does it help? | Parthood constraints as auxiliary losses; verification-in-the-loop evaluation; preliminary SAPIEN result or the experimental design with hypotheses and power [state clearly which]; violation rate as a failure predictor |
| 37–42 | The five-year program | Three themes, six trainee slots, the funding sequence (Discovery, JELF, Alliance, Vector); extension to CAD assemblies and medical part labels; the SC 42 contribution |
| 42–45 | Why here | The Semantic Technologies Laboratory, the Robotics Institute, Vector; what the group would offer MIE students; one slide on independence from existing programs, said once and plainly |

Preparation: rehearse once with Prof. Grüninger and once with a Robotics Institute colleague [name]; prepare backup slides on the industrial verification stack (for questions on feasibility), on the Harvard work (for questions on breadth), and on the company (for questions on time commitment — answer with the arrangement stated in the cover letter). Bring the theorem, the counter-model and one measured number; the committee remembers those.
