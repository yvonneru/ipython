export const meta = {
  name: 'funding-draft-packages',
  description: 'Draft a submission-ready application package per funding opportunity, then have an adversarial critic score and fix it in place',
  phases: [
    { title: 'Draft', detail: 'proposal-drafter writes funding/applications/<slug>/' },
    { title: 'Critique', detail: 'proposal-critic scores against funder criteria and fixes in place' },
  ],
}

const PROFILE_FILES = [
  'funding/profile/applicant_profile.md',
  'funding/profile/research_program.md',
  'funding/profile/axiomality_company.md',
  'funding/templates/gruninger_nserc_style.md',
  'funding/templates/gruninger_physical_turing_test_proposal.txt',
  'funding/templates/gruninger_commonsense_cobotics_proposal.txt',
]
const SOURCE_DRAFTS_DIR = 'funding/source_drafts'

const DRAFT_SCHEMA = {
  type: 'object',
  required: ['slug', 'files_written', 'open_items', 'summary'],
  properties: {
    slug: { type: 'string' },
    files_written: { type: 'array', items: { type: 'string' } },
    open_items: { type: 'array', items: { type: 'string' }, description: 'every [bracketed] item the applicant must supply' },
    funder_format_notes: { type: 'string', description: 'page/character limits and required headings found, with source URLs' },
    summary: { type: 'string' },
  },
}

const CRITIC_SCHEMA = {
  type: 'object',
  required: ['slug', 'criteria', 'remaining_risks', 'changes_made'],
  properties: {
    slug: { type: 'string' },
    criteria: { type: 'array', items: { type: 'object', required: ['criterion', 'score_before', 'score_after'], properties: { criterion: { type: 'string' }, weight: { type: 'string' }, score_before: { type: 'integer', minimum: 1, maximum: 5 }, score_after: { type: 'integer', minimum: 1, maximum: 5 }, note: { type: 'string' } } } },
    invented_facts_found: { type: 'array', items: { type: 'string' } },
    changes_made: { type: 'array', items: { type: 'string' } },
    remaining_risks: { type: 'array', items: { type: 'string' } },
  },
}

function draftPrompt(o) {
  return `You are drafting a complete application package for Dr. Yi Ru for the opportunity below. Today is 2026-09-25.

READ FIRST, in this order (use the Read tool; use Glob to list ${SOURCE_DRAFTS_DIR}/ and read every file there):
${PROFILE_FILES.map(f => ' - ' + f).join('\n')}
 - every file in ${SOURCE_DRAFTS_DIR}/ (existing CPRA, Vector, DSI, CIRTA drafts and emails — reuse their strongest sentences and never contradict them)

OPPORTUNITY (registry entry, possibly abbreviated): ${JSON.stringify(o, null, 1)}
If the entry above is abbreviated (only a slug and a few fields), look up the full record by its "slug" in funding/registry/opportunities.json (Grep for the slug, then Read the surrounding record) — it contains the verified deadline, eligibility flags, evidence quotes, required documents and next actions you must use.

Then use WebSearch (load with ToolSearch("select:WebSearch"); WebFetch and curl are blocked by network policy) to find the funder's required components, headings, page/character limits and review criteria for the current cycle; record what you found and its URLs in the README under "Format and criteria (verify on the official page)".

WRITE the package under funding/applications/${o.slug}/ with these files (omit a file only if the program truly has no such component; say so in README):
 - README.md — one-page brief: program, deadline(s) incl. internal/referee deadlines, eligibility conditions (mark which remain unconfirmed for this applicant), review criteria and weights, what is submitted where and in what format, who must do what by when (applicant / Prof. Grüninger / referees / institution / company officer), a submission checklist, a "How this proposal meets the criteria" table, and the list of every [bracketed] item that still needs the applicant.
 - proposal.md — the research proposal (or business/technical plan for company programs) in the funder's headings and within its page limit. Where the funder does not prescribe headings, use the Grüninger structure from funding/templates/gruninger_nserc_style.md: Recent Progress; Objectives (an italic long-term challenge, then numbered objectives); Literature Review; Methodology as Themes → Projects → Open Research Questions; Impact. Name datasets, tools, theorems and milestones concretely. Number citations and include a Bibliography.
 - statement.md — personal / research / contributions statement, or the cover letter, as required.
 - referee_brief.md — what the program is, what the form asks, what reviewers score, the 3–4 points that would help, the letter deadline.
 - budget_and_timeline.md — budget with justification where money is requested; otherwise a milestone timeline.
 - emails.md — ready-to-send messages to the supervisor / sponsor / nominator / referees / institutional office / company officer, each with subject line.

RULES: first person for the applicant; declarative voice; every factual claim must come from the profile, the drafts or the registry entry, and anything unconfirmed stays in [brackets] rather than being invented (no invented paper titles, grant numbers, dates, dollar figures, names of sponsors); respect page and character limits; tailor the framing to this funder's mandate (data science, AI safety/assurance, manufacturing, health, robotics, standards, or commercialization as appropriate — see "Adjacent framings" in research_program.md). For company programs, write from the AXIOMALITY brief and mark incorporation, revenue, ownership and headcount facts as [confirm].

Return the structured output (files written, open items, format notes, summary).`
}

function criticPrompt(o) {
  return `You are a skeptical member of the review panel for "${o.name}" (${o.funder}). Today is 2026-09-25.

Read funding/applications/${o.slug}/ (every file), the profile files below, and the registry entry.
${PROFILE_FILES.slice(0, 3).map(f => ' - ' + f).join('\n')}
Registry entry (abbreviated; look up the full record by slug "${o.slug}" in funding/registry/opportunities.json): ${JSON.stringify({ name: o.name, funder: o.funder, url: o.url, deadline: o.deadline, tier: o.tier, fit_score: o.fit_score }, null, 1)}

1. Reconstruct the funder's review criteria and weights (use WebSearch via ToolSearch("select:WebSearch") if the README does not state them; WebFetch/curl are blocked). Score each criterion 1–5 as a tough reviewer would, and write the concrete reasons a panel would reject or down-rank this package: vague objectives, claims without evidence, missing required components, page/character-limit or format violations, weak fit with the mandate, unaddressed eligibility risks, a plan indistinguishable from the supervisor's programs, missing HQP/training or EDI content where required, missing budget justification.
2. Cross-check every number, date, title, award, affiliation and name against funding/profile/applicant_profile.md and the source drafts. Any fact not traceable to those files must be put in [brackets] or removed. List what you found under invented_facts_found.
3. FIX THE PACKAGE IN PLACE with Edit/Write: tighten objectives, add missing components, resolve format issues, strengthen the criteria mapping, keep [brackets] for applicant-only facts. Do not pad. Keep within limits.
4. Append a "## Review log" section to funding/applications/${o.slug}/README.md with the before/after scores, what changed, and the remaining risks.

Return the structured output.`
}

const opps = args.opportunities
log(`drafting ${opps.length} package(s)`)

const results = await pipeline(
  opps,
  o => agent(draftPrompt(o), { label: `draft:${o.slug}`, phase: 'Draft', schema: DRAFT_SCHEMA, effort: 'high' }),
  (drafted, o) => {
    if (!drafted) { log(`${o.slug}: draft failed`); return null }
    return agent(criticPrompt(o), { label: `critique:${o.slug}`, phase: 'Critique', schema: CRITIC_SCHEMA, effort: 'high' })
      .then(c => ({ slug: o.slug, name: o.name, draft: drafted, critique: c }))
  }
)

return results.filter(Boolean)
