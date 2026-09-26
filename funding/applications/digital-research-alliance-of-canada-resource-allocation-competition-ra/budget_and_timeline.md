# Resource request and allocation-year timeline — RAC 2027 RRG

*No money is requested; the "budget" is the in-kind resource request in the Alliance's units. Every count rests on the bracketed assumptions of the compute-bundle estimate (funding/applications/compute-and-data-access-bundle/README.md §"Compute and storage requirement estimate"), which rests on profile/research_program.md; the research program gives no counts, so all counts are assumptions until replaced by pilot measurements. Dataset sizes marked "registry" are unverified. §0 is the eligibility test; §7 reconciles this file with the bundle and records the arithmetic corrected in review (2026-09-26). Re-derive every line when an assumption changes.*

## 0. Eligibility test (read first)

Search results on 2026-09-26, attributed to the Alliance Rapid Access Service page (https://www.alliancecan.ca/en/our-services/advanced-research-computing/accessing-resources/rapid-access-service; not opened; **verify in the RAC 2027 Application Guide**): "A minimum of compute resources (currently set at 200 core-years for CPU and 25 RGU-years for GPUs) is required to be eligible to submit a RAC application", and "PIs can request a maximum of 40 TB of project storage and 100 TB of nearline storage in any General Purpose cluster without submitting a RAC application."

| Resource | This request (central) | Threshold / ceiling | Result |
|---|---|---|---|
| GPU | [7,000] H100-hours ≈ [9.7] RGU-years (range [6.9–11.1]) | ≥ 25 RGU-years to apply | **Below.** 25 RGU-years = 25 × 8,760 ÷ 12.15 ≈ 18,000 H100-hours, which the matrix in §2 reaches only if the measured per-run cost is ≥ ≈ [61] H100-hours (assumed: [24]) |
| CPU | O2/O1: ≈ [1.4] core-years expected, [2] planned, ≈ [3.3] worst case; simulation cores ride on the GPU jobs | ≥ 200 core-years to apply | **Far below.** RAS opportunistic CPU is the right route |
| Project storage | [20 TB] | RAS: up to 40 TB without RAC | **Within RAS.** The PI can request it now, with no competition |
| Raw-corpus working space | peak ≈ [50 TB] while corpora are extracted | scratch [quota, purge policy and increase route — verify]; nearline is tape-backed [verify] and unsuitable for active extraction | Scratch, not nearline |

**Consequence.** As drafted, the RRG request is not eligible, and its storage and CPU parts do not need RAC. **Gate (decision by 20 Oct 2026; README):** submit the RRG only if (a) the RAC 2027 Guide shows a threshold this request meets (e.g. a different rule for AI compute on Killarney/PAICE), or (b) a measured per-run cost, or other GPU projects in the group, justify ≥ 25 RGU-years *without inflating the design*. Otherwise: the PI files a RAS storage request (20 TB project); O2 CPU runs on RAS opportunistic queues; O3 GPU uses RAS opportunistic GPU plus the routes in §5; and a RAC 2028 request is made with a year of measured usage.

## 1. Resource request (allocation year 1 Apr 2027 – 31 Mar 2028), if the gate passes

| Resource | Quantity | Alliance unit | Derivation |
|---|---|---|---|
| GPU for SAPIEN training and evaluation | [5,000] GPU-hours (main matrix + verification + development, §2) | RGU-years at the target GPU's factor: on H100-80G (12.15 RGU [docs.mila.quebec; verify on the Alliance RAC 2027 table]) 5,000 h ≈ **[6.9] RGU-years** | §2. The target GPU must run SAPIEN's renderer [Vulkan on the compute nodes — verify on the target cluster] |
| GPU for the Isaac Lab half-matrix | [2,000] GPU-hours | RTX-class GPUs only [Killarney L40S tier, if confirmed; RGU factor — verify] | Isaac Sim/Isaac Lab camera rendering needs RT cores; NVIDIA's requirements have listed A100/H100 as unsupported [verify the current page]. If no RTX partition exists on the target system, this line moves to the NVIDIA Academic Grant workstation (§5) and drops out of the request |
| GPU total | **[7,000] GPU-hours ≈ [9.7] RGU-years if all H100** (range [6.9–11.1]) | RGU-years | Below the 25 RGU-year minimum: see §0 |
| CPU (O2 re-audit, O1 verification) | ≈ 12,200 core-hours expected ≈ **[1.4] core-years**; [2] planned; ≈ [3.3] worst case | core-years | §3 |
| CPU alongside GPU (SAPIEN physics/rendering) | [8] cores per GPU × [7,000] GPU-hours ≈ 56,000 core-hours ≈ [6.4] core-years | inside the GPU jobs [verify the cores-per-GPU share on the target cluster; cores above that share are charged] | §2 |
| Large-memory jobs | [2–4] jobs at 256 GB | jobs / node-hours [express per the form] | Datalog materialization of the largest corpus; Mace4 counter-model search |
| Project storage | [20 TB] | TB (project), **within the RAS ceiling** | instance store [2–10 TB] + audit outputs, mappings, corrected-annotation diffs [< 1 TB] + O3 checkpoints and logs [2–5 TB] + headroom |
| Scratch (transient) | peak ≈ [50 TB] | TB (scratch) [quota and increase route — verify] | raw corpora extracted one at a time, then deleted: OXE ~9 TB, DROID ~1.7 TB, AgiBot World Beta "tens of TB (>40 TB)", ShapeNet+PartNet [~2 TB], PartNet-Mobility/GAPartNet/PartNetE [tens of GB each] (registry figures) |
| Nearline | none in year 1 | — | frozen audit snapshots per ontology version can be archived later if the project quota tightens |
| Cloud | none | — | — |
| Software | Prover9/Mace4; [Z3]; [Soufflé]; Python; PyTorch; SAPIEN; [Isaac Lab]; LeRobot/RLDS readers | — | all open source; the hardware limits are in the GPU rows above |

## 2. GPU derivation (O3 policy experiments)

| Block | Count | Basis |
|---|---|---|
| Conditions | 8 | {no ontology loss, ontology loss} × {constraint-guided augmentation off, on} = 4, plus 4 single-axiom-family ablations |
| Held-out PartNet-Mobility category splits | [5] | minimum for confidence intervals across categories |
| Seeds | [3] | |
| Main training runs | 8 × 5 × 3 = **120** | |
| Pooled-data transfer runs | {raw pooled, ontology-aligned pooled} × [3] target vocabularies × [3] seeds = **18** | third hypothesis |
| GPU-hours per run | [24] | one GPU; SAPIEN rendering + ~[1M] environment steps. **Replace with the measured pilot figure, and state which GPU it was measured on**: 24 A100-40G hours would convert at 4.0 RGU, not 12.15 |
| Training subtotal | 138 × 24 ≈ **[3,300]** | |
| Verification-in-the-loop evaluation | [+25 %] ≈ **[800]** | violation rate alongside task success, every run |
| Second simulator ([Isaac Lab], half matrix) | ≈ **[2,000]** | replication; RTX-class GPUs only (§1) |
| Development, debugging, failed runs | [+30 %] of training ≈ **[1,000]** | |
| **Total** | **≈ [7,000] GPU-hours** (range [4,000–10,000]) | ≈ [9.7] RGU-years if all on H100 |
| Break-even for the RAC minimum | ≈ 18,000 H100-hours ≈ **[61] H100-hours per run** with the same matrix | reported so the gate is decided on a measured number, not by enlarging the matrix |
| CPU alongside GPU | [8] cores per GPU × 7,000 h ≈ 56,000 core-hours ≈ [6.4] core-years | SAPIEN physics/rendering; runs inside the GPU jobs |

Cut order if scaled back: Isaac Lab replication (−2,000) → third seed (−46 runs: −1,100 training, −275 evaluation) → fifth split (−16 runs after the seed cut: −384 training, −96 evaluation). All three hypotheses survive all three cuts; only precision drops.

## 3. CPU derivation (O2 re-audit and O1 verification)

| Block | Count | Basis |
|---|---|---|
| Instances to check (seven corpora) | [~20M] | PartNet [~574k part instances]; PartNet-Mobility 2,347 models / [~14k movable parts]; GAPartNet [~8.5k]; PartNetE [~PartNet-Mobility scale]; AgiBot World [~15M episode-derived]; OXE [~4M]; DROID [~0.3M]. All bracketed except the PartNet-Mobility model count (web search 2026-09-25) |
| Passes | [15] | [3] ontology versions × [5] axiom-family conditions (four families dropped one at a time + full) |
| Tier 1 (Datalog/SMT bulk), whole programme | 20M × [0.2 s] × 15 ≈ 60M core-s ≈ **[16,700] core-hours** | embarrassingly parallel array jobs; 64 GB standard nodes |
| Tier 2 (Prover9/Mace4 residual), whole programme | budget [50k] obligations × [5] passes; expected **[4,000] core-hours**; worst case (every obligation hits the [300 s] timeout) 50k × 300 s × 5 ≈ **[20,800] core-hours** | UNKNOWN/timeout is a first-class output, so the worst case is bounded |
| O1 verification of the ontology | **< 500 core-hours** | hundreds of obligations × minutes |
| Whole programme | ≈ 21,200 core-hours expected; ≈ 38,000 worst case | |
| Done at Harvard before the allocation year | ≈ [9,000] core-hours (≈ 1 core-year: pipeline + first audit across five corpora; HMS O2 + ACCESS Explore, bundle §0.3) | |
| **Allocation year** | ≈ **12,200 core-hours ≈ [1.4] core-years expected**; [2] planned (bundle figure); ≈ 29,000 core-hours ≈ **[3.3] worst case** | far below the 200 core-year RAC minimum: RAS opportunistic CPU |

## 4. Storage derivation

| Item | Size | Where |
|---|---|---|
| Raw corpora during extraction | ~[15 TB] floor (five corpora, Alpha/subsets) to ~[50–70 TB] (all seven incl. AgiBot Beta), registry "secure ~15–50 TB"; extracted one corpus at a time, so the peak is set by AgiBot World Beta (>40 TB) | scratch [verify quota and purge window; ask for a temporary increase, or stage AgiBot Beta in parts] |
| Instance store + audit outputs (metadata only) | [2–10 TB] | project |
| Mappings, diffs, reports (no frames) | [< 1 TB] | project; public releases on the Hugging Face Hub |
| O3 rollouts, checkpoints, logs | [2–5 TB] | project (checkpoints) + scratch (rollouts) |
| **Request** | **[20 TB] project** (within the 40 TB RAS ceiling) + scratch for raw corpora | RAS storage request by the PI; no RAC needed |

Before Harvard access ends (the Harvard affiliation runs to the Toronto start, June 2027 or later), the instance store, outputs and code [2–10 TB] are mirrored to Alliance project storage by 1 Mar 2027. Raw corpora are re-downloaded in Canada rather than transferred.

## 5. Non-duplication and the other GPU routes (state on the form if asked)

Harvard-period requests (HMS O2; NSF ACCESS Explore/Accelerate; NAIRR; Google/AWS research credits) carry O1, the first audit across five corpora and the O3 pilot ([500–1,000] GPU-hours) between Oct 2026 and the move; none of them extends past Dr. Ru's Harvard appointment. If an ACCESS Accelerate allocation is awarded for the Toronto period, it is closed early or transferred to the Harvard co-PI and unused credits returned. If the RRG is not submitted (§0), the O3 matrix runs on: RAS opportunistic GPU (SAPIEN runs; slower, no guaranteed throughput); an NVIDIA Academic Grant RTX workstation or DGX Cloud credits (Isaac Lab; Prof. Grüninger as PI, first window after the U of T start); Vector compute only if a Vector affiliation is obtained (Vector DPF, 28 Feb 2027); and [a U of T Robotics Institute / Vector collaborator's existing GPU allocation, with Dr. Ru as a sponsored user — name]. With that mix the matrix stretches beyond 31 Mar 2028, and the cut order in §2 applies.

## 6. Timeline

### Before the allocation year

| When | Milestone |
|---|---|
| 2 Oct 2026 | Ask to the PI: CCDB account, sponsored role, RAS storage request, conditional RRG (emails.md §1) |
| 9 Oct 2026 | PI's decision on sponsoring the role and filing the RAS storage request |
| ~10–19 Oct 2026 | Sponsored role active; [1–2 calibration runs on RAS opportunistic GPU or, if the HMS supervisor permits, an HMS O2 GPU partition] |
| 17 Oct 2026 | CPRA deadline (salary route for the postdoc; independent of RAC) |
| **20 Oct 2026** | **Gate:** RAC 2027 Guide read (thresholds, headings, limits, AI-compute route); measured per-run cost if any. RRG go/no-go. If go: full draft to the PI |
| 30 Oct 2026 | If go: submitted (hard close 3 Nov) |
| [Nov 2026] | PI files the RAS storage request (20 TB project) [route — verify]; independent of the gate |
| 15 Jan 2027 | Public LeRobot-compatible validator + audit report on 2–3 datasets (self-imposed; cited in later applications) |
| 1 Mar 2027 | Instance store and code mirrored to Alliance project storage |
| [Dec 2026 – Mar 2027 — verify] | RAC results (only if submitted) |
| [June 2027 or later] | Dr. Ru's U of T start (never April: STRATEGY Addendum 6). Until then Dr. Ru uses the Alliance resources remotely as a sponsored external collaborator [verify that this is allowed] |

