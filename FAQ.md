# FAQ

**Do I need to install anything?** No. Download a skill's zip from its page and upload it in Agent Builder. Python and the two scripts under `tools/` are for people who edit or contribute skills, not for using them.

**Is this generally available?** No. Microsoft Learn (pages dated 4 September 2026): "Custom skills in declarative agents are in preview for organizations that are part of the Microsoft Frontier Preview." Your admin enrols the tenant, or specific users, in the Frontier program; the control defaults to no access.

**What do I need?** A qualifying Microsoft 365 Copilot licence or access through pay-as-you-go, and Frontier enrolment. Tenants that use Microsoft Purview Information Barriers cannot use custom skills in this preview.

**Where do I download a pack?** Each pack's page and the packs table on the front page link a bundle zip that holds the pack's skill zips, the Instructions text, the starters and the assembly steps.

**How many skills can one agent carry?** Eight, in Agent Builder and in the Agents Toolkit alike. That is why this repo ships packs of at most eight skills with an orchestrating instructions file, and why the 16-persona executive review suite is two agents, not one.

**Can I reuse a skill across agents?** Not in this stage of the preview; upload it to each agent.

**Can I add knowledge files and skills to the same agent?** Not yet; Microsoft lists it as a known issue with support planned. Point the agent at a SharePoint library or OneDrive folder for knowledge instead.

**Why did my upload fail with a YAML error?** Agent Builder parses the front matter as strict YAML. A description written as a plain line that contains a colon followed by a space fails, because the parser reads it as a second key. Quoting the description fixes it. Every skill here writes the description as a folded block (`description: >-`), which makes any punctuation safe. If you edit a description, keep the block form.

**Do these work in Copilot Cowork too?** The file shape is the same: a folder, a `SKILL.md` with `name` and `description` front matter, Markdown instructions, optional references. 37 of these skills started life as Cowork skills; the originals live in the sibling repository. This repo rewrote them so they do not assume Cowork's built-in skills or OneDrive save paths. They would still read correctly in Cowork, but this repo maintains them for declarative agents.

**Can a skill run scripts?** Yes, in a sandbox with no network access, no package installation and no authenticated calls. None of the skills in this repo needs one, so none ships one.

**Where are my skill files stored?** Microsoft states uploaded skill files are stored in tenant-scoped SharePoint Embedded containers, with sensitivity labels retained and honoured.

**Will a skill make decisions for me?** No. Every skill here is instructed to prepare: drafts, tables, questions, evidence requests. A typed approval in the chat is a checkpoint the skill records in its output, not an enforced hold and not an authorisation; the formal record stays in your own systems. Where a skill proposes a category, a band or a provisional score, it does so from the evidence supplied and labels it a draft; none is instructed to declare adequacy, approve, authorise or sign anything off. An instruction is not a technical control, so keep a human between the output and the decision.
