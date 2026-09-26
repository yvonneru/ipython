"""v2 slide figures (1600 px wide, same palette / fonts as figures/make_figures.py).

benchmark_v2_recall.png       per-class recall, engine vs strong vs structural baseline (SYNTHETIC, noisy)
benchmark_v2_sensitivity.png  detection rate vs injected magnitude (where the engine and strong baseline differ)
real_data_summary.png         REAL datasets: verdict shares per check family + annotated real findings
real_finding_example.png      one real finding plotted (DROID: commanded motion not executed / joint limit)
"""
from __future__ import annotations

import json
import textwrap

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from figures.make_figures import CRIMSON, DPI, GREY, INK, LABELS, MUTED, TEAL  # noqa: E402  (also sets rcParams)
from engine.real_mode import FAMILIES  # noqa: E402
from inject.inject import ERROR_CLASSES  # noqa: E402
from util import FIG_DIR, RESULTS_DIR, ROOT  # noqa: E402

AMBER = "#D98E04"   # strong baseline (new series; validated CVD-separable from TEAL, labelled directly)
SERIES = (("engine", "AXIOMALITY engine", TEAL), ("strong", "Strong rules baseline (1 week)", AMBER),
          ("structural", "Structural baseline (1 afternoon)", INK))
VERDICT_COL = {"PASS": TEAL, "REPAIR": AMBER, "REJECT": CRIMSON, "UNKNOWN": GREY}


def _clean(ax):
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)


def benchmark_v2_recall(res: dict) -> None:
    pc, ov = res["per_class"], res["overall"]
    fig, ax = plt.subplots(figsize=(16, 9), dpi=DPI)
    x, w = np.arange(len(ERROR_CLASSES)), 0.26
    for j, (k, name, col) in enumerate(SERIES):
        vals = [pc[c][f"{k}_recall"] * 100 for c in ERROR_CLASSES]
        xs = x + (j - 1) * (w + 0.02)
        ax.bar(xs, vals, w, color=col, label=name, zorder=3)
        for xi, v in zip(xs, vals):
            ax.text(xi, v + 1.5, f"{v:.0f}%", ha="center", va="bottom", fontsize=12, color=INK, fontweight="bold")
    ax.set_xticks(x, [LABELS[c] for c in ERROR_CLASSES], fontsize=14)
    ax.set_ylim(0, 112)
    ax.set_yticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"])
    ax.set_ylabel("Recall (share of corrupted episodes flagged)")
    ax.grid(axis="y", color=GREY, lw=1, zorder=0)
    _clean(ax)
    ax.legend(loc="upper left", bbox_to_anchor=(0, 1.03), ncol=3, frameon=False, fontsize=14)
    E, S, B = ov["engine"], ov["strong"], ov["structural"]
    fig.suptitle("Benchmark v2: per-class recall on noisy data", x=0.06, ha="left", fontsize=26, fontweight="bold", y=0.97)
    fig.text(0.06, 0.885, f"Internal prototype | SYNTHETIC noisy episodes (0.2-0.5 deg joint noise, 3 mm object noise, "
             f"+-5 ms jitter, dropped frames) | 3 task variants | n = {res['per_class_n']}/class, {res['episodes']} total",
             fontsize=12.5, color=MUTED)
    fig.text(0.06, 0.03, f"Overall recall {E['recall']:.2f} / {S['recall']:.2f} / {B['recall']:.2f}   |   precision "
             f"{E['precision']:.2f} / {S['precision']:.2f} / {B['precision']:.2f}   |   false rejects on clean "
             f"{E['false_rejects_clean']} / {S['false_rejects_clean']} / {B['false_rejects_clean']}   |   valid failures kept "
             f"{E['valid_failures_kept']} each   |   {E['ms_per_episode']:.0f} / {S['ms_per_episode']:.1f} / "
             f"{B['ms_per_episode']:.1f} ms per episode", fontsize=12.5, color=INK)
    fig.subplots_adjust(left=0.06, right=0.98, top=0.83, bottom=0.17)
    fig.savefig(FIG_DIR / "benchmark_v2_recall.png", dpi=DPI)
    plt.close(fig)


