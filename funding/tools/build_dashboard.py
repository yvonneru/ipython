#!/usr/bin/env python3
"""Generate funding/registry/dashboard.html from opportunities.json (tier A/B), the package
directories and the next-10-days checklist. Self-contained HTML; safe to republish as an artifact."""
import json, os, re, datetime, html
HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, "..", "registry"))
APPS = os.path.normpath(os.path.join(HERE, "..", "applications"))
OUT = os.path.join(REG, "dashboard.html")
TODAY = datetime.date.today()

def parse_date(d):
    m = re.match(r"(20\d{2})-(\d{2})-(\d{2})", d or "")
    if not m: return None
    try: return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError: return None

reg = json.load(open(os.path.join(REG, "opportunities.json")))
E = [e for e in reg["entries"].values() if e.get("tier") in ("A", "B")]
pkgs = {d for d in os.listdir(APPS) if os.path.isdir(os.path.join(APPS, d))}
def pkg_of(e):
    if e.get("slug") in pkgs: return e["slug"]
    if e.get("bundle") in pkgs: return e["bundle"]
    return None
rows = []
for e in E:
    d = parse_date(e.get("deadline"))
    rows.append({
        "name": e.get("name", ""), "funder": e.get("funder", ""), "url": e.get("url", ""),
        "tier": e.get("tier"), "fit": e.get("fit_score") or 0, "entity": e.get("applicant_entity") or "",
        "deadline": (e.get("deadline") or "")[:60], "date": d.isoformat() if d else None,
        "days": (d - TODAY).days if d else None, "conf": (e.get("deadline_confidence") or "low"),
        "amount": (e.get("amount") or "")[:90], "pkg": pkg_of(e), "type": e.get("type") or "",
        "flags": (e.get("eligibility_flags") or e.get("risks_and_flags") or [])[:2],
        "actions": (e.get("next_actions") or [])[:2],
        "verdict": e.get("verdict") or "",
    })
rows.sort(key=lambda r: (r["date"] is None, r["date"] or "9999", -r["fit"]))
dated = [r for r in rows if r["date"] and r["days"] is not None and r["days"] >= 0]
rolling = [r for r in rows if not r["date"] or (r["days"] is not None and r["days"] < 0)]
n_pkgs = len([d for d in pkgs])
n30 = len([r for r in dated if r["days"] <= 30])

CHECKLIST = [
    ("2026-09-26", "Kempner go/no-go (deadline 1 Oct, 6 pm ET). Default: no. Go only if two Kempner mentors and three referees confirm today."),
    ("2026-09-26", "Record citizenship / immigration status; locate the proof-of-status document for CPRA; check the PhD conferral date (Klarman needs on or after 1 May 2025)."),
    ("2026-09-28", "Prof. Grüninger's yes/no on supervising from spring 2027 and on the Schmidt AI in Science co-supervision. Schmidt go/no-go."),
    ("2026-09-30", "If Schmidt is a go: package to Grüninger; one consolidated letter request to each referee (Schmidt + CPRA text boxes)."),
    ("2026-10-02", "CPRA full draft (2-page outline, 4-page statements, Form 201 texts) to Grüninger and referees. Ask him in the same message for the REPFP nomination, RAC 2027 PI role and Alliance International."),
    ("2026-10-03", "Record AXIOMALITY's legal entity and country/province of incorporation (decides the Canadian company stack). Request the HMS O2 compute account."),
    ("2026-10-05", "Schmidt AI in Science deadline, 5 pm ET (only if go)."),
    ("2026-10-09", "CPRA referee reports in the NSERC system. Order the transcript and the SGS requirements-met letter if the transcript shows only conferral."),
    ("2026-10-15", "AWS Cloud Credit for Research and NSF ACCESS Explore requests filed. Klarman (15 Oct) only with a committed Cornell host."),
    ("2026-10-14", "Submit CPRA after running Verify in the portal. Deadline Saturday 17 Oct, 8 pm ET (NSERC moves weekend deadlines to Monday; do not rely on it)."),
]
DECIDERS = [
    ("Citizenship / immigration status", "Decides the CPRA proof-of-status document, work-permit lead times for a Toronto start, NAIRR and DOE resources, Fulbright-type programs. Needed by 26 Sept."),
    ("AXIOMALITY legal entity and incorporation", "Decides IRAP, SR&ED, TIAP, Vector FastLane, Scale AI, DIGITAL, Mitacs partner status, SBIR/STTR. Needed by 3 Oct."),
    ("Spring 2027 Toronto vs Sept 2027 US start", "CPRA, Vector, DSI, REPFP and CIRTA cannot be combined with Kempner, Klarman, Stanford, Princeton, UC PPFP or Activate. Choose the fork before asking referees."),
    ("Prof. Grüninger's agreement", "Supervisor for CPRA, Schmidt, Vector co-sponsor, REPFP nominator; PI for RAC 2027, Alliance International, Alliance Advantage, Amazon Research Awards."),
]

