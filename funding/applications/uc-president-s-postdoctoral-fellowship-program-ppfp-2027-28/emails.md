# Emails — UC President's Postdoctoral Fellowship 2027–28

Send order (see the gate at the top of README.md):
- **3 (program office) — now.** It commits no one and its answers feed the go/no-go.
- **1 and 2 (mentor candidates) — only after the applicant has recorded "PPFP: go" in STRATEGY.md (by 8 Oct 2026); send by 10 Oct 2026** (registry next action). STRATEGY.md Addendum 5 skips the US fork by default; without the recorded decision, nothing below is sent.
- **4–6 (referees) — only after a tenured UC mentor has agreed (by 20 Oct) and after the CPRA is filed (17 Oct)**, so no PPFP request competes with the CPRA letters.

Attach to 1, 2 and 4–6: proposal.md (as PDF), statement.md (as PDF), CV. [Brackets] to fill.

---

## 1. To the proposed mentor at UC San Diego — send by 10 October 2026, after the go decision

[Before sending: confirm on the UCSD CSE directory and his homepage that Prof. Su still holds a tenured UCSD appointment (search on 2026-09-26 found him listed as Associate Professor and Hillbot co-founder/CTO, and an April 2026 press report suggesting he might move); if he has left UCSD or is on extended leave, he cannot serve and email 2, or another tenured UCSD robotics faculty member [name], becomes primary.]

Subject: UC President's Postdoctoral Fellowship 2027–28 — would you consider serving as my faculty mentor? (verified parts ontology + audit of PartNet-Mobility)

Dear Professor [Su — confirm],

I am a postdoctoral researcher at Harvard Medical School and completed my PhD in Information Engineering at the University of Toronto in 2025. I am writing to ask whether you would consider serving as my faculty mentor for an application to the UC President's Postdoctoral Fellowship Program (applicant deadline 1 November; mentor letter due 1 December), to be held in your group from [September 2027]. The program asks for a tenured UC faculty mentor other than the dissertation advisor; my advisor is at Toronto.

My research builds formally verified first-order ontologies of physical objects and their parts and uses them as specifications, audits and inductive biases for robot-learning data and policies. I was a core contributor to ISO/IEC 21838-4:2023 (the TUpper top-level ontology), and with Michael Grüninger I have developed a theory of material constitution as a parthood-preserving mapping between mereologies (two papers submitted to Synthese) that states exactly when two part decompositions of one object are compatible. The program I propose applies that theory to the datasets your group maintains: a verified ontology of rigid, articulated, functional and assembly parts; an automated audit of PartNet, PartNet-Mobility, GAPartNet and the large real-robot corpora for parthood-axiom violations and cross-dataset inconsistency, which nobody has yet checked against any formal specification; and then the ontology as a constraint on part-aware manipulation policies in SAPIEN, measuring the effect on generalization to held-out categories. The proposal (under 1,000 words) and a short background statement are attached. Everything — axioms, mappings, corrected annotations, code — would be released openly, and I would want corrections to flow back into the datasets themselves.

I have also built and shipped production data systems as a founder, so the audit at dataset scale is engineering I have done before, not only proposed.

If this is of interest, I would be glad to talk at any time in the next two weeks. What I would ask of a mentor is the letter of support by 1 December, a place in the group from the start date, and access to the SAPIEN/PartNet-Mobility infrastructure for the audit; what the group would get is a verified parts ontology, a quantitative audit of its own datasets, and co-authorship on the audit and learning papers.

Thank you for considering it.

Best regards,
Yi Ru
[phone] · yi.ru@alumni.utoronto.ca

---

## 2. To a UC Berkeley (BAIR) faculty candidate — send by 10 October 2026, after the go decision, in parallel or as fallback

[Choose a **tenured** BAIR faculty member (assistant professors cannot serve as primary mentor) whose group produced one of the audited corpora — e.g., [Sergey Levine, EECS — DROID / Open X-Embodiment co-author; confirm tenure, fit and willingness] — and verify tenure on the department directory before sending.]

Subject: UC President's Postdoctoral Fellowship 2027–28 — mentor inquiry (verified ontologies for robot-learning data)

Dear Professor [name],

I am a postdoctoral researcher at Harvard Medical School (PhD, Information Engineering, University of Toronto, 2025), and I am writing to ask whether you would consider serving as my faculty mentor for the UC President's Postdoctoral Fellowship (applicant deadline 1 November; mentor letter due 1 December; start [September 2027]). The program asks for a tenured UC faculty mentor other than the dissertation advisor; my advisor is at Toronto.

[Two sentences on why this group: name the group's datasets, benchmarks or policy-learning work that the audit (O2) or the constraint-based training (O3) would use, drawn from the group's own publications — do not send until filled.]