def benchmark_v2_sensitivity(res: dict) -> None:
    sw = res["sensitivity_sweep"]["curves"]
    titles = {"laptop_sunk_mm": "laptop sunk into table", "persistent_teleport_mm": "object jumps after release",
              "floating_after_release_mm": "object hovers after release", "laptop_floating_mm": "laptop floating"}
    fig, axes = plt.subplots(1, 4, figsize=(16, 6.5), dpi=DPI, sharey=True)
    for ax, (kind, title) in zip(axes, titles.items()):
        rows = sw[kind]
        mm = [r["mm"] for r in rows]
        for k, name, col in SERIES:
            ax.plot(mm, [r[k] * 100 for r in rows], color=col, lw=2.5, marker="o", ms=8, label=name,
                    markeredgecolor="white", markeredgewidth=2, zorder=3)
        ax.set_title(title, fontsize=15, loc="left", color=INK)
        ax.set_xlabel("injected magnitude (mm)", fontsize=13)
        ax.set_ylim(-5, 108)
        ax.grid(color=GREY, lw=0.8, zorder=0)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
    axes[0].set_ylabel("detected (%)")
    axes[0].set_yticks([0, 50, 100], ["0%", "50%", "100%"])
    axes[0].legend(loc="upper left", bbox_to_anchor=(0, 1.32), ncol=3, frameon=False, fontsize=13)
    fig.suptitle("Where the engine and the strong baseline differ: smallest detectable error", x=0.06, ha="left",
                 fontsize=22, fontweight="bold", y=0.98)
    fig.text(0.06, 0.02, f"SYNTHETIC noisy episodes; {res['sensitivity_sweep']['n_base_episodes']} identical clean base "
             "episodes per point; calibrated tolerances as in the benchmark.\nInterpenetration (not shown): "
             "5-30 mm all caught by both rule-based checkers.", fontsize=12, color=MUTED)
    fig.subplots_adjust(left=0.06, right=0.98, top=0.74, bottom=0.21, wspace=0.12)
    fig.savefig(FIG_DIR / "benchmark_v2_sensitivity.png", dpi=DPI)
    plt.close(fig)


def real_data_summary(rep: dict) -> None:
    names = list(rep["datasets"])
    fig = plt.figure(figsize=(16, 11), dpi=DPI)
    fam_labels = [f.replace("_", " ") for f in FAMILIES]
    for i, n in enumerate(names):
        d = rep["datasets"][n]
        ax = fig.add_axes([0.10 + i * 0.30, 0.33, 0.25, 0.47])
        y = np.arange(len(FAMILIES))[::-1]
        left = np.zeros(len(FAMILIES))
        for v in ("PASS", "REPAIR", "REJECT", "UNKNOWN"):
            vals = np.array([d["family_table"][f][v] for f in FAMILIES])
            ax.barh(y, vals, 0.72, left=left, color=VERDICT_COL[v], edgecolor="white", lw=2, label=v, zorder=3)
            left += vals
        ax.set_xlim(0, 100)
        ax.set_xticks([0, 50, 100], ["0", "50", "100%"], fontsize=11)
        ax.set_yticks(y, fam_labels if i == 0 else [""] * len(y), fontsize=12)
        ax.tick_params(axis="y", length=0)
        for s in ("top", "right", "left", "bottom"):
            ax.spines[s].set_visible(False)
        v = d["verdicts"]
        ax.set_title(f"{n}\n{d['robot_type']} | {d['episodes']} episodes, {d['frames']:,} frames\n"
                     f"episode verdicts: PASS {v['PASS']} | REPAIR {v['REPAIR']} | REJECT {v['REJECT']}", fontsize=13,
                     loc="left", color=INK)
        if i == 0:
            ax.legend(loc="upper left", bbox_to_anchor=(0, 1.2), ncol=4, frameon=False, fontsize=12)
    fig.suptitle("Real-data mode on REAL robot datasets (Open X-Embodiment subsets)", x=0.03, ha="left",
                 fontsize=24, fontweight="bold", y=0.985)
    fig.text(0.03, 0.935, "Share of episodes per verdict and check family. Grey = UNKNOWN: the dataset lacks the input "
             "(no timestamps anywhere, no object state anywhere).", fontsize=13, color=MUTED)
    dr = rep["datasets"]["droid_100"]
    picks = [f for f in dr["findings"] if f["family"] in ("action_state", "joint_limits", "schema")][:3]
    for j, f in enumerate(picks):
        x0 = 0.03 + j * 0.325
        ax = fig.add_axes([x0, 0.05, 0.31, 0.19])
        ax.axis("off")
        ax.add_patch(plt.Rectangle((0, 0), 1, 1, fc="white", ec=CRIMSON, lw=2, transform=ax.transAxes))
        head = f"droid_100 | episode {f['episode']}" + (f" | frame {f['frame']}" if f["frame"] is not None else "")
        ax.text(0.04, 0.88, head, fontsize=12.5, fontweight="bold", color=CRIMSON, transform=ax.transAxes, va="top")
        body = f["what"]
        why = {"schema": "Documented as '6x joint velocities, 1x gripper position'; it is the commanded Cartesian pose.",
               "action_state": "Recorded (action, next state) pairs contradict each other: stuck arm or stale stream.",
               "joint_limits": "Panda datasheet limit 3.7525 rad; a Franka FR3 allows 4.52 rad, so this may be an "
                               "arm-model mismatch."}[f["family"]]
        ax.text(0.04, 0.70, "\n".join(textwrap.wrap(body, 56)[:4]), fontsize=11, color=INK, transform=ax.transAxes, va="top")
        ax.text(0.04, 0.26, "\n".join(textwrap.wrap(why, 60)[:3]), fontsize=10.5, color=MUTED, transform=ax.transAxes,
                va="top", style="italic")
    fig.savefig(FIG_DIR / "real_data_summary.png", dpi=DPI)
    plt.close(fig)


