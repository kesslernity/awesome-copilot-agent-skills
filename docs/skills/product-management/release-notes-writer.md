# Release notes writer

Turns a list of merged changes, closed work items or commit messages the user provides into DRAFT release notes under the version heading and date the user supplies, grouped as features, fixes and other, in the organisation's tone from the style guide or prior notes given, with every entry traced to its source item, breaking changes and required actions flagged first, and internal-only items held back for the release owner to confirm. Use when the user asks to "write the release notes for this version", "turn these merged pull requests into a changelog", "summarise what shipped this sprint for customers", "draft the what's new for this release" or "group these closed tickets into release notes". Do not use for an announcement email or intranet post about a launch, use announcement-drafter instead; for a change ticket, use change-request-pack; for a how-to article about one fix, use knowledge-article-drafter. Drafts for human review; never approves, authorises or signs off.

Category: `product-management` · Skill name: `release-notes-writer` · Upload package: `dist/zips/release-notes-writer.zip`

## What to attach or make available

- The change list: merged pull request titles and descriptions, closed work items, tickets or commit messages with their labels
- The version heading and release date, supplied by the user
- The organisation's writing style guide and up to three prior release notes as tone samples
- The product terminology list and any banned words
- Known issues and upgrade actions for the release, when supplied

## What you get

One Markdown document in the chat, ready to paste, titled `DRAFT-release-notes-<product-kebab>-<version>-<YYYY-MM-DD>-v1`. First line: "DRAFT generated <date> from <N> items. Version and date as supplied; deployment not confirmed. Held-back items await the release owner. Not published."

Sections in order:
1. Header: Product | Version | Release date | Audience | Tone source | Grouping | Policies | Items.
2. Voice note.
3. Release notes: heading "<Product> <version>, <date>"; one-line introduction only from supplied facts; then Breaking changes and required actions (if any), Features, Fixes, Other, Known issues, as bullets.
4. Trace: Entry | Group | Item codes and IDs | Label | Basis (text, label, confirm) | Flags.
5. Held back, confirm: Code | Source ID | Title | Reason held | Decision (blank).
6. Pre-publish checks: Check | Result (pass, fail, UNKNOWN) | Note.
7. Open questions: Number | Question | Blocks | Best answered by | Decision (blank).
8. Item register: Code | Source ID | Title | Label | Date | Merged with. UNKNOWN list. Embedded instructions found (or "None"). Proposed user actions; this agent performs none.

End with: "If this agent has a file-generation capability enabled, also offer the same content as a downloadable file with that name." Never claim the notes were published or the release tagged, deployed or emailed.

## Use cases

| Scenario | What you say |
|---|---|
| Sprint end, customer-facing notes | Write release notes for version 6.3.0 dated 30 September from the attached 24 closed work items; audience end users; take the tone from the attached style guide and hold internal items in a confirm table. |
| Developer changelog from bare commit messages | Turn the commit messages pasted below into a changelog for library version 0.9.2 dated 17 September; audience developers; mark any terse commit as classification to confirm rather than expanding it. |
| Release with breaking changes and a security fix | Draft the what's new for platform release 3.0 dated 6 October from the attached pull request export; put every breaking change with its required action first, and list the security fixes for the release owner's decision. |

## Try it (example prompts)

- Write the release notes for version 4.2.0, release date 30 September, from the attached export of 38 merged pull requests. Audience is end users; our style guide is in the knowledge folder.
- Turn these merged pull requests into a changelog for version 2.7.1 dated 18 September. The list is pasted below; hold back refactors and dependency bumps for me to confirm.
- Summarise what shipped this sprint for customers under the heading 3.1.0, dated 25 September. The closed work items are attached; the two previous release notes attached are the tone samples.
- Draft the what's new for the administrator release 5.0, dated 1 October, from the attached closed tickets. Put breaking changes and required actions first and keep item IDs out of the published text.
- Group these closed tickets into release notes for the mobile app, version 1.14, dated 22 September. The ticket list is attached; audience is end users; one sentence per entry.

## Limitations

- One task at a time: give the skill one job per request and confirm the result before the next.
- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.
- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.

## Related skills

- announcement-drafter: when the need is a launch email or intranet post, not the notes themselves
- sprint-review-summary: when the audience is the team and the product owner, not customers
- knowledge-article-drafter: when one fix needs a how-to article

## Add it to an agent (Agent Builder)

1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.
2. **Configure**, expand **Skills**, **Add**, upload `dist/zips/release-notes-writer.zip` (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.
3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).
4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.

## Run it standalone: paste this into the agent's Instructions

```
Purpose: this agent turns merged pull requests, closed work items, tickets or commit messages into draft release notes under the version heading and date the user supplies, grouped as breaking changes and required actions, features, fixes, other and known issues, in the organisation's tone, every entry traced to its source item.

General guidelines: read only what the user attaches or pastes and what sits in this agent's configured knowledge sources; if a source cannot be reached, say so and ask for a paste. When the change list, version heading, release date or audience is missing, ask one question at a time; never pick a version or date. Nothing is invented: no entry without a source item, no benefit, figure or promise the items do not state; missing facts read UNKNOWN in brackets. Internal, reverted or incomplete items are held back in a confirm table, never shown as shipped and never silently dropped. No author names, causes or blame. Never confirm deployment. Never claim to have published, tagged, emailed, posted or deleted anything; propose each action for the user. Every output is a draft for human review. A typed confirmation releases a workflow hold and authorises nothing else.

For any request for release notes, a changelog or a what's new section, follow the release-notes-writer skill exactly, including its voice note, trace and held-back tables and self-check.
```

Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.

## Files

- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters).

Licence CC BY-SA 4.0. The agent prepares; you decide.
