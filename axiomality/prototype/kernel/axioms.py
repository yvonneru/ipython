"""Z3 encoding of the knowledge kernel.

* ``kernel_facts()``      ground facts: class properties, size ranges, phase ranks.
* ``check_object`` / ``check_phases`` / ``check_contact_event``
                          per-episode decisions used by the engine; violated rule
                          IDs come from Z3 unsat cores.
* ``self_check()``        the "rulebook self-check": Z3 must find a model of the
                          whole axiom set (type layer + a bounded symbolic
                          episode), the seed scene 109 must satisfy the scene
                          axioms, and each episode rule is tested for
                          independence (not implied by the others).
"""
from __future__ import annotations

import time

import numpy as np
from z3 import (And, Bool, BoolVal, Const, EnumSort, ForAll, Function, Implies, IntSort, Not, Or, Real,
                RealSort, RealVal, BoolSort, Solver, is_true, sat, unsat)

from kernel.geometry import box_penetration
from kernel.rulebook import (ARM, CLASSES, CONTACT_PHASES, PHASE_RANK, PHASES, PHYS, PROPERTIES, RULES, VOCAB,
                             horizontal_dims)

ClsSort, _cls = EnumSort("ObjClass", list(VOCAB))
CLS = dict(zip(VOCAB, _cls))
PhaseSort, _ph = EnumSort("Phase", list(PHASES))
PH = dict(zip(PHASES, _ph))
PROP = {p: Function(p, ClsSort, BoolSort()) for p in PROPERTIES}
DIMS = ("hmax", "hmin", "height")
LO = {d: Function(f"{d}_lo", ClsSort, RealSort()) for d in DIMS}
HI = {d: Function(f"{d}_hi", ClsSort, RealSort()) for d in DIMS}
rank = Function("rank", PhaseSort, IntSort())
APERTURE = RealVal(str(ARM["gripper_aperture"]))


def R(x: float):
    return RealVal(repr(float(x)))


def kernel_facts() -> list:
    facts = []
    for c, spec in CLASSES.items():
        facts += [PROP[p](CLS[c]) == BoolVal(spec[p]) for p in PROPERTIES]
        for d in DIMS:
            facts += [LO[d](CLS[c]) == R(spec[d][0]), HI[d](CLS[c]) == R(spec[d][1])]
    facts += [rank(PH[p]) == PHASE_RANK[p] for p in PHASES]
    return facts


FACTS = kernel_facts()
_BASE = Solver()
_BASE.add(FACTS)


def _absle(e, b):
    return And(e <= b, -e <= b)


# ---------------------------------------------------------------- type layer
def rule_qty01(hx, hn, h):
    return And(hx > 0, hn > 0, h > 0, hn <= hx)


def rule_qty02(c, hx, hn, h):
    return And(*[And(LO[d](c) <= v, v <= HI[d](c)) for d, v in zip(DIMS, (hx, hn, h))])


def rule_type02(c, hn):
    return And(PROP["graspable"](c), hn <= APERTURE)


_x = Const("x", ClsSort)
RULE_TYPE04 = ForAll([_x], And(PROP["rigid"](_x) == Not(PROP["deformable"](_x)),
                               Implies(PROP["container"](_x), PROP["rigid"](_x))))


def violated(facts: list, tracked: dict) -> list[str]:
    """All tracked rules that conflict with the facts (iterated unsat cores)."""
    remaining, out = dict(tracked), []
    while remaining:
        _BASE.push()
        _BASE.add(facts)
        for rid, f in remaining.items():
            _BASE.assert_and_track(f, rid)
        res = _BASE.check()
        core = [str(c) for c in _BASE.unsat_core()] if res == unsat else []
        _BASE.pop()
        if res != unsat:
            break
        if not core:  # facts alone inconsistent
            out.append("FACTS-INCONSISTENT")
            break
        out += core
        for c in core:
            remaining.pop(c, None)
    return out


def check_object(label: str, dims: dict, manipulated: bool) -> list[str]:
    hmax, hmin, height = horizontal_dims(dims)
    c, hx, hn, h = Const("c", ClsSort), Real("hx"), Real("hn"), Real("h")
    facts = [c == CLS[label], hx == R(hmax), hn == R(hmin), h == R(height)]
    tracked = {"R-QTY-01": rule_qty01(hx, hn, h), "R-QTY-02": rule_qty02(c, hx, hn, h)}
    if manipulated:
        tracked["R-TYPE-02"] = rule_type02(c, hn)
    return violated(facts, tracked)


