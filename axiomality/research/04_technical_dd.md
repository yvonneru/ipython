# AXIOMALITY — Technical Due Diligence (Formal Methods / KR / Robot Learning)

Date: 2026-09-25. Reviewer role: technical DD, formal methods + knowledge representation + robot learning.

Method note. Web search and page fetches were rate- and egress-limited in this session (arXiv, Semantic Scholar, ISO/IEC webstores, NIST PDF host, and most academic mirrors were blocked). Where I could not open a primary source I say so explicitly. I was able to shallow-clone the public COLORE repository (the source of TUpper's axioms) and inspect it directly, which is the strongest evidence in this memo. "Verified" below means I saw a primary or near-primary source; "search-snippet" means I saw only a search engine excerpt; "unverified" means neither.

---

## A. Verification of public facts

### A1. ISO/IEC 21838-4:2023 (TUpper) — VERIFIED, with caveats on "35 items"

- The standard exists: *ISO/IEC 21838-4:2023 Information technology — Top-level ontologies (TLO) — Part 4: TUpper*, ISO catalogue page https://www.iso.org/standard/78928.html; IEC webstore https://webstore.iec.ch/en/publication/88945. Developed in ISO/IEC JTC 1/SC 32 (Data management and interchange) per https://www.iso.org/committee/45342/x/catalogue/ and the ISO/IEC 21838 overview https://en.wikipedia.org/wiki/ISO/IEC_21838.
- The 21838 series is: Part 1 (requirements), Part 2 (BFO), Part 3 (DOLCE), Part 4 (TUpper). So the claim "one of three internationally recognised top-level ontologies alongside BFO and DOLCE" is **accurate in the narrow sense of "the three TLOs that have ISO/IEC 21838 parts"**. It is not a statement about adoption: BFO has orders of magnitude more users (OBO Foundry, IOF); DOLCE is widely used in robotics (KnowRob/SOMA use DOLCE's DUL). TUpper's adoption outside the Toronto group is thin.
- Provenance: TUpper was written by Michael Grüninger's group (Semantic Technologies Laboratory, Dept. of Mechanical & Industrial Engineering, University of Toronto). Journal description: Grüninger, Ru, Thai, "TUpper: A top level ontology within standards", *Applied Ontology* 17(1):143–165, 2022, https://journals.sagepub.com/doi/abs/10.3233/AO-220263. The public CLIF source `ontologies/tupper/tupper.clif` in COLORE carries "Copyright (c) University of Toronto … Contributors: Michael Gruninger — initial implementation" and the licence **CC BY-SA 4.0** (https://github.com/gruninger/colore/tree/master/ontologies/tupper). I could not find any public listing of ISO project editors or contributors for Part 4 (ISO does not publish them), so "team participated in drafting" and "responsible for 22 of 35 items" are **unverifiable from public sources**. The only named contributor in the public axiom files is Grüninger; the Applied Ontology paper has two additional co-authors (Yi Ru, Jona Thai).
- Structure (verified by cloning https://github.com/gruninger/colore): `tupper.clif` imports four root modules — `psl_disc_state/disc_state`, `psl_actocc/actocc`, `occupy/occupy_root`, `fount/fount`. Following `cl-imports` transitively pulls in **94 CLIF files across roughly 30 COLORE hierarchies**: PSL core / occurrence trees / discrete states / activity occurrences / durations (process), mereology and mereotopology, multidimensional mereotopology (CODI), timepoints, mass / length / area / volume / density / velocity (physical quantities), shape and shape features, matter and constitution, box-world/card-world (spatial toy worlds), plus algebraic hierarchies (vector spaces, fields, groups, lattices). The accompanying `TUpper-Terms.html` groups terms into three sections ("PSL Modules", "Spatial Modules", "FOUnt Modules") and lists roughly 58 distinct terms. A rough count gives ~3,300 sentences in the closure. **Nothing in the public sources maps to "35 items"**; the number could be a clause count in the ISO document (which I could not open) or an internal count. Treat "22 of 35" as an interview question, not a fact.
- Relation to PSL and COLORE: ISO's abstract states TUpper "contains modules from the ontologies within existing international standards" and "extends PSL [ISO 18629] with modules for physical objects, location, and units of measure" (ISO page above; StandICT summary https://standict.eu/standards-repository/isoiec-dis-21838-4-information-technology-top-level-ontologies-tlo-part-4). COLORE (Common Logic Ontology Repository) is the Toronto lab's repository of first-order ontologies in CLIF, described at https://ontologforum.org/index.php/COLORE and https://ceur-ws.org/Vol-2050/FOUST_paper_2.pdf ("Upper Ontologies in COLORE"); the DOL papers cite it as ">500 Common Logic ontologies" (https://arxiv.org/pdf/1208.0293). My clone shows 190 ontology directories and a `verification/` tree containing **756 Prover9/Mace4 `.in` files, 189 `.model` and 99 `.proof` files**, last commit 2024-12-12. This confirms the lab's stated methodology (consistency via Mace4 finite models, entailment via Prover9 proofs) is real and long-standing.
- IOF alignment: COLORE has an `iof` directory; IOF Core itself is BFO-based. "Aligned with BFO, DOLCE, IOF" is plausible for TUpper's mathematical modules (COLORE has `dolce_*` modules and a documented DOLCE–PSL merge, https://ceur-ws.org/Vol-3249/paper1-FOUST.pdf context) but I found no published TUpper↔BFO alignment artefact.

### A2. NIST IR 8530 — EXISTS; the specific claim is UNVERIFIED

NIST IR 8530 is *"A unified model of core metrological concepts"* by D. Flater, D. Foxvog and R. Kacker, 2024, https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8530.pdf (search-snippet; PDF host blocked). It is a metrology concept model that "software documentation, ontologies, and vocabulary standards can reference". Given that TUpper has units-of-measure and physical-quantity modules and the NIST authors work on measurement ontologies, a mention of TUpper as one of several formal ontologies is plausible, but I could not confirm the phrase "representative formal ontology". Ask the company for the page citation.

### A3. FOIS and the "outstanding paper" award — PARTLY VERIFIED

FOIS (Formal Ontology in Information Systems) is the flagship conference of the IAOA; it awards an IOS-Press-sponsored **Best Paper Award** (e.g., FOIS 2018, 2020, 2021, 2023 winners listed at http://fois2018.cs.uct.ac.za/, https://www.inf.unibz.it/~ntroquard/MISC/FOIS2021_best_paper_award.pdf, https://ebooks.iospress.nl/doi/10.3233/FAIA377). I found no award literally named "outstanding paper", and none of the winners I saw were Toronto papers. Ask for the year and paper title; it is a two-minute check against dblp (https://dblp.org/db/conf/fois/index.html). "21 papers", "one English monograph", "invited AAAI talk" and "University of Toronto AI PhD" are checkable once a name is provided; I did not attempt to identify the founder from indirect clues.

### A4. ISO/IEC 24707 Common Logic — VERIFIED

ISO/IEC 24707:2018 (second edition, replaces 2007) specifies Common Logic with the CLIF, CGIF and XCL dialects; first-order model theory with signature-free syntax (https://www.iso.org/standard/66249.html, https://en.wikipedia.org/wiki/Common_Logic). Grüninger's GitHub hosts a `Common-Logic` repository of "Documents for the developments of ISO 24707 Edition 2" (https://github.com/gruninger/Common-Logic), consistent with editorial involvement of the Toronto group in the CL standard. Writing all axioms in CL is therefore natural for this lineage; it is also why the toolchain is Prover9/Mace4 (COLORE has CLIF→Prover9 conversions).

### A5. Prover9 / Mace4 status — VERIFIED (mixed)

- Original development by W. McCune ended in 2009 (LADR-2009-11A; https://www.cs.unm.edu/~mccune/prover9/, https://en.wikipedia.org/wiki/Prover9). The `laitep/ladr` repository preserves LADR-2009-11A as "v1.0.0" (release dated 2024-10-31; https://github.com/laitep/ladr/releases). The `ai4reason/Prover9` mirror is based on LADR-2017-11A (https://github.com/ai4reason/Prover9).
- A search-snippet from https://prover9.org/ states that in March 2026 J. P. Machado and L. Lesyna released "LADR-2026", backward compatible with LADR-2009. I could not open the page; treat as likely but unconfirmed.
- Credibility: Prover9/Mace4 remain standard in the ontology-verification community (COLORE is built on them), and Mace4's finite-model finding is the right tool for "this module is consistent" (any finite model is a proof of consistency). But for scale and speed, modern provers dominate: Garbacz (JOWO 2022, https://ceur-ws.org/Vol-3249/paper1-FOUST.pdf) checked BFO/DOLCE subtheories with Vampire and notes Vampire is "usually, but not always, faster than Prover9". A serious 2026 stack should also run Vampire/E (CASC winners) and, for ground checks, Z3/cvc5. Using Prover9/Mace4 alone is a credibility yellow flag, not a red one.

### A6. Specula, arXiv 2607.25333 — VERIFIED, but the analogy is loose

*"Specula: Scaling formal specifications for autonomous model checking of system code"*, Cheng, Pial, Tang, Su, Ma, Hackett, Beschastnikh, Huang, Xu; Microsoft Research and university co-authors; submitted 2026-07-28, v2 2026-08-03 (https://arxiv.org/abs/2607.25333; https://www.microsoft.com/en-us/research/publication/specula-scaling-formal-specifications-for-autonomous-model-checking-of-system-code/; code https://github.com/specula-org/Specula, Apache-2.0). It uses LLM coding agents to write **TLA+** specifications and invariants, checks them with **TLC**, confirms bugs against real code, and reports 249 bugs in 48 projects. It has nothing to do with ontologies, Common Logic or Prover9. The valid takeaway for AXIOMALITY is only the pattern: LLM proposes formal artefacts, a mechanical checker validates, a loop repairs. That pattern is now common (autoformalisation with Lean, LLM-generated STL/LTL monitors, etc.), so citing Specula signals awareness, not differentiation.

### A7. Safety standards — VERIFIED

ISO 10218-1/-2:2025 were published in 2025 and fold ISO/TS 15066 collaborative requirements into the base standard (https://www.iso.org/standard/73933.html; https://www.automate.org/robotics/blogs/updated-iso-10218-faq). ISO 13482 (service/personal-care robots) is under revision at FDIS stage (https://www.iso.org/standard/83498.html). I found **no public machine-readable formalisation** of either standard; any "ISO 13482 constraint set" is the company's own interpretation and cannot carry the standard's authority. A Passport field "ISO 13482 constraint set: 0 violations" is a claim about the company's encoding, not conformity.

---

## B. State of the art and prior art

### B1. Ontologies for robot experience
- **KnowRob / SOMA (Bremen, CRC EASE)**: KnowRob is a hybrid knowledge base for robots (OWL + Prolog, ensemble of reasoners; https://github.com/knowrob/knowrob, BSD-3). SOMA is an OWL ontology on top of DOLCE+DnS Ultralite (DUL) covering activities, motions, contact and agent–environment interaction (https://github.com/ease-crc/soma; "Foundations of SOMA" https://ai.uni-bremen.de/papers/bessler21soma.pdf). The EASE project's NEEMs (narrative-enabled episodic memories) are exactly "robot episodes annotated against a foundational ontology" and have existed for years. AXIOMALITY's domain layer (embodiment, affordances, contact events, task phases) overlaps heavily with SOMA; the difference is TUpper/PSL (first-order, CL) versus DUL (OWL, description logic).
- Other robotics ontologies: IEEE 1872 (CORA), a recent modular ontology for robotic orchestration (https://ceur-ws.org/Vol-4169/paper7.pdf).

### B2. Scene-graph grounding with VLMs
ConceptGraphs (ICRA 2024; Grounded-SAM + CLIP + LLaVA + GPT-4; https://github.com/concept-graphs/concept-graphs, MIT, ~960 stars), Open3DSG (https://arxiv.org/pdf/2402.12259), hierarchical open-vocabulary 3D scene graphs (RSS 2024, https://www.roboticsproceedings.org/rss20/p077.pdf), Event-Grounding Graph — a unified spatio-temporal scene graph from robot observations (https://arxiv.org/pdf/2510.18697), MomaGraph state-aware scene graphs for task planning (https://arxiv.org/pdf/2512.16909). "VLM + graph proposes objects/relations/events per frame" is commodity in 2026.

### B3. VLM auto-labelling of robot datasets
ECoT auto-labelled all of Bridge v2 (2.5M transitions) with Prismatic-7B, Grounding DINO, OWL-v2, SAM and Gemini (https://embodied-cot.github.io/, https://arxiv.org/pdf/2407.08693; follow-ups https://arxiv.org/pdf/2606.03784, https://arxiv.org/html/2606.30552). Xiaomi-Robotics-1 uses a hierarchical Qwen3-VL / InternVL annotation pipeline over 100K hours (https://arxiv.org/pdf/2607.15330). Gemini-based labelling of subtasks with manual spot checks is standard practice at DeepMind-scale labs. So the labelling step is not novel; **the audit of labels** is the open problem.

### B4. Physics / quality checks on trajectories
- **VISTA** (https://arxiv.org/pdf/2606.04708): trajectory-level validation for UMI data scoring continuity, self-collision risk and execution fidelity — i.e., kinematic plausibility without torque.
- **lerobot-doctor** (https://github.com/FilippoGorini/lerobot-doctor, fork of jashshah999): 12 structural checks (timestamps, dropped frames, NaN/clipping, frozen actuators, video decode, URDF joint limits). No semantic or dynamics checks.
- "Auditing Instruction-Trajectory Mismatches in Multimodal Robot Demonstrations" (https://arxiv.org/pdf/2608.07895), "An Efficient Metric for Data Quality Measurement in Imitation Learning" (https://arxiv.org/pdf/2605.01544), "Geometry Guided Self-Consistency for Physical AI" (https://arxiv.org/pdf/2605.08638), and physics-generated hybrid curation (https://www.mdpi.com/2076-3417/16/6/2968) show the community converging on "check the data" in 2025–26.
- **No Free Checker: A Survey of Verifiers for Robot Policies** (https://arxiv.org/pdf/2609.09250; reading list https://github.com/ZJUSCL/Awesome-Robot-Verifier) organises 153 papers: human, rule-based/formal (STL, CBFs, reachability, TAMP feasibility, LLM-written monitors), learned verifiers (reward models, success detectors, data-curation scorers), and model-intrinsic verifiers (uncertainty, ensembles), plus conformal calibration under distribution shift. **Dataset-level certification and ontology-checked scene graphs do not appear as categories** — supporting the claim that the specific combination is not yet occupied in the literature.

### B5. Neuro-symbolic constraints
LTN (AIJ 2022, https://www.sciencedirect.com/science/article/abs/pii/S0004370221002009), DeepProbLog, semantic loss, t-norm losses (https://arxiv.org/pdf/1907.11468). Directly relevant negative results: **reasoning shortcuts** — models satisfy logical losses while learning wrong concepts (https://arxiv.org/pdf/2604.23377, https://arxiv.org/pdf/2510.14538). Zero-shot conditioning of diffusion models by neuro-symbolic constraints (https://arxiv.org/pdf/2308.16534) is prior art for "axioms as composable energy terms in diffusion policies".

### B6. Conformal prediction in robotics
KnowNo (CoRL 2023; https://arxiv.org/abs/2307.01928) and Introspective Planning (https://arxiv.org/pdf/2402.06529). Coverage guarantees are marginal and assume exchangeability; the No-Free-Checker survey has a dedicated section on conformal calibration under covariate shift.

### B7. Runtime monitoring / guardrails
3Laws Robotics (CBF safety filters, https://www.crunchbase.com/organization/3laws-robotics); **RoboGuard** (root-of-trust LLM turns rules + semantic graph into LTL, plans checked by synthesis with SPOT; https://github.com/KumarRobotics/RoboGuard, arXiv 2503.07885) — this is essentially "semantic guardrails compiled from a knowledge graph" and is the closest prior art to AXIOMALITY's guardrail product; RTAMT online STL monitors with ROS (https://arxiv.org/pdf/2005.11827), mstlo Rust STL monitor (https://arxiv.org/pdf/2605.26847); "Silent Failures in Physical AI" literature review of runtime action authorisation (https://arxiv.org/pdf/2606.00090).

### B8. Data formats and provenance
LeRobot v3 (Oct 2025; chunked parquet + mp4, streaming; 54.6% of Hub datasets by late 2025; https://huggingface.co/blog/lerobot-datasets-v3, https://github.com/huggingface/lerobot/blob/main/docs/source/porting_datasets_v3.mdx) has no built-in validation. RLDS/Open X-Embodiment (60 datasets, 22 embodiments, >1M trajectories; https://github.com/google-deepmind/open_x_embodiment) likewise. Croissant (MLCommons metadata, https://github.com/mlcommons/croissant) has no signing/certification. Sigstore **model-transparency** signs a manifest of file hashes for ML models with transparency-log verification (https://github.com/sigstore/model-transparency); C2PA binds content hashes to signed assertions for media (https://github.com/contentauth/c2pa-rs). A "Passport" = signed manifest (hash + kernel version + check results) is a straightforward composition of these; **offline verification with a public key is standard practice, not an invention.**

### B9. Is anyone doing the full combination?
I found no public company or paper doing "ontology-checked scene graphs + physics residuals + signed certificates" for robot datasets (GitHub searches for those combinations returned zero repositories; the verifier survey has no such category). Each component has mature prior art. The combination and the packaging (Passport) are the novelty; the science inside is mostly integration.

### B10. Is "one kernel, two products" technically sound?
Partly. The same CL axioms can be (i) grounded over a finite scene graph into quantifier-free/EPR SMT problems for offline checks and runtime monitors, and (ii) relaxed via t-norms into differentiable losses (exactly what LTN does). But the three compiled forms are **not semantically equivalent**: fuzzy relaxation is neither sound nor complete w.r.t. first-order entailment; runtime guardrails need a latency-bounded propositional/STL subset; offline checks can afford Mace4/Vampire. "Same axiom set" is true only at source level, and the two products stress different subsets (safety/geometry vs. semantic typing). It is a good engineering story; it is not a theorem.

---

## C. Technical risk assessment

| # | Risk | Severity | Why | De-risking evidence |
|---|------|----------|-----|---------------------|
| 1 | **Grounding accuracy**: a scene graph can be logically consistent and factually wrong. Axioms only reject *contradictions*; a VLM that consistently mislabels "mug" as "cup" or hallucinates a plausible relation passes every check. | **High** | Consistency ≠ truth. The 97%/96.4% "coverage" numbers say how many frames got a consistent label, not how many are correct. Without an independent signal (multi-view geometry, depth, tracking, human audit) hallucinations are unbounded. | Blind human-audited precision/recall on a held-out set with **injected** label errors; per-class confusion; disagreement rate between two VLMs; report *factual* accuracy, not consistency rate. |
| 2 | **Decidability/scalability of SMT over first-order axioms**. Full TUpper closure (~3,300 sentences with functions, orderings, arithmetic over quantities) is undecidable in general; Z3's E-matching is "inherently incomplete", MBQI is a decision procedure only for fragments such as EPR/Bernays–Schönfinkel (https://microsoft.github.io/z3guide/docs/logic/Quantifiers). | **Medium** | Manageable *if* per-frame checks are ground/EPR over a bounded scene graph; then it is fast and decidable. The risk is what is dropped to get there (function symbols, dense time, units arithmetic) and whether "unknown" results are silently treated as "pass". | Publish the fragment used per check; latency histograms per frame; count of `unknown`/timeout verdicts and how they are handled. |
| 3 | **"Machine-proven consistent" gives no domain-level correctness**. Mace4 finding a finite model proves the *top-level* theory has *some* model; it says nothing about whether the robotics domain axioms (affordances, contact events, ISO 13482 encoding) are correct, complete, or even consistent with the data. | **Medium** | The rare asset (verified TLO) sits at the layer furthest from the product's value. Domain modules are new, unverified, and unlike mereology have no representation theorems. | Show Prover9/Mace4 (or Vampire) artefacts for the *domain* modules; competency questions with proofs; conservative-extension checks of domain over TUpper. |
| 4 | **Physics residual needs τ and contact wrench f**. DROID's RLDS release exposes `cartesian_position`, `joint_positions`, `joint_velocities`, `gripper_position` — no torque/effort keys appear in the policy-learning code (verified by grep of https://github.com/droid-dataset/droid_policy_learning). LeRobot SO-100/ALOHA-style datasets are position-only. | **High** | Without τ and f the "dynamics residual" collapses to kinematic smoothness + joint limits (what VISTA and lerobot-doctor already do). PINN/FNO surrogates need per-embodiment identification data. "99.1% physics pass" is then a kinematics number dressed as dynamics. | Demonstrate on a torque-logged dataset (Franka raw HDF5, Kuka iiwa) with injected dynamic errors; state which datasets get "kinematic-only" vs "dynamic" passports. |
| 5 | **Conformal coverage is population-level**. Coverage ≥ 1−α holds marginally over an exchangeable calibration set; a Passport's "conformal coverage 0.94" is not a per-trajectory guarantee and breaks under embodiment/scene shift. | **Medium** | Buyers will read 0.94 as per-episode reliability. Cross-embodiment reuse is exactly the covariate-shift case where exchangeability fails. | Report group-conditional coverage by robot/scene; shift tests; stop putting a single coverage number on the certificate without the calibration population. |
| 6 | **Cost decline ¥430→¥85/h**. Drivers that *do* fall with kernel coverage: axiom authoring (amortised), human adjudication of contradictions (fewer novel cases), cached VLM outputs. Drivers that *don't*: VLM inference per frame, SMT/prover time (grows with axioms), and the long tail of novel scenes. | **Medium** | The curve is a hypothesis; a 5× fall implies human review currently dominates cost. Also ¥35/h augmentation marginal cost is a GPU-hours number that ignores re-verification. | Unit-economics breakdown per hour: VLM tokens, GPU, prover CPU, human minutes; show the curve on real batches over time. |
| 7 | **Augmentation shares blind spots with the checker**. Variants generated under the same kernel and re-verified by the same engine cannot reveal errors the kernel does not encode; they can amplify systematic label bias. | **Medium** | Classic self-verification loop. | Held-out human evaluation of augmented episodes; downstream policy success with/without augmentation. |
| 8 | **Buyer acceptance**. PI, Figure, NVIDIA and DeepMind run in-house curation (ECoT-style pipelines, Cosmos-Curate https://github.com/nvidia-cosmos/cosmos-curate, manual spot checks) and are unlikely to outsource trust; a third-party certificate is more valuable to *sellers* (data vendors, AgiBot-style collectors) and *insurers/regulators* than to frontier labs. | **High (commercial)** | The "passport" model works where there is an information asymmetry between data seller and buyer — that is the data-marketplace layer, not the frontier labs named in the deck. | LOIs from data vendors or a lab's data-procurement team; evidence a buyer changed a purchase decision on a Passport. |
| 9 | **Simpler baselines likely match**. lerobot-doctor + URDF + a VLM judge + a few hundred hand-written rules will catch most gross errors at a fraction of the complexity. | **High** | Unless the ontology catches errors rules cannot (cross-frame temporal contradictions, part-whole violations, occurrence-tree inconsistencies), the formal layer is cost without benefit. | Head-to-head benchmark on injected errors (Demo 1 below) with a rules+VLM baseline; show error classes only the axioms catch. |
| 10 | **Runtime guardrail latency**. RoboGuard-style LTL checking with a root-of-trust LLM is seconds, not milliseconds; SMT with quantifiers is not real-time. p95/p99 targets are achievable only for a precompiled propositional/STL subset. | **Low–Medium** | Company already gates this separately, which is sensible. | Latency histograms on a real control loop; false-block rate on benign plans (RoboGuard reports this style of metric). |

Additional diligence item — **IP/licence**: TUpper's CLIF source is CC BY-SA 4.0, copyright University of Toronto. A proprietary "kernel" that is a derivative of those files may carry share-alike obligations if distributed (SaaS use is arguably not distribution, but Passport specs that embed axioms are). Confirm the licensing position and any university IP agreement.

---

## D. Scientific-merit verdict

**Verdict: engineering of known parts with one genuinely rare ingredient.**

Genuinely rare:
- Deep, verified, first-order top-level-ontology expertise in the TUpper/PSL/COLORE lineage, with an existing culture of machine-checked consistency (756 Prover9/Mace4 problem files in the public repo). Very few people in the world can write and verify Common Logic axiomatisations of process, mereotopology and physical quantities. Applying that to robot data is unusual.
- Representation theorems (reducibility/amalgamation; https://dl.acm.org/doi/10.1145/3565364, https://ceur-ws.org/Vol-1248/WoMO14-Paper3.pdf) are real results from this group, so "modules merge structure-preservingly" is defensible for the mathematical modules.

Commodity:
- VLM/graph scene proposals, VLM auto-labelling, kinematic checks, LTN-style logic losses, conformal wrappers, STL/LTL runtime monitors, signed manifests. Each has open-source prior art from 2023–26.

Unproven / research-direction:
- Axioms as composable energy terms in diffusion world models (prior art exists for constraint-guided diffusion; no evidence here).
- LLM-proposed axioms checked by provers for the robotics domain (pattern is known; value depends on the domain modules that do not yet exist publicly).

Publishable: a benchmark paper on detecting injected semantic/physical errors with formal + learned checkers; a verified robotics domain ontology over TUpper with competency questions. Defensible: weakly — the moat is expertise and accumulated verified domain axioms, not a patentable mechanism; the ontology base is CC BY-SA.

### Three demos that would convince a technical VC
1. **Blind injected-error benchmark.** Take 200 episodes from DROID and 200 from LeRobot v3 community datasets; inject controlled errors (wrong object label, impossible relation, reversed event order, teleported object, 3-frame time warp, joint-limit violation, gripper-state/contact mismatch). Run (a) lerobot-doctor + hand rules, (b) a VLM judge alone, (c) AXIOMALITY's engine. Report precision/recall per error class, cost per hour, and — critically — which error classes only (c) catches. Have a third party hold the injection key.
2. **Cross-embodiment reuse with downstream lift.** Build the kernel-checked labels on Franka (DROID), then apply the *unchanged* kernel to SO-100 and a humanoid dataset; report fraction of axioms/checks reused without edits, human agreement of labels, and — the number that matters — success rate of a policy (π0-class or ACT) trained on Passport-filtered vs. unfiltered data, matched for hours.
3. **Public verifier + sample Passport.** Publish the Passport spec, a public key, a CLI verifier, and a Passport for one open dataset. Invite tampering (flip a frame, edit a label, re-encode a video) and show the verifier fails; show that a third party can recompute the coverage/physics numbers from the spec. This converts "trust us" into "check us" and is the single strongest de-risking artefact for the certificate business.

---

## E. Presenting the science on two VC slides

**Slide 1 — "What we check, and why a rulebook isn't enough"**
- Keep: one picture of a robot episode with three overlaid checks — *does the story make sense* (objects, parts, events consistent across frames), *is the motion physically possible* (smoothness, limits, contact), *is it safe by the standard's rules*. One sentence: "We turned the ISO top-level ontology our team helped write into a machine-checkable rulebook for robot data."
- Rename: "Common Logic axioms verified with Prover9/Mace4" → "a mathematically checked rulebook"; "scene graph + SMT" → "every frame is cross-examined for contradictions"; "physics residual" → "we recompute the physics and flag what doesn't add up"; "conformal coverage" → "calibrated confidence".
- Cut: Stone duality/Birkhoff, representation theorems, ISO clause numbers, "22 of 35", GraphRAG, t-norms, PINN/FNO.

**Slide 2 — "Evidence: the same rulebook, three uses, one benchmark"**
- Keep: one table — injected-error benchmark (rules+VLM vs. us), cost per hour, and downstream policy lift. One line on the Passport: "signed, offline-verifiable, anyone can re-check it". One line on guardrails: "same rulebook, precompiled for millisecond checks".
- Rename: "Passport" is fine; "runtime semantic guardrails" → "real-time safety check"; "feedback loop with LLM-proposed axioms" → "the rulebook learns new rules and proves them before use".
- Cut: Specula citation, ¥430→¥85 curve unless backed by a unit-economics table, and any coverage percentage without a denominator.

---

## Source list (primary or near-primary)
- ISO/IEC 21838-4:2023 — https://www.iso.org/standard/78928.html ; https://webstore.iec.ch/en/publication/88945 ; https://en.wikipedia.org/wiki/ISO/IEC_21838
- TUpper paper — https://journals.sagepub.com/doi/abs/10.3233/AO-220263
- COLORE repo (cloned; tupper.clif, verification/) — https://github.com/gruninger/colore ; https://ontologforum.org/index.php/COLORE ; https://ceur-ws.org/Vol-2050/FOUST_paper_2.pdf
- Representation theorems — https://dl.acm.org/doi/10.1145/3565364 ; https://ceur-ws.org/Vol-1248/WoMO14-Paper3.pdf
- Common Logic — https://www.iso.org/standard/66249.html ; https://github.com/gruninger/Common-Logic
- NIST IR 8530 — https://nvlpubs.nist.gov/nistpubs/ir/2024/NIST.IR.8530.pdf
- FOIS awards — http://fois2018.cs.uct.ac.za/ ; https://www.inf.unibz.it/~ntroquard/MISC/FOIS2021_best_paper_award.pdf ; https://ebooks.iospress.nl/doi/10.3233/FAIA377
- Prover9/Mace4 — https://www.cs.unm.edu/~mccune/prover9/ ; https://github.com/laitep/ladr/releases ; https://prover9.org/ ; Garbacz 2022 https://ceur-ws.org/Vol-3249/paper1-FOUST.pdf
- Specula — https://arxiv.org/abs/2607.25333 ; https://github.com/specula-org/Specula
- Z3 quantifiers — https://microsoft.github.io/z3guide/docs/logic/Quantifiers
- KnowRob/SOMA — https://github.com/knowrob/knowrob ; https://github.com/ease-crc/soma ; https://ai.uni-bremen.de/papers/bessler21soma.pdf
- ConceptGraphs — https://github.com/concept-graphs/concept-graphs ; Event-Grounding Graph https://arxiv.org/pdf/2510.18697
- ECoT — https://embodied-cot.github.io/ ; https://arxiv.org/pdf/2407.08693 ; Xiaomi-Robotics-1 https://arxiv.org/pdf/2607.15330
- VISTA — https://arxiv.org/pdf/2606.04708 ; lerobot-doctor — https://github.com/FilippoGorini/lerobot-doctor ; audit paper https://arxiv.org/pdf/2608.07895
- No Free Checker survey — https://arxiv.org/pdf/2609.09250 ; https://github.com/ZJUSCL/Awesome-Robot-Verifier
- LTN / reasoning shortcuts — https://www.sciencedirect.com/science/article/abs/pii/S0004370221002009 ; https://arxiv.org/pdf/2604.23377 ; diffusion constraints https://arxiv.org/pdf/2308.16534
- KnowNo — https://arxiv.org/abs/2307.01928
- RoboGuard — https://github.com/KumarRobotics/RoboGuard ; 3Laws — https://www.crunchbase.com/organization/3laws-robotics ; RTAMT https://arxiv.org/pdf/2005.11827 ; Silent Failures review https://arxiv.org/pdf/2606.00090
- LeRobot v3 — https://huggingface.co/blog/lerobot-datasets-v3 ; OXE/RLDS — https://github.com/google-deepmind/open_x_embodiment ; DROID code — https://github.com/droid-dataset/droid_policy_learning
- Provenance — https://github.com/sigstore/model-transparency ; https://github.com/contentauth/c2pa-rs ; https://github.com/mlcommons/croissant
- Safety standards — https://www.iso.org/standard/73933.html ; https://www.iso.org/standard/83498.html ; https://www.automate.org/robotics/blogs/updated-iso-10218-faq
