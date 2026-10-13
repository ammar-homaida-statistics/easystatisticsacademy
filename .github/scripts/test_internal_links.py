"""Small deterministic fixtures for the generated-site link auditor."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from audit_internal_links import audit, signature


class InternalLinkAuditTests(unittest.TestCase):
    def test_valid_pages_assets_relative_routes_and_anchors(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "lessons").mkdir()
            (root / "css").mkdir()
            (root / "css" / "style.css").write_text("body{}", encoding="utf-8")
            (root / "index.html").write_text("""
              <a href="/lessons/">Lessons</a><a href="#intro">Intro</a>
              <h2 id="intro">Intro</h2><a href="https://external.example/nope">Other</a>
              <link rel="stylesheet" href="/css/style.css">
            """, encoding="utf-8")
            (root / "lessons" / "index.html").write_text("""
              <a href="/">Home</a><a href="../#intro">Start</a>
              <a href="?q=1#lesson">Here</a><h2 id="lesson">Example</h2>
            """, encoding="utf-8")
            self.assertEqual(audit(root), [])

    def test_reports_missing_destinations_and_static_anchors(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text("""
              <a href="/missing/">Broken lesson</a>
              <a href="#nonexistent">Broken heading</a>
              <img src="/images/absent.png">
              <a href="mailto:info@example.com">Contact</a>
              <a href="https://unrelated.example/not-here">External</a>
            """, encoding="utf-8")
            issues = audit(root)
            self.assertEqual([i["reason"] for i in issues],
                             ["missing-page-or-asset", "missing-static-anchor",
                              "missing-page-or-asset"])
            self.assertTrue(any("index.html|/missing/|missing-page-or-asset"
                                == signature(i) for i in issues))


if __name__ == "__main__":
    unittest.main()
