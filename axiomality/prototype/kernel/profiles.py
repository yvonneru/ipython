"""Tolerance profiles and rule-encoding accounting for the v2 (noisy) benchmark.

The v1 rulebook (kernel/rulebook.py, ax-kernel-0.1.0-demo) is left untouched so that
the v1 passport keeps verifying. v2 adds:

* ``SENSOR_MODEL``: the declared noise model of the v2 synthetic recordings.
* ``phys_profile(overrides)``: context manager that temporarily overrides the shared
  ``PHYS`` constants. The engine, the Z3 self-check and the rulebook hash all read
  the same dict, so a profile changes them consistently.
* v2-only engine switches (all default to v1 behaviour when absent):
    max_single_drops   isolated single dropped frames tolerated by R-TIME-02
    smooth_window      odd window for rolling-median positions (support / sink /
                       penetration tests) and Savitzky-Golay-style quadratic fits
                       (R-SUP-01 free-fall test, R-TYPE-03 fragile acceleration)
    event_snap_s       contact events snap to the nearest frame within this time
* ``rule_encoding_counts()``: exact accounting of which rules are decided by Z3 per
  episode, which are Z3-encoded only in the rulebook self-check, and which are
  numeric-only.
"""
from __future__ import annotations

import copy
from contextlib import contextmanager

from kernel.rulebook import PHYS, RULES, spec
from util import canonical_json, sha256_hex

RULEBOOK_V2_VERSION = "ax-kernel-0.2.0-noise"

SENSOR_MODEL = {
    "joint_noise_deg": [0.2, 0.5],        # per-episode sigma drawn uniformly from this range
    "object_pos_noise_m": 0.003,           # sigma per axis (vision / mocap object tracking)
    "object_yaw_noise_rad": 0.01,
    "gripper_width_noise_m": 0.0005,
    "timestamp_jitter_s": 0.005,           # uniform +-5 ms on every timestamp
    "dropped_frame_prob": 0.3,             # probability that an episode has one dropped frame
    "tcp": "recorded TCP = FK(recorded noisy joints), as on real arms",
}

# Starting point for calibration (v1 values plus the v2 switches). The calibration in
# benchmark_v2.py widens a tolerance only if clean calibration episodes (disjoint seeds)
# are falsely rejected by the rule that reads it.
V2_START = {"max_single_drops": 2, "smooth_window": 5, "event_snap_s": 0.5 / 30.0, "qd_margin": 1.0}

# Which PHYS knob each rule reads (used by the calibration loop).
RULE_KNOBS = {
    "R-TIME-02": ["dt_rel_tol"], "R-TIME-01": ["dt_rel_tol"], "R-PERM-02": ["static_tol"],
    "R-PERM-03": ["comove_tol"], "R-SPAT-01": ["pen_tol"], "R-SPAT-02": ["pen_tol"],
    "R-SUP-01": ["support_tol", "ballistic_az"], "R-SUP-02": ["support_tol", "flight_slack_frames"],
    "R-JNT-02": ["qd_margin"],
    "R-GRIP-01": ["grip_width_tol"], "R-TYPE-03": ["a_fragile"], "R-CONT-01": ["reach"],
    "R-KIN-01": ["fk_tol"], "R-PERM-01": ["v_max"],
}


def widen(p: dict, knob: str, factor: float = 1.25) -> None:
    if knob == "ballistic_az":
        lo, hi = p["ballistic_az"]
        p["ballistic_az"] = (round(lo * factor, 4), round(hi / factor, 4))
    elif knob == "flight_slack_frames":
        p[knob] = p[knob] + 1
    else:
        p[knob] = round(p[knob] * factor, 6)


@contextmanager
def phys_profile(overrides: dict | None):
    saved = copy.deepcopy(PHYS)
    try:
        if overrides:
            PHYS.update(overrides)
        yield PHYS
    finally:
        PHYS.clear()
        PHYS.update(saved)


def spec_v2(overrides: dict) -> dict:
    with phys_profile(overrides):
        s = copy.deepcopy(spec())
    s["version"] = RULEBOOK_V2_VERSION
    s["sensor_model"] = SENSOR_MODEL
    counts = rule_encoding_counts()
    for r in s["rules"]:
        r["z3_scope"] = counts["scope"][r["id"]]
    return s


def rulebook_v2_hash(overrides: dict) -> str:
    return "sha256:" + sha256_hex(canonical_json(spec_v2(overrides)))


# Rules whose per-episode verdict is computed by a Z3 query (engine/verifier.py calls
# axioms.check_object / check_phases / check_contact_event and reads the unsat core).
Z3_PER_EPISODE = ("R-QTY-01", "R-QTY-02", "R-TYPE-02", "R-PHASE-01", "R-PHASE-02", "R-PHASE-03", "R-PHASE-04",
                  "R-CONT-01", "R-CONT-02")


def rule_encoding_counts(selfcheck: dict | None = None) -> dict:
    """Exact accounting. ``selfcheck`` is results/rulebook_selfcheck.json (recomputed if None)."""
    if selfcheck is None:
        import json
        from util import RESULTS_DIR
        selfcheck = json.loads((RESULTS_DIR / "rulebook_selfcheck.json").read_text())
    all_ids = [r for r, *_ in RULES]
    sym = set(selfcheck["symbolically_encoded_rules"])
    per_ep = set(Z3_PER_EPISODE)
    scope = {}
    for r in all_ids:
        if r in per_ep:
            scope[r] = "z3_per_episode_decision+selfcheck"
        elif r in sym:
            scope[r] = "z3_selfcheck_only (per-episode verdict computed numerically)"
        else:
            scope[r] = "numeric_only"
    labels = {r: k for r, _, k, _ in RULES}
    mislabelled = [r for r in all_ids if (labels[r] == "z3") != (r in sym)]
    return {
        "total_rules": len(all_ids),
        "z3_encoded_in_selfcheck": len(sym),
        "z3_decides_per_episode": len(per_ep),
        "z3_selfcheck_only": len(sym - per_ep),
        "numeric_only": len(set(all_ids) - sym),
        "numeric_only_rules": sorted(set(all_ids) - sym),
        "z3_per_episode_rules": sorted(per_ep),
        "z3_selfcheck_only_rules": sorted(sym - per_ep),
        "rulebook_kind_label_counts": {"z3": sum(v == "z3" for v in labels.values()),
                                       "numeric": sum(v == "numeric" for v in labels.values())},
        "rulebook_kind_label_disagrees_with_selfcheck": mislabelled,
        "note": ("Per-episode, only the rules in z3_per_episode_rules are decided by a Z3 query. The other "
                 "Z3-encoded rules are encoded symbolically for the rulebook self-check (consistency and "
                 "independence on a bounded 14-frame 1-D abstraction) but are evaluated per episode with numpy "
                 "against the same constants. In real-data mode no Z3 query is made at all."),
        "scope": scope,
    }
