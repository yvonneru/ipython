# Registry changelog

## 2026-09-25 — initial build
- 16 categories scouted by 16 web-searching agents (categories.json); the session's 200-search budget was exhausted after roughly the first eight scouts, so later scouts and all verifiers worked from prior knowledge and marked their records `unverifiable` with what to check.
- Verifier agents (5 opportunities each) tiered every record A–D; near-duplicates coalesced by name similarity and URL.
- Direct fetches of funder pages were blocked by the environment's network policy: every deadline carries a confidence level and must be confirmed on the official page before it is relied upon.
