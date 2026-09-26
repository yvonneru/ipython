"""Slide figures (1600 px wide, white background, DejaVu Sans, AXIOMALITY palette)."""
from __future__ import annotations

import json
import textwrap

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, FancyBboxPatch, Polygon  # noqa: E402

from passport.passport import verify  # noqa: E402
from util import FIG_DIR, HELDOUT_FILE, KEY_FILE, PASSPORT_FILE, RESULTS_DIR, ROOT, read_jsonl  # noqa: E402

INK, CRIMSON, TEAL, GREY = "#151A2D", "#C8123F", "#0F8B8D", "#D5D8E0"
MUTED = "#5A6072"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 15, "axes.edgecolor": GREY, "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK, "text.color": INK, "figure.facecolor": "white",
                     "axes.facecolor": "white", "savefig.facecolor": "white"})
DPI = 100
LABELS = {"a_wrong_label": "(a) wrong\nobject label", "b_impossible_relation": "(b) impossible\nrelation",
          "c_phase_order": "(c) illegal\nphase order", "d_teleport": "(d) object\nteleport",
          "e_timestamp_warp": "(e) timestamp\nwarp", "f_joint_limit": "(f) joint-limit\nviolation",
          "g_gripper_contact_mismatch": "(g) gripper /\ncontact mismatch"}


def benchmark_recall(res: dict) -> None:
    pc, ov = res["per_class"], res["overall"]
    classes = list(LABELS)
    e = [pc[c]["engine_recall"] * 100 for c in classes]
    b = [pc[c]["baseline_recall"] * 100 for c in classes]
    fig, ax = plt.subplots(figsize=(16, 9), dpi=DPI)
    x, w = np.arange(len(classes)), 0.36
    for xs, vals, col, name in ((x - w / 2 - 0.01, e, TEAL, "AXIOMALITY engine"), (x + w / 2 + 0.01, b, INK, "Rules-only baseline")):
        ax.bar(xs, vals, w, color=col, label=name, zorder=3)
        for xi, v in zip(xs, vals):
            ax.text(xi, v + 1.5, f"{v:.0f}%", ha="center", va="bottom", fontsize=15, color=INK, fontweight="bold")
    ax.set_xticks(x, [LABELS[c] for c in classes], fontsize=14)
    ax.set_ylim(0, 112)
    ax.set_yticks([0, 25, 50, 75, 100], ["0%", "25%", "50%", "75%", "100%"])
    ax.set_ylabel("Recall (share of corrupted episodes flagged)")
    ax.grid(axis="y", color=GREY, lw=1, zorder=0)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.legend(loc="upper left", bbox_to_anchor=(0, 1.02), ncol=2, frameon=False, fontsize=15)
    E, B = ov["engine"], ov["baseline"]
    fig.suptitle("Per-class recall on injected errors", x=0.06, ha="left", fontsize=26, fontweight="bold", y=0.97)
    fig.text(0.06, 0.885, f"Internal prototype | SYNTHETIC episodes from sample 109 | n = 10 episodes per class, "
             f"{res['episodes']} episodes total", fontsize=15, color=MUTED)
    fig.text(0.06, 0.03, f"Precision: engine {E['precision']:.2f}, baseline {B['precision']:.2f}   |   "
             f"False rejects on clean: {E['false_reject_rate_clean']:.0%} / {B['false_reject_rate_clean']:.0%}   |   "
             f"Valid failures kept: {E['valid_failures_kept']} / {B['valid_failures_kept']}   |   "
             f"{E['ms_per_episode']:.1f} ms vs {B['ms_per_episode']:.1f} ms per episode", fontsize=14, color=INK)
    fig.subplots_adjust(left=0.06, right=0.98, top=0.83, bottom=0.17)
    fig.savefig(FIG_DIR / "benchmark_recall.png", dpi=DPI)
    plt.close(fig)


