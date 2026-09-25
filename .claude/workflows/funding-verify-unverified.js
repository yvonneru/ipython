export const meta = {
  name: 'funding-verify-unverified-by-file',
  description: 'Verifiers read their slice of the unverified-candidates file by category and index range, then tier them',
  phases: [{ title: 'Verify', detail: 'one verifier per category slice of up to 5 candidates' }],
}

const SCRATCH = (args && args.scratch) || '/tmp/funding-scratch'
const FILE = SCRATCH + '/unverified_args.json'
const PROFILE_FILES = [
  'funding/profile/applicant_profile.md',
  'funding/profile/research_program.md',
  'funding/profile/axiomality_company.md',
]

const VER_SCHEMA = {
  type: 'object',
  required: ['verified'],
  properties: {
    verified: {
      type: 'array',
      items: {
        type: 'object',
        required: ['name', 'funder', 'url', 'country', 'type', 'verdict', 'tier', 'fit_score', 'deadline', 'deadline_confidence', 'amount', 'duration', 'eligibility_summary', 'eligibility_flags', 'evidence', 'next_actions', 'estimated_prep_days', 'sources'],
        properties: {
          name: { type: 'string' }, funder: { type: 'string' }, url: { type: 'string' }, country: { type: 'string' }, type: { type: 'string' }, applicant_entity: { type: 'string' },
          verdict: { type: 'string', enum: ['confirmed', 'corrected', 'unverifiable', 'ineligible', 'closed_for_cycle', 'discontinued'] },
          tier: { type: 'string', enum: ['A', 'B', 'C', 'D'] }, fit_score: { type: 'integer', minimum: 0, maximum: 100 },
          deadline: { type: 'string' }, deadline_confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
          internal_or_referee_deadlines: { type: 'string' }, amount: { type: 'string' }, duration: { type: 'string' },
          eligibility_summary: { type: 'string' }, eligibility_flags: { type: 'array', items: { type: 'string' } },
          evidence: { type: 'array', items: { type: 'object', required: ['claim', 'quote', 'url'], properties: { claim: { type: 'string' }, quote: { type: 'string' }, url: { type: 'string' } } } },
          corrections: { type: 'string' }, required_documents: { type: 'array', items: { type: 'string' } },
          next_actions: { type: 'array', items: { type: 'string' } }, estimated_prep_days: { type: 'integer' }, tier_rationale: { type: 'string' },
          sources: { type: 'array', items: { type: 'string' } },
        },
      },
    },
  },
}

function verifyPrompt(cat, start, end, i) {
  return `You are an adversarial verifier of funding opportunities for Dr. Yi Ru. Today is 2026-09-25.

FIRST read these three files with the Read tool:
${PROFILE_FILES.map(f => ' - ' + f).join('\n')}

Then Read ${FILE}. It is {"candidates": [...]}. Your candidates are those whose "category" equals "${cat}", taken in file order, positions ${start} to ${end - 1} inclusive (0-based within that category). Verify exactly those candidates and no others.

For EACH candidate: try to REFUTE it, then tier it.
1. WebSearch is available (load with ToolSearch("select:WebSearch")) but the budget is shared across many agents: use AT MOST ONE search per candidate, on the single fact that decides its value (current-cycle deadline or the eligibility rule). WebFetch and curl are blocked. If the search does not settle it, verdict = unverifiable and say exactly what to check.
2. Check: deadline right for the 2026–27 cycle; discontinued/renamed; eligible given PhD requirements completed March 2025, current Harvard Medical School postdoc, not at a Canadian university now, U of T MIE under Prof. Grüninger from spring 2027, citizenship UNKNOWN, company incorporation country UNKNOWN; amount/duration.
3. Tier: A = eligible (or pending ONE confirmable fact) AND deadline by end of March 2027 AND fit >= 70. B = eligible but 6–15 months out or needs a sponsor/nominator first. C = monitor. D = ineligible / not worth it (say why).
4. next_actions with dates; estimated_prep_days; internal/referee deadlines. Keep name and funder EXACTLY as given so the registry merge matches them; put corrections in the corrections field.

Return ONLY the structured output. Also write the identical JSON to ${SCRATCH}/verified_${cat}_9${i}.json with the Write tool before returning.`
}

const counts = args.counts
const jobs = []
for (const [cat, n] of Object.entries(counts)) {
  for (let s = 0, i = 0; s < n; s += 5, i++) jobs.push({ cat, start: s, end: Math.min(n, s + 5), i })
}
log(`verifying ${Object.values(counts).reduce((a, b) => a + b, 0)} candidates in ${jobs.length} chunk(s)`)

const results = await parallel(jobs.map(j => () =>
  agent(verifyPrompt(j.cat, j.start, j.end, j.i), { label: `verify:${j.cat}:9${j.i}`, phase: 'Verify', schema: VER_SCHEMA, effort: 'medium' })
))
const verified = results.filter(Boolean).flatMap(r => r.verified || [])
log(`verified ${verified.length}; failed chunks: ${results.filter(r => !r).length}`)
return { verified_count: verified.length, tiers: verified.reduce((m, v) => (m[v.tier] = (m[v.tier] || 0) + 1, m), {}) }