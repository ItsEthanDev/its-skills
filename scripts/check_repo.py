#!/usr/bin/env python3
"""Check the skill catalog, distribution notices, and existing audit entries."""

import argparse
from collections import Counter
from pathlib import Path
import re
import sys


CLASSIFICATIONS = {"Copied", "Adapted", "Inspired", "Original"}
LINK = re.compile(r"\[(`?)([a-z0-9]+(?:-[a-z0-9]+)*)\1\]\(([^\s)]+)\)")


def table_rows(root, filename, section, columns, errors):
    """Read the repository's pipe-table format, scoped to one H2 section."""
    try:
        lines = (root / filename).read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        errors.append(f"{filename}: cannot read file: {exc.strerror}")
        return []

    in_section = False
    found_section = False
    found_header = False
    found_separator = False
    rows = []
    for number, line in enumerate(lines, 1):
        if line.startswith("## ") or line.startswith("# "):
            if in_section:
                break
            in_section = line == f"## {section}"
            found_section |= in_section
            continue
        if not in_section or not line.lstrip().startswith("|"):
            continue
        location = f"{filename}:{number}"
        stripped = line.strip()
        if not stripped.endswith("|"):
            errors.append(f"{location}: malformed table row (missing trailing pipe)")
            continue
        cells = [cell.strip() for cell in stripped[1:-1].split("|")]
        if not found_header:
            if cells != columns:
                errors.append(f"{location}: expected table header: {' | '.join(columns)}")
                continue
            found_header = True
            continue
        if not found_separator:
            if len(cells) != len(columns) or not all(
                re.fullmatch(r":?-{3,}:?", cell) for cell in cells
            ):
                errors.append(f"{location}: malformed table separator")
            found_separator = True
            continue
        if len(cells) != len(columns) or not all(cells):
            errors.append(f"{location}: malformed table row")
            continue
        rows.append((location, cells))

    if not found_section:
        errors.append(f"{filename}: missing section '## {section}'")
    elif not found_header or not found_separator:
        errors.append(f"{filename}: missing complete table in '## {section}'")
    return rows


def check_entries(root, rows, skills, target, errors):
    names = []
    for location, cells in rows:
        match = LINK.fullmatch(cells[0])
        if not match:
            errors.append(f"{location}: expected a Markdown skill link in the first column")
            continue
        _, name, link = match.groups()
        names.append(name)
        if name not in skills:
            errors.append(f"{location}: unknown skill '{name}'")
        expected = f"skills/{name}/{target}"
        if link != expected:
            errors.append(f"{location}: expected link '{expected}', got '{link}'")
        elif not (root / link).is_file():
            errors.append(f"{location}: link target is not a file: {link}")
    for name, count in sorted(Counter(names).items()):
        if count > 1:
            errors.append(f"{rows[0][0].split(':')[0]}: duplicate entry for '{name}'")
    return set(names)


def check_repo(root):
    """Return all consistency errors; an empty list means the checks passed."""
    root = Path(root)
    errors = []
    skills = {path.parent.name for path in (root / "skills").glob("*/SKILL.md") if path.is_file()}
    if not skills:
        errors.append("skills/: no skills found (expected skills/*/SKILL.md)")
    for name in sorted(skills):
        for required in ("LICENSE", "PROVENANCE.md"):
            path = Path("skills") / name / required
            if not (root / path).is_file():
                errors.append(f"{path}: missing required file")

    catalog = table_rows(root, "README.md", "Skill catalog", ["Skill", "Purpose"], errors)
    catalog_names = check_entries(root, catalog, skills, "SKILL.md", errors)
    for name in sorted(skills - catalog_names):
        errors.append(f"README.md: missing catalog entry for '{name}'")

    inventory = table_rows(
        root, "THIRD-PARTY-NOTICES.md", "Skill inventory",
        ["Skill", "Classification", "Evidence"], errors,
    )
    check_entries(root, inventory, skills, "PROVENANCE.md", errors)
    for location, cells in inventory:
        if cells[1] not in CLASSIFICATIONS:
            errors.append(f"{location}: unknown classification '{cells[1]}'")
    # The inventory is intentionally not required to cover every skill.
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parent.parent,
        help="repository root (defaults to this script's repository)",
    )
    args = parser.parse_args()
    errors = check_repo(args.root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Repository consistency checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
