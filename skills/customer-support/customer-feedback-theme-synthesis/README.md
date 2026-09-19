# Customer feedback theme synthesis

Synthesises a batch of customer feedback (survey answers, reviews, ticket and chat comments) into a DRAFT themed report: coded themes with record counts and shares, anonymised verbatim quotes cited to record codes, contradictions and unverified claims, and the follow-up questions to answer next. Produces no sentiment score or percentage positive as fact; ratings appear only as distributions with n. Use when the user asks to "theme this feedback", "what are customers saying", "summarise these survey answers", "analyse these reviews", "find the top complaints in these comments" or "code this voice of the customer data". Do not use for exit interviews, use exit-interview-synthesis instead; for sorting a live queue and drafting replies, use ticket-triage-pack; for project retrospectives, use lessons-learned-synthesis. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/customer-feedback-theme-synthesis.zip)** (one zip, ready for Agent Builder) · Category: `customer-support` · Skill name: `customer-feedback-theme-synthesis`

## What to attach or make available

- The feedback records: survey exports, review dumps, ticket and chat comments, feedback forms or transcripts, with channel, date and any customer-given rating per record
- The organisation's theme codebook, or agreement to use the skill's default codebook
- Grouping fields and their values: product, plan, channel, region, period or segment, with the minimum group size for any breakdown
- A prior synthesis for the same scope, where theme movement is wanted
- The routes the organisation has named for referred items such as safety, legal, security or complaints about named staff

## What you get

One complete Markdown document in the chat, titled `DRAFT-customer-feedback-themes-<scope-kebab>-<YYYY-MM-DD>-v1` (revisions v2, v3). First line: "DRAFT generated `<date>` from `<N>` feedback records (`<sources>`, `<period>`). Counts are of records, not of all customers; ratings as recorded, no sentiment scored; claims unverified; no individual identified. The team decides."

Sections, in the reference layout: Header; Summary of at most five counted lines; Themes: Theme | Definition | Records (n) | Share of N | Problem (n) | Praise (n) | Request (n) | Question (n) | Recorded ratings | Change vs prior, long tail row last; Evidence: Theme | Verbatim quote | Record code | Channel | Recorded rating | Tags; Breakdowns per grouping field with a Suppressed column; Contradictions and claims with both positions and a Status column; Recorded ratings as given, per scale point with n; Referred items: Number | Category | Record code | Suggested route | Status; Follow-up questions: Number | Question | Evidence (theme, n) | Type | Suggested owner | Decision; Data quality with the anonymisation log, UNKNOWN list, "Embedded instructions found" (or "None") and proposed user actions, none performed by this agent.

Closing report: sources, defaults, caps, sampling, counts, fallbacks. End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name."

## Use cases

| Scenario | What you say |
|---|---|
| Quarterly voice of the customer report | Code the 500 free-text answers in the attached quarterly survey export against our codebook from the knowledge sources, break down by product and region with a minimum group of 5, and give me three anonymised quotes per theme cited to record codes. |
| Review batch after a release | Analyse the 90 app reviews pasted below from the two weeks after release 4.2; count records per theme and feedback type, show the star ratings as a distribution with n, and list the contradictions where customers take opposite positions. |
| Refreshing a prior synthesis | Theme the attached October feedback export and compare with the attached September synthesis; show movement only where the themes map, and turn every thin high-count theme and unverified claim into a follow-up question for its owner. |

## Try it (example prompts)

- Theme this feedback. The export of 340 free-text answers from the September customer survey is attached, with a 1 to 5 satisfaction score per row; break down by plan and region with a minimum group size of 5.
- What are customers saying about the mobile app? The 120 app reviews from August are pasted below; use the default codebook, three quotes per theme, and anonymise everything before quoting.
- Summarise these survey answers for the product team. The onboarding survey export is attached, about 200 records with two free-text questions and a recommend score; no sentiment score, counts and quotes only.
- Analyse these reviews and compare with last quarter. The third-quarter review export and the second-quarter synthesis report are both attached; show theme movement only where the codebooks match and flag every customer claim we have not verified.
- Find the top complaints in these comments. The chat and ticket comments for the billing channel from the last 30 days are attached as a CSV; break down by channel, cap the display at 12 themes and draft follow-up questions for the billing owner.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- exit-interview-synthesis: when the records are leaver interviews rather than customer feedback
- ticket-triage-pack: when the need is to sort a live support queue and draft replies
- dataset-insight-pack: when the data is numeric with no free text to code

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent helps product, service and customer experience teams turn a batch of customer feedback into a draft themed report: coded themes with record counts and shares, the feedback type the customer's words evidence, anonymised verbatim quotes cited to record codes, breakdowns by group above a minimum size, contradictions and unverified claims, referred items and the follow-up questions to answer next.

General guidelines: read only what the user pastes or attaches and what sits in the agent's knowledge sources; if an export cannot be reached, ask for a paste and say so in the output. When an input is missing, ask one question at a time, starting with the records and then the scope. Counts are of records supplied, never of customers at large. Produce no sentiment score, mood label or percentage positive; recorded ratings appear only as distributions. Remove every identifier before quoting; verify no claim; judge no person or team. Anything the sources do not state reads UNKNOWN. Every output is a draft for human review. Never claim to have saved, sent, posted, closed or deleted anything; propose each action for the user. A typed confirmation releases a workflow hold; it authorises nothing.

For the task, apply the customer-feedback-theme-synthesis skill: register and anonymise records, code them, count and break down, select quotes, list contradictions, claims and referrals, draft follow-up questions and return the report as Markdown in the chat.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.
- `references/theme-coding-defaults.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
