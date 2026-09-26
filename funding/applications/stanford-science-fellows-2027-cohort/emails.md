# Emails — Stanford Science Fellows (2027 cohort)

Send order (deadline 16 October 2026, 11:59 pm Eastern, per the program FAQ — confirm on the page before sending anything): 1 (program office) and 7 (SGS) today; 2 (Grüninger) today; 3–4 (candidate hosts) today after checking the Stanford directory; 5 (formal-methods host, optional) today; 6 (HMS supervisor) today; 8 (referees) once the host is confirmed and the draft is final (target 2 Oct). If the program office replies that computer science / robotics is out of scope, or that the prior-postdoc cap is exceeded, stop and do not send 8. [Brackets] to confirm.

## 1. To the Stanford Science Fellows program office — send today

**Subject:** Stanford Science Fellows 2027 — three eligibility questions before I apply

Dear Stanford Science Fellows team,

I am preparing an application for the 2027 cohort (deadline 16 October) and have three questions the FAQ does not settle for my case.

1. Scope. My research is in knowledge representation and automated reasoning applied to robot-learning datasets — a formally verified first-order theory of parts and wholes, tested empirically against the datasets that manipulation policies are trained on. Does the program treat computer science and robotics of this kind as "fundamental research in a natural science discipline"?
2. Prior postdoctoral experience. I have held a postdoctoral appointment at Harvard Medical School since [month year]. For the two-year limit measured at the fellowship start, is the count made in whole months to the start date I request (I would request 1 July 2027), and are partial months or leave counted?
3. PhD date. All requirements for my PhD (University of Toronto) were completed in March 2025 and the degree was conferred in [month 2025 — confirm]. I understand either date is within the window; please tell me if the program needs the conferral date documented in a particular form.

Two smaller questions: is there a page limit or prompt for the career statement beyond the font and margin rules; and is there a place in the application to disclose an outside activity (I am a founder of a small company outside my research role)?

Thank you very much.

Yi Ru
Postdoctoral Researcher, Harvard Medical School
yi.ru@alumni.utoronto.ca

## 2. To Prof. Michael Grüninger — send today

**Subject:** Stanford Science Fellows (deadline Oct 16) — collaborator and reference, alongside the CPRA

Dear Michael,

Following my note about the CPRA: a further opportunity has a deadline three weeks out, and I would like to apply to it in parallel. Stanford's Science Fellows program is a university-wide three-year postdoctoral fellowship (stipend, research funds, professional development) for fundamental research across the natural sciences, with a Stanford faculty host. The program is the same — the verified parts ontology as a TUpper extension with PSL, the audit of the part-level robot datasets, and the ontology as an inductive bias for part-aware policies — with the Stanford angle that PartNet/ShapeNet and DROID, two of the corpora I would audit, were built there [in part].

Two requests. First, may I name you as external collaborator on Theme 1, for the COLORE verification methodology and the contribution back to SC 32? The fellowship requires a Stanford host, so your role would be collaborator rather than supervisor. Second, would you write a reference letter? The program advises that one of the three letters come from the PhD advisor [confirm that Michael was the PhD supervisor of record — the profile leaves this blank]. Letters are uploaded through Academic Jobs Online; I have asked referees for October 12. The draft research statement (two pages) and career statement are attached, with a one-page brief on what reviewers weigh; the research statement reuses the CPRA outline, so the reading is short.

One more small thing: could you send me the reference list from the Physical Turing Test and Cobotics proposals for the mereotopology verification and vision-benchmark analysis papers? I cite them as [14] and want the published versions.

I should say plainly that a Stanford start in July 2027 and a Toronto start in spring 2027 cannot both happen; I am applying to both and will decide when offers arrive, and I will keep you informed at every step.

Best,
Yi

## 3. To candidate host 1 (PartNet/ShapeNet or DROID author; robot learning / 3D perception) — send today

**Subject:** Stanford Science Fellows — would you consider being my faculty host? (deadline Oct 16)

Dear Prof. [name],

I am a postdoctoral researcher at Harvard Medical School, and a knowledge-representation researcher by training (PhD, University of Toronto, 2025; core contributor to ISO/IEC 21838-4, the TUpper top-level ontology standard [confirm role wording]). I am applying to the Stanford Science Fellows program and am writing to ask whether you would consider being my faculty host. The program requires that a host agree before an award is made; a letter of support from the host is optional, and I would ask for only a short one.