def esc(s): return html.escape(str(s or ""))
def days_chip(r):
    if r["days"] is None: return '<span class="chip rolling">rolling</span>'
    d = r["days"]
    cls = "due" if d <= 7 else "soon" if d <= 30 else "later"
    label = "today" if d == 0 else f"{d} d"
    return f'<span class="chip {cls}">{label}</span>'
def row_html(r):
    pkg = f'<span class="pkg" title="funding/applications/{esc(r["pkg"])}">package ready</span>' if r["pkg"] else '<span class="pkg none">no package</span>'
    flags = "".join(f"<li>{esc(f)}</li>" for f in r["flags"])
    acts = "".join(f"<li>{esc(a)}</li>" for a in r["actions"])
    name = f'<a href="{esc(r["url"])}" target="_blank" rel="noopener">{esc(r["name"])}</a>' if r["url"].startswith("http") else esc(r["name"])
    return f'''<article class="row" data-tier="{r["tier"]}" data-entity="{esc(r["entity"])}" data-text="{esc((r["name"]+" "+r["funder"]+" "+r["type"]).lower())}">
  <div class="when"><div class="date">{esc(r["date"] or r["deadline"][:24])}</div>{days_chip(r)}<div class="conf">conf. {esc(r["conf"])}</div></div>
  <div class="what"><h3>{name}</h3><div class="funder">{esc(r["funder"])}</div>
    <div class="meta"><span class="tier t{r["tier"]}">Tier {r["tier"]}</span><span class="fit">fit {r["fit"]}</span><span class="entity">{esc(r["entity"])}</span>{pkg}</div>
    <div class="amount">{esc(r["amount"])}</div>
    <details><summary>flags and next actions</summary><ul class="flags">{flags}</ul><ul class="acts">{acts}</ul></details>
  </div></article>'''

