# Awesome Copilot Agent Skills

> **{{N_SKILLS}} custom skills for Microsoft 365 Copilot declarative agents, across {{N_CATEGORIES}} disciplines, plus ready-to-assemble packs of eight.** Upload a zip in Agent Builder or add the folder with the Agents Toolkit. Every skill is a folder you can read before you trust it.

> **Status: preview.** Microsoft Learn, pages dated 4 September 2026: "Custom skills in declarative agents are in preview for organizations that are part of the Microsoft Frontier Preview." Not available in tenants that use Purview Information Barriers. You need a qualifying Microsoft 365 Copilot licence (or pay-as-you-go access) and Frontier enrolment.

[![GitHub stars](https://img.shields.io/github/stars/kesslernity/awesome-copilot-agent-skills?style=flat-square)](https://github.com/kesslernity/awesome-copilot-agent-skills/stargazers)
[![Licence: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![Skills](https://img.shields.io/badge/skills-{{N_SKILLS}}-blue)](skills/)

Optional reading, not required to install or use anything here: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=hero), the free one-page sheet on phrasing prompts that these skills assume.

**Trust first.** Every folder holds plain files you can read before you upload: one `SKILL.md` and, where present, a `references/` folder of Markdown. No scripts, no network, no connectors from inside a skill, drafts only, and no safety authorisation of any kind. Details and the disclaimer: [SECURITY.md](SECURITY.md).

---

## Who this is for

You build agents in Agent Builder or the Agents Toolkit for a Microsoft 365 Copilot tenant that is in the Frontier program, and you want the agent to do a specific job the same way every time: a month-end close checklist, a blameless postmortem, an NDA triage, a P&ID discipline check. Each skill packages one such job as instructions the agent loads only when the task calls for it.

Everyone else, there is a sibling repo for you:

- **Copilot Cowork user?** [awesome-copilot-cowork-skills](https://github.com/kesslernity/awesome-copilot-cowork-skills): the same skill idea as a folder drop into OneDrive, no admin, no Studio. 37 of the skills here started life there.
- **No Copilot licence?** [awesome-copilot-chat-agents](https://github.com/kesslernity/awesome-copilot-chat-agents): 82 agents for the free Copilot Chat tier.
- **Governed, org-wide agent in Copilot Studio?** [awesome-copilot-studio-agents](https://github.com/kesslernity/awesome-copilot-studio-agents): 103 declarative agents.
- **Just prompts?** [awesome-microsoft-copilot-prompts](https://github.com/kesslernity/awesome-microsoft-copilot-prompts).

---

## What a skill is (60 seconds)

Microsoft's definition: a skill is a directory with a required `SKILL.md` (a name and a description in YAML front matter, then instructions under 20,000 characters), optional resource files, optional scripts. The agent loads a skill's contents into context only when the task needs it, which is how an agent carries far more guidance than the 8,000-character instructions field allows.

Every skill in this repo:

- has exactly two front-matter keys, `name` (kebab-case, equal to the folder name) and `description` as a folded block (`description: >-`). **Agent Builder parses the front matter as strict YAML**: a plain description with a colon followed by a space in it fails the upload (the parser reads a second key). Quoting also works; the folded block is what this repo uses. Learned on a real upload, 16 September 2026.
- uses the same eight headings: Purpose, When to use, Inputs, Procedure, Output, Fallbacks and edge cases, Rules, Self-check.
- is capability-neutral. It reads what the user attaches or pastes and what sits in the agent's knowledge sources; it never claims to have saved, sent, moved or deleted anything. Outputs are complete Markdown in the chat, with a downloadable file offered when the agent has that capability.
- prepares and never decides. Drafts, tables, questions and evidence requests. UNKNOWN where the data is missing. A typed approval in the chat is a checkpoint the skill records in its output, not an enforced hold and not an authorisation. Where a skill proposes a category, a band or a provisional score, it does so from the evidence supplied and labels it a draft; nothing is instructed to declare adequacy, approve, authorise or sign off, and nothing touches permits, isolations or operational decisions.
- ships no scripts. The sandbox has no network and no package installation; none of these jobs needs code.

---

## Install

### Agent Builder (zip upload, about two minutes per skill)

1. Download the skill's zip from [`dist/zips/`](dist/zips/) (one zip per skill, `SKILL.md` at the root, exactly the tree Microsoft's page shows). Or clone the repo and run `python3 tools/check_skills.py` to rebuild every zip.
2. In Copilot chat, select **Agents & Skills**, then **New agent** (or open an existing agent).
3. **Configure**, expand **Skills**, select **Add**, upload the complete zip. Never upload `SKILL.md` on its own.
4. Review the name, description, instructions and files it shows you. Open **Preview** and try one of the trigger phrases from the skill's description.

Up to eight skills per agent, 50 MB per zip. Do not attach knowledge files to an agent that carries skills: in this preview the two cannot be combined (Microsoft lists it as a known issue). Point the agent at a SharePoint library or OneDrive folder instead.

### Agents Toolkit (directory)

Set `TEAMSFX_AGENT_SKILLS=true`, use declarative agent manifest version 1.9, then from your agent project: `atk add skill --from <path to the downloaded skill folder>` (an absolute path, or copy the folder into the project first) and `atk provision --env local`. The app package is limited to 10 MB in total.

### Other doors, same files

- **Copilot Cowork.** The same folder shape is a Cowork custom skill: copy a skill folder into your OneDrive under `Documents/Cowork/skills/<skill-name>/` (the path Microsoft documents, relative to the OneDrive root) and start a new conversation. The Cowork-native versions of 37 of these skills live in the sibling repository.
- **Cowork plugin for a whole tenant.** The repo carries `.claude-plugin/plugin.json`, the structure Microsoft documents for `atk import openplugin --path <this repo> --output <project folder> --privacy-url <url> --terms-url <url>`, which builds a Cowork plugin package (a Microsoft 365 app manifest) from a skills bundle; the package then deploys through the admin centre's integrated apps page. Trim `.claude-plugin/marketplace.json` to the skills you want first. Documented by Microsoft, not yet exercised from this repository.
- **Claude Code.** `/plugin marketplace add kesslernity/awesome-copilot-agent-skills` then install the bundle; the skills read the same way there.

---

## Packs: eight skills, one agent

Because an agent carries at most eight skills, the repo groups skills into packs with an orchestrating `agent-instructions.md` (under 8,000 characters), conversation starters and the list of zips to upload. See [`packs/`](packs/). The first pack, [PFD to P&ID drafting assistant](packs/engineering-pfd-to-pid/), was assembled in Agent Builder and exercised in a Frontier tenant on 16 September 2026.

{{PACKS_TABLE}}

---

## Skill directory

{{SKILL_DIRECTORY}}

---

## Checking your own skills

`python3 tools/check_skills.py` asserts every limit on Microsoft's support matrix (front matter as strict YAML, instructions under 20,000 characters, eight skills per pack, allowed file types, depth of three, 25 MB per file, 50 MB per zip) plus this repo's rules, then rebuilds `dist/zips/`. Point it at your own `skills/` folder before an upload and the YAML error never reaches Agent Builder.

---

## Limits, from Microsoft's support matrix

| Item | Agent Builder | Agents Toolkit |
|---|---|---|
| Skills per agent | 8 | 8 |
| Skill package | .zip, up to 50 MB | directory (no .zip); app package up to 10 MB |
| File size | 25 MB per file | no skill-level limit |
| Files across all skills | 350 | 350 (the Toolkit how-to says 400) |
| Directory depth | 3 | 3 |
| Reuse across agents | not at this stage of the preview | not at this stage of the preview |
| Scripts | sandbox: no network, no package installation | same |
| Skills plus embedded knowledge files | not yet supported | not yet supported |

Sources: Microsoft Learn, "Custom skills in declarative agents (preview)", "Add custom skills to your declarative agent in Agent Builder", "Add custom skills to a declarative agent created with Microsoft 365 Agents Toolkit", all last updated 4 September 2026.

---

## Contributing

One skill per folder, run the checker, open a pull request. Rules in [CONTRIBUTING.md](CONTRIBUTING.md); questions in the [FAQ](FAQ.md).

## Disclaimer

Provided for demonstration and educational purposes. Test every skill in your own environment before relying on it, verify every figure and quote it produces, and keep a human between any output and any decision. Nothing here authorises operations, permits, isolations or work.

## Licence

[CC BY-SA 4.0](LICENSE), the same as the sibling repositories. Reuse, adapt and redistribute with attribution, under the same licence.

## More from Kesslernity

- [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=footer): the free one-page sheet for phrasing prompts.
- [Free Copilot field guides](https://www.kesslernity.com/guides?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=footer): open guides, no email at the door.
- [AI at Work newsletter](https://newsletter.kesslernity.com/?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=footer): what changed in Copilot, every other Tuesday.
