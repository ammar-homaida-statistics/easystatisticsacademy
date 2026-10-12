#!/usr/bin/env python3
"""Inventory damaged math placeholders and reject additions to a frozen baseline.

This command only reads source files and prints a report; it never changes pages
or writes a baseline. Python 3.9+ and the standard library are sufficient.
"""

import argparse
from collections import Counter
import json
from pathlib import Path, PurePosixPath
import re
import sys


EXTENSIONS = {".md", ".markdown", ".html", ".htm"}
EXCLUDED = {
    ".git", ".github", ".bundle", ".jekyll-cache", "_site", "vendor",
    "node_modules",
}
# Literal private-use characters found where formulas should be in the source.
# Also report isolated delimiters, so an incomplete new marker cannot evade CI.
PLACEHOLDER = re.compile(r"\uea01[0-9]+\uea02|[\uea01\uea02]")
SCHEMA_VERSION = 1


def scan_sources(root):
    """Return per-page token counts, their line numbers, and files inspected."""
    pages = {}
    locations = {}
    scanned = 0
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if (not path.is_file() or path.suffix.lower() not in EXTENSIONS
                or any(part in EXCLUDED for part in relative.parts)):
            continue
        scanned += 1
        counts = Counter()
        found = []
        for line_number, line in enumerate(
                path.read_text(encoding="utf-8-sig").splitlines(), 1):
            for match in PLACEHOLDER.finditer(line):
                token = match.group()
                counts[token] += 1
                found.append((line_number, token))
        if counts:
            name = relative.as_posix()
            pages[name] = dict(sorted(counts.items()))
            locations[name] = found
    return pages, locations, scanned


def load_baseline(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if (not isinstance(data, dict)
            or type(data.get("schema_version")) is not int
            or data["schema_version"] != SCHEMA_VERSION):
        raise ValueError("Baseline must have schema_version: 1")
    pages = data.get("pages")
    if not isinstance(pages, dict):
        raise ValueError("Baseline pages must be an object")
    for name, counts in pages.items():
        source_path = PurePosixPath(name)
        if (not name or source_path.is_absolute() or ".." in source_path.parts
                or "\\" in name or source_path.as_posix() != name
                or source_path.suffix.lower() not in EXTENSIONS
                or any(part in EXCLUDED for part in source_path.parts)):
            raise ValueError(f"Invalid baseline source path: {name!r}")
        if not isinstance(counts, dict) or not counts:
            raise ValueError(f"Expected token counts for {name}")
        for token, count in counts.items():
            if PLACEHOLDER.fullmatch(token) is None:
                raise ValueError(f"Unrecognized baseline token in {name}: {token!r}")
            if type(count) is not int or count < 1:
                raise ValueError(f"Baseline counts must be positive integers: {name}")
    return pages


def section_summary(pages):
    sections = {}
    for name, counts in pages.items():
        parts = PurePosixPath(name).parts
        section = parts[0] if len(parts) > 1 else "(root)"
        totals = sections.setdefault(section, {"affected_pages": 0,
                                                "placeholder_occurrences": 0})
        totals["affected_pages"] += 1
        totals["placeholder_occurrences"] += sum(counts.values())
    return dict(sorted(sections.items()))


def regressions(pages, baseline):
    """Compare individual tokens on each page; reductions cannot offset additions."""
    additions = []
    for name, counts in pages.items():
        allowed = baseline.get(name, {})
        for token, count in counts.items():
            previous = allowed.get(token, 0)
            if count > previous:
                additions.append((name, token, previous, count))
    return additions


def escaped(token):
    return token.encode("unicode_escape").decode("ascii")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parents[2],
                        help="Source checkout to inspect")
    parser.add_argument("--baseline", type=Path,
                        help="Baseline JSON; defaults to ROOT/.github/math-placeholder-baseline.json")
    parser.add_argument("--inventory", action="store_true",
                        help="Print a JSON inventory without applying the regression gate")
    parser.add_argument("--details", action="store_true",
                        help="Also print every existing placeholder's source location")
    options = parser.parse_args(argv)
    root = options.root.resolve()
    if not root.is_dir():
        parser.error(f"Source directory does not exist: {root}")
    try:
        pages, locations, scanned = scan_sources(root)
        baseline = None if options.inventory else load_baseline(
            options.baseline or root / ".github/math-placeholder-baseline.json")
    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    sections = section_summary(pages)
    occurrences = sum(sum(counts.values()) for counts in pages.values())
    if options.inventory:
        print(json.dumps({
            "schema_version": SCHEMA_VERSION,
            "scanned_files": scanned,
            "affected_pages": len(pages),
            "placeholder_occurrences": occurrences,
            "sections": sections,
            "pages": pages,
        }, ensure_ascii=True, indent=2, sort_keys=True))
        return 0

    print(f"Inspected {scanned} Markdown/HTML source files.")
    print("Section | Affected pages | Placeholder occurrences")
    for section, totals in sections.items():
        print(f"{section} | {totals['affected_pages']} | "
              f"{totals['placeholder_occurrences']}")
    print(f"TOTAL | {len(pages)} | {occurrences}")
    if options.details:
        for name, found in locations.items():
            for line, token in found:
                print(f"{name}:{line}: {escaped(token)}")

    additions = regressions(pages, baseline)
    if additions:
        for name, token, previous, count in additions:
            lines = [str(line) for line, value in locations[name] if value == token]
            print(f"NEW: {name}:{','.join(lines[previous:])}: {escaped(token)} "
                  f"(baseline {previous}, current {count}, added {count - previous})",
                  file=sys.stderr)
        added = sum(count - previous for _, _, previous, count in additions)
        print(f"FAIL: {added} new placeholder occurrence(s) exceed the baseline.",
              file=sys.stderr)
        return 1

    debt = sum(sum(counts.values()) for counts in baseline.values())
    print(f"PASS: no new placeholder occurrences; current {occurrences}, baseline {debt}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
