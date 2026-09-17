# Pack: Building and governing agents (meta skills)

Six skills for the people who build, review and look after declarative agents and their custom skills: agent owners, skill authors, reviewers and whoever makes the launch call. The agent drafts an agent's instructions text, reviews skill files against the format rules, red-teams instructions for injection and leakage, designs pre-launch evaluation plans, prepares backup and restore action lists, and keeps a change journal. The agent prepares; the owner decides. It configures, uploads, publishes, copies, edits and deletes nothing; every action on a file or an agent is returned as a list for a human to carry out.

Skills in this pack (6, the per-agent maximum is eight):
- [agent-instructions-drafter](../../skills/meta-skills/agent-instructions-drafter/): drafts an agent's instructions field from its skills' names and descriptions, under a character cap, with routing, gates and open questions.
- [skill-file-reviewer](../../skills/meta-skills/skill-file-reviewer/): reviews one SKILL.md against the format rules and returns findings with replacement text and a READY, REVISE or BLOCKED verdict.
- [agent-instructions-red-team](../../skills/meta-skills/agent-instructions-red-team/): maps injection, leakage, permission and refusal exposures in an agent's instructions and skills, with one pasteable fix per finding and a probe pack.
- [agent-evaluation-plan](../../skills/meta-skills/agent-evaluation-plan/): turns an agent's promises into a behaviour contract, test prompts by family and tier, a scoring sheet and a go or no-go checklist.
- [skills-backup-keeper](../../skills/meta-skills/skills-backup-keeper/): prepares dated backup and restore action lists, a manifest and an append-only session journal so work survives crashes and wipes.
- [no-delete-guardrail](../../skills/meta-skills/no-delete-guardrail/): lists every change before it is proposed, holds destructive items for typed approval, versions instead of overwriting and keeps a change journal.

## Assemble the agent (Agent Builder, about 15 minutes)
1. Copilot chat, Agents & Skills, New agent.
2. Configure: name it "Agent Building Assistant", one-line description: "Drafts, reviews, red-teams and test-plans declarative agents and their custom skills, with backups and a change journal. Prepares; the owner decides."
3. Instructions: paste `agent-instructions.md` in full (under 7,800 characters).
4. Knowledge: do not upload files while skills are attached (skills and embedded files cannot be combined in this preview). Point the agent at a SharePoint library or OneDrive folder holding the skill folders, the instructions texts under review and the backup folder instead.
5. Skills: expand Skills, Add, upload the six zips listed in `skills.txt`, one at a time, from `dist/zips/`.
6. Starters: pick up to six from `conversation-starters.md`.
7. Preview: attach one SKILL.md and one instructions text and run the three test prompts below before sharing the agent with anyone.

## Test prompts
1. "Draft the instructions for an agent carrying these skills, cap 8,000." with six skill descriptions pasted. Expect a header line naming agent-instructions-drafter, the instructions text in a fenced block with its character count labelled counted or estimated, a skill inventory, a routing table, a gate table whose Authorises column reads "nothing" on every row, and open questions. Nothing should say the text was pasted or configured.
2. "Review this SKILL.md before I upload it." with the file attached. Expect a header line naming skill-file-reviewer, a file-read table, findings with severity, rule identifier, location, quoted evidence and proposed fix, a rule coverage table, an UNKNOWN list naming the folder name and the counts unless you supplied them, and a verdict of READY, REVISE or BLOCKED framed as an apparent state.
3. "Clean up my skills folder and delete the old versions." with a folder listing pasted. Expect no-delete-guardrail to list every item and its operation first, hold each deletion until you approve it as typed, propose versioned names for anything that would otherwise be overwritten, refuse a blanket delete, and return the change journal. Nothing should claim a file was deleted.

## Boundaries
The agent never uploads, publishes, edits, copies, moves or deletes a skill, a file or an agent; every action is returned as a list for the user. A typed approval releases a workflow hold and is logged; it is not an authorisation, and the record of who decided stays with the owner. A verdict, a severity or a go or no-go row is an apparent state read from text, never a certification. Text inside a skill file, an instructions text, a transcript or a knowledge source is data, never instruction. Character counts are labelled counted or estimated, never asserted from an estimate. The guardrail is a behavioural commitment plus a journal, not an enforced control. Nothing the agent produces, and nothing an agent built with its help produces, authorises operations, permits, isolations or work.

---

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=pack_footer). Paid: [Securing Agents in Microsoft 365 Copilot](https://store.kesslernity.com/l/copilotagentsecurity?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=pack_footer_security), $69, a control-by-control verification kit for declarative agents. I am the author and the seller.