### Allocation year (1 Apr 2027 – 31 Mar 2028)

| Quarter | O2 (CPU, storage) | O3 (GPU) | Outputs |
|---|---|---|---|
| Q1 (Apr–Jun 2027; Dr. Ru still at Harvard, working remotely) | Raw corpora re-downloaded to scratch, one at a time; instance store rebuilt on project storage; Tier-1 re-audit of seven corpora with the released ontology begins | Per-run cost re-measured on the target system; main matrix begins (conditions 1–4 × splits × seeds) | Audit report v1 across five corpora (from Harvard) published with ontology v1 |
| Q2 (Jul–Sep 2027) | Tier 1 complete; Tier-2 residual proving; label mappings across seven corpora proved | Main matrix complete (120 runs); verification-in-the-loop evaluation | Audit/data paper submitted; corrected-annotation diffs released where permitted |
| Q3 (Oct–Dec 2027) | Re-audit with ontology v2 (post-review); merged ontology-aligned corpus assembled (licence-permitting subsets) | Pooled-transfer block (18 runs); Isaac Lab half-matrix (RTX GPUs) | Methods paper (ML venue) submitted; ontology contributed to COLORE; SC 32 contribution prepared |
| Q4 (Jan–Mar 2028) | Toolkit packaged and documented; final audit statistics frozen | Ablation analysis; final evaluation | Robotics-venue paper; RAC 2028: full application with a year of measured usage (Fast Track applies only to renewing an RRG scored > 2.0/5) |

