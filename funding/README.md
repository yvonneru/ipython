# Funding agents for Dr. Yi Ru / AXIOMALITY

A self-contained agent system that finds, verifies, tiers, drafts and tracks funding applications: postdoctoral fellowships (Canada, US, international), research grants, faculty and society-of-fellows positions, non-dilutive and accelerator funding for AXIOMALITY, compute credits, and prizes. Built 2026-09-25 from the CV, the AXIOMALITY decks, Prof. Michael Grüninger's NSERC proposals (the style template), and the existing CPRA / Vector / DSI / CIRTA drafts.

The agents do everything up to the point of submission. They cannot press "submit" on a funder's portal, sign on behalf of the applicant, or answer the facts only the applicant knows (citizenship, company incorporation, thesis title, exact patent numbers). Those facts are marked `[in brackets]` everywhere and are listed per package in each `README.md`.

## Layout

```
funding/
  README.md                 this file
  STRATEGY.md               portfolio, sequencing, dependencies (written by portfolio-strategist)
  profile/                  ground truth about the applicant, the research program, the company
  templates/                Grüninger NSERC proposals + a digest of their structure and voice
  source_drafts/            the drafts that already existed (CPRA, Vector, DSI, CIRTA, emails)
  registry/
    categories.json         the 16 search categories with seed programs
    opportunities.json      the registry (one record per opportunity; schema in opportunities.schema.json)
    TRACKER.md              human-readable tracker grouped by tier, sorted by deadline
    deadlines.ics           calendar file for tier A/B deadlines (14-day alarms)
    CHANGELOG.md            dated changes from rescans
  applications/<slug>/      one package per tier A/B opportunity: README, proposal, statement, referee brief, budget/timeline, emails
  tools/merge_registry.py   merges scout/verifier JSON into the registry and regenerates TRACKER.md + deadlines.ics
.claude/agents/             funding-scout, eligibility-verifier, proposal-drafter, proposal-critic, deadline-tracker, portfolio-strategist
.claude/workflows/          funding-discover-verify.js, funding-draft-packages.js, funding-weekly-rescan.js
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
4. **Weekly rescan**: launch `.claude/workflows/funding-weekly-rescan.js` with `args = {categories, watch: <tier A/B entries>, known_names: <all names in the registry>, scratch}`, then merge. A scheduled Routine does this automatically (see the session that created it; disable it from the Routines list if unwanted).
5. **Mark progress**: edit the `status` field of an entry in `opportunities.json` (`not_started | drafting | waiting_on_referees | submitted | awarded | declined`) and re-run `merge_registry.py` without `--scratch` to refresh the tracker.

## Verification caveat

In the environment where this was built, direct fetches of funder web pages were blocked by the network policy, so every deadline and eligibility statement was established from web-search results (titles and snippets) and marked with a confidence level. Before relying on any date, open the official page linked in the registry. Entries marked `unverifiable` list exactly what to check.

## Facts the applicant must confirm before any submission

See `profile/applicant_profile.md`. The decisive ones: citizenship / permanent-residency status (NSERC PDF-type programs, Canada Research Chairs, NSF, DoD, SBIR/STTR, Fulbright); AXIOMALITY's legal entity and country of incorporation (IRAP, SR&ED, Mitacs, SBIR/STTR, EIC); the Harvard Medical School appointment details; thesis title and supervisor; the exact publication and patent lists; whether Prof. Grüninger holds an active tri-agency grant (CIRTA nominator requirement).
