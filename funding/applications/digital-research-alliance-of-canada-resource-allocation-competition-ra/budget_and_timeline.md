# Resource request and allocation-year timeline — RAC 2027 RRG

*No money is requested; the "budget" is the in-kind resource request in the Alliance's units. Every figure rests on the bracketed assumptions inherited from the compute-bundle estimate (funding/applications/compute-and-data-access-bundle/README.md §"Compute and storage requirement estimate"), which in turn rests on profile/research_program.md; the research program gives no counts, so all counts are assumptions until replaced by pilot measurements. Dataset sizes marked "registry" are unverified. Re-derive every line when an assumption changes.*

## 1. Resource request (allocation year 1 Apr 2027 – 31 Mar 2028)

| Resource | Quantity | Alliance unit | Derivation |
|---|---|---|---|
| GPU, H100-class ([Killarney or Trillium-GPU — confirm; confirm whether AI compute is requested inside the RRG form]) | [5,000–8,000] GPU-hours, central estimate [7,000] | RGU-years: 7,000 h × 12.15 RGU ÷ 8,760 h ≈ **[9.7] RGU-years** (range [6.9–11.1]) at 12.15 RGU per H100-80G [factor from docs.mila.quebec — verify on the Alliance RAC 2027 RGU table; if the target system is A100-40G, the factor is 4.0 and the same hours ≈ [3.2] RGU-years] | see §2 |
| CPU | [2] core-years planned; worst case up to [7] | core-years | see §3 |
| Large-memory nodes | [2–4] jobs at 256 GB | jobs / node-hours [express per the form] | Datalog materialization of the largest corpus; Mace4 counter-model search |
| Project storage | [20 TB] | TB (project) | instance store [2–10 TB] + audit outputs + mappings + corrected-annotation diffs [< 1 TB] + headroom for seven corpora |
| Nearline / scratch storage | [50 TB] | TB (nearline or scratch — [confirm the Alliance categories and which is appropriate for transient raw corpora]) | raw corpora during extraction: OXE ~9 TB, DROID ~1.7 TB, AgiBot World Beta "tens of TB (>40 TB)", ShapeNet+PartNet [~2 TB], PartNet-Mobility/GAPartNet/PartNetE [tens of GB each] (registry figures); O3 rollouts and checkpoints [2–5 TB] |
| Cloud | none | — | — |
| Software | Prover9/Mace4; [Z3]; [Soufflé]; Python; PyTorch; SAPIEN; [Isaac Lab]; LeRobot/RLDS readers | — | all open source; SAPIEN and Isaac Lab need CUDA/RTX-capable GPUs — H100 nodes qualify [verify driver/OS on the target system] |

Rapid Access Service defaults (opportunistic GPU; ~[1 TB] project storage) cannot carry the instance store or the training matrix; that is the reason for an RRG request rather than RAS alone.

## 2. GPU derivation (O3 policy experiments)

| Block | Count | Basis |
|---|---|---|
| Conditions | 8 | {no ontology loss, ontology loss} × {constraint-guided augmentation off, on} = 4, plus 4 single-axiom-family ablations |
| Held-out PartNet-Mobility category splits | [5] | minimum for confidence intervals across categories |
| Seeds | [3] | |
| Main training runs | 8 × 5 × 3 = **120** | |
| Pooled-data transfer runs | {raw pooled, ontology-aligned pooled} × [3] target vocabularies × [3] seeds = **18** | third hypothesis |
| GPU-hours per run | [24] | one A100/H100-class GPU; SAPIEN rendering + ~[1M] environment steps — **replace with the measured pilot figure** |
| Training subtotal | 138 × 24 ≈ **[3,300]** | |
| Verification-in-the-loop evaluation | [+25 %] ≈ **[800]** | violation rate alongside task success, every run |
| Second simulator ([Isaac Lab], half matrix) | ≈ **[2,000]** | replication |
| Development, debugging, failed runs | [+30 %] of training ≈ **[1,000]** | |
| **Total** | **≈ [7,000] GPU-hours** (range [4,000–10,000]) | ≈ [9.7] RGU-years at 12.15 RGU/H100 |
| CPU alongside GPU | [8] cores per GPU → ≈ [1] core-year | SAPIEN physics/rendering |

Cut order if scaled back: Isaac Lab replication (−2,000) → third seed (−1,100 training, −275 eval) → fifth split (−660 training, −165 eval). The three hypotheses survive all three cuts; only precision drops.

## 3. CPU derivation (O2 re-audit and O1 verification)