If the matrix runs without an RRG (§5), Q1–Q2 O3 work continues into Q3–Q4 and the pooled-transfer block and Isaac Lab half-matrix move to the RAC 2028 year.

Reporting: usage and outputs summarized in the RAC 2028 application; publications acknowledge the Alliance and the host site.

## 7. Reconciliation with the compute bundle

| Item | Bundle (README estimate; applications.md §0.3, §F) | This package | Reason for any difference |
|---|---|---|---|
| O3 GPU | ~7,000 GPU-hours [4,000–10,000]; Toronto main matrix [5,000–8,000]; §F leaves RGU unconverted | [7,000] central, inside [5,000–8,000]; converted: ≈ [9.7] RGU-years on H100 | Same numbers. This package adds the RGU conversion, the 25 RGU-year test and the RTX constraint for Isaac Lab |
| O2/O1 CPU, Toronto period | "~2 core-years planned; up to ~7 worst case" | 1.4 expected / [2] planned / 3.3 worst case | Bundle worst case uses Tier-2 ≈ 60,000 core-hours, which is 50k × 300 s × **15** passes; its own derivation says **5** passes (≈ 20,800). Both are shown here; the 15-pass reading gives ≈ 8 core-years |
| SAPIEN CPU | "~8 cores per GPU → ~1 core-year" | ≈ 56,000 core-hours ≈ 6.4 core-years, inside the GPU jobs | Arithmetic slip in the bundle: 8 × 7,000 = 56,000 core-hours. Correct it in the bundle too |
| Total CPU in the previous draft of this package | "[2] core-years" while itemizing Tier 1 17,000 + Tier 2 4,000 + SAPIEN ~1 core-year (≈ 3.4 core-years) | 1.4 expected (O2/O1) + simulation inside GPU jobs | Previous total did not match its own lines, and counted the whole-programme Tier 1 in the allocation year |
| Storage | "~20 TB project + ~50 TB nearline/scratch"; "RAS default (~1 TB project) cannot hold this" | 20 TB project via a RAS request; raw corpora on scratch | RAS allows up to 40 TB project and 100 TB nearline without RAC (search 2026-09-26). Nearline is tape-backed and unsuitable for active extraction |
| Cut order "fifth split (−660 training)" | — | −384 training / −96 evaluation after the seed cut | 16 runs × 24 h; the earlier figure matched no run count |
