# Cover letter and team statement — ARIA Rolling Opportunity Seed

ARIA takes no separate personal statement; the seed form asks for the team and why it is the right one [verify field names]. ARIA states that ideas can come from anywhere and welcomes early-career applicants and atypical backgrounds; the team statement leans on that rather than on seniority. The cover letter below accompanies the submission or an initial approach to the Programme Director; the team statement is written to paste into the form.

---

## Cover letter

[Date]

[Programme Director name], Smarter Robot Bodies [or Safeguarded AI]
Advanced Research and Invention Agency, London

Dear [Dr./Prof. name],

I am submitting an Opportunity Seed proposal, "Machine-checkable evidence for robot training data", led from [UK host institution] with the Semantic Technologies Laboratory at the University of Toronto and the robotics-data company AXIOMALITY as partners. It asks for GBP [amount] over 12 months.

The idea is simple to state and has never been tried: treat the part-level datasets that physical AI is trained on — PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World — as artefacts that can be checked against a formal specification, and build that specification as a verified first-order ontology of physical object parts. No dataset or learned model is currently required to satisfy the axioms of parthood; the poor transfer across part vocabularies and brittle generalization to new object categories that the field observes have never been measured, because there has been nothing to measure them against. In twelve months we will release the verified ontology, the first quantitative audit of parthood consistency in robot datasets with corrected annotations and proof-backed cross-dataset mappings, a merged corpus, an audit toolkit, and simulation evidence on whether ontology-consistent training improves generalization and whether ontology-violation rate predicts task failure.

I bring the three things the seed needs. I am a core contributor to ISO/IEC 21838-4:2023, the international standard for the TUpper top-level ontology, so the ontology will be built on a standard I helped verify and can be contributed back through ISO/IEC JTC 1/SC 42. With Prof. Michael Grüninger I developed a formal theory of material constitution as a parthood-preserving mapping between mereologies, now under review at Synthese, which is exactly the theory of when two part decompositions of one object are compatible. And I have carried formal methods into production: as a founder I shipped ontology-governed data-integration systems at scale, and AXIOMALITY, the company I founded in 2026, has built an offline verification Engine and a machine-proven-consistent knowledge kernel that this seed will use as its testbed.

The work is ambitious in ARIA's sense: if violation rate predicts failure, robot policies gain an interpretable, machine-checkable failure signal independent of task labels; if ontology-aligned pooling transfers across part vocabularies, the field's separate datasets become one corpus. Either result changes how physical-AI data is built and bought, ahead of the evidence requirements the EU AI Act will impose on robots from August 2028.

More than half of the work — the audit pipeline, the simulation experiments and the funded research-engineer post — is carried out at [UK host] under [UK co-lead], which is the lead organisation for the award; the toolkit, corrected data and audit service will be homed there, and the commercial follow-on will be offered first to UK robot builders [name any UK design partner, or delete]. I would welcome a conversation before or after review, and I can demonstrate the current verification pipeline on any part-level dataset the programme cares about.

Yours sincerely,

Yi Ru, PhD
Postdoctoral Researcher, Harvard Medical School [confirm appointment wording; not on the CV] · Founder and CEO, AXIOMALITY
yi.ru@alumni.utoronto.ca · ORCID [id]

---

## Team statement (for the form)

**Dr. Yi Ru — lead applicant (formal ontology, verification, data systems).** PhD in Information Engineering, University of Toronto (2025; Fast Track PhD); postdoctoral researcher, Harvard Medical School, [laboratory/department], since [month year — confirm; the appointment is not on the CV]; about 1.5 years post-PhD. Core contributor to ISO/IEC 21838-4:2023 (TUpper) within ISO/IEC JTC 1/SC 42 [confirm role wording]. First author of two formal-ontology papers submitted to Synthese (2026) with M. Grüninger. Founder/CEO of AXIOMALITY (2026); co-founder and CEO of Uing Technologies (2022–present), which built structured 3D physical-world datasets and launched one of the first AR pet-interaction apps on the Apple Vision Pro App Store; founding-team member of MICAS (>USD 5M angel investment; >USD 50M annual revenue; 100+ team); first inventor on granted patents in 3D recognition, indoor modelling and automatic reconstruction [reconcile counts]. Distinguished Paper Award, FOIS 2018 [confirm role]. Owns O1 (ontology), the audit design in O2, and overall delivery.

**[UK co-lead — name, institution] (robot learning / formal verification).** [Two sentences: group, relevant datasets or simulators, prior work on part-aware manipulation or on verification of learned systems.] Owns the UK-based audit pipeline execution and the SAPIEN experiments (O2 execution, O3); hosts the project and administers the award.

**Prof. Michael Grüninger — collaborator, University of Toronto (MIE), Semantic Technologies Laboratory.** Author of the ontology lifecycle methodology, the Process Specification Language and the COLORE repository (2,580+ first-order ontologies); lead of TUpper (ISO/IEC 21838-4); current NSERC programs "Ontologies for the Physical Turing Test" and "Commonsense Cobotics", the latter asking which mereotopologies are implicit in ShapeNet and PartNet decompositions. Provides the verification framework, COLORE placement and SC 42 dissemination; co-supervises the ontology work [pending his agreement].

**AXIOMALITY — industrial testbed and translation partner [role to decide].** CTO ([name]; McMaster University AI doctorate); robotics lead ([name]; mechanical/electronic engineering doctorate, autonomous-system perception); senior 3D asset lead ([name]; 10+ years production experience). Supplies the offline verification Engine (ingestion → scene graph → SMT check), adapters for LeRobot, RLDS, ROS 2/MCAP, OpenUSD/USDZ, PLY and JSON, and 100,000 measured 3D asset packages [confirm licence for research use]. Carries results into the data Passport product. [Legal entity, country of incorporation, ownership and headcount — confirm before naming the company on the form.]

**Why this team fits ARIA's portfolio.** It mixes the team types ARIA looks for — an academic formal-methods group, a robotics group with real experiments, and a start-up with an engine and a market — around one artefact, and it is measured on results: an ontology that verifies, numbers on datasets people already train on, and a policy experiment with a pre-registered hypothesis. The lead is early-career (PhD 2025) with a founder's rather than a conventional academic track, which ARIA says it welcomes. **UK benefit:** the award is held and more than half the work done at [UK host]; the toolkit, data releases and audit service are homed in the UK; the founder's conflict of interest with AXIOMALITY is declared and the company's role is in kind.
