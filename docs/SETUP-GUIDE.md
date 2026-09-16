# Setup guide: from a skill folder to a working agent

Everything here follows Microsoft Learn's pages on custom skills in declarative agents (last updated 4 September 2026) plus what a real upload taught us on 16 September 2026. Where the pages are silent, this guide says so.

## 0. Before you start: are you allowed in?

- **Preview, Frontier only.** "Custom skills in declarative agents are in preview for organizations that are part of the Microsoft Frontier Preview." Your Microsoft 365 admin enrols the tenant or specific users in the Frontier program (the control defaults to no access). If you cannot see **Agents & Skills** in Copilot chat, or an agent's Configure pane has no **Skills** section, you are not in yet: ask the admin, not the licence desk.
- **Licence.** A qualifying Microsoft 365 Copilot licence, or access through pay-as-you-go.
- **Two blockers you cannot work around.** Tenants that use Microsoft Purview Information Barriers cannot use custom skills in this preview. And an agent cannot carry both custom skills and embedded knowledge files yet (support is planned); put the knowledge in a SharePoint library or OneDrive folder instead.

## 1. Pick what to build: one skill or a pack

- **One skill, standalone.** Good for trying the format. Each skill folder has a `README.md` with an Instructions block you can paste into the agent, example prompts, and the knowledge it expects.
- **A pack.** An agent carries at most eight skills, so `packs/<pack-name>/` groups up to eight skills around one job, with an `agent-instructions.md` (the orchestrator, under 8,000 characters), `conversation-starters.md`, `skills.txt` (the zips to upload) and a `README.md` with the assembly steps and test prompts. Start with a pack when the job has stages and gates; start with a skill when it is one task.

## 2. Get the files

Download the repo as a zip from the green **Code** button (or `git clone`). The upload packages are pre-built in `dist/zips/`, one per skill, with `SKILL.md` at the root of the zip, exactly the tree Microsoft's page shows:

```
my-skill.zip
|-- SKILL.md            # required
|-- references/         # optional, this repo's companion files
```

If you edit a skill, rebuild the zips: `python3 tools/check_skills.py` (needs PyYAML: `pip install pyyaml`). It also asserts every published limit before you ever open Agent Builder.

## 3. Door one: Agent Builder (no code, about ten minutes for a pack)

1. In Copilot chat, select **Agents & Skills**, then **New agent**.
2. **Configure** tab. Name the agent, give it a one-line description (the pack README suggests one), and paste the pack's `agent-instructions.md` into **Instructions**. For a standalone skill, paste the Instructions block from the skill's README.
3. **Knowledge.** Do not upload files while skills are attached (see section 0). Add a SharePoint site or OneDrive folder that holds the documents the skills expect: the skill README lists them under "What to attach or make available".
4. **Skills.** Expand **Skills**, select **Add**, upload one complete zip from `dist/zips/`. Repeat for every skill in the pack's `skills.txt`, up to eight. Upload the whole zip; never upload `SKILL.md` on its own.
5. **Starters.** Paste up to six lines from `conversation-starters.md`.
6. **Preview.** Run the pack's test prompts (in its README) or the skill's example prompts before you share the agent. The agent matches the request against the skill descriptions, so describe the task the way the description does; if the skill does not fire, rephrase the request first, then sharpen the description.
7. **Share** when the preview behaves. Sharing an agent that carries skills follows the same route as any agent you built.

Agent Builder can also create a skill from a natural-language description ("Add a reusable skill that always follows these steps ..."). That is how Microsoft demonstrates the feature; this repo gives you the finished folders instead, so you can read every line before you trust it.

## 4. Door two: Microsoft 365 Agents Toolkit (for people who build agents as code)

1. Set the environment variable `TEAMSFX_AGENT_SKILLS=true` before launching the CLI or Visual Studio Code (restart VS Code if it was open).
2. Your declarative agent manifest must be version 1.9.
3. From the agent project: `atk add skill --from <path to the downloaded skill folder>` for each skill (a directory, not a zip; give an absolute path to the folder you downloaded, or copy it into the project first), then `atk provision --env local`.
4. The complete app package is limited to 10 MB; eight skills per agent; directory depth of three.

## 5. The one gotcha that will bite you first

**Agent Builder parses the `SKILL.md` front matter as strict YAML.** A description written as a plain line that contains a colon followed by a space fails the upload, because the parser reads it as a second key. Quoting the description fixes it; so does the folded block every skill in this repo uses:

```yaml
---
name: skill-name
description: >-
  What the skill produces, from what. Use when the user asks for ... or says ...
---
```

Keep that form if you edit a description. The checker fails on invalid YAML before you upload.

## 6. Limits to plan around

| Limit | Agent Builder | Agents Toolkit |
|---|---|---|
| Skills per agent | 8 | 8 |
| Package | .zip, up to 50 MB; 25 MB per file | directory; app package up to 10 MB |
| Files across all skills | 350 | 350 (Toolkit how-to says 400) |
| Directory depth | 3 | 3 |
| Instructions in `SKILL.md` | under 20,000 characters | same |
| Agent Instructions field | under 8,000 characters | same |
| Reuse a skill across agents | not at this stage of the preview | same |
| Scripts | sandbox: no network, no package installation | same |

## 7. For the admin: four lines for the rollout plan

1. Decide who is in Frontier and who may upload skill packages; the control is yours and defaults to no access.
2. Treat a skill zip like any other file entering the tenant: it is stored in a tenant-scoped SharePoint Embedded container, sensitivity labels are retained and honoured, and it should pass the same review as an attachment from outside.
3. Read the scripts. None of the skills here ships one; if a third-party skill does, the sandbox blocks network and package installs, but the script still runs against your data.
4. Put the Frontier gate and the model policy in the plan, and re-check this guide's Learn pages when the preview label changes.

## 8. When it does not work

| Symptom | First thing to check |
|---|---|
| No **Skills** section in Configure | Frontier enrolment for your account, then the Information Barriers exclusion |
| Upload rejected with a YAML or format error | The front matter (section 5); run the checker |
| Skill uploaded but never triggers | The description is the trigger. Use its words in the prompt; then sharpen the description |
| Knowledge files greyed out or missing after adding skills | Skills and embedded files cannot be combined yet; use SharePoint or OneDrive knowledge |
| Ninth skill will not add | Eight per agent; split into two agents (the executive review suite is two packs for this reason) |
| Agent answers as if it saved or sent something | It did not; every skill here is instructed to propose actions for you to perform, and an instruction is not a technical control. Report it as a skill bug if the wording implies otherwise |

## 9. Try it in Copilot Cowork instead

The file shape is the same folder-plus-`SKILL.md`. These skills were rewritten for agents and no longer assume Cowork's built-in skills or OneDrive save paths, so they read correctly there too, but the sibling repository awesome-copilot-cowork-skills is where the Cowork-native versions live and are maintained.
