# Security and trust

What is inside every skill folder in this repository, and what is not:

- **Plain files you can read before you upload.** One `SKILL.md` (front matter plus Markdown instructions) and, where present, a `references/` folder of Markdown. Nothing else ships in the zip.
- **No scripts.** None of the skills executes code. Microsoft's sandbox for skill scripts has no network access and no package installation; these skills need neither.
- **No network, no connectors from inside a skill.** A skill reads what the user attaches or pastes and what the agent's configured knowledge sources hold. Connectors, plugins and MCP servers are the agent's business, configured by the tenant, not the skill's.
- **Drafts only.** Every skill is instructed to prepare: tables, drafts, questions, evidence requests. Where one proposes a category, a band or a provisional score, it does so from the evidence supplied and labels it a draft; none is instructed to declare adequacy, approve, authorise or sign anything off. A typed approval in the chat is a checkpoint the skill records in its output, not an enforced hold and not an authorisation; there is no audit log outside your own systems. Instructions are not technical controls, which is why the last line of this file is not decoration.
- **Safety-critical boundary.** No skill advises or performs safety authorisation of any kind: permit-to-work, isolation and lock-out, confined-space entry, job safety analysis approval, incident classification, inspection sign-off. Where a skill touches process safety it produces questions for the responsible engineer and quotes the documents, nothing more.
- **Verification before upload.** `python3 tools/check_skills.py` asserts the published limits and this repo's rules, including strict YAML front matter, allowed file types, depth, size and the absence of hidden files, and rebuilds the zips.

Treat a skill zip like any other file entering your tenant: it is stored in a tenant-scoped SharePoint Embedded container, sensitivity labels are honoured, and it should pass the same review as an attachment from outside. Report a problem with a skill by opening an issue; do not include tenant data in the report.

Disclaimer: these skills are provided for demonstration and educational purposes. Test them in your own environment before relying on them for anything that matters, and keep a human between any output and any decision.
