export const meta = {
  name: 'funding-weekly-rescan',
  description: 'Weekly: re-verify upcoming tier A/B deadlines and scan every category for newly announced programs',
  phases: [
    { title: 'Re-verify', detail: 'tier A/B entries with deadlines within 90 days or low confidence' },
    { title: 'Scan', detail: 'one scout per category looking only for programs not already in the registry' },
  ],
}

const SCRATCH = (args && args.scratch) || '/tmp/funding-scratch'
const PROFILE_FILES = [
  'funding/profile/applicant_profile.md',
  'funding/profile/research_program.md',
  'funding/profile/axiomality_company.md',
]

const RECHECK_SCHEMA = {
  type: 'object', required: ['verified'],
  properties: { verified: { type: 'array', items: { type: 'object', required: ['name', 'funder', 'url', 'verdict', 'tier', 'deadline', 'deadline_confidence', 'evidence', 'next_actions'], properties: {
    name: { type: 'string' }, funder: { type: 'string' }, url: { type: 'string' }, country: { type: 'string' }, type: { type: 'string' },
    verdict: { type: 'string', enum: ['confirmed', 'corrected', 'unverifiable', 'ineligible', 'closed_for_cycle', 'discontinued'] },
    tier: { type: 'string', enum: ['A', 'B', 'C', 'D'] }, fit_score: { type: 'integer' },
    deadline: { type: 'string' }, deadline_confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
    internal_or_referee_deadlines: { type: 'string' }, amount: { type: 'string' }, duration: { type: 'string' },
    eligibility_summary: { type: 'string' }, eligibility_flags: { type: 'array', items: { type: 'string' } },
    evidence: { type: 'array', items: { type: 'object', properties: { claim: { type: 'string' }, quote: { type: 'string' }, url: { type: 'string' } } } },
    corrections: { type: 'string' }, next_actions: { type: 'array', items: { type: 'string' } }, estimated_prep_days: { type: 'integer' }, sources: { type: 'array', items: { type: 'string' } },
  } } } },
}

const SCAN_SCHEMA = {
  type: 'object', required: ['opportunities', 'coverage_notes'],
  properties: { coverage_notes: { type: 'string' }, opportunities: { type: 'array', items: { type: 'object', required: ['name', 'funder', 'url', 'country', 'type', 'deadline', 'deadline_confidence', 'amount', 'duration', 'eligibility_summary', 'applicant_entity', 'fit_score', 'fit_rationale', 'sources'], properties: {
    name: { type: 'string' }, funder: { type: 'string' }, url: { type: 'string' }, country: { type: 'string' }, type: { type: 'string' },
    deadline: { type: 'string' }, deadline_confidence: { type: 'string', enum: ['high', 'medium', 'low'] }, cycle_note: { type: 'string' },
    amount: { type: 'string' }, duration: { type: 'string' }, eligibility_summary: { type: 'string' }, applicant_entity: { type: 'string' },
    required_documents: { type: 'array', items: { type: 'string' } }, fit_score: { type: 'integer' }, fit_rationale: { type: 'string' },
    risks_and_flags: { type: 'array', items: { type: 'string' } }, sources: { type: 'array', items: { type: 'string' } },
  } } } },
}

const watch = args.watch || []
const cats = args.categories || []
const known = (args.known_names || []).join('; ')

function recheckPrompt(chunk, i) {
  return `Re-verify these funding opportunities for Dr. Yi Ru (read ${PROFILE_FILES.join(', ')} first). Use WebSearch (ToolSearch("select:WebSearch"); WebFetch/curl are blocked). For each: confirm or correct the deadline for the current cycle, check for closure/renaming, re-check eligibility against the profile, keep or change the tier (A/B/C/D) with a reason, and update next_actions with dates. Record evidence quotes with URLs. Write the JSON to ${SCRATCH}/verified_recheck_${i}.json and return it.\n\n${JSON.stringify(chunk, null, 1)}`
}
function scanPrompt(c) {
  return `You are a funding scout for Dr. Yi Ru (read ${PROFILE_FILES.join(', ')} first). Category: ${c.title}. Scope: ${c.notes}. Use WebSearch (ToolSearch("select:WebSearch"); WebFetch/curl are blocked), at least 15 queries focused on NEW or newly opened programs (announcements, "call for applications", "now open", "2027 competition") in the last ~2 months. Do NOT return any of these already-known programs: ${known}. Return only genuinely new or newly reopened opportunities with the full record (deadline, confidence, amount, duration, eligibility, fit_score, fit_rationale, risks_and_flags, sources). Write the JSON to ${SCRATCH}/scout_${c.key}.json and return it.`
}

const chunks = []
for (let i = 0; i < watch.length; i += 5) chunks.push(watch.slice(i, i + 5))
log(`re-verifying ${watch.length} watched entries in ${chunks.length} chunk(s); scanning ${cats.length} categories`)

const [rechecks, scans] = await parallel([
  () => parallel(chunks.map((ch, i) => () => agent(recheckPrompt(ch, i), { label: `recheck:${i}`, phase: 'Re-verify', schema: RECHECK_SCHEMA, effort: 'medium' }))),
  () => parallel(cats.map(c => () => agent(scanPrompt(c), { label: `scan:${c.key}`, phase: 'Scan', schema: SCAN_SCHEMA, effort: 'medium' }))),
])

return {
  rechecked: (rechecks || []).filter(Boolean).flatMap(r => r.verified || []),
  new_candidates: (scans || []).filter(Boolean).flatMap(s => s.opportunities || []),
}