def passport_card(pp: dict, valid: bool) -> None:
    fig = plt.figure(figsize=(16, 10), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0.6, 0.6), 14.8, 8.8, boxstyle="round,pad=0,rounding_size=0.3", fc="white", ec=INK, lw=2.5))
    ax.add_patch(FancyBboxPatch((0.6, 7.9), 14.8, 1.5, boxstyle="round,pad=0,rounding_size=0.3", fc=INK, ec=INK))
    ax.add_patch(plt.Rectangle((0.6, 7.9), 14.8, 0.4, fc=INK, ec=INK))
    ax.text(1.2, 8.85, "AXIOMALITY  DATA PASSPORT", color="white", fontsize=30, fontweight="bold", va="center")
    ax.text(1.2, 8.25, f"{pp['dataset_id']}  -  {pp['title']}", color=GREY, fontsize=15, va="center")
    badge_col, badge_txt = (TEAL, "SIGNATURE VALID") if valid else (CRIMSON, "SIGNATURE INVALID")
    ax.add_patch(FancyBboxPatch((11.3, 8.3), 3.7, 0.8, boxstyle="round,pad=0.05,rounding_size=0.35", fc=badge_col, ec="white", lw=2))
    ax.text(13.15, 8.7, ("✓ " if valid else "✗ ") + badge_txt, color="white", fontsize=17, fontweight="bold",
            ha="center", va="center")
    vc = pp["verdict_counts"]
    rs = pp["real_synthetic"]
    fields = [("Content hash", pp["content"]["content_hash"][:39] + "..."),
              ("Accepted split", f"{pp['content']['episodes']} episodes, {pp['content']['frames']:,} frames"),
              ("Verdicts", f"submitted {vc['submitted']}  |  PASS {vc['PASS']}  |  REPAIR {vc['REPAIR']}  |  "
                           f"REJECT {vc['REJECT']}  |  UNKNOWN {vc['UNKNOWN']}"),
              ("Rulebook", f"{pp['rulebook']['version']}  ({pp['rulebook']['hash'][:23]}...)"),
              ("Real / synthetic", f"{rs['real']} real / {rs['synthetic']} synthetic  (100% synthetic demo data)"),
              ("Seed sample", f"{pp['provenance']['seed_sample']['folder']}/{pp['provenance']['seed_sample']['filename']}"
                              f"  (sha256 {pp['provenance']['seed_sample']['sha256'][:12]}...)"),
              ("Engine / checks", f"{pp['checks']['engine']}  |  z3 {pp['checks']['tools']['z3-solver']}  |  "
                                  f"{len(pp['checks']['rule_families'])} rule families"),
              ("Issued / key", f"{pp['issued_at']}  |  {pp['signature']['key_id']} (demo key)")]
    y = 7.3
    for k, v in fields:
        ax.text(1.2, y, k.upper(), fontsize=13, color=MUTED, fontweight="bold", va="center")
        ax.text(4.6, y, v, fontsize=16, color=INK, va="center", family="DejaVu Sans Mono" if "hash" in k.lower() else None)
        ax.plot([1.2, 14.8], [y - 0.38, y - 0.38], color=GREY, lw=1)
        y -= 0.78
    ax.text(1.2, 0.95, "Verify offline:  python verify_passport.py   (Ed25519 signature + recomputed content hash)",
            fontsize=14, color=INK)
    ax.text(14.8, 0.95, "Synthetic demo  |  not a safety certification", fontsize=13, color=CRIMSON, ha="right")
    fig.savefig(FIG_DIR / "passport_card.png", dpi=DPI)
    plt.close(fig)