# ---------------------------------------------------------------- phase layer
def _phase_rules(P, success, full=True):
    n = len(P)
    rules = {
        "R-PHASE-01": P[0] == PH["approach"],
        "R-PHASE-02": And(*[rank(P[i + 1]) > rank(P[i]) for i in range(n - 1)]) if n > 1 else BoolVal(True),
        "R-PHASE-04": And(P[0] != PH["abort"], *[Implies(P[i] == PH["abort"], And(Not(success), Or(
            P[i - 1] == PH["grasp"], P[i - 1] == PH["transport"]))) for i in range(1, n)]),
    }
    if full:
        rules["R-PHASE-03"] = Implies(success, And(P[-1] == PH["release"], BoolVal(n == 5)))
        rules["R-PHASE-04"] = And(rules["R-PHASE-04"], Implies(Not(success), P[-1] == PH["abort"]))
    return rules


def check_phases(segment_labels: list[str], outcome_success: bool) -> list[tuple[str, int]]:
    """Returns [(rule_id, offending_segment_index)] for a run-length phase sequence."""
    n = len(segment_labels)
    P = [Const(f"p{i}", PhaseSort) for i in range(n)]
    s = Bool("success")
    facts = [P[i] == PH[lab] for i, lab in enumerate(segment_labels)] + [s == BoolVal(outcome_success)]
    out = []
    for rid in violated(facts, _phase_rules(P, s)):
        seg = n - 1
        for m in range(1, n + 1):  # localise: shortest violating prefix
            pre = _phase_rules(P[:m], s, full=False)
            if rid in pre and violated(facts[:m] + facts[-1:], {rid: pre[rid]}):
                seg = m - 1
                break
        out.append((rid, seg))
    return out


# ---------------------------------------------------------------- contact layer
def check_contact_event(kind: str, closed: bool, dist: float, opened: bool, free_after: bool) -> list[str]:
    cl, op, fr, d = Bool("closed"), Bool("opened"), Bool("free_after"), Real("dist")
    facts = [cl == BoolVal(closed), op == BoolVal(opened), fr == BoolVal(free_after), d == R(dist)]
    if kind == "contact_begin":
        return violated(facts, {"R-CONT-01": And(cl, d <= R(PHYS["reach"]))})
    return violated(facts, {"R-CONT-02": Or(op, fr)})


