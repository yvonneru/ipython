# Dataset licences — ShapeNet, PartNet, PartNet-Mobility/SAPIEN, GAPartNet, PartNet-Ensembled, AgiBot World, Open X-Embodiment, DROID

Drafted 2026-09-25 for Dr. Yi Ru. Source of every licence statement: the registry record `dataset-access-licences-shapenet-partnet-partnet-mobility-sapien-gapar` (6981053de7aa), whose terms are "as best known, unverified", plus three web searches run by this drafting session on 2026-09-25 (marked "web search"). **The exact terms text must be re-read at registration time and saved as PDF**; everything below is a planning view, not legal advice. AXIOMALITY's counsel gives the company-side position [Q1 2027].

## 1. Licence table

| Dataset | Holder / where obtained | Licence as far as known | Who signs / registers | What matters for the academic program | What matters for AXIOMALITY |
|---|---|---|---|---|---|
| **ShapeNet** | Stanford / Princeton / TTIC · shapenet.org | Registration with institutional email; non-commercial research use; no redistribution [registry, unverified] | Dr. Ru, harvard.edu now; [re-register from utoronto.ca in 2027 if the terms bind use to the registering institution — confirm] | Base licence for PartNet, PartNet-Mobility and PartNet-Ensembled (all derived from ShapeNet) — so its no-redistribution clause reaches every derived corpus. Meshes are never re-hosted; [whether derived annotations may be published — confirm] | Excluded without a separate agreement. The registry's reading is that the Engine may be *validated* on it but nothing derived may be sold or redistributed; [counsel to confirm whether internal validation of a commercial product is itself "commercial use" under the terms] |
| **PartNet** | Stanford (Mo et al.) · partnet.cs.stanford.edu | Registration with institutional email; non-commercial; no redistribution [registry, unverified]; ShapeNet terms also apply | Dr. Ru, harvard.edu | Core O2 audit corpus (fine-grained part hierarchies). Release audit reports and label mappings; corrected-annotation diffs only if [derived annotations may be published — confirm] | Excluded without an agreement; a separate data agreement with Stanford is the route if commercial Passport use is ever needed [counsel, Q1 2027] |
| **PartNet-Mobility (SAPIEN)** | UC San Diego, Hao Su lab · sapien.ucsd.edu (SAPIEN account + terms); gated Hugging Face mirror `sapien-sim/PartNetMobility` (web search) | SAPIEN terms of use: "Researchers shall use the Database only for non-commercial research and educational purposes" and must also abide by the ShapeNet terms (web search, sapien.ucsd.edu; consistent with the registry). 2,347 articulated objects, 46 categories, URDF articulation annotations (web search) | Dr. Ru, with institutional email, as an individual researcher — explicitly not via AXIOMALITY (registry: ManiSkill record) | Core corpus for O2 and the O3 simulator assets (SAPIEN). [Whether corrected annotations may be redistributed — confirm; decisive for the ManiSkill maintainers proposal in applications.md §J] | Excluded; the O3 simulation assets therefore stay on the academic side, and the Engine's PartNet-Mobility validation cannot appear in commercial evidence packs without an agreement with UCSD [counsel] |
| **GAPartNet** | Peking University EPIC Lab · github.com/PKU-EPIC/GAPartNet (request form) | Code MIT on GitHub; dataset released after a request form, non-commercial [registry, unverified — the dataset licence is distinct from the code licence; confirm] | Dr. Ru via the request form, institutional email | Core O2 corpus (generalizable actionable parts). Same release policy as PartNet | Excluded without an agreement; Chinese-origin holder — [counsel: any cross-border data-agreement considerations] |
| **PartNet-Ensembled (PartNetE)** | Introduced by the PartSLIP paper (Liu et al., CVPR 2023, UCSD); assembled from PartNet and PartNet-Mobility (web search: arxiv 2212.01558; project page colin97.github.io/PartSLIP_page) | **Not found.** Neither the registry nor the web search located a licence; as a re-packaging of PartNet + PartNet-Mobility it presumably inherits the ShapeNet, PartNet and SAPIEN non-commercial terms [confirm with the authors]. [Hosting location — GitHub/Drive link on the project page — confirm] | Dr. Ru; email to the PartSLIP authors (§3.4) | Listed in research_program.md as an audit corpus; low marginal cost once PartNet and PartNet-Mobility are in hand, since its contents are drawn from them. [Counts unknown; the README estimate assumes PartNet-Mobility scale] | Excluded on the same basis as its sources |
| **AgiBot World** | AgiBot (Shanghai) · huggingface.co/agibot-world (gated) | CC BY-NC-SA 4.0 for the Alpha subset [registry, unverified]; Beta releases "far larger" — [licence of Beta not recorded; confirm on the dataset card] | Dr. Ru's Hugging Face account; gated-dataset acceptance (no approval step recorded) | Largest O2 corpus (episodes; sizes: Alpha [not recorded], Beta tens of TB). Share-alike: any published derived annotations must carry CC BY-NC-SA 4.0, and a merged corpus that includes AgiBot-derived material becomes NC-SA as a whole — keep AgiBot outputs in their own repository. [Teleoperation footage may show operators — the audit uses no frames; confirm no personal-data handling is triggered] | Excluded (NC). The registry names a separate data agreement with AgiBot as the route if commercial Passport use is needed [counsel, Q1 2027]. Cannot be mixed into any commercial evidence pack |
| **Open X-Embodiment (OXE)** | Google DeepMind and the OXE consortium · robotics-transformer-x.github.io; RLDS on Google Cloud Storage (~9 TB) | Per sub-dataset; mostly CC BY 4.0 / Apache-2.0 [registry, unverified]; [pull the sub-dataset licence table — some sub-datasets may carry NC or other terms] | Nobody — download without approval; attribution per sub-dataset | Audit corpus with sparse part labels; the CC BY / Apache sub-datasets are the only OXE material that may be re-hosted in a merged corpus (with attribution) | The commercially reusable subsets (with attribution) are, with DROID, the only candidates for Passport demonstrations without separate agreements [counsel to confirm per sub-dataset] |
| **DROID** | Stanford IRIS Lab and collaborators · droid-dataset.github.io; GCS and via LeRobot on Hugging Face (~1.7 TB RLDS; raw larger) | CC BY 4.0 (data), MIT (code) [registry, unverified] | Nobody — download without approval; attribution required | Audit corpus; re-hosting of derived subsets permitted with attribution; the natural first public audit target (LeRobot format available) | Commercial reuse permitted with attribution [confirm on the dataset page]; the first-choice Passport demonstration corpus |

