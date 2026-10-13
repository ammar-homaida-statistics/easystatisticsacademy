"""Check generated search/CSS assets and exercise real browser search behavior.

Install playwright==1.62.0 and its Chromium browser, then run after Jekyll builds:
python .github/scripts/test_search.py --site _site
Use --browser /path/to/chromium to use a local system browser.
External resources are stubbed; these checks target local search and assets.
"""

import argparse
from functools import partial
from html.parser import HTMLParser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading
import unittest
from urllib.parse import unquote, urlsplit

from playwright.sync_api import expect, sync_playwright


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--site", type=Path, default=Path("_site"))
parser.add_argument("--browser")
options = parser.parse_args()
SITE = options.site.resolve()


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


class Stylesheets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and "stylesheet" in attrs.get("rel", "").split():
            self.urls.append(attrs["href"])


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = json.loads((SITE / "search.json").read_text())
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(SITE)))
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.origin = "http://127.0.0.1:" + str(cls.server.server_port)
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(executable_path=options.browser, headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        self.context = self.browser.new_context()
        # MathJax/video availability is unrelated to search regression checks.
        self.context.route("https://**", lambda route: route.fulfill(status=200, body=""))
        self.page = self.context.new_page()
        self.errors = []
        self.page.on("pageerror", lambda error: self.errors.append(str(error)))

    def tearDown(self):
        self.assertEqual(self.errors, [], "Unexpected browser JavaScript errors")
        self.context.close()

    def open(self):
        self.page.goto(self.origin + "/", wait_until="networkidle")
        self.input = self.page.get_by_role("searchbox", name="Search statistical lessons")
        self.results = self.page.get_by_role("region", name="Search results")
        self.status = self.page.get_by_role("status")

    def test_generated_index_and_css(self):
        self.assertIsInstance(self.records, list)
        urls = []
        for record in self.records:
            for key in ("title", "url", "content"):
                self.assertIsInstance(record[key], str)
            url = record["url"]
            self.assertTrue(url.startswith("/") and not url.startswith("//"))
            target = SITE / unquote(urlsplit(url).path).lstrip("/")
            if url.endswith("/"):
                target = target / "index.html"
            self.assertTrue(target.is_file(), url)
            urls.append(url)
        self.assertEqual(len(urls), len(set(urls)))
        styles = set()
        for path in SITE.rglob("*.html"):
            source = path.read_text()
            links = Stylesheets()
            links.feed(source)
            for url in links.urls:
                if url.startswith("/") and not url.startswith("//"):
                    self.assertTrue((SITE / urlsplit(url).path.lstrip("/")).is_file(), (path, url))
                    styles.add(urlsplit(url).path)
            if 'id="site-search"' in source:
                self.assertEqual(source.count('src="/js/search.js"'), 1)
                self.assertNotIn("SimpleJekyllSearch(", source)
        # The refreshed homepage alone also loads a page-scoped stylesheet.
        self.assertEqual(styles, {"/css/style.css", "/css/home.css"})
        home_links = Stylesheets()
        home_links.feed((SITE / "index.html").read_text())
        self.assertEqual({urlsplit(url).path for url in home_links.urls},
                         {"/css/style.css", "/css/home.css"})
        lesson_links = Stylesheets()
        lesson_links.feed((SITE / "descriptive/spread/variance/index.html").read_text())
        self.assertEqual({urlsplit(url).path for url in lesson_links.urls},
                         {"/css/style.css"})

    def test_homepage_responsive_layout(self):
        self.open()
        expect(self.page.locator(".esa-home-hero h1")).to_be_visible()
        expect(self.page.locator('link[href^="/css/home.css"]')).to_have_count(1)
        for width in (375, 768, 1280):
            self.page.set_viewport_size({"width": width, "height": 850})
            overflow = self.page.evaluate("""() => ({
                documentWidth: document.documentElement.scrollWidth,
                viewportWidth: window.innerWidth,
                outliers: [...document.querySelectorAll("body *")].map(el => {
                    const r = el.getBoundingClientRect();
                    return {tag: el.tagName, className: String(el.className || "").slice(0, 90),
                            right: Math.round(r.right), left: Math.round(r.left)};
                }).filter(x => x.right > window.innerWidth + 1 || x.left < -1).slice(0, 12)
            })""")
            self.assertLessEqual(
                overflow["documentWidth"], overflow["viewportWidth"],
                f"Homepage overflows at {width}px: {overflow}",
            )
            expect(self.page.locator(".esa-home-hero")).to_be_visible()
        self.page.goto(self.origin + "/descriptive/spread/variance/", wait_until="networkidle")
        expect(self.page.locator('link[href^="/css/home.css"]')).to_have_count(0)

    def test_descriptive_continue_reading_storage(self):
        """Resume only known descriptive blocks and treat stored labels as plain text."""
        self.page.goto(self.origin + "/descriptive/", wait_until="networkidle")
        key = "esa_continue_descriptive_last_block_v0"
        panel = self.page.locator("#continue-reading-descriptive")
        label = self.page.locator("#continue-reading-descriptive-label")
        link = self.page.locator("#continue-reading-descriptive-btn")
        expect(panel).to_be_hidden()

        def set_stored(payload):
            self.page.evaluate(
                "([key, value]) => localStorage.setItem(key, JSON.stringify(value))",
                [key, payload],
            )
            self.page.reload(wait_until="networkidle")

        for path in ("/descriptive/data-variables/", "/descriptive/spread/",
                     "/descriptive/shape/", "/descriptive/reporting/"):
            with self.subTest(valid_path=path):
                set_stored({"url": path, "label": "Last block"})
                expect(panel).to_be_visible()
                expect(label.locator("strong")).to_have_text("Last block")
                expect(link).to_have_attribute("href", path)

        malicious_label = '<img src=x onerror="window.esaInjected=true"> & statistics'
        set_stored({"url": "/descriptive/spread/", "label": malicious_label})
        expect(panel).to_be_visible()
        expect(label.locator("strong")).to_have_text(malicious_label)
        self.assertEqual(label.locator("img, script").count(), 0)
        self.assertIsNone(self.page.evaluate("window.esaInjected"))

        invalid = (
            {"url": "https://example.com", "label": "External"},
            {"url": "//example.com/path", "label": "Protocol-relative"},
            {"url": "javascript:alert(1)", "label": "JavaScript"},
            {"url": "/descriptive/spread/../shape/", "label": "Traversal"},
            {"url": "/descriptive/spread/?next=elsewhere", "label": "Extra query"},
            {"url": "/descriptive/not-a-block/", "label": "Unknown"},
            {"url": "/descriptive/spread/", "label": 42},
            {"url": "/descriptive/spread/", "label": "  "},
        )
        for payload in invalid:
            with self.subTest(invalid_payload=payload):
                set_stored(payload)
                expect(panel).to_be_hidden()
                expect(link).to_have_attribute("href", "#")

    def test_representative_lessons_and_navigation(self):
        self.open()
        cases = {
            "variance": "/descriptive/spread/variance/",
            "Bayes’ theorem": "/probability/conditional/bayes-theorem/",
            "normal distribution": "/probability/distributions/normal-distribution/",
            "linear regression": "/modeling/simple-linear-regression/",
            "What is a confidence interval?": "/inference/confidence-intervals/what-is-a-confidence-interval/",
            "  VARIANCE  ": "/descriptive/spread/variance/",
        }
        for query, url in cases.items():
            self.input.fill(query)
            expect(self.results.locator("a").first).to_have_attribute("href", url)
            self.assertLessEqual(self.results.locator("a").count(), 8)
            expect(self.status).to_contain_text("shown.")
        self.results.locator("a").first.click()
        expect(self.page).to_have_url(self.origin + cases["variance"])

    def test_empty_special_characters_and_no_results(self):
        self.open()
        for query in ("", "   ", "\t"):
            self.input.fill(query)
            expect(self.results).to_be_hidden()
            expect(self.status).to_have_text("")
        for query in ("esa-no-such-lesson-93742", "[.*]+", '<script>alert("x")</script>'):
            self.input.fill(query)
            expect(self.results).to_have_text("No results found.")
            expect(self.status).to_have_text("No results found.")
        self.input.fill("%")
        expect(self.results.locator("a").first).to_be_visible()

    def test_keyboard_and_outside_dismissal(self):
        self.open()
        self.input.fill("variance")
        self.input.press("Tab")
        expect(self.results.locator("a").first).to_be_focused()
        self.page.keyboard.press("Escape")
        expect(self.results).to_be_hidden()
        expect(self.input).to_be_focused()
        self.input.fill("normal")
        self.input.press("ArrowDown")
        expect(self.results.locator("a").first).to_be_focused()
        self.page.keyboard.press("Escape")
        expect(self.results).to_be_hidden()
        self.input.fill("variance")
        self.page.locator("h1").click()
        expect(self.results).to_be_hidden()
        self.input.fill("normal")
        self.page.locator(".brand").focus()
        expect(self.results).to_be_hidden()

    def test_delayed_index_completion(self):
        requests = []
        self.page.route("**/search.json", lambda route: requests.append(route))
        self.page.goto(self.origin + "/", wait_until="domcontentloaded")
        self.page.get_by_role("searchbox", name="Search statistical lessons").fill("variance")
        expect(self.page.locator("#search-status")).to_have_text("Loading search…")
        self.assertEqual(len(requests), 1)
        requests[0].fulfill(status=200, content_type="application/json", body=json.dumps(self.records))
        expect(self.page.locator("#search-results a").first).to_have_attribute("href", "/descriptive/spread/variance/")

    def test_index_failures(self):
        for status, body in ((404, "missing"), (200, "[invalid"), (200, "{}"),
                             (200, '[{"title":"bad","content":"bad","url":"//example.com"}]')):
            with self.subTest(status=status, body=body):
                self.page.route("**/search.json", lambda route:
                                route.fulfill(status=status, content_type="application/json", body=body))
                self.open()
                expect(self.results).to_be_hidden()
                self.input.fill("variance")
                expect(self.status).to_have_text("Search is temporarily unavailable. Please try again.")
                expect(self.results.locator("a")).to_have_count(0)
                self.page.unroute("**/search.json")

    def test_dismissed_pending_query_stays_closed(self):
        requests = []
        self.page.route("**/search.json", lambda route: requests.append(route))
        self.page.goto(self.origin + "/", wait_until="domcontentloaded")
        search = self.page.get_by_role("searchbox", name="Search statistical lessons")
        search.fill("variance")
        expect(self.page.locator("#search-status")).to_have_text("Loading search…")
        search.press("Escape")
        requests[0].fulfill(status=200, content_type="application/json", body=json.dumps(self.records))
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator("#search-results")).to_be_hidden()
        expect(self.page.locator("#search-status")).to_have_text("")

    def test_literal_markup_and_entities(self):
        fixture = [{"title": '<img src=x onerror="window.esaInjected=true"> &amp; β',
                    "url": "/descriptive/spread/variance/", "content": 'Literal <script>bad()</script> &amp; β'}]
        self.page.route("**/search.json", lambda route:
                        route.fulfill(content_type="application/json", body=json.dumps(fixture)))
        self.open()
        self.input.fill("β")
        expect(self.results.locator("a")).to_have_count(1)
        expect(self.results.locator(".search-title")).to_have_text('<img src=x onerror="window.esaInjected=true"> & β')
        expect(self.results.locator("img, script")).to_have_count(0)
        self.assertIsNone(self.page.evaluate("window.esaInjected"))


if __name__ == "__main__":
    unittest.main(argv=[__file__], verbosity=2)
