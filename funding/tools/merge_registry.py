#!/usr/bin/env python3
"""Merge scout/verifier JSON output into funding/registry/opportunities.json and
regenerate TRACKER.md and deadlines.ics.

Usage:
  python3 funding/tools/merge_registry.py --scratch <dir>   # merge new scout_*.json / verified_*.json
  python3 funding/tools/merge_registry.py                   # just regenerate TRACKER.md and deadlines.ics

Rules: verified records override scouted ones; entries are keyed by a normalized
name+funder; nothing is ever deleted (an entry that disappears keeps its last state).
"""
import argparse, glob, json, os, re, sys, datetime, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, "..", "registry"))
OPP = os.path.join(REG, "opportunities.json")
TRACKER = os.path.join(REG, "TRACKER.md")
ICS = os.path.join(REG, "deadlines.ics")
TODAY = datetime.date.today().isoformat()

TIER_ORDER = {"A": 0, "B": 1, "C": 2, "D": 3, None: 4, "": 4}

def norm(s):
    s = (s or "").lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    stop = {"the", "of", "for", "and", "a", "an", "in", "program", "programme", "award", "awards", "fellowship", "fellowships", "grant", "grants", "2026", "2027", "cycle", "competition"}
    return " ".join(w for w in s.split() if w not in stop)

def key(rec):
    return hashlib.sha1((norm(rec.get("name")) + "|" + norm(rec.get("funder"))).encode()).hexdigest()[:12]

def slugify(rec):
    s = re.sub(r"[^a-z0-9]+", "-", (rec.get("name") or "").lower()).strip("-")
    return s[:70] or key(rec)

def load_registry():
    if os.path.exists(OPP):
        with open(OPP) as f:
            return json.load(f)
    return {"generated": TODAY, "entries": {}}

def merge(reg, scratch):
    entries = reg["entries"]
    n_scout = n_ver = 0
    for path in sorted(glob.glob(os.path.join(scratch, "scout_*.json"))):
        cat = os.path.basename(path)[len("scout_"):-len(".json")]
        try:
            data = json.load(open(path))
        except Exception as e:
            print(f"skip {path}: {e}", file=sys.stderr); continue
        for rec in data.get("opportunities", []):
            k = key(rec)
            rec = dict(rec); rec["category"] = cat; rec.setdefault("tier", None); rec.setdefault("verdict", "scouted")
            if k not in entries:
                rec["id"] = k; rec["slug"] = slugify(rec); rec["first_seen"] = TODAY
                entries[k] = rec; n_scout += 1
            else:
                cur = entries[k]
                for f, v in rec.items():
                    if f not in cur or cur[f] in (None, "", [], "unknown"):
                        cur[f] = v
    for path in sorted(glob.glob(os.path.join(scratch, "verified_*.json"))):
        base = os.path.basename(path)[len("verified_"):-len(".json")]
        cat = re.sub(r"_\d+$", "", base)
        try:
            data = json.load(open(path))
        except Exception as e:
            print(f"skip {path}: {e}", file=sys.stderr); continue
        for rec in data.get("verified", []):
            k = key(rec)
            rec = dict(rec); rec["category"] = cat; rec["last_checked"] = TODAY
            if k in entries:
                cur = entries[k]
                cur.update({f: v for f, v in rec.items() if v not in (None, "", [])})
            else:
                rec["id"] = k; rec["slug"] = slugify(rec); rec["first_seen"] = TODAY
                entries[k] = rec
            n_ver += 1
    reg["generated"] = TODAY
    print(f"merged {n_scout} new scouted, {n_ver} verified records; registry now has {len(entries)} entries")
    return reg


CONF_RANK = {"high": 3, "medium": 2, "low": 1, None: 0, "": 0}
VERDICT_RANK = {"confirmed": 4, "corrected": 4, "closed_for_cycle": 3, "ineligible": 3, "discontinued": 3, "unverifiable": 2, "scouted": 1, None: 0}

def _tokens(rec):
    return set(norm(rec.get("name")).split())

def coalesce(reg, threshold=0.6):
    """Merge near-duplicate entries (same funder tokens overlap and name Jaccard >= threshold).
    The record with the stronger verdict / deadline confidence survives; sources are unioned;
    the surviving slug is the one that already has a package directory, if any."""
    entries = reg["entries"]
    ids = list(entries.keys())
    dropped = set()
    for i, a in enumerate(ids):
        if a in dropped: continue
        for b in ids[i+1:]:
            if b in dropped: continue
            ra, rb = entries[a], entries[b]
            fa, fb = set(norm(ra.get("funder")).split()), set(norm(rb.get("funder")).split())
            if fa and fb and not (fa & fb): continue
            ta, tb = _tokens(ra), _tokens(rb)
            if not ta or not tb: continue
            j = len(ta & tb) / len(ta | tb)
            if j < threshold: continue
            def rank(r): return (VERDICT_RANK.get(r.get("verdict"), 0), CONF_RANK.get(r.get("deadline_confidence"), 0), r.get("fit_score") or 0)
            keep, drop = (ra, rb) if rank(ra) >= rank(rb) else (rb, ra)
            keep_id, drop_id = (a, b) if keep is ra else (b, a)
            app_dir = os.path.join(REG, "..", "applications")
            if os.path.isdir(os.path.join(app_dir, drop["slug"])) and not os.path.isdir(os.path.join(app_dir, keep["slug"])):
                keep["slug"] = drop["slug"]
            keep["sources"] = sorted(set((keep.get("sources") or []) + (drop.get("sources") or [])))
            for f, v in drop.items():
                if f not in keep or keep[f] in (None, "", [], "unknown"):
                    keep[f] = v
            alt = drop.get("deadline")
            if alt and alt != keep.get("deadline"):
                keep["cycle_note"] = ((keep.get("cycle_note") or "") + f" | alternative deadline seen: {alt} ({drop.get('deadline_confidence')})").strip(" |")
            keep.setdefault("merged_from", []).append(drop.get("name"))
            dropped.add(drop_id)
    for d in dropped: del entries[d]
    if dropped: print(f"coalesced {len(dropped)} near-duplicate entries")
    return reg