My work builds formally verified first-order ontologies of physical objects and their parts (ISO/IEC 21838-4:2023 core contributor; a theory of material constitution and mereological pluralism with Michael Grüninger, two papers submitted to Synthese) and uses them to audit the part-level datasets robot-learning models are trained on and to constrain part-aware manipulation policies. The attached proposal sets out the three objectives; the audit would produce the first quantitative measurement of parthood consistency in robot datasets, released openly, and the learning experiments test whether ontology-consistent training improves generalization to unseen categories.

I would be glad to talk at your convenience in the next two weeks. Thank you for considering it.

Best regards,
Yi Ru

---

## 3. To the PPFP program office — send now

To: [ppfpinfo@berkeley.edu — address from a 2026-09-26 search snippet; confirm on the ppfp.ucop.edu contact page]

Subject: 2027–28 application — four questions before I apply

Dear PPFP Program Office,

I am considering an application to the President's Postdoctoral Fellowship Program for 2027–28 with a mentor at [UC San Diego / UC Berkeley]. Four questions the website did not settle for my case:

1. Is the applicant deadline 1 November 2026 (a Sunday) with mentor and reference letters due 1 December 2026, as in the 2026–27 cycle, and is the mentor named in the application before submission?
2. Is the appointment one year with a possible second year, when are 2027–28 awards announced, and what is the start-date window?
3. My dissertation advisor is [name]; one reference must be the thesis advisor. If the advisor is [unavailable / on leave], may a co-supervisor or thesis committee member substitute?
4. I am the founder of a small company. Is there a program policy on outside activities during the fellowship, beyond the host campus's own policy? [If relevant: I am not a US citizen [status]; the website says selected fellows must document work authorization — is visa sponsorship arranged by the host campus?]

Thank you.

Yi Ru
[phone] · yi.ru@alumni.utoronto.ca

---

## 4. To the thesis advisor — send once a mentor has agreed and the CPRA is filed

[If the thesis advisor is Prof. Grüninger, merge 4 into 5: he is the required advisor reference, and the second reference becomes the Harvard supervisor (email 6, bracketed paragraph).]

Subject: Reference for the UC President's Postdoctoral Fellowship — letter due 1 December

Dear [name],

I am applying to the UC President's Postdoctoral Fellowship Program for a fellowship in [Prof. Hao Su's group at UC San Diego — confirm], starting [September 2027], on a program that applies verified mereological ontologies to object–part representation in robot-learning datasets. The program requires one reference from the thesis advisor. Would you be willing to write it?

The application is due 1 November; after I submit, the system will email you a link to upload a letter, due 1 December (I have asked for 24 November so I can confirm receipt). I attach a one-page brief on what reviewers score and the points that would help most, together with the proposal, my background statement and CV. [If the CPRA request went to the same person: the CPRA letter from October can be adapted; the main difference is the emphasis on readiness for a faculty career and on the mentor's environment.]

Thank you — and please tell me if the timing is difficult.

Best regards,
Yi

---

## 5. To Prof. Michael Grüninger — send once a mentor has agreed and the CPRA is filed

Subject: UC President's Postdoctoral Fellowship (US option, Sept 2027) — reference and a heads-up

Dear Michael,

Alongside the CPRA application you are supporting, I am keeping one US option open: the UC President's Postdoctoral Fellowship, with [Prof. Hao Su at UC San Diego — confirm], whose group maintains SAPIEN and PartNet-Mobility, as proposed mentor. The program is the same as the CPRA outline — the parts ontology as a TUpper extension with PSL, the dataset audit, and the ontology as a constraint on policies — but the audit would be done with the maintainers of the datasets. A UC fellowship would start in September 2027 and could not be held with a spring-2027 Toronto award, so this is a fallback, not a change of plan; if the CPRA is awarded on 31 March 2027 I will withdraw or decline.

Would you be willing to serve as my second reference (the first must be my thesis advisor)? The application is due 1 November; the system emails you an upload link after I submit, and letters are due 1 December (I have asked for 24 November). The CPRA text adapts directly; the criteria add readiness for a faculty career and the mentor's environment. A one-page brief and the proposal are attached.

I would also like to use the material-constitution manuscript as my writing sample (up to 35 pages, PDF). Are you comfortable with that while it is under review at Synthese?

Best,
Yi

---

## 6. To the Harvard postdoctoral supervisor — send once a mentor has agreed and the CPRA is filed

Subject: UC postdoctoral fellowship application (Sept 2027 option) — heads-up

Dear [name],

In addition to [the Canadian award I mentioned — adjust to what the supervisor already knows], I am applying to the UC President's Postdoctoral Fellowship for a fellowship starting [September 2027] with [Prof. Hao Su at UC San Diego — confirm] as mentor. The application is due 1 November. [If asked to serve as the second reference instead of Prof. Grüninger: Would you be willing to serve as one of my two references? The system emails an upload link after submission; letters are due 1 December.] Nothing changes here before [summer 2027], and I will keep you informed of the outcome.

Thank you,
Yi
