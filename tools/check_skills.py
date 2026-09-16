#!/usr/bin/env python3
"""Check every skill under skills/ against the Microsoft Learn limits for custom skills in declarative agents (pages dated 2026-09-04)
and this repo's own rules, then build dist/zips/<skill>.zip with SKILL.md at the root of the zip (the shape Agent Builder uploads).

    python3 tools/check_skills.py            # check + build zips
    python3 tools/check_skills.py --no-zip   # check only

Exit 1 on any failure. Needs PyYAML (pip install pyyaml) because Agent Builder parses the front matter as strict YAML and rejects invalid YAML."""
import pathlib, re, sys, zipfile, json
try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml (Agent Builder rejects invalid YAML front matter, so the check must parse it the same way)")

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"; DIST = ROOT / "dist" / "zips"
ALLOWED = {".md", ".txt", ".json", ".xml", ".yaml", ".yml", ".ini", ".config", ".utf8", ".docx", ".doc", ".docm", ".pdf", ".rtf", ".ppt", ".pptx", ".ppsm", ".xlsx", ".xls", ".xlsm", ".csv", ".tsv", ".html", ".htm", ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".log",
           ".py", ".js", ".mjs", ".cjs", ".ts", ".mts", ".sh", ".bash"}
FORBIDDEN = [("—", "em dash"), ("–", "en dash"), ("Cowork", "Cowork reference"), ("/Documents/Cowork", "Cowork folder path"), ("built-in skill", "Cowork built-in"),
             ("Kesslernity", "brand name inside a skill"), ("http://", "URL"), ("https://", "URL"),
             ("SPPID", "vendor product name"), ("SmartPlant", "vendor product name")]
HEADINGS = ["## Purpose", "## When to use", "## Inputs", "## Procedure", "## Output", "## Fallbacks and edge cases", "## Rules", "## Self-check"]
FM = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)

def check(skill_dir):
    fails = []
    f = skill_dir / "SKILL.md"
    if not f.exists():
        return [f"{skill_dir}: SKILL.md missing"]
    s = f.read_text(encoding="utf-8")
    m = FM.match(s)
    if not m:
        return [f"{skill_dir}: no YAML front matter block"]
    fm, body = m.group(1), m.group(2)
    try:
        meta = yaml.safe_load(fm)
    except yaml.YAMLError as e:
        return [f"{skill_dir}: front matter is not valid YAML ({str(e).splitlines()[0]})"]
    if not isinstance(meta, dict) or list(meta.keys()) != ["name", "description"]:
        fails.append(f"{skill_dir}: front matter keys must be exactly name, description (got {list(meta.keys()) if isinstance(meta, dict) else type(meta)})")
    else:
        if meta["name"] != skill_dir.name or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", str(meta["name"])) or len(str(meta["name"])) > 64:
            fails.append(f"{skill_dir}: name {meta['name']!r} must be 1 to 64 chars, lowercase a-z 0-9 and single hyphens, and equal the folder name (agentskills.io rule, enforced by Microsoft surfaces)")
        d = str(meta["description"]).strip()
        if not (40 <= len(d) <= 1024): fails.append(f"{skill_dir}: description length {len(d)} (want 40 to 1024, the spec cap)")
        if not re.search(r"^description:\s*>-", fm, re.M): fails.append(f"{skill_dir}: description must be a folded block scalar (description: >-) so punctuation is YAML-safe")
    if len(body) >= 20000: fails.append(f"{skill_dir}: instructions {len(body)} chars, must be under 20,000")
    if len(body) < 1500: fails.append(f"{skill_dir}: instructions only {len(body)} chars, suspiciously short")
    for h in HEADINGS:
        if h not in body: fails.append(f"{skill_dir}: missing heading {h!r}")
    for needle, why in FORBIDDEN:
        if needle in s: fails.append(f"{skill_dir}: forbidden text ({why}): {needle!r}")
    for p in skill_dir.rglob("*"):
        if p.is_file():
            rel = p.relative_to(skill_dir).as_posix()
            if p.name != "SKILL.md" and not rel.startswith(("references/", "assets/", "scripts/")):
                fails.append(f"{skill_dir}: payload may only hold SKILL.md plus references/, assets/ or scripts/ (found {rel}); docs go to docs/skills/")
            if p.name.startswith("."): fails.append(f"{skill_dir}: hidden file {rel} (Cowork rejects hidden files; Agent Builder would ship it)")
            if p.suffix.lower() not in ALLOWED and p.name != "SKILL.md": fails.append(f"{skill_dir}: file type not allowed: {p.relative_to(skill_dir)}")
            if len(p.relative_to(skill_dir).parts) > 3: fails.append(f"{skill_dir}: depth over 3: {p.relative_to(skill_dir)}")
            if p.stat().st_size > 25 * 1024 * 1024: fails.append(f"{skill_dir}: file over 25 MB: {p.relative_to(skill_dir)}")
            if p.suffix.lower() in (".md", ".txt"):
                t = p.read_text(encoding="utf-8", errors="ignore")
                for needle, why in FORBIDDEN:
                    if needle in t and p.name != "SKILL.md": fails.append(f"{skill_dir}: forbidden text in {p.relative_to(skill_dir)} ({why})")
    for ref in re.findall(r"references/[A-Za-z0-9_./-]+\.md", body):
        if not (skill_dir / ref).exists(): fails.append(f"{skill_dir}: references {ref} but the file is missing")
    return fails

def build_zip(skill_dir):
    DIST.mkdir(parents=True, exist_ok=True)
    out = DIST / f"{skill_dir.name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(skill_dir.rglob("*")):
            rel = p.relative_to(skill_dir).as_posix()
            if p.is_file() and not p.name.startswith(".") and (p.name == "SKILL.md" or rel.startswith(("references/", "assets/", "scripts/"))):
                z.write(p, rel)   # payload only: SKILL.md at the zip root plus its companion folders, nothing else ships to the agent
    if out.stat().st_size > 50 * 1024 * 1024:
        return f"{out.name} over 50 MB"
    return None

def main():
    dirs = sorted(p.parent for p in SKILLS.rglob("SKILL.md"))
    fails = []; n_files = 0
    for d in dirs:
        fails += check(d); n_files += sum(1 for p in d.rglob("*") if p.is_file())
    names = [d.name for d in dirs]
    for n in sorted(set(names)):
        if names.count(n) > 1: fails.append(f"duplicate skill name across categories: {n}")
    if "--no-zip" not in sys.argv and not fails:
        DIST.mkdir(parents=True, exist_ok=True)
        for z in DIST.glob("*.zip"):            # a renamed or removed skill must not leave a stale zip behind
            if z.stem not in names: z.unlink(); print("removed stale zip", z.name)
        for d in dirs:
            e = build_zip(d)
            if e: fails.append(e)
    summary = {"skills": len(dirs), "files": n_files, "categories": len({d.parent.name for d in dirs}), "failures": len(fails)}
    print(json.dumps(summary))
    for x in fails: print("FAIL", x)
    if fails: sys.exit(1)
    print(f"PASS: {len(dirs)} skills hold every Learn limit and repo rule" + ("" if "--no-zip" in sys.argv else f"; zips in {DIST.relative_to(ROOT)}/"))

if __name__ == "__main__":
    main()
