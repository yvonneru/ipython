export const meta = {
  name: 'funding-discover-verify',
  description: 'Scout funding opportunities per category via web search, then adversarially verify deadlines and eligibility and assign tiers',
  phases: [
    { title: 'Scout', detail: 'one web-searching scout per category' },
    { title: 'Verify', detail: 'adversarial verifiers, 5 opportunities each' },
  ],
}

const SCRATCH = (args && args.scratch) || '/tmp/funding-scratch'
const PROFILE_FILES = [
  'funding/profile/applicant_profile.md',
  'funding/profile/research_program.md',
  'funding/profile/axiomality_company.md',
]

const OPP_SCHEMA = {
  type: 'object',
  required: ['opportunities', 'coverage_notes'],
  properties: {
    coverage_notes: { type: 'string', description: 'What was searched, what was excluded and why, what could not be verified' },
    opportunities: {
      type: 'array',
      items: {
        type: 'object',
        required: ['name', 'funder', 'url', 'country', 'type', 'deadline', 'deadline_confidence', 'amount', 'duration', 'eligibility_summary', 'applicant_entity', 'fit_score', 'fit_rationale', 'sources'],
        properties: {
          name: { type: 'string' },
          funder: { type: 'string' },
          url: { type: 'string' },
          country: { type: 'string' },
          type: { type: 'string', enum: ['postdoc_fellowship', 'research_grant', 'training_award', 'faculty_position', 'society_fellowship', 'startup_nondilutive', 'accelerator_or_program', 'competition_or_prize', 'compute_or_credits', 'standards_participation', 'other'] },
          deadline: { type: 'string', description: 'YYYY-MM-DD, or "rolling", or "expected YYYY-MM (unconfirmed)", or "unknown"' },
          deadline_confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
          cycle_note: { type: 'string' },
          amount: { type: 'string' },
          duration: { type: 'string' },
          eligibility_summary: { type: 'string' },
          citizenship_requirement: { type: 'string' },
          years_since_phd_limit: { type: 'string' },
          needs_host_or_nominator: { type: 'string' },
          applicant_entity: { type: 'string', enum: ['individual', 'institution', 'company', 'either'] },
          required_documents: { type: 'array', items: { type: 'string' } },
          fit_score: { type: 'integer', minimum: 0, maximum: 100 },
          fit_rationale: { type: 'string' },
          risks_and_flags: { type: 'array', items: { type: 'string' } },
          sources: { type: 'array', items: { type: 'string' } },
        },
      },
    },
  },
}

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
          name: { type: 'string' },
          funder: { type: 'string' },
          url: { type: 'string' },
          country: { type: 'string' },
          type: { type: 'string' },
          applicant_entity: { type: 'string' },
          verdict: { type: 'string', enum: ['confirmed', 'corrected', 'unverifiable', 'ineligible', 'closed_for_cycle', 'discontinued'] },
          tier: { type: 'string', enum: ['A', 'B', 'C', 'D'] },
          fit_score: { type: 'integer', minimum: 0, maximum: 100 },
          deadline: { type: 'string' },
          deadline_confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
          internal_or_referee_deadlines: { type: 'string' },
          amount: { type: 'string' },
          duration: { type: 'string' },
          eligibility_summary: { type: 'string' },
          eligibility_flags: { type: 'array', items: { type: 'string' } },
          evidence: { type: 'array', items: { type: 'object', required: ['claim', 'quote', 'url'], properties: { claim: { type: 'string' }, quote: { type: 'string' }, url: { type: 'string' } } } },
          corrections: { type: 'string' },
          required_documents: { type: 'array', items: { type: 'string' } },
          next_actions: { type: 'array', items: { type: 'string' } },
          estimated_prep_days: { type: 'integer' },
          tier_rationale: { type: 'string' },
          sources: { type: 'array', items: { type: 'string' } },
        },
      },
    },
  },
}

function scoutPrompt(c) {
  return `You are a funding scout working for Dr. Yi Ru. Today is 2026-09-25.

FIRST read these three files with the Read tool; they are the ground truth about the applicant, the research program and the company:
${PROFILE_FILES.map(f => ' - ' + f).join('\n')}

CATEGORY: ${c.title}
SCOPE: ${c.notes}
SEED PROGRAMS (check every one, then go well beyond them): ${c.seeds}

TOOLS: load WebSearch with ToolSearch("select:WebSearch") and use it heavily — at least 25 distinct searches. WebFetch and curl are BLOCKED by the network policy; do not try them. Rely on search-result titles/snippets. Good query shapes: "<program> 2026 deadline", "<program> 2027 competition", "<program> postdoctoral eligibility citizenship", "<program> application deadline October 2026", site-restricted searches on the funder's domain, and "<funder> new program 2026" to catch renamed or new programs.

GOAL: an exhaustive list (target 15–30 entries) of opportunities in this category that Dr. Ru (as an individual) or AXIOMALITY (as a company) could apply to, or be nominated for, between now and December 2027, ranked by fit. Include prestigious long shots. Include programs whose eligibility hinges on an unconfirmed fact (citizenship / permanent residency, company incorporation country, gender or equity self-identification, nominator availability, US-institution requirement) and put the dependency in risks_and_flags rather than omitting the program. Exclude only programs that are clearly discontinued or clearly ineligible (e.g., PhD-students-only), and list those exclusions with one line each in coverage_notes.

FOR EVERY OPPORTUNITY: the current-cycle deadline as an ISO date if findable; if this year's deadline has already passed, give the next expected date from the funder's usual pattern and mark deadline_confidence low or medium; amount and duration; eligibility (citizenship, years since PhD, host/nominator/supervisor required, employer requirements); required documents; a fit_score 0–100 against the profile; a 2–3 sentence fit_rationale that names which objective (O1 specification / O2 audit / O3 inductive bias) or which company asset it maps to; and the source URLs you relied on.

Facts to keep in mind: PhD requirements completed March 2025 (U of T, Information Engineering); currently a postdoc at Harvard Medical School; not currently affiliated with a Canadian university; intends to return to U of T MIE under Prof. Michael Grüninger from spring 2027; citizenship unknown; AXIOMALITY incorporation country unknown; founder/CEO with prior venture track record.

Return ONLY the structured output. Also write the identical JSON to ${SCRATCH}/scout_${c.key}.json with the Write tool before returning.`
}