page = f'''<title>Ru Funding Radar</title>
<meta name="description" content="Deadline radar for Dr. Yi Ru and AXIOMALITY: every tier A/B funding opportunity, days left, package status, and the next ten working days.">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root {{ --bg:#F6F8F7; --surface:#FFFFFF; --ink:#18211F; --muted:#5C6B67; --line:#D9E1DE; --accent:#0E6B63; --accent-ink:#FFFFFF; --due:#A63A2C; --soon:#9A6A11; --later:#3B6E68; --chip-bg:#EEF3F1; --tierA:#0E6B63; --tierB:#4A5D9A; --pkg:#1F6B3A; color-scheme: light; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#0F1614; --surface:#172220; --ink:#E7ECEA; --muted:#9BABA5; --line:#2A3835; --accent:#5CC0B4; --accent-ink:#0F1614; --due:#F08A7A; --soon:#E2B15C; --later:#7CC7BE; --chip-bg:#1F2C29; --tierA:#5CC0B4; --tierB:#9FB0E8; --pkg:#7ED39A; color-scheme: dark; }} }}
:root[data-theme="dark"] {{ --bg:#0F1614; --surface:#172220; --ink:#E7ECEA; --muted:#9BABA5; --line:#2A3835; --accent:#5CC0B4; --accent-ink:#0F1614; --due:#F08A7A; --soon:#E2B15C; --later:#7CC7BE; --chip-bg:#1F2C29; --tierA:#5CC0B4; --tierB:#9FB0E8; --pkg:#7ED39A; color-scheme: dark; }}
body {{ background:var(--bg); color:var(--ink); font-family:"IBM Plex Sans", system-ui, sans-serif; font-size:15px; line-height:1.5; padding-inline:16px; padding-block:24px 48px; }}
.wrap {{ max-width:1080px; margin:0 auto; display:grid; gap:28px; }}
h1,h2,h3 {{ font-family:"Source Serif 4", Georgia, serif; font-weight:600; text-wrap:balance; margin:0; }}
h1 {{ font-size:clamp(28px,4vw,40px); line-height:1.1; }}
h2 {{ font-size:22px; margin-bottom:12px; }}
h3 {{ font-size:17px; line-height:1.3; }}
h3 a {{ color:inherit; text-decoration:none; border-bottom:1px solid var(--line); }}
h3 a:hover, h3 a:focus {{ border-bottom-color:var(--accent); }}
.sub {{ color:var(--muted); max-width:65ch; }}
.eyebrow {{ font-family:"IBM Plex Mono", ui-monospace, monospace; font-size:12px; letter-spacing:.08em; text-transform:uppercase; color:var(--accent); }}
.stats {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; }}
.stat {{ background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:14px 16px; }}
.stat .n {{ font-family:"IBM Plex Mono", ui-monospace, monospace; font-size:30px; font-variant-numeric:tabular-nums; line-height:1; color:var(--accent); }}
.stat .l {{ color:var(--muted); font-size:13px; margin-top:6px; }}
.controls {{ display:flex; flex-wrap:wrap; gap:8px; align-items:center; }}
.controls input {{ flex:1 1 220px; padding:8px 10px; border:1px solid var(--line); border-radius:6px; background:var(--surface); color:var(--ink); font:inherit; }}
.controls button {{ padding:7px 12px; border:1px solid var(--line); border-radius:999px; background:var(--surface); color:var(--ink); font:inherit; font-size:13px; cursor:pointer; }}
.controls button[aria-pressed="true"] {{ background:var(--accent); color:var(--accent-ink); border-color:var(--accent); }}
.controls button:focus-visible, .controls input:focus-visible, details summary:focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; }}
.list {{ display:grid; gap:10px; }}
.row {{ display:grid; grid-template-columns:150px 1fr; gap:14px; background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:14px 16px; }}
.row[hidden] {{ display:none; }}
.when {{ display:grid; gap:6px; align-content:start; }}
.date {{ font-family:"IBM Plex Mono", ui-monospace, monospace; font-variant-numeric:tabular-nums; font-size:15px; font-weight:500; }}
.conf {{ color:var(--muted); font-size:12px; }}
.chip {{ display:inline-block; font-family:"IBM Plex Mono", ui-monospace, monospace; font-size:12px; padding:2px 8px; border-radius:999px; background:var(--chip-bg); color:var(--later); width:max-content; }}
.chip.due {{ color:var(--due); font-weight:500; }} .chip.soon {{ color:var(--soon); }} .chip.rolling {{ color:var(--muted); }}
.funder {{ color:var(--muted); font-size:13px; }}
.meta {{ display:flex; flex-wrap:wrap; gap:8px; align-items:center; margin-top:8px; font-size:13px; }}
.tier {{ font-family:"IBM Plex Mono", ui-monospace, monospace; font-size:12px; padding:1px 7px; border-radius:4px; border:1px solid currentColor; }}
.tA {{ color:var(--tierA); }} .tB {{ color:var(--tierB); }}
.fit, .entity {{ color:var(--muted); }}
.pkg {{ color:var(--pkg); font-weight:500; }} .pkg.none {{ color:var(--muted); font-weight:400; }}
.amount {{ margin-top:6px; font-size:13px; }}
details {{ margin-top:8px; font-size:13px; }} summary {{ cursor:pointer; color:var(--accent); }}
details ul {{ margin:6px 0 0 18px; padding:0; }} .acts li {{ color:var(--ink); }} .flags li {{ color:var(--muted); }}
.check {{ display:grid; gap:8px; padding:0; margin:0; }}
.check li {{ display:grid; grid-template-columns:110px 1fr; gap:12px; background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:10px 14px; list-style:none; }}
.check .d {{ font-family:"IBM Plex Mono", ui-monospace, monospace; font-variant-numeric:tabular-nums; font-size:13px; color:var(--accent); }}
.deciders {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:12px; }}
.deciders div {{ border-left:3px solid var(--accent); padding:4px 12px; }}
.deciders b {{ display:block; margin-bottom:4px; }}
.note {{ color:var(--muted); font-size:13px; max-width:70ch; }}
@media (max-width:560px) {{ .row {{ grid-template-columns:1fr; }} .check li {{ grid-template-columns:1fr; }} }}
@media (prefers-reduced-motion: no-preference) {{ .row {{ transition: border-color .15s; }} }}
</style>
<div class="wrap">
  <header>
    <div class="eyebrow">Funding radar · generated {TODAY.isoformat()}</div>
    <h1>Ru Funding Radar</h1>
    <p class="sub">Every tier A and B opportunity for Dr. Yi Ru and AXIOMALITY from the registry, sorted by deadline, with days left, confidence and package status. Dates come from search results and must be confirmed on the official page before you rely on them. NSERC-style deadlines close at 8 pm ET.</p>
  </header>
  <section class="stats">
    <div class="stat"><div class="n">{len([r for r in rows if r["tier"]=="A"])}</div><div class="l">tier A (prepare now)</div></div>
    <div class="stat"><div class="n">{len([r for r in rows if r["tier"]=="B"])}</div><div class="l">tier B (this cycle, dependencies first)</div></div>
    <div class="stat"><div class="n">{n30}</div><div class="l">dated deadlines in the next 30 days</div></div>
    <div class="stat"><div class="n">{n_pkgs}</div><div class="l">application packages drafted</div></div>
  </section>
  <section>
    <div class="eyebrow">Next ten working days</div>
    <h2>What to do first</h2>
    <ul class="check">{"".join(f'<li><span class="d">{esc(d)}</span><span>{esc(t)}</span></li>' for d,t in CHECKLIST)}</ul>
  </section>
  <section>
    <div class="eyebrow">Two facts and two choices</div>
    <h2>What decides the portfolio</h2>
    <div class="deciders">{"".join(f'<div><b>{esc(a)}</b><span class="note">{esc(b)}</span></div>' for a,b in DECIDERS)}</div>
  </section>
  <section>
    <div class="eyebrow">Dated deadlines</div>
    <h2>Deadline timeline</h2>
    <div class="controls">
      <input id="q" type="search" placeholder="filter by name, funder or type" aria-label="filter">
      <button id="fA" aria-pressed="true">Tier A</button><button id="fB" aria-pressed="true">Tier B</button>
      <button id="fI" aria-pressed="true">individual</button><button id="fC" aria-pressed="true">company / institution</button>
    </div>
    <div class="list" id="dated">{"".join(row_html(r) for r in dated)}</div>
  </section>
  <section>
    <div class="eyebrow">Rolling and undated</div>
    <h2>Continuous intake, compute and standards</h2>
    <p class="note">Rolling programs and those whose next date is not published. Compute, standards and Canadian company programs are covered by the three bundles under funding/applications.</p>
    <div class="list" id="rolling">{"".join(row_html(r) for r in rolling)}</div>
  </section>
  <p class="note">Source: funding/registry/opportunities.json on branch claude/funding-agent-opportunities-q4a84z. Regenerate with python3 funding/tools/build_dashboard.py.</p>
</div>
<script>
(function(){{
  var q=document.getElementById('q'), b={{A:document.getElementById('fA'),B:document.getElementById('fB'),I:document.getElementById('fI'),C:document.getElementById('fC')}};
  var rows=Array.prototype.slice.call(document.querySelectorAll('.row'));
  function on(el){{return el.getAttribute('aria-pressed')==='true';}}
  function apply(){{
    var t=(q.value||'').toLowerCase();
    rows.forEach(function(r){{
      var tier=r.getAttribute('data-tier'), ent=r.getAttribute('data-entity')||'';
      var okT=(tier==='A'&&on(b.A))||(tier==='B'&&on(b.B));
      var isInd=ent==='individual'||ent==='either', isCo=ent!=='individual';
      var okE=(isInd&&on(b.I))||(isCo&&on(b.C));
      var okQ=!t||(r.getAttribute('data-text')||'').indexOf(t)>=0;
      r.hidden=!(okT&&okE&&okQ);
    }});
  }}
  Object.keys(b).forEach(function(k){{ b[k].addEventListener('click',function(){{ b[k].setAttribute('aria-pressed', on(b[k])?'false':'true'); apply(); }}); }});
  q.addEventListener('input',apply);
  try {{ var s=localStorage.getItem('radar-q'); if(s) {{ q.value=s; apply(); }} q.addEventListener('input',function(){{ try{{localStorage.setItem('radar-q',q.value);}}catch(e){{}} }}); }} catch(e) {{}}
}})();
</script>
'''
open(OUT, "w").write(page)
print(f"wrote {OUT}: {len(rows)} A/B rows ({len(dated)} dated, {len(rolling)} rolling), {n_pkgs} packages, {len(page)//1024} KB")


