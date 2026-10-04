#!/usr/bin/env python3
"""Build and validate the source-derived ItsSkills direct dependency graph."""
import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote
from markdown_it import MarkdownIt

ROLES = ("stages", "playbooks", "techniques", "principles")
ALLOWED = {"stages": set(ROLES), "playbooks": {"playbooks", "techniques", "principles"},
           "techniques": {"techniques", "principles"}, "principles": {"principles"}}
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PARSER = MarkdownIt("commonmark", {"html": True})

class GraphError(Exception):
    pass

def strip_frontmatter(text):
    lines = text.splitlines(keepends=True)
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() in ("---", "..."):
                return "\n" * (i + 1) + "".join(lines[i + 1:])
    return text

def markdown_tokens(text):
    """Let Markdown syntax distinguish comments from literal inline-code content."""
    return PARSER.parse(strip_frontmatter(text))

def inventory(root):
    skills = {}
    problems = []
    source_root = root / "skills"
    if not source_root.is_dir():
        raise GraphError(f"{source_root}: missing skills directory")
    for role in ROLES:
        directory = source_root / role
        if not directory.exists():
            continue
        for skill_dir in sorted(p for p in directory.iterdir() if p.is_dir()):
            main = skill_dir / "SKILL.md"
            if not main.is_file():
                continue
            front = re.match(r"\A---\r?\n([\s\S]*?)\r?\n(?:---|\.\.\.)[ \t]*(?:\r?\n|$)", main.read_text(encoding="utf-8"))
            values = re.findall(r"(?m)^name:[ \t]*(.+?)[ \t]*$", front[1]) if front else []
            names = []
            for value in values:
                value = re.split(r"[ \t]+#", value, maxsplit=1)[0].strip()
                if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                    value = value[1:-1]
                names.append(value)
            if len(names) != 1 or len(names[0]) > 64 or not NAME.fullmatch(names[0]):
                problems.append(f"{main.relative_to(root)}: expected one valid frontmatter name")
                continue
            name = names[0]
            if skill_dir.name != name:
                problems.append(f"{main.relative_to(root)}: directory identity does not match name {name!r}")
            if name in skills:
                problems.append(f"{main.relative_to(root)}: duplicate skill name {name!r} (also {skills[name]['path']})")
                continue
            resources = sorted(p.relative_to(root).as_posix() for p in skill_dir.rglob("*.md") if p.is_file())
            skills[name] = {"name": name, "role": role, "path": main.relative_to(root).as_posix(), "resources": resources,
                            "files": [root / p for p in resources], "dependencies": set()}
    if problems:
        raise GraphError("\n".join(problems))
    return skills

def target_skill(href, source, root, skills):
    href = href.split("#", 1)[0].split("?", 1)[0]
    if not href or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", href) or href.startswith("/"):
        return None
    candidate = (source.parent / unquote(href)).resolve()
    try:
        relative = candidate.relative_to(root.resolve()).as_posix()
    except ValueError:
        return None
    for name, skill in skills.items():
        directory = str(Path(skill["path"]).parent)
        if relative == directory or relative.startswith(directory + "/"):
            return name
    return None

def build(root):
    skills = inventory(root)
    names = set(skills)
    evidence = {}
    residual = []
    for owner, skill in skills.items():
        for source in skill["files"]:
            relative = source.relative_to(root).as_posix()
            text = source.read_text(encoding="utf-8")
            for block in markdown_tokens(text):
                if block.type != "inline" or not block.children:
                    continue
                line_range = block.map or [0, 0]
                for token in block.children:
                    if token.type == "code_inline" and token.content in names:
                        target = token.content
                        if target != owner:
                            evidence.setdefault((owner, target, relative, line_range[0] + 1, line_range[1]), None)
                    elif token.type == "link_open":
                        target = target_skill(token.attrGet("href") or "", source, root, skills)
                        if target and target != owner:
                            residual.append(f"{relative}:{line_range[0] + 1}: residual cross-skill link to {target}")
    if residual:
        raise GraphError("\n".join(sorted(set(residual))))
    for source, target, _p, _a, _b in evidence:
        if skills[target]["role"] not in ALLOWED[skills[source]["role"]]:
            raise GraphError(f"{_p}:{_a}: forbidden role direction {source} ({skills[source]['role']}) -> {target} ({skills[target]['role']})")
        skills[source]["dependencies"].add(target)
    edges = [{"from": a, "to": b, "evidence": [{"source": p, "line_range": [start, end]} for x, y, p, start, end in sorted(evidence) if x == a and y == b]}
             for a in sorted(skills) for b in sorted(skills[a]["dependencies"])]
    adjacency = {n: skills[n]["dependencies"] for n in skills}
    visiting, visited = set(), set()
    def visit(node, trail):
        if node in visiting:
            raise GraphError(f"dependency cycle: {' -> '.join(trail + [node])}")
        if node in visited: return
        visiting.add(node)
        for nxt in sorted(adjacency[node]): visit(nxt, trail + [node])
        visiting.remove(node); visited.add(node)
    for node in sorted(skills): visit(node, [])
    nodes = [{"name": n, "role": skills[n]["role"], "path": skills[n]["path"], "resources": skills[n]["resources"],
              "dependencies": sorted(skills[n]["dependencies"])} for n in sorted(skills)]
    return {"version": 1, "nodes": nodes, "edges": edges}

