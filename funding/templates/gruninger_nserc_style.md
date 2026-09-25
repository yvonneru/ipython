# Template digest — Prof. Michael Grüninger's NSERC Discovery Grant proposal style

Derived from "Ontologies for the Physical Turing Test" and "Commonsense Cobotics" (5 pages each, NSERC PIN header, numbered references). Use this structure for any research proposal unless the funder prescribes its own headings; when the funder prescribes headings, map these sections onto them.

## Structure (5 pages, 12 pt, tight)
1. Recent Progress — one-line definition of the field ("An ontology is a computer-interpretable specification..."), then 3–4 bulleted bodies of prior work, each a bold-led paragraph with citations, closing with concrete artifacts (repositories, standards, awards). Establishes credibility and the tools that will be reused.
2. Objectives — a paragraph of motivation ending in a long-term vision or challenge, set off in italics as a single sentence ("Given a set of verbal instructions, together with a sequence of annotated images, answer questions about..."). Then "the proposed research program has N primary objectives:" as a bulleted/numbered list, each one sentence. Objectives are clustered around named themes.
3. Literature Review — short (half a page); names the specific gaps: limited expressiveness, unintended models, lack of integration, datasets without formal semantics, no prior ontological analysis.
4. Methodology — opens with the methodology lineage ("designed using my widely accepted ontology lifecycle methodology from [17]"), the verification standard ("characterize the models of an ontology up to isomorphism..."), and how competency questions come from the application. Then Themes (2–3), each with an italic problem statement, then Projects (x.1, x.2, x.3), each with a short method paragraph and a bulleted list of "Open Research Questions" tagged with the HQP who will own them (PhD1, MASc2...). Every question is a yes/no or "which/what" question that can be answered by a theorem or a counter-model.
5. Impact — two paragraphs: (a) near-term applied impact (manufacturing, benchmark quality, hallucination reduction) and HQP outcomes; (b) long-term open knowledge network / COLORE / testbeds.

## Voice and conventions
- Declarative, first-person singular for prior work ("My research has focussed on..."), plural for the program ("we will specify...").
- Every claim about ontologies is stated in terms of models, axioms, entailment, definability, verification; avoid marketing language.
- Datasets and benchmarks are named explicitly (Visual Genome, NLVR, ShapeNet, PartNet, Folio, PIQA...).
- Cite by number; keep a separate bibliography page.
- HQP training is explicit: each open research question is assigned to a named trainee slot.
- Distinguish verification (models of the axioms vs intended models) from validation (are the intended models the right ones).

## Mapping to the applicant's program
- Recent Progress → TUpper/ISO 21838-4 contribution; material-constitution and mereological-pluralism theory (Synthese submissions); knowledge-system architecture thesis; production deployments; AXIOMALITY kernel.
- Objectives → O1 specification, O2 audit, O3 inductive bias; long-term challenge: "Can the part-level representations that robot-learning systems learn be shown to satisfy the axioms of parthood that humans use, and does enforcing those axioms improve generalization?"
- Themes → Theme 1 Parts (O1), Theme 2 Audit (O2), Theme 3 Learning (O3). Open research questions per project, tagged PhD/MASc/undergrad where the funder cares about HQP; tagged "Y1/Y2 milestone" for fellowships.
- Impact → dataset quality for physical AI; EU AI Act Annex I evidence; COLORE and SC 42 contributions; AXIOMALITY commercialization path (only where the funder rewards commercialization).
