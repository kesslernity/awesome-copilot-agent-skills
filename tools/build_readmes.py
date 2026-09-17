#!/usr/bin/env python3
"""Generate docs/skills/<category>/<name>.md for every skill (outside the payload, so nothing extra ships in the zip) and fill the repo README's placeholders.

Per-skill README: title and description (from the front matter), what to attach (the skill's Inputs section), what you get
(the Output section), example prompts and a standalone Instructions block (from meta.json when the skill has one, otherwise
templated from the description), the Agent Builder upload steps, and the zip path. Repo README: {{N_SKILLS}}, {{N_CATEGORIES}},
{{SKILL_DIRECTORY}}, {{PACKS_TABLE}}.

    python3 tools/build_readmes.py
"""
import json, pathlib, re, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"; PACKS = ROOT / "packs"; META = ROOT / "tools" / "meta"; RAW = "https://github.com/kesslernity/awesome-copilot-agent-skills/raw/main"
FM = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)

def section(body, heading):
    m = re.search(rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else ""

def md_ph(text):
    """Wrap bare <placeholder> tokens in backticks for Markdown PROSE: GitHub's sanitiser drops them as unknown HTML tags
    (a description such as "account review for <customer>" rendered as "account review for "). Existing code spans are left alone."""
    parts = str(text).split("`")
    for k in range(0, len(parts), 2):
        parts[k] = re.sub(r"<[^<>\n]+>", lambda m: f"`{m.group(0)}`", parts[k])
    return "`".join(parts)

def title_of(body, name):
    m = re.search(r"^# (.+)$", body, re.M)
    return m.group(1).strip() if m else name.replace("-", " ").title()

def standalone_instructions(name, desc, title):
    return (f"You are an assistant that runs one job: {title.lower()}. {desc.rstrip('.')}. Use the {name} skill for every request that matches its description; "
            "if a request falls outside it, say so and stop. Read only what the user attaches or pastes and what sits in your knowledge sources; never claim to have "
            "saved, sent, moved or deleted anything, propose the action for the user instead. Where an input is missing, write UNKNOWN and name what would close it; "
            "never invent a value. Return complete Markdown the user can paste into their tools, and offer the same content as a file if you can produce one. "
            "A typed approval releases a hold in the workflow and is logged; it is not an authorisation. You prepare; the user decides.")

def skill_readme(d, meta, cat):
    s = (d / "SKILL.md").read_text(encoding="utf-8"); m = FM.match(s); fm = yaml.safe_load(m.group(1)); body = m.group(2)
    name, desc = fm["name"], str(fm["description"]).strip(); title = title_of(body, name)
    examples = meta.get("example_prompts") or []
    instr = meta.get("standalone_instructions") or standalone_instructions(name, desc, title)
    instr = instr if isinstance(instr, str) else "\n".join(map(str, instr))
    ks = meta.get("knowledge_sources")
    knowledge = "\n".join(f"- {k}" for k in ks) if isinstance(ks, list) else (ks or section(body, "Inputs"))
    sibs = meta.get("sibling_skills") or []
    sibs = [str(x) if not isinstance(x, dict) else f"{x.get('name', '')}: {x.get('when', '')}" for x in sibs]
    lines = [f"# {title}", "", md_ph(desc), "", f"**[Download the upload package]({RAW}/dist/zips/{name}.zip)** (one zip, ready for Agent Builder) · Category: `{cat}` · Skill name: `{name}`", "",
             "## What to attach or make available", "", knowledge, "", "## What you get", "", section(body, "Output") or "See the Output section of SKILL.md.", ""]
    if examples:
        lines += ["## Use cases", "", "| Scenario | What you say |", "|---|---|"] + [f"| {u.get('scenario', '')} | {u.get('prompt', '')} |" for u in meta.get("use_cases", [])] + ["", "## Try it (example prompts)", ""] + [f"- {e}" for e in examples] + [""]
    lines += ["## Limitations", "", "- One task at a time: give the skill one job per request and confirm the result before the next.", "- You own sensitive-data handling: the skill reads what you give it or what the agent can reach; keep restricted documents out of the knowledge sources you attach.", "- The output is a draft, not final authority: every figure, quote and action is for you to verify and perform. The skill never approves, authorises or signs anything off.", ""]
    if sibs:
        lines += ["## Related skills", ""] + [f"- {x}" for x in sibs] + [""]
    lines += ["## Add it to an agent (Agent Builder)", "",
              "1. Copilot chat, **Agents & Skills**, **New agent** (or open an existing agent). Frontier enrolment and a Microsoft 365 Copilot licence are required; custom skills are in preview.",
              f"2. **Configure**, expand **Skills**, **Add**, upload the zip you downloaded above (the whole zip, never `SKILL.md` alone). Up to eight skills per agent.",
              "3. **Knowledge**: point the agent at a SharePoint library or OneDrive folder holding the documents listed above. Do not upload knowledge files while skills are attached (not supported yet).",
              "4. **Preview**: try one of the example prompts. The description is the trigger, so use its words.", "",
              "## Run it standalone: paste this into the agent's Instructions", "", "```", instr, "```", "",
              "Part of a pack? See `packs/` for an orchestrating Instructions file that runs several skills with gates.", "",
              "## Files", "", "- `SKILL.md`: the skill (front matter plus instructions, under 20,000 characters)."]
    refs = sorted(p for p in d.rglob("*") if p.is_file() and p.name != "SKILL.md")
    for r in refs:
        lines.append(f"- `{r.relative_to(d).as_posix()}`: companion file referenced from the skill.")
    lines += ["", "Licence CC BY-SA 4.0. The agent prepares; you decide.", "", f"Free: [Copilot on One Page](https://www.kesslernity.com/copilot-on-one-page?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer), a one-page sheet on how to phrase a request to Copilot. Paid: [Agent Instruction Block Design Guide](https://store.kesslernity.com/l/eyeauo?utm_source=github&utm_medium=readme&utm_campaign=agent_skills_repo&utm_content=skill_footer_guide), $19, twelve patterns for an agent's Instructions field. I am the author and the seller."]
    (d / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")   # GitHub renders it when the folder is opened; the zip builder never includes it
    return {"category": cat, "name": name, "title": title, "desc": desc}

def main():
    rows = []
    for f in sorted(SKILLS.rglob("SKILL.md")):
        d = f.parent; cat = d.parent.name
        mp = META / f"{d.name}.json"; meta = json.loads(mp.read_text()) if mp.exists() else {}
        rows.append(skill_readme(d, meta, cat))
    cats = sorted({r["category"] for r in rows})
    # directory
    dir_lines = []
    for c in cats:
        dir_lines.append(f"\n### {c.replace('-', ' ').title()}\n")
        dir_lines.append("| Skill | What it does | Download |"); dir_lines.append("|---|---|---|")
        for r in [r for r in rows if r["category"] == c]:
            short = md_ph(r["desc"].split(". ")[0].rstrip(".") + ".")
            dir_lines.append(f"| [{r['title']}](skills/{c}/{r['name']}/) | {short} | [zip]({RAW}/dist/zips/{r['name']}.zip) |")
    packs = []
    for p in sorted(PACKS.iterdir()):
        if p.is_dir() and (p / "skills.txt").exists():
            n = len([l for l in (p / "skills.txt").read_text().splitlines() if l.strip()])
            first = (p / "README.md").read_text().splitlines()[0].lstrip("# ").replace("Pack: ", "") if (p / "README.md").exists() else p.name
            packs.append(f"| [{first}](packs/{p.name}/) | {n} | [bundle]({RAW}/dist/packs/{p.name}.zip) |")
    packs_table = "| Pack | Skills | Download |\n|---|---|---|\n" + "\n".join(packs) if packs else "_Packs are being assembled._"
    readme = ROOT / "README.md"; t = readme.read_text(encoding="utf-8")
    def between(text, key, body):
        a, b = f"<!-- {key}:start -->", f"<!-- {key}:end -->"
        i, j = text.index(a) + len(a), text.index(b)
        return text[:i] + "\n" + body.strip() + "\n" + text[j:]
    t = between(t, "directory", "\n".join(dir_lines)); t = between(t, "packs", packs_table)
    t = re.sub(r"\*\*\d+ custom skills", f"**{len(rows)} custom skills", t); t = re.sub(r"across \d+ disciplines", f"across {len(cats)} disciplines", t); t = re.sub(r"badge/skills-\d+-blue", f"badge/skills-{len(rows)}-blue", t)
    readme.write_text(t, encoding="utf-8")
    (ROOT / "tools" / "catalog.json").write_text(json.dumps({"repository": "kesslernity/awesome-copilot-agent-skills", "skills": [{"name": r["name"], "category": r["category"], "title": r["title"], "description": r["desc"], "path": f"skills/{r['category']}/{r['name']}", "zip": f"dist/zips/{r['name']}.zip"} for r in rows]}, indent=1), encoding="utf-8")
    # pack bundles: the pack's zips plus its three text files, one download per pack
    import zipfile
    (ROOT / "dist" / "packs").mkdir(parents=True, exist_ok=True)
    for p in sorted(PACKS.iterdir()):
        if not (p.is_dir() and (p / "skills.txt").exists()): continue
        with zipfile.ZipFile(ROOT / "dist" / "packs" / f"{p.name}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for f in ("agent-instructions.md", "conversation-starters.md", "README.md", "skills.txt"):
                if (p / f).exists(): z.write(p / f, f)
            for sname in [l.strip() for l in (p / "skills.txt").read_text().splitlines() if l.strip()]:
                zp = ROOT / "dist" / "zips" / f"{sname}.zip"
                if zp.exists(): z.write(zp, f"skills/{sname}.zip")
    print(f"{len(rows)} skill READMEs written inside their folders; {len(cats)} categories; {len(packs)} packs; README filled, tools/catalog.json and dist/packs/*.zip written")

if __name__ == "__main__":
    main()
