#!/usr/bin/env python3
"""One-off and reusable registry hygiene: merge known duplicate groups, align registry slugs to
existing package directories, drop entries flagged as duplicates, and add hand-curated entries.
Run after merge_registry.py --scratch; then run merge_registry.py (no args) to regenerate outputs."""
import json, os, re, datetime, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, "..", "registry"))
APPS = os.path.normpath(os.path.join(HERE, "..", "applications"))
OPP = os.path.join(REG, "opportunities.json")
TODAY = datetime.date.today().isoformat()
sys.path.insert(0, HERE)
from merge_registry import norm, VERDICT_RANK, CONF_RANK, slugify, key

reg = json.load(open(OPP)); E = reg["entries"]

# 1. drop entries a verifier explicitly flagged as duplicates in the name
for k in [k for k, e in E.items() if "[DUPLICATE" in (e.get("name") or "")]:
    print("drop flagged duplicate:", E[k]["name"][:80]); del E[k]

# 2. explicit duplicate groups (name-prefix regexes, case-insensitive); best record survives
GROUPS = [
    r"^kempner institute research fellowship", r"^digital research alliance of canada - (2027 )?resource allocation competition",
    r"^nserc alliance international collaboration grant", r"^branco weiss fellowship", r"^vector (institute )?distinguished postdoctoral",
    r"^vector institute compute", r"^nvidia inception \(startup program\)", r"^harvard innovation labs venture program",
    r"^aws activate", r"^ieee (standards association / ieee ras )?ontologies for robotics", r"^(royal society )?newton international fellowship",
    r"^nrc (industrial research assistance program|irap)", r"^u of t data sciences institute", r"^mitacs accelerate,? postdoctoral",
]
def rank(e):
    has_pkg = os.path.isdir(os.path.join(APPS, e.get("slug", "")))
    return (VERDICT_RANK.get(e.get("verdict"), 0), 1 if e.get("last_checked") == TODAY else 0, CONF_RANK.get(e.get("deadline_confidence"), 0), has_pkg, e.get("fit_score") or 0)
for pat in GROUPS:
    ids = [k for k, e in E.items() if re.match(pat, (e.get("name") or "").lower())]
    if len(ids) < 2: continue
    ids.sort(key=lambda k: rank(E[k]), reverse=True)
    keep = E[ids[0]]
    for d in ids[1:]:
        drop = E[d]
        if os.path.isdir(os.path.join(APPS, drop.get("slug", ""))) and not os.path.isdir(os.path.join(APPS, keep.get("slug", ""))):
            keep["slug"] = drop["slug"]
        keep["sources"] = sorted(set((keep.get("sources") or []) + (drop.get("sources") or [])))
        for f, v in drop.items():
            if f not in keep or keep[f] in (None, "", [], "unknown"): keep[f] = v
        if drop.get("deadline") and drop["deadline"] != keep.get("deadline"):
            keep["cycle_note"] = ((keep.get("cycle_note") or "") + f" | alternative deadline seen: {drop['deadline'][:60]}").strip(" |")
        keep.setdefault("merged_from", []).append(drop.get("name"))
        # keep the best tier of the group
        if (drop.get("tier") or "Z") < (keep.get("tier") or "Z"): keep["tier"] = drop["tier"]
        del E[d]
    print(f"merged {len(ids)-1} into: {keep['name'][:70]}")

# 3. align slugs to existing package directories by token overlap
dirs = [d for d in os.listdir(APPS) if os.path.isdir(os.path.join(APPS, d))]
taken = {e["slug"] for e in E.values()}
for d in dirs:
    if d in taken: continue
    dt = set(re.sub(r"[^a-z0-9]+", " ", d).split()) - {"2027", "2026", "the", "of", "and", "for", "in", "a"}
    best, bs = None, 0
    for k, e in E.items():
        et = set(norm(e.get("name")).split()) | set(re.sub(r"[^a-z0-9]+", " ", e.get("slug", "")).split())
        if not et: continue
        j = len(dt & et) / len(dt | et)
        if j > bs: best, bs = k, j
    if best and bs >= 0.35 and not os.path.isdir(os.path.join(APPS, E[best]["slug"])):
        print(f"slug {E[best]['slug'][:45]} -> {d} (j={bs:.2f})"); E[best]["slug"] = d; taken.add(d)
    else:
        print(f"UNMATCHED package dir: {d} (best j={bs:.2f} -> {E[best]['name'][:50] if best else None})")

