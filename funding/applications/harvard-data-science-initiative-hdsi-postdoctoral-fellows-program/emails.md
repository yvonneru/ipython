# Emails — HDSI Postdoctoral Fellows Program (2026-27 call)

Send order: 1 (HDSI program office) and 2 (HMS supervisor) by 3 Oct; 3 and 4 (prospective Harvard mentors) by 10 Oct after checking the HDSI faculty pages and departmental directories; 5 (Prof. Grüninger) and 6 (external referee) by 24 Oct once mentors have agreed; 7 (referee package) at deadline − 21 days. Deadline: [November or early December 2026 — confirm]. [Brackets] to confirm. No company officer email is needed: this is an individual fellowship.

## 1. To the HDSI program office — send by 3 Oct

**To:** datascience@harvard.edu
**Subject:** Postdoctoral Fellows Program 2026-27 — eligibility of a current Harvard postdoc and application details

Dear HDSI team,

I am a postdoctoral researcher at Harvard Medical School ([laboratory/department]) and intend to apply to the Postdoctoral Fellows Program for the coming cycle. Before I approach faculty, could you confirm a few points?

1. Is the 2026-27 call open or expected to open, and what is the application deadline?
2. Are current Harvard postdoctoral researchers eligible, and must the faculty we name be outside our current laboratory?
3. What is the PhD window for eligibility, and is it counted from the date requirements were met or the conferral date? (Mine were completed in March 2025.)
4. What are the components and limits — research statement length, whether a separate personal statement or cover letter is required, number of reference letters and their deadline, and whether faculty we name submit anything themselves?
5. What are the 2026-27 salary and research allocation, and the expected start date?

Thank you very much.

Yi Ru
Postdoctoral Researcher, Harvard Medical School · yi.ru@alumni.utoronto.ca

## 2. To the Harvard Medical School postdoctoral supervisor — send by 3 Oct

**Subject:** HDSI Postdoctoral Fellows application — heads-up, and a reference

Dear [name],

I would like to apply to the Harvard Data Science Initiative's Postdoctoral Fellows Program for the coming cycle (deadline expected in [November/early December]). The proposed program is the one I have described to you: a verified ontology of object parts used to audit and align the part-level datasets physical-AI models are trained on, with an extension to anatomical part labels in medical imaging [one sentence linking to the laboratory's interests, if applicable]. It is my own program and would be run with faculty in Statistics, SEAS and Biomedical Informatics.

Two requests. Would you be willing to write one of my reference letters? Letters are uploaded through HDSI's portal; I will send the draft statement and a one-page brief three weeks before the deadline. And could you tell me whether you would be comfortable being one of the faculty I name, or whether — as I expect HDSI may require — the named faculty should be outside our laboratory? Either way I want the application to be something you are comfortable with.

I should also say that I am applying in parallel to postdoctoral awards in Canada with a spring-2027 start, as I mentioned; only one path can be taken and I will keep you informed at each step. Nothing changes here in the meantime.

Thank you,
Yi

## 3. To a prospective mentor in Statistics or Computer Science (Mentor 1) — send by 10 Oct

**Subject:** HDSI Postdoctoral Fellows application — would you be willing to be a named faculty mentor?

Dear Prof. [name],

I am a postdoctoral researcher at Harvard Medical School, with a PhD in Information Engineering from the University of Toronto (2025), and I am preparing an application to the HDSI Postdoctoral Fellows Program. Applicants name at least two Harvard faculty with whom they would like to work; I am writing to ask whether you would be willing to be one of them.

