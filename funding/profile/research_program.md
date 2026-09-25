# Research program — "Verified mereological ontologies for object–part representation in physical AI"

Distilled from the CPRA outline references, the Vector research statement, the DSI proposal and the CIRTA brief. This is the applicant's own program, complementary to but distinct from Prof. Grüninger's NSERC programs ("Ontologies for the Physical Turing Test"; "Commonsense Cobotics").

## Problem
Robot-learning datasets (PartNet, PartNet-Mobility, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment, DROID) annotate objects as hierarchies of parts with kinematic, functional and visual labels. Each dataset defines "part" operationally; no dataset or learned model is required to satisfy the axioms of parthood; there is no principled way to map labels across datasets; pooled training silently mixes incompatible part vocabularies. Consequences (poor transfer across part vocabularies, brittle generalization to new object categories) are observed but have never been measured, because there has been no formal specification to measure against.

## Objectives
- O1 — Ontology as specification. Axiomatize and verify a modular first-order ontology of physical object parts (rigid, articulated, functional, assembly) as an extension of TUpper (ISO/IEC 21838-4) integrated with the Process Specification Language (PSL) for state change under manipulation. Verification: consistency, non-triviality, module relationships, representation theorems (Prover9 / Mace4; COLORE methodology). Theory base: material constitution as a parthood-preserving mapping between mereologies; mereological pluralism (two Synthese submissions).
- O2 — Ontology as audit. A two-tier pipeline (Datalog/SMT for bulk; first-order theorem proving for residual hard cases) translates annotation hierarchies into ontology instances and checks them. Output: the first quantitative measurement of parthood consistency in robot datasets; corrected annotations; provably meaning-preserving cross-dataset label mappings; a merged, ontology-aligned corpus; a reusable audit toolkit (applicable to medical image part labels, CAD assemblies, BIM).
- O3 — Ontology as inductive bias. Training methods that use the ontology to shape part-aware manipulation policies: differentiable relaxations of parthood constraints as auxiliary losses; constraint-guided data augmentation for underrepresented categories; verification-in-the-loop evaluation reporting ontology-violation rate alongside task success. Hypotheses: ontology-consistent training improves generalization to unseen PartNet-Mobility categories; violation rate predicts task failure; pooled ontology-aligned data transfers across part vocabularies. Experiments in SAPIEN [+ second simulator], ablations by axiom family.

## Deliverables
Verified parts ontology (open licence; contributed to COLORE and ISO/IEC JTC 1/SC 42); first quantitative audit of parthood consistency in robot datasets with public release; merged ontology-aligned corpus; audit toolkit; two ML-venue papers and one robotics-venue paper (24-month plan) or an audit/data paper plus a methods paper (12-month plan).

## Timeline templates
- 24 months: M1–8 ontology + verification + audit pipeline + first audit; M6–16 data release, pooled-data experiments, augmentation; M12–24 constraint-based training, verification-in-the-loop evaluation, papers.
- 12 months: M1–4 ontology + schema mappings; M4–8 audit pipeline + results across five datasets + release; M8–12 pooling and policy experiments, methods paper, toolkit.

## Why Toronto / why this environment
Verified-ontology methodology with tool support exists only in the Semantic Technologies Laboratory (MIE, U of T); U of T Robotics Institute and Vector Institute supply the robotics community and compute; the applicant has done both formal theory and production data integration.

## Keywords
formal ontology; mereology; knowledge representation; automated theorem proving; physical AI; robot manipulation; articulated objects; dataset alignment; neuro-symbolic learning; ISO/IEC 21838; data quality; data provenance; verification.

## Adjacent framings (for non-KR funders)
- Data science / data quality: specification-based auditing of hierarchical annotations.
- AI safety / assurance / trustworthy AI: machine-checkable evidence for training data; provable consistency; interpretable failure signals for policies; compliance with EU AI Act Annex I (robots, from 2 Aug 2028), NIST AI RMF.
- Manufacturing / digital twins / standards: TUpper/ISO lineage; product lifecycle; CAD assemblies.
- Biomedical (Harvard context): ontology-driven integration of heterogeneous data; part-labels in medical imaging; the audit toolkit generalizes.
- Robotics: cross-embodiment schema; part-aware manipulation; benchmark quality.