# ---- applications/INDEX.md: one line per package, sorted by deadline ----
def _pkg_index():
    lines = ["# Application packages", "", f"Generated {TODAY.isoformat()} by tools/build_dashboard.py. One directory per opportunity (or bundle); each README.md has the deadline table, eligibility status, checklist, criteria mapping, open [bracketed] items and, once critiqued, a Review log.", "",
             "| Deadline | Days | Tier | Package | Funder | Reviewed |", "|---|---|---|---|---|---|"]
    by_dir = {}
    for e in reg["entries"].values():
        for d in (e.get("slug"), e.get("bundle")):
            if d in pkgs:
                cur = by_dir.get(d)
                if cur is None or (e.get("tier") or "Z") < (cur.get("tier") or "Z"): by_dir[d] = e
    items = []
    for d in sorted(pkgs):
        e = by_dir.get(d, {})
        dt = parse_date(e.get("deadline")) if e else None
        reviewed = "yes" if "## Review log" in open(os.path.join(APPS, d, "README.md")).read() else "no" if os.path.exists(os.path.join(APPS, d, "README.md")) else "-"
        items.append((dt or datetime.date(2999,1,1), d, e, dt, reviewed))
    for _, d, e, dt, reviewed in sorted(items):
        days = str((dt - TODAY).days) if dt else "rolling"
        name = e.get("name", d) if not d.endswith("bundle") else d.replace("-", " ").capitalize()
        lines.append(f"| {dt.isoformat() if dt else (e.get('deadline') or '')[:40]} | {days} | {e.get('tier','')} | [{name[:80]}]({d}/README.md) | {(e.get('funder') or '')[:60]} | {reviewed} |")
    open(os.path.join(APPS, "INDEX.md"), "w").write("\n".join(lines) + "\n")
    print(f"wrote {os.path.join(APPS, 'INDEX.md')}: {len(items)} packages")
_pkg_index()
