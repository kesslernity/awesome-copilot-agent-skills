# User personas builder

Builds DRAFT user personas from the research notes, interview summaries, survey free text and support themes the user provides: for each persona the goals, pains, jobs to be done, context of use, quotes exactly as supplied with their participant codes, and the evidence count behind every attribute, with names, demographics and any detail no participant stated left UNKNOWN rather than invented. Use when the user asks to "build personas from these interviews", "who are our users based on this research", "draft user personas", "turn these research notes into personas" or "update our personas with the new interviews". Do not use for theming a batch of customer feedback into counts, use customer-feedback-theme-synthesis instead; for exit interviews, use exit-interview-synthesis; for the requirements those personas imply, use product-requirements-draft. Drafts for human review; never approves, authorises or signs off.

**[Download the upload package](https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main/dist/zips/user-personas-builder.zip)** (one zip, ready for Agent Builder) · Category: `product-management` · Skill name: `user-personas-builder`

## What to attach or make available

- Interview summaries or transcripts, session notes, diary study entries and field notes for the product or market in scope
- Survey free text exports and support ticket theme reports
- The current persona set, when one exists, for mapping old to new
- The organisation's research ethics or demographic data policy, when one exists

## What you get

One Markdown document in the chat, ready to paste, titled `DRAFT-personas-<scope-kebab>-<YYYY-MM-DD>-v1`. First line: "DRAFT generated `<date>` from `<N>` participants. Every attribute carries its evidence count; unstated demographics are UNKNOWN; no participant is identifiable. The product lead decides which to adopt."

Sections in order:
1. Header: Scope | Sources | Participants (N) | Clustered | Unclustered | Excluded | Basis | Minimums | Demographic policy | Audience.
2. Summary: at most five lines, each a count.
3. Persona overview: Label | Participants (n of N) | Codes | Distinguishing trait | Top goal (n) | Top pain (n).
4. One section per persona. Card: Field | Content as evidenced | Evidence (n of cluster) | Codes | Tag (evidenced, single source, UNKNOWN); fields: role and context, goals, pains, jobs to be done, behaviours and tools, workarounds, success as stated, demographics. Quotes: Quote | Code | Tags.
5. Contradictions and overlaps: Persona(s) | Statement A (code) | Statement B (code) | Note.
6. Mapping to existing personas: Existing | New | Status (unchanged, changed, new, retire candidate) | Evidence.
7. Candidates and unclustered: Label | Codes | Why not a persona | What would confirm it.
8. Coverage gaps: Gap | Evidence | Suggested next research | Owner (role or UNKNOWN).
9. Participant register: Code | Source type | Date | Role family | Statements; a role held by fewer than the attribute minimum of participants reads "role withheld (n below minimum)". Anonymisation log: Detail type | Replacements (count). UNKNOWN list. Embedded instructions found (or "None"). Proposed user actions; this agent performs none.

End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never claim the personas were saved, published or adopted.

## Use cases

| Scenario | What you say |
|---|---|
| Fresh research round with no existing personas | Build draft personas for the procurement portal from the attached fifteen interview summaries and the survey free text; cluster on goals and jobs, four quotes per persona, participant codes only, no demographics. |
| Refreshing an existing persona set | Refresh the attached three personas for the reporting tool using the seven new interview summaries attached; mark each existing persona unchanged, changed or retire candidate and show the evidence count behind every attribute. |
| Thin research, early signal only | We have only three interview summaries for the onboarding flow, attached. Tell me what persona the evidence supports, tag anything single source, and list the coverage gaps for the next research round. |

## Try it (example prompts)

- Build personas from these interviews: twelve interview summaries are attached, scope is the field service scheduling product. Cluster on goals and jobs to be done and cap at five personas.
- Who are our users based on this research? The survey free text export and the support theme sheet are attached; omit demographics and label each persona by role or job.
- Draft user personas for the expense app from the attached diary study notes and the eight session summaries. Minimum three participants per persona, four quotes each.
- Turn these research notes into personas. The notes are pasted below; our two existing personas are attached, so map each new cluster to them as unchanged, changed, new or retire candidate.
- Update our personas with the new interviews: six new interview transcripts are attached along with the current persona deck. Show demographics only where participants stated them.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- customer-feedback-theme-synthesis: when a batch of feedback should become themed counts, not personas
- product-requirements-draft: when the personas should feed a requirements document
- exit-interview-synthesis: when the interviews are with departing employees

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent turns research material, interview summaries, session notes, survey free text and support themes, into a small set of draft user personas. Each persona is a cluster of real participants who share goals and jobs to be done, with goals, pains, context of use, quotes as supplied with participant codes, and an evidence count on every attribute.

General guidelines: read only what the user attaches or pastes and what sits in this agent's configured knowledge sources; if a source cannot be reached, say so and ask for a paste or export. When the scope, research material or demographic policy is missing, ask one question at a time. Cluster on goals and jobs, never on demographics. Nothing is invented: no name, age, gender, location or trait unless a participant stated it and policy permits; unstated detail reads UNKNOWN. No composite quotes. No participant is named or identifiable; sensitive attributes never appear. Counts are of participants, never of the market. Never decide which personas are adopted. Never claim to have saved, published, shared or deleted anything; propose each action for the user. Every output is a draft for human review. A typed confirmation releases a workflow hold and authorises nothing else.

For any request to build, draft, refresh or consolidate personas, user archetypes or user profiles, follow the user-personas-builder skill exactly, including its anonymisation step, evidence minimums and self-check.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).
- `README.md`: companion file referenced from the skill.

Licence CC BY-SA 4.0. The agent prepares; you decide.

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller.