## 2. What may be released, per dataset (planning matrix; every cell subject to the re-read terms)

| Output | ShapeNet / PartNet / PartNet-Mobility / GAPartNet / PartNet-Ensembled | AgiBot World | OXE (CC BY / Apache sub-datasets) | DROID |
|---|---|---|---|---|
| Raw data re-hosted | No (no redistribution) | No (NC-SA; re-hosting not planned) | Yes, with attribution [per sub-dataset] | Yes, with attribution |
| Ontology instance store (metadata only) | Internal to the allocation; not published | Internal | May be published | May be published |
| Audit reports (violation statistics, counter-model summaries) | Yes [confirm "derived work" wording does not bar statistics] | Yes, under CC BY-NC-SA 4.0 | Yes | Yes |
| Label mappings (vocabulary → ontology) | Yes [confirm] | Yes, CC BY-NC-SA 4.0 | Yes | Yes |
| Corrected-annotation diffs | [Only if derived annotations may be published — confirm per dataset; for PartNet-Mobility the ManiSkill maintainers' hosting is the preferred route] | Yes, CC BY-NC-SA 4.0 | Yes | Yes |
| Inclusion in the public merged ontology-aligned corpus | No | No (would make the corpus NC-SA) | Yes | Yes |
| Use in AXIOMALITY commercial evidence packs | No, without an agreement | No, without an agreement | Yes, with attribution [counsel] | Yes, with attribution [counsel] |
| Use for internal validation of the AXIOMALITY Engine | [Counsel: whether this is "commercial use"] | [Counsel] | Yes | Yes |

Consequence for the research program's deliverable "merged, ontology-aligned corpus": the public corpus is limited to the OXE CC BY / Apache sub-datasets and DROID; for the non-commercial datasets the deliverable is mappings, reports and (where permitted) diffs. State this in every proposal (applications.md §0.5).

## 3. Registration order and email domains

1. By 3 Oct 2026, with harvard.edu: shapenet.org → partnet.cs.stanford.edu → sapien.ucsd.edu (SAPIEN account; also request the gated Hugging Face mirror). Save each accepted terms text as PDF in the legal folder.
2. By 10 Oct 2026: GAPartNet request form; AgiBot World gated acceptance on Hugging Face (read the card for the Beta licence); pull the OXE sub-dataset licence table and the DROID licence; email the PartSLIP authors for PartNet-Ensembled.
3. 17 Oct 2026 (CPRA deadline): all registrations done so the proposal can state the corpora are in hand.
4. April 2027 or later: [if any terms bind use to the registering institution, re-register from the utoronto.ca staff address; alumni.utoronto.ca may be rejected]. Mirror the instance store to Alliance storage by 1 Mar 2027; raw corpora are re-downloaded in Toronto, not transferred.

## 4. Request texts

### 4.1 ShapeNet and PartNet — "intended use" field on the registration forms (≈100 words)

Academic research on the formal consistency of part annotations. I am a postdoctoral researcher at Harvard Medical School [laboratory] (PhD, University of Toronto, 2025; core contributor to ISO/IEC 21838-4) working with Prof. Michael Grüninger (University of Toronto) on a verified first-order ontology of physical object parts. I will translate the part hierarchies of [ShapeNet-derived PartNet / PartNet] into ontology instances and check them with SMT solvers and automated theorem provers, producing per-category consistency statistics and label mappings to other part vocabularies. Non-commercial research use only; no redistribution of meshes or annotations; results published as statistics, mappings and papers. Institutional email: [harvard.edu address].

### 4.2 SAPIEN / PartNet-Mobility — account request field, plus a terms question to the SAPIEN team

**Account "purpose" field (≈60 words):** Non-commercial academic research: auditing the part and articulation annotations of PartNet-Mobility against a verified first-order ontology of physical object parts, and using SAPIEN as the primary simulator for ontology-constrained manipulation-policy experiments. Postdoctoral researcher, Harvard Medical School [laboratory]; collaborator of Prof. Michael Grüninger, University of Toronto. I agree to the SAPIEN terms of use and to the ShapeNet terms of use.

**Email — Subject: PartNet-Mobility terms of use — publication of derived annotation corrections**

Dear SAPIEN team,

I have registered for PartNet-Mobility under my institutional address ([harvard.edu]) for a non-commercial academic project: a formal audit of part and articulation annotations against a machine-verified ontology of physical object parts, in collaboration with Prof. Michael Grüninger (University of Toronto). Before I publish anything I would like to confirm three points under the terms of use: (1) may I publish per-category statistics of annotation inconsistencies, with counter-models that reference model ids and part names but contain no geometry? (2) may I publish a "diff" of corrected part-hierarchy annotations (model id, part id, corrected parent/joint labels) that is usable only by researchers who have themselves accepted the terms? (3) if the answer to (2) is no, would the lab consider hosting such corrections itself — I would be glad to contribute them to the ManiSkill/SAPIEN repositories? I will of course credit PartNet-Mobility, SAPIEN and ShapeNet in every output.

Thank you,
Yi Ru — Postdoctoral Researcher, Harvard Medical School · yi.ru@alumni.utoronto.ca [ORCID]

### 4.3 GAPartNet — request form and covering email to the PKU EPIC Lab

**Form fields:** Name: Yi Ru · Institution: Harvard Medical School [laboratory] (from [April 2027 or later]: University of Toronto, MIE) · Email: [harvard.edu] · Purpose (≈80 words): Non-commercial academic research auditing the actionable-part annotations of GAPartNet against a verified first-order ontology of physical object parts (extending ISO/IEC 21838-4), producing consistency statistics and provably meaning-preserving mappings between GAPartNet's part vocabulary and those of PartNet, PartNet-Mobility, AgiBot World, Open X-Embodiment and DROID. Collaboration with Prof. Michael Grüninger, University of Toronto. No redistribution; results released as statistics, mappings and papers.

**Email — Subject: GAPartNet dataset request — licence of the dataset (as distinct from the MIT code)**

Dear GAPartNet team,

I have submitted the dataset request form ([date]) for a non-commercial academic project auditing part annotations across several datasets against a verified ontology of physical object parts. Two questions: (1) could you confirm the licence that applies to the dataset itself — the GitHub repository is MIT-licensed, and I want to be sure whether the dataset carries the same or a non-commercial licence; (2) may I publish per-category consistency statistics and a mapping table from GAPartNet's part vocabulary to the ontology, and, where terms allow, a diff of corrected part labels (object id, part id, corrected label — no geometry)? GAPartNet will be credited in all outputs.

Thank you,
Yi Ru — Postdoctoral Researcher, Harvard Medical School · yi.ru@alumni.utoronto.ca

### 4.4 PartNet-Ensembled (PartNetE) — email to the PartSLIP authors

**Subject: PartNet-Ensembled (PartNetE) — access and licence terms for an annotation-consistency audit**

Dear Dr. Liu and co-authors,

I am a postdoctoral researcher at Harvard Medical School (PhD, University of Toronto, 2025), working with Prof. Michael Grüninger on a formally verified ontology of physical object parts and a quantitative audit of part annotations in robot-learning datasets. PartNet-Ensembled, introduced in PartSLIP (CVPR 2023), is one of the corpora I intend to audit alongside PartNet and PartNet-Mobility, from which it is assembled. Could you tell me (1) where the current release is hosted [project page link — confirm], (2) under what licence it is distributed — I assume the ShapeNet, PartNet and SAPIEN non-commercial terms apply, and I have accepted all three — and (3) whether I may publish per-category consistency statistics and a mapping from the PartNetE part vocabulary to the ontology? I would be glad to share the audit results with you before publication.

Best regards,
Yi Ru — Postdoctoral Researcher, Harvard Medical School · yi.ru@alumni.utoronto.ca [ORCID]

### 4.5 AgiBot World — gated acceptance and a licence question to the AgiBot World team

**Gated-access "purpose" field (if asked, ≈50 words):** Academic, non-commercial research: auditing object–part annotations in AgiBot World episodes against a verified first-order ontology of physical object parts and publishing consistency statistics and vocabulary mappings under CC BY-NC-SA 4.0. Postdoctoral researcher, Harvard Medical School; collaborator of Prof. Michael Grüninger, University of Toronto.

**Email — Subject: AgiBot World — licence of the Beta release and publication of derived annotation statistics**

Dear AgiBot World team,

I have accepted the AgiBot World terms on Hugging Face ([date], account [handle]) for a non-commercial academic audit of part annotations against a verified ontology. Could you confirm (1) whether the Beta releases carry the same CC BY-NC-SA 4.0 licence as the Alpha subset, and (2) that publishing per-episode and per-category consistency statistics, a mapping from your object/part vocabulary to the ontology, and corrected-annotation diffs (episode id, object id, part id, corrected label — no frames) under CC BY-NC-SA 4.0 with attribution is consistent with the terms? I do not intend to re-host any frames. I would also be glad to share the audit results with your data team before publication.

Thank you,
Yi Ru — Postdoctoral Researcher, Harvard Medical School · yi.ru@alumni.utoronto.ca

### 4.6 Open X-Embodiment and DROID — no request needed

Download directly; record each OXE sub-dataset's licence from the table on robotics-transformer-x.github.io and the DROID licence from droid-dataset.github.io in the legal folder [date, URL, licence, attribution string]. Optional email to a sub-dataset owner only where the table is silent on the licence: "Dear [owner], your dataset [name] is listed in Open X-Embodiment without an explicit licence on the aggregate table; could you confirm the licence that applies so that I can attribute and, if permitted, re-host an ontology-aligned subset of its part annotations? — Yi Ru, Harvard Medical School."

### 4.7 AXIOMALITY commercial-use enquiry — template for the CTO or counsel (send only after counsel's written position, Q1 2027; never from Dr. Ru's academic registration)

**Subject: Commercial data agreement enquiry — [ShapeNet/PartNet | PartNet-Mobility | AgiBot World]**

Dear [licensing contact],

AXIOMALITY [legal entity, country] builds a verification and certification layer for embodied-AI training data (an offline Engine that checks episode and asset annotations against a machine-verified ontology, and a per-release evidence pack). Our academic collaborators use [dataset] under its non-commercial terms; we would like to understand whether [holder] offers a commercial licence or data agreement that would allow (1) validation of our Engine on [dataset] for commercial purposes, and (2) inclusion of consistency statistics and corrected annotations derived from [dataset] in commercial evidence packs delivered to our customers, with attribution. We do not seek to redistribute [dataset] itself. Could you indicate whether such an agreement is available and, if so, its terms and the contact for negotiation?

Kind regards,
[CTO name], CTO, AXIOMALITY · [company-domain email] · [website]

## 5. Bracketed items in this file

- [Current terms text of ShapeNet, PartNet, SAPIEN/PartNet-Mobility, GAPartNet (dataset vs code), AgiBot World Alpha and Beta, each OXE sub-dataset, DROID — re-read and save at registration]
- [Whether derived annotations / corrected-annotation diffs may be published, per dataset]
- [Whether registration binds use to the registering institution; whether alumni.utoronto.ca is accepted; utoronto.ca staff address available from the appointment]
- [PartNet-Ensembled hosting location, counts and licence — PartSLIP authors]
- [Whether teleoperation footage in AgiBot World / DROID triggers any personal-data handling rule at HMS or U of T — the audit uses no frames]
- [Counsel's position (Q1 2027): whether internal Engine validation on NC datasets is "commercial use"; which datasets may appear in commercial evidence packs; cross-border considerations for GAPartNet/AgiBot agreements]
- [Attribution strings for each OXE sub-dataset and DROID]
- [ORCID; HMS laboratory name; harvard.edu address; Hugging Face handle; CTO name; company-domain email; legal entity and country]