The proposal asks what learned manipulation policies represent about parts and wholes. I build a verified first-order ontology of object parts, audit the part-level datasets the field trains on (PartNet, PartNet-Mobility, GAPartNet, AgiBot World, Open X-Embodiment, DROID) against it — nobody has yet checked them against any formal specification — and then use the ontology as an inductive bias: differentiable relaxations of parthood constraints as auxiliary losses, constraint-guided augmentation, and an evaluation protocol that reports ontology-violation rate beside task success, in SAPIEN on held-out PartNet-Mobility categories. Your group built [PartNet / DROID — one sentence on the host's dataset or robot-learning work — confirm], which is why I am asking you rather than anyone else: the audit is most useful to the people who designed the annotation schema, and what I would bring is a verified ontology, an audit toolkit and a public, ontology-aligned corpus.

The deadline is October 16, so I would be grateful for even a short reply. I attach the two-page research statement and would be glad to meet for twenty minutes this week.

Best regards,
Yi Ru

## 4. To candidate host 2 (robot manipulation and learning) — send today

**Subject:** Stanford Science Fellows — faculty host for a verified-ontology approach to part-aware manipulation (deadline Oct 16)

Dear Prof. [name],

I am a postdoctoral researcher at Harvard Medical School applying to the Stanford Science Fellows program, and I am writing to ask whether you would consider being my faculty host (the program requires a host's agreement before an award; a host letter is optional).

My background is formal ontology: I build first-order theories of parts and wholes whose consistency is machine-checked, and with Michael Grüninger (Toronto) I developed a theory of when two part decompositions of the same object are compatible (under review at *Synthese*). The fellowship proposal applies this to robot learning: a verified ontology of object parts, an audit of the part-level datasets the field trains on, and — the part I would want your guidance on — training and evaluation methods that use the ontology to improve generalization to unseen object categories and report, beside task success, whether a policy's inferred object structure violates the axioms. Your work on [one sentence on the host's manipulation or policy-learning work and platform — confirm] is the setting I would want to run these experiments in, in simulation in years one and two and on your platform in year three.

The deadline is October 16. I attach the two-page research statement and would welcome a short conversation this week if you have time.

Best regards,
Yi Ru

## 5. To a formal-methods or knowledge-systems faculty member (optional; as host or informal second mentor) — send today

**Subject:** Stanford Science Fellows — the formal-methods side of a robot-learning proposal (deadline Oct 16)

Dear Prof. [name],

I am applying to the Stanford Science Fellows program and would like to ask whether you would consider [being my faculty host / acting as an informal second mentor] for the formal-methods side of the program.

The proposal verifies a first-order ontology of object parts (Common Logic; Prover9/Mace4), compiles a fragment of it to Datalog/SMT to audit millions of part annotations in robot-learning datasets with theorem proving for the residual cases, and relaxes the same axioms into differentiable losses for policy training. The open questions I would want your view on are which fragment compiles to SMT without losing violations the prover finds, and how to keep the relaxation faithful to the axioms. Your work on [one sentence — confirm] bears directly on both[; and the third-year transfer of the audit to biomedical part labels is where a knowledge-systems group would make the difference — adjust to the recipient].

The deadline is October 16; the two-page research statement is attached. A twenty-minute conversation this week would be very welcome.

Best regards,
Yi Ru

## 6. To the Harvard Medical School postdoctoral supervisor — send today

**Subject:** Stanford Science Fellows application (deadline Oct 16) — reference and a heads-up

Dear [name],

I would like to apply for the Stanford Science Fellows program (start [1 July 2027], three years), on the program I described to you — verified ontologies of object parts as specification, audit and inductive bias for robot learning. The deadline is October 16.

Would you be willing to write a reference letter, uploaded through Academic Jobs Online by October 12? I attach the draft research statement, career statement and a one-page brief. Nothing changes in the lab before [July 2027], and if this happens I would like to plan the transition so it is useful to the group. I would also be grateful for a copy of my appointment letter, since the program counts prior postdoctoral experience to the start date.

Thank you,
Yi

## 7. To the School of Graduate Studies (or MIE graduate office) — send today, if not already sent for the CPRA

**Subject:** Letter confirming dates of PhD completion and conferral — for postdoctoral fellowship applications

Dear [name / Graduate Awards Office],

I completed my PhD in Information Engineering (Department of [MIE]) in 2025 and am applying to several postdoctoral fellowships whose eligibility windows are measured from the doctorate. Could you please issue a letter on institutional letterhead confirming (a) the date on which all requirements for my PhD were completed, [date — final thesis submission], and (b) the conferral date, and advise whether the official transcript I have ordered from the Office of the Registrar will itself show both dates? A PDF by [date, two weeks from now] would be ideal. My student number is [number].

Thank you very much.

Yi Ru

## 8. To each referee — send once the host is confirmed and the draft is final (target 2 Oct)

**Subject:** Reference for the Stanford Science Fellows program — by October 12

Dear [name],

Thank you for agreeing to write for me. The final research statement, career statement and CV are attached, together with a one-page brief on what the fellowship is and what reviewers weigh. My proposed faculty host is [name, department].

The upload link will come from Academic Jobs Online once I enter your name. The application closes October 16 at 11:59 pm Eastern; the program accepts letters after that date but says reviewers need not read them, so I have asked for letters by October 12. Please tell me if the timing is difficult and I will adjust.

With thanks,
Yi Ru