function verifyPrompt(c, chunk, i) {
  return `You are an adversarial verifier of funding opportunities for Dr. Yi Ru. Today is 2026-09-25.

FIRST read these three files with the Read tool:
${PROFILE_FILES.map(f => ' - ' + f).join('\n')}

Category: ${c.title}. Below are ${chunk.length} candidate opportunities found by a scout. Your job is to try to REFUTE each one, then tier it.

For EACH candidate:
1. Run at least 2 fresh WebSearch queries (load with ToolSearch("select:WebSearch"); WebFetch and curl are BLOCKED — do not try them). Check: Is the stated deadline right for the 2026–27 cycle, or has it passed / moved? Has the program been discontinued, renamed or replaced (e.g., Banting and NSERC PDF were folded into the Canada Postdoctoral Research Award)? Is the applicant actually eligible given: PhD requirements completed March 2025; currently a Harvard Medical School postdoc; not currently at a Canadian university; would hold a Canadian award at U of T MIE under Prof. Grüninger from spring 2027; citizenship UNKNOWN; company incorporation country UNKNOWN? Are amount and duration right?
2. Record evidence as short quotes with URLs (from search snippets). If confirming evidence cannot be found, verdict = unverifiable and say exactly what the applicant must check on the official page.
3. Assign a tier:
   A = eligible (or eligible pending ONE confirmable fact) AND deadline within ~6 months (by end of March 2027) AND fit_score >= 70 → prepare now.
   B = eligible, but deadline is 6–15 months out, or the application first requires securing a sponsor / nominator / co-supervisor / institutional endorsement.
   C = monitor: this cycle's deadline has passed and the next is >6 months away, or fit is moderate (50–69), or eligibility is doubtful.
   D = ineligible or not worth the effort — say why in tier_rationale.
4. List concrete next_actions (who must do what by when, e.g. "ask Grüninger to confirm supervision by 2 Oct", "confirm permanent-resident status", "identify a Vector faculty sponsor by 15 Jan 2027"), estimated_prep_days for a complete application, and any internal / referee / letter-of-intent deadlines.
5. Keep the name, funder, url, country, type and applicant_entity fields; correct them if wrong and note the correction in corrections.

Return ONLY the structured output. Also write the identical JSON to ${SCRATCH}/verified_${c.key}_${i}.json with the Write tool before returning.

CANDIDATES (JSON):
${JSON.stringify(chunk, null, 1)}`
}

const cats = args.categories
const CHUNK = 5

const results = await pipeline(
  cats,
  c => agent(scoutPrompt(c), { label: `scout:${c.key}`, phase: 'Scout', schema: OPP_SCHEMA, effort: 'high' }),
  (scouted, c) => {
    if (!scouted || !Array.isArray(scouted.opportunities)) { log(`${c.key}: scout returned nothing`); return null }
    const opps = scouted.opportunities
    log(`${c.key}: ${opps.length} candidates from scout; verifying in chunks of ${CHUNK}`)
    const chunks = []
    for (let i = 0; i < opps.length; i += CHUNK) chunks.push(opps.slice(i, i + CHUNK))
    return parallel(chunks.map((ch, i) => () =>
      agent(verifyPrompt(c, ch, i), { label: `verify:${c.key}:${i}`, phase: 'Verify', schema: VER_SCHEMA, effort: 'high' })
    )).then(vs => {
      const verified = vs.filter(Boolean).flatMap(v => v.verified || [])
      const dropped = chunks.length - vs.filter(Boolean).length
      if (dropped) log(`${c.key}: ${dropped} verifier chunk(s) failed — those candidates remain unverified in scout_${c.key}.json`)
      log(`${c.key}: ${verified.length} verified (A=${verified.filter(v => v.tier === 'A').length}, B=${verified.filter(v => v.tier === 'B').length}, C=${verified.filter(v => v.tier === 'C').length}, D=${verified.filter(v => v.tier === 'D').length})`)
      return { category: c.key, coverage_notes: scouted.coverage_notes, scouted_count: opps.length, verified }
    })
  }
)

return results.filter(Boolean)