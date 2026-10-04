"""Public-CLI integration tests using disposable repository trees."""
import json
import os
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent / "graph.sh"
ROLES = ("stages", "playbooks", "techniques", "principles")

def make_skill(root, role, name, body=""):
    path = root / "skills" / role / name / "SKILL.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\nname: {name}\ndescription: fixture\n---\n\n{body}\n", encoding="utf-8")
    return path

class GraphCliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        self.root.mkdir()
        alpha = make_skill(self.root, "playbooks", "alpha", "alpha cites `beta`, `beta` and itself `alpha`. Unknown `not-a-skill`.\n\nPlain beta.\n\n<!-- `gamma` -->\n\n````md\n```inline example\n`gamma`\n```\n````\n\n    `gamma`\n\nA multi `` `gamma` `` span.\n")
        alpha.write_text(alpha.read_text().replace("description: fixture", "description: `gamma`", 1), encoding="utf-8")
        make_skill(self.root, "playbooks", "beta")
        make_skill(self.root, "principles", "gamma")
        make_skill(self.root, "techniques", "delta")
        resource = self.root / "skills/playbooks/alpha/references/context.md"
        resource.parent.mkdir()
        resource.write_text("Resource says `gamma`.\n", encoding="utf-8")
        self.env = dict(os.environ)
        self.env["NIX_CONFIG"] = "experimental-features = nix-command flakes"

    def tearDown(self): self.tmp.cleanup()

    def cli(self, command, *args, cwd=None):
        return subprocess.run(["sh", str(TOOL), "--root", str(self.root), command, *args], cwd=cwd,
                              env=self.env, text=True, capture_output=True)

    def generate(self):
        result = self.cli("generate")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_exact_nodes_edges_resources_determinism_and_nonrepo_cwd(self):
        self.generate()
        raw = (self.root / "dependencies.json").read_text()
        data = json.loads(raw)
        self.assertEqual([n["name"] for n in data["nodes"]], ["alpha", "beta", "delta", "gamma"])
        self.assertEqual(next(n for n in data["nodes"] if n["name"] == "delta")["dependencies"], [])
        pairs = {(e["from"], e["to"]) for e in data["edges"]}
        self.assertEqual(pairs, {("alpha", "beta"), ("alpha", "gamma")})
        edge = next(e for e in data["edges"] if e["to"] == "gamma")
        self.assertEqual([x["source"] for x in edge["evidence"]], ["skills/playbooks/alpha/references/context.md"])
        self.assertIn("skills/playbooks/alpha/references/context.md", data["nodes"][0]["resources"])
        md = (self.root / "DEPENDENCIES.md").read_text()
        self.assertIn("| `alpha` | playbooks |", md)
        self.assertIn("flowchart LR", md)
        self.assertIn("skill_alpha --> skill_beta", md)
        self.assertEqual(set(re.findall(r"skill_([a-z]+) --> skill_([a-z]+)", md)), pairs)
        self.assertEqual(set(re.findall(r'skill_([a-z]+)\["[a-z]+"\]', md)), {"alpha", "beta", "delta", "gamma"})
        self.assertEqual(self.cli("check", cwd="/").returncode, 0)
        self.assertEqual(self.cli("generate").returncode, 0)
        self.assertEqual((self.root / "dependencies.json").read_text(), raw)

    def test_nested_sources_only_and_missing_skill_root(self):
        legacy = self.root / "playbooks/ghost/SKILL.md"
        legacy.parent.mkdir(parents=True)
        legacy.write_text("---\nname: ghost\n---\n", encoding="utf-8")
        self.generate()
        data = json.loads((self.root / "dependencies.json").read_text())
        self.assertEqual({n["name"] for n in data["nodes"]}, {"alpha", "beta", "delta", "gamma"})
        self.assertTrue(all(n["path"].startswith("skills/") for n in data["nodes"]))
        (self.root / "skills").rename(self.root / "sources")
        result = self.cli("check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing skills directory", result.stderr)

    def test_exact_source_lines_and_literal_comment_text(self):
        make_skill(self.root, "playbooks", "alpha", "Prefix `beta` suffix.\n\nMulti ``beta``.\n\n`<!--x-->delta<!--x-->`\n\nInline <!-- `delta` --> end.")
        self.generate()
        data = json.loads((self.root / "dependencies.json").read_text())
        self.assertEqual({(e["from"], e["to"]) for e in data["edges"]}, {("alpha", "beta"), ("alpha", "gamma")})
        edge = next(e for e in data["edges"] if e["to"] == "beta")
        self.assertEqual(edge["evidence"][0]["line_range"], [6, 6])

    def test_quoted_names_length_and_frontmatter_boundary(self):
        main = make_skill(self.root, "playbooks", "alpha", "`beta`")
        main.write_text(main.read_text().replace("name: alpha", "name: 'alpha'"), encoding="utf-8")
        self.generate()
        main.write_text("prefix ---\nname: alpha\n---\n`beta`\n", encoding="utf-8")
        self.assertNotEqual(self.cli("generate").returncode, 0)
        make_skill(self.root, "playbooks", "alpha")
        make_skill(self.root, "techniques", "a" * 65)
        self.assertNotEqual(self.cli("generate").returncode, 0)

    def test_cross_skill_script_link_is_rejected(self):
        resource = self.root / "skills/playbooks/beta/scripts/run.sh"
        resource.parent.mkdir()
        resource.write_text("#!/bin/sh\n", encoding="utf-8")
        make_skill(self.root, "playbooks", "alpha", "[helper](../beta/scripts/run.sh)")
        result = self.cli("generate")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("residual cross-skill link", result.stderr)

    def test_missing_stale_and_check_is_nonmutating(self):
        result = self.cli("check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing output", result.stderr)
        self.generate()
        before = (self.root / "DEPENDENCIES.md").read_text()
        (self.root / "skills/playbooks/alpha/SKILL.md").write_text("---\nname: alpha\n---\n`gamma`\n")
        check = self.cli("check")
        self.assertNotEqual(check.returncode, 0)
        self.assertIn("stale output", check.stderr)
        self.assertEqual((self.root / "DEPENDENCIES.md").read_text(), before)

    def test_invalid_unknown_role_cycle_and_residual_link(self):
        make_skill(self.root, "playbooks", "alpha", "`not-a-skill`")
        make_skill(self.root, "principles", "gamma", "`alpha`")
        result = self.cli("generate")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("forbidden role direction", result.stderr)
        make_skill(self.root, "playbooks", "alpha", "`beta`")
        make_skill(self.root, "playbooks", "beta", "`alpha`")
        make_skill(self.root, "principles", "gamma")
        result = self.cli("generate")
        self.assertIn("dependency cycle", result.stderr)
        make_skill(self.root, "playbooks", "alpha", "[other](../beta/SKILL.md)")
        result = self.cli("generate")
        self.assertIn("residual cross-skill link", result.stderr)

    def test_malformed_duplicate_identity_and_unknown_ignored(self):
        (self.root / "skills/playbooks/alpha/SKILL.md").write_text("---\nname: Invalid_Name\n---\n", encoding="utf-8")
        self.assertIn("valid frontmatter name", self.cli("check").stderr)
        make_skill(self.root, "playbooks", "alpha")
        make_skill(self.root, "techniques", "alpha")
        self.assertIn("duplicate skill name", self.cli("check").stderr)
        import shutil
        shutil.rmtree(self.root / "skills/techniques/alpha")
        make_skill(self.root, "techniques", "directory-name")
        (self.root / "skills/techniques/directory-name").rename(self.root / "skills/techniques/mismatched")
        self.assertIn("directory identity", self.cli("check").stderr)

    def test_missing_nix_fails_without_installing(self):
        bindir = Path(self.tmp.name) / "bin"
        bindir.mkdir()
        import shutil
        env = dict(self.env, PATH=str(bindir))
        result = subprocess.run([shutil.which("sh"), str(TOOL), "--root", str(self.root), "check"], env=env, text=True, capture_output=True)
        self.assertEqual(result.returncode, 127)
        self.assertIn("Nix is required", result.stderr)
        (bindir / "nix").symlink_to(shutil.which("nix"))
        result = subprocess.run([shutil.which("sh"), str(TOOL), "--root", str(self.root), "generate"], env=env, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_safe_relocation_and_subset_impact_traversal_data(self):
        make_skill(self.root, "playbooks", "beta", "`gamma`")
        (self.root / "skills/playbooks/alpha/references/context.md").write_text("No skill references here.\n")
        self.generate()
        data = json.loads((self.root / "dependencies.json").read_text())
        outgoing = {n["name"]: n["dependencies"] for n in data["nodes"]}
        selected = set(); todo = ["alpha"]
        while todo:
            item = todo.pop()
            if item not in selected: selected.add(item); todo.extend(outgoing[item])
        self.assertEqual(selected, {"alpha", "beta", "gamma"})
        users = {"gamma"}; todo = ["gamma"]
        while todo:
            target = todo.pop()
            for source, deps in outgoing.items():
                if target in deps and source not in users: users.add(source); todo.append(source)
        self.assertEqual(users, {"alpha", "beta", "gamma"})
        relocated = Path(self.tmp.name) / "moved"
        import shutil
        shutil.copytree(self.root, relocated)
        relocated_tool = relocated / "tools/skill-graph"
        shutil.copytree(TOOL.parent, relocated_tool)
        result = subprocess.run(["sh", str(relocated_tool / "graph.sh"), "check"], cwd="/", env=self.env, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)

if __name__ == "__main__": unittest.main()
