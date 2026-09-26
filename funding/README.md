# Funding agents for Dr. Yi Ru / AXIOMALITY

A self-contained agent system that finds, verifies, tiers, drafts and tracks funding applications: postdoctoral fellowships (Canada, US, international), research grants, faculty and society-of-fellows positions, non-dilutive and accelerator funding for AXIOMALITY, compute credits, and prizes. Built 2026-09-25 from the CV, the AXIOMALITY decks, Prof. Michael Grüninger's NSERC proposals (the style template), and the existing CPRA / Vector / DSI / CIRTA drafts.

The agents do everything up to the point of submission. They cannot press "submit" on a funder's portal, sign on behalf of the applicant, or answer the facts only the applicant knows (citizenship, company incorporation, thesis title, exact patent numbers). Those facts are marked `[in brackets]` everywhere and are listed per package in each `README.md`.

## Layout

```
funding/
  README.md                 this file
  STRATEGY.md               portfolio, sequencing, dependencies (written by portfolio-strategist); the Addendum at the end overrides the body
  COMPLETENESS_REVIEW.md    51 findings from the completeness critic (5 blockers) and the ranked list of applicant-only questions
  profile/                  ground truth about the applicant, the research program, the company
  templates/                Grüninger NSERC proposals + a digest of their structure and voice
  source_drafts/            the drafts that already existed (CPRA, Vector, DSI, CIRTA, emails)
  registry/
    categories.json         the 16 search categories with seed programs
    opportunities.json      the registry (one record per opportunity; schema in opportunities.schema.json)
    TRACKER.md              human-readable tracker grouped by tier, sorted by deadline
    deadlines.ics           calendar file: confirmed full-date tier A/B deadlines only, 14-day alarms
    dashboard.html          the deadline radar page (published privately as a claude.ai artifact)
    CHANGELOG.md            dated changes from rescans
  applications/INDEX.md     every package sorted by deadline, with tier and whether it has been critiqued
  applications/<slug>/      one package per tier A/B opportunity: README, proposal, statement, referee brief, budget/timeline, emails
  applications/*-bundle/    compute and data access; standards participation; Canadian company non-dilutive funding
  profile/master_cv_outline.md  skeleton of the master CV that every tri-agency CV and publication list is trimmed from
  tools/merge_registry.py   merges scout/verifier JSON into the registry and regenerates TRACKER.md + deadlines.ics
  tools/cleanup_registry.py merges duplicate groups, maps package directories to registry entries, adds curated entries
  tools/build_dashboard.py  regenerates registry/dashboard.html and applications/INDEX.md
.claude/agents/             funding-scout, eligibility-verifier, proposal-drafter, proposal-critic, deadline-tracker, portfolio-strategist
.claude/workflows/          funding-discover-verify.js, funding-verify-unverified.js, funding-draft-packages.js, funding-weekly-rescan.js
```

## Tiers

- **A** — eligible (or eligible pending one confirmable fact), deadline within ~6 months, fit ≥ 70. Prepare now.
- **B** — eligible; deadline 6–15 months out, or a sponsor / nominator / co-supervisor / institutional endorsement must be secured first.
- **C** — monitor: this cycle closed and the next is >6 months away, moderate fit, or doubtful eligibility.
- **D** — ineligible or not worth the effort (reason recorded).

## How to run

1. **Full discovery** (first run, or when the profile changes): launch `.claude/workflows/funding-discover-verify.js` with `args = {categories: <subset of registry/categories.json>, scratch: <dir>}`. On a small machine, launch several workflows in parallel with disjoint category subsets. Then `python3 funding/tools/merge_registry.py --scratch <dir>`.
2. **Draft packages**: launch `.claude/workflows/funding-draft-packages.js` with `args = {opportunities: <tier A/B entries from opportunities.json>}`. Each package is drafted, then adversarially critiqued and fixed in place; scores are appended to the package README.
3. **Strategy**: run the `portfolio-strategist` agent to (re)write `funding/STRATEGY.md`.
4. **Weekly rescan**: a scheduled Routine named "Weekly funding rescan (Yi Ru / AXIOMALITY)" runs every Monday at 8:45 am Toronto time in a fresh cloud session. It re-verifies tier A/B deadlines within 90 days, looks for newly announced programs, regenerates the tracker, appends to CHANGELOG.md, commits and pushes. It stops immediately if it cannot push to this branch. Pause or delete it from the Routines list on claude.ai. To run it by hand, launch `.claude/workflows/funding-weekly-rescan.js` with `args = {categories, watch: <tier A/B entries>, known_names: <all names in the registry>, scratch}`, then run the three tools in order: `cleanup_registry.py`, `merge_registry.py`, `build_dashboard.py`.
5. **Mark progress**: edit the `status` field of an entry in `opportunities.json` (`not_started | drafting | waiting_on_referees | submitted | awarded | declined`) and re-run `merge_registry.py` without `--scratch` to refresh the tracker.

## What exists as of 2026-09-26

- 443 opportunities in the registry across 16 categories; 56 tier A/B.
- 32 application packages (29 single-opportunity packages and 3 bundles), each drafted from the profile, Prof. Grüninger's NSERC proposal style and the existing CPRA/Vector/DSI/CIRTA drafts, then attacked by a critic agent that scored it against the funder's criteria, removed or bracketed untraceable claims and fixed it in place. See `applications/INDEX.md`.
- A strategy memo with a month-by-month calendar to December 2027, a dependency list per person and a next-ten-working-days checklist.

## Verification caveat

In the environment where this was built, direct fetches of funder web pages were blocked by the network policy, so every deadline and eligibility statement was established from web-search results (titles and snippets) and marked with a confidence level. Before relying on any date, open the official page linked in the registry. Entries marked `unverifiable` list exactly what to check.

## Facts the applicant must confirm before any submission

See `profile/applicant_profile.md`. The decisive ones: citizenship / permanent-residency status (NSERC PDF-type programs, Canada Research Chairs, NSF, DoD, SBIR/STTR, Fulbright); AXIOMALITY's legal entity and country of incorporation (IRAP, SR&ED, Mitacs, SBIR/STTR, EIC); the Harvard Medical School appointment details; thesis title and supervisor; the exact publication and patent lists; whether Prof. Grüninger holds an active tri-agency grant (CIRTA nominator requirement).