def render(data):
    roles = {n["name"]: n["role"] for n in data["nodes"]}
    ids = {n: "skill_" + re.sub(r"[^A-Za-z0-9_]", "_", n) for n in roles}
    lines = ["# Skill Dependencies", "", "Arrows point from a skill to each skill it references. References are conservative and do not grant execution authority.", "", "```mermaid", "flowchart LR"]
    for role in ROLES:
        nodes = [n for n in sorted(roles) if roles[n] == role]
        if nodes:
            lines.append(f"  subgraph {role}")
            for name in nodes: lines.append(f'    {ids[name]}["{name}"]')
            lines.append("  end")
    for edge in data["edges"]: lines.append(f"  {ids[edge['from']]} --> {ids[edge['to']]}")
    lines += ["```", "", "Legend: `A --> B` means A directly references B. Nodes are grouped by source role.", "", "## Direct dependencies", "", "| Skill | Role | Direct dependencies and evidence |", "| --- | --- | --- |"]
    by_pair = {(e["from"], e["to"]): e["evidence"] for e in data["edges"]}
    for node in data["nodes"]:
        deps = []
        for target in node["dependencies"]:
            sources = by_pair[(node["name"], target)]
            refs = ", ".join(f"[{ev['source']}:{ev['line_range'][0]}](<{ev['source']}?plain=1#L{ev['line_range'][0]}>)" for ev in sources)
            deps.append(f"`{target}` ({refs})")
        lines.append(f"| `{node['name']}` | {node['role']} | {'; '.join(deps) if deps else '—'} |")
    lines += ["", "## JSON interface", "", "`dependencies.json` has schema version 1. `nodes` is sorted by name and contains each skill's `name`, `role`, repository-relative main `path`, Markdown `resources`, and sorted direct `dependencies`. `edges` has one item per direct pair; each item's `evidence` records a repository-relative `source` and inclusive Markdown block `line_range` (paragraph/block line range, not token offsets). Consumers can traverse outgoing edges for subsets and incoming edges for potential impact. `resources` lists Markdown scan inputs, not a complete installation manifest. Map other resources, including scripts and assets, to the directory containing their owning node's main `path`.", ""]
    return "\n".join(lines)

def outputs(root, data):
    return {root / "DEPENDENCIES.md": render(data), root / "dependencies.json": json.dumps(data, indent=2, ensure_ascii=False) + "\n"}

def command(args):
    toolroot = Path(__file__).resolve().parents[2]
    root = Path(args.root).resolve() if args.root else toolroot
    if not root.is_dir(): raise GraphError(f"root is not a directory: {root}")
    data = build(root)
    files = outputs(root, data)
    if args.command == "generate":
        for path, content in files.items(): path.write_text(content, encoding="utf-8")
        print(f"generated {len(data['nodes'])} skills and {len(data['edges'])} edges")
    elif args.command == "check":
        stale = []
        for path, content in files.items():
            if not path.is_file(): stale.append(f"missing output: {path.relative_to(root)}")
            elif path.read_text(encoding="utf-8") != content: stale.append(f"stale output: {path.relative_to(root)}")
        if stale: raise GraphError("\n".join(stale))
        print(f"fresh: {len(data['nodes'])} skills and {len(data['edges'])} edges")
    elif args.command == "test":
        import unittest
        from test_graph import GraphCliTests
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(GraphCliTests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        if not result.wasSuccessful(): raise GraphError("tests failed")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Generate, check, or test the committed direct skill dependency graph.")
    parser.add_argument("--root", help="source repository root (default: this tool's repository)")
    parser.add_argument("command", nargs="?", choices=("generate", "check", "test"))
    args = parser.parse_args()
    if not args.command: parser.print_help(); return 2
    try: return command(args)
    except (GraphError, OSError, UnicodeError) as exc:
        print(f"skill-graph: {exc}", file=sys.stderr); return 1

if __name__ == "__main__":
    sys.exit(main())
