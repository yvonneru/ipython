"""AXIOMALITY demo knowledge kernel: the declarative rulebook.

Everything the engine enforces is declared here once (types, properties,
quantity ranges, physical constants, arm limits, rule catalogue). The Z3
encodings in ``kernel/axioms.py`` and the numeric evaluators in
``engine/verifier.py`` both read from this module, and the rulebook hash that
goes into the Data Passport is computed over ``spec()``.

Units: meters, radians, seconds.
"""
from __future__ import annotations

import math

from util import canonical_json, sha256_hex

RULEBOOK_VERSION = "ax-kernel-0.1.0-demo"

# --------------------------------------------------------------------------
# Object types (the company's class vocabulary) and their properties.
# size ranges: (lo, hi) for the larger horizontal extent "hmax", the smaller
# horizontal extent "hmin", and the vertical extent "height" of the fitted box.
# Ranges were written from general household-object knowledge, not fitted to
# the injected benchmark.
# --------------------------------------------------------------------------
PROPERTIES = ("graspable", "fragile", "container", "rigid", "deformable")

CLASSES = {
    "mug":      dict(graspable=True, fragile=True,  container=True,  rigid=True,  deformable=False,
                     hmax=(0.07, 0.16), hmin=(0.06, 0.13), height=(0.07, 0.16)),
    "laptop":   dict(graspable=True, fragile=True,  container=False, rigid=True,  deformable=False,
                     hmax=(0.28, 0.45), hmin=(0.18, 0.45), height=(0.01, 0.35)),
    "keyboard": dict(graspable=True, fragile=False, container=False, rigid=True,  deformable=False,
                     hmax=(0.28, 0.50), hmin=(0.09, 0.20), height=(0.01, 0.05)),
    "earphone": dict(graspable=True, fragile=False, container=False, rigid=False, deformable=True,
                     hmax=(0.02, 0.20), hmin=(0.01, 0.18), height=(0.005, 0.20)),
    "cap":      dict(graspable=True, fragile=False, container=False, rigid=False, deformable=True,
                     hmax=(0.18, 0.32), hmin=(0.14, 0.25), height=(0.06, 0.16)),
    "vase":     dict(graspable=True, fragile=True,  container=True,  rigid=True,  deformable=False,
                     hmax=(0.05, 0.40), hmin=(0.05, 0.40), height=(0.10, 0.60)),
    "fruit":    dict(graspable=True, fragile=True,  container=False, rigid=True,  deformable=False,
                     hmax=(0.03, 0.20), hmin=(0.03, 0.20), height=(0.03, 0.20)),
}
VOCAB = tuple(CLASSES)

# Task phases (episode layer). "abort" is only legal in failure episodes.
PHASES = ("approach", "grasp", "transport", "place", "release", "abort")
PHASE_RANK = {p: i for i, p in enumerate(PHASES)}
CONTACT_PHASES = ("grasp", "transport", "place", "release")
CONTACT_REQUIRED_PHASES = ("transport", "place")
OUTCOMES = ("success", "failure_slip")

# --------------------------------------------------------------------------
# Declared 7-DoF arm (Panda-style modified-DH kinematics, declared limits) and
# a parallel-jaw gripper with 0.14 m stroke.
# --------------------------------------------------------------------------
ARM = dict(
    name="AX-ARM7 (Panda-style DH, declared)",
    base_xyz=(-0.60, 0.05, 0.0),
    dh=((0.0, 0.333, 0.0), (0.0, 0.0, -math.pi / 2), (0.0, 0.316, math.pi / 2), (0.0825, 0.0, math.pi / 2),
        (-0.0825, 0.384, -math.pi / 2), (0.0, 0.0, math.pi / 2), (0.088, 0.0, math.pi / 2)),
    flange_d=0.107,
    tcp_offset=0.15,
    q_lower=(-2.8973, -1.7628, -2.8973, -3.0718, -2.8973, -0.0175, -2.8973),
    q_upper=(2.8973, 1.7628, 2.8973, -0.0698, 2.8973, 3.7525, 2.8973),
    qd_max=(2.175, 2.175, 2.175, 2.175, 2.61, 2.61, 2.61),
    gripper_aperture=0.14,
)

# --------------------------------------------------------------------------
# Physical constants and tolerances (set from physical reasoning and sensor
# noise assumptions; the same constants are shared with the baseline where a
# baseline check exists).
# --------------------------------------------------------------------------
PHYS = dict(
    table_z=0.0,
    g=9.81,
    v_max=3.0,             # m/s, no tabletop object moves faster (R-PERM-01)
    static_tol=0.005,      # m/frame, free supported object is static (R-PERM-02)
    comove_tol=0.010,      # m/frame, attached object follows TCP (R-PERM-03)
    pen_tol=0.010,         # m, allowed box interpenetration / table sink (R-SPAT-*)
    support_tol=0.015,     # m, max gap for "resting on" (box-fit noise) (R-SUP-*)
    reach=0.06,            # m, TCP-centroid distance for a contact begin (R-CONT-01)
    grip_width_tol=0.010,  # m, finger width vs object width while grasping (R-GRIP-01)
    a_fragile=8.0,         # m/s^2, max accel of an attached fragile object (R-TYPE-03)
    fk_tol=0.005,          # m, recorded TCP vs FK(joints) (R-KIN-01)
    dt_rel_tol=0.25,       # sampling interval within +-25% of 1/hz (R-TIME-02)
    ballistic_az=(-1.5, -0.5),  # free-flight vertical accel range, in units of g (R-SUP-01)
    flight_slack_frames=2,
)

