# Funding workflows

Run from the repository root with the Workflow tool (or `/workflows`). Scripts read their inputs from `args`; they cannot read files themselves.

| Script | What it does | Args |
|---|---|---|
| `funding-discover-verify.js` | One web-searching scout per category, then adversarial verifiers (5 opportunities each) that refute deadlines/eligibility and assign tiers A–D. Writes `scout_<cat>.json` / `verified_<cat>_<i>.json` into `args.scratch`. | `{ "categories": [<entries from funding/registry/categories.json>], "scratch": "<dir>" }` |
| `funding-draft-packages.js` | For each opportunity: proposal-drafter writes `funding/applications/<slug>/`, then proposal-critic scores and fixes it in place. | `{ "opportunities": [<entries from opportunities.json with tier A or B>] }` |
| `funding-weekly-rescan.js` | Re-verifies every tier A/B deadline within 90 days, scans each category for new programs, and reports changes. | `{ "categories": [...], "watch": [<tier A/B entries>], "scratch": "<dir>" }` |

After a discovery or rescan run: `python3 funding/tools/merge_registry.py --scratch <dir>` merges results and regenerates `funding/registry/TRACKER.md` and `deadlines.ics`.

Concurrency: the runtime caps concurrent agents per workflow at min(16, CPUs − 2). On a small machine, launch several workflows in parallel with disjoint category subsets (this is how the first run was done: eight workflows of two categories each).