def real_finding_example(rep: dict) -> None:
    dr = rep["datasets"]["droid_100"]
    stuck = next(f for f in dr["findings"] if f["family"] == "action_state")
    lim = next(f for f in dr["findings"] if f["family"] == "joint_limits")
    info = json.loads((ROOT / "data" / "real" / "droid_100" / "meta" / "info.json").read_text())
    fig = plt.figure(figsize=(16, 8), dpi=DPI)
    # left: stuck arm
    df = pd.read_parquet(ROOT / "data" / "real" / "droid_100" / "data" / "chunk-000" / f"episode_{stuck['episode']:06d}.parquet")
    q = np.stack(df["observation.state"])[:, :7]
    qa = np.stack(df["action.joint_position"])
    ax = fig.add_axes([0.06, 0.14, 0.42, 0.62])
    j = int(np.argmax(np.abs(qa - q).max(0)))
    k0 = stuck["frame"]
    ax.axvspan(k0, k0 + 15, color=CRIMSON, alpha=0.10, lw=0)
    ax.plot(q[:, j], color=INK, lw=2.5, label=f"observed joint {j + 1}")
    ax.plot(qa[:, j], color=AMBER, lw=2.5, ls="--", label=f"commanded joint {j + 1}")
    ax.set_xlabel("frame (15 Hz)")
    ax.set_ylabel("rad")
    ax.grid(color=GREY, lw=0.8)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(loc="center right", frameon=False, fontsize=13)
    ax.set_title(f"episode {stuck['episode']} ({stuck['source']})", loc="left", fontsize=14, color=INK)
    ax.text(k0 + 0.5, ax.get_ylim()[1], f"frames {k0}-{k0 + 14}: command moves,\njoints bit-identical", color=CRIMSON,
            fontsize=12.5, va="top", fontweight="bold")
    # right: joint 6 vs datasheet limit
    df = pd.read_parquet(ROOT / "data" / "real" / "droid_100" / "data" / "chunk-000" / f"episode_{lim['episode']:06d}.parquet")
    q = np.stack(df["observation.state"])[:, :7]
    hi = info["axiomality_profile"]["limits"]["q_upper"][5]
    ax2 = fig.add_axes([0.55, 0.14, 0.42, 0.62])
    over = q[:, 5] > hi
    ax2.plot(q[:, 5], color=INK, lw=2.5, label="observed joint 6")
    ax2.axhline(hi, color=CRIMSON, lw=2, ls="--", label=f"Panda datasheet limit {hi} rad")
    ax2.fill_between(np.arange(len(q)), hi, q[:, 5], where=over, color=CRIMSON, alpha=0.18, lw=0)
    ax2.set_xlabel("frame (15 Hz)")
    ax2.grid(color=GREY, lw=0.8)
    for s in ("top", "right"):
        ax2.spines[s].set_visible(False)
    ax2.legend(loc="lower right", frameon=False, fontsize=13)
    ax2.set_title(f"episode {lim['episode']} ({lim['source']})", loc="left", fontsize=14, color=INK)
    kmax = int(np.argmax(q[:, 5]))
    ax2.annotate(f"{q[kmax, 5]:.3f} rad (+{(q[kmax, 5] - hi) * 1e3:.0f} mrad)\nframes {np.flatnonzero(over)[0]}-"
                 f"{np.flatnonzero(over)[-1]}", (kmax, q[kmax, 5]), xytext=(-230, -10), textcoords="offset points",
                 color=CRIMSON, fontsize=12.5, fontweight="bold", arrowprops=dict(arrowstyle="-", color=CRIMSON))
    fig.suptitle("Two real findings in DROID (droid_100, Franka Panda)", x=0.06, ha="left", fontsize=24,
                 fontweight="bold", y=0.97)
    fig.text(0.06, 0.845, "REAL data. Left: commanded motion not executed (REJECT, action-state family).\nRight: joint 6 "
             "beyond the Panda datasheet limit (REJECT; the arm could be an FR3, whose joint-6 limit is 4.52 rad).",
             fontsize=13, color=MUTED)
    fig.savefig(FIG_DIR / "real_finding_example.png", dpi=DPI)
    plt.close(fig)


def main() -> None:
    res = json.loads((RESULTS_DIR / "benchmark_v2.json").read_text())
    benchmark_v2_recall(res)
    benchmark_v2_sensitivity(res)
    rp = RESULTS_DIR / "real_data.json"
    if rp.exists():
        rep = json.loads(rp.read_text())
        real_data_summary(rep)
        real_finding_example(rep)
    print("[figures v2] benchmark_v2_recall.png, benchmark_v2_sensitivity.png, real_data_summary.png, "
          "real_finding_example.png -> figures/")


if __name__ == "__main__":
    main()