The program is a data-quality method for hierarchically annotated data. Robot-learning datasets (PartNet, PartNet-Mobility, GAPartNet, AgiBot World, Open X-Embodiment, DROID) annotate objects as hierarchies of parts under independently designed schemas, and no one has checked them against any formal specification of parthood. I build that specification as a verified first-order ontology (I am a core contributor to ISO/IEC 21838-4, and co-author of a formal theory of when two part decompositions are compatible, under review at Synthese), compile its decidable fragment to Datalog/SMT for a bulk audit with theorem proving for residual cases, and release corrected annotations and provably meaning-preserving cross-dataset mappings. The component I would hope to work on with you is the measurement design: violation rates by axiom family with bootstrap intervals, stratified by category and depth, with annotators and source laboratories as random effects so that disagreement is estimated rather than averaged away [adjust to the faculty member's methods]. A two-page summary is attached.

What I would ask: agreement to be named, roughly monthly meetings if the fellowship is awarded, and a short confirmation if the portal requests one [verify]. What you would get: an ontology-aligned corpus and audit toolkit usable in your own work and co-authorship on the audit paper. I would be glad to meet at your convenience.

Best regards,
Yi Ru

## 4. To a prospective mentor in SEAS (Mentor 2) or HMS/DBMI (Mentor 3) — send by 10 Oct

**Subject:** HDSI Postdoctoral Fellows application — would you be willing to be a named faculty mentor?

Dear Prof. [name],

[Opening paragraph as in email 3.]

[For Mentor 2 (robot learning):] The component I would hope to work on with you is the effect of the specification on learning: training part-aware manipulation policies in SAPIEN [and your simulator of choice] on native versus ontology-aligned pooled data, evaluating on held-out PartNet-Mobility categories, and adding differentiable parthood constraints and a verification-in-the-loop protocol that reports a policy's ontology-violation rate alongside task success. I would need access to a policy-training pipeline and compute; in return the group gets an aligned corpus, an interpretable failure signal and co-authorship on the methods paper.

[For Mentor 3 (biomedical ontologies / segmentation):] The component I would hope to work on with you is the health-sciences extension: running the same audit on a multi-organ segmentation resource against an anatomical partonomy [e.g., TotalSegmentator against the Foundational Model of Anatomy — adjust to the faculty member's resources] to measure where segmentation practice and anatomical theory diverge. No patient-identifiable data is needed for a label-hierarchy audit [confirm]. In return the group gets a data-quality report on the resource and co-authorship on the imaging paper.

[Closing paragraph as in email 3.]

Best regards,
Yi Ru

## 5. To Prof. Michael Grüninger — send by 24 Oct, after mentors agree

**Subject:** HDSI Postdoctoral Fellows (Harvard) — external collaborator and reference, alongside the CPRA

Dear Michael,

Following the CPRA and the Kempner note: I am also applying to the Harvard Data Science Initiative's Postdoctoral Fellows Program, a two-year fellowship with a deadline in [November/early December]. It is the same program — the verified parts ontology, the dataset audit and the measured effect on learning — but written for a data-science committee, so the audit pipeline and the measurement design lead and there is an extension to anatomical part labels in medical imaging.

Two requests. HDSI requires Harvard faculty as the named mentors, so may I name you as external collaborator for the COLORE verification methodology and the contribution back to SC 42, as in the other applications? And would you write a reference letter? Letters are uploaded through HDSI's portal; I have asked referees for [deadline − 7 days]. The draft statement is attached with a one-page brief on what reviewers weigh; it reuses the CPRA outline, so the reading is short.

As with Kempner, an HDSI start in [September 2027] and a Toronto start in spring 2027 cannot both happen; I am applying to both and will decide when offers arrive, and I will keep you informed at every step.

Best,
Yi

## 6. To the external referee [name — applied ontology, data integration or robot learning] — send by 24 Oct

**Subject:** Reference for the Harvard Data Science Initiative Postdoctoral Fellows Program — by [date]

Dear [name],

I am applying to the Harvard Data Science Initiative's two-year Postdoctoral Fellows Program, on a program that applies verified mereological ontologies to the auditing and alignment of part-level annotations in robot-learning and medical-imaging datasets. Would you be willing to serve as one of my [three] referees?

You would receive an upload link from HDSI's portal once I enter your name, and the letter would be due by [deadline − 7 days, or the portal's referee date]. I attach a one-page brief on the program and what reviewers weigh, together with the research statement and my CV.

Thank you for considering it — please let me know if the timing is difficult and I will adjust.

Best regards,
Yi Ru

## 7. Referee package — send at deadline − 21 days to all referees

**Subject:** HDSI Postdoctoral Fellows — final draft and referee brief

Dear [name],

Thank you again for agreeing to write. Attached are the final research statement, the cover letter/personal statement, my current CV and the one-page referee brief. The named Harvard faculty are [Mentor 1], [Mentor 2] and [Mentor 3]; Prof. Grüninger is external collaborator. The portal link should have reached you from HDSI; if it has not by [date], please tell me and I will re-send the request. The letter deadline is [date].

With thanks,
Yi
