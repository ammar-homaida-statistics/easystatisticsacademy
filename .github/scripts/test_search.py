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
            "/modeling/", "/inference/", "/foundations/"])
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