def verdict_example(verdicts: list, heldout: list, key: dict) -> None:
    cands = [(key[v["episode_id"]]["magnitude_m"], i) for i, v in enumerate(verdicts)
             if key[v["episode_id"]]["class"] == "d_teleport" and key[v["episode_id"]]["mode"] == "glitch"
             and any(f["rule"] == "R-PERM-01" for f in v["findings"])]
    _, i = max(cands)
    v, ep = verdicts[i], heldout[i]
    f0 = next(f for f in v["findings"] if f["rule"] == "R-PERM-01")
    k = f0["frame"]
    mug = np.array(ep["frames"]["object_poses"]["obj0"])
    lap = np.array(ep["frames"]["object_poses"]["obj1"])
    tcp = np.array(ep["frames"]["tcp_pose"])
    dims = {o["id"]: o["dimensions"] for o in ep["scene"]["objects"]}
    fig = plt.figure(figsize=(16, 9), dpi=DPI)
    ax = fig.add_axes([0.08, 0.1, 0.45, 0.74])
    L, W = dims["obj1"]["length"], dims["obj1"]["width"]
    c, s = np.cos(lap[0, 3]), np.sin(lap[0, 3])
    corners = np.array([[L / 2, W / 2], [-L / 2, W / 2], [-L / 2, -W / 2], [L / 2, -W / 2]]) @ np.array([[c, s], [-s, c]]) + lap[0, :2]
    ax.add_patch(Polygon(corners, fc=GREY, ec=MUTED, lw=1.5, zorder=1))
    ax.text(*lap[0, :2], "laptop", ha="center", va="center", fontsize=14, color=INK)
    tr = ep["meta"]["target_region"]
    ax.add_patch(Circle(tr["center"], tr["radius"], fc="none", ec=TEAL, ls="--", lw=2, zorder=2))
    ax.text(tr["center"][0], tr["center"][1] + tr["radius"] + 0.02, "target region", ha="center", fontsize=13, color=TEAL)
    ax.plot(tcp[:, 0], tcp[:, 1], color=MUTED, lw=1.5, ls=":", zorder=2, label="gripper (TCP) path")
    ax.plot(mug[:, 0], mug[:, 1], color=INK, lw=2, marker="o", ms=4, zorder=3, label="mug trajectory (recorded)")
    ax.plot(mug[[k - 1, k], 0], mug[[k - 1, k], 1], color=CRIMSON, lw=3, zorder=4)
    ax.scatter(*mug[k, :2], s=260, color=CRIMSON, zorder=5, edgecolor="white", lw=2, label=f"violating frame {k}")
    ax.annotate(f"frame {k}", mug[k, :2], xytext=(10, -30), textcoords="offset points", color=CRIMSON, fontsize=15,
                fontweight="bold")
    ax.set_aspect("equal")
    ax.set_xlabel("x (m, table frame)")
    ax.set_ylabel("y (m)")
    ax.grid(color=GREY, lw=0.8)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    ax.legend(loc="lower left", frameon=False, fontsize=13)
    fig.suptitle("Verdict example: a rejected episode", x=0.08, ha="left", fontsize=26, fontweight="bold", y=0.96)
    fig.text(0.08, 0.875, f"{ep['episode_id']}  |  top-down view  |  SYNTHETIC episode with an injected teleport",
             fontsize=15, color=MUTED)
    tx = fig.add_axes([0.56, 0.1, 0.41, 0.74])
    tx.axis("off")
    tx.add_patch(FancyBboxPatch((0.0, 0.86), 0.36, 0.1, boxstyle="round,pad=0,rounding_size=0.03", fc=CRIMSON,
                                ec=CRIMSON, transform=tx.transAxes))
    tx.text(0.18, 0.91, "REJECT", color="white", fontsize=22, fontweight="bold", ha="center", va="center",
            transform=tx.transAxes)
    reason = f"{f0['message']}; rule {f0['rule']}"
    tx.text(0, 0.78, "\n".join(textwrap.wrap(reason, 44)), fontsize=17, color=INK, va="top", transform=tx.transAxes,
            fontweight="bold")
    others = [f for f in v["findings"] if f is not f0][:3]
    tx.text(0, 0.62, f"{ep['episode_id']}: outcome label '{ep['meta']['outcome']}', {len(mug)} frames @ "
            f"{ep['meta']['hz']:.0f} Hz\n{len(v['findings'])} finding(s), checked in {v['ms']:.0f} ms",
            fontsize=13, color=MUTED, transform=tx.transAxes)
    y = 0.50
    if others:
        tx.text(0, y, "Other findings", fontsize=14, color=MUTED, fontweight="bold", transform=tx.transAxes)
        y -= 0.06
        for f in others:
            txt = "\n".join(textwrap.wrap(f"{f['rule']}: {f['message']}", 52))
            tx.text(0, y, txt, fontsize=13, color=INK, va="top", transform=tx.transAxes)
            y -= 0.07 * (txt.count("\n") + 1) + 0.03
    tx.text(0, 0.02, "R-PERM-01: no tabletop object moves faster than v_max = 3.0 m/s\n(object permanence, knowledge kernel "
            "ax-kernel-0.1.0-demo)", fontsize=12, color=MUTED, transform=tx.transAxes)
    fig.savefig(FIG_DIR / "verdict_example.png", dpi=DPI)
    plt.close(fig)


def main() -> None:
    res = json.loads((RESULTS_DIR / "benchmark.json").read_text())
    benchmark_recall(res)
    ok, _ = verify()
    passport_card(json.loads(PASSPORT_FILE.read_text()), ok)
    verdict_example(json.loads((RESULTS_DIR / "engine_verdicts.json").read_text()), read_jsonl(HELDOUT_FILE),
                    json.loads(KEY_FILE.read_text())["episodes"])
    print(f"[figures] {', '.join(p.name for p in sorted(FIG_DIR.glob('*.png')))} -> {FIG_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
