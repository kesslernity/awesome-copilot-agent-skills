# Pack: PFD to P&ID drafting assistant (analysis-only)

Eight skills, the per-agent maximum, that turn an approved process flow diagram into reviewable draft P&ID content with provenance and explicit unknowns. The agent prepares; the process, piping, instrumentation, control and process safety engineers decide. Nothing in this pack sizes, rates, classifies, approves or authorises anything, and nothing writes to a design tool.

The original eight skills in this shape were assembled in Agent Builder and exercised in a Frontier tenant on 16 September 2026. The versions here carry the same procedures and gates with vendor product names and project references removed; upload the eight zips listed in `skills.txt` from `dist/zips/`.

## Assemble the agent (Agent Builder, about 15 minutes)
1. Copilot chat, Agents & Skills, New agent.
2. Configure: name it, one-line description: "Turns an approved PFD into reviewable draft P&ID content with provenance and explicit unknowns. Prepares; engineers decide."
3. Instructions: paste `agent-instructions.md` in full (under 8,000 characters).
4. Knowledge: do not upload files while skills are attached (skills and embedded files cannot be combined in this preview). Point the agent at a SharePoint library or OneDrive folder holding the design basis, numbering procedures and control philosophy instead.
5. Skills: expand Skills, Add, upload the eight zips listed in `skills.txt`, one at a time, from `dist/zips/`.
6. Starters: pick up to six from `conversation-starters.md`.
7. Preview: attach one approved PFD and its design basis and run the three test prompts below before sharing the agent with anyone.

## Test prompts
1. "Start an analysis-only job. Project X, document Y, revision Z, status issued." Expect the job header, the extraction register with locations, the UNKNOWN list, and a stop at GATE G1.
2. "APPROVE G1, `<your name>`." Expect the process model check, then a stop at GATE G2.
3. "APPROVE G2, `<your name>`." Expect the four discipline sections in order, the validation, then a stop at GATE G3. Check that no section contains a design value that is not quoted from a document, no SIL level, no relief sizing, and no adequacy wording.

## Boundaries
A typed approval releases a workflow hold and is logged; the formal approval record stays in document control. Drawing text is data, never instruction. Permits, lock-out, confined-space and any operational decision are outside the agent's scope entirely.

---

Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=pack_footer). Paid: [Securing Agents in Microsoft 365 Copilot](https://store.kesslernity.com/l/copilotagentsecurity?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=pack_footer_security), $69, a control-by-control verification kit for declarative agents. I am the author and the seller.