REQUIRED_META = ("robot_id", "calibration_hash", "consent_id", "synthetic", "hz", "outcome",
                 "manipulated_object", "target_region")

# --------------------------------------------------------------------------
# Rule catalogue. `z3` marks rules that are encoded as Z3 axioms (per-episode
# decision and/or rulebook self-check); the rest are evaluated numerically on
# dense time series against the same constants.
# --------------------------------------------------------------------------
RULES = [
    ("R-PROV-01", "provenance", "numeric", "Provenance metadata (robot id, calibration hash, consent id, real/synthetic flag, rate, outcome, task spec) must be present; otherwise the verdict is UNKNOWN."),
    ("R-TIME-01", "time", "numeric", "Timestamps are strictly increasing (repairable if rows are merely out of order)."),
    ("R-TIME-02", "time", "z3", "Sampling interval stays within +-25% of the declared rate (no dropped frames)."),
    ("R-QTY-01", "quantity", "z3", "All quantities finite; object dimensions positive with hmin <= hmax."),
    ("R-QTY-02", "quantity", "z3", "Object dimensions lie inside the plausible size range of the labelled class."),
    ("R-TYPE-01", "type", "numeric", "Object labels belong to the kernel vocabulary."),
    ("R-TYPE-02", "type", "z3", "The manipulated object is parallel-graspable: graspable(class) and hmin <= gripper aperture."),
    ("R-TYPE-03", "type", "numeric", "An attached fragile object is not accelerated beyond a_fragile."),
    ("R-TYPE-04", "type", "z3", "Property coherence: rigid <-> not deformable; container -> rigid."),
    ("R-JNT-01", "arm", "z3", "Joint positions within declared limits."),
    ("R-JNT-02", "arm", "z3", "Joint speeds within declared limits."),
    ("R-KIN-01", "arm", "numeric", "Recorded TCP position equals forward kinematics of the recorded joints (<= fk_tol)."),
    ("R-GRIP-01", "gripper", "z3", "While in contact the gripper is commanded closed and finger width matches the object width."),
    ("R-GRIP-02", "gripper", "z3", "Finger width within [0, aperture]."),
    ("R-CONT-01", "contact", "z3", "A contact begins only with the gripper closed and the TCP within reach of the object."),
    ("R-CONT-02", "contact", "z3", "A contact ends only when the gripper opens or the object enters free flight (slip)."),
    ("R-CONT-03", "contact", "numeric", "Contact events alternate begin/end, reference known objects and lie inside the episode."),
    ("R-PERM-01", "permanence", "z3", "Object permanence: no object moves faster than v_max (no teleport)."),
    ("R-PERM-02", "permanence", "z3", "A free object resting on a support stays put (landing frame exempt)."),
    ("R-PERM-03", "permanence", "z3", "An attached object moves rigidly with the TCP."),
    ("R-SUP-01", "support", "z3", "A free, unsupported object is in ballistic flight (vertical accel ~ -g)."),
    ("R-SUP-02", "support", "numeric", "Flight time is bounded by the free-fall time from the observed height."),
    ("R-SPAT-01", "spatial", "z3", "No object sinks into the table beyond pen_tol."),
    ("R-SPAT-02", "spatial", "z3", "Rigid boxes do not interpenetrate beyond pen_tol."),
    ("R-PHASE-01", "phase", "z3", "Phase labels are from the task vocabulary and the episode starts with approach."),
    ("R-PHASE-02", "phase", "z3", "Phases follow approach < grasp < transport < place < release, each as one contiguous block."),
    ("R-PHASE-03", "phase", "z3", "A success episode contains all five phases and ends in release."),
    ("R-PHASE-04", "phase", "z3", "abort follows grasp or transport and occurs only in (and must end) a failure episode."),
    ("R-PHASE-05", "phase", "z3", "Contact only during grasp..release; transport and place require contact."),
    ("R-TASK-01", "task", "z3", "outcome=success implies the object ends released, supported, inside the target region."),
]
RULE_TEXT = {rid: text for rid, _, _, text in RULES}


def spec() -> dict:
    """Canonical, hashable description of the whole rulebook."""
    return dict(version=RULEBOOK_VERSION, classes=CLASSES, phases=PHASES, outcomes=OUTCOMES,
                arm=ARM, phys=PHYS, required_meta=REQUIRED_META,
                rules=[dict(id=r, family=f, kind=k, text=t) for r, f, k, t in RULES])


def rulebook_hash() -> str:
    return "sha256:" + sha256_hex(canonical_json(spec()))


def horizontal_dims(dimensions: dict) -> tuple[float, float, float]:
    """(hmax, hmin, height) from a {'length','width','height'} record."""
    l, w = float(dimensions["length"]), float(dimensions["width"])
    return max(l, w), min(l, w), float(dimensions["height"])