# ---------------------------------------------------------------- self-check
def symbolic_episode(N: int = 14, hz: float = 30.0, gw: float = 0.12, h: float = 0.12, target_x: float = 0.30,
                     radius: float = 0.05):
    """Bounded symbolic episode (1-D horizontal + vertical) with every episode rule
    instantiated over all frames. Returns (vars, {rule_id: [formulas]})."""
    P = PHYS
    t = [Real(f"t{k}") for k in range(N)]
    ph = [Const(f"ph{k}", PhaseSort) for k in range(N)]
    cmd = [Bool(f"closed{k}") for k in range(N)]
    c = [Bool(f"contact{k}") for k in range(N)]
    w, ox, og, ex, ez = ([Real(f"{n}{k}") for k in range(N)] for n in ("w", "ox", "og", "ex", "ez"))
    q = [[Real(f"q{k}_{j}") for j in range(7)] for k in range(N)]
    success = Bool("success")
    sup, pen, st, cm = R(P["support_tol"]), R(P["pen_tol"]), R(P["static_tol"]), R(P["comove_tol"])
    rules = {rid: [] for rid in ("R-TIME-01", "R-TIME-02", "R-JNT-01", "R-JNT-02", "R-GRIP-01", "R-GRIP-02",
                                 "R-CONT-01", "R-CONT-02", "R-PERM-01", "R-PERM-02", "R-PERM-03", "R-SUP-01",
                                 "R-SPAT-01", "R-PHASE-01", "R-PHASE-02", "R-PHASE-03", "R-PHASE-04",
                                 "R-PHASE-05", "R-TASK-01")}
    for k in range(N):
        rules["R-JNT-01"] += [And(q[k][j] >= R(ARM["q_lower"][j]), q[k][j] <= R(ARM["q_upper"][j])) for j in range(7)]
        rules["R-GRIP-02"].append(And(w[k] >= 0, w[k] <= APERTURE))
        rules["R-GRIP-01"].append(Implies(c[k], And(cmd[k], _absle(w[k] - R(gw), R(P["grip_width_tol"])))))
        rules["R-SPAT-01"].append(og[k] >= -pen)
        falling = (og[k + 1] < og[k]) if k < N - 1 else BoolVal(False)
        rules["R-SUP-01"].append(Implies(And(Not(c[k]), og[k] > sup), falling))
        rules["R-PHASE-05"] += [Implies(c[k], Or(*[ph[k] == PH[p] for p in CONTACT_PHASES])),
                                Implies(Or(ph[k] == PH["transport"], ph[k] == PH["place"]), c[k])]
    for k in range(N - 1):
        dt = t[k + 1] - t[k]
        d = {n: v[k + 1] - v[k] for n, v in (("ox", ox), ("og", og), ("ex", ex), ("ez", ez))}
        rules["R-TIME-01"].append(dt > 0)
        rules["R-TIME-02"].append(And(dt >= R((1 - P["dt_rel_tol"]) / hz), dt <= R((1 + P["dt_rel_tol"]) / hz)))
        rules["R-JNT-02"] += [_absle(q[k + 1][j] - q[k][j], R(ARM["qd_max"][j]) * dt) for j in range(7)]
        rules["R-PERM-01"] += [_absle(d["ox"], R(P["v_max"]) * dt), _absle(d["og"], R(P["v_max"]) * dt)]
        rules["R-PERM-02"].append(Implies(And(Not(c[k]), Not(c[k + 1]), og[k] <= sup, og[k + 1] <= sup),
                                          And(_absle(d["ox"], st), _absle(d["og"], st))))
        rules["R-PERM-03"].append(Implies(And(c[k], c[k + 1]),
                                          And(_absle(d["ox"] - d["ex"], cm), _absle(d["og"] - d["ez"], cm))))
        rules["R-CONT-01"].append(Implies(And(Not(c[k]), c[k + 1]), And(
            cmd[k + 1], _absle(ex[k + 1] - ox[k + 1], R(P["reach"])),
            _absle(ez[k + 1] - og[k + 1] - R(h / 2), R(P["reach"])))))
        rules["R-CONT-02"].append(Implies(And(c[k], Not(c[k + 1])), Or(Not(cmd[k + 1]), og[k + 1] > sup)))
        rules["R-PHASE-02"].append(rank(ph[k + 1]) >= rank(ph[k]))
        rules["R-PHASE-04"].append(Implies(And(ph[k + 1] == PH["abort"], ph[k] != PH["abort"]),
                                           And(Not(success), Or(ph[k] == PH["grasp"], ph[k] == PH["transport"]))))
    rules["R-PHASE-01"].append(ph[0] == PH["approach"])
    rules["R-PHASE-03"].append(Implies(success, And(ph[-1] == PH["release"], *[
        Or(*[ph[k] == PH[p] for k in range(N)]) for p in PHASES[:5]])))
    rules["R-PHASE-04"] += [ph[0] != PH["abort"], Implies(Not(success), ph[-1] == PH["abort"])]
    rules["R-TASK-01"].append(Implies(success, And(Not(c[-1]), og[-1] <= sup, og[-1] >= -pen,
                                                   _absle(ox[-1] - R(target_x), R(radius)))))
    v = dict(t=t, ph=ph, cmd=cmd, c=c, w=w, ox=ox, og=og, ex=ex, ez=ez, q=q, success=success)
    return v, rules