# 3b. explicit package-directory assignments (name regex -> directory), overriding token matching
EXPLICIT = {
    r"^vector (institute )?distinguished postdoctoral": "vector-institute-distinguished-postdoctoral-fellowship-spring-2027",
    r"^vector institute compute": None,  # keep its own slug; it is covered by the Vector package
    r"^stanford science fellows": "stanford-science-fellows-2027-cohort",
    r"^mitacs accelerate,? postdoctoral stream": "mitacs-accelerate-postdoctoral-fellowship-stream",
    r"^nrc irap": "nrc-irap-financial-support-for-technology-innovation",
    r"^activate fellowship": "activate-fellowship-2027",
    r"^kempner institute research fellowship": "kempner-institute-research-fellowship-2027-cohort",
    r"^canada postdoctoral research award \(cpra\) - nserc": "canada-postdoctoral-research-award-cpra-nserc-stream-2026-competition",
    r"^eric and wendy schmidt ai in science": "eric-and-wendy-schmidt-ai-in-science-postdoctoral-fellowship-u-of-t",
    r"^(cornell )?klarman fellowships": "klarman-fellowships-2027-cohort",
    r"^u of t data sciences institute \(dsi\) postdoctoral": "u-of-t-data-sciences-institute-dsi-postdoctoral-fellowship-2027-call",
    r"^canada impact\+ research training awards": "canada-impact-research-training-awards-cirta-postdoctoral-2027-cycle",
    r"^princeton presidential postdoctoral": "princeton-presidential-postdoctoral-research-fellows-program",
    r"^harvard innovation labs venture program": "harvard-innovation-labs-venture-program-i-lab-president-s-innovation-c",
    r"^branco weiss fellowship": "branco-weiss-fellowship-society-in-science-2027",
    r"^university of toronto mie": "university-of-toronto-mie-assistant-professor-industrial-engineering-i",
    r"^cra trustworthy ai": "cra-trustworthy-ai-research-fellowship-for-early-career-scholars-2027-",
    r"^harvard data science initiative \(hdsi\) postdoctoral": "harvard-data-science-initiative-hdsi-postdoctoral-fellows-program",
    r"^tiap critical technologies": "tiap-critical-technologies-initiative-ai-quantum-robotics-ventures",
    r"^nserc alliance international collaboration grant": "nserc-alliance-international-collaboration-grant-u-of-t-x-harvard-us-r",
    r"^digital research alliance of canada - (2027 )?resource allocation": "digital-research-alliance-of-canada-resource-allocation-competition-ra",
    r"^mitacs accelerate global excellence": "mitacs-accelerate-global-excellence-award-postdoctoral",
    r"^creative destruction lab": "creative-destruction-lab-toronto-ai-stream-2027",
    r"^alexander von humboldt research fellowship": "alexander-von-humboldt-research-fellowship-postdoctoral",
    r"^harvard society of fellows": "harvard-society-of-fellows-junior-fellowship-2028",
    r"^(royal society )?newton international": "royal-society-newton-international-fellowship-2027",
    r"^aria programme calls": "aria-opportunity-seeds-and-programme-calls",
    r"^amazon research awards": "amazon-research-awards-fall-2026-robotics",
}
for pat, d in EXPLICIT.items():
    for e in E.values():
        if re.match(pat, (e.get("name") or "").lower()):
            if d is None:
                if os.path.isdir(os.path.join(APPS, e.get("slug", ""))) and e["slug"] in EXPLICIT.values(): e["slug"] = slugify(e) + "-compute"
            else:
                e["slug"] = d