| Block | Count | Basis |
|---|---|---|
| Instances to check (seven corpora) | [~20M] | PartNet [~574k part instances]; PartNet-Mobility 2,347 models / [~14k movable parts]; GAPartNet [~8.5k]; PartNetE [~PartNet-Mobility scale]; AgiBot World [~15M episode-derived]; OXE [~4M]; DROID [~0.3M] — all bracketed except the PartNet-Mobility model count (web search 2026-09-25) |
| Passes | [15] | [3] ontology versions × [5] axiom-family conditions (four families dropped one at a time + full) |
| Tier 1 (Datalog/SMT bulk) | 20M × [0.2 s] × 15 ≈ 60M core-s ≈ **[17,000] core-hours ≈ [2] core-years** (range [1–4]) | embarrassingly parallel array jobs; 64 GB standard nodes |
| Tier 2 (Prover9/Mace4 residual) | budget [50k] obligations × [300 s] timeout × [5] passes; expected **[4,000] core-hours**, worst case **[60,000]** | UNKNOWN/timeout is a first-class output → worst case bounded |
| O1 verification of the ontology | **< 500 core-hours** | hundreds of obligations × minutes |
| SAPIEN physics/rendering | **[~1] core-year** | from §2 |
| **Total** | **≈ [2] core-years planned** (Tier 1 in the allocation year is the re-audit only; the first audit across five corpora is done at Harvard); **up to [7] worst case** | |

## 4. Storage derivation

| Item | Size | Basis |
|---|---|---|
| Raw corpora during extraction | ~[15 TB] floor (five corpora, Alpha/subsets) to ~[50–70 TB] (all seven incl. AgiBot Beta) | registry: "secure ~15–50 TB" |
| Instance store + audit outputs (metadata only) | [2–10 TB] | [10–20 %] of raw |
| Merged ontology-aligned corpus (mappings, diffs, reports; no frames) | [< 1 TB] | licence-driven |
| O3 rollouts, checkpoints, logs | [2–5 TB] scratch | |
| **Request** | **[20 TB] project + [50 TB] nearline/scratch** | raw corpora are deleted after extraction; instance store and outputs are kept |

Before Harvard access ends (spring 2027) the instance store, outputs and code [2–10 TB] are mirrored to Alliance storage (RAS default now; RAC storage from 1 Apr 2027); raw corpora are re-downloaded in Toronto rather than transferred.

## 5. Non-duplication with other requests (state on the form if asked)

Harvard-period requests (HMS O2; NSF ACCESS Explore/Accelerate; NAIRR; Google/AWS research credits) carry O1, the first audit across five corpora and the O3 pilot ([500–1,000] GPU-hours) between Oct 2026 and Mar 2027; none of them extends past Dr. Ru's move. If an ACCESS Accelerate allocation is awarded for the Toronto period, it is closed early or transferred to the Harvard co-PI and unused credits returned. NVIDIA Academic Grant hardware/credits [if awarded, from spring 2027] carry interactive development and Isaac Lab installation, not the batch matrix.

## 6. Timeline

### Before the allocation year

| When | Milestone |
|---|---|
| 2 Oct 2026 | Ask to the PI sent; CCDB role requested |
| 9 Oct 2026 | PI's decision |
| 17 Oct 2026 | CPRA deadline (salary route for the postdoc; independent of RAC) |
| 20 Oct 2026 | Full draft to the PI; assumptions replaced by pilot measurements where available |
| 30 Oct 2026 | Submitted (hard close 3 Nov) |
| 15 Jan 2027 | Public LeRobot-compatible validator + audit report on 2–3 datasets (self-imposed; cited in later applications) |
| 1 Mar 2027 | Instance store and code mirrored to Alliance storage |
| [Dec 2026 – Mar 2027 — verify] | RAC results |

### Allocation year (1 Apr 2027 – 31 Mar 2028)

| Quarter | O2 (CPU, storage) | O3 (GPU) | Outputs |
|---|---|---|---|
| Q1 (Apr–Jun 2027) | Raw corpora re-downloaded to nearline; instance store rebuilt; released-ontology-version re-audit Tier 1 across seven corpora begins | Per-run cost re-measured on the target system; main matrix begins (conditions 1–4 × splits × seeds) | Audit report v1 across five corpora (from Harvard) published with ontology v1 |
| Q2 (Jul–Sep 2027) | Tier 1 complete; Tier 2 residual proving; label mappings across seven corpora proved | Main matrix complete (120 runs); verification-in-the-loop evaluation | Audit/data paper submitted; corrected-annotation diffs released where permitted |
| Q3 (Oct–Dec 2027) | Re-audit with ontology v2 (post-review); merged ontology-aligned corpus assembled (licence-permitting subsets) | Pooled-transfer block (18 runs); Isaac Lab half-matrix | Methods paper (ML venue) submitted; ontology contributed to COLORE; SC 42 contribution prepared |
| Q4 (Jan–Mar 2028) | Toolkit packaged and documented; final audit statistics frozen | Ablation analysis; final evaluation | Robotics-venue paper; RAC 2028 renewal (Fast Track if science score > 2.0/5) with a year of usage |

Reporting: usage and outputs summarized in the RAC 2028 progress report; publications acknowledge the Alliance and the host site.