def parse_date(d):
    if not d: return None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", d)
    if m: return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.search(r"(\d{4})-(\d{2})", d)
    if m: return datetime.date(int(m.group(1)), int(m.group(2)), 28)
    return None

def sort_key(rec):
    d = parse_date(rec.get("deadline"))
    return (TIER_ORDER.get(rec.get("tier"), 4), d or datetime.date(2999, 1, 1), -(rec.get("fit_score") or 0))

def write_tracker(reg):
    entries = sorted(reg["entries"].values(), key=sort_key)
    lines = [f"# Funding tracker — Dr. Yi Ru / AXIOMALITY", "", f"Generated {reg['generated']} from `opportunities.json` ({len(entries)} entries). Tiers: A = prepare now; B = this cycle after securing a sponsor/nominator or 6–15 months out; C = monitor; D = ineligible / not worth it. Deadline confidence: H/M/L. Verify every date on the official page before relying on it.", ""]
    for tier in ["A", "B", "C", "D", None]:
        group = [e for e in entries if (e.get("tier") or None) == tier]
        if not group: continue
        title = {"A": "Tier A — prepare now", "B": "Tier B — this cycle, dependencies first", "C": "Tier C — monitor", "D": "Tier D — ineligible or deprioritized", None: "Unverified (scouted only)"}[tier]
        lines += [f"## {title} ({len(group)})", "", "| Deadline | Conf | Opportunity | Funder | Country | Type | Amount | Fit | Entity | Flags | Package |", "|---|---|---|---|---|---|---|---|---|---|---|"]
        for e in group:
            flags = "; ".join((e.get("eligibility_flags") or e.get("risks_and_flags") or [])[:3])
            pkg = f"[pkg](../applications/{e['slug']}/README.md)" if os.path.isdir(os.path.join(REG, "..", "applications", e["slug"])) else ""
            url = e.get("url") or ""
            name = f"[{e.get('name','')}]({url})" if url else e.get("name", "")
            lines.append(f"| {e.get('deadline','')} | {(e.get('deadline_confidence') or '?')[:1].upper()} | {name} | {e.get('funder','')} | {e.get('country','')} | {e.get('type','')} | {e.get('amount','')} | {e.get('fit_score','')} | {e.get('applicant_entity','')} | {flags} | {pkg} |")
        lines.append("")
    with open(TRACKER, "w") as f:
        f.write("\n".join(lines).replace("\n\n\n", "\n\n"))
    print(f"wrote {TRACKER}")

def write_ics(reg):
    out = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//funding-agents//deadlines//EN", "CALSCALE:GREGORIAN"]
    for e in reg["entries"].values():
        if e.get("tier") not in ("A", "B"): continue
        d = parse_date(e.get("deadline"))
        if not d: continue
        uid = e["id"] + "@funding-agents"
        summ = f"DEADLINE: {e.get('name')} ({e.get('funder')})"
        desc = f"Tier {e.get('tier')} | conf {e.get('deadline_confidence')} | {e.get('amount','')} | {e.get('url','')}"
        out += ["BEGIN:VEVENT", f"UID:{uid}", f"DTSTAMP:{TODAY.replace('-','')}T000000Z", f"DTSTART;VALUE=DATE:{d.isoformat().replace('-','')}", f"SUMMARY:{summ}", f"DESCRIPTION:{desc}", "BEGIN:VALARM", "TRIGGER:-P14D", "ACTION:DISPLAY", f"DESCRIPTION:14 days to {e.get('name')}", "END:VALARM", "END:VEVENT"]
    out.append("END:VCALENDAR")
    with open(ICS, "w") as f:
        f.write("\r\n".join(out) + "\r\n")
    print(f"wrote {ICS}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--scratch", help="directory containing scout_*.json and verified_*.json")
    a = ap.parse_args()
    reg = load_registry()
    if a.scratch:
        reg = merge(reg, a.scratch)
        reg = coalesce(reg)
        with open(OPP, "w") as f:
            json.dump(reg, f, indent=1, ensure_ascii=False)
        print(f"wrote {OPP}")
    write_tracker(reg)
    write_ics(reg)