# 3c. bundle coverage: entries served by a bundled package get a `bundle` field the tracker links to
BUNDLES = {
    "compute-and-data-access-bundle": [r"nvidia inception", r"nvidia isaac", r"harvard institutional compute", r"aws cloud credit for research", r"google cloud research credits", r"dataset access licences", r"nsf access allocations", r"hugging face lerobot", r"nairr pilot", r"digital research alliance of canada - rapid access", r"nvidia academic grant", r"google for startups", r"aws activate", r"maniskill / sapien", r"vector institute compute", r"google tpu research cloud"],
    "standards-participation-bundle": [r"iso/iec jtc 1/sc 42", r"ieee (standards association / ieee ras )?ontologies for robotics", r"standards council of canada", r"iaoa community programs"],
    "canada-company-nondilutive-bundle": [r"^sr&ed", r"^mitacs accelerate \(axiomality", r"^nserc alliance advantage", r"^scale ai", r"^digital global innovation cluster", r"^oci ", r"^intellectual property ontario", r"^utest", r"^vector institute fastlane", r"^innovative solutions canada", r"^ai compute access fund", r"^canexport", r"^elevateip", r"^nrc irap youth", r"^communitech", r"^lab2market"],
}
for b, pats in BUNDLES.items():
    for e in E.values():
        n = (e.get("name") or "").lower()
        if any(re.search(pt, n) for pt in pats) and not os.path.isdir(os.path.join(APPS, e.get("slug", ""))):
            e["bundle"] = b

# 4. hand-curated additions (from the completeness review; unverified until checked on the official page)
ADD = [
 {"name": "UC President's Postdoctoral Fellowship Program (PPFP) 2027-28", "funder": "University of California, Office of the President", "url": "https://ppfp.ucop.edu/ppfp/", "country": "United States", "type": "postdoc_fellowship", "applicant_entity": "individual", "deadline": "2026-11-01 (expected; annual 1 Nov pattern — unverified)", "deadline_confidence": "medium", "amount": "USD ~70,000-80,000 salary plus benefits and research/travel (confirm)", "duration": "1-2 years", "eligibility_summary": "Any nationality; PhD by the start date; requires a UC faculty mentor (e.g., UCSD Hao Su lab for SAPIEN/PartNet-Mobility, Berkeley BAIR); emphasizes contributions to diversity and equal opportunity. Added from the completeness review; not scouted or verified in this run.", "eligibility_flags": ["unverified — check 2027-28 dates and criteria on ppfp.ucop.edu", "needs a UC faculty mentor by mid-October", "Sept 2027 start conflicts with a spring-2027 Toronto award"], "tier": "B", "fit_score": 64, "verdict": "unverifiable", "category": "us_top_university_postdocs", "next_actions": ["Confirm 2027-28 deadline and whether a mentor letter is due at submission", "Email a UCSD/Berkeley mentor candidate by 10 Oct 2026 if the US fork is chosen"], "sources": ["https://ppfp.ucop.edu/ppfp/"], "estimated_prep_days": 6},
 {"name": "Google TPU Research Cloud (TRC) — free TPU access for researchers", "funder": "Google", "url": "https://sites.research.google/trc/about/", "country": "United States / global", "type": "compute_or_credits", "applicant_entity": "individual", "deadline": "rolling", "deadline_confidence": "high", "amount": "Free access to Cloud TPUs (quota-based; egress/storage may be charged) for a period, renewable", "duration": "typically 30 days, renewable", "eligibility_summary": "Researchers who agree to share results publicly; short application form. Added from the completeness review; belongs with the compute-and-data-access bundle (JAX/TPU port of O3 training required).", "eligibility_flags": ["O3 policy training is PyTorch/SAPIEN-based; TPU use requires a JAX port or TPU-compatible stack"], "tier": "B", "fit_score": 55, "verdict": "unverifiable", "category": "compute_data_credits", "next_actions": ["Apply only if a TPU-compatible training stack is planned"], "sources": ["https://sites.research.google/trc/about/"], "estimated_prep_days": 1},
]
for rec in ADD:
    k = key(rec); rec["id"] = k; rec["slug"] = slugify(rec); rec["first_seen"] = TODAY; rec["last_checked"] = TODAY
    if k not in E: E[k] = rec; print("added:", rec["name"][:60])

reg["generated"] = TODAY
json.dump(reg, open(OPP, "w"), indent=1, ensure_ascii=False)
print("entries:", len(E))
