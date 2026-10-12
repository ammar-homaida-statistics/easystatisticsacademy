"""Behavioral tests for the read-only placeholder regression gate.

All edited pages below are temporary fixtures, never educational source files.
"""

from contextlib import redirect_stderr, redirect_stdout
import hashlib
from io import StringIO
import json
from pathlib import Path
import tempfile
import unittest

from validate_math_placeholders import main


TOKEN = "\uea010\uea02"
OTHER = "\uea011\uea02"


class MathPlaceholderTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.baseline = self.root / ".github/math-placeholder-baseline.json"
        self.baseline.parent.mkdir()
        self.write("probability/existing/index.md", f"# Existing\n{TOKEN}\n")
        self.write_baseline({"probability/existing/index.md": {TOKEN: 1}})

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def write_baseline(self, pages):
        self.baseline.write_text(json.dumps({"schema_version": 1, "pages": pages}),
                                 encoding="utf-8")

    def run_check(self, *args):
        output, errors = StringIO(), StringIO()
        with redirect_stdout(output), redirect_stderr(errors):
            code = main(["--root", str(self.root), *args])
        return code, output.getvalue(), errors.getvalue()

    def fingerprints(self):
        return {path.relative_to(self.root).as_posix():
                hashlib.sha256(path.read_bytes()).hexdigest()
                for path in self.root.rglob("*") if path.is_file()}

    def test_existing_debt_passes_without_writing(self):
        before = self.fingerprints()
        code, output, errors = self.run_check()
        self.assertEqual(code, 0, errors)
        self.assertIn("probability | 1 | 1", output)
        self.assertIn("PASS: no new", output)
        self.assertEqual(self.fingerprints(), before)

    def test_duplicate_existing_token_fails_with_source_line(self):
        self.write("probability/existing/index.md", f"{TOKEN}\n{TOKEN}\n")
        code, _, errors = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("probability/existing/index.md:2:", errors)
        self.assertIn("baseline 1, current 2, added 1", errors)

    def test_new_token_fails_even_when_page_total_is_unchanged(self):
        self.write("probability/existing/index.md", f"{OTHER}\n")
        code, _, errors = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("baseline 0, current 1, added 1", errors)

    def test_new_page_fails_even_when_existing_page_is_repaired(self):
        self.write("probability/existing/index.md", "Fixed formula\n")
        self.write("inference/new/index.html", f"<p>{TOKEN}</p>\n")
        code, output, errors = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("inference | 1 | 1", output)
        self.assertIn("inference/new/index.html:1:", errors)

    def test_removing_known_placeholders_passes(self):
        self.write("probability/existing/index.md", "Fixed formula\n")
        code, output, errors = self.run_check()
        self.assertEqual(code, 0, errors)
        self.assertIn("TOTAL | 0 | 0", output)

    def test_deleting_affected_page_passes(self):
        (self.root / "probability/existing/index.md").unlink()
        code, _, errors = self.run_check()
        self.assertEqual(code, 0, errors)

    def test_source_line_changes_do_not_reset_the_baseline(self):
        self.write("probability/existing/index.md", f"\nNew explanation\n\n{TOKEN}\n")
        code, _, errors = self.run_check()
        self.assertEqual(code, 0, errors)

    def test_partial_markers_fail(self):
        for marker in ("\uea01", "\uea02", "\uea01missing\uea02"):
            with self.subTest(marker=marker):
                self.write("modeling/new.md", marker)
                code, _, errors = self.run_check()
                self.assertEqual(code, 1)
                self.assertIn("modeling/new.md:1:", errors)

    def test_templates_are_checked(self):
        self.write("_includes/new.html", f"<p>{TOKEN}</p>")
        code, _, errors = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("_includes/new.html:1:", errors)

    def test_generated_files_test_fixtures_and_baseline_are_excluded(self):
        for directory in (".github", "_site", "vendor", "node_modules", ".git"):
            self.write(f"{directory}/nested/fixture.md", TOKEN)
        code, output, errors = self.run_check()
        self.assertEqual(code, 0, errors)
        self.assertIn("TOTAL | 1 | 1", output)

    def test_inventory_is_machine_readable_and_read_only(self):
        self.write("descriptive/new.markdown", f"{TOKEN} {OTHER}\n")
        before = self.fingerprints()
        code, output, errors = self.run_check("--inventory")
        self.assertEqual(code, 0, errors)
        data = json.loads(output)
        self.assertEqual(data["affected_pages"], 2)
        self.assertEqual(data["placeholder_occurrences"], 3)
        self.assertEqual(data["sections"]["descriptive"],
                         {"affected_pages": 1, "placeholder_occurrences": 2})
        self.assertEqual(self.fingerprints(), before)

    def test_details_show_escaped_tokens_and_locations(self):
        code, output, errors = self.run_check("--details")
        self.assertEqual(code, 0, errors)
        self.assertIn("probability/existing/index.md:2: \\uea010\\uea02", output)

    def test_missing_baseline_fails_closed(self):
        self.baseline.unlink()
        code, _, errors = self.run_check()
        self.assertEqual(code, 2)
        self.assertIn("ERROR:", errors)

    def test_invalid_baselines_fail_closed(self):
        invalid = [
            [], {"schema_version": 2, "pages": {}},
            {"schema_version": True, "pages": {}},
            {"schema_version": 1, "pages": []},
            {"schema_version": 1, "pages": {"../escape.md": {TOKEN: 1}}},
            {"schema_version": 1, "pages": {"lesson.md": {TOKEN: -1}}},
            {"schema_version": 1, "pages": {"lesson.md": {TOKEN: True}}},
            {"schema_version": 1, "pages": {"lesson.md": {"not a token": 1}}},
        ]
        for data in invalid:
            with self.subTest(data=data):
                self.baseline.write_text(json.dumps(data), encoding="utf-8")
                code, _, errors = self.run_check()
                self.assertEqual(code, 2)
                self.assertIn("ERROR:", errors)


if __name__ == "__main__":
    unittest.main(verbosity=2)
