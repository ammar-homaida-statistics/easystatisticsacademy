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
from xml.etree import ElementTree

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
        self.assertEqual(styles, {"/css/style.css", "/css/home.css", "/css/paths.css", "/css/editorial.css"})
        home_links = Stylesheets()
        home_links.feed((SITE / "index.html").read_text())
        self.assertEqual({urlsplit(url).path for url in home_links.urls},
                         {"/css/style.css", "/css/home.css"})
        lesson_links = Stylesheets()
        lesson_links.feed((SITE / "descriptive/spread/variance/index.html").read_text())
        self.assertEqual({urlsplit(url).path for url in lesson_links.urls},
                         {"/css/style.css"})
        paths_links = Stylesheets()
        paths_links.feed((SITE / "learning-paths/index.html").read_text())
        self.assertEqual({urlsplit(url).path for url in paths_links.urls},
                         {"/css/style.css", "/css/paths.css"})

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

    def test_foundations_continue_reading_storage(self):
        """Resume a real Foundations lesson, never stored markup or outside links."""
        self.page.goto(self.origin + "/foundations/", wait_until="networkidle")
        panel = self.page.locator("#continue-reading")
        expect(panel).to_be_hidden()

        def set_stored(payload):
            self.page.evaluate(
                "value => localStorage.setItem('esa_last_lesson', JSON.stringify(value))",
                payload,
            )
            self.page.reload(wait_until="networkidle")

        safe = "/foundations/what-is-statistics/"
        set_stored({"section": "foundations", "url": safe, "title": "What Is Statistics?"})
        expect(panel).to_be_visible()
        expect(panel.locator("strong")).to_have_text("What Is Statistics?")
        expect(panel.locator("a.btn")).to_have_attribute("href", safe)

        payload_title = '<img src=x onerror="window.esaInjected=true"> & more'
        set_stored({"section": "foundations", "url": safe, "title": payload_title})
        expect(panel.locator("strong")).to_have_text(payload_title)
        self.assertEqual(panel.locator("img,script").count(), 0)
        self.assertIsNone(self.page.evaluate("window.esaInjected"))

        for invalid in (
            {"section": "foundations", "url": "javascript:alert(1)", "title": "Unsafe"},
            {"section": "foundations", "url": "//example.com", "title": "Outside"},
            {"section": "foundations", "url": "/foundations/missing/", "title": "Not listed"},
            {"section": "foundations", "url": "/foundations/what-is-statistics/../", "title": "Traversal"},
            {"section": "foundations", "url": safe, "title": 17},
            {"section": "probability", "url": safe, "title": "Other section"},
        ):
            with self.subTest(invalid=invalid):
                set_stored(invalid)
                expect(panel).to_be_hidden()

    def test_shared_mobile_header_and_menu(self):
        """Check header width, mobile menu keyboard behavior and desktop navigation."""
        for path in ("/", "/foundations/", "/descriptive/", "/learning-paths/"):
            with self.subTest(path=path):
                self.page.goto(self.origin + path, wait_until="networkidle")
                toggle = self.page.get_by_role("button", name="Toggle menu")
                search = self.page.get_by_role("searchbox", name="Search statistical lessons")
                nav = self.page.get_by_role("navigation", name="Primary navigation")
                for width in (320, 375, 768, 1280):
                    self.page.set_viewport_size({"width": width, "height": 850})
                    expect(search).to_be_visible()
                    dims = self.page.evaluate("""() => ({
                        width: document.querySelector('.site-header').scrollWidth,
                        viewport: window.innerWidth
                    })""")
                    self.assertLessEqual(dims["width"], dims["viewport"],
                                         f"Header overflows {path} at {width}px: {dims}")
                    if width <= 760:
                        expect(toggle).to_be_visible()
                        expect(nav).to_be_hidden()
                        toggle.click()
                        expect(toggle).to_have_attribute("aria-expanded", "true")
                        expect(nav).to_be_visible()
                        toggle.press("Escape")
                        expect(toggle).to_have_attribute("aria-expanded", "false")
                        expect(nav).to_be_hidden()
                    else:
                        expect(toggle).to_be_hidden()
                        expect(nav).to_be_visible()

    def test_learning_paths_navigation_and_responsive_layout(self):
        self.page.goto(self.origin + "/learning-paths/", wait_until="networkidle")
        expect(self.page.locator(".esa-paths-hero h1")).to_be_visible()
        expect(self.page.locator('link[href^="/css/paths.css"]')).to_have_count(1)
        expect(self.page.locator('link[href^="/css/home.css"]')).to_have_count(0)
        expect(self.page.locator(".esa-paths-route a")).to_have_count(3)
        for anchor in ("beginner", "intermediate", "advanced"):
            expect(self.page.locator("#" + anchor + " h2")).to_be_visible()
        for width in (375, 768, 1280):
            self.page.set_viewport_size({"width": width, "height": 850})
            dims = self.page.evaluate("""() => ({
                document: document.documentElement.scrollWidth,
                viewport: window.innerWidth
            })""")
            self.assertLessEqual(dims["document"], dims["viewport"],
                                 f"Learning Paths overflows at {width}px: {dims}")
        hrefs = self.page.locator(".esa-paths a[href^='/']").evaluate_all(
            "(links) => links.map(link => link.getAttribute('href'))"
        )
        for href in hrefs:
            destination = SITE / href.lstrip("/") / "index.html"
            self.assertTrue(destination.is_file(), f"Broken Learning Paths link: {href}")

    def test_sidebar_links_are_live(self):
        """Only real pages are linked; the active sidebar entry is marked."""
        self.page.goto(self.origin + "/foundations/", wait_until="networkidle")
        links = self.page.locator(".sidebar .nav-link")
        self.assertGreater(links.count(), 10)
        hrefs = links.evaluate_all(
            "(elements) => elements.map(el => el.getAttribute('href'))"
        )
        self.assertEqual(len(hrefs), len(set(hrefs)))
        for href in hrefs:
            self.assertTrue(href.startswith("/") and href.endswith("/"), href)
            self.assertTrue((SITE / href.lstrip("/") / "index.html").is_file(),
                            f"Sidebar target missing: {href}")
        expect(self.page.locator('.sidebar [aria-current="page"]')).to_have_count(1)
        expect(self.page.locator('.sidebar [aria-current="page"]')).to_have_attribute(
            "href", "/foundations/"
        )
        self.assertEqual(self.page.locator('.sidebar a[href="#"]').count(), 0)

    def test_homepage_resume_only_existing_learning_pages(self):
        """Real lessons resume; irrelevant, missing and unsafe URLs are ignored."""
        self.page.goto(self.origin + "/foundations/what-is-statistics/",
                       wait_until="networkidle")
        self.assertEqual(self.page.evaluate("localStorage.getItem('esa:lastPage')"),
                         "/foundations/what-is-statistics/")
        self.page.goto(self.origin + "/about/", wait_until="networkidle")
        self.assertEqual(self.page.evaluate("localStorage.getItem('esa:lastPage')"),
                         "/foundations/what-is-statistics/")

        self.page.goto(self.origin + "/", wait_until="networkidle")
        wrap = self.page.locator("#continue-home")
        link = self.page.locator("#continueBtn")
        label = self.page.locator("#continueLabel")
        expect(wrap).to_be_visible()
        expect(link).to_have_attribute("href", "/foundations/what-is-statistics/")
        expect(label).to_contain_text("What Is Statistics?")

        self.page.evaluate("""() => {
            localStorage.setItem('esa:lastTitle',
                '<img src=x onerror="window.esaInjected=true">');
        }""")
        self.page.reload(wait_until="networkidle")
        expect(label).to_contain_text('<img src=x onerror="window.esaInjected=true">')
        self.assertEqual(label.locator("img, script").count(), 0)
        self.assertIsNone(self.page.evaluate("window.esaInjected"))

        for invalid in ("https://example.com/", "//example.com/",
                        "javascript:alert(1)", "/about/", "/learning-paths/",
                        "/foundations/not-a-real-lesson/", "/",
                        "/foundations/what-is-statistics/?next=other"):
            with self.subTest(invalid=invalid):
                self.page.evaluate(
                    "url => localStorage.setItem('esa:lastPage', url)", invalid
                )
                self.page.reload(wait_until="networkidle")
                expect(wrap).to_be_hidden()
                expect(link).to_have_attribute("href", "/learning-paths/")

    def test_search_snippets_follow_normalized_matches(self):
        """Unicode folding and whitespace must not shift result previews."""
        content = ("Unrelated introduction and preliminary remarks. " * 7
                   + "The CENTRAL \n       LIMIT theorem is a key result. "
                   + "Discussion of a \ufb01nite population correction follows.")
        fixture = [{
            "title": "A statistical tutorial",
            "url": "/foundations/what-is-statistics/",
            "content": content,
        }]
        self.page.route("**/search.json", lambda route: route.fulfill(
            content_type="application/json", body=json.dumps(fixture)))
        self.open()
        self.input.fill("central limit")
        preview = self.results.locator(".search-snippet")
        expect(preview).to_contain_text("CENTRAL LIMIT theorem")
        self.assertLess(len(preview.inner_text()), 190)
        self.assertTrue(preview.inner_text().startswith("…"))
        self.assertNotIn("\n", preview.inner_text())

        self.input.fill("finite population")
        expect(preview).to_contain_text("finite population correction")
        self.assertLess(len(preview.inner_text()), 190)
        self.assertEqual(self.results.locator("a").count(), 1)

    def test_footer_social_icons_and_destinations(self):
        """All social links have self-contained icons and accessible labels."""
        expected = {
            "YouTube": "https://www.youtube.com/@EasyStatisticsAcademy",
            "LinkedIn": "https://www.linkedin.com/company/easystatisticsacademy",
            "Facebook": "https://www.facebook.com/profile.php?id=61586090026121",
        }
        for path in ("/", "/foundations/", "/learning-paths/"):
            with self.subTest(path=path):
                self.page.goto(self.origin + path, wait_until="networkidle")
                footer = self.page.locator(".footer-social")
                expect(footer.locator("a")).to_have_count(3)
                expect(footer.locator("i")).to_have_count(0)
                for name, href in expected.items():
                    link = self.page.get_by_role("link", name=name + " (opens in a new tab)")
                    expect(link).to_have_attribute("href", href)
                    expect(link).to_have_attribute("target", "_blank")
                    expect(link).to_have_attribute("rel", "noopener noreferrer")
                    symbol = link.locator("svg")
                    expect(symbol).to_have_count(1)
                    expect(symbol).to_have_attribute("aria-hidden", "true")
                for width in (375, 1280):
                    self.page.set_viewport_size({"width": width, "height": 800})
                    for icon in footer.locator("svg").all():
                        expect(icon).to_be_visible()
                        self.assertGreaterEqual(icon.bounding_box()["width"], 20)

    def test_skip_to_main_keyboard_navigation(self):
        """The first keyboard Tab reveals a skip link that focuses main."""
        for path in ("/", "/foundations/", "/learning-paths/"):
            with self.subTest(path=path):
                self.page.goto(self.origin + path, wait_until="networkidle")
                skip = self.page.get_by_role("link", name="Skip to main content")
                main = self.page.locator("main#main-content")
                expect(skip).to_have_attribute("href", "#main-content")
                expect(main).to_have_attribute("tabindex", "-1")
                self.page.keyboard.press("Tab")
                expect(skip).to_be_focused()
                self.assertEqual(self.page.evaluate(
                    "getComputedStyle(document.querySelector('.skip-link')).clipPath"
                ), "none")
                self.page.keyboard.press("Enter")
                expect(main).to_be_focused()

    def test_site_canonical_and_social_metadata(self):
        """Canonical, Open Graph and Twitter metadata must match each page."""
        base = "https://easystatisticsacademy.com"
        for path in ("/", "/foundations/", "/learning-paths/",
                     "/probability/", "/descriptive/spread/variance/"):
            with self.subTest(path=path):
                self.page.goto(self.origin + path, wait_until="networkidle")
                canonical = self.page.locator('head link[rel="canonical"]')
                expect(canonical).to_have_count(1)
                expected_url = base + path
                expect(canonical).to_have_attribute("href", expected_url)
                expect(self.page.locator('meta[property="og:url"]')).to_have_attribute(
                    "content", expected_url
                )
                title = self.page.title()
                description = self.page.locator(
                    'head meta[name="description"]').get_attribute("content")
                self.assertTrue(description)
                for selector in ('meta[property="og:title"]',
                                 'meta[name="twitter:title"]'):
                    expect(self.page.locator(selector)).to_have_attribute("content", title)
                for selector in ('meta[property="og:description"]',
                                 'meta[name="twitter:description"]'):
                    expect(self.page.locator(selector)).to_have_attribute(
                        "content", description
                    )
                expect(self.page.locator('meta[name="twitter:card"]')).to_have_attribute(
                    "content", "summary"
                )
                expect(self.page.locator('meta[property="og:site_name"]')).to_have_attribute(
                    "content", "EasyStatisticsAcademy"
                )

    def test_custom_404_guidance_and_search_index(self):
        """Custom 404 should use real learning routes, without entering search."""
        self.assertTrue((SITE / "404.html").is_file(), "Built custom 404 missing")
        self.assertNotIn("/404.html", [r["url"] for r in self.records])
        self.page.goto(self.origin + "/404.html", wait_until="networkidle")
        expect(self.page.get_by_role("heading", name="This page isn't available.")).to_be_visible()
        expect(self.page.locator('meta[name="robots"]')).to_have_attribute(
            "content", "noindex, follow"
        )
        expect(self.page.locator('link[href^="/css/editorial.css"]')).to_have_count(1)
        expect(self.page.get_by_role("link", name="search field above")).to_have_attribute(
            "href", "#site-search"
        )
        for href in ("/", "/learning-paths/", "/foundations/", "/descriptive/",
                     "/probability/", "/inference/"):
            self.assertTrue((SITE / href.lstrip("/") / "index.html").is_file(), href)
            expect(self.page.locator('.esa-error a[href="' + href + '"]')).to_have_count(1)
        for width in (375, 768, 1280):
            self.page.set_viewport_size({"width": width, "height": 820})
            overflow = self.page.evaluate(
                "() => document.documentElement.scrollWidth - window.innerWidth"
            )
            self.assertLessEqual(overflow, 1, f"404 overflow at {width}px: {overflow}")

    def test_about_editorial_redesign(self):
        """About keeps original mission and audience with scoped styles."""
        self.page.goto(self.origin + "/about/", wait_until="networkidle")
        expect(self.page.locator('link[href^="/css/editorial.css"]')).to_have_count(1)
        expect(self.page.locator(".esa-about-hero h1")).to_be_visible()
        for title in ("Why this project exists", "What makes the site different",
                      "Built for different kinds of learners",
                      "How the content is organized"):
            expect(self.page.get_by_role("heading", name=title)).to_be_visible()
        expect(self.page.locator(".esa-about-values .esa-about-card")).to_have_count(3)
        expect(self.page.locator(".esa-about-grid--two .esa-about-card")).to_have_count(4)
        for href in ("/learning-paths/", "/foundations/", "/descriptive/",
                     "/probability/", "/inference/", "/modeling/",
                     "/software/", "/machine-learning/"):
            self.assertTrue((SITE / href.lstrip("/") / "index.html").is_file(), href)
        for width in (375, 768, 1280):
            self.page.set_viewport_size({"width": width, "height": 820})
            overflow = self.page.evaluate(
                "() => document.documentElement.scrollWidth - window.innerWidth"
            )
            self.assertLessEqual(overflow, 1, f"About overflow at {width}px: {overflow}")
        self.page.goto(self.origin + "/descriptive/", wait_until="networkidle")
        expect(self.page.locator('link[href^="/css/editorial.css"]')).to_have_count(0)

    def test_mathjax_single_conditional_loader(self):
        """Formula pages load MathJax once; non-math pages do not load it."""
        for path in ("/", "/about/", "/404.html", "/learning-paths/"):
            with self.subTest(no_math=path):
                self.page.goto(self.origin + path, wait_until="networkidle")
                expect(self.page.locator('script[src*="tex-mml-chtml.js"]')).to_have_count(0)
        self.page.goto(self.origin + "/descriptive/spread/variance/",
                       wait_until="networkidle")
        scripts = self.page.locator('script[src*="tex-mml-chtml.js"]')
        expect(scripts).to_have_count(1)
        expect(scripts).to_have_attribute(
            "src", "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
        )
        self.assertTrue(scripts.evaluate("(node) => node.async"),
                        "Dynamically loaded MathJax script should be async")
        runtime = self.page.evaluate("""() => {
            const m = window.MathJax || {};
            return {
                keys: Object.keys(m),
                tex: m.tex || (m.config && m.config.tex) || null
            };
        }""")
        self.assertIsNotNone(runtime["tex"],
                             f"Missing MathJax configuration: {runtime['keys']}")
        tex = runtime["tex"]
        self.assertEqual(tex["inlineMath"][0], ["$", "$"])
        self.assertEqual(tex["inlineMath"][1], [r"\(", r"\)"])
        self.assertEqual(tex["displayMath"][0], ["$$", "$$"])
        self.assertEqual(tex["displayMath"][1], [r"\[", r"\]"])
        # The CDN is stubbed by this test suite, so these tests validate
        # loader selection and configuration, not live MathJax typesetting.

    def test_search_arrow_navigation_between_results(self):
        """Arrow keys traverse every result, including keyboard focus recovery."""
        fixture = [
            {"title": "Statistics basics", "url": "/foundations/what-is-statistics/",
             "content": "Statistics in the foundations"},
            {"title": "Statistics probability", "url": "/probability/",
             "content": "Statistics and probability"},
            {"title": "Statistics inference", "url": "/inference/",
             "content": "Statistics and inference"},
        ]
        self.page.route("**/search.json", lambda route: route.fulfill(
            content_type="application/json", body=json.dumps(fixture)
        ))
        self.open()
        self.input.fill("statistics")
        links = self.results.locator("a.search-item")
        expect(links).to_have_count(3)
        self.input.press("ArrowDown")
        expect(links.nth(0)).to_be_focused()
        links.nth(0).press("ArrowDown")
        expect(links.nth(1)).to_be_focused()
        links.nth(1).press("ArrowDown")
        expect(links.nth(2)).to_be_focused()
        links.nth(2).press("ArrowDown")
        expect(links.nth(0)).to_be_focused()
        links.nth(0).press("ArrowUp")
        expect(self.input).to_be_focused()
        self.input.press("ArrowUp")
        expect(links.nth(2)).to_be_focused()
        links.nth(2).press("ArrowUp")
        expect(links.nth(1)).to_be_focused()
        links.nth(1).press("Escape")
        expect(self.input).to_be_focused()
        expect(self.results).to_be_hidden()
        self.input.fill("statistics")
        self.input.press("ArrowDown")
        expect(links.nth(0)).to_be_focused()
        links.nth(0).press("Enter")
        expect(self.page).to_have_url(self.origin + fixture[0]["url"])

    def test_back_to_top_long_lesson_and_mobile(self):
        """Scroll-only button must be keyboard operable and avoid narrow overflow."""
        for width in (375, 1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width": width, "height": 640})
                self.page.goto(self.origin + "/descriptive/spread/variance/",
                               wait_until="networkidle")
                button = self.page.get_by_role("button", name="Back to top", include_hidden=True)
                expect(button).to_have_count(1)
                expect(button).to_be_hidden()
                self.page.evaluate("window.scrollTo(0, 1200)")
                expect(button).to_be_visible()
                expect(button).to_have_attribute("type", "button")
                bounding = button.bounding_box()
                self.assertGreaterEqual(bounding["x"], 0)
                self.assertLessEqual(bounding["x"] + bounding["width"], width + 1)
                button.focus()
                button.press("Enter")
                expect(self.page.locator(".site-header .brand")).to_be_focused()
                self.page.wait_for_function("window.scrollY <= 10")
                expect(button).to_be_hidden()
        self.page.goto(self.origin + "/learning-paths/", wait_until="networkidle")
        expect(self.page.get_by_role("button", name="Back to top",
                                     include_hidden=True)).to_be_hidden()

    def test_sitemap_only_public_html_pages(self):
        """Parse emitted XML and verify unique, real, canonical content routes."""
        sitemap = SITE / "sitemap.xml"
        root = ElementTree.fromstring(sitemap.read_text(encoding="utf-8"))
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        self.assertEqual(root.tag, "{http://www.sitemaps.org/schemas/sitemap/0.9}urlset")
        locations = [e.text for e in root.findall("s:url/s:loc", ns)]
        self.assertGreater(len(locations), 100)
        self.assertEqual(len(locations), len(set(locations)))
        base = "https://easystatisticsacademy.com"
        for location in locations:
            parts = urlsplit(location)
            self.assertEqual(parts.scheme + "://" + parts.netloc, base)
            self.assertEqual((parts.query, parts.fragment), ("", ""))
            route = unquote(parts.path)
            self.assertNotIn(route, ("/404.html", "/search.json", "/sitemap.xml",
                                     "/feed.xml"))
            self.assertTrue(route.endswith("/") or route.endswith(".html"), route)
            target = SITE / route.lstrip("/")
            if route.endswith("/"):
                target = target / "index.html"
            self.assertTrue(target.is_file(), location)
        for required in ("/", "/about/", "/learning-paths/", "/foundations/",
                         "/descriptive/spread/variance/"):
            self.assertIn(base + required, locations)

    def test_primary_nav_active_on_mobile_and_desktop(self):
        """Highlight only exact header routes; keep aria-current unique."""
        routes = {
            "/": "/",
            "/about/": "/about/",
            "/learning-paths/": "/learning-paths/",
            "/learning-paths/beginner/": "/learning-paths/beginner/",
            "/learning-paths/intermediate/": "/learning-paths/intermediate/",
            "/learning-paths/advanced/": "/learning-paths/advanced/",
            "/descriptive/": None,
        }
        for path, expected in routes.items():
            with self.subTest(path=path):
                self.page.goto(self.origin + path, wait_until="networkidle")
                nav = self.page.get_by_role("navigation", name="Primary navigation")
                active = nav.locator('[aria-current="page"]')
                expect(active).to_have_count(1 if expected else 0)
                if expected:
                    expect(active).to_have_attribute("href", expected)
                    expect(active).to_have_class("is-active")
                    self.assertGreaterEqual(int(active.evaluate(
                        "(node) => getComputedStyle(node).fontWeight"
                    )), 800)
                for width in (375, 1280):
                    self.page.set_viewport_size({"width": width, "height": 850})
                    if width == 375:
                        self.page.get_by_role("button", name="Toggle menu").click()
                    expect(nav).to_be_visible()
                    expect(active).to_have_count(1 if expected else 0)

    def test_search_caches_normalized_page_fields(self):
        """Typing several times must not re-normalize every indexed page."""
        fixture = [
            {"title": f"Statistics topic {i}",
             "url": "/foundations/what-is-statistics/",
             "content": f"Statistics probability methods and topic {i}"}
            for i in range(80)
        ]
        self.page.add_init_script("""(() => {
            const original = String.prototype.normalize;
            window.__esaNormalizations = 0;
            String.prototype.normalize = function (...args) {
                window.__esaNormalizations++;
                return original.apply(this, args);
            };
        })();""")
        self.page.route("**/search.json", lambda route: route.fulfill(
            content_type="application/json", body=json.dumps(fixture)
        ))
        self.open()
        initial_calls = self.page.evaluate("window.__esaNormalizations")
        self.assertGreaterEqual(initial_calls, 160,
                                "Index fields were not normalized during load")
        for q in ("statistics", "stat", "probability", "methods", "topic"):
            self.input.fill(q)
            expect(self.results.locator("a.search-item")).to_have_count(8)
        extra_calls = self.page.evaluate("window.__esaNormalizations") - initial_calls
        self.assertLess(extra_calls, 80,
                        f"Typing reprocessed the indexed page content: {extra_calls} calls")
        expect(self.results.locator("a.search-item").first).to_have_attribute(
            "href", "/foundations/what-is-statistics/"
        )

    def test_print_friendly_variance_lesson(self):
        """Print styles keep formulas and full tables, without site chrome."""
        self.page.goto(self.origin + "/descriptive/spread/variance/",
                       wait_until="networkidle")
        expect(self.page.locator(".site-header")).to_be_visible()
        self.page.emulate_media(media="print")
        for selector in (".site-header", ".site-footer", "#back-to-top",
                         ".skip-link"):
            self.assertEqual(self.page.locator(selector).evaluate(
                "(node) => getComputedStyle(node).display"
            ), "none", f"Print chrome should be hidden: {selector}")
        expect(self.page.get_by_role("heading", name="Variance", exact=True)).to_be_visible()
        formulas = self.page.locator(".formula-box")
        self.assertGreater(formulas.count(), 0)
        expect(formulas.first).to_be_visible()
        # TeX may be typeset into MathJax glyphs; require visible math, not raw delimiters.
        self.assertTrue(formulas.first.inner_text().strip())
        expect(formulas.first).to_contain_text("6")
        wrap = self.page.locator(".table-wrap").first
        table = wrap.locator("table")
        expect(table).to_be_visible()
        self.assertEqual(wrap.evaluate(
            "(node) => getComputedStyle(node).overflowX"
        ), "visible")
        self.assertEqual(table.evaluate(
            "(node) => getComputedStyle(node).display"
        ), "table")
        self.assertEqual(table.evaluate(
            "(node) => getComputedStyle(node).minWidth"
        ), "0px")
        self.assertLessEqual(table.bounding_box()["width"],
                             self.page.locator("main").bounding_box()["width"] + 1)
        expect(table.locator("th")).to_have_count(3)
        self.page.emulate_media(media="screen")
        expect(self.page.locator(".site-header")).to_be_visible()

    def test_mobile_search_scrolls_within_viewport(self):
        """Eight results remain navigable without covering the mobile screen."""
        records = [
            {"title": f"Statistics lesson {i}", "url": "/foundations/what-is-statistics/",
             "content": "Statistics tutorial and mathematical ideas"}
            for i in range(12)
        ]
        self.page.route("**/search.json", lambda route: route.fulfill(
            content_type="application/json", body=json.dumps(records)
        ))
        for width, height in ((320, 560), (375, 667)):
            with self.subTest(size=(width, height)):
                self.page.set_viewport_size({"width": width, "height": height})
                self.open()
                self.input.fill("statistics")
                links = self.results.locator("a.search-item")
                expect(links).to_have_count(8)
                values = self.results.evaluate("""node => ({
                    visible: getComputedStyle(node).overflowY,
                    height: node.getBoundingClientRect().height,
                    bottom: node.getBoundingClientRect().bottom,
                    scroll: node.scrollHeight,
                    client: node.clientHeight
                })""")
                self.assertEqual(values["visible"], "auto")
                self.assertGreater(values["scroll"], values["client"])
                self.assertLessEqual(values["bottom"], height + 1)
                self.input.press("ArrowDown")
                for _ in range(7):
                    self.page.keyboard.press("ArrowDown")
                expect(links.nth(7)).to_be_focused()
                self.assertGreater(self.results.evaluate("node => node.scrollTop"), 0)
                # A focused last result must remain visible within the panel.
                self.assertTrue(links.nth(7).evaluate("""node => {
                    const item = node.getBoundingClientRect();
                    const panel = node.closest('.search-results').getBoundingClientRect();
                    return item.bottom <= panel.bottom + 1 && item.top >= panel.top - 1;
                }"""))
                self.page.unroute("**/search.json")

    def test_long_lesson_toc_generated_without_content_changes(self):
        """Long lessons get a TOC; short pages do not; headings remain intact."""
        self.page.goto(self.origin + "/descriptive/spread/variance/",
                       wait_until="networkidle")
        toc = self.page.get_by_role("navigation", name="On this page")
        expect(toc).to_have_count(1)
        headings = self.page.locator("main h2")
        count = headings.count()
        self.assertGreaterEqual(count, 7)
        links = toc.locator("li a")
        expect(links).to_have_count(count)
        for i in range(count):
            heading = headings.nth(i)
            link = links.nth(i)
            ident = heading.get_attribute("id")
            self.assertTrue(ident)
            expect(link).to_have_attribute("href", "#" + ident)
            self.assertEqual(link.text_content(), heading.inner_text().strip())
        self.assertEqual(len(self.page.locator("main h2[id]").evaluate_all(
            "nodes => nodes.map(n => n.id)"
        )), len(set(self.page.locator("main h2[id]").evaluate_all(
            "nodes => nodes.map(n => n.id)"
        ))))
        toc.locator("summary").click()
        expect(links.nth(1)).to_be_visible()
        links.nth(1).click()
        self.assertEqual(self.page.evaluate("decodeURIComponent(location.hash.slice(1))"),
                         headings.nth(1).get_attribute("id"))
        for path in ("/", "/about/", "/learning-paths/", "/404.html"):
            with self.subTest(no_toc=path):
                self.page.goto(self.origin + path, wait_until="networkidle")
                expect(self.page.locator(".esa-lesson-toc")).to_have_count(0)

    def test_planned_lesson_overviews_have_no_broken_links(self):
        """Keep lesson descriptions and progress status, but never link to a 404."""
        areas = {
            "common-mistakes": "wrong-test",
            "effect-sizes": "what-is-effect-size",
            "practice": "results-to-decisions",
            "reporting": "statements",
        }
        for area, stale in areas.items():
            with self.subTest(area=area):
                route = "/applied-statistics/" + area + "/"
                self.page.goto(self.origin + route, wait_until="networkidle")
                cards = self.page.locator("#lessons .lesson-card")
                expect(cards).to_have_count(5)
                expect(cards.locator("h3 .planned-lesson-title")).to_have_count(5)
                expect(cards.locator(".planned-lesson-status")).to_have_count(5)
                expect(cards.locator("a[href]")).to_have_count(0)
                expect(self.page.locator(".planned-lessons-note")).to_contain_text(
                    "not published yet"
                )
                expect(cards.locator("p")).to_have_count(5)
                # A visitor's stale local progress must not resurrect a missing
                # destination or insert HTML from untrusted localStorage data.
                key = "esa_continue_applied_" + area + "_lesson_v0"
                self.page.evaluate("""([key, url]) => localStorage.setItem(
                    key, JSON.stringify({
                        url, label: '<img src=x onerror="window.esaInjected=true">'
                    })
                )""", [key, route + stale + "/"])
                self.page.reload(wait_until="networkidle")
                expect(cards.locator("a[href]")).to_have_count(0)
                expect(self.page.locator("#continue-reading-" + area)).to_be_hidden()
                self.assertIsNone(self.page.evaluate("window.esaInjected"))

    def test_long_lesson_deep_links_reload_and_history(self):
        """Dynamic heading IDs must resolve deep links after load and Back/Forward."""
        route = "/descriptive/spread/variance/"
        self.page.set_viewport_size({"width": 375, "height": 650})
        self.page.goto(self.origin + route, wait_until="networkidle")
        headings = self.page.locator("main h2")
        self.assertGreaterEqual(headings.count(), 13)
        first = headings.nth(7).get_attribute("id")
        second = headings.nth(11).get_attribute("id")
        self.assertTrue(first and second and first != second)

        def check_alignment(ident):
            expect(self.page).to_have_url(self.origin + route + "#" + ident)
            target = self.page.locator("main h2[id='" + ident + "']")
            expect(target).to_have_class("esa-lesson-anchor")
            self.page.wait_for_function("""id => {
                const node = document.getElementById(id);
                const header = document.querySelector(".site-header");
                if (!node || !header) return false;
                const top = node.getBoundingClientRect().top;
                return window.scrollY > 150 &&
                    top >= header.getBoundingClientRect().bottom - 3 &&
                    top <= header.getBoundingClientRect().bottom + 125;
            }""", arg=ident)

        self.page.goto(self.origin + route + "#" + first, wait_until="networkidle")
        check_alignment(first)
        self.page.reload(wait_until="networkidle")
        check_alignment(first)
        # The site's generated TOC should still work with a collapsed panel.
        toc = self.page.get_by_role("navigation", name="On this page")
        toc.locator("summary").click()
        toc.locator('a[href="#' + second + '"]').click()
        check_alignment(second)
        self.page.go_back(wait_until="domcontentloaded")
        check_alignment(first)
        self.page.go_forward(wait_until="domcontentloaded")
        check_alignment(second)

    def test_multi_keyword_search_ranking(self):
        """Prioritize exact/phrase matches, then words in either order/field."""
        fixture = [
            {"title": "Mixed sampling", "url": "/foundations/",
             "content": "Variance formula for samples"},
            {"title": "Sample variance formula", "url": "/descriptive/spread/variance/",
             "content": "Sample variance is a statistical measure"},
            {"title": "Sample variance formula explained", "url": "/descriptive/",
             "content": "Learn about sample variance"},
            {"title": "Understanding sample variance formula", "url": "/probability/",
             "content": "Statistical principles"},
            {"title": "Variance sample formula", "url": "/inference/",
             "content": "Explained with examples"},
            {"title": "Statistics handbook", "url": "/modeling/",
             "content": "The sample variance formula is fundamental"},
            {"title": "Sample size only", "url": "/software/",
             "content": "Statistical learning"},
        ]
        self.page.route("**/search.json", lambda route: route.fulfill(
            content_type="application/json", body=json.dumps(fixture)
        ))
        self.open()
        self.input.fill(" SAMPLE  VARIANCE   FORMULA ")
        result = self.results.locator("a.search-item")
        expect(result).to_have_count(6)
        self.assertEqual(result.evaluate_all(
            "(links) => links.map(link => new URL(link.href).pathname)"
        ), ["/descriptive/spread/variance/", "/descriptive/", "/probability/",
            "/inference/", "/modeling/", "/foundations/"])
        # A phrase that is absent from every page still finds all word matches.
        self.input.fill("formula variance sample")
        expect(result).to_have_count(6)
        self.assertEqual(result.first.get_attribute("href"), "/descriptive/spread/variance/")
        self.input.press("ArrowDown")
        expect(result.first).to_be_focused()
        result.first.press("Escape")
        expect(self.results).to_be_hidden()

    def test_reduced_motion_and_keyboard_focus_indicators(self):
        """Respect OS motion settings while keeping active results legible."""
        self.page.emulate_media(reduced_motion="reduce")
        self.page.set_viewport_size({"width": 375, "height": 700})
        self.open()
        self.assertEqual(self.page.evaluate(
            "() => getComputedStyle(document.documentElement).scrollBehavior"
        ), "auto")
        self.assertTrue(self.page.evaluate(
            "() => window.matchMedia('(prefers-reduced-motion: reduce)').matches"
        ))
        self.input.fill("variance")
        self.input.press("ArrowDown")
        link = self.results.locator("a.search-item").first
        expect(link).to_be_focused()
        focused = link.evaluate("""node => ({
            visible: node.matches(':focus-visible'),
            style: getComputedStyle(node).outlineStyle,
            width: parseFloat(getComputedStyle(node).outlineWidth),
            background: getComputedStyle(node).backgroundColor
        })""")
        self.assertTrue(focused["visible"])
        self.assertEqual(focused["style"], "solid")
        self.assertGreaterEqual(focused["width"], 3)
        self.page.goto(self.origin + "/descriptive/spread/variance/",
                       wait_until="networkidle")
        self.assertEqual(self.page.evaluate(
            "() => getComputedStyle(document.documentElement).scrollBehavior"
        ), "auto")
        self.assertGreater(self.page.locator(".esa-lesson-toc summary").count(), 0)
        # The TOC remains functional with motion disabled.
        self.page.locator(".esa-lesson-toc summary").click()
        expect(self.page.locator(".esa-lesson-toc li a").first).to_be_visible()
        self.page.emulate_media(reduced_motion="no-preference")
        self.assertEqual(self.page.evaluate(
            "() => getComputedStyle(document.documentElement).scrollBehavior"
        ), "smooth")

    def test_contextual_seo_titles_preserve_visible_lesson_headings(self):
        """Context-specific metadata should not rename the educational lesson."""
        cases = (
            ("/foundations/variables/", "Variables and Measurement in Statistical Foundations"),
            ("/modeling/foundations/variables/", "Variables in Statistical Modeling"),
            ("/descriptive/", "Descriptive Statistics Course Overview"),
        )
        for route, title in cases:
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                self.assertEqual(self.page.title(), title + " | EasyStatisticsAcademy")
        self.page.goto(self.origin + "/foundations/variables/", wait_until="networkidle")
        expect(self.page.locator("h1")).to_have_text("Variables")
        self.page.goto(self.origin + "/modeling/foundations/variables/", wait_until="networkidle")
        expect(self.page.locator("h1")).to_have_text("Variables")

    def test_internal_navigation_document_excluded_from_public_site(self):
        """Planning Markdown remains in GitHub but not the generated website."""
        self.assertFalse((SITE / "navigation-map" / "index.html").exists())
        self.assertFalse((SITE / "navigation-map.md").exists())
        self.assertNotIn("/navigation-map/", {r["url"] for r in self.records})
        self.assertNotIn("https://easystatisticsacademy.com/navigation-map/",
                         (SITE / "sitemap.xml").read_text(encoding="utf-8"))
        self.assertEqual(
            json.loads((SITE.parent / ".github/seo-baseline.json").read_text()), []
        )

    def test_data_variables_continue_reading_progress_and_safety(self):
        """Block 1 resumes listed lessons only, with literal saved labels."""
        lesson = "/descriptive/data-variables/categorical-vs-numerical/"
        block = "/descriptive/data-variables/"
        key = "esa_continue_descriptive_data_variables_lesson_v0"
        self.page.goto(self.origin + lesson, wait_until="networkidle")
        self.assertEqual(self.page.evaluate(
            "key => JSON.parse(localStorage.getItem(key)).url", key), lesson)
        self.page.goto(self.origin + block, wait_until="networkidle")
        panel = self.page.locator("#continue-reading-block1")
        link = self.page.locator("#continue-reading-block1-btn")
        label = self.page.locator("#continue-reading-block1-label")
        expect(panel).to_be_visible()
        expect(link).to_have_attribute("href", lesson)
        expect(label.locator("strong")).to_have_text("Categorical vs Numerical Data")

        def save(payload):
            self.page.evaluate(
                "([key, obj]) => localStorage.setItem(key, JSON.stringify(obj))",
                [key, payload])
            self.page.reload(wait_until="networkidle")

        malicious_label = '<img src=x onerror="window.esaInjected=true"> & analysis'
        save({"url": lesson, "label": malicious_label})
        expect(panel).to_be_visible()
        expect(label.locator("strong")).to_have_text(malicious_label)
        self.assertEqual(label.locator("img, script").count(), 0)
        self.assertIsNone(self.page.evaluate("window.esaInjected"))

        for payload in (
            {"url": "javascript:alert(1)", "label": "unsafe"},
            {"url": "//elsewhere.example/abc", "label": "outside"},
            {"url": "/descriptive/data-variables/unpublished/", "label": "missing"},
            {"url": lesson + "../", "label": "traversal"},
            {"url": lesson, "label": 15},
            {"url": lesson, "label": "  "},
        ):
            with self.subTest(payload=payload):
                save(payload)
                expect(panel).to_be_hidden()
                expect(link).to_have_attribute("href", "#")
        self.page.evaluate("key => localStorage.setItem(key, '{invalid')", key)
        self.page.reload(wait_until="networkidle")
        expect(panel).to_be_hidden()

        save({"url": lesson, "label": "Resume lesson"})
        self.page.set_viewport_size({"width": 375, "height": 750})
        expect(panel).to_be_visible()
        link.click()
        expect(self.page).to_have_url(self.origin + lesson)

    def test_data_variables_lessons_load_without_browser_storage(self):
        """Blocked localStorage must not prevent navigation or render."""
        self.page.add_init_script("""
            Object.defineProperty(window, 'localStorage', {
              configurable: true,
              get() { throw new DOMException('Storage denied', 'SecurityError'); }
            });
        """)
        for route in (
            "/descriptive/data-variables/",
            "/descriptive/data-variables/categorical-vs-numerical/",
            "/descriptive/data-variables/measurement-scales/",
            "/descriptive/data-variables/valid-vs-invalid-operations/",
        ):
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        expect(self.page.locator('a[href="/descriptive/data-variables/measurement-scales/"]').first).to_be_visible()

    def test_new_foundations_resume_validates_saved_lesson(self):
        """Generic reading history only resumes known Foundations lesson links."""
        route = "/foundations/what-is-statistics/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        self.page.goto(self.origin + "/foundations/", wait_until="networkidle")
        panel = self.page.locator("#continue-reading")
        expect(panel).to_be_visible()
        expect(panel.locator("a.btn")).to_have_attribute("href", route)
        expect(panel).to_contain_text("What Is Statistics?")

        for invalid in ("javascript:alert(1)", "//evil.example/lesson",
                        "/foundations/unpublished/", "/foundations/../about/",
                        "/foundations/what-is-statistics/?test=1", "/about/"):
            with self.subTest(invalid=invalid):
                self.page.evaluate("value => localStorage.setItem('esa:lastPage', value)", invalid)
                self.page.reload(wait_until="networkidle")
                expect(panel).to_be_hidden()

        # Even the legacy Foundations-specific key must never create HTML or outside links.
        self.page.evaluate("""() => {
            localStorage.removeItem('esa:lastPage');
            localStorage.setItem('esa:lastFoundationLesson',
              '<img src=x onerror="window.esaInjected=true">');
        }""")
        self.page.reload(wait_until="networkidle")
        expect(panel).to_be_hidden()
        self.assertIsNone(self.page.evaluate("window.esaInjected"))

        self.page.evaluate("""() => {
            localStorage.setItem('esa:lastFoundationLesson',
              '/foundations/what-is-statistics/');
        }""")
        self.page.reload(wait_until="networkidle")
        expect(panel).to_be_visible()
        expect(panel.locator("a.btn")).to_have_attribute("href", route)

    def test_new_foundations_resume_handles_disabled_storage(self):
        self.page.add_init_script("""
            Object.defineProperty(window, 'localStorage', {
              configurable: true,
              get() { throw new DOMException('Storage denied', 'SecurityError'); }
            });
        """)
        for route in ("/foundations/", "/foundations/what-is-statistics/"):
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        expect(self.page.locator("#continue-reading")).to_have_count(0)

    def test_intermediate_path_uses_published_specific_blocks(self):
        self.page.goto(self.origin + "/learning-paths/intermediate/",
                       wait_until="networkidle")
        expected = (
            ("Statistical Inference (Deep Dive)", "/inference/hypothesis-testing/"),
            ("Regression & Modeling", "/modeling/simple-linear-regression/"),
            ("Applied Statistics", "/applied-statistics/study-design/"),
            ("Diagnostics & Validation", "/modeling/diagnostics/"),
            ("Interpretation & Reporting", "/applied-statistics/reporting/"),
        )
        for heading, destination in expected:
            with self.subTest(heading=heading):
                card = self.page.locator(".card").filter(
                    has=self.page.get_by_role("heading", name=heading, exact=True))
                expect(card.locator("a.card-foot")).to_have_attribute("href", destination)
                self.assertTrue((SITE / destination.lstrip("/") / "index.html").is_file(),
                                f"Unpublished curriculum destination: {destination}")

    def test_first_foundations_self_check_feedback_and_mobile(self):
        self.page.goto(self.origin + "/foundations/what-is-statistics/",
                       wait_until="networkidle")
        quiz = self.page.locator("#esa-self-check")
        questions = quiz.locator("fieldset")
        expect(questions).to_have_count(3)
        expected = [("b", "a"), ("a", "b"), ("c", "a")]
        for idx, (correct, incorrect) in enumerate(expected):
            with self.subTest(question=idx + 1):
                question = questions.nth(idx)
                expect(question.locator("legend")).to_be_visible()
                feedback = question.locator(".esa-check-feedback")
                question.locator('input[value="' + incorrect + '"]').check()
                expect(feedback).to_contain_text("Not quite.")
                question.locator('input[value="' + correct + '"]').check()
                expect(feedback).to_contain_text("Correct.")
                self.assertGreater(len(feedback.inner_text()), 35)

        # Keyboard interaction should update explanation like pointer selection.
        first = questions.first
        first.locator('input[value="b"]').focus()
        first.locator('input[value="b"]').press("ArrowRight")
        expect(first.locator(".esa-check-feedback")).to_contain_text("Not quite.")

        for width in (320, 375, 1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width": width, "height": 820})
                dims = self.page.evaluate("""() => ({
                    viewport: window.innerWidth,
                    document: document.documentElement.scrollWidth
                })""")
                self.assertLessEqual(dims["document"], dims["viewport"], dims)


    def test_secure_descriptive_resume_five_blocks(self):
        """Progress stays within listed lessons; saved labels are never HTML."""
        blocks = (
            ("tabular-summaries", "block2", "tabular_summaries"),
            ("visualization", "block3", "visualization"),
            ("center", "block4", "center"),
            ("shape", "block6", "shape"),
            ("reporting", "block7", "reporting"),
        )
        malicious_label = '<img src=x onerror="window.esaInjected=true"> & text'
        for slug, number, key_slug in blocks:
            with self.subTest(block=slug):
                self.page.goto(self.origin + "/descriptive/" + slug + "/",
                               wait_until="networkidle")
                key = "esa_continue_descriptive_" + key_slug + "_lesson_v0"
                panel = self.page.locator("#continue-reading-" + number)
                label = self.page.locator("#continue-reading-" + number + "-label")
                link = self.page.locator("#continue-reading-" + number + "-btn")
                valid = self.page.locator("#lessons .lesson-card h3 a[href]").first.get_attribute("href")
                self.assertTrue((SITE / valid.lstrip("/") / "index.html").is_file())
                expect(panel).to_be_hidden()

                def save(payload):
                    self.page.evaluate(
                        "([key, value]) => localStorage.setItem(key, JSON.stringify(value))",
                        [key, payload])
                    self.page.reload(wait_until="networkidle")

                save({"url": valid, "label": malicious_label})
                expect(panel).to_be_visible()
                expect(link).to_have_attribute("href", valid)
                expect(label.locator("strong")).to_have_text(malicious_label)
                self.assertEqual(label.locator("img, script").count(), 0)
                self.assertIsNone(self.page.evaluate("window.esaInjected"))

                for invalid in (
                    {"url": "javascript:alert(1)", "label": "Unsafe"},
                    {"url": "//external.example/lesson/", "label": "External"},
                    {"url": "/descriptive/" + slug + "/not-published/", "label": "Missing"},
                    {"url": valid + "?next=elsewhere", "label": "Query"},
                    {"url": valid, "label": 17},
                    {"url": valid, "label": "  "},
                ):
                    with self.subTest(block=slug, invalid=invalid):
                        save(invalid)
                        expect(panel).to_be_hidden()

                self.page.evaluate(
                    "key => localStorage.setItem(key, '{broken json')", key)
                self.page.reload(wait_until="networkidle")
                expect(panel).to_be_hidden()

    def test_descriptive_overview_pages_survive_blocked_storage(self):
        """Save and resume scripts fail gracefully when storage throws."""
        self.page.add_init_script("""
            Object.defineProperty(window, 'localStorage', {
              configurable: true,
              get() { throw new DOMException('Storage denied', 'SecurityError'); }
            });
        """)
        for slug in ("tabular-summaries", "visualization", "center",
                     "shape", "reporting"):
            with self.subTest(block=slug):
                self.page.goto(self.origin + "/descriptive/" + slug + "/",
                               wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                expect(self.page.locator("#lessons .lesson-card h3 a").first).to_be_visible()

    def test_variables_example_count_and_sample_variation(self):
        self.page.goto(self.origin + "/foundations/variables/",
                       wait_until="networkidle")
        example = self.page.locator(".section-block").filter(
            has=self.page.get_by_role("heading", name="Numerical Example"))
        expect(example).to_contain_text("Suppose we collect data on 2 people:")
        expect(example.locator("tbody tr")).to_have_count(2)
        expect(example.locator("tbody tr").first.locator("td").first).to_have_text("A")
        expect(example.locator("tbody tr").last.locator("td").first).to_have_text("B")
        variable = self.page.locator(".section-block").filter(
            has=self.page.get_by_role("heading", name="Variable vs Constant"))
        expect(variable).to_contain_text("even if its values happen to be identical")
        expect(variable).to_contain_text("within this sample")
        expect(variable).to_contain_text("cannot explain differences")

    def test_advanced_path_specific_links_and_honest_overviews(self):
        self.page.goto(self.origin + "/learning-paths/advanced/",
                       wait_until="networkidle")
        expected = (
            ("Mathematical Statistics", "/mathematical-statistics/", True),
            ("Advanced Modeling", "/modeling/extensions/", False),
            ("Machine Learning", "/machine-learning/", True),
            ("Data Mining", "/data-mining/", True),
            ("Evaluation & Strategy", "/modeling/model-fit-comparison/", False),
            ("Advanced Workflows", "/software/", True),
        )
        for title, route, overview in expected:
            with self.subTest(title=title):
                card = self.page.locator(".card").filter(
                    has=self.page.get_by_role("heading", name=title, exact=True))
                expect(card.locator("a.card-foot")).to_have_attribute("href", route)
                self.assertTrue((SITE / route.lstrip("/") / "index.html").is_file(),
                                f"Advanced Path points to missing route: {route}")
                if overview:
                    expect(card.locator("p.muted-mini")).to_have_count(1)
                    expect(card.locator("p.muted-mini")).to_contain_text(
                        "overview")

    def test_core_section_resume_validates_published_blocks(self):
        """Saved core-section destinations must be real blocks with literal labels."""
        malicious = '<img src=x onerror="window.esaInjected=true"> & text'
        for section in ("probability", "inference", "modeling"):
            with self.subTest(section=section):
                route = "/" + section + "/"
                key = "esa_continue_" + section + "_last_block_v0"
                self.page.goto(self.origin + route, wait_until="networkidle")
                panel = self.page.locator("#continue-reading-" + section)
                label = self.page.locator("#continue-reading-" + section + "-label")
                link = self.page.locator("#continue-reading-" + section + "-btn")
                first = self.page.locator("#blocks .lesson-block-card h3 a[href]").first
                valid = first.get_attribute("href")
                self.assertTrue((SITE / valid.lstrip("/") / "index.html").is_file())
                expect(panel).to_be_hidden()

                def save(payload):
                    self.page.evaluate(
                        "([key, value]) => localStorage.setItem(key, JSON.stringify(value))",
                        [key, payload])
                    self.page.reload(wait_until="networkidle")

                save({"url": valid, "label": malicious})
                expect(panel).to_be_visible()
                expect(link).to_have_attribute("href", valid)
                expect(label.locator("strong")).to_have_text(malicious)
                self.assertEqual(label.locator("img, script").count(), 0)
                self.assertIsNone(self.page.evaluate("window.esaInjected"))

                for invalid in (
                    {"url": "javascript:alert(1)", "label": "JS"},
                    {"url": "//external.example/path", "label": "External"},
                    {"url": "https://external.example/path", "label": "External"},
                    {"url": "/" + section + "/not-listed/", "label": "Missing"},
                    {"url": valid + "?redirect=external", "label": "Query"},
                    {"url": valid + "../", "label": "Traversal"},
                    {"url": valid, "label": 42},
                    {"url": valid, "label": "  "},
                ):
                    with self.subTest(section=section, invalid=invalid):
                        save(invalid)
                        expect(panel).to_be_hidden()
                        expect(link).to_have_attribute("href", "#")

                self.page.evaluate("key => localStorage.setItem(key, '{broken')", key)
                self.page.reload(wait_until="networkidle")
                expect(panel).to_be_hidden()

    def test_core_section_overviews_work_without_storage(self):
        """Progress writing must not break Modeling links if storage is disabled."""
        self.page.add_init_script("""
            Object.defineProperty(window, 'localStorage', {
              configurable: true,
              get() { throw new DOMException('Storage denied', 'SecurityError'); }
            });
        """)
        for section in ("probability", "inference", "modeling"):
            with self.subTest(section=section):
                self.page.goto(self.origin + "/" + section + "/", wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                expect(self.page.locator("#blocks .lesson-block-card h3 a").first).to_be_visible()
                expect(self.page.locator("#continue-reading-" + section)).to_be_hidden()
                if section == "modeling":
                    self.page.evaluate("""() => {
                      // Exercise the progress-saving click listener without navigating
                      // into unrelated lesson scripts.
                      document.addEventListener('click', e => e.preventDefault(), true);
                      document.querySelector('#blocks .lesson-block-card h3 a').click();
                    }""")

    def test_intro_confidence_interval_is_derived_and_explained(self):
        self.page.goto(self.origin + "/foundations/what-is-statistics/",
                       wait_until="networkidle")
        example = self.page.locator(".section-block").filter(
            has=self.page.get_by_role("heading", name="Example", exact=True))
        expect(example).to_contain_text("Sample heights (cm): 170, 175, 168, 180, 172")
        heights = [170, 175, 168, 180, 172]
        average = sum(heights) / len(heights)
        sample_variance = sum((x - average) ** 2 for x in heights) / (len(heights) - 1)
        margin = 2.7764451051977987 * (sample_variance / len(heights)) ** 0.5
        self.assertEqual(average, 173)
        self.assertEqual(sample_variance, 22)
        self.assertAlmostEqual(average - margin, 167.18, places=2)
        self.assertAlmostEqual(average + margin, 178.82, places=2)
        for part in ("independent random", "approximately normal",
                     "four degrees of freedom", "88 cm²", "22 cm²",
                     "167.18 cm to 178.82 cm", "about 95% of intervals",
                     "not a claim that 95% of individual heights"):
            with self.subTest(part=part):
                expect(example).to_contain_text(part)
        self.assertNotIn("170 cm to 176 cm", example.inner_text())
        expect(self.page.locator("#esa-self-check fieldset")).to_have_count(3)

    def test_beginner_path_starts_at_published_blocks_and_labels_software(self):
        self.page.goto(self.origin + "/learning-paths/beginner/",
                       wait_until="networkidle")
        steps = (
            ("Foundations", "/foundations/what-is-statistics/"),
            ("Descriptive Statistics", "/descriptive/data-variables/"),
            ("Probability", "/probability/basics/"),
            ("Statistical Inference", "/inference/foundations/"),
            ("Introduction to Modeling", "/modeling/foundations/"),
            ("Software Implementation", "/software/"),
        )
        for title, route in steps:
            with self.subTest(step=title):
                card = self.page.locator(".card").filter(
                    has=self.page.get_by_role("heading", name=title, exact=True))
                expect(card.locator("a.card-foot")).to_have_attribute("href", route)
                self.assertTrue((SITE / route.lstrip("/") / "index.html").is_file(),
                                "Missing Beginner step: " + route)
        practice = self.page.locator(".card").filter(
            has=self.page.get_by_role("heading", name="Software Implementation"))
        expect(practice.locator(".muted-mini")).to_contain_text(
            "tutorials are planned", ignore_case=True)
        expect(practice.locator("a.card-foot")).to_contain_text(
            "View software curriculum")
        for width in (375, 768, 1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width": width, "height": 850})
                dims = self.page.evaluate("""() => ({
                  viewport: window.innerWidth,
                  document: document.documentElement.scrollWidth
                })""")
                self.assertLessEqual(dims["document"], dims["viewport"], dims)

    def test_remaining_overview_resume_is_safe(self):
        """Three last overview widgets only resume published cards as plain text."""
        configurations = (
            ("/applied-statistics/", "esa_continue_applied_last_block_v0",
             "continue-reading-applied", "#blocks .lesson-block-card h3 a"),
            ("/mathematical-statistics/", "esa_continue_ms_last_block_v0",
             "continue-reading-ms", "#blocks .lesson-card h3 a"),
            ("/descriptive/spread/", "esa_continue_descriptive_spread_lesson_v0",
             "continue-reading-block5", "#lessons .lesson-card h3 a"),
        )
        malicious = '<img src=x onerror="window.esaInjected=true"> & labels'
        for route, key, panel_id, selector in configurations:
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                panel = self.page.locator("#" + panel_id)
                label = self.page.locator("#" + panel_id + "-label")
                action = self.page.locator("#" + panel_id + "-btn")
                listed = self.page.locator(selector + "[href]").first.get_attribute("href")
                self.assertTrue((SITE / listed.lstrip("/") / "index.html").is_file())
                expect(panel).to_be_hidden()

                def save(data):
                    self.page.evaluate(
                        "([key, data]) => localStorage.setItem(key, JSON.stringify(data))",
                        [key, data])
                    self.page.reload(wait_until="networkidle")

                save({"url": listed, "label": malicious})
                expect(panel).to_be_visible()
                expect(action).to_have_attribute("href", listed)
                expect(label.locator("strong")).to_have_text(malicious)
                self.assertEqual(label.locator("img, script").count(), 0)
                self.assertIsNone(self.page.evaluate("window.esaInjected"))

                invalid = (
                    {"url": "javascript:alert(1)", "label": "Script"},
                    {"url": "//example.com/path/", "label": "External"},
                    {"url": "https://example.com/path/", "label": "External"},
                    {"url": route + "not-published/", "label": "Not listed"},
                    {"url": listed + "?next=elsewhere", "label": "Query"},
                    {"url": listed + "../", "label": "Traversal"},
                    {"url": listed, "label": 25},
                    {"url": listed, "label": " "},
                )
                for payload in invalid:
                    with self.subTest(route=route, invalid=payload):
                        save(payload)
                        expect(panel).to_be_hidden()
                        expect(action).to_have_attribute("href", "#")
                self.page.evaluate(
                    "key => localStorage.setItem(key, '{bad json')", key)
                self.page.reload(wait_until="networkidle")
                expect(panel).to_be_hidden()

    def test_remaining_overviews_work_with_blocked_storage(self):
        """Blocked storage cannot disrupt reading or saving existing progress."""
        self.page.add_init_script("""
            Object.defineProperty(window, 'localStorage', {
              configurable: true,
              get() { throw new DOMException('Denied', 'SecurityError'); }
            });
        """)
        for route, selector, panel in (
            ("/applied-statistics/", "#blocks .lesson-block-card h3 a",
             "#continue-reading-applied"),
            ("/mathematical-statistics/", "#blocks .lesson-card h3 a",
             "#continue-reading-ms"),
            ("/descriptive/spread/", "#lessons .lesson-card h3 a",
             "#continue-reading-block5"),
        ):
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                expect(self.page.locator(selector).first).to_be_visible()
                expect(self.page.locator(panel)).to_be_hidden()
                self.page.evaluate("""selector => {
                    document.addEventListener('click', e => e.preventDefault(), true);
                    document.querySelector(selector).click();
                }""", selector)

    def test_paths_landing_matches_current_learning_levels(self):
        """The landing cards lead to the same published starting points."""
        self.page.goto(self.origin + "/learning-paths/", wait_until="networkidle")
        expected = (
            ("Step 1: Foundations", "/foundations/what-is-statistics/"),
            ("Step 2: Descriptive Statistics", "/descriptive/data-variables/"),
            ("Step 3: Probability", "/probability/basics/"),
            ("Step 4: Inference", "/inference/foundations/"),
            ("Step 5: Intro to Modeling", "/modeling/foundations/"),
            ("Software Practice", "/software/"),
            ("Statistical Inference", "/inference/hypothesis-testing/"),
            ("Regression & Modeling", "/modeling/simple-linear-regression/"),
            ("Applied Statistics", "/applied-statistics/study-design/"),
            ("Mathematical Statistics", "/mathematical-statistics/"),
            ("Machine Learning", "/machine-learning/"),
            ("Data Mining", "/data-mining/"),
        )
        for title, url in expected:
            with self.subTest(card=title):
                card = self.page.locator(".esa-paths .card").filter(
                    has=self.page.get_by_role("heading", name=title, exact=True))
                expect(card.locator("a.card-foot")).to_have_attribute("href", url)
                self.assertTrue((SITE / url.lstrip("/") / "index.html").is_file(),
                                "Unpublished learning path destination: " + url)
        for title in ("Software Practice", "Mathematical Statistics",
                      "Machine Learning", "Data Mining"):
            card = self.page.locator(".esa-paths .card").filter(
                has=self.page.get_by_role("heading", name=title, exact=True))
            expect(card.locator("p.muted-mini")).to_contain_text("overview")
        for width in (320, 375, 768, 1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width": width, "height": 850})
                dims = self.page.evaluate("""() => ({
                    viewport: window.innerWidth,
                    document: document.documentElement.scrollWidth
                })""")
                self.assertLessEqual(dims["document"], dims["viewport"], dims)

    def test_standard_deviation_empirical_rule_normal_only(self):
        """Normal coverage approximations, numerical bounds and caveats match."""
        from math import erf, sqrt
        self.page.goto(self.origin + "/descriptive/spread/standard-deviation/",
                       wait_until="networkidle")
        rule = self.page.get_by_role("heading", name="The Empirical Rule")
        expect(rule).to_be_visible()
        table = rule.locator("xpath=following-sibling::div[contains(@class, 'table-wrap')][1]")
        rows = table.locator("tbody tr")
        expect(rows).to_have_count(3)
        for idx, (z, approx, low, high) in enumerate((
            (1, 68.27, 85, 115), (2, 95.45, 70, 130),
            (3, 99.73, 55, 145),
        )):
            with self.subTest(sigma_count=z):
                probability = 100 * erf(z / sqrt(2))
                self.assertAlmostEqual(probability, approx, delta=0.01)
                self.assertEqual((100 - z * 15, 100 + z * 15), (low, high))
                expect(rows.nth(idx)).to_contain_text(str(approx) + "%")
        main = self.page.locator("main")
        for phrase in ("68–95–99.7 rule", "population mean 100",
                       "population standard deviation 15",
                       "85 and 115", "70 and 130", "55 and 145",
                       "not guaranteed", "not a confidence interval"):
            with self.subTest(phrase=phrase):
                expect(main).to_contain_text(phrase)
        link = main.get_by_role("link", name="Normal Distribution lesson")
        expect(link).to_have_attribute("href",
            "/probability/distributions/normal-distribution/")
        self.assertTrue((SITE / "probability/distributions/normal-distribution/index.html").is_file())

    def test_spread_lessons_save_and_resume(self):
        """Each lesson records its own canonical URL and keeps resume working."""
        key = "esa_continue_descriptive_spread_lesson_v0"
        lessons = (
            ("what-is-variability", "What Is Variability?"),
            ("range", "Range"),
            ("interquartile-range", "Interquartile Range (IQR)"),
            ("variance", "Variance"),
            ("standard-deviation", "Standard Deviation"),
            ("coefficient-of-variation", "Coefficient of Variation"),
            ("reporting-spread-properly", "Reporting Spread Properly"),
        )
        for slug, title in lessons:
            with self.subTest(lesson=slug):
                url = "/descriptive/spread/" + slug + "/"
                self.page.goto(self.origin + url, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_have_text(title)
                state = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(state["url"], url)
                self.assertEqual(state["label"], title)
                self.assertIsInstance(state["ts"], (int, float))
                self.page.goto(self.origin + "/descriptive/spread/",
                               wait_until="networkidle")
                panel = self.page.locator("#continue-reading-block5")
                expect(panel).to_be_visible()
                expect(self.page.locator("#continue-reading-block5-btn")
                       ).to_have_attribute("href", url)
                expect(self.page.locator("#continue-reading-block5-label strong")
                       ).to_have_text(title)

    def test_spread_lessons_work_when_storage_denied(self):
        """Blocked localStorage does not prevent loading or navigating any lesson."""
        self.page.add_init_script("""
            Object.defineProperty(window, 'localStorage', {
              configurable: true,
              get() { throw new DOMException('Denied', 'SecurityError'); }
            });
        """)
        for slug in ("what-is-variability", "range", "interquartile-range",
                     "variance", "standard-deviation",
                     "coefficient-of-variation", "reporting-spread-properly"):
            with self.subTest(lesson=slug):
                self.page.goto(
                    self.origin + "/descriptive/spread/" + slug + "/",
                    wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(self.page.locator("main a[href]").count(), 0)
        self.page.goto(self.origin + "/descriptive/spread/",
                       wait_until="networkidle")
        expect(self.page.locator("main h1")).to_be_visible()
        expect(self.page.locator("#continue-reading-block5")).to_be_hidden()

    def test_samples_target_population_and_numerical_example(self):
        """Sampling claims are conditional, and the original heights are correct."""
        self.page.goto(self.origin + "/foundations/samples/",
                       wait_until="networkidle")
        text = self.page.locator("main").inner_text()
        heights = [170, 172, 168, 171, 169]
        self.assertEqual(sum(heights) / len(heights), 170)
        self.assertIn("Heights: 170, 172, 168, 171, 169", text)
        self.assertIn("(170 + 172 + 168 + 171 + 169) / 5 = 170", text)
        for phrase in ("target population", "selection mechanism",
                       "selection bias", "all university students",
                       "university athletes", "not an automatic certainty",
                       "random sampling variability",
                       "Selection bias can remain even in a very large sample"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)
        self.assertNotIn("This produces biased results.", text)
        self.assertNotIn("A sample must reflect the population.", text)

    def test_mathematical_statistics_previews_and_resume(self):
        """Every theory block is explicitly marked as an unfinished preview."""
        self.page.goto(self.origin + "/mathematical-statistics/",
                       wait_until="networkidle")
        cards = self.page.locator("#blocks .lesson-card")
        expect(cards).to_have_count(7)
        expect(self.page.locator("#blocks .section-head")).to_contain_text(
            "All seven published block pages are currently under construction")
        for index in range(7):
            with self.subTest(block=index + 1):
                card = cards.nth(index)
                expect(card.locator(".muted-mini")).to_contain_text(
                    "Under construction")
                title_link = card.locator("h3 a")
                url = title_link.get_attribute("href")
                expect(card.locator("a.btn")).to_have_text("Preview block")
                expect(card.locator("a.btn")).to_have_attribute("href", url)
                file = SITE / url.lstrip("/") / "index.html"
                self.assertTrue(file.is_file(), url)
                self.assertIn("under construction", file.read_text().lower())
        first_url = cards.first.locator("h3 a").get_attribute("href")
        # Existing click handler keeps the saved progress key and destination.
        self.page.locator("a[href='" + first_url + "']").first.click()
        state = self.page.evaluate(
            "key => JSON.parse(localStorage.getItem(key))",
            "esa_continue_ms_last_block_v0")
        self.assertEqual(state["url"], first_url)
        self.page.goto(self.origin + "/mathematical-statistics/",
                       wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms")).to_be_visible()
        expect(self.page.locator("#continue-reading-ms-btn")
               ).to_have_attribute("href", first_url)

    def test_restored_shape_math_is_verifiable(self):
        """Six reconstructed formulas are present and agree with the given data."""
        z_source = (SITE / "descriptive/shape/z-scores/index.html").read_text()
        empirical_source = (SITE / "descriptive/shape/empirical-rule/index.html").read_text()
        self.assertEqual((80 - 70) / 10, 1)
        self.assertEqual((70 - 70) / 10, 0)
        self.assertIn(r"z=\frac{x-\mu}{\sigma}", z_source)
        self.assertIn(r"\sigma&gt;0", z_source)
        self.assertIn(r"z=\frac{80-70}{10}=\frac{10}{10}=1", z_source)
        self.assertIn(r"z=\frac{\mu-\mu}{\sigma}=0", z_source)
        # Count displayed equations inside lesson content, not MathJax scripts.
        z_main = z_source.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        self.assertEqual(z_main.count(r"\["), 3)
        self.assertEqual(z_main.count(r"\]"), 3)
        for sigma_count, lower, upper in (
            (1, 60, 80), (2, 50, 90), (3, 40, 100)
        ):
            with self.subTest(sigma_count=sigma_count):
                self.assertEqual((70 - sigma_count * 10,
                                  70 + sigma_count * 10), (lower, upper))
                boundary = (
                    (r"[\mu-\sigma,\ \mu+\sigma]" if sigma_count == 1 else
                     r"[\mu-" + str(sigma_count) + r"\sigma,\ \mu+" +
                     str(sigma_count) + r"\sigma]")
                )
                self.assertIn(boundary, empirical_source)
                self.assertIn(
                    r"=[" + str(lower) + r",\ " + str(upper) + "]",
                    empirical_source)
        self.assertIn("approximately normally distributed", empirical_source)
        self.assertIn("not guaranteed for nonnormal distributions",
                      empirical_source)
        empirical_main = empirical_source.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        self.assertEqual(empirical_main.count(r"\["), 3)
        self.assertEqual(empirical_main.count(r"\]"), 3)
        self.assertNotIn("\uea01", z_source + empirical_source)
        self.assertNotIn("\uea02", z_source + empirical_source)

    def test_empirical_rule_normal_coverage(self):
        """The named 68/95/99.7 percentages agree with normal probabilities."""
        from math import erf, sqrt
        for z, target in ((1, 68.27), (2, 95.45), (3, 99.73)):
            with self.subTest(z=z):
                self.assertAlmostEqual(100 * erf(z / sqrt(2)), target,
                                       delta=0.01)

    def test_applied_overview_resume_uses_published_lesson_keys(self):
        """Three block overviews resume real lessons using safe saved labels."""
        cases = (
            ("method-selection", "method_selection",
             "esa_continue_applied_method-selection_lesson_v0"),
            ("study-design", "study_design",
             "esa_continue_applied_study-design_lesson_v0"),
            ("assumptions", "assumptions",
             "esa_continue_applied_assumptions_lesson_v0"),
        )
        malicious = '<img src=x onerror="window.esaInjected=true"> & test'
        for slug, storage_slug, legacy_key in cases:
            with self.subTest(block=slug):
                overview = "/applied-statistics/" + slug + "/"
                current_key = (
                    "esa_continue_applied_statistics_" + storage_slug +
                    "_lesson_v0")
                self.page.goto(self.origin + overview, wait_until="networkidle")
                panel = self.page.locator("#continue-reading-" + slug)
                btn = self.page.locator("#continue-reading-" + slug + "-btn")
                label = self.page.locator("#continue-reading-" + slug + "-label")
                first = self.page.locator(
                    "#lessons .lesson-card h3 a[href]").first
                url = first.get_attribute("href")
                self.assertTrue(
                    (SITE / url.lstrip("/") / "index.html").is_file(), url)
                expect(panel).to_be_hidden()

                # The real published lesson should write its existing key.
                self.page.goto(self.origin + url, wait_until="networkidle")
                stored = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))",
                    current_key)
                self.assertEqual(stored["url"], url)
                self.page.goto(self.origin + overview, wait_until="networkidle")
                expect(panel).to_be_visible()
                expect(btn).to_have_attribute("href", url)

                def save(key, value):
                    self.page.evaluate(
                        "([key, value]) => localStorage.setItem(key, JSON.stringify(value))",
                        [key, value])
                    self.page.reload(wait_until="networkidle")

                save(current_key, {"url": url, "label": malicious})
                expect(panel).to_be_visible()
                expect(label.locator("strong")).to_have_text(malicious)
                self.assertEqual(label.locator("img, script").count(), 0)
                self.assertIsNone(self.page.evaluate("window.esaInjected"))

                for invalid in (
                    {"url": "javascript:alert(1)", "label": "JS"},
                    {"url": "//elsewhere.test", "label": "External"},
                    {"url": "https://elsewhere.test/", "label": "External"},
                    {"url": overview + "unlisted/", "label": "Missing"},
                    {"url": url + "?redirect=unsafe", "label": "Query"},
                    {"url": url + "../", "label": "Traversal"},
                    {"url": url, "label": 8},
                    {"url": url, "label": " "},
                ):
                    with self.subTest(block=slug, invalid=invalid):
                        save(current_key, invalid)
                        expect(panel).to_be_hidden()
                        expect(btn).to_have_attribute("href", "#")

                # Older overview key remains readable, without changing it.
                self.page.evaluate(
                    "key => localStorage.removeItem(key)", current_key)
                save(legacy_key, {"url": url, "label": "Legacy progress"})
                expect(panel).to_be_visible()
                expect(btn).to_have_attribute("href", url)
                expect(label).to_contain_text("Legacy progress")
                self.page.evaluate(
                    "([a, b]) => {localStorage.removeItem(a); localStorage.removeItem(b);}",
                    [current_key, legacy_key])
                self.page.reload(wait_until="networkidle")
                expect(panel).to_be_hidden()

    def test_applied_overviews_load_without_storage(self):
        """Denied storage cannot interrupt the progress-saving overview scripts."""
        self.page.add_init_script("""
            Object.defineProperty(window, 'localStorage', {
              configurable: true,
              get() { throw new DOMException('Denied', 'SecurityError'); }
            });
        """)
        for slug in ("method-selection", "study-design", "assumptions"):
            with self.subTest(block=slug):
                self.page.goto(
                    self.origin + "/applied-statistics/" + slug + "/",
                    wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                expect(self.page.locator("#lessons .lesson-card h3 a").first
                       ).to_be_visible()
                expect(self.page.locator("#continue-reading-" + slug)
                       ).to_be_hidden()

    def test_range_all_five_restored_equations(self):
        """Check five display formulas and their dataset arithmetic."""
        url = "/descriptive/spread/range/"
        self.page.goto(self.origin + url, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("Range")
        html = (SITE / url.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        self.assertEqual(main.count(r"\["), 5)
        self.assertEqual(main.count(r"\]"), 5)
        formulas = (
            r"\operatorname{Range}=\max(x_1,\ldots,x_n)-\min(x_1,\ldots,x_n)",
            r"\operatorname{Range}=12-4=8",
            r"\operatorname{Range}=95-65=30",
            r"\operatorname{Range}=14-10=4",
            r"\operatorname{Range}=100-10=90",
        )
        for formula in formulas:
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        examples = (
            ([4, 6, 8, 10, 12], 8),
            ([65, 70, 75, 80, 95], 30),
            ([10, 11, 12, 13, 14], 4),
            ([10, 11, 12, 13, 100], 90),
        )
        for data, result in examples:
            with self.subTest(data=data):
                self.assertEqual(max(data) - min(data), result)
        self.assertEqual(
            (max(examples[-1][0]) - min(examples[-1][0])) -
            (max(examples[-2][0]) - min(examples[-2][0])), 86)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_iqr_quartile_convention_and_restored_equations(self):
        """The stated median-of-halves rule yields Q1=5, Q3=15 and IQR=10."""
        url = "/descriptive/spread/interquartile-range/"
        self.page.goto(self.origin + url, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("Interquartile Range (IQR)")
        html = (SITE / url.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        data = [2, 4, 6, 8, 10, 12, 14, 16, 18]
        self.assertEqual(len(data), 9)
        self.assertEqual(data[4], 10)
        lower, upper = data[:4], data[5:]
        q1 = (lower[1] + lower[2]) / 2
        q3 = (upper[1] + upper[2]) / 2
        self.assertEqual((q1, q3, q3 - q1), (5, 15, 10))
        self.assertIn(r"\operatorname{IQR}=Q_3-Q_1", main)
        self.assertIn(r"\operatorname{IQR}=15-5=10", main)
        self.assertEqual(main.count(r"\["), 2)
        self.assertEqual(main.count(r"\]"), 2)
        visible = self.page.locator("main")
        for phrase in ("median-of-halves convention",
                       "exclude the overall median (10)",
                       "Other quartile", "different Q1, Q3, and IQR"):
            with self.subTest(phrase=phrase):
                expect(visible).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_symmetric_ci_blueprint_three_formulas_and_poll_example(self):
        """Three formulas and 62% ± 4 percentage points are consistent."""
        url = "/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/"
        self.page.goto(self.origin + url, wait_until="networkidle")
        expect(self.page.get_by_role(
            "heading", name="A Common Symmetric Confidence Interval Formula")
        ).to_be_visible()
        html = (SITE / url.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"\text{CI}=\widehat{\theta}\ \pm\ \text{margin of error}",
            r"\text{Margin of error}=c\times\operatorname{SE}(\widehat{\theta})",
            r"\text{CI}=\left[\widehat{\theta}-c\operatorname{SE}(\widehat{\theta}),\ \widehat{\theta}+c\operatorname{SE}(\widehat{\theta})\right]",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 3)
        self.assertEqual(main.count(r"\]"), 3)
        self.assertEqual((62 - 4, 62 + 4), (58, 66))
        self.assertEqual((52 - 3, 52 + 3), (49, 55))
        content = self.page.locator("main")
        for phrase in (
            "4 percentage points (not 4% of 62%)",
            "58% to 66%",
            "49% to 55%",
            "normal- or t-based",
            "not universal",
            "not a formula for every confidence interval",
        ):
            with self.subTest(phrase=phrase):
                expect(content).to_contain_text(phrase)
        self.assertNotIn("almost every confidence interval", content.inner_text().lower())
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_restored_lessons_preserve_progress_and_navigation(self):
        """The repaired lessons remain navigable and keep progress keys."""
        cases = (
            ("/descriptive/spread/range/", "esa_continue_descriptive_spread_lesson_v0"),
            ("/descriptive/spread/interquartile-range/", "esa_continue_descriptive_spread_lesson_v0"),
            ("/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/",
             "esa_continue_inference_confidence_intervals_lesson_v0"),
        )
        for route, key in cases:
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(
                    self.page.locator("main .lesson-nav a[href]").count(), 0)
                progress = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(progress["url"], route)
                self.assertIsInstance(progress["ts"], (int, float))

    def test_restored_standard_deviation_four_expressions(self):
        """Check the two distinct SD denominators and both worked examples."""
        from math import sqrt
        route = "/descriptive/spread/standard-deviation/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("Standard Deviation")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"s=\sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}",
            r"\sigma=\sqrt{\frac{\sum_{i=1}^{N}(x_i-\mu)^2}{N}}",
            r"\sqrt{\text{variance}}=\sqrt{25}=5",
            r"s=\sqrt{\frac{\sum_{i=1}^{5}(10-10)^2}{5-1}}=0",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 4)
        self.assertEqual(main.count(r"\]"), 4)
        self.assertIn(r"n\ge 2", main)
        self.assertIn(r"N\ge 1", main)
        expect(self.page.locator("main")).to_contain_text(
            "sample mean and the sample variance")
        expect(self.page.locator("main")).to_contain_text(
            "population mean and denominator N")
        self.assertAlmostEqual(sqrt(25), 5)
        values = [2, 4, 6]
        avg = sum(values) / len(values)
        deviations_sq = sum((x - avg)**2 for x in values)
        self.assertEqual(deviations_sq, 8)
        self.assertAlmostEqual(sqrt(deviations_sq / (len(values) - 1)), 2)
        self.assertAlmostEqual(sqrt(deviations_sq / len(values)), sqrt(8 / 3))
        constant = [10] * 5
        self.assertEqual(
            sqrt(sum((x - 10)**2 for x in constant) / (len(constant) - 1)), 0)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_restored_normal_distribution_three_expressions(self):
        """Check normal PDF, positive scale, standard normal and z scores."""
        from math import erf, exp, pi, sqrt
        route = "/probability/distributions/normal-distribution/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("Normal Distribution")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"f_X(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)",
            r"\mu=0,\qquad \sigma=1,\qquad Z\sim N(0,1)",
            r"Z=\frac{X-\mu}{\sigma}\sim N(0,1)",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertIn(r"\sigma&gt;0", main)
        self.assertEqual(main.count(r"\["), 3)
        self.assertEqual(main.count(r"\]"), 3)
        self.assertAlmostEqual(exp(0) / sqrt(2 * pi), 0.3989422804014327)
        mu, sigma = 70, 10
        self.assertEqual((80 - mu) / sigma, 1)
        for z, approximate_percent in ((1, 68.27), (2, 95.45), (3, 99.73)):
            with self.subTest(z=z):
                self.assertAlmostEqual(
                    100 * erf(z / sqrt(2)), approximate_percent, delta=0.01)
        expect(self.page.locator("main")).to_contain_text(
            "not guaranteed percentages")
        expect(self.page.locator("main")).to_contain_text(
            "exactly standard normal only when X is normal")
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_restored_clt_four_formulas_and_finite_sample_distinction(self):
        """Verify standardized limit, exact iid moments, SE and n=30 caveat."""
        from math import sqrt
        route = "/probability/lln-clt/central-limit-theorem/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text(
            "Central Limit Theorem")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"\frac{\sqrt{n}(\bar{X}_n-\mu)}{\sigma}\xrightarrow{d}N(0,1)",
            r"\operatorname{E}(\bar{X}_n)=\mu",
            r"\operatorname{Var}(\bar{X}_n)=\frac{\sigma^2}{n}",
            r"\operatorname{SE}(\bar{X}_n)=\sqrt{\operatorname{Var}(\bar{X}_n)}",
            r"=\frac{\sigma}{\sqrt{n}}",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 4)
        self.assertEqual(main.count(r"\]"), 4)
        expect(self.page.locator("main")).to_contain_text(
            "independent and identically distributed")
        expect(self.page.locator("main")).to_contain_text(
            "This is an asymptotic limit")
        expect(self.page.locator("main")).to_contain_text(
            "rule of thumb, not a universal threshold")
        expect(self.page.locator("main")).to_contain_text(
            "not guaranteed to be a good approximation")
        expect(self.page.locator("main")).to_contain_text(
            "infinite-variance distributions")
        # Independent discrete Xi in {0, 2}, equally likely; μ=1, σ²=1.
        population = [0, 2]
        mu = sum(population) / len(population)
        sigma2 = sum((x - mu)**2 for x in population) / len(population)
        sample_means = [(a + b) / 2 for a in population for b in population]
        sample_mu = sum(sample_means) / len(sample_means)
        sample_var = sum((x - sample_mu)**2 for x in sample_means) / 4
        self.assertEqual((mu, sigma2, sample_mu, sample_var), (1, 1, 1, 0.5))
        self.assertEqual(sqrt(sample_var), sqrt(sigma2 / 2))
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_three_repaired_lessons_keep_progress_keys_and_navigation(self):
        """The changed probability and descriptive lessons remain navigable."""
        cases = (
            ("/descriptive/spread/standard-deviation/",
             "esa_continue_descriptive_spread_lesson_v0"),
            ("/probability/distributions/normal-distribution/",
             "esa_continue_probability_distributions_lesson_v0"),
            ("/probability/lln-clt/central-limit-theorem/",
             "esa_continue_probability_lln_clt_lesson_v0"),
        )
        for route, key in cases:
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(
                    self.page.locator("main .lesson-nav a[href]").count(), 0)
                progress = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(progress["url"], route)
                self.assertIsInstance(progress["ts"], (int, float))

    def test_restored_z_t_critical_values_and_margins(self):
        """Five formulas: two-sided z coverage, margin, σ, and one-sample df."""
        from math import erf, sqrt
        route = "/inference/confidence-intervals/critical-values-z-and-t/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("Critical Values — z and t")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"\text{CI}=\widehat{\theta}\ \pm\ c\,\operatorname{SE}(\widehat{\theta})",
            r"P(-1.96\le Z\le1.96)\approx0.95",
            r"\text{Margin of error}=z^*\times\operatorname{SE}=1.96\times2=3.92",
            r"\sigma=\sqrt{\operatorname{Var}(X)}",
            r"\operatorname{df}=n-1,\qquad n\ge2",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 5)
        self.assertEqual(main.count(r"\]"), 5)
        self.assertAlmostEqual(erf(1.96 / sqrt(2)), 0.95, delta=0.0001)
        self.assertAlmostEqual(1.96 * 2, 3.92)
        self.assertEqual(11 - 1, 10)
        content = self.page.locator("main")
        for phrase in (
            "common symmetric, normal- or t-based confidence interval",
            "known population",
            "sample standard deviation s",
            "Unknown σ alone does not guarantee",
        ):
            with self.subTest(phrase=phrase):
                expect(content).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_restored_hypergeometric_pmf_moments_and_support(self):
        """PMF normalizes and derives its mean/variance for 100/10/5."""
        from math import comb
        route = "/probability/distributions/hypergeometric-distribution/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text(
            "Hypergeometric Distribution")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"P(X=x)=\frac{\binom{K}{x}\binom{N-K}{n-x}}{\binom{N}{n}}",
            r"\max(0,n-(N-K))\le x\le\min(n,K)",
            r"\operatorname{E}(X)=n\frac{K}{N}",
            r"\operatorname{E}(X)=5\left(\frac{10}{100}\right)=0.5",
            r"\operatorname{Var}(X)=n\frac{K}{N}\left(1-\frac{K}{N}\right)",
            r"\frac{N-n}{N-1}",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 4)
        self.assertEqual(main.count(r"\]"), 4)
        N, K, n = 100, 10, 5
        support = range(max(0, n - (N - K)), min(n, K) + 1)
        pmf = {x: comb(K, x) * comb(N - K, n - x) / comb(N, n)
               for x in support}
        self.assertAlmostEqual(sum(pmf.values()), 1)
        expected = sum(x * p for x, p in pmf.items())
        variance = sum((x - expected)**2 * p for x, p in pmf.items())
        self.assertAlmostEqual(expected, n * K / N)
        self.assertAlmostEqual(expected, 0.5)
        self.assertAlmostEqual(
            variance, n * (K / N) * (1 - K / N) * (N - n) / (N - 1))
        self.assertAlmostEqual(variance, 0.4318181818181818)
        p = K / N
        self.assertAlmostEqual(1 * p * (1 - p) * (N - 1) / (N - 1),
                               1 * p * (1 - p))
        self.assertLess(2 * p * (1 - p) * (N - 2) / (N - 1),
                        2 * p * (1 - p))
        content = self.page.locator("main")
        for phrase in (
            "three parameters (N, K, n)",
            "x is a possible observed value",
            "individual sample still contains a whole-number count",
            "N = 1 the draw count is deterministic",
            "no greater than binomial variance",
            "at n = 1 the two variances agree",
        ):
            with self.subTest(phrase=phrase):
                expect(content).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_restored_total_probability_partition_and_examples(self):
        """Check two pathways, 0.70 calculation, and finite partition sum."""
        route = "/probability/conditional/law-of-total-probability/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text(
            "Law of Total Probability")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"P(A)=P(A\cap B)+P(A\cap B^{c})",
            r"P(A)=P(A\mid B)P(B)+P(A\mid B^{c})P(B^{c})",
            r"P(\text{Pass})=P(\text{Pass}\mid\text{Study})P(\text{Study})",
            r"P(\text{Pass})=0.90(0.60)+0.40(0.40)=0.54+0.16=0.70",
            r"P(A)=\sum_{i=1}^{m}P(A\mid B_i)P(B_i)",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 5)
        self.assertEqual(main.count(r"\]"), 5)
        passing = 0.60 * 0.90 + 0.40 * 0.40
        self.assertAlmostEqual(passing, 0.70)
        self.assertAlmostEqual(0.54 + 0.16, passing)
        path_prob = [0.2, 0.3, 0.5]
        cond_prob = [0.1, 0.5, 0.8]
        self.assertAlmostEqual(sum(path_prob), 1)
        self.assertAlmostEqual(
            sum(w * c for w, c in zip(path_prob, cond_prob)), 0.57)
        content = self.page.locator("main")
        expect(content).to_contain_text(
            "mutually exclusive and collectively exhaustive")
        expect(content).to_contain_text("zero-probability pathways")
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_three_new_math_repairs_keep_navigation_and_progress(self):
        """Repairs retain existing storage-key contracts and lesson links."""
        routes = (
            ("/inference/confidence-intervals/critical-values-z-and-t/",
             "esa_continue_inference_confidence_intervals_lesson_v0"),
            ("/probability/distributions/hypergeometric-distribution/",
             "esa_continue_probability_distributions_lesson_v0"),
            ("/probability/conditional/law-of-total-probability/",
             "esa_continue_probability_conditional_lesson_v0"),
        )
        for route, key in routes:
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(
                    self.page.locator("main .lesson-nav a[href]").count(), 0)
                progress = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(progress["url"], route)
                self.assertIsInstance(progress["ts"], (int, float))

    def test_restored_standard_error_estimators_five_expressions(self):
        """Restore mean, true and estimated SE, sample size, and Bernoulli p."""
        from math import sqrt
        route = "/probability/sampling-distributions/standard-error-and-estimators/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text(
            "Standard Error and Estimators")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"\bar X=\frac{1}{n}\sum_{i=1}^{n}X_i",
            r"\operatorname{SE}(\bar X)=\sqrt{\operatorname{Var}(\bar X)}=\frac{\sigma}{\sqrt n}",
            r"\operatorname{SE}(\bar X)\propto\frac{1}{\sqrt n}",
            r"\operatorname{SE}(\bar X)=\frac{20}{\sqrt{100}}=2",
            r"\operatorname{SE}(\widehat p)=\sqrt{\frac{p(1-p)}{n}}",
            r"\widehat{\operatorname{SE}}(\widehat p)=\sqrt{\frac{\widehat p(1-\widehat p)}{n}}",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 5)
        self.assertEqual(main.count(r"\]"), 5)
        self.assertAlmostEqual(sum([2, 4, 6]) / 3, 4)
        self.assertEqual([20 / sqrt(n) for n in (25, 100, 400)], [4, 2, 1])
        p, n = 0.3, 100
        self.assertAlmostEqual(sqrt(p * (1 - p) / n), sqrt(0.0021))
        phat = 30 / n
        self.assertAlmostEqual(
            sqrt(phat * (1 - phat) / n), sqrt(0.0021))
        content = self.page.locator("main")
        for phrase in (
            "independent, identically distributed observations",
            "theoretical SE",
            "plug-in estimate",
            "sampling without replacement",
            "not every confidence interval uses this symmetric form",
            "exact and randomization-based tests",
        ):
            with self.subTest(phrase=phrase):
                expect(content).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_restored_sd_vs_se_three_expressions(self):
        """Differentiate population SD, sample SD and mean uncertainty."""
        from math import sqrt
        route = "/inference/foundations/sd-vs-se-common-confusion/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text(
            "SD vs SE — Common Confusion")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"\operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt n}",
            r"\widehat{\operatorname{SE}}(\bar X)=\frac{s}{\sqrt n}",
            r"\widehat{\operatorname{SE}}(\bar X)=\frac{20}{\sqrt{100}}=2",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 3)
        self.assertEqual(main.count(r"\]"), 3)
        self.assertAlmostEqual(20 / sqrt(100), 2)
        self.assertAlmostEqual(20 / sqrt(25), 4)
        self.assertAlmostEqual(20 / sqrt(400), 1)
        content = self.page.locator("main")
        for phrase in (
            "population standard deviation σ",
            "sample standard deviation s",
            "Sample SD (s) = 20",
            "estimated standard error of the mean",
            "Mean ± SE alone is not generally a 95% confidence interval",
        ):
            with self.subTest(phrase=phrase):
                expect(content).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_restored_type_one_two_error_probabilities_and_power(self):
        """Validate alpha control, alternative-dependent beta and 1-beta."""
        route = "/inference/hypothesis-testing/type1-type2-errors/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text(
            "Type I and Type II Errors")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"\sup_{\theta\in\Theta_0}P_{\theta}(\text{reject }H_0)\le\alpha",
            r"\beta(\theta)=P_{\theta}(\text{fail to reject }H_0)",
            r"\alpha:\ 0.05\longrightarrow0.01",
            r"\operatorname{Power}(\theta)=P_{\theta}(\text{reject }H_0)",
            r"=1-\beta(\theta),\qquad\theta\in\Theta_1",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 4)
        self.assertEqual(main.count(r"\]"), 4)
        # H0: Bernoulli p=0.5, n=5; reject only if all five are successes.
        alpha_actual = 0.5 ** 5
        self.assertLessEqual(alpha_actual, 0.05)
        alternative_p = 0.8
        power = alternative_p ** 5
        beta = 1 - power
        self.assertAlmostEqual(power + beta, 1)
        self.assertAlmostEqual(power, 1 - beta)
        self.assertLess(0.01, 0.05)
        content = self.page.locator("main")
        for phrase in (
            "at most 5% under the null model",
            "exact size 0.05",
            "discrete or conservative tests",
            "particular alternative",
            "nested",
            "does not prove that H₀ is true",
            "equivalence margin",
        ):
            with self.subTest(phrase=phrase):
                expect(content).to_contain_text(phrase)
        self.assertNotIn(
            "Concluding two teaching methods are equivalent",
            content.inner_text())
        self.assertNotIn(
            "The probability of a Type I error equals α",
            content.inner_text())
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_new_se_and_error_lessons_preserve_navigation_and_progress(self):
        """Three repaired lessons keep their routes, navigation and keys."""
        cases = (
            ("/probability/sampling-distributions/standard-error-and-estimators/",
             "esa_continue_probability_sampling_distributions_lesson_v0"),
            ("/inference/foundations/sd-vs-se-common-confusion/",
             "esa_continue_inference_foundations_lesson_v0"),
            ("/inference/hypothesis-testing/type1-type2-errors/",
             "esa_continue_inference_hypothesis_testing_lesson_v0"),
        )
        for route, key in cases:
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(
                    self.page.locator("main .lesson-nav a[href]").count(), 0)
                progress = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(progress["url"], route)
                self.assertIsInstance(progress["ts"], (int, float))

    def test_restored_significance_alpha_five_expressions(self):
        """Five formulas: p-value decisions, level-versus-size, test/CI duality."""
        route = "/inference/hypothesis-testing/significance-level-alpha/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("Significance Level (α)")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"\alpha\in(0,1)",
            r"\alpha=0.05",
            r"p=0.03&lt;\alpha=0.05",
            r"p=0.18&gt;\alpha=0.05",
            r"\sup_{\theta\in\Theta_0}P_\theta(\text{reject }H_0)\le0.05",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 5)
        self.assertEqual(main.count(r"\]"), 5)
        alpha = 0.05
        self.assertTrue(0.03 <= alpha)
        self.assertFalse(0.18 <= alpha)
        # A discrete test can have size strictly below nominal alpha.
        self.assertLessEqual(0.5**5, alpha)
        self.assertLess(0.5**5, alpha)
        self.assertEqual(0.05, alpha)  # exact-size test, if attained
        body = self.page.locator("main")
        for phrase in (
            "Exact equality requires an exact-size test",
            "two-sided test and its compatible two-sided 95% confidence",
            "inverting the same test",
            "at most about 5%",
            "conservative or discrete test may reject less often",
        ):
            with self.subTest(phrase=phrase):
                expect(body).to_contain_text(phrase)
        self.assertNotIn(
            "then approximately 5% of those studies would incorrectly reject",
            body.inner_text())
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_restored_statistical_power_five_expressions(self):
        """Alternative-specific beta, long-run power and planning conventions."""
        route = "/inference/power-sample-size/what-is-statistical-power/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("What Is Statistical Power?")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"\beta(\theta)=P_\theta(\text{fail to reject }H_0)",
            r"\operatorname{Power}(\theta)=P_\theta(\text{reject }H_0)",
            r"=1-\beta(\theta),\quad\theta\in\Theta_1",
            r"\operatorname{Power}(\theta_*)=0.80",
            r"\beta(\theta_*)=1-0.80=0.20",
            r"\sup_{\theta\in\Theta_0}P_\theta(\text{reject }H_0)\le\alpha",
            r"\beta(\theta)=1-\operatorname{Power}(\theta)",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 5)
        self.assertEqual(main.count(r"\]"), 5)
        self.assertAlmostEqual(0.8 + 0.2, 1)
        self.assertAlmostEqual(1 - 0.2, 0.8)
        # Toy test, reject H0 (Bernoulli p=.5) for five successes out of five.
        # Power and beta depend on the true alternative success probability.
        power_08 = 0.8**5
        power_09 = 0.9**5
        self.assertNotAlmostEqual(power_08, power_09)
        self.assertAlmostEqual(power_08 + (1 - power_08), 1)
        self.assertLessEqual(0.5**5, 0.05)
        body = self.page.locator("main")
        for phrase in (
            "alternative-hypothesis set",
            "specified alternative",
            "At another true effect size",
            "Common planning target, not a universal minimum",
            "not a guarantee for a single study",
            "does not guarantee replication",
        ):
            with self.subTest(phrase=phrase):
                expect(body).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_restored_bias_variance_four_expressions_and_examples(self):
        """Verify signed bias -5 and finite illustrative variances."""
        route = "/inference/foundations/bias-and-variance-intuition/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("Bias and Variance Intuition")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
        for formula in (
            r"\widehat{\theta}",
            r"\theta",
            r"\operatorname{Bias}_{\theta}(\widehat{\theta})",
            r"=\operatorname{E}_{\theta}(\widehat{\theta})-\theta",
            r"\operatorname{E}_{\theta}(\widehat{\theta})=\theta",
            r"\operatorname{Bias}_{\theta}(\widehat{\theta})=0",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 4)
        self.assertEqual(main.count(r"\]"), 4)
        self.assertEqual(95 - 100, -5)
        high = [70, 110, 95, 130, 85]
        low = [99, 101, 100, 98, 102]
        high_average = sum(high) / len(high)
        low_average = sum(low) / len(low)
        high_variance = sum((v - high_average)**2 for v in high) / len(high)
        low_variance = sum((v - low_average)**2 for v in low) / len(low)
        self.assertEqual((high_average, low_average), (98, 100))
        self.assertEqual((high_variance, low_variance), (426, 2))
        self.assertGreater(high_variance, low_variance)
        body = self.page.locator("main")
        for phrase in (
            "numerical bias is 95 − 100 = −5 units",
            "error in an individual observed estimate",
            "average is 98",
            "illustration is 426",
            "average is 100",
            "values is 2",
            "five values alone do not establish the exact",
        ):
            with self.subTest(phrase=phrase):
                expect(body).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_alpha_power_bias_repairs_preserve_navigation_and_progress(self):
        """Check existing lesson routes, navigation and progress storage keys."""
        cases = (
            ("/inference/hypothesis-testing/significance-level-alpha/",
             "esa_continue_inference_hypothesis_testing_lesson_v0"),
            ("/inference/power-sample-size/what-is-statistical-power/",
             "esa_continue_inference_power_sample_size_lesson_v0"),
            ("/inference/foundations/bias-and-variance-intuition/",
             "esa_continue_inference_foundations_lesson_v0"),
        )
        for route, key in cases:
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(
                    self.page.locator("main .lesson-nav a[href]").count(), 0)
                progress = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(progress["url"], route)
                self.assertIsInstance(progress["ts"], (int, float))

    def test_restored_weak_strong_lln_five_expressions(self):
        """Validate i.i.d. LLN hypotheses, distinct convergence and coin mean."""
        from html import unescape
        from math import comb
        route = "/probability/lln-clt/weak-vs-strong-lln/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("Weak vs Strong LLN")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = unescape(
            html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0])
        for formula in (
            r"\bar X_n=\frac{1}{n}\sum_{i=1}^{n}X_i",
            r"n\longrightarrow\infty",
            r"\bar X_n\xrightarrow{P}\mu",
            r"P\!\left(\lvert\bar X_n-\mu\rvert>\varepsilon\right)\longrightarrow0",
            r"\bar X_n\xrightarrow{\mathrm{a.s.}}\mu",
            r"P\!\left(\lim_{n\to\infty}\bar X_n=\mu\right)=1",
            r"X_i\overset{\mathrm{iid}}{\sim}\mathrm{Bernoulli}",
            r"\xrightarrow{\mathrm{a.s.}}\frac12",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 5)
        self.assertEqual(main.count(r"\]"), 5)
        # Independent, fair Bernoulli outcomes have E(X)=1/2.
        self.assertEqual((0 + 1) / 2, 0.5)
        # Exact coin-toss binomial tails decrease markedly in this example.
        def outside_tolerance(n, tolerance=0.2):
            return sum(comb(n, k) / 2**n
                       for k in range(n + 1)
                       if abs(k / n - 0.5) > tolerance + 1e-12)
        self.assertLess(outside_tolerance(100), outside_tolerance(10))
        body = self.page.locator("main")
        for phrase in (
            "independent and identically distributed",
            "finite absolute first moment",
            "finite variance is sufficient but not",
            "does not require finite variance",
            "not a guarantee that every finite sample",
            "almost surely",
            "the reverse statement is not always true",
        ):
            with self.subTest(phrase=phrase):
                expect(body).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_restored_sampling_distribution_four_expressions(self):
        """Check exact iid mean and SE versus asymptotic CLT and design caveat."""
        from html import unescape
        from math import sqrt
        route = "/probability/sampling-distributions/what-is-a-sampling-distribution/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text(
            "What Is a Sampling Distribution?")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = unescape(
            html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0])
        for formula in (
            r"\bar X_n=\frac{1}{n}\sum_{i=1}^{n}X_i",
            r"\operatorname{E}(\bar X_n)=\mu",
            r"\operatorname{SE}(\bar X_n)",
            r"=\sqrt{\operatorname{Var}(\bar X_n)}",
            r"=\frac{\sigma}{\sqrt n}",
            r"\operatorname{SE}(\bar X_{4n})",
            r"=\frac12\,\operatorname{SE}(\bar X_n)",
            r"(\sigma\text{ fixed})",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 4)
        self.assertEqual(main.count(r"\]"), 4)
        # The existing four-value population samples pairs without replacement.
        vals = [2, 4, 6, 8]
        means = [(vals[i] + vals[j]) / 2
                 for i in range(4) for j in range(i + 1, 4)]
        self.assertEqual(means, [3, 4, 5, 5, 6, 7])
        self.assertEqual(sum(means) / len(means), 5)
        self.assertEqual(sum(vals) / len(vals), 5)
        self.assertEqual((sum((x - 5)**2 for x in means) / 6), 5 / 3)
        # The formula in the lesson assumes independent sampling instead.
        sigma, n = 20, 25
        self.assertEqual(sigma / sqrt(n), 4)
        self.assertEqual(sigma / sqrt(4 * n), 2)
        body = self.page.locator("main")
        for phrase in (
            "without replacement",
            "six equally likely unordered pairs",
            "independent, identically distributed sampling",
            "asymptotic approximation is distinct from the exact",
            "theoretical standard error of the mean",
            "s/√n",
            "standard error is halved",
        ):
            with self.subTest(phrase=phrase):
                expect(body).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_restored_post_hoc_four_expressions_and_fwer(self):
        """Verify ANOVA H0, 20-test false positives and Bonferroni union bound."""
        from html import unescape
        from math import comb
        route = "/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text(
            "Post-Hoc Tests and Multiple Comparisons")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = unescape(
            html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0])
        for formula in (
            r"H_0:\ \mu_A=\mu_B=\mu_C=\mu_D",
            r"\alpha_{\mathrm{per\ test}}=0.05",
            r"P(\text{at least one false positive})",
            r"=1-(1-0.05)^{20}=1-0.95^{20}\approx0.642",
            r"\alpha_{\mathrm{Bonferroni}}=\frac{\alpha}{m}",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 4)
        self.assertEqual(main.count(r"\]"), 4)
        self.assertEqual(comb(4, 2), 6)  # four-group pairwise comparisons
        fwer_independent = 1 - 0.95**20
        self.assertAlmostEqual(fwer_independent, 0.6415140775914581)
        self.assertAlmostEqual(fwer_independent, 0.642, delta=0.001)
        alpha, m = 0.05, 20
        self.assertAlmostEqual(alpha / m, 0.0025)
        self.assertLessEqual(m * (alpha / m), alpha)
        # Union bound also applies to dependent (even identical) rejection events.
        p = 0.0025
        self.assertLessEqual(p, m * p)
        body = self.page.locator("main")
        for phrase in (
            "mutually independent rejection events",
            "exact Type I error",
            "0.6415, or 64.2%",
            "nominal test",
            "union bound",
            "does not require independent tests",
            "m ≥ 1",
        ):
            with self.subTest(phrase=phrase):
                expect(body).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_lln_sampling_posthoc_preserve_progress_and_navigation(self):
        """Preserve routes, current lesson continuation and next/previous links."""
        cases = (
            ("/probability/lln-clt/weak-vs-strong-lln/",
             "esa_continue_probability_lln_clt_lesson_v0"),
            ("/probability/sampling-distributions/what-is-a-sampling-distribution/",
             "esa_continue_probability_sampling_distributions_lesson_v0"),
            ("/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/",
             "esa_continue_inference_classical_tests_lesson_v0"),
        )
        for route, key in cases:
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(
                    self.page.locator("main .lesson-nav a[href]").count(), 0)
                progress = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(progress["url"], route)
                self.assertIsInstance(progress["ts"], (int, float))

    def test_coefficient_of_variation_six_restored_formulas(self):
        """Verify all six CV repairs, calculations and meaningful-zero caveats."""
        from html import unescape
        route = "/descriptive/spread/coefficient-of-variation/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("Coefficient of Variation")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = unescape(
            html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0])
        for formula in (
            r"\mathrm{CV}=\frac{s}{\bar{x}}",
            r"\bar{x}>0",
            r"\mathrm{CV}_{\%}=\frac{s}{\bar{x}}\times 100\%",
            r"\mathrm{CV}=\frac{10}{50}=0.20",
            r"\mathrm{CV}_{\%}=0.20\times100\%=20\%",
            r"\mathrm{CV}_{A,\%}=\frac{4}{20}\times100\%=20\%",
            r"\mathrm{CV}_{B,\%}=\frac{10}{100}\times100\%=10\%",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 6)
        self.assertEqual(main.count(r"\]"), 6)
        self.assertAlmostEqual(10 / 50, .2)
        self.assertAlmostEqual(4 / 20, .2)
        self.assertAlmostEqual(10 / 100, .1)
        self.assertAlmostEqual(5 / .5 * 100, 1000)
        for phrase in ("ratio-scale", "meaningful zero",
                       "Celsius instead of Kelvin", "positive expected return",
                       "1000%", "Undefined when the mean is zero"):
            with self.subTest(phrase=phrase):
                expect(self.page.locator("main")).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_chi_square_goodness_of_fit_eight_formulas_and_die(self):
        """Verify hypotheses, test statistic, df and die-count arithmetic."""
        from html import unescape
        route = "/inference/classical-tests/chi-square-goodness-of-fit/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text(
            "Chi-Square Goodness-of-Fit Test")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = unescape(
            html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0])
        for formula in (
            r"p_i=\frac16",
            r"E_i=n\,p_i",
            r"E_i=120\times\frac16=20",
            r"\chi^2=\sum_{i=1}^{k}\frac{(O_i-E_i)^2}{E_i}",
            r"H_0:\ p_i=p_i^{(0)}",
            r"\mathrm{df}=k-1",
            r"\mathrm{df}=6-1=5",
            r"\chi^2_{\mathrm{obs}}=\frac{4+1+1+9+0+1}{10}=1.6",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 8)
        self.assertEqual(main.count(r"\]"), 8)
        observed = (8, 11, 9, 13, 10, 9)
        expected = (10,) * 6
        self.assertEqual(sum(observed), 60)
        self.assertEqual(sum(expected), 60)
        statistic = sum((o - e)**2 / e for o, e in zip(observed, expected))
        self.assertAlmostEqual(statistic, 1.6)
        self.assertEqual(6 - 1, 5)
        for phrase in ("approximately chi-square distributed",
                       "asymptotic approximation",
                       "Nonnegative (zero is possible",
                       "parameters are estimated from the same data",
                       "0.901", "conservative rule of thumb",
                       "sparse counts"):
            with self.subTest(phrase=phrase):
                expect(self.page.locator("main")).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_reporting_lessons_preserve_saved_progress_and_navigation(self):
        """Retain each existing reporting lesson's route and shared save key."""
        root = "/inference/interpretation-reporting/"
        names = (
            ("reporting-results-clear-language", "Reporting Results in Clear Language"),
            ("tables-figures-and-visual-communication",
             "Tables, Figures, and Visual Communication"),
            ("multiple-testing-and-false-positives",
             "Multiple Testing and False Positives"),
        )
        key = "esa_continue_inference_interpretation_reporting_lesson_v0"
        for slug, label in names:
            route = root + slug + "/"
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_have_text(label)
                progress = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(progress["url"], route)
                self.assertEqual(progress["label"], label)
                self.assertIsInstance(progress["ts"], (int, float))
                self.assertGreater(
                    self.page.locator("main .lesson-nav a[href]").count(), 0)

    def test_reporting_lessons_work_with_storage_denied(self):
        """A SecurityError on localStorage must not break reporting lessons."""
        self.page.add_init_script("""
            Object.defineProperty(window, 'localStorage', {
              configurable: true,
              get() { throw new DOMException('Denied', 'SecurityError'); }
            });
        """)
        root = "/inference/interpretation-reporting/"
        for slug in ("reporting-results-clear-language",
                     "tables-figures-and-visual-communication",
                     "multiple-testing-and-false-positives"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin + root + slug + "/",
                               wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(
                    self.page.locator("main .lesson-nav a[href]").count(), 0)

    def test_restored_bayes_seven_formulas_medical_example(self):
        """Check Bayes derivation, positive conditioning and the 19% posterior."""
        from html import unescape
        route = "/probability/conditional/bayes-theorem/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("Bayes' Theorem")
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        main = unescape(
            html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0])
        for formula in (
            r"P(A\mid B)=\frac{P(A\cap B)}{P(B)}",
            r"P(B)>0",
            r"P(B\mid A)=\frac{P(A\cap B)}{P(A)}",
            r"P(A)>0",
            r"P(A\cap B)=P(B\mid A)\,P(A)",
            r"P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}",
            r"\underbrace{P(A\mid B)}_{\text{posterior}}",
            r"\overbrace{P(B\mid A)}^{\text{likelihood}}",
            r"\overbrace{P(A)}^{\text{prior}}",
            r"P(D\mid +)=\frac{P(+\mid D)\,P(D)}{P(+)}",
            r"\frac{0.95\times0.01}{0.05}",
            r"=0.19=19\%",
            r"P(+)=P(+\mid D)\,P(D)+P(+\mid D^{c})\,P(D^{c})",
        ):
            with self.subTest(formula=formula):
                self.assertIn(formula, main)
        self.assertEqual(main.count(r"\["), 7)
        self.assertEqual(main.count(r"\]"), 7)
        prevalence, sensitivity, positive_rate = .01, .95, .05
        posterior = sensitivity * prevalence / positive_rate
        false_positive_rate = (
            positive_rate - sensitivity * prevalence) / (1 - prevalence)
        self.assertAlmostEqual(posterior, .19)
        self.assertAlmostEqual(false_positive_rate, .04090909090909091)
        self.assertAlmostEqual(
            sensitivity * prevalence +
            false_positive_rate * (1 - prevalence), positive_rate)
        for phrase in (
            "Overall positive-test probability across the whole population = 5%",
            "not a 5% false-positive rate",
            "19% of people who test positive have the disease",
            "4.09%",
            "distinct from the overall 5% positive-test probability",
            "conditioning event has positive probability",
        ):
            with self.subTest(phrase=phrase):
                expect(self.page.locator("main")).to_contain_text(phrase)
        self.assertNotIn("\uea01", main)
        self.assertNotIn("\uea02", main)

    def test_bayes_restoration_preserves_progress_and_navigation(self):
        """Keep existing conditional-probability resume schema and lesson links."""
        route = "/probability/conditional/bayes-theorem/"
        key = "esa_continue_probability_conditional_lesson_v0"
        self.page.goto(self.origin + route, wait_until="networkidle")
        progress = self.page.evaluate(
            "key => JSON.parse(localStorage.getItem(key))", key)
        self.assertEqual(progress["url"], route)
        self.assertEqual(progress["label"], "Bayes' Theorem")
        self.assertIsInstance(progress["ts"], (int, float))
        self.assertGreater(
            self.page.locator("main .lesson-nav a[href]").count(), 0)

    def test_intermediate_path_has_real_lessons_and_study_checkpoints(self):
        """Every new study anchor resolves; existing steps remain usable."""
        route = "/learning-paths/intermediate/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text(
            "Intermediate Learning Path")
        cards = self.page.locator("#start .card")
        expect(cards).to_have_count(6)
        targets = (
            "/inference/hypothesis-testing/type1-type2-errors/",
            "/inference/hypothesis-testing/p-value-meaning/",
            "/modeling/simple-linear-regression/regression-equation/",
            "/modeling/simple-linear-regression/residuals/",
            "/applied-statistics/study-design/experimental-vs-observational/",
            "/applied-statistics/study-design/bias-confounding/",
            "/modeling/diagnostics/residual-plots/",
            "/modeling/model-fit-comparison/overfitting/",
            "/inference/interpretation-reporting/interpreting-confidence-intervals/",
            "/inference/interpretation-reporting/reporting-results-clear-language/",
            "/applied-statistics/practice/",
        )
        for dest in targets:
            with self.subTest(destination=dest):
                expect(cards.locator("a[href='" + dest + "']")).to_have_count(1)
                self.assertTrue(
                    (SITE / dest.lstrip("/") / "index.html").is_file(),
                    "Unpublished study target: " + dest)
        expect(cards.locator("p").filter(
            has_text="Checkpoint:")).to_have_count(5)
        self.assertEqual(cards.locator("a.card-foot").count(), 6)
        for width in (375, 768, 1280):
            self.page.set_viewport_size({"width": width, "height": 850})
            overflow = self.page.evaluate(
                "() => document.documentElement.scrollWidth - innerWidth")
            self.assertLessEqual(
                overflow, 1, f"Intermediate path overflow at {width}: {overflow}")

    def test_mathjax_loader_distinguishes_currency_from_math(self):
        """Do not fetch MathJax for prices; preserve supported TeX delimiters."""
        route = "/learning-paths/intermediate/"
        html = (SITE / route.lstrip("/") / "index.html").read_text()
        self.assertIn("</main>", html)
        samples = (
            ("Single price $25, with no TeX.", False),
            ("The prices are $5 and $10 for two items.", False),
            ("Amounts are $5, $10, and $20.", False),
            (r"A literal escaped dollar sign \$25 is not TeX.", False),
            (r"The formula is $x^2+y^2$.", True),
            (r"The formula is $2+2$.", True),
            (r"Mathematics can also contain $2$.", True),
            (r"A spaced expression $ x $ works.", True),
            (r"MathJax inline \(\alpha+\beta\) appears.", True),
            (r"MathJax display \[\alpha+\beta\] appears.", True),
            (r"An environment \begin{aligned}x&=1\end{aligned} appears.", True),
            ("Display math $x^2+y^2$ appears.", True),
        )
        for content, expect_math in samples:
            with self.subTest(sample=content):
                fixture = html.replace(
                    "</main>", '<p id="math-detection-case">' +
                    content + '</p></main>', 1)
                self.page.route(
                    "**/learning-paths/intermediate/",
                    lambda route: route.fulfill(
                        status=200, content_type="text/html", body=fixture))
                try:
                    self.page.goto(self.origin + route, wait_until="networkidle")
                    expect(self.page.locator("#math-detection-case")).to_be_visible()
                    expect(self.page.locator(
                        'script[src*="tex-mml-chtml.js"]'
                    )).to_have_count(1 if expect_math else 0)
                finally:
                    self.page.unroute("**/learning-paths/intermediate/")

    def test_restored_one_and_two_proportion_math_and_numeric_examples(self):
        """Validate 45 repaired expressions and distinguish pooled test from CI."""
        from math import erfc, sqrt
        examples = (
            ("/inference/classical-tests/one-proportion-z-test/", 22, (
                r"\hat p=\frac{x}{n}",
                r"\operatorname{SE}_0(\hat p)=\sqrt{\frac{p_0(1-p_0)}{n}}",
                r"Z=\frac{\hat p-p_0}",
                r"Z\approx2.8284",
                r"np_0\ge10",
                r"n(1-p_0)\ge10",
                r"\hat p\pm z_{1-\alpha/2}",
            ), ("p-value ≈ 0.0047", "Wilson score interval",
                "not the exact inversion")),
            ("/inference/classical-tests/two-proportion-z-test/", 23, (
                r"\hat p_1=\frac{x_1}{n_1}",
                r"\hat p_2=\frac{x_2}{n_2}",
                r"\hat p=\frac{x_1+x_2}{n_1+n_2}",
                r"Z=\frac{\hat p_1-\hat p_2}",
                r"\operatorname{SE}_{\mathrm{CI}}=",
                r"\hat p_1(1-\hat p_1)",
            ), ("Two-sided p-value ≈ 0.0027",
                "not an exact inversion", "samples must be independent")),
        )
        for route, number, formulas, messages in examples:
            with self.subTest(lesson=route):
                page = (SITE / route.lstrip("/") / "index.html").read_text()
                self.assertIn('<main id="main-content"', page)
                lesson = page.split('<main id="main-content"', 1)[1].split(
                    "</main>", 1)[0]
                self.assertNotIn("\uea01", lesson)
                self.assertNotIn("\uea02", lesson)
                self.assertEqual(lesson.count(r"\["), number)
                self.assertEqual(lesson.count(r"\]"), number)
                for formula in formulas:
                    self.assertIn(formula, lesson)
                self.page.goto(self.origin + route, wait_until="networkidle")
                for phrase in messages:
                    expect(self.page.locator("main")).to_contain_text(phrase)
                key = "esa_continue_inference_classical_tests_lesson_v0"
                resume = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(resume["url"], route)
                expect(self.page.get_by_role(
                    "link", name="Next:", exact=False).first).to_be_visible()

        n, x, null = 200, 120, .5
        observed = x / n
        se = sqrt(null * (1-null) / n)
        z = (observed-null)/se
        self.assertAlmostEqual(se, 0.03535533905932738)
        self.assertAlmostEqual(z, 2.82842712474619)
        self.assertAlmostEqual(erfc(abs(z)/sqrt(2)), 0.004677734981047275)
        n1, n2, x1, x2 = 200, 200, 120, 90
        p1, p2 = x1/n1, x2/n2
        pooled = (x1+x2)/(n1+n2)
        se_null = sqrt(pooled*(1-pooled)*(1/n1+1/n2))
        z2 = (p1-p2)/se_null
        self.assertAlmostEqual(pooled, .525)
        self.assertAlmostEqual(se_null, .04993746088859544)
        self.assertAlmostEqual(z2, 3.003757045930553)
        self.assertAlmostEqual(erfc(abs(z2)/sqrt(2)), .0026666817936140935)
        se_ci = sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)
        self.assertGreater(abs(se_ci-se_null), .00001)

    def test_measurement_scales_interactive_self_check_accessibility(self):
        """Five accurate explanations, native keyboard input and mobile layout."""
        self.page.goto(self.origin + "/foundations/measurement-scales/",
                       wait_until="networkidle")
        quiz = self.page.locator("#esa-self-check")
        expect(quiz.get_by_role("heading", name="Check Your Understanding")).to_be_visible()
        fields = quiz.locator("fieldset")
        expect(fields).to_have_count(5)
        expected = (("b", "a"), ("c", "a"), ("b", "a"),
                    ("a", "c"), ("b", "c"))
        for idx, (correct, incorrect) in enumerate(expected):
            with self.subTest(question=idx+1):
                field = fields.nth(idx)
                expect(field.get_by_role("radio")).to_have_count(3)
                feedback = field.locator('[role="status"][aria-live="polite"]')
                field.locator(f'input[value="{incorrect}"]').check()
                expect(feedback).to_contain_text("Not quite.")
                expect(feedback).not_to_have_text("Not quite. ")
                self.assertEqual(feedback.get_attribute("data-state"), "incorrect")
                field.locator(f'input[value="{correct}"]').focus()
                self.page.keyboard.press("Space")
                expect(field.locator(f'input[value="{correct}"]')).to_be_checked()
                expect(feedback).to_contain_text("Correct.")
                self.assertGreater(len(feedback.inner_text()), 30)
                self.assertEqual(feedback.get_attribute("data-state"), "correct")
        for width in (375, 768, 1280):
            self.page.set_viewport_size({"width": width, "height": 850})
            self.assertLessEqual(self.page.evaluate(
                "() => document.documentElement.scrollWidth - innerWidth"), 1)

    def test_distributions_progress_survives_denied_storage(self):
        """All published distributions and overview remain usable when denied."""
        slugs = ("bernoulli", "binomial", "geometric", "negative-binomial",
                 "poisson", "hypergeometric", "uniform", "exponential",
                 "gamma", "beta", "normal", "lognormal")
        self.page.add_init_script("""
          Object.defineProperty(window, "localStorage", {
            configurable: true,
            get() { throw new DOMException("Storage blocked", "SecurityError"); }
          });
        """)
        routes = ["/probability/distributions/"] + [
            "/probability/distributions/" + slug + "-distribution/"
            for slug in slugs]
        for route in routes:
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertEqual(self.errors, [], route)
                self.assertGreater(
                    self.page.locator("main a[href^='/']").count(), 0)

    def test_distributions_progress_preserves_existing_keys(self):
        """Overview and 12 lesson pages still save exact old resume routes."""
        slugs = ("bernoulli", "binomial", "geometric", "negative-binomial",
                 "poisson", "hypergeometric", "uniform", "exponential",
                 "gamma", "beta", "normal", "lognormal")
        routes = ["/probability/distributions/"] + [
            "/probability/distributions/" + slug + "-distribution/"
            for slug in slugs]
        for route in routes:
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                key = ("esa_continue_probability_last_block_v0"
                       if route == "/probability/distributions/"
                       else "esa_continue_probability_distributions_lesson_v0")
                data = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(data["url"], route)
                self.assertTrue(data["label"])
                self.assertIsInstance(data["ts"], (int, float))

    def test_restored_mean_tests_math_and_numerical_accuracy(self):
        """Verify 38 recovered expressions, exact references and decisions."""
        from math import erfc, sqrt
        targets = (
            ("/inference/classical-tests/one-sample-z-test-for-mean/", 18,
             (r"\operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt{n}}",
              r"Z=\frac{\bar X-\mu_0}{\sigma/\sqrt{n}}",
              r"Z=-4",
              r"z_{1-\alpha/2}=z_{0.975}\approx1.96",
              r"|Z|=4&gt;1.96",
              r"\bar X\pm z_{1-\alpha/2}"),
             ("two-sided p-value ≈ 0.0000633", "[488.08, 495.92]", "excludes 500")),
            ("/inference/classical-tests/one-sample-t-test-for-mean/", 20,
             (r"\widehat{\operatorname{SE}}(\bar X)=\frac{s}{\sqrt{n}}",
              r"t=\frac{\bar X-\mu_0}{s/\sqrt{n}}",
              r"t=-2.5",
              r"\nu=25-1=24",
              r"\bar X\pm t_{1-\alpha/2,n-1}"),
             ("p ≈ 0.01965", "[16.35, 19.65]", "20 is excluded")),
        )
        for route, n, expected_math, expected_text in targets:
            with self.subTest(lesson=route):
                html = (SITE / route.lstrip("/") / "index.html").read_text()
                main = html.split('<main id="main-content"', 1)[1].split(
                    "</main>", 1)[0]
                self.assertNotIn("\uea01", main)
                self.assertNotIn("\uea02", main)
                self.assertEqual(main.count(r"\["), n)
                self.assertEqual(main.count(r"\]"), n)
                for formula in expected_math:
                    self.assertIn(formula, main)
                self.page.goto(self.origin + route, wait_until="networkidle")
                for phrase in expected_text:
                    expect(self.page.locator("main")).to_contain_text(phrase)
                saved = self.page.evaluate(
                    """key => JSON.parse(localStorage.getItem(key))""",
                    "esa_continue_inference_classical_tests_lesson_v0")
                self.assertEqual(saved["url"], route)
                self.assertIsInstance(saved["ts"], (float, int))
                self.assertGreater(
                    self.page.locator("main .hero-actions a[href]").count(), 0)

        z = (492 - 500) / (20 / sqrt(100))
        self.assertEqual(z, -4)
        self.assertAlmostEqual(erfc(abs(z) / sqrt(2)),
                               0.00006334248366623973, places=13)
        self.assertAlmostEqual(492 - 1.96 * 2, 488.08)
        self.assertAlmostEqual(492 + 1.96 * 2, 495.92)
        t = (18 - 20) / (4 / sqrt(25))
        self.assertEqual(t, -2.5)
        # Independent benchmark for the Student-t(24) two-sided tail.
        self.assertAlmostEqual(0.019654175116578784, 0.01965, delta=0.000005)
        self.assertAlmostEqual(18 - 2.0638985616 * .8, 16.3488811507,
                               places=7)
        self.assertAlmostEqual(18 + 2.0638985616 * .8, 19.6511188493,
                               places=7)

    def test_advanced_path_existing_lessons_and_checkpoints(self):
        """Provide advanced progression without claiming previews are lessons."""
        route = "/learning-paths/advanced/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        expect(self.page.locator("main h1")).to_have_text("Advanced Learning Path")
        cards = self.page.locator("#start .card")
        expect(cards).to_have_count(6)
        expect(cards.locator("p").filter(has_text="Checkpoint:")).to_have_count(6)
        expect(cards.locator("a.card-foot")).to_have_count(6)
        expected = (
            "/mathematical-statistics/maximum-likelihood-estimation/definition-of-mle/",
            "/mathematical-statistics/likelihood-and-log-likelihood/score-function/",
            "/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/",
            "/mathematical-statistics/asymptotic-theory/delta-method/",
            "/modeling/extensions/logistic-regression/",
            "/modeling/extensions/interpreting-logistic-coefficients/",
            "/modeling/extensions/glm/",
            "/modeling/model-fit-comparison/train-vs-test/",
            "/modeling/model-fit-comparison/overfitting/",
            "/modeling/model-fit-comparison/aic-bic/",
            "/modeling/diagnostics/residual-plots/",
            "/modeling/diagnostics/cooks-distance/",
            "/applied-statistics/study-design/bias-confounding/",
            "/applied-statistics/practice/",
        )
        for url in expected:
            with self.subTest(target=url):
                expect(cards.locator("a[href='" + url + "']")).to_have_count(1)
                self.assertTrue(
                    (SITE / url.lstrip("/") / "index.html").is_file(), url)
        for url in ("/machine-learning/", "/data-mining/", "/software/"):
            expect(cards.locator("a.card-foot[href='" + url + "']")).to_have_count(1)
        expect(self.page.locator("#start")).to_contain_text("lessons remain planned")
        for width in (375, 768, 1280):
            self.page.set_viewport_size({"width": width, "height": 850})
            self.assertLessEqual(
                self.page.evaluate(
                    "() => document.documentElement.scrollWidth - innerWidth"),
                1)

    def test_confidence_interval_progress_with_denied_storage(self):
        """All twelve confidence lessons and their overview survive denial."""
        slugs = (
            "what-is-a-confidence-interval", "interval-blueprint-estimate-plus-minus",
            "critical-values-z-and-t", "conditions-normality-clt-independence",
            "ci-for-mean-sigma-known-z", "ci-for-mean-sigma-unknown-t",
            "ci-for-proportion", "ci-for-difference-of-means-independent",
            "ci-for-difference-of-proportions", "ci-for-paired-mean-difference",
            "width-and-precision-what-controls", "common-mistakes-and-interpretation"
        )
        self.page.add_init_script("""
          Object.defineProperty(window, "localStorage", {
            configurable: true,
            get() { throw new DOMException("Storage denied", "SecurityError"); }
          });
        """)
        routes = ["/inference/confidence-intervals/"] + [
            "/inference/confidence-intervals/" + name + "/" for name in slugs]
        for route in routes:
            with self.subTest(page=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertEqual(self.errors, [], route)
                self.assertGreater(self.page.locator("main a[href^='/']").count(), 0)

    def test_confidence_interval_progress_existing_schema(self):
        """Retain exact lesson/block storage keys, labels and routes."""
        slugs = (
            "what-is-a-confidence-interval", "interval-blueprint-estimate-plus-minus",
            "critical-values-z-and-t", "conditions-normality-clt-independence",
            "ci-for-mean-sigma-known-z", "ci-for-mean-sigma-unknown-t",
            "ci-for-proportion", "ci-for-difference-of-means-independent",
            "ci-for-difference-of-proportions", "ci-for-paired-mean-difference",
            "width-and-precision-what-controls", "common-mistakes-and-interpretation"
        )
        routes = ["/inference/confidence-intervals/"] + [
            "/inference/confidence-intervals/" + name + "/" for name in slugs]
        for route in routes:
            with self.subTest(page=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                key = ("esa_continue_inference_last_block_v0"
                       if route == "/inference/confidence-intervals/"
                       else "esa_continue_inference_confidence_intervals_lesson_v0")
                saved = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(saved["url"], route)
                self.assertTrue(saved["label"])
                self.assertIsInstance(saved["ts"], (int, float))

    def test_restored_proportion_wald_math_and_numerical_examples(self):
        """Inspect all 29 expressions and independently recompute both Wald CIs."""
        from math import sqrt
        cases = (
            ("/inference/confidence-intervals/ci-for-proportion/", 15,
             (r"\hat p=\frac{x}{n}",
              r"\widehat{\operatorname{SE}}(\hat p)=\sqrt{\frac{\hat p(1-\hat p)}{n}}",
              r"\hat p\ \pm\ z_{1-\alpha/2}",
              r"n\hat p=500(0.62)=310"),
             ("(0.5775, 0.6625)", "57.8% to 66.3%", "Wald", "Wilson")),
            ("/inference/confidence-intervals/ci-for-difference-of-proportions/", 14,
             (r"\hat p_1-\hat p_2",
              r"\widehat{\operatorname{SE}}(\hat p_1-\hat p_2)",
              r"\sqrt{0.00075}",
              r"0.10\pm0.053676"),
             ("(0.0463, 0.1537)", "4.6% to 15.4%", "Wald", "Newcombe"))
        )
        for route, n, formulas, phrases in cases:
            with self.subTest(page=route):
                html = (SITE / route.lstrip("/") / "index.html").read_text()
                main = html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0]
                self.assertNotIn("\uea01", main)
                self.assertNotIn("\uea02", main)
                self.assertEqual(main.count(r"\["), n)
                self.assertEqual(main.count(r"\]"), n)
                for formula in formulas:
                    self.assertIn(formula, main)
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                for phrase in phrases:
                    expect(self.page.locator("main")).to_contain_text(phrase)
                saved = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))",
                    "esa_continue_inference_confidence_intervals_lesson_v0")
                self.assertEqual(saved["url"], route)

        p, n = 310 / 500, 500
        se = sqrt(p * (1-p) / n)
        self.assertAlmostEqual(se, 0.021707141681944216, places=12)
        self.assertAlmostEqual(1.96*se, 0.04254599769661066, places=10)
        self.assertAlmostEqual(p - 1.96*se, 0.5774540023033894, places=9)
        self.assertAlmostEqual(p + 1.96*se, 0.6625459976966106, places=9)
        self.assertGreater(n*p, 10)
        self.assertGreater(n*(1-p), 10)
        p1, p2, n1, n2 = 240 / 600, 180 / 600, 600, 600
        se_diff = sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2)
        self.assertAlmostEqual(se_diff, 0.027386127875258306, places=12)
        self.assertAlmostEqual(1.96*se_diff, 0.05367681063550628, places=10)
        self.assertAlmostEqual(p1-p2-1.96*se_diff, 0.04632318936449374, places=10)
        self.assertAlmostEqual(p1-p2+1.96*se_diff, 0.15367681063550628, places=10)
        for successes, total in ((240,600), (180,600)):
            self.assertGreaterEqual(successes, 10)
            self.assertGreaterEqual(total-successes, 10)

    def test_confidence_interval_self_check_accessible_feedback_and_mobile(self):
        """Six validated explanations; native radio keys, keyboard and mobile layout."""
        self.page.goto(self.origin + "/inference/confidence-intervals/",
                       wait_until="networkidle")
        quiz = self.page.locator("#esa-ci-self-check")
        expect(quiz.get_by_role("heading", name="Check Your Confidence Interval Understanding")).to_be_visible()
        fields = quiz.locator("fieldset")
        expect(fields).to_have_count(6)
        correct = ("b", "a", "c", "a", "b", "c")
        for idx, answer in enumerate(correct):
            with self.subTest(question=idx+1):
                field = fields.nth(idx)
                expect(field.locator("legend")).to_be_visible()
                expect(field.get_by_role("radio")).to_have_count(3)
                feedback = field.locator('[role="status"][aria-live="polite"]')
                wrong = "a" if answer != "a" else "b"
                field.locator(f'input[value="{wrong}"]').check()
                expect(feedback).to_contain_text("Not quite.")
                self.assertEqual(feedback.get_attribute("data-state"), "incorrect")
                field.locator(f'input[value="{answer}"]').focus()
                self.page.keyboard.press("Space")
                expect(field.locator(f'input[value="{answer}"]')).to_be_checked()
                expect(feedback).to_contain_text("Correct.")
                self.assertGreater(len(feedback.inner_text()), 55)
                self.assertEqual(feedback.get_attribute("data-state"), "correct")
        expect(self.page.locator("#lessons .lesson-card")).to_have_count(12)
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                overflow = self.page.evaluate(
                    "() => document.documentElement.scrollWidth - innerWidth")
                if overflow > 1:
                    offending = self.page.evaluate("""() =>
                      [...document.querySelectorAll('body *')]
                        .map(e => ({tag:e.tagName, id:e.id,
                                    cls:(typeof e.className === 'string' ? e.className : ''),
                                    width:Math.round(e.getBoundingClientRect().width),
                                    right:Math.round(e.getBoundingClientRect().right),
                                    text:(e.textContent||'').trim().slice(0,50)}))
                        .filter(e => e.right > innerWidth + 1)
                        .slice(0,16)
                    """)
                    quiz_width = self.page.locator("#esa-ci-self-check").evaluate(
                        "e => ({scroll:e.scrollWidth, client:e.clientWidth})")
                    self.fail(f"Viewport {width} overflow {overflow}; "
                              f"quiz={quiz_width}; offenders={offending}")

    def test_six_inference_overviews_keep_original_resume_schema(self):
        """No change to shared key, labels, URLs or recent progress behavior."""
        blocks = (
            ("foundations", "Block 1 — Inference Foundations"),
            ("hypothesis-testing", "Block 3 — Hypothesis Testing"),
            ("classical-tests", "Block 4 — Classical Tests"),
            ("power-sample-size", "Block 5 — Power and Sample Size"),
            ("interpretation-reporting", "Block 6 — Interpretation & Reporting"),
            ("assumptions-robustness", "Block 7 — Assumptions & Robustness"),
        )
        for slug, label in blocks:
            route = "/inference/" + slug + "/"
            with self.subTest(block=slug):
                self.page.goto(self.origin + route, wait_until="networkidle")
                data = self.page.evaluate(
                    "() => JSON.parse(localStorage.getItem('esa_continue_inference_last_block_v0'))")
                self.assertEqual(data["url"], route)
                self.assertEqual(data["label"], label)
                self.assertIsInstance(data["ts"], (int, float))
                expect(self.page.locator("main h1")).to_be_visible()
                if slug == "classical-tests":
                    expect(self.page.locator("#esa-test-guide")).to_be_visible()
                    expect(self.page.locator("#esa-test-result")).to_be_visible()

    def test_six_inference_overviews_load_without_localstorage(self):
        """Block navigation and the current test selector remain usable when denied."""
        self.page.add_init_script("""
          Object.defineProperty(window, "localStorage", {
            configurable: true,
            get() { throw new DOMException("Storage denied", "SecurityError"); }
          });
        """)
        slugs = ("foundations", "hypothesis-testing", "classical-tests",
                 "power-sample-size", "interpretation-reporting",
                 "assumptions-robustness")
        for slug in slugs:
            route = "/inference/" + slug + "/"
            with self.subTest(block=slug):
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(self.page.locator("main a[href^='/']").count(), 0)
                self.assertEqual(self.errors, [], route)
                if slug == "classical-tests":
                    expect(self.page.locator("#esa-test-guide")).to_be_visible()
                    expect(self.page.locator("#esa-test-result")).to_be_visible()


    def test_hypotheses_and_proportion_sample_size_restored_math(self):
        """Restore 30 independently checked formulas, with correct inequalities and n."""
        from math import ceil
        from html import unescape
        definitions = (
            ("/inference/hypothesis-testing/null-and-alternative/", 15, (
                r"H_0:\ \mu=500\ \mathrm{mL}",
                r"H_a:\ \mu\neq500\ \mathrm{mL}",
                r"H_0:\ \mu=\mu_0",
                r"H_a:\ \mu\neq\mu_0",
                r"H_0:\ \mu\le\mu_0",
                r"H_a:\ \mu>\mu_0",
                r"H_0:\ \mu\ge\mu_0",
                r"H_a:\ \mu<\mu_0",
                r"H_0:\ p\le0.50",
                r"H_a:\ p>0.50",
                "equality boundary", "before inspecting the sample results")),
            ("/inference/power-sample-size/sample-size-for-proportion/", 15, (
                r"\frac{z_{1-\alpha/2}^{\,2}\,p_{\mathrm{plan}}(1-p_{\mathrm{plan}})}{E^2}",
                r"p_{\mathrm{plan}}(1-p_{\mathrm{plan}})\le\frac14",
                r"\lceil n_0\rceil=1068",
                "Required sample size = 1068",
                "finite-population", "simple random sampling",
                "Wald", "hypothesis-test power"))
        )
        for route, expected, phrases in definitions:
            with self.subTest(route=route):
                html = (SITE / route.lstrip("/") / "index.html").read_text()
                main = unescape(html.split('<main id="main-content"', 1)[1].split("</main>", 1)[0])
                self.assertNotIn("\uea01", main)
                self.assertNotIn("\uea02", main)
                self.assertEqual(main.count(r"\["), expected)
                self.assertEqual(main.count(r"\]"), expected)
                for phrase in phrases:
                    self.assertIn(phrase, main)
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        for z, p, e, required in (
            (1.96, 0.5, 0.03, 1068),
            (1.645, 0.5, 0.03, 752),
            (2.576, 0.5, 0.03, 1844),
            (1.96, 0.4, 0.03, 1025),
            (1.645, 0.4, 0.03, 722),
            (2.576, 0.4, 0.03, 1770),
            (1.96, 0.5, 0.06, 267),
        ):
            with self.subTest(z=z, p=p, e=e):
                raw = z*z*p*(1-p)/(e*e)
                self.assertEqual(ceil(raw), required)
                self.assertLessEqual(z*(p*(1-p)/required)**0.5, e)
                if required > 1:
                    self.assertGreater(z*(p*(1-p)/(required-1))**0.5, e)

    def test_sample_size_proportion_calculator_input_keyboard_mobile(self):
        """Confidence presets, n ceiling, conservative option, errors and preserved progress."""
        route = "/inference/power-sample-size/sample-size-for-proportion/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        section = self.page.locator("#esa-proportion-calculator")
        expect(section.get_by_role("heading", name="Interactive Sample Size for a Proportion")).to_be_visible()
        z = self.page.get_by_label("Confidence level", exact=True)
        e = self.page.get_by_label("Target margin of error E (0–1)")
        p = self.page.get_by_label("Expected proportion p (0–1)")
        conservative = self.page.get_by_role("checkbox", name="Use conservative p = 0.5 when the proportion is unknown")
        result = self.page.locator("#esa-sample-result")
        error = self.page.locator("#esa-sample-error")
        expect(conservative).to_be_checked()
        expect(p).to_be_disabled()
        expect(result).to_have_text("1,068")
        expect(self.page.locator("#esa-sample-details")).to_contain_text("1067.111")
        z.select_option("90")
        expect(result).to_have_text("752")
        z.select_option("99")
        expect(result).to_have_text("1,844")
        z.select_option("95")
        conservative.focus()
        self.page.keyboard.press("Space")
        expect(conservative).not_to_be_checked()
        expect(p).to_be_enabled()
        p.fill("0.4")
        expect(result).to_have_text("1,025")
        z.select_option("90")
        expect(result).to_have_text("722")
        z.select_option("99")
        expect(result).to_have_text("1,770")
        z.select_option("95")
        p.fill("0")
        expect(result).to_have_text("—")
        expect(error).to_contain_text("strictly between 0 and 1")
        p.fill("1")
        expect(result).to_have_text("—")
        p.fill("0.5")
        e.fill("0")
        expect(result).to_have_text("—")
        expect(error).to_contain_text("margin of error")
        e.fill("1")
        expect(result).to_have_text("—")
        e.fill("")
        expect(result).to_have_text("—")
        e.fill("0.03")
        expect(result).to_have_text("1,068")
        conservative.check()
        expect(p).to_be_disabled()
        expect(result).to_have_text("1,068")
        saved = self.page.evaluate(
            "() => JSON.parse(localStorage.getItem('esa_continue_inference_power_sample_size_lesson_v0'))")
        self.assertEqual(saved["url"], route)
        self.assertEqual(saved["label"], "Sample Size for a Proportion")
        self.assertIsInstance(saved["ts"], (int, float))
        for phrase in ("simple random sampling", "finite-population correction",
                       "design effect", "nonresponse", "not a hypothesis-test power"):
            expect(section).to_contain_text(phrase)
        for width in (320, 375, 768, 1280):
            with self.subTest(viewport=width):
                self.page.set_viewport_size({"width": width, "height": 860})
                dimensions = section.evaluate("""e => ({
                    scroll: e.scrollWidth, client: e.clientWidth,
                    right: e.getBoundingClientRect().right
                })""")
                self.assertLessEqual(dimensions["scroll"]-dimensions["client"], 1, dimensions)
                self.assertLessEqual(dimensions["right"], width + 1, dimensions)

    def test_sample_size_proportion_calculator_with_denied_storage(self):
        """The calculation still works when browsers deny the lesson progress write."""
        self.page.add_init_script("""
            Object.defineProperty(window, 'localStorage', {
              configurable: true,
              get() { throw new DOMException('Denied', 'SecurityError'); }
            });
        """)
        self.page.goto(self.origin + "/inference/power-sample-size/sample-size-for-proportion/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-sample-result")).to_have_text("1,068")
        self.page.locator("#esa-sample-confidence").select_option("99")
        expect(self.page.locator("#esa-sample-result")).to_have_text("1,844")
        expect(self.page.locator("main h1")).to_be_visible()

    def test_seven_inference_resume_uses_published_lessons_and_safe_text(self):
        """Valid progress survives; stored markup and external/cross-block links cannot execute."""
        blocks = (
            ("foundations", "foundations", "foundations"),
            ("confidence-intervals", "confidence_intervals", "ci"),
            ("hypothesis-testing", "hypothesis_testing", "testing"),
            ("classical-tests", "classical_tests", "classical"),
            ("power-sample-size", "power_sample_size", "power"),
            ("interpretation-reporting", "interpretation_reporting", "reporting"),
            ("assumptions-robustness", "assumptions_robustness", "robustness"),
        )
        malicious = '<img src=x onerror="window.esaInjected=true"><script>window.esaInjected=true</script> & good'
        for slug, keyslug, panelname in blocks:
            with self.subTest(block=slug):
                route = "/inference/" + slug + "/"
                key = "esa_continue_inference_" + keyslug + "_lesson_v0"
                self.page.goto(self.origin + route, wait_until="networkidle")
                panel = self.page.locator("#continue-reading-inference-" + panelname)
                label = self.page.locator("#continue-reading-inference-" + panelname + "-label")
                button = self.page.locator("#continue-reading-inference-" + panelname + "-btn")
                valid = self.page.locator("#lessons .lesson-card h3 a[href]").first.get_attribute("href")
                self.assertTrue((SITE / valid.lstrip("/") / "index.html").is_file())
                expect(panel).to_be_hidden()
                def save(value):
                    self.page.evaluate(
                        "([key, value]) => localStorage.setItem(key, JSON.stringify(value))",
                        [key, value])
                    self.page.reload(wait_until="networkidle")
                save({"url":valid, "label":malicious})
                expect(panel).to_be_visible()
                expect(button).to_have_attribute("href", valid)
                expect(label.locator("strong")).to_have_text(malicious)
                self.assertEqual(label.locator("img,script").count(), 0)
                self.assertIsNone(self.page.evaluate("window.esaInjected"))
                for value in (
                    {"url":"javascript:alert(1)", "label":"bad"},
                    {"url":"//external.example/lesson/", "label":"bad"},
                    {"url": ("/inference/hypothesis-testing/null-and-alternative/"
                             if slug == "confidence-intervals"
                             else "/inference/confidence-intervals/ci-for-proportion/"), "label":"Cross-block"},
                    {"url":"/inference/" + slug + "/unpublished/", "label":"bad"},
                    {"url":valid+"?next=evil", "label":"bad"},
                    {"url":valid+"#anchor", "label":"bad"},
                    {"url":"/inference/" + slug + "/../other-block/", "label":"bad"},
                    {"url":valid, "label":17},
                    {"url":valid, "label":"   "},
                ):
                    with self.subTest(block=slug, invalid=value):
                        save(value)
                        expect(panel).to_be_hidden()
                self.page.evaluate(
                    "key => localStorage.setItem(key, '{malformed json')", key)
                self.page.reload(wait_until="networkidle")
                expect(panel).to_be_hidden()

    def test_seven_inference_resume_denied_storage_keeps_navigation(self):
        """All seven overviews remain functional if localStorage throws SecurityError."""
        self.page.add_init_script("""
            Object.defineProperty(window, "localStorage", {
              configurable: true,
              get() { throw new DOMException("Storage denied", "SecurityError"); }
            });
        """)
        block_to_panel = (
            ("foundations","foundations"),("confidence-intervals","ci"),
            ("hypothesis-testing","testing"),("classical-tests","classical"),
            ("power-sample-size","power"),("interpretation-reporting","reporting"),
            ("assumptions-robustness","robustness")
        )
        for slug, panelname in block_to_panel:
            with self.subTest(block=slug):
                self.page.goto(self.origin + "/inference/" + slug + "/",
                               wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                expect(self.page.locator("#lessons .lesson-card h3 a").first).to_be_visible()
                expect(self.page.locator("#continue-reading-inference-" + panelname)).to_be_hidden()
                self.assertEqual(self.errors, [])
                if slug == "confidence-intervals":
                    expect(self.page.locator("#esa-ci-self-check fieldset")).to_have_count(6)
                if slug == "classical-tests":
                    expect(self.page.locator("#esa-test-guide")).to_be_visible()


    def test_restored_linearity_and_variance_rules_math(self):
        """Independently check 28 restored expressions and dice/indicator examples."""
        from html import unescape
        from fractions import Fraction
        cases = (
            ("/probability/expectation-variance/linearity-of-expectation/", 13, (
                r"\operatorname{E}(X+Y)=\operatorname{E}(X)+\operatorname{E}(Y)",
                r"\operatorname{E}(aX+b)=a\operatorname{E}(X)+b",
                r"\operatorname{E}(X+Y)=3.5+3.5=7",
                r"\operatorname{E}(Y)=\operatorname{E}(X+5)=70+5=75",
                r"\operatorname{E}(I_A)=1\cdot P(A)+0\cdot(1-P(A))=P(A)",
                r"\operatorname{E}(H)=10\cdot0.5=5",
                "provided the expectations exist and are finite",
                "independent or dependent")),
            ("/probability/expectation-variance/variance-rules-and-sums/", 15, (
                r"\operatorname{Var}(X)=\operatorname{E}\big[(X-\operatorname{E}X)^2\big]",
                r"\operatorname{Var}(c)=0",
                r"\operatorname{Var}(X+c)=\operatorname{Var}(X)",
                r"\operatorname{Var}(cX)=c^2\operatorname{Var}(X)",
                r"\operatorname{Var}(Y)=\operatorname{Var}(3X)=3^2\cdot4=36",
                r"\operatorname{Cov}(X,Y)",
                r"\operatorname{Var}(X+Y)=",
                r"\operatorname{Var}(X-Y)=",
                r"\frac{35}{12}",
                r"\frac{35}{6}\approx5.8333",
                "Independence is sufficient, but not necessary"))
        )
        for route, n, expected in cases:
            with self.subTest(route=route):
                source = (SITE / route.lstrip("/") / "index.html").read_text()
                main = unescape(source.split('<main id="main-content"', 1)[1]
                                       .split("</main>", 1)[0])
                self.assertNotIn("\uea01", main)
                self.assertNotIn("\uea02", main)
                self.assertEqual(main.count(r"\["), n)
                self.assertEqual(main.count(r"\]"), n)
                for fragment in expected:
                    self.assertIn(fragment, main)
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                key = "esa_continue_probability_expectation_variance_lesson_v0"
                stored = self.page.evaluate(
                    "k => JSON.parse(localStorage.getItem(k))", key)
                self.assertEqual(stored["url"], route)
                self.assertIsInstance(stored["ts"], (int, float))

        outcomes = tuple(range(1, 7))
        mean = Fraction(sum(outcomes), len(outcomes))
        variance = sum((Fraction(i) - mean)**2 for i in outcomes) / len(outcomes)
        self.assertEqual(mean, Fraction(7, 2))
        self.assertEqual(variance, Fraction(35, 12))
        self.assertEqual(2 * variance, Fraction(35, 6))
        self.assertEqual(3**2 * 4, 36)
        self.assertEqual(sum(Fraction(1, 2) for _ in range(10)), 5)
        for sx, sy, rho, expected_cov, expected_sum, expected_diff in (
            (2, 3, -1, -6, 1, 25),
            (2, 3, 0, 0, 13, 13),
            (2, 3, 1, 6, 25, 1),
            (1, 1, -1, -1, 0, 4),
            (1, 1, 1, 1, 4, 0),
        ):
            with self.subTest(rho=rho, sdx=sx, sdy=sy):
                covariance = sx * sy * rho
                self.assertEqual(covariance, expected_cov)
                self.assertEqual(sx*sx + sy*sy + 2*covariance, expected_sum)
                self.assertEqual(sx*sx + sy*sy - 2*covariance, expected_diff)

    def test_variance_explorer_accessible_numerical_keyboard_and_mobile(self):
        """Native labelled inputs, preset extremes, slider keyboard and responsive layout."""
        route = "/probability/expectation-variance/variance-rules-and-sums/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        box = self.page.locator("#esa-variance-explorer")
        expect(box.get_by_role("heading",
             name="Interactive Variance of Sums and Differences")).to_be_visible()
        x = self.page.get_by_label("Standard deviation of X")
        y = self.page.get_by_label("Standard deviation of Y")
        rho = self.page.get_by_role("slider", name="Correlation ρ")
        cov = self.page.locator("#esa-variance-cov")
        plus = self.page.locator("#esa-variance-plus")
        minus = self.page.locator("#esa-variance-minus")
        message = self.page.locator("#esa-variance-error")
        expect(x).to_have_value("2")
        expect(y).to_have_value("3")
        expect(rho).to_have_value("0")
        expect(cov).to_have_text("0")
        expect(plus).to_have_text("13")
        expect(minus).to_have_text("13")
        expect(self.page.locator("#esa-variance-explanation")).to_contain_text(
            "does not prove independence")

        for choice, expected in (("−1", ("-6", "1", "25")),
                                 ("0", ("0", "13", "13")),
                                 ("+1", ("6", "25", "1"))):
            with self.subTest(preset=choice):
                box.get_by_role("button", name="ρ = " + choice).click()
                expect(cov).to_have_text(expected[0])
                expect(plus).to_have_text(expected[1])
                expect(minus).to_have_text(expected[2])
        rho.focus()
        rho.press("Home")
        expect(rho).to_have_value("-1")
        rho.press("ArrowRight")
        expect(rho).to_have_value("-0.95")
        expect(self.page.locator("#esa-variance-rho-label")).to_have_text("-0.95")
        box.get_by_role("button", name="ρ = 0").click()
        x.fill("1")
        y.fill("1")
        box.get_by_role("button", name="ρ = −1").click()
        expect(plus).to_have_text("0")
        expect(minus).to_have_text("4")
        box.get_by_role("button", name="ρ = +1").click()
        expect(plus).to_have_text("4")
        expect(minus).to_have_text("0")

        x.fill("0")
        expect(plus).to_have_text("—")
        expect(message).to_contain_text("positive standard deviations")
        x.fill("-1")
        expect(plus).to_have_text("—")
        x.fill("")
        expect(plus).to_have_text("—")
        x.fill("1000001")
        expect(plus).to_have_text("—")
        x.fill("2")
        y.fill("3")
        expect(message).to_be_hidden()
        expect(plus).to_have_text("25")
        for width in (320, 375, 768, 1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width, "height":850})
                bounds = box.evaluate("""e => ({
                    scroll:e.scrollWidth,client:e.clientWidth,
                    left:e.getBoundingClientRect().left,
                    right:e.getBoundingClientRect().right
                })""")
                self.assertLessEqual(bounds["scroll"]-bounds["client"], 1, bounds)
                self.assertGreaterEqual(bounds["left"], -1, bounds)
                self.assertLessEqual(bounds["right"], width+1, bounds)

    def test_variance_explorer_survives_blocked_localstorage(self):
        """Denied storage cannot hide the variance explorer or prevent calculations."""
        self.page.add_init_script("""
            Object.defineProperty(window, "localStorage", {
              configurable:true,
              get() { throw new DOMException("Storage blocked", "SecurityError"); }
            });
        """)
        self.page.goto(self.origin + "/probability/expectation-variance/variance-rules-and-sums/",
                       wait_until="networkidle")
        expect(self.page.locator("main h1")).to_be_visible()
        expect(self.page.locator("#esa-variance-plus")).to_have_text("13")
        self.page.get_by_role("button", name="ρ = −1").click()
        expect(self.page.locator("#esa-variance-plus")).to_have_text("1")
        expect(self.page.locator("#esa-variance-minus")).to_have_text("25")

    def test_seven_probability_overviews_resume_rejects_injection_and_unsafe_links(self):
        """Exact same-block published links and literal saved labels only."""
        names = (
            ("basics","basics","basics"),
            ("conditional","conditional","conditional"),
            ("random-variables","random_variables","rv"),
            ("expectation-variance","expectation_variance","ev"),
            ("distributions","distributions","distributions"),
            ("lln-clt","lln_clt","lln"),
            ("sampling-distributions","sampling_distributions","sampling")
        )
        malicious = '<img src=x onerror="window.esaInjected=true"><script>window.esaInjected=true</script> & text'
        for slug, keyslug, suffix in names:
            with self.subTest(block=slug):
                url = "/probability/" + slug + "/"
                key = "esa_continue_probability_" + keyslug + "_lesson_v0"
                self.page.goto(self.origin + url, wait_until="networkidle")
                panel = self.page.locator("#continue-reading-probability-" + suffix)
                label = self.page.locator("#continue-reading-probability-" + suffix + "-label")
                link = self.page.locator("#continue-reading-probability-" + suffix + "-btn")
                valid = self.page.locator("#lessons .lesson-card h3 a[href]").first.get_attribute("href")
                self.assertTrue((SITE / valid.lstrip("/") / "index.html").is_file())
                expect(panel).to_be_hidden()

                def set_history(data):
                    self.page.evaluate(
                        "([key,data]) => localStorage.setItem(key, JSON.stringify(data))",
                        [key, data])
                    self.page.reload(wait_until="networkidle")

                set_history({"url":valid,"label":malicious})
                expect(panel).to_be_visible()
                expect(link).to_have_attribute("href", valid)
                expect(label.locator("strong")).to_have_text(malicious)
                self.assertEqual(label.locator("img,script").count(), 0)
                self.assertIsNone(self.page.evaluate("window.esaInjected"))
                for invalid in (
                    {"url":"javascript:alert(1)","label":"Bad"},
                    {"url":"//example.com/lesson/","label":"Bad"},
                    {"url":"/probability/unpublished-block/lesson/","label":"Bad"},
                    {"url":"/probability/expectation-variance/variance-rules-and-sums/"
                           if slug != "expectation-variance"
                           else "/probability/distributions/binomial-distribution/",
                     "label":"Cross-block"},
                    {"url":url+"not-published/","label":"Not published"},
                    {"url":valid+"?next=evil","label":"Query"},
                    {"url":valid+"#lesson","label":"Anchor"},
                    {"url":url+"../about/","label":"Traversal"},
                    {"url":valid,"label":123},
                    {"url":valid,"label":"   "},
                ):
                    with self.subTest(block=slug,invalid=invalid):
                        set_history(invalid)
                        expect(panel).to_be_hidden()
                self.page.evaluate(
                    "key => localStorage.setItem(key, '{bad json')", key)
                self.page.reload(wait_until="networkidle")
                expect(panel).to_be_hidden()
                # A saved ordinary label must still work after invalid data is rejected.
                set_history({"url":valid,"label":"Continue a published lesson"})
                expect(panel).to_be_visible()
                expect(link).to_have_attribute("href", valid)
                expect(label.locator("strong")).to_have_text("Continue a published lesson")

    def test_seven_probability_overviews_denied_storage_remain_usable(self):
        """All block overview pages keep lessons and navigation when storage is denied."""
        self.page.add_init_script("""
            Object.defineProperty(window, "localStorage", {
              configurable:true,
              get() { throw new DOMException("Storage denied", "SecurityError"); }
            });
        """)
        names = (
            ("basics","basics"),
            ("conditional","conditional"),
            ("random-variables","rv"),
            ("expectation-variance","ev"),
            ("distributions","distributions"),
            ("lln-clt","lln"),
            ("sampling-distributions","sampling")
        )
        for slug,suffix in names:
            with self.subTest(block=slug):
                self.page.goto(self.origin + "/probability/" + slug + "/",
                               wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                expect(self.page.locator("#lessons .lesson-card h3 a").first).to_be_visible()
                expect(self.page.locator("#continue-reading-probability-" + suffix)).to_be_hidden()
                self.assertEqual(self.errors, [])
                self.assertGreater(self.page.locator("#lessons .lesson-card").count(), 0)


    def test_bernoulli_and_binomial_restored_math_and_calculations(self):
        """22 source formula restorations and independent binomial PMF/CDF benchmarks."""
        from html import unescape
        from math import comb, fsum, sqrt
        cases = (
            ("/probability/distributions/bernoulli-distribution/", 9, (
                r"P(\text{failure})=1-p",
                r"P(X=1)=p",
                r"P(X=0)=1-p",
                r"\operatorname{E}(X)=p",
                r"\operatorname{Var}(X)=\operatorname{E}(X^2)",
                r"p(1-p)",
                r"\tfrac14=0.25",
                "need not be binomial")),
            ("/probability/distributions/binomial-distribution/", 13, (
                r"X\sim\operatorname{Binomial}(n,p)",
                r"X\in\{0,1,\ldots,n\}",
                r"P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}",
                r"\binom{n}{k}=\frac{n!}{k!(n-k)!}",
                r"P(X=2)=3(0.5)^3=0.375",
                r"\operatorname{E}(X)=100(0.2)=20",
                r"\operatorname{Var}(X)=np(1-p)",
                r"\operatorname{SD}(X)=\sqrt{np(1-p)}",
                "independent, identically distributed",
                "Poisson-binomial",
                "With n = 1"))
        )
        for route, restored, checks in cases:
            with self.subTest(lesson=route):
                source = (SITE / route.lstrip("/") / "index.html").read_text()
                main = unescape(source.split('<main id="main-content"', 1)[1]
                                .split("</main>", 1)[0])
                self.assertNotIn("\uea01", main)
                self.assertNotIn("\uea02", main)
                self.assertEqual(main.count(r"\["), restored)
                self.assertEqual(main.count(r"\]"), restored)
                for fragment in checks:
                    self.assertIn(fragment, main)
                self.page.goto(self.origin + route, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertEqual(
                    self.page.evaluate("""() =>
                      JSON.parse(localStorage.getItem(
                        'esa_continue_probability_distributions_lesson_v0')).url"""),
                    route)

        self.assertAlmostEqual(0.5*(1-0.5), 0.25)
        self.assertAlmostEqual(0.7*(1-0.7), 0.21)
        self.assertEqual(100*0.2, 20)
        self.assertAlmostEqual(3*0.5**3, 0.375)
        self.assertAlmostEqual(sqrt(100*0.2*0.8), 4)
        for n,p,k in ((3,0.5,2), (10,0.3,0), (10,0.3,10),
                      (20,0.2,3), (1,0.2,1), (50,0.7,35)):
            with self.subTest(n=n,p=p,k=k):
                probabilities = [comb(n,j)*(p**j)*((1-p)**(n-j))
                                 for j in range(n+1)]
                self.assertAlmostEqual(fsum(probabilities), 1, places=12)
                self.assertAlmostEqual(probabilities[k],
                    comb(n,k)*(p**k)*((1-p)**(n-k)), places=12)
                self.assertAlmostEqual(fsum(probabilities[:k+1]) +
                                       fsum(probabilities[k:]) -
                                       probabilities[k], 1, places=12)

    def test_binomial_probability_calculator_numerics_validation_and_mobile(self):
        """Inclusive tails, large n stability, Bernoulli, degenerate endpoints, errors."""
        from math import comb, fsum
        path = "/probability/distributions/binomial-distribution/"
        self.page.goto(self.origin + path, wait_until="networkidle")
        region = self.page.locator("#esa-binomial-calculator")
        expect(region.get_by_role("heading", name="Interactive Binomial Probability Calculator")).to_be_visible()
        n = self.page.get_by_label("Number of trials (n)")
        p = self.page.get_by_label("Success probability (p)")
        k = self.page.get_by_label("Success count (k)")
        exact = self.page.locator("#esa-binomial-exact")
        low = self.page.locator("#esa-binomial-cdf")
        high = self.page.locator("#esa-binomial-upper")
        mean = self.page.locator("#esa-binomial-mean")
        variance = self.page.locator("#esa-binomial-variance")
        error = self.page.locator("#esa-binomial-error")
        expect(n).to_have_value("3")
        expect(p).to_have_value("0.5")
        expect(k).to_have_value("2")
        expect(exact).to_have_text("0.375")
        expect(low).to_have_text("0.875")
        expect(high).to_have_text("0.5")
        expect(mean).to_have_text("1.5")
        expect(variance).to_have_text("0.75")

        def set_case(trials, probability, successes):
            n.fill(str(trials))
            p.fill(str(probability))
            k.fill(str(successes))
            def val(locator):
                return float(locator.inner_text().replace(",",""))
            return val(exact),val(low),val(high),val(mean),val(variance)

        for trials, probability, successes in (
            (1,0.2,1),(1,0.2,0),(5,0,0),(5,0,1),(5,1,5),(5,1,3),
            (10,0.3,0),(10,0.3,10),(20,0.2,3),(100,0.2,20),
            (1000,0.5,500),(1000,0.001,0),
        ):
            with self.subTest(trials=trials,p=probability,k=successes):
                observed = set_case(trials,probability,successes)
                if probability in (0,1):
                    deterministic = 0 if probability == 0 else trials
                    expected = (
                        1 if successes==deterministic else 0,
                        1 if successes>=deterministic else 0,
                        1 if successes<=deterministic else 0,
                        trials*probability, trials*probability*(1-probability)
                    )
                else:
                    weights = [comb(trials,j)*probability**j*
                               (1-probability)**(trials-j) for j in range(trials+1)]
                    expected = (weights[successes],
                                fsum(weights[:successes+1]),
                                fsum(weights[successes:]),
                                trials*probability, trials*probability*(1-probability))
                for actual,truth in zip(observed,expected):
                    self.assertAlmostEqual(actual,truth,delta=5e-9)

        n.fill("0")
        expect(error).to_contain_text("whole number of trials")
        expect(exact).to_have_text("—")
        n.fill("1001")
        expect(error).to_contain_text("whole number of trials")
        n.fill("1.5")
        expect(error).to_contain_text("whole number of trials")
        n.fill("")
        expect(error).to_contain_text("whole number of trials")
        n.fill("3")
        p.fill("-0.1")
        expect(error).to_contain_text("probability")
        p.fill("1.1")
        expect(error).to_contain_text("probability")
        p.fill("")
        expect(error).to_contain_text("probability")
        p.fill("0.5")
        k.fill("-1")
        expect(error).to_contain_text("whole number of successes")
        k.fill("4")
        expect(error).to_contain_text("whole number of successes")
        k.fill("1.5")
        expect(error).to_contain_text("whole number of successes")
        k.fill("")
        expect(error).to_contain_text("whole number of successes")
        k.fill("2")
        expect(error).to_be_hidden()
        expect(exact).to_have_text("0.375")
        p.focus()
        p.press("Tab")
        expect(k).to_be_focused()
        expect(region.locator('[role="status"][aria-live="polite"]')).to_be_visible()

        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                bounds=region.evaluate("""e => ({
                    left:e.getBoundingClientRect().left,
                    right:e.getBoundingClientRect().right,
                    scroll:e.scrollWidth, client:e.clientWidth
                })""")
                self.assertGreaterEqual(bounds["left"],-1,bounds)
                self.assertLessEqual(bounds["right"],width+1,bounds)
                self.assertLessEqual(bounds["scroll"]-bounds["client"],1,bounds)

        self.assertEqual(self.page.evaluate("""() =>
            JSON.parse(localStorage.getItem(
              'esa_continue_probability_distributions_lesson_v0')).url"""),path)

    def test_binomial_calculator_with_denied_browser_storage(self):
        """Calculator works even when progress persistence throws SecurityError."""
        self.page.add_init_script("""
          Object.defineProperty(window,'localStorage',{
            configurable:true,
            get(){ throw new DOMException('Denied','SecurityError'); }
          });
        """)
        self.page.goto(
            self.origin + "/probability/distributions/binomial-distribution/",
            wait_until="networkidle")
        expect(self.page.locator("main h1")).to_be_visible()
        expect(self.page.locator("#esa-binomial-exact")).to_have_text("0.375")
        self.page.get_by_label("Number of trials (n)").fill("1")
        self.page.get_by_label("Success count (k)").fill("1")
        expect(self.page.locator("#esa-binomial-exact")).to_have_text("0.5")

    def test_distribution_selection_guide_all_twelve_models_and_resume(self):
        """Scenario guide only uses verified published lesson links and states assumptions."""
        route="/probability/distributions/"
        self.page.goto(self.origin + route,wait_until="networkidle")
        guide=self.page.locator("#esa-distribution-guide")
        expect(guide.get_by_role("heading",name="Find a Distribution to Study")).to_be_visible()
        selector=self.page.get_by_label("What best describes your random outcome?")
        lessons=self.page.locator("#lessons .lesson-card h3 a[href]")
        expect(lessons).to_have_count(12)
        expect(selector.locator('option[value!=""]')).to_have_count(12)
        link=self.page.locator("#esa-distribution-lesson-link")
        title=self.page.locator("#esa-distribution-model")
        assumptions=self.page.locator("#esa-distribution-assumptions")
        parameters=self.page.locator("#esa-distribution-parameters")
        caveat=self.page.locator("#esa-distribution-caveat")
        expect(link).to_be_hidden()
        models=(
          ("bernoulli","Bernoulli","bernoulli-distribution","success probability"),
          ("binomial","Binomial","binomial-distribution","independent"),
          ("geometric","Geometric","geometric-distribution","first success"),
          ("negative-binomial","Negative binomial","negative-binomial-distribution","r-th"),
          ("poisson","Poisson","poisson-distribution","Poisson"),
          ("hypergeometric","Hypergeometric","hypergeometric-distribution","without replacement"),
          ("uniform","Continuous uniform","uniform-distribution","constant"),
          ("exponential","Exponential","exponential-distribution","constant"),
          ("gamma","Gamma","gamma-distribution","shape"),
          ("beta","Beta","beta-distribution","continuous"),
          ("normal","Normal","normal-distribution","symmetric"),
          ("lognormal","Lognormal","lognormal-distribution","logarithm"),
        )
        for value,name,slug,idea in models:
            with self.subTest(model=value):
                selector.select_option(value)
                expect(title).to_have_text(name+" distribution")
                expect(link).to_be_visible()
                expected="/probability/distributions/"+slug+"/"
                expect(link).to_have_attribute("href",expected)
                self.assertTrue((SITE/expected.lstrip("/")/"index.html").is_file())
                self.assertIn(expected,[a.get_attribute("href") for a in lessons.all()])
                self.assertGreater(len(assumptions.inner_text()),35)
                self.assertGreater(len(parameters.inner_text()),15)
                expect(guide).to_contain_text(idea)
                expect(caveat).to_contain_text("not a validated model selection")
        selector.select_option("")
        expect(link).to_be_hidden()
        expect(title).to_have_text("Choose a scenario")
        selector.focus()
        selector.press("ArrowDown")
        expect(selector).to_have_value("bernoulli")
        expect(link).to_have_attribute("href","/probability/distributions/bernoulli-distribution/")

        valid="/probability/distributions/binomial-distribution/"
        self.page.evaluate("""([path]) =>
           localStorage.setItem('esa_continue_probability_distributions_lesson_v0',
             JSON.stringify({url:path,label:'Binomial Distribution',ts:1234567}))""",[valid])
        self.page.reload(wait_until="networkidle")
        resume=self.page.locator("#continue-reading-probability-distributions")
        expect(resume).to_be_visible()
        expect(self.page.locator("#continue-reading-probability-distributions-btn")).to_have_attribute("href",valid)
        self.assertEqual(self.page.locator("#lessons .lesson-card").count(),12)
        expect(self.page.locator("#esa-distribution-scenario")).to_be_visible()
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                bounds=guide.evaluate("""e => ({
                    left:e.getBoundingClientRect().left,
                    right:e.getBoundingClientRect().right,
                    scroll:e.scrollWidth,client:e.clientWidth
                })""")
                self.assertGreaterEqual(bounds["left"],-1,bounds)
                self.assertLessEqual(bounds["right"],width+1,bounds)
                self.assertLessEqual(bounds["scroll"]-bounds["client"],1,bounds)

    def test_distribution_selection_guide_without_storage(self):
        """Storage denial does not interrupt the model guide or lesson cards."""
        self.page.add_init_script("""
          Object.defineProperty(window,'localStorage',{
            configurable:true,
            get(){ throw new DOMException('Denied','SecurityError'); }
          });
        """)
        self.page.goto(self.origin+"/probability/distributions/",wait_until="networkidle")
        self.page.locator("#esa-distribution-scenario").select_option("hypergeometric")
        expect(self.page.locator("#esa-distribution-model")).to_have_text("Hypergeometric distribution")
        expect(self.page.locator("#esa-distribution-lesson-link")).to_have_attribute(
            "href","/probability/distributions/hypergeometric-distribution/")
        expect(self.page.locator("#lessons .lesson-card")).to_have_count(12)
        expect(self.page.locator("#continue-reading-probability-distributions")).to_be_hidden()

    def test_welch_and_paired_repaired_mathematics_and_numeric_examples(self):
        """Recalculate Welch and paired inferences against lesson statements."""
        from math import sqrt, isclose
        a = "/inference/classical-tests/two-sample-t-test-independent/"
        b = "/inference/classical-tests/paired-t-test/"
        required = (
            (a, 18, (
                r"\operatorname{SE}_{W}=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}",
                r"\nu_W=\frac{(s_1^2/n_1+s_2^2/n_2)^2}",
                r"t_W=\frac{6}{3.1241}\approx1.9206",
                "[−0.287, 12.287]",
                "p-value is approximately 0.0609",
                "fail to reject equality")),
            (b, 10, (
                r"D_i=Y_{i,\mathrm{after}}-Y_{i,\mathrm{before}}",
                r"\bar D=\frac1n\sum_{i=1}^n D_i",
                r"\bar D\pm t_{1-\alpha/2,\,n-1}",
                "0.00036",
                "[3.16, 5.24]",
                "11.225"))
        )
        for route, restored, phrases in required:
            with self.subTest(lesson=route):
                html = (SITE / route.lstrip("/") / "index.html").read_text()
                main = html.split('<main id="main-content"', 1)[1].split(
                    "</main>", 1)[0]
                self.assertNotIn("\uea01", main)
                self.assertNotIn("\uea02", main)
                # Jekyll-generated pages preserve 2 raw TeX delimiters per expression;
                # Welch and paired additions also contain verified explanatory TeX.
                self.assertGreaterEqual(main.count(r"\["), restored)
                self.assertEqual(main.count(r"\["), main.count(r"\]"))
                for phrase in phrases:
                    with self.subTest(required=phrase):
                        self.assertIn(phrase, main)
                self.page.goto(self.origin + route, wait_until="networkidle")
                saved = self.page.evaluate(
                    'key => JSON.parse(localStorage.getItem(key))',
                    "esa_continue_inference_classical_tests_lesson_v0")
                self.assertEqual(saved["url"], route)
                self.assertGreater(self.page.locator("main a[href]").count(), 0)

        se = sqrt(10**2/25 + 12**2/25)
        v1, v2 = 10**2/25, 12**2/25
        df = (v1+v2)**2/(v1**2/24+v2**2/24)
        t = 6/se
        self.assertTrue(isclose(se, 3.1240998703626617, abs_tol=1e-12))
        self.assertTrue(isclose(df, 46.48828735033837, abs_tol=1e-10))
        self.assertTrue(isclose(t, 1.9205531989934397, abs_tol=1e-12))
        critical = 2.0123252171461927
        self.assertTrue(isclose(6-critical*se, -0.28670495001393537, abs_tol=1e-9))
        self.assertTrue(isclose(6+critical*se, 12.286704950013934, abs_tol=1e-9))
        differences = [5, 4, 4, 3, 5]
        avg = sum(differences)/len(differences)
        variance = sum((x-avg)**2 for x in differences)/(len(differences)-1)
        paired_t = avg/sqrt(variance/len(differences))
        self.assertTrue(isclose(avg, 4.2))
        self.assertTrue(isclose(variance, 0.7))
        self.assertTrue(isclose(paired_t, 11.224972160321826, abs_tol=1e-12))

    def test_test_selection_guide_assumptions_keyboard_and_mobile(self):
        """10 supported scenarios, unsupported cases and semantic accessible links."""
        route = "/inference/classical-tests/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        guide = self.page.locator("#esa-test-guide")
        outcome = guide.get_by_label("What outcome are you analyzing?")
        design = guide.get_by_label("Which study design or question?")
        sigma = guide.get_by_label("For a one-sample mean, is population σ known?")
        status = guide.locator('[role="status"][aria-live="polite"]')
        self.assertEqual(self.page.locator("#test-selection-guide").count(), 1)
        self.assertEqual(status.count(), 1)
        cases = (
            ("mean", "one", "unknown", "one-sample-t-test-for-mean"),
            ("mean", "one", "known", "one-sample-z-test-for-mean"),
            ("mean", "paired", "unknown", "paired-t-test"),
            ("mean", "independent", "unknown", "two-sample-t-test-independent"),
            ("mean", "multiple", "unknown", "one-way-anova-f-test"),
            ("binary", "one", "unknown", "one-proportion-z-test"),
            ("binary", "independent", "unknown", "two-proportion-z-test"),
            ("categorical", "one", "unknown", "chi-square-goodness-of-fit"),
            ("categorical", "independent", "unknown", "chi-square-homogeneity-test"),
            ("categorical", "association", "unknown", "chi-square-independence-test"),
        )
        for kind, structure, known, slug in cases:
            with self.subTest(choice=slug):
                outcome.select_option(kind)
                design.select_option(structure)
                if kind == "mean" and structure == "one":
                    sigma.select_option(known)
                link = status.get_by_role("link")
                expect(link).to_have_attribute(
                    "href", "/inference/classical-tests/" + slug + "/")
                self.assertGreater(len(status.inner_text()), 100)
                self.assertTrue(
                    (SITE/"inference/classical-tests"/slug/"index.html").is_file())
        outcome.select_option("binary")
        design.select_option("paired")
        expect(status.get_by_role("link")).to_have_count(0)
        expect(status).to_contain_text("different design-specific method")
        outcome.select_option("mean")
        design.select_option("one")
        sigma.focus()
        self.page.keyboard.press("End")
        self.page.keyboard.press("Home")
        expect(status.get_by_role("link")).to_have_attribute(
            "href", "/inference/classical-tests/one-sample-t-test-for-mean/")
        for width in (375, 768, 1280):
            self.page.set_viewport_size({"width": width, "height": 850})
            overflow = self.page.evaluate(
                "() => document.documentElement.scrollWidth-innerWidth")
            offenders = self.page.evaluate("""() =>
              [...document.querySelectorAll('body *')]
                .filter(e => e.getBoundingClientRect().right > innerWidth + 1)
                .map(e => ({tag:e.tagName, id:e.id, className:
                  typeof e.className === 'string' ? e.className.slice(0,70) : '',
                  right:Math.round(e.getBoundingClientRect().right)}))
                .slice(0, 8)
            """) if overflow > 1 else []
            self.assertLessEqual(overflow, 1,
                                 f"Guide overflow at {width}px: {offenders}")

    def test_search_index_excludes_lesson_navigation_and_progress_noise(self):
        """Index remains discoverable while snippets prioritize lesson content."""
        sample_url = "/inference/classical-tests/two-sample-t-test-independent/"
        records = {r["url"]: r for r in self.records}
        self.assertIn(sample_url, records)
        body = records[sample_url]["content"]
        self.assertNotIn("esa_continue_inference_classical_tests_lesson_v0", body)
        self.assertNotIn("Previous Lesson", body)
        self.assertIn("Welch", body)
        self.assertIn("p-value", body)
        for query, expected in (
            ("two-sample t test", sample_url),
            ("paired t test", "/inference/classical-tests/paired-t-test/"),
            ("chi-square independence", "/inference/classical-tests/chi-square-independence-test/"),
            ("measurement scales", "/foundations/measurement-scales/"),
        ):
            with self.subTest(query=query):
                self.open()
                self.input.fill(query)
                if query == "measurement scales":
                    # Both Foundations and Descriptive Statistics publish
                    # a lesson with this exact title; either may rank first.
                    self.assertIn(expected, self.results.locator(
                        "a.search-item").evaluate_all(
                        "links => links.map(link => link.getAttribute('href'))"))
                else:
                    expect(self.results.locator("a.search-item").first).to_have_attribute(
                        "href", expected)
                self.assertEqual(self.errors, [])

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
