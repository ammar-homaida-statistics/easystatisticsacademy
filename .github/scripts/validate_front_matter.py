#!/usr/bin/env python3
"""Validate YAML front matter without rendering or modifying website pages.

Setup: python -m pip install PyYAML==6.0.3
Run:   python .github/scripts/validate_front_matter.py
An optional --root PATH supports checking another source snapshot.
Requires Python 3.9+. The .github directory is excluded by Jekyll.
"""

import argparse
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    sys.exit("Install the validator dependency: python -m pip install PyYAML==6.0.3")


EXTENSIONS = {
    ".md", ".markdown", ".html", ".htm", ".json", ".xml", ".txt",
    ".css", ".scss", ".sass", ".js",
}
EXCLUDED = {".git", ".github", ".bundle", ".jekyll-cache", "_site", "vendor"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    root = parser.parse_args().root.resolve()
    if not root.is_dir():
        parser.error(f"Source directory does not exist: {root}")

    checked = 0
    errors = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if (not path.is_file() or path.suffix.lower() not in EXTENSIONS
                or any(part in EXCLUDED for part in relative.parts)):
            continue
        try:
            lines = path.read_text(encoding="utf-8-sig").splitlines()
            if not lines or lines[0] != "---":
                continue  # Static files without front matter are valid.
            checked += 1
            end = next((i for i in range(1, len(lines)) if lines[i] == "---"), None)
            if end is None:
                raise ValueError("Missing closing front-matter delimiter")
            metadata = yaml.safe_load("\n".join(lines[1:end]))
            if metadata is not None and not isinstance(metadata, dict):
                raise ValueError("Front matter must be a YAML mapping or empty")
        except (UnicodeError, OSError, ValueError, yaml.YAMLError) as error:
            errors.append(f"{relative}: {error}")

    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {checked} front-matter documents; {len(errors)} errors.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
