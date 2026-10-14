"""Regression fixtures for generated-site SEO metadata checks."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from audit_seo import audit


def html(title="Statistics", description="Learn core statistics.", canonical="/",
         robots="", headings=1):
    heading = "<h1>Statistical overview</h1>" * headings
    return f"""<!doctype html>
      <html lang="en"><head><title>{title}</title>
      <meta name="description" content="{description}">
      <link rel="canonical" href="https://easystatisticsacademy.com{canonical}">
      {('<meta name="robots" content="'+robots+'">') if robots else ''}
      </head><body><main id="main-content">{heading}</main></body></html>"""


class SeoAuditTests(unittest.TestCase):
    def test_valid_indexable_and_noindex_pages(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "lesson").mkdir()
            (root / "index.html").write_text(html(), encoding="utf-8")
            (root / "lesson" / "index.html").write_text(html(
                title="Lesson", canonical="/lesson/"), encoding="utf-8")
            (root / "404.html").write_text(html(
                title="Not found", canonical="/404.html", robots="noindex, follow"),
                encoding="utf-8")
            (root / "google.html").write_text("verification", encoding="utf-8")
            (root / "sitemap.xml").write_text("""<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
              <url><loc>https://easystatisticsacademy.com/</loc></url>
              <url><loc>https://easystatisticsacademy.com/lesson/</loc></url>
              </urlset>""", encoding="utf-8")
            self.assertEqual(audit(root), [])

    def test_reports_missing_duplicate_incorrect_and_indexed_noindex(self):
        with TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "lesson").mkdir()
            (root / "copy").mkdir()
            (root / "copy" / "index.html").write_text(html(
                canonical="/copy/"), encoding="utf-8")
            (root / "index.html").write_text(html(
                description="", headings=0, canonical="/wrong/"), encoding="utf-8")
            (root / "lesson" / "index.html").write_text(html(
                robots="noindex", headings=2, canonical="/lesson/"), encoding="utf-8")
            (root / "404.html").write_text(html(
                title="404", canonical="/404.html"), encoding="utf-8")
            (root / "sitemap.xml").write_text("""<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
              <url><loc>https://easystatisticsacademy.com/</loc></url>
              <url><loc>https://easystatisticsacademy.com/lesson/</loc></url>
              </urlset>""", encoding="utf-8")
            found = set(audit(root))
            for entry in [
                ("index.html", "missing-or-empty-description"),
                ("index.html", "missing-h1"),
                ("index.html", "canonical-mismatch"),
                ("lesson/index.html", "multiple-h1"),
                ("lesson/index.html", "noindex-in-sitemap"),
                ("404.html", "404-missing-noindex"),
                ("index.html", "duplicate-title"),
                ("copy/index.html", "duplicate-title"),
                ("copy/index.html", "indexable-not-in-sitemap"),
            ]:
                self.assertIn(entry, found)


if __name__ == "__main__":
    unittest.main()