def self_check(seed_scene: dict) -> dict:
    t0 = time.perf_counter()
    rep = {"rulebook_rules": len(RULES), "object_types": len(VOCAB), "phase_labels": len(PHASES),
           "ground_facts": len(FACTS)}

    # 1. type layer: one object of every class + a manipulated mug, plus property coherence.
    s = Solver()
    s.add(FACTS)
    s.assert_and_track(RULE_TYPE04, "R-TYPE-04")
    objs = {}
    for cls in VOCAB + ("manip_mug",):
        c = Const(f"c_{cls}", ClsSort)
        hx, hn, h = Real(f"hx_{cls}"), Real(f"hn_{cls}"), Real(f"h_{cls}")
        s.add(c == CLS["mug" if cls == "manip_mug" else cls], rule_qty01(hx, hn, h), rule_qty02(c, hx, hn, h))
        if cls == "manip_mug":
            s.add(rule_type02(c, hn))
        objs[cls] = (hx, hn, h)
    res = s.check()
    type_ok = res == sat
    witness = {}
    if type_ok:
        m = s.model()
        for cls, vs in objs.items():
            witness[cls] = [round(float(m.eval(v).as_fraction()), 4) for v in vs]
    n_type_assertions = len(s.assertions())
    rep["type_layer"] = {"result": str(res), "witness_dims_hmax_hmin_height": witness}

    # 2. seed scene 109 (verbatim) against scene axioms.
    objs_seed = seed_scene["objects"]
    scene_findings, notes = [], []
    for o in objs_seed:
        v = check_object(o["name"], o["dimensions"], manipulated=(o["name"] == "mug"))
        scene_findings += [f"{o['name']}:{r}" for r in v]
        gap = o["centroid"]["z"] - o["dimensions"]["height"] / 2 - PHYS["table_z"]
        notes.append(f"{o['name']} bottom gap to table = {gap * 1000:+.1f} mm")
        g = Real("gap")
        scene_findings += [f"{o['name']}:{r}" for r in violated([g == R(gap)], {
            "R-SPAT-01": g >= -R(PHYS["pen_tol"]), "R-SUP-01": g <= R(PHYS["support_tol"])})]
    pa = [np.array([[o["centroid"]["x"], o["centroid"]["y"], o["centroid"]["z"], o["rotations"]["z"]]]) for o in objs_seed]
    da = [(o["dimensions"]["length"], o["dimensions"]["width"], o["dimensions"]["height"]) for o in objs_seed]
    depth = float(box_penetration(pa[0], da[0], pa[1], da[1])[0])
    dz = Real("depth")
    scene_findings += violated([dz == R(depth)], {"R-SPAT-02": dz <= R(PHYS["pen_tol"])})
    notes.append(f"mug-laptop separation = {-depth * 1000:.1f} mm")
    rep["seed_scene_109"] = {"result": "consistent" if not scene_findings else "violations",
                             "violations": scene_findings, "notes": notes}

    # 3. episode layer: bounded symbolic episode must admit a success and a slip failure.
    v, rules = symbolic_episode()
    all_f = [f for fs in rules.values() for f in fs]
    ep = {}
    for name, extra in (("success", [v["success"], v["ox"][-1] - v["ox"][0] >= 0.15, v["og"][0] >= 0, v["og"][0] <= 0.005]),
                        ("slip_failure", [Not(v["success"]), Or(*[And(v["c"][k], Not(v["c"][k + 1]), v["cmd"][k + 1])
                                                                  for k in range(len(v["c"]) - 1)])])):
        s = Solver()
        s.add(FACTS + all_f + extra)
        r = s.check()
        entry = {"result": str(r)}
        if r == sat:
            m = s.model()
            entry["phase_sequence"] = [str(m.eval(p)) for p in v["ph"]]
            entry["contact"] = [int(is_true(m.eval(x))) for x in v["c"]]
            entry["object_x"] = [round(float(m.eval(x).as_fraction()), 3) for x in v["ox"]]
        ep[name] = entry
    rep["episode_layer"] = {"frames": len(v["t"]), "instantiated_axioms": len(all_f), **ep}

    # 4. independence: rule r is not implied by the remaining axioms.
    indep = {}
    for rid, fs in rules.items():
        s = Solver()
        s.add(FACTS + [f for r2, f2 in rules.items() if r2 != rid for f in f2] + [Not(And(*fs))])
        indep[rid] = str(s.check()) == "sat"
    rep["independence"] = {"independent": [r for r, ok in indep.items() if ok],
                           "implied_by_others": [r for r, ok in indep.items() if not ok]}
    rep["total_z3_assertions"] = n_type_assertions + len(FACTS) + len(all_f)
    rep["symbolically_encoded_rules"] = sorted(set(rules) | {"R-QTY-01", "R-QTY-02", "R-TYPE-02", "R-TYPE-04",
                                                             "R-SPAT-02"})
    rep["numeric_only_rules"] = sorted({r for r, *_ in RULES} - set(rep["symbolically_encoded_rules"]))
    ok = type_ok and not scene_findings and all(e["result"] == "sat" for e in ep.values())
    rep["result"] = "SATISFIABLE (rulebook consistent)" if ok else "FAILED"
    rep["seconds"] = round(time.perf_counter() - t0, 3)
    return rep
