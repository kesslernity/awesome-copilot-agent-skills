# Default theme codebook, evidence grades, owner basis and anonymisation

Used by the lessons learned synthesis skill when the user supplies no codebook. The header of the synthesis says "codebook: default" when this file applies. A user codebook replaces the theme table; the grades, owner basis and anonymisation rules still apply.

## Default themes

| Code | Theme | Definition | Typical phrases in sources |
|------|-------|------------|----------------------------|
| T01 | Scope and requirements | Clarity, stability and sign-off of what was to be delivered | "scope creep", "requirements changed", "unclear acceptance criteria" |
| T02 | Schedule and estimation | Planning realism, estimate accuracy, critical path handling | "underestimated", "optimistic plan", "slipped", "float" |
| T03 | Resourcing and skills | Availability, continuity and capability of the team | "key person left", "onboarding took", "no one knew the tool" |
| T04 | Stakeholder engagement and communication | Involvement of sponsors, users and affected functions; reporting cadence | "not consulted", "late buy-in", "status reports too long" |
| T05 | Governance and decisions | Decision rights, escalation, gate reviews, speed of decisions | "waited weeks for a decision", "unclear who approves" |
| T06 | Vendor and contract | Procurement, contract terms, supplier performance, change orders | "change order", "supplier missed", "contract did not cover" |
| T07 | Quality and testing | Test coverage, defect handling, acceptance, rework | "found in production", "rework", "test environment unavailable" |
| T08 | Risk and change management | RAID discipline, contingency, change control | "risk log not used", "no contingency", "change control bypassed" |
| T09 | Tools, data and environments | Fitness of tooling, data readiness, access, integration | "data migration", "access took weeks", "two systems of record" |
| T10 | Handover and benefits | Transition to operations, training, benefits tracking | "no run book", "benefits never measured", "support not ready" |
| T11 | Health, safety and environment | Any statement touching safety of people, plant or environment | Always written in observation form ("n of N sources report ...") with "recommendation: referred"; the full form is never used; always also referred; never becomes a recommendation to add, change, relax or bypass a control |
| T12 | Ways of working | Team rituals, collaboration, remote or on-site working | "daily stand-up helped", "too many meetings", "time zones" |

A statement may carry more than one code. A new theme needs statements from at least two sources and no fitting code, and is labelled "new theme, confirm" in the lessons table.

## Polarity and phase

| Polarity | Meaning |
|----------|---------|
| Went well | The source names a practice to keep |
| Went badly | The source names a problem or loss |
| Suggestion | The source proposes a change without stating a problem or success |

Phases: initiation, planning, execution, close, benefits. Where the source states no phase, write "phase UNKNOWN".

## Evidence grades

| Grade | Basis | Note |
|-------|-------|------|
| A | Stated in an official source (signed-off closing report or review), or supported by a quoted measured fact (dates, quantities, variances) in any source | Quote the fact with its source |
| B | Stated by two or more independent informal sources | Two retros written by the same author count once |
| C | Stated by one informal source | Never raised to B by the agent's own reasoning |

A theme's grade is the best grade among its statements. The grade describes the evidence, not the importance of the lesson.

## Lesson statement form

Full form, only where every part is quoted in the evidence: "When <situation>, <practice>, because <consequence observed>." Otherwise, observation form: "n of N sources report <observation>; recommendation UNKNOWN." T11 statements always take the observation form, closing with "recommendation: referred".

## Owner basis for follow-ups

| Basis | When to use | What to write |
|-------|-------------|---------------|
| Named in source | The source names a role or function to act | The role as the source names it |
| Catalogue mapping | The user supplied an owner catalogue and one role holds the process the follow-up concerns | The catalogue role, with the theme code that justified the mapping |
| UNKNOWN | Neither applies | UNKNOWN, and the follow-up appears in Open questions |

Owners are recommended, never assigned. Named individuals are never proposed as owners; a person in a source becomes their role.

## Anonymisation replacement table

| Detail type | Replacement | Example |
|-------------|-------------|---------|
| Person | Role token in square brackets | [delivery lead], [sponsor], [tester] |
| Small team or unit below three people | Generic token | [the integration team] |
| Internal team or function (default policy) | Name kept as the source writes it | The user may tighten to a generic token such as [the integration team] |
| Vendor or other external company (default policy) | Token, consistent across the document; the token-to-name key is returned as a separate block for the user to hold outside the document | [vendor A], [vendor B]; the user may loosen for the sponsor audience by typed instruction, recorded in the header |
| Exact date that identifies a person (a leaving date, a sick-leave period) | Month or quarter | "March" for "14 March" |
| Unique attribute (only person with a given role, nationality, condition) | Generalised | "a team member" |
| Recognisable incident | Paraphrased and tagged | "[paraphrased] a data load failed twice in the same week" |

Re-identification test before a quote ships: could a reader who knows the project name the person from the quote alone? If yes, paraphrase and tag, or drop the quote.

## Quote limits by audience

| Audience | Quotes per theme | Length | Extra rule |
|----------|------------------|--------|------------|
| Sponsor and portfolio office (default) | Up to three | About 40 words each | Internal team names as the policy allows; vendors as tokens unless the user loosens the policy by typed instruction |
| Wider circulation or all staff | Up to two | About 25 words each | Team-identifying quotes paraphrased |
| Vendor-facing | Up to one | About 25 words | No internal team names; vendors as tokens; contractual matters referred, not quoted |
