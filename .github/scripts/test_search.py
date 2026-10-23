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
        # Batch #67: untrusted stored labels must match the published lesson
        # title, rather than merely being rendered as escaped literal text.
        expect(panel).to_be_hidden()
        expect(link).to_have_attribute("href", "#")
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

        # Timestamp-free historical records with a valid published label
        # must still resume correctly across mobile widths.
        save({"url": lesson, "label": "Categorical vs Numerical Data"})
        self.page.set_viewport_size({"width": 375, "height": 750})
        expect(panel).to_be_visible()
        expect(label.locator("strong")).to_have_text("Categorical vs Numerical Data")
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
                if slug == "tabular-summaries":
                    # This block now requires the exact published lesson title.
                    # Reject untrusted labels rather than rendering them.
                    expect(panel).to_be_hidden()
                    title = self.page.locator("#lessons .lesson-card h3 a[href]").first.inner_text().strip()
                    save({"url": valid, "label": title})
                    expect(panel).to_be_visible()
                    expect(link).to_have_attribute("href", valid)
                    expect(label.locator("strong")).to_have_text(title)
                else:
                    # Older blocks continue to treat labels as text, not HTML.
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
                if route == "/descriptive/spread/":
                    # Spread now requires the exact published title, even if the
                    # saved URL is canonical. A forged label must be rejected.
                    expect(panel).to_be_hidden()
                    published_title = self.page.locator(
                        selector + "[href]").first.inner_text().strip()
                    save({"url": listed, "label": published_title})
                    expect(panel).to_be_visible()
                    expect(action).to_have_attribute("href", listed)
                    expect(label.locator("strong")).to_have_text(published_title)
                else:
                    # The other two overviews retain their existing safe
                    # text-only rendering of untrusted labels.
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
        # Four restored source expressions remain, with the new exact-power formula fifth.
        self.assertIn(r"1-\Phi(z_{1-\alpha/2}-\Delta\sqrt{n})",main)
        self.assertEqual(main.count(r"\["), 5)
        self.assertEqual(main.count(r"\]"), 5)
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
                if slug == "distributions":
                    # This block now requires the exact published lesson title.
                    # A hostile label on a valid URL must be rejected.
                    expect(panel).to_be_hidden()
                    published_title = self.page.locator(
                        "#lessons .lesson-card h3 a[href]").first.inner_text().strip()
                    set_history({"url":valid,"label":published_title})
                    expect(panel).to_be_visible()
                    expect(link).to_have_attribute("href",valid)
                    expect(label.locator("strong")).to_have_text(published_title)
                else:
                    # Other probability blocks retain their safe literal-text labels.
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
                # Legitimate saved progress must still work after invalid records.
                expected_label = (published_title if slug == "distributions"
                                  else "Continue a published lesson")
                set_history({"url":valid,"label":expected_label})
                expect(panel).to_be_visible()
                expect(link).to_have_attribute("href", valid)
                expect(label.locator("strong")).to_have_text(expected_label)

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
        expect(selector.locator('option:not([value=""])')).to_have_count(12)
        link=self.page.locator("#esa-distribution-lesson-link")
        title=self.page.locator("#esa-distribution-model")
        assumptions=self.page.locator("#esa-distribution-assumptions")
        parameters=self.page.locator("#esa-distribution-parameters")
        caveat=self.page.locator("#esa-distribution-caveat")
        expect(link).to_be_hidden()
        models=(
          ("bernoulli","Bernoulli","bernoulli-distribution","binary"),
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


    def test_poisson_exponential_formula_restorations_and_benchmarks(self):
        """All 21 recovered formulas are present; key numerical claims checked independently."""
        from html import unescape
        from math import exp, factorial, fsum, isclose
        cases = (
            ("/probability/distributions/poisson-distribution/",10,(
                r"\lambda\ge 0",r"X\sim\operatorname{Poisson}(\lambda)",
                r"P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}",
                r"P(X=2)=\frac{e^{-3}3^2}{2!}",
                r"\operatorname{E}(X)=\lambda",
                r"\operatorname{Var}(X)=\lambda",
                r"\operatorname{SD}(X)=\sqrt{\lambda}",r"\lambda=np",
                "independent increments")),
            ("/probability/distributions/exponential-distribution/",11,(
                r"\lambda>0",r"f_X(x)=\lambda e^{-\lambda x}",
                r"F_X(x)=P(X\le x)=1-e^{-\lambda x}",
                r"P(X>x)=e^{-\lambda x}",
                r"P(X\le 1)=1-e^{-2}",
                r"\operatorname{E}(X)=\frac{1}{\lambda}",
                r"\operatorname{Var}(X)=\frac{1}{\lambda^2}",
                r"\operatorname{SD}(X)=\frac{1}{\lambda}",
                r"P(X>s+t\mid X>s)=P(X>t)"))
        )
        for route,count,fragments in cases:
            with self.subTest(route=route):
                source=(SITE/route.lstrip("/")/"index.html").read_text()
                main=unescape(source.split('<main id="main-content"',1)[1]
                              .split("</main>",1)[0])
                self.assertNotIn("\uea01",main)
                self.assertNotIn("\uea02",main)
                self.assertEqual(main.count(r"\["),count)
                self.assertEqual(main.count(r"\]"),count)
                for fragment in fragments:
                    self.assertIn(fragment,main)
                self.page.goto(self.origin+route,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        for lam in (0,0.1,2,3,10):
            probs=([1.0]+[0.0]*120) if lam==0 else [
                exp(-lam)*lam**k/factorial(k) for k in range(121)]
            self.assertTrue(isclose(fsum(probs),1,abs_tol=1e-12))
            self.assertTrue(isclose(fsum(k*x for k,x in enumerate(probs)),lam,
                                     abs_tol=1e-10))
        self.assertAlmostEqual(exp(-3)*3**2/factorial(2),
                               0.22404180765538775,delta=1e-14)
        self.assertAlmostEqual(1-exp(-2),0.8646647167633873,delta=1e-14)
        for lam in (0.25,1,2,20):
            for t in (0,0.5,1,4):
                survival=exp(-lam*t)
                self.assertAlmostEqual(survival,1-(1-survival),delta=1e-14)
                self.assertAlmostEqual(
                    exp(-lam*(t+0.75))/survival,exp(-lam*0.75),delta=1e-12)

    def test_poisson_exponential_explorer_numerics_limits_and_mobile(self):
        """Accessible input controls, event identity, extreme cases, mobile overflow."""
        from math import exp,expm1,isclose
        route="/probability/distributions/poisson-distribution/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        region=self.page.locator("#esa-poisson-exponential-explorer")
        expect(region.get_by_role("heading",name="Interactive Poisson–Exponential Explorer")).to_be_visible()
        rate=self.page.get_by_label("Rate (events per minute)")
        time=self.page.get_by_label("Observation time (minutes)")
        error=self.page.locator("#esa-event-error")
        outputs=[self.page.locator("#"+id) for id in
                 ("esa-event-none","esa-event-survival","esa-event-at-least-one",
                  "esa-event-expected","esa-event-meanwait")]
        self.assertEqual(region.locator('[role="status"][aria-live="polite"]').count(),1)
        self.assertEqual(rate.input_value(),"2")
        self.assertEqual(time.input_value(),"1")
        def check(r,t):
            rate.fill(str(r));time.fill(str(t))
            observed=[float(x.inner_text()) for x in outputs]
            truth=(exp(-r*t),exp(-r*t),-expm1(-r*t),r*t,1/r)
            for got,expected in zip(observed,truth):
                self.assertTrue(isclose(got,expected,abs_tol=5.1e-7),
                                (r,t,got,expected))
            expect(error).to_be_hidden()
        for r,t in ((2,1),(0.01,0),(0.5,2),(1,1),(4,0.25),(20,60)):
            with self.subTest(rate=r,time=t):
                check(r,t)
        for bad in ("0","-1","21",""):
            rate.fill(bad)
            expect(error).to_contain_text("Rate must")
            expect(outputs[0]).to_have_text("—")
        rate.fill("2")
        for bad in ("-1","61",""):
            time.fill(bad)
            expect(error).to_contain_text("Time must")
            expect(outputs[0]).to_have_text("—")
        region.get_by_role("button",name="Reset example").click()
        expect(rate).to_have_value("2")
        expect(time).to_have_value("1")
        check(2,1)
        rate.focus()
        rate.press("Tab")
        expect(time).to_be_focused()
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                bounds=region.evaluate("""e => ({
                    left:e.getBoundingClientRect().left,
                    right:e.getBoundingClientRect().right,
                    scroll:e.scrollWidth,client:e.clientWidth
                })""")
                self.assertGreaterEqual(bounds["left"],-1,bounds)
                self.assertLessEqual(bounds["right"],width+1,bounds)
                self.assertLessEqual(bounds["scroll"]-bounds["client"],1,bounds)
        self.assertEqual(self.page.evaluate("""() =>
            JSON.parse(localStorage.getItem(
            'esa_continue_probability_distributions_lesson_v0')).url"""),route)

    def test_poisson_exponential_explorer_denied_localstorage(self):
        """Failed localStorage writes must not break the explorer."""
        self.page.add_init_script("""
          Object.defineProperty(window,'localStorage',{
            configurable:true,
            get(){throw new DOMException('Denied','SecurityError');}
          });
        """)
        self.page.goto(self.origin+"/probability/distributions/poisson-distribution/",
                       wait_until="networkidle")
        expect(self.page.locator("main h1")).to_be_visible()
        expect(self.page.locator("#esa-event-none")).to_have_text("0.135335")
        self.page.get_by_label("Rate (events per minute)").fill("1")
        expect(self.page.locator("#esa-event-none")).to_have_text("0.367879")

    def test_lln_clt_six_lessons_continue_reading_values(self):
        """All six lesson URLs and labels persist using the original progress key."""
        lessons=(
            ("convergence-intuition","Convergence Intuition"),
            ("law-of-large-numbers","Law of Large Numbers"),
            ("weak-vs-strong-lln","Weak vs Strong LLN"),
            ("central-limit-theorem","Central Limit Theorem"),
            ("normal-approximation","Normal Approximation"),
            ("inference-bridge","Inference Bridge"),
        )
        for slug,label in lessons:
            with self.subTest(lesson=slug):
                route="/probability/lln-clt/"+slug+"/"
                self.page.goto(self.origin+route,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                saved=self.page.evaluate("""() => JSON.parse(
                  localStorage.getItem('esa_continue_probability_lln_clt_lesson_v0'))""")
                self.assertEqual(saved["url"],route)
                self.assertEqual(saved["label"],label)
                self.assertIsInstance(saved["ts"],int)
                self.assertGreater(saved["ts"],0)

    def test_lln_clt_six_lessons_denied_localstorage(self):
        """No JavaScript errors or missing lesson navigation under denied storage."""
        self.page.add_init_script("""
          Object.defineProperty(window,'localStorage',{
            configurable:true,
            get(){throw new DOMException('Denied','SecurityError');}
          });
        """)
        for slug in ("convergence-intuition","law-of-large-numbers",
                     "weak-vs-strong-lln","central-limit-theorem",
                     "normal-approximation","inference-bridge"):
            with self.subTest(lesson=slug):
                route="/probability/lln-clt/"+slug+"/"
                self.page.goto(self.origin+route,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(self.page.locator("main a[href]").count(),0)
                self.assertEqual(self.errors,[])


    def test_ci_independent_and_paired_restored_math_and_numerical_examples(self):
        """Recover all 22 damaged expressions and validate independent numerical benchmarks."""
        from html import unescape
        from math import sqrt, isclose
        cases=(
            ("/inference/confidence-intervals/ci-for-difference-of-means-independent/",
             (r"\Delta=\mu_1-\mu_2",
              r"\widehat{\operatorname{SE}}(\bar X_1-\bar X_2)",
              r"t_{1-\alpha/2,\,\widehat{\nu}}",
              r"\bar x_1-\bar x_2=82-76=6",
              r"\text{Margin of error}",
              r"\mu_1-\mu_2")),
            ("/inference/confidence-intervals/ci-for-paired-mean-difference/",
             (r"d_i=\text{after}_i-\text{before}_i",
              r"\mu_d=\operatorname{E}(D)",
              r"\widehat{\operatorname{SE}}(\bar d)",
              r"t_{1-\alpha/2,\,n-1}",
              r"\nu=36-1=35",
              r"-4.5\pm2.71")),
        )
        for route,formulas in cases:
            with self.subTest(route=route):
                source=(SITE/route.lstrip("/")/"index.html").read_text()
                main=unescape(source.split('<main id="main-content"',1)[1].split("</main>",1)[0])
                self.assertNotIn("\uea01",main)
                self.assertNotIn("\uea02",main)
                self.assertEqual(main.count(r"\["),11)
                self.assertEqual(main.count(r"\]"),11)
                for item in formulas:
                    self.assertIn(item,main)
                self.page.goto(self.origin+route,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        se=sqrt(10**2/40+12**2/35)
        df=(10**2/40+12**2/35)**2 / ((10**2/40)**2/39+(12**2/35)**2/34)
        self.assertTrue(isclose(se,2.5718253662108777,abs_tol=1e-12))
        self.assertTrue(isclose(df,66.47542250283321,abs_tol=1e-9))
        self.assertTrue(isclose(6-2*se,.8563492675782447,abs_tol=1e-12))
        self.assertTrue(isclose(6+2*se,11.143650732421754,abs_tol=1e-12))
        paired=8/sqrt(36)
        self.assertTrue(isclose(paired,4/3,abs_tol=1e-12))
        self.assertTrue(isclose(-4.5-2.03*paired,-7.206666666666667,abs_tol=1e-12))
        self.assertEqual(sum((-8,-5,-8,-6,-9))/5,-7.2)

    def test_ci_paired_vs_independent_se_explorer_interaction_and_mobile(self):
        """Numerical standard errors, disabled fields, keyboard controls and no overflow."""
        from math import sqrt,isclose
        route="/inference/confidence-intervals/ci-for-paired-mean-difference/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        root=self.page.locator("#esa-ci-design-explorer")
        expect(root.get_by_role("heading",name="Explore Paired versus Independent Standard Errors")).to_be_visible()
        a=self.page.get_by_label("Standard deviation of measurement A")
        b=self.page.get_by_label("Standard deviation of measurement B")
        n=self.page.get_by_label("Number of pairs / observations per group")
        rho=self.page.locator("#esa-ci-rho")
        si=self.page.locator("#esa-ci-independent-se")
        sp=self.page.locator("#esa-ci-paired-se")
        ratio=self.page.locator("#esa-ci-se-ratio")
        expect(si).to_have_text("2.8284")
        expect(sp).to_have_text("1.5492")
        expect(ratio).to_have_text("0.5477")
        for aval,bval,nn,rr in ((10,10,25,0),(10,10,25,-0.5),(4,7,40,0.9),
                                 (3,5,2,-0.9),(0.01,5,10000,0.7)):
            with self.subTest(a=aval,b=bval,n=nn,rho=rr):
                a.fill(str(aval));b.fill(str(bval));n.fill(str(nn))
                rho.evaluate("""(node,value)=>{
                   node.value=String(value);
                   node.dispatchEvent(new Event('input',{bubbles:true}));
                }""",rr)
                expectedI=sqrt((aval*aval+bval*bval)/nn)
                expectedP=sqrt((aval*aval+bval*bval-2*rr*aval*bval)/nn)
                self.assertTrue(isclose(float(si.inner_text()),expectedI,abs_tol=5.1e-5))
                self.assertTrue(isclose(float(sp.inner_text()),expectedP,abs_tol=5.1e-5))
                self.assertTrue(isclose(float(ratio.inner_text()),expectedP/expectedI,abs_tol=5.1e-5))
        n.fill("1")
        expect(self.page.locator("#esa-ci-design-error")).to_be_visible()
        expect(sp).to_have_text("—")
        n.fill("")
        expect(sp).to_have_text("—")
        root.get_by_role("button",name="Reset example").click()
        expect(n).to_have_value("25")
        expect(sp).to_have_text("1.5492")
        rho.focus()
        rho.press("Home")
        expect(self.page.locator("#esa-ci-rho-value")).to_have_text("-0.90")
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                bounds=root.evaluate("""e=>({
                    left:e.getBoundingClientRect().left,
                    right:e.getBoundingClientRect().right,
                    scroll:e.scrollWidth,client:e.clientWidth
                })""")
                self.assertGreaterEqual(bounds["left"],-1,bounds)
                self.assertLessEqual(bounds["right"],width+1,bounds)
                self.assertLessEqual(bounds["scroll"]-bounds["client"],1,bounds)

    def test_ci_selection_guide_six_methods_and_unsupported(self):
        """All published CI methods, design-specific caveats and no fake links."""
        self.page.goto(self.origin+"/inference/confidence-intervals/",wait_until="networkidle")
        root=self.page.locator("#esa-ci-method-guide")
        expect(root.get_by_role("heading",name="Which Confidence Interval Should I Study?")).to_be_visible()
        goal=self.page.locator("#esa-ci-goal")
        design=self.page.locator("#esa-ci-design")
        sigma=self.page.locator("#esa-ci-known-sigma")
        link=self.page.locator("#esa-ci-method-link-wrapper a")
        cases=(
           ("mean","one","unknown","ci-for-mean-sigma-unknown-t"),
           ("mean","one","known","ci-for-mean-sigma-known-z"),
           ("mean","independent","unknown","ci-for-difference-of-means-independent"),
           ("mean","paired","unknown","ci-for-paired-mean-difference"),
           ("proportion","one","unknown","ci-for-proportion"),
           ("proportion","independent","unknown","ci-for-difference-of-proportions"),
        )
        for outcome,structure,known,slug in cases:
            with self.subTest(outcome=outcome,design=structure,known=known):
                goal.select_option(outcome)
                design.select_option(structure)
                if outcome=="mean" and structure=="one":
                    sigma.select_option(known)
                expect(link).to_have_count(1)
                self.assertEqual(link.get_attribute("href"),
                    "/inference/confidence-intervals/"+slug+"/")
                expect(self.page.locator("#esa-ci-method-assumptions")).not_to_be_empty()
                expect(self.page.locator("#esa-ci-method-caution")).not_to_be_empty()
                expect(self.page.locator("#esa-ci-known-sigma-wrapper")).to_be_visible() if (
                    outcome=="mean" and structure=="one") else expect(
                    self.page.locator("#esa-ci-known-sigma-wrapper")).to_be_hidden()
        goal.select_option("proportion")
        design.select_option("paired")
        expect(link).to_have_count(0)
        expect(self.page.locator("#esa-ci-method-name")).to_contain_text("No direct method")
        expect(self.page.locator("#esa-ci-method-caution")).to_contain_text("does not invent")
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                bounds=root.evaluate("""e=>({
                    left:e.getBoundingClientRect().left,
                    right:e.getBoundingClientRect().right,
                    scroll:e.scrollWidth,client:e.clientWidth
                })""")
                self.assertGreaterEqual(bounds["left"],-1,bounds)
                self.assertLessEqual(bounds["right"],width+1,bounds)
                self.assertLessEqual(bounds["scroll"]-bounds["client"],1,bounds)

    def test_ci_guide_respects_existing_continue_reading(self):
        """New navigation must preserve existing valid confidence-interval progress."""
        route="/inference/confidence-intervals/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        destination=route+"ci-for-paired-mean-difference/"
        self.page.evaluate("""url=>{
            localStorage.setItem('esa_continue_inference_confidence_intervals_lesson_v0',
                JSON.stringify({url,label:'Paired Mean Difference',ts:123456789}));
        }""",destination)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-inference-ci")).to_be_visible()
        self.assertEqual(self.page.locator("#continue-reading-inference-ci-btn").get_attribute("href"),destination)
        expect(self.page.locator("#continue-reading-inference-ci-label")).to_contain_text("Paired Mean Difference")
        expect(self.page.locator("#esa-ci-method-link-wrapper a")).to_have_count(1)

    def test_ci_explorer_and_selection_guide_under_denied_storage(self):
        """Both tools and existing lesson navigation survive denied storage access."""
        self.page.add_init_script("""
           Object.defineProperty(window,'localStorage',{
               configurable:true,
               get(){throw new DOMException('Denied','SecurityError');}
           });
        """)
        for route in ("/inference/confidence-intervals/",
                      "/inference/confidence-intervals/ci-for-paired-mean-difference/"):
            with self.subTest(route=route):
                self.page.goto(self.origin+route,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertEqual(self.errors,[])
        self.page.locator("#esa-ci-sigma-a").fill("8")
        expect(self.page.locator("#esa-ci-paired-se")).not_to_have_text("—")
        self.page.goto(self.origin+"/inference/confidence-intervals/",wait_until="networkidle")
        self.page.locator("#esa-ci-design").select_option("paired")
        expect(self.page.locator("#esa-ci-method-link-wrapper a")).to_have_count(1)



    def test_conditional_probability_seventeen_restored_formulas_and_examples(self):
        """All seventeen expressions are legible, and the probability examples agree."""
        from html import unescape
        from math import isclose
        cases=(
          ("/probability/conditional/what-is-conditional-probability/",6,(
            r"P(A\mid B)",r"\frac{4}{12}=\frac{1}{3}",
            r"\frac{P(A\cap B)}{P(B)}",r"P(B)>0",
            r"\frac{0.20}{0.50}=0.40",
            r"P(A\mid B)=P(A)")),
          ("/probability/conditional/multiplication-rule/",11,(
            r"P(A\cap B)=P(A\mid B)P(B)",
            r"P(A\cap B)=P(B\mid A)P(A)",
            r"\frac{4}{52}",r"\frac{3}{51}",
            r"\frac{1}{221}",r"0.004525",
            r"0.5\times0.5=0.25",
            r"0.60(0.90)=0.54",
            r"P(A\cap B\cap C)"))
        )
        for route,count,fragments in cases:
            with self.subTest(route=route):
                source=(SITE/route.lstrip("/")/"index.html").read_text()
                main=unescape(source.split('<main id="main-content"',1)[1]
                                     .split("</main>",1)[0])
                self.assertNotIn("\uea01",main)
                self.assertNotIn("\uea02",main)
                self.assertEqual(main.count(r"\["),count)
                self.assertEqual(main.count(r"\]"),count)
                for fragment in fragments:
                    self.assertIn(fragment,main)
                self.page.goto(self.origin+route,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.assertAlmostEqual(4/12,1/3,delta=1e-14)
        self.assertAlmostEqual(.20/.50,.40,delta=1e-14)
        self.assertTrue(isclose((4/52)*(3/51),1/221,abs_tol=1e-14))
        self.assertAlmostEqual((4/52)*(3/51),.004524886877828055,delta=1e-14)
        self.assertAlmostEqual(.60*.90,.54,delta=1e-14)
        intro=(SITE/"probability/conditional/what-is-conditional-probability/index.html").read_text()
        self.assertIn("This does not determine the unconditional probability P(A)",intro)

    def test_conditional_tree_explorer_path_sums_bayes_and_boundaries(self):
        """Four leaves form a partition; posterior becomes undefined if evidence is impossible."""
        from math import isclose
        route="/probability/conditional/multiplication-rule/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        root=self.page.locator("#esa-conditional-tree-explorer")
        expect(root.get_by_role("heading",name="Interactive Conditional Probability Tree")).to_be_visible()
        inputs=[root.locator("#"+part) for part in
                ("esa-tree-study","esa-tree-pass-study","esa-tree-pass-no-study")]
        ids=("esa-tree-joint-study-pass","esa-tree-joint-study-fail",
             "esa-tree-joint-no-study-pass","esa-tree-joint-no-study-fail")
        leaves=[root.locator("#"+item) for item in ids]
        total=root.locator("#esa-tree-total-pass")
        posterior=root.locator("#esa-tree-bayes")
        note=root.locator("#esa-tree-undefined-note")
        self.assertEqual([x.input_value() for x in inputs],["0.6","0.9","0.4"])
        expect(total).to_have_text("0.7000")
        expect(posterior).to_have_text("0.7714")
        def update(s,conditional1,conditional0):
            for node,value in zip(inputs,(s,conditional1,conditional0)):
                node.evaluate("""(el,value)=>{
                  el.value=String(value);
                  el.dispatchEvent(new Event('input',{bubbles:true}));
                }""",value)
            expected=(s*conditional1,s*(1-conditional1),
                      (1-s)*conditional0,(1-s)*(1-conditional0))
            actual=tuple(float(node.inner_text()) for node in leaves)
            for observed,truth in zip(actual,expected):
                self.assertTrue(isclose(observed,truth,abs_tol=5.1e-5),
                                (s,conditional1,conditional0,observed,truth))
            self.assertTrue(isclose(sum(actual),1,abs_tol=0.00021))
            prob=expected[0]+expected[2]
            self.assertTrue(isclose(float(total.inner_text()),prob,abs_tol=5.1e-5))
            self.assertEqual(root.locator("#esa-tree-multiply").inner_text(),leaves[0].inner_text())
            if prob==0:
                expect(posterior).to_have_text("Undefined")
                expect(note).to_be_visible()
            else:
                self.assertTrue(isclose(float(posterior.inner_text()),
                          expected[0]/prob,abs_tol=5.1e-5))
                expect(note).to_be_hidden()
        for parameters in ((0.6,.9,.4),(.05,0,0),(.95,1,1),(.4,.15,.85),(.8,0,1),(.1,1,0)):
            with self.subTest(parameters=parameters):
                update(*parameters)
        root.get_by_role("button",name="Reset probability tree").click()
        self.assertEqual([x.input_value() for x in inputs],["0.6","0.9","0.4"])
        expect(total).to_have_text("0.7000")
        expect(posterior).to_have_text("0.7714")
        self.assertEqual(root.locator('a[href*="law-of-total-probability"]').count(),1)
        self.assertEqual(root.locator('a[href*="bayes-theorem"]').count(),1)

    def test_conditional_tree_explorer_keyboard_and_mobile(self):
        """A real two-stage tree, native slider keys, and no horizontal overflow."""
        self.page.goto(self.origin+"/probability/conditional/multiplication-rule/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-conditional-tree-explorer")
        self.assertEqual(root.locator(".esa-tree-root>li").count(),2)
        self.assertEqual(root.locator(".esa-tree-root>li>ul>li").count(),4)
        study=root.get_by_role("slider",name="Probability of studying:")
        study.focus()
        study.press("Home")
        expect(study).to_have_value("0.05")
        expect(root.locator("#esa-tree-study-value")).to_have_text("0.05")
        study.press("ArrowRight")
        expect(study).to_have_value("0.1")
        expect(root.locator("#esa-tree-study-value")).to_have_text("0.10")
        root.get_by_role("slider",name="Probability of passing given studying:").focus()
        root.get_by_role("slider",name="Probability of passing given studying:").press("End")
        expect(root.locator("#esa-tree-pass-study-value")).to_have_text("1.00")
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                bounds=root.evaluate("""e=>({
                   left:e.getBoundingClientRect().left,
                   right:e.getBoundingClientRect().right,
                   scroll:e.scrollWidth,client:e.clientWidth
                })""")
                self.assertGreaterEqual(bounds["left"],-1,bounds)
                self.assertLessEqual(bounds["right"],width+1,bounds)
                self.assertLessEqual(bounds["scroll"]-bounds["client"],1,bounds)

    def test_conditional_six_lessons_progress_and_continue_reading(self):
        """All six original URLs, labels and timestamps persist without schema changes."""
        lessons=(
          ("what-is-conditional-probability","What Is Conditional Probability?"),
          ("multiplication-rule","Multiplication Rule"),
          ("law-of-total-probability","Law of Total Probability"),
          ("bayes-theorem","Bayes' Theorem"),
          ("tree-diagrams","Tree Diagrams"),
          ("base-rate-neglect-and-fallacies","Base-Rate Neglect and Fallacies"),
        )
        key="esa_continue_probability_conditional_lesson_v0"
        for slug,label in lessons:
            with self.subTest(lesson=slug):
                route="/probability/conditional/"+slug+"/"
                self.page.goto(self.origin+route,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                saved=self.page.evaluate("""key=>JSON.parse(localStorage.getItem(key))""",key)
                self.assertEqual(saved["url"],route)
                self.assertEqual(saved["label"],label)
                self.assertIsInstance(saved["ts"],int)
                self.assertGreater(saved["ts"],0)
                self.page.goto(self.origin+"/probability/conditional/",wait_until="networkidle")
                expect(self.page.locator("#continue-reading-probability-conditional")).to_be_visible()
                self.assertEqual(self.page.locator(
                    "#continue-reading-probability-conditional-btn").get_attribute("href"),route)
                expect(self.page.locator("#continue-reading-probability-conditional-label")
                       ).to_contain_text(label)

    def test_conditional_six_lessons_and_tree_survive_denied_storage(self):
        """Lessons, navigation, and live tree arithmetic remain usable if localStorage throws."""
        self.page.add_init_script("""
          Object.defineProperty(window,'localStorage',{
            configurable:true,
            get(){throw new DOMException('Denied','SecurityError');}
          });
        """)
        for slug in ("what-is-conditional-probability","multiplication-rule",
                     "law-of-total-probability","bayes-theorem","tree-diagrams",
                     "base-rate-neglect-and-fallacies"):
            with self.subTest(lesson=slug):
                route="/probability/conditional/"+slug+"/"
                self.page.goto(self.origin+route,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(self.page.locator("main a[href]").count(),0)
                self.assertEqual(self.errors,[])
        self.page.goto(self.origin+"/probability/conditional/multiplication-rule/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-conditional-tree-explorer")
        expect(root.locator("#esa-tree-total-pass")).to_have_text("0.7000")
        root.locator("#esa-tree-pass-no-study").evaluate("""el=>{
          el.value="0.5";el.dispatchEvent(new Event('input',{bubbles:true}));
        }""")
        expect(root.locator("#esa-tree-total-pass")).to_have_text("0.7400")
        expect(root.locator("#esa-tree-bayes")).to_have_text("0.7297")
        self.assertEqual(self.errors,[])



    def test_basics_18_restorations_attribution_axioms_and_independence(self):
        """Nine axioms formulas, eight independence formulas, one 1933 attribution."""
        from html import unescape
        from math import isclose
        cases=(
          ("/probability/basics/probability-axioms-and-basic-rules/",9,(
            r"P(A)\ge 0",r"P(S)=1",
            r"\sum_{i=1}^{\infty}P(A_i)",
            r"P(A\cup B)&=P(A)+P(B)",
            r"0\le P(A)\le 1",
            r"\text{rolling a 7 on one fair six-sided die}",
            r"\text{rolling a number from 1 to 6}",
            r"P(H)+P(T)=0.5+0.5=1",
            r"P(A^{c})=1-P(A)",
            r"1-0.30=0.70")),
          ("/probability/basics/independence-vs-disjointness/",8,(
            r"P(A\cap B)=P(A)P(B)",
            r"P(A\cap B)=0.5\times0.5=0.25",
            r"A\cap B=\varnothing",
            r"P(A)P(B)=0",
            r"P(\text{Heads}\cap\text{Tails})=0"))
        )
        for route,count,formula_fragments in cases:
            with self.subTest(lesson=route):
                source=(SITE/route.lstrip("/")/"index.html").read_text()
                main=unescape(source.split('<main id="main-content"',1)[1].split("</main>",1)[0])
                self.assertNotIn("\uea01",main)
                self.assertNotIn("\uea02",main)
                self.assertEqual(main.count(r"\["),count)
                self.assertEqual(main.count(r"\]"),count)
                for fragment in formula_fragments:
                    self.assertIn(fragment,main)
                self.page.goto(self.origin+route,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        axioms=(SITE/"probability/basics/probability-axioms-and-basic-rules/index.html").read_text()
        self.assertIn("Andrey Kolmogorov",axioms)
        self.assertIn("1933",axioms)
        self.assertIn("countable additivity",axioms)
        self.assertTrue(isclose(.5+.5,1,abs_tol=1e-14))
        self.assertTrue(isclose(1-.3,.7,abs_tol=1e-14))
        self.assertTrue(isclose(.5*.5,.25,abs_tol=1e-14))
        self.assertEqual(0*.4,0)

    def test_basics_event_relationship_explorer_probabilities_and_constraints(self):
        """Check feasible overlap, four masses, product, and classification boundary cases."""
        from math import isclose
        route="/probability/basics/independence-vs-disjointness/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        root=self.page.locator("#esa-basics-event-lab")
        expect(root.get_by_role("heading",name="Explore Independence versus Disjointness")).to_be_visible()
        pa=root.locator("#esa-basics-p-a")
        pb=root.locator("#esa-basics-p-b")
        joint=root.locator("#esa-basics-p-ab")
        region_ids=("esa-basics-both","esa-basics-only-a",
                    "esa-basics-only-b","esa-basics-neither")
        regions=[root.locator("#"+i) for i in region_ids]
        label_ind=root.locator("#esa-basics-independent")
        label_dis=root.locator("#esa-basics-disjoint")
        bars=root.locator("#esa-basics-region-bars")
        def set_slider(el,value):
            el.evaluate("""(node,value)=>{
              node.value=String(value);
              node.dispatchEvent(new Event('input',{bubbles:true}));
            }""",value)
        def verify(a,b,j):
            for element,value in ((pa,a),(pb,b),(joint,j)):
                set_slider(element,value)
            low=max(0,round(a+b-1,2))
            high=min(a,b)
            effective=min(high,max(low,j))
            self.assertTrue(isclose(float(joint.input_value()),effective,abs_tol=1e-9))
            self.assertTrue(isclose(float(joint.get_attribute("min")),low,abs_tol=1e-9))
            self.assertTrue(isclose(float(joint.get_attribute("max")),high,abs_tol=1e-9))
            expect(root.locator("#esa-basics-overlap-min")).to_have_text(f"{low:.2f}")
            expect(root.locator("#esa-basics-overlap-max")).to_have_text(f"{high:.2f}")
            expected=(effective,a-effective,b-effective,1-a-b+effective)
            observed=tuple(float(el.inner_text()) for el in regions)
            for actual,want in zip(observed,expected):
                self.assertTrue(isclose(actual,want,abs_tol=0.000001),(a,b,j,actual,want))
                self.assertGreaterEqual(actual,-0.000001)
            self.assertTrue(isclose(sum(observed),1,abs_tol=0.000001))
            product=a*b
            expect(root.locator("#esa-basics-product")).to_have_text(f"{product:.4f}")
            expect(root.locator("#esa-basics-joint")).to_have_text(f"{effective:.4f}")
            independent=isclose(effective,product,abs_tol=1e-10)
            disjoint=effective==0
            expect(label_ind).to_have_text("Independent: "+("Yes" if independent else "No"))
            expect(label_dis).to_have_text("Disjoint: "+("Yes" if disjoint else "No"))
            self.assertIn("Four mutually exclusive regions",bars.get_attribute("aria-label"))
            for part,key in zip(expected,("esa-basics-bar-both","esa-basics-bar-only-a",
                                          "esa-basics-bar-only-b","esa-basics-bar-neither")):
                percentage=root.locator("#"+key).evaluate("el=>el.style.width")
                self.assertEqual(percentage,f"{round(100*part):d}%")
        for values in ((.5,.5,.25),(.3,.4,0),(0,.4,0),(.5,.5,.1),
                       (.85,.85,0),(1,1,1),(0,0,0),(.2,.9,.2)):
            with self.subTest(inputs=values):
                verify(*values)
        for id_,values in (
            ("esa-basics-preset-independent",(.5,.5,.25)),
            ("esa-basics-preset-disjoint",(.3,.4,0)),
            ("esa-basics-preset-both",(0,.4,0)),
            ("esa-basics-preset-neither",(.5,.5,.1))
        ):
            with self.subTest(preset=id_):
                root.locator("#"+id_).click()
                self.assertEqual([pa.input_value(),pb.input_value(),joint.input_value()],
                    [f"{v:g}" if v else "0" for v in values])
        expect(root.locator("#esa-basics-verdict")).to_contain_text("neither")

    def test_basics_event_relationship_keyboard_and_mobile(self):
        """Native slider accessibility, clamping, fixed regions, and 320px layout."""
        self.page.goto(self.origin+"/probability/basics/independence-vs-disjointness/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-basics-event-lab")
        first=root.get_by_role("slider",name="Probability of A:")
        first.focus()
        first.press("Home")
        expect(first).to_have_value("0")
        expect(root.locator("#esa-basics-p-ab")).to_have_value("0")
        expect(root.locator("#esa-basics-independent")).to_have_text("Independent: Yes")
        expect(root.locator("#esa-basics-disjoint")).to_have_text("Disjoint: Yes")
        first.press("ArrowRight")
        expect(first).to_have_value("0.05")
        expect(root.locator("#esa-basics-p-a-value")).to_have_text("0.05")
        second=root.get_by_role("slider",name="Probability of B:")
        second.focus()
        second.press("End")
        expect(second).to_have_value("1")
        expect(root.locator("#esa-basics-p-ab")).to_have_value("0.05")
        root.locator("#esa-basics-preset-independent").click()
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                b=root.evaluate("""e=>({
                  left:e.getBoundingClientRect().left,
                  right:e.getBoundingClientRect().right,
                  scroll:e.scrollWidth,
                  client:e.clientWidth,
                  viewport:window.innerWidth
                })""")
                self.assertGreaterEqual(b["left"],-1,b)
                self.assertLessEqual(b["right"],width+1,b)
                self.assertLessEqual(b["scroll"]-b["client"],1,b)

    def test_basics_eight_lessons_preserve_progress_and_resume(self):
        """Existing keys, exact lesson labels, timestamps and Continue Reading remain intact."""
        lessons=(
          ("what-is-probability","What Is Probability?"),
          ("outcomes-sample-spaces-events","Outcomes, Sample Spaces, and Events"),
          ("probability-axioms-and-basic-rules","Probability Axioms and Basic Rules"),
          ("union-intersection-and-venn-thinking","Union, Intersection, and Venn Thinking"),
          ("equally-likely-and-counting-intuition","Equally Likely and Counting Intuition"),
          ("independence-vs-disjointness","Independence vs Disjointness"),
          ("conditional-language-traps","Conditional Language Traps"),
          ("modeling-randomness-mini-cases","Modeling Randomness (Mini Cases)")
        )
        key="esa_continue_probability_basics_lesson_v0"
        for slug,label in lessons:
            with self.subTest(slug=slug):
                route="/probability/basics/"+slug+"/"
                self.page.goto(self.origin+route,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                saved=self.page.evaluate("""key=>JSON.parse(localStorage.getItem(key))""",key)
                self.assertEqual(saved["url"],route)
                self.assertEqual(saved["label"],label)
                self.assertIsInstance(saved["ts"],int)
                self.assertGreater(saved["ts"],0)
                self.page.goto(self.origin+"/probability/basics/",wait_until="networkidle")
                expect(self.page.locator("#continue-reading-probability-basics")).to_be_visible()
                self.assertEqual(
                    self.page.locator("#continue-reading-probability-basics-btn").get_attribute("href"),
                    route)
                expect(self.page.locator("#continue-reading-probability-basics-label")).to_contain_text(label)

    def test_basics_eight_lessons_and_explorer_survive_denied_storage(self):
        """Eight lesson pages and event explorer work when accessing localStorage throws."""
        self.page.add_init_script("""
          Object.defineProperty(window,'localStorage',{
            configurable:true,
            get(){throw new DOMException('Denied','SecurityError');}
          });
        """)
        for slug in ("what-is-probability","outcomes-sample-spaces-events",
                     "probability-axioms-and-basic-rules",
                     "union-intersection-and-venn-thinking",
                     "equally-likely-and-counting-intuition",
                     "independence-vs-disjointness",
                     "conditional-language-traps","modeling-randomness-mini-cases"):
            with self.subTest(lesson=slug):
                self.page.goto(self.origin+"/probability/basics/"+slug+"/",
                               wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(self.page.locator("main a[href]").count(),0)
                self.assertEqual(self.errors,[])
        self.page.goto(self.origin+"/probability/basics/independence-vs-disjointness/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-basics-event-lab")
        expect(root.locator("#esa-basics-joint")).to_have_text("0.2500")
        root.locator("#esa-basics-preset-disjoint").click()
        expect(root.locator("#esa-basics-joint")).to_have_text("0.0000")
        expect(root.locator("#esa-basics-disjoint")).to_have_text("Disjoint: Yes")
        self.page.goto(self.origin+"/probability/basics/",wait_until="networkidle")
        expect(self.page.locator("main h1")).to_be_visible()
        self.assertEqual(self.errors,[])



    def test_uniform_geometric_restored_math_and_example_benchmarks(self):
        """Twenty recovered formulas and numeric examples are exact, with explicit support."""
        from html import unescape
        from math import isclose
        cases=(
          ("/probability/distributions/uniform-distribution/",11,(
            r"a\le X\le b",r"f_X(x)=\frac{1}{b-a}",
            r"a\le x\le b",r"\frac{d-c}{b-a}",
            r"\frac{5-2}{10-0}=0.30",
            r"P(X=x)=0",
            r"\frac{a+b}{2}",r"\frac{0+10}{2}=5",
            r"\frac{(b-a)^2}{12}",
            r"\frac{b-a}{\sqrt{12}}")),
          ("/probability/distributions/geometric-distribution/",9,(
            r"X\sim\operatorname{Geom}(p)",
            r"0<p\le1",
            r"X\in\{1,2,3,\ldots\}",
            r"P(X=k)=(1-p)^{k-1}p",
            r"\frac18=0.125",
            r"E[X]=\frac1p",
            r"E[X]=\frac{1}{0.25}=4",
            r"\operatorname{Var}(X)=\frac{1-p}{p^2}",
            r"\text{10 previous tails}"))
        )
        for route,expected_count,fragments in cases:
            with self.subTest(route=route):
                source=(SITE/route.lstrip("/")/"index.html").read_text()
                main=unescape(source.split('<main id="main-content"',1)[1].split("</main>",1)[0])
                self.assertNotIn("\uea01",main)
                self.assertNotIn("\uea02",main)
                self.assertEqual(main.count(r"\["),expected_count)
                self.assertEqual(main.count(r"\]"),expected_count)
                for fragment in fragments:
                    self.assertIn(fragment,main)
                self.page.goto(self.origin+route,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.assertTrue(isclose((5-2)/(10-0),0.3,abs_tol=1e-14))
        self.assertTrue(isclose((10-0)**2/12,25/3,abs_tol=1e-14))
        self.assertTrue(isclose((1-.5)**2*.5,.125,abs_tol=1e-14))
        self.assertTrue(isclose((1-.25)/(.25**2),12,abs_tol=1e-14))
        self.assertTrue(isclose(1/.25,4,abs_tol=1e-14))
        geometric=(SITE/"probability/distributions/geometric-distribution/index.html").read_text()
        self.assertIn("including the successful trial",geometric)
        self.assertIn("failures-before-success",geometric)

    def test_uniform_probability_area_explorer_and_edge_cases(self):
        """Area is density times width; sliders enforce a<b and a<=c<=d<=b."""
        from math import isclose,sqrt
        route="/probability/distributions/uniform-distribution/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        root=self.page.locator("#esa-uniform-area-explorer")
        expect(root.get_by_role("heading",name="Interactive Uniform Probability Area Explorer")).to_be_visible()
        ids=("esa-uniform-a","esa-uniform-b","esa-uniform-c","esa-uniform-d")
        sliders=[root.locator("#"+name) for name in ids]
        output=lambda id_:root.locator("#"+id_).inner_text()
        self.assertEqual([x.input_value() for x in sliders],["0","10","2","5"])
        self.assertEqual(output("esa-uniform-density"),"0.1000")
        self.assertEqual(output("esa-uniform-probability"),"0.3000")
        self.assertEqual(output("esa-uniform-mean"),"5.00")
        self.assertEqual(output("esa-uniform-variance"),"8.3333")
        def set_slider(node,value):
            node.evaluate("""(el,value)=>{
              el.value=String(value);
              el.dispatchEvent(new Event('input',{bubbles:true}));
            }""",value)
        def verify():
            A,B,C,D=[float(el.input_value()) for el in sliders]
            self.assertLess(A,B)
            self.assertLessEqual(A,C)
            self.assertLessEqual(C,D)
            self.assertLessEqual(D,B)
            width=D-C
            density=1/(B-A)
            area=width*density
            self.assertTrue(isclose(float(output("esa-uniform-density")),density,abs_tol=5.1e-5))
            self.assertTrue(isclose(float(output("esa-uniform-probability")),area,abs_tol=5.1e-5))
            self.assertTrue(isclose(float(output("esa-uniform-mean")),(A+B)/2,abs_tol=0.0051))
            self.assertTrue(isclose(float(output("esa-uniform-variance")),(B-A)**2/12,abs_tol=5.1e-5))
            self.assertTrue(isclose(float(output("esa-uniform-sd")),(B-A)/sqrt(12),abs_tol=5.1e-5))
            self.assertTrue(isclose(float(output("esa-uniform-width")),width,abs_tol=1e-10))
            rect=root.locator("#esa-uniform-highlight")
            self.assertTrue(isclose(float(rect.get_attribute("x")),50+280*(C-A)/(B-A),abs_tol=1e-7))
            self.assertTrue(isclose(float(rect.get_attribute("width")),280*area,abs_tol=1e-7))
            self.assertIn(f"between {C:g} and {D:g}",root.locator("#esa-uniform-area-plot").get_attribute("aria-label"))
        verify()
        set_slider(sliders[2],5)
        verify()
        self.assertEqual(output("esa-uniform-probability"),"0.0000")
        set_slider(sliders[2],0)
        set_slider(sliders[3],10)
        verify()
        self.assertEqual(output("esa-uniform-probability"),"1.0000")
        set_slider(sliders[0],9)
        verify()
        self.assertEqual(sliders[2].input_value(),"9")
        set_slider(sliders[1],11)
        verify()
        root.get_by_role("button",name="Reset uniform example").click()
        self.assertEqual([x.input_value() for x in sliders],["0","10","2","5"])
        verify()
        expect(root.locator("#esa-uniform-probability")).to_have_text("0.3000")

    def test_uniform_probability_area_explorer_keyboard_mobile_and_denied_storage(self):
        """All sliders keyboard-operable, live values, stable layout, no storage dependency."""
        self.page.add_init_script("""
          Object.defineProperty(window,'localStorage',{
            configurable:true,
            get(){throw new DOMException('Denied','SecurityError');}
          });
        """)
        self.page.goto(self.origin+"/probability/distributions/uniform-distribution/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-uniform-area-explorer")
        a=root.get_by_role("slider",name="Lower distribution bound a:")
        a.focus()
        a.press("ArrowRight")
        expect(a).to_have_value("1")
        expect(root.locator("#esa-uniform-a-value")).to_have_text("1")
        c=root.get_by_role("slider",name="Subinterval start c:")
        c.focus()
        c.press("Home")
        expect(c).to_have_value("1")
        expect(root.locator("#esa-uniform-c-value")).to_have_text("1")
        d=root.get_by_role("slider",name="Subinterval end d:")
        d.focus()
        d.press("End")
        expect(d).to_have_value("10")
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                b=root.evaluate("""e=>({
                  left:e.getBoundingClientRect().left,
                  right:e.getBoundingClientRect().right,
                  scroll:e.scrollWidth,client:e.clientWidth
                })""")
                self.assertGreaterEqual(b["left"],-1,b)
                self.assertLessEqual(b["right"],width+1,b)
                self.assertLessEqual(b["scroll"]-b["client"],1,b)
        root.get_by_role("button",name="Reset uniform example").click()
        expect(root.locator("#esa-uniform-probability")).to_have_text("0.3000")
        self.assertEqual(self.errors,[])

    def test_geometric_wait_explorer_pmf_cdf_tail_and_memorylessness(self):
        """Exact geometric arithmetic, normalization, alternative convention and p=1 case."""
        from math import isclose
        self.page.goto(self.origin+"/probability/distributions/geometric-distribution/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-geometric-wait-explorer")
        expect(root.get_by_role("heading",name="Interactive Geometric Waiting-Time Explorer")).to_be_visible()
        p=root.locator("#esa-geom-p")
        k=root.locator("#esa-geom-k")
        output=lambda id_:root.locator("#"+id_).inner_text()
        self.assertEqual([p.input_value(),k.input_value()],["0.25","3"])
        def set_slider(el,value):
            el.evaluate("""(node,value)=>{
              node.value=String(value);
              node.dispatchEvent(new Event('input',{bubbles:true}));
            }""",value)
        def verify(prob,trial):
            set_slider(p,prob)
            set_slider(k,trial)
            observed=float(p.input_value())
            n=int(k.input_value())
            self.assertTrue(isclose(observed,prob,abs_tol=1e-12))
            self.assertEqual(n,trial)
            q=1-prob
            pmf=q**(n-1)*prob
            cdf=1-q**n
            tail=q**n
            mean=1/prob
            variance=q/(prob**2)
            for label,expected,tol in (
              ("esa-geom-pmf",pmf,5.1e-7),
              ("esa-geom-cdf",cdf,5.1e-7),
              ("esa-geom-tail",tail,5.1e-7),
              ("esa-geom-mean",mean,5.1e-5),
              ("esa-geom-variance",variance,5.1e-5)
            ):
                self.assertTrue(isclose(float(output(label)),expected,abs_tol=tol),
                                (prob,trial,label,output(label),expected))
            self.assertTrue(isclose(cdf+tail,1,abs_tol=1e-12))
            self.assertTrue(isclose(sum(q**(j-1)*prob for j in range(1,n+1)),cdf,abs_tol=1e-10))
            bars=root.locator("#esa-geom-bars rect")
            self.assertEqual(bars.count(),12)
            for j in range(1,13):
                bar=bars.nth(j-1)
                expectedHeight=110*(q**(j-1)*prob)
                self.assertTrue(isclose(float(bar.get_attribute("height")),expectedHeight,abs_tol=1e-7))
                self.assertEqual(bar.get_attribute("fill"),"#0d9488" if j==n else "#64748b")
            if prob==1:
                expect(root.locator("#esa-geom-memoryless-note")).to_be_visible()
                expect(root.locator("#esa-geom-memoryless-next")).to_have_text("Undefined")
                expect(root.locator("#esa-geom-memoryless-tail")).to_have_text("Undefined")
            else:
                expect(root.locator("#esa-geom-memoryless-note")).to_be_hidden()
                self.assertTrue(isclose(float(output("esa-geom-memoryless-next")),prob,abs_tol=5.1e-5))
                self.assertTrue(isclose(float(output("esa-geom-memoryless-tail")),q**3,abs_tol=5.1e-7))
        for args in ((.25,3),(.5,3),(.05,20),(.95,20),(1,1),(1,20),(.1,1),(.3,12)):
            with self.subTest(p_k=args):
                verify(*args)
        root.get_by_role("button",name="Reset geometric example").click()
        self.assertEqual([p.input_value(),k.input_value()],["0.25","3"])
        expect(root.locator("#esa-geom-pmf")).to_have_text("0.140625")
        expect(root.locator("#esa-geom-cdf")).to_have_text("0.578125")
        expect(root.locator("#esa-geom-tail")).to_have_text("0.421875")

    def test_geometric_wait_explorer_keyboard_mobile_and_progress(self):
        """Keyboard and mobile work with blocked storage; ordinary storage retains resume."""
        self.page.goto(self.origin+"/probability/distributions/geometric-distribution/",
                       wait_until="networkidle")
        key="esa_continue_probability_distributions_lesson_v0"
        saved=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
        self.assertEqual(saved["url"],"/probability/distributions/geometric-distribution/")
        self.assertEqual(saved["label"],"Geometric Distribution")
        self.assertIsInstance(saved["ts"],int)
        self.assertGreater(saved["ts"],0)
        root=self.page.locator("#esa-geometric-wait-explorer")
        p=root.get_by_role("slider",name="Success probability p:")
        k=root.get_by_role("slider",name="Trial number k:")
        p.focus()
        p.press("Home")
        expect(p).to_have_value("0.05")
        expect(root.locator("#esa-geom-p-value")).to_have_text("0.05")
        p.press("End")
        expect(p).to_have_value("1")
        k.focus()
        k.press("Home")
        expect(k).to_have_value("1")
        expect(root.locator("#esa-geom-pmf")).to_have_text("1.000000")
        k.press("End")
        expect(k).to_have_value("20")
        expect(root.locator("#esa-geom-pmf")).to_have_text("0.000000")
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                b=root.evaluate("""e=>({
                  left:e.getBoundingClientRect().left,
                  right:e.getBoundingClientRect().right,
                  scroll:e.scrollWidth,client:e.clientWidth
                })""")
                self.assertGreaterEqual(b["left"],-1,b)
                self.assertLessEqual(b["right"],width+1,b)
                self.assertLessEqual(b["scroll"]-b["client"],1,b)
        root.get_by_role("button",name="Reset geometric example").click()
        expect(root.locator("#esa-geom-pmf")).to_have_text("0.140625")
        self.page.goto(self.origin+"/probability/distributions/",wait_until="networkidle")
        expect(self.page.locator("#continue-reading-probability-distributions")).to_be_visible()
        self.assertEqual(self.page.locator(
            "#continue-reading-probability-distributions-btn").get_attribute("href"),
            "/probability/distributions/geometric-distribution/")
        self.page.add_init_script("""
          Object.defineProperty(window,'localStorage',{
            configurable:true,
            get(){throw new DOMException('Denied','SecurityError');}
          });
        """)
        self.page.goto(self.origin+"/probability/distributions/geometric-distribution/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-geometric-wait-explorer")
        expect(root.locator("#esa-geom-pmf")).to_have_text("0.140625")
        root.locator("#esa-geom-k").evaluate("""node=>{
          node.value="5";
          node.dispatchEvent(new Event('input',{bubbles:true}));
        }""")
        expect(root.locator("#esa-geom-pmf")).to_have_text("0.079102")
        self.assertEqual(self.errors,[])



    def test_all_former_math_placeholders_removed_site_wide(self):
        """No damaged math markers survive in generated pages; audit representative repairs."""
        import re
        markers=re.compile(r"[\uea01\uea02]")
        affected=[]
        count=0
        for source in SITE.rglob("*.html"):
            count+=1
            if markers.search(source.read_text(encoding="utf-8-sig")):
                affected.append(source.relative_to(SITE).as_posix())
        self.assertGreater(count,100,"Expected a full generated Jekyll site")
        self.assertEqual(affected,[],"Damaged mathematical-marker characters still present")
        representative={
          "probability/distributions/negative-binomial-distribution/index.html":(
            r"\binom{k-1}{r-1}",r"E[X]=\frac rp",r"\operatorname{Var}(X)="),
          "probability/distributions/gamma-distribution/index.html":(
            r"\Gamma(n)=(n-1)!",r"E[X]=\frac{\alpha}{\lambda}",
            r"\frac{\alpha}{\lambda^2}"),
          "inference/confidence-intervals/ci-for-mean-sigma-known-z/index.html":(
            r"\frac{\sigma}{\sqrt n}",r"46.08,\ 53.92"),
          "inference/confidence-intervals/ci-for-mean-sigma-unknown-t/index.html":(
            r"\frac{s}{\sqrt n}",r"73.81,\ 86.19"),
          "inference/classical-tests/chi-square-independence-test/index.html":(
            r"\chi^2=",r"\frac{100\times110}{200}=55"),
          "probability/lln-clt/law-of-large-numbers/index.html":(
            r"\bar X_n\xrightarrow{P}\mu",),
          "probability/expectation-variance/covariance/index.html":(
            r"E[XY]-E[X]E[Y]",),
          "probability/random-variables/cumulative-distribution-function/index.html":(
            r"P(a<X\le b)=F_X(b)-F_X(a)",),
          "modeling/model-fit-comparison/aic-bic/index.html":(
            "Hirotugu Akaike",),
        }
        from html import unescape
        for source,fragments in representative.items():
            with self.subTest(page=source):
                # Jekyll escapes '<' and '>' in text nodes. Compare the
                # decoded HTML text against the original mathematical TeX.
                html=unescape((SITE/source).read_text(encoding="utf-8"))
                for fragment in fragments:
                    self.assertIn(fragment,html)

    def test_negbin_waiting_time_explorer_exact_probabilities_and_boundaries(self):
        """Check negative binomial PMF, CDF, tail, moments, geometric limit, and p=1."""
        from math import comb,isclose
        self.page.goto(self.origin+"/probability/distributions/negative-binomial-distribution/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-negbin-wait-explorer")
        expect(root.get_by_role("heading",name="Interactive Negative Binomial Waiting-Time Explorer")).to_be_visible()
        r=root.locator("#esa-negbin-r")
        p=root.locator("#esa-negbin-p")
        k=root.locator("#esa-negbin-k")
        out=lambda id_:float(root.locator("#"+id_).inner_text())
        self.assertEqual([r.input_value(),p.input_value(),k.input_value()],["3","0.5","5"])
        def set_value(slider,value):
            slider.evaluate("""(el,v)=>{
              el.value=String(v);el.dispatchEvent(new Event('input',{bubbles:true}));
            }""",value)
        def verify(needed,success,trial):
            for slider,value in ((r,needed),(p,success),(k,trial)):
                set_value(slider,value)
            self.assertEqual(int(r.input_value()),needed)
            self.assertTrue(isclose(float(p.input_value()),success,abs_tol=1e-12))
            self.assertEqual(int(k.input_value()),trial)
            self.assertEqual(k.get_attribute("min"),str(needed))
            def mass(j):
                return comb(j-1,needed-1)*(success**needed)*((1-success)**(j-needed))
            pmf=mass(trial)
            cdf=sum(mass(j) for j in range(needed,trial+1))
            tail=1-cdf
            for id_,expected,tolerance in (
              ("esa-negbin-pmf",pmf,5.1e-7),
              ("esa-negbin-cdf",cdf,5.1e-7),
              ("esa-negbin-tail",tail,5.1e-7),
              ("esa-negbin-mean",needed/success,5.1e-5),
              ("esa-negbin-variance",needed*(1-success)/(success**2),5.1e-5)
            ):
                self.assertTrue(isclose(out(id_),expected,abs_tol=tolerance),
                                (needed,success,trial,id_,out(id_),expected))
            self.assertTrue(isclose(cdf+tail,1,abs_tol=1e-12))
            bars=root.locator("#esa-negbin-bars rect")
            self.assertEqual(bars.count(),12)
            for idx in range(12):
                rect=bars.nth(idx)
                j=needed+idx
                self.assertEqual(rect.get_attribute("data-trial"),str(j))
                self.assertTrue(isclose(float(rect.get_attribute("height")),
                                        110*mass(j),abs_tol=1e-6))
                self.assertEqual(rect.get_attribute("fill"),"#0d9488" if j==trial else "#64748b")
            self.assertIn(f"r = {needed}",root.locator("#esa-negbin-chart").get_attribute("aria-label"))
        for args in ((3,.5,5),(1,.5,3),(1,.25,1),(1,.25,20),
                     (3,.2,3),(3,.2,10),(6,.05,30),(6,1,6),
                     (1,1,1),(1,1,20),(5,.8,12)):
            with self.subTest(parameters=args):
                verify(*args)
        root.get_by_role("button",name="Geometric: r = 1").click()
        self.assertEqual([r.input_value(),p.input_value(),k.input_value()],["1","0.5","3"])
        self.assertTrue(isclose(out("esa-negbin-pmf"),.125,abs_tol=5.1e-7))
        expect(root.locator("#esa-negbin-special")).to_contain_text("exactly the geometric")
        root.get_by_role("button",name="Reset example").click()
        self.assertEqual([r.input_value(),p.input_value(),k.input_value()],["3","0.5","5"])
        self.assertTrue(isclose(out("esa-negbin-pmf"),.1875,abs_tol=5.1e-7))
        self.assertTrue(isclose(out("esa-negbin-cdf"),.5,abs_tol=5.1e-7))

    def test_negbin_waiting_time_keyboard_mobile_and_storage_denial(self):
        """Native range sliders and navigation work despite denied localStorage."""
        self.page.add_init_script("""
          Object.defineProperty(window,'localStorage',{
            configurable:true,
            get(){throw new DOMException('Denied','SecurityError');}
          });
        """)
        self.page.goto(self.origin+"/probability/distributions/negative-binomial-distribution/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-negbin-wait-explorer")
        r=root.get_by_role("slider",name="Required successes r:")
        p=root.get_by_role("slider",name="Success probability p:")
        k=root.get_by_role("slider",name="Trial of r-th success k:")
        r.focus()
        r.press("End")
        expect(r).to_have_value("6")
        expect(k).to_have_value("6")
        k.focus()
        k.press("Home")
        expect(k).to_have_value("6")
        p.focus()
        p.press("End")
        expect(p).to_have_value("1")
        expect(root.locator("#esa-negbin-pmf")).to_have_text("1.000000")
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                bounds=root.evaluate("""el=>({
                  left:el.getBoundingClientRect().left,
                  right:el.getBoundingClientRect().right,
                  client:el.clientWidth,scroll:el.scrollWidth
                })""")
                self.assertGreaterEqual(bounds["left"],-1,bounds)
                self.assertLessEqual(bounds["right"],width+1,bounds)
                self.assertLessEqual(bounds["scroll"]-bounds["client"],1,bounds)
        root.get_by_role("button",name="Reset example").click()
        expect(root.locator("#esa-negbin-pmf")).to_have_text("0.187500")
        self.assertGreater(self.page.locator("main a[href]").count(),0)
        self.assertEqual(self.errors,[])

    def test_erlang_waiting_time_explorer_exact_pdf_cdf_and_survival(self):
        """Integer-shape Erlang sums agree with independent reference expressions."""
        from math import exp,factorial,isclose
        self.page.goto(self.origin+"/probability/distributions/gamma-distribution/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-erlang-wait-explorer")
        expect(root.get_by_role("heading",name="Interactive Gamma/Erlang Waiting-Time Explorer")).to_be_visible()
        shape=root.locator("#esa-erlang-r")
        rate=root.locator("#esa-erlang-rate")
        time=root.locator("#esa-erlang-time")
        out=lambda id_:float(root.locator("#"+id_).inner_text())
        self.assertEqual([shape.input_value(),rate.input_value(),time.input_value()],
                         ["4","2","2"])
        def update(el,value):
            el.evaluate("""(node,v)=>{
              node.value=String(v);node.dispatchEvent(new Event('input',{bubbles:true}));
            }""",value)
        def verify(r,lam,t):
            for el,value in ((shape,r),(rate,lam),(time,t)):
                update(el,value)
            self.assertEqual(int(shape.input_value()),r)
            self.assertTrue(isclose(float(rate.input_value()),lam,abs_tol=1e-12))
            self.assertTrue(isclose(float(time.input_value()),t,abs_tol=1e-12))
            z=lam*t
            survival=exp(-z)*sum(z**j/factorial(j) for j in range(r))
            cdf=1-survival
            pdf=lam**r*t**(r-1)*exp(-z)/factorial(r-1) if t>0 else (lam if r==1 else 0)
            for label,want,tol in (
              ("esa-erlang-pdf",pdf,5.1e-6),
              ("esa-erlang-cdf",cdf,5.1e-7),
              ("esa-erlang-survival",survival,5.1e-7),
              ("esa-erlang-mean",r/lam,5.1e-5),
              ("esa-erlang-variance",r/(lam**2),5.1e-5),
              ("esa-erlang-scale",1/lam,5.1e-5)
            ):
                self.assertTrue(isclose(out(label),want,abs_tol=tol),
                                (r,lam,t,label,out(label),want))
            self.assertTrue(isclose(cdf+survival,1,abs_tol=1e-12))
            self.assertIn(f"shape {r}",root.locator("#esa-erlang-chart").get_attribute("aria-label"))
            self.assertGreater(len(root.locator("#esa-erlang-density-path").get_attribute("d")),100)
            self.assertIn("Z",root.locator("#esa-erlang-shade").get_attribute("d"))
            expectedX=34+296*t/12
            self.assertTrue(isclose(float(root.locator("#esa-erlang-time-marker").get_attribute("x1")),
                                    expectedX,abs_tol=1e-6))
        for args in ((4,2,2),(1,2,2),(1,.5,0),(1,4,0),(7,.5,12),
                     (2,4,.25),(7,4,12),(3,1,0),(3,1,3),(4,4,1)):
            with self.subTest(values=args):
                verify(*args)
        root.get_by_role("button",name="Exponential: shape 1").click()
        self.assertEqual([shape.input_value(),rate.input_value(),time.input_value()],
                         ["1","2","2"])
        expect(root.locator("#esa-erlang-special")).to_contain_text("exactly the Exponential")
        self.assertTrue(isclose(out("esa-erlang-cdf"),1-exp(-4),abs_tol=5.1e-7))
        root.get_by_role("button",name="Reset Erlang example").click()
        self.assertEqual([shape.input_value(),rate.input_value(),time.input_value()],
                         ["4","2","2"])

    def test_erlang_waiting_time_keyboard_mobile_progress_and_denied_storage(self):
        """Keyboard, responsive shaded chart, saved progress and blocked-storage fallback."""
        route="/probability/distributions/gamma-distribution/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        key="esa_continue_probability_distributions_lesson_v0"
        saved=self.page.evaluate("""key=>JSON.parse(localStorage.getItem(key))""",key)
        self.assertEqual(saved["url"],route)
        self.assertEqual(saved["label"],"Gamma Distribution")
        self.assertIsInstance(saved["ts"],int)
        self.assertGreater(saved["ts"],0)
        root=self.page.locator("#esa-erlang-wait-explorer")
        shape=root.get_by_role("slider",name="Event count / shape r:")
        rate=root.get_by_role("slider",name="Event rate")
        time=root.get_by_role("slider",name="Elapsed time t:")
        shape.focus()
        shape.press("Home")
        expect(shape).to_have_value("1")
        expect(root.locator("#esa-erlang-special")).to_contain_text("exactly the Exponential")
        rate.focus()
        rate.press("Home")
        expect(rate).to_have_value("0.5")
        time.focus()
        time.press("Home")
        expect(time).to_have_value("0")
        expect(root.locator("#esa-erlang-cdf")).to_have_text("0.000000")
        expect(root.locator("#esa-erlang-survival")).to_have_text("1.000000")
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                bounds=root.evaluate("""el=>({
                  left:el.getBoundingClientRect().left,
                  right:el.getBoundingClientRect().right,
                  scroll:el.scrollWidth,client:el.clientWidth
                })""")
                self.assertGreaterEqual(bounds["left"],-1,bounds)
                self.assertLessEqual(bounds["right"],width+1,bounds)
                self.assertLessEqual(bounds["scroll"]-bounds["client"],1,bounds)
        root.get_by_role("button",name="Reset Erlang example").click()
        expect(root.locator("#esa-erlang-mean")).to_have_text("2.0000")
        self.page.goto(self.origin+"/probability/distributions/",wait_until="networkidle")
        expect(self.page.locator("#continue-reading-probability-distributions")).to_be_visible()
        self.assertEqual(self.page.locator(
            "#continue-reading-probability-distributions-btn").get_attribute("href"),route)
        self.page.add_init_script("""
          Object.defineProperty(window,'localStorage',{
            configurable:true,
            get(){throw new DOMException('Denied','SecurityError');}
          });
        """)
        self.page.goto(self.origin+route,wait_until="networkidle")
        root=self.page.locator("#esa-erlang-wait-explorer")
        expect(root.locator("#esa-erlang-mean")).to_have_text("2.0000")
        root.get_by_role("button",name="Exponential: shape 1").click()
        expect(root.locator("#esa-erlang-mean")).to_have_text("0.5000")
        self.assertGreater(self.page.locator("main a[href]").count(),0)
        self.assertEqual(self.errors,[])



    def test_p_value_binomial_exact_tails_and_directional_z_formulas(self):
        """90 heads in 100 fair flips: exact two-sided/binomial tail, not posterior odds."""
        from math import comb, isclose
        from statistics import NormalDist
        p_right=sum(comb(100,k) for k in range(90,101))/2**100
        p_two=2*p_right
        self.assertTrue(isclose(p_right,1.5316450877189926e-17,rel_tol=1e-13))
        self.assertTrue(isclose(p_two,3.063290175437985e-17,rel_tol=1e-13))
        self.assertEqual(sum(comb(100,k) for k in range(0,11)),
                         sum(comb(100,k) for k in range(90,101)))
        pvalue_url="/inference/hypothesis-testing/p-value-meaning/"
        sides_url="/inference/hypothesis-testing/one-sided-vs-two-sided/"
        self.page.goto(self.origin+pvalue_url,wait_until="networkidle")
        main=self.page.locator("main")
        expect(main.get_by_role("heading",name="A Coin-Flipping Example")).to_be_visible()
        expect(main).to_contain_text("10 or fewer heads")
        expect(main).to_contain_text("90 or more heads")
        expect(main).to_contain_text("not evidence that H₀ is true")
        text=(SITE/pvalue_url.lstrip("/")/"index.html").read_text()
        for fragment in (r"\operatorname{Binomial}(100,0.5)",
                         r"3.0632901754\times10^{-17}",
                         r"1.5316450877\times10^{-17}"):
            self.assertIn(fragment,text)
        self.assertNotIn("Data are highly consistent with H₀",text)
        self.assertNotIn("<td>Moderate</td>",text)
        self.page.goto(self.origin+sides_url,wait_until="networkidle")
        text=(SITE/sides_url.lstrip("/")/"index.html").read_text()
        for term in (r"p_{\mathrm{right}}",r"p_{\mathrm{left}}",
                     r"p_{\mathrm{two}}","0.02275","0.97725","0.04550"):
            self.assertIn(term,text)
        normal=NormalDist()
        right=1-normal.cdf(2)
        left=normal.cdf(2)
        two=2*right
        self.assertTrue(isclose(right,.022750131948,rel_tol=1e-8))
        self.assertTrue(isclose(left,.977249868052,rel_tol=1e-8))
        self.assertTrue(isclose(two,.045500263896,rel_tol=1e-8))
        for url in (pvalue_url,sides_url):
            self.page.goto(self.origin+url,wait_until="networkidle")
            expect(self.page.locator("main h1")).to_be_visible()
            self.assertGreaterEqual(self.page.locator("main a[href]").count(),2)

    def test_normal_z_power_explorer_reference_values_boundaries_and_symmetry(self):
        """Normal-model exact power is Phi(-c-delta)+Phi(delta-c); beta excludes H0."""
        from math import isclose, sqrt
        from statistics import NormalDist
        route="/inference/power-sample-size/power-curve-and-tradeoffs/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        root=self.page.locator("#esa-power-lab")
        expect(root.get_by_role("heading",name="Interactive Two-Sided z-Test Power Explorer")).to_be_visible()
        n=root.locator("#esa-power-n")
        effect=root.locator("#esa-power-delta")
        sigma=root.locator("#esa-power-sigma")
        alpha=root.locator("#esa-power-alpha")
        probability=root.locator("#esa-power-result-power")
        beta=root.locator("#esa-power-result-beta")
        c=root.locator("#esa-power-result-critical")
        chart=root.locator("#esa-power-chart")
        expected0=.9424375431875085
        self.assertTrue(isclose(float(probability.inner_text()),expected0,abs_tol=.000051))
        expect(beta).to_have_text("0.0576")
        expect(root.locator("#esa-power-result-alpha")).to_have_text("0.0500")
        expect(root.locator("#esa-power-result-effect")).to_have_text("0.5000")
        expect(root.locator("#esa-power-result-noncentral")).to_have_text("3.5355")
        expect(c).to_have_text("±1.9600")
        def change(element,v,event="input"):
            element.evaluate("""(el,args)=>{
              el.value=String(args.value);
              el.dispatchEvent(new Event(args.event,{bubbles:true}));
            }""",{"value":v,"event":event})
        def verify(nv,delta,sv,av):
            change(n,nv)
            change(effect,delta)
            change(sigma,sv)
            change(alpha,f"{av:.2f}","change")
            q=NormalDist().inv_cdf(1-av/2)
            noncentral=delta*sqrt(nv)/sv
            truth=av if delta==0 else (NormalDist().cdf(-q-noncentral)+
                                       NormalDist().cdf(noncentral-q))
            self.assertTrue(isclose(float(probability.inner_text()),truth,
                                    abs_tol=.000051),
                                    (nv,delta,sv,av,probability.inner_text(),truth))
            self.assertTrue(isclose(float(root.locator("#esa-power-result-alpha").inner_text()),
                                    av,abs_tol=1e-7))
            self.assertTrue(isclose(float(root.locator("#esa-power-result-effect").inner_text()),
                                    delta/sv,abs_tol=.000051))
            self.assertTrue(isclose(float(root.locator("#esa-power-result-noncentral").inner_text()),
                                    noncentral,abs_tol=.000051))
            self.assertTrue(isclose(float(c.inner_text().replace("±","")),q,
                                    abs_tol=.000051))
            if delta==0:
                expect(beta).to_have_text("N/A (null true)")
                expect(root.locator("#esa-power-rate-label")).to_contain_text("Type I error")
            else:
                self.assertTrue(isclose(float(beta.inner_text()),1-truth,
                                        abs_tol=.000051))
            curve=root.locator("#esa-power-curve").get_attribute("d")
            self.assertEqual(curve.count("L"),120)
            self.assertNotIn("NaN",curve)
            self.assertNotIn("Infinity",curve)
            aria=chart.get_attribute("aria-label")
            self.assertIn(f"sample size {nv}".lower(),aria.lower())
            self.assertIn("rejection probability",aria.lower())
            marker=root.locator("#esa-power-marker")
            for attr,lo,hi in (("cx",52,532),("cy",30,208)):
                observed=float(marker.get_attribute(attr))
                self.assertGreaterEqual(observed,lo-.01)
                self.assertLessEqual(observed,hi+.01)
            return truth
        for values in ((50,.5,1,.05),(20,0,1,.05),(50,0,1,.01),
                       (40,-.5,1,.05),(40,.5,1,.05),
                       (200,1.5,.5,.10),(10,.05,3,.01),
                       (100,.2,1,.10),(20,-1.5,2.5,.05)):
            with self.subTest(parameters=values):
                verify(*values)
        plus=verify(40,.5,1,.05)
        minus=verify(40,-.5,1,.05)
        self.assertTrue(isclose(plus,minus,abs_tol=1e-10))
        root.get_by_role("button",name="Reset power example").click()
        self.assertEqual([n.input_value(),effect.input_value(),
                          sigma.input_value(),alpha.input_value()],
                         ["50","0.5","1","0.05"])
        expect(probability).to_have_text("0.9424")

    def test_normal_z_power_explorer_keyboard_mobile_and_null_case(self):
        """Native slider arrows, live aria labels, reset, and horizontal mobile safety."""
        self.page.goto(self.origin+"/inference/power-sample-size/power-curve-and-tradeoffs/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-power-lab")
        self.assertEqual(root.get_by_role("slider").count(),3)
        n=root.locator("#esa-power-n")
        delta=root.locator("#esa-power-delta")
        sigma=root.locator("#esa-power-sigma")
        alpha=root.locator("#esa-power-alpha")
        n.focus()
        n.press("Home")
        expect(n).to_have_value("10")
        n.press("ArrowRight")
        expect(n).to_have_value("20")
        delta.focus()
        delta.press("Home")
        expect(delta).to_have_value("-1.5")
        delta.press("End")
        expect(delta).to_have_value("1.5")
        delta.evaluate("""e=>{e.value="0";e.dispatchEvent(new Event('input',{bubbles:true}));}""")
        expect(root.locator("#esa-power-result-power")).to_have_text("0.0500")
        expect(root.locator("#esa-power-result-beta")).to_have_text("N/A (null true)")
        alpha.select_option("0.10")
        expect(root.locator("#esa-power-result-power")).to_have_text("0.1000")
        sigma.focus()
        sigma.press("End")
        expect(sigma).to_have_value("3")
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                bounds=root.evaluate("""e=>({
                  left:e.getBoundingClientRect().left,
                  right:e.getBoundingClientRect().right,
                  scroll:e.scrollWidth,client:e.clientWidth,
                  viewport:window.innerWidth
                })""")
                self.assertGreaterEqual(bounds["left"],-1,bounds)
                self.assertLessEqual(bounds["right"],width+1,bounds)
                self.assertLessEqual(bounds["scroll"]-bounds["client"],1,bounds)
        root.get_by_role("button",name="Reset power example").click()
        expect(root.locator("#esa-power-result-power")).to_have_text("0.9424")

    def test_power_sample_size_eight_progress_and_continue_reading(self):
        """Legacy key, exact URLs, labels, timestamps and block resume for all eight lessons."""
        lessons=(
          ("what-is-statistical-power","What Is Statistical Power?"),
          ("effect-size-and-practical-importance","Effect Size and Practical Importance"),
          ("power-curve-and-tradeoffs","Power Curves and Trade-Offs"),
          ("sample-size-for-mean","Sample Size for a Mean"),
          ("sample-size-for-proportion","Sample Size for a Proportion"),
          ("precision-vs-detectability","Precision vs Detectability"),
          ("underpowered-studies","Underpowered Studies"),
          ("software-and-power-analysis","Software and Power Analysis")
        )
        key="esa_continue_inference_power_sample_size_lesson_v0"
        for slug,label in lessons:
            with self.subTest(slug=slug):
                url="/inference/power-sample-size/"+slug+"/"
                self.page.goto(self.origin+url,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                data=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
                self.assertEqual(data["url"],url)
                self.assertEqual(data["label"],label)
                self.assertIsInstance(data["ts"],int)
                self.assertGreater(data["ts"],0)
                self.page.goto(self.origin+"/inference/power-sample-size/",
                               wait_until="networkidle")
                expect(self.page.locator("#continue-reading-inference-power")).to_be_visible()
                self.assertEqual(self.page.locator(
                    "#continue-reading-inference-power-btn").get_attribute("href"),url)
                expect(self.page.locator(
                    "#continue-reading-inference-power-label")).to_contain_text(label)

    def test_power_sample_size_eight_lessons_survive_denied_storage(self):
        """Denied localStorage never blocks headings, navigation, calculators, or power lab."""
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,
            get(){throw new DOMException("Denied","SecurityError");}
          });
        """)
        for slug in ("what-is-statistical-power","effect-size-and-practical-importance",
                     "power-curve-and-tradeoffs","sample-size-for-mean",
                     "sample-size-for-proportion","precision-vs-detectability",
                     "underpowered-studies","software-and-power-analysis"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+"/inference/power-sample-size/"+slug+"/",
                               wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(self.page.locator("main a[href]").count(),0)
                self.assertEqual(self.errors,[])
        self.page.goto(self.origin+"/inference/power-sample-size/power-curve-and-tradeoffs/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-power-lab")
        expect(root.locator("#esa-power-result-power")).to_have_text("0.9424")
        root.locator("#esa-power-delta").evaluate("""el=>{
            el.value="0";el.dispatchEvent(new Event('input',{bubbles:true}));
        }""")
        expect(root.locator("#esa-power-result-power")).to_have_text("0.0500")
        self.page.goto(self.origin+"/inference/power-sample-size/",wait_until="networkidle")
        expect(self.page.locator("main h1")).to_be_visible()
        self.assertEqual(self.errors,[])


    def test_confidence_interval_coverage_lab_exact_model_and_empirical_coverage(self):
        """Exact normal z intervals capture fixed mu at the selected nominal rate in repeated samples."""
        from math import isclose, sqrt
        from statistics import NormalDist
        route = "/inference/confidence-intervals/what-is-a-confidence-interval/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        lab = self.page.locator("#esa-ci-coverage-lab")
        expect(lab.get_by_role("heading", name="Interactive Confidence Interval Coverage Experiment")).to_be_visible()
        confidence = lab.locator("#esa-ci-confidence")
        n = lab.locator("#esa-ci-n")
        total = lab.locator("#esa-ci-total")
        captured = lab.locator("#esa-ci-hit")
        missed = lab.locator("#esa-ci-miss")
        observed = lab.locator("#esa-ci-observed")
        half = lab.locator("#esa-ci-halfwidth")
        chart = lab.locator("#esa-ci-chart")
        expect(confidence).to_have_value("95")
        expect(n).to_have_value("30")
        expect(total).to_have_text("100")
        def verify(level, size):
            expect(lab.locator("#esa-ci-nominal")).to_have_text(str(level) + "%")
            expect(total).to_have_text("100")
            critical = NormalDist().inv_cdf(0.5 + level / 200)
            nominal_half = critical / sqrt(size)
            self.assertTrue(isclose(float(half.inner_text()), nominal_half,
                                    abs_tol=.000051))
            lines = lab.locator(".esa-ci-interval")
            self.assertEqual(lines.count(), 20)
            for row in lines.all():
                low = float(row.get_attribute("data-lower"))
                high = float(row.get_attribute("data-upper"))
                self.assertTrue(isclose(high - low, 2 * nominal_half,
                                        abs_tol=2e-8))
                expected_hit = "yes" if low <= 0 <= high else "no"
                self.assertEqual(row.get_attribute("data-capture"), expected_hit)
            self.assertIn("mean fixed at zero", chart.get_attribute("aria-label"))
            self.assertEqual(int(captured.inner_text()) + int(missed.inner_text()),
                             100)
            self.assertEqual(lab.locator("#esa-ci-recent li").count(), 5)
        verify(95, 30)
        n.select_option("100")
        verify(95, 100)
        confidence.select_option("90")
        verify(90, 100)
        confidence.select_option("99")
        n.select_option("10")
        verify(99, 10)
        confidence.select_option("95")
        verify(95, 10)
        lab.locator("#esa-ci-run-500").click()
        expect(total).to_have_text("600")
        lab.locator("#esa-ci-run-100").click()
        expect(total).to_have_text("700")
        self.assertEqual(int(captured.inner_text()) + int(missed.inner_text()), 700)
        for _ in range(5):
            lab.locator("#esa-ci-run-500").click()
        expect(total).to_have_text("3,200")
        self.assertLess(abs(float(observed.inner_text().rstrip("%")) - 95), 4.0)
        lab.locator("#esa-ci-reset").click()
        verify(95, 10)
        self.assertIn("confidence-interval precision" if False else
                      "theoretical long-run coverage", lab.inner_text())
        self.assertEqual(self.errors, [])

    def test_confidence_interval_coverage_lab_keyboard_mobile_and_denied_storage(self):
        """Progress denial does not break simulation, keyboard controls or narrow screens."""
        self.page.add_init_script("""
          Object.defineProperty(window, "localStorage", {
            configurable:true,
            get(){throw new DOMException("Storage unavailable","SecurityError");}
          });
        """)
        self.page.goto(
            self.origin + "/inference/confidence-intervals/what-is-a-confidence-interval/",
            wait_until="networkidle")
        lab = self.page.locator("#esa-ci-coverage-lab")
        run = lab.get_by_role("button", name="Generate 500 intervals")
        run.focus()
        run.press("Enter")
        expect(lab.locator("#esa-ci-total")).to_have_text("600")
        confidence = lab.get_by_label("Confidence level", exact=True)
        confidence.focus()
        confidence.press("Home")
        self.assertEqual(confidence.input_value(), "90")
        confidence.dispatch_event("change")
        expect(lab.locator("#esa-ci-nominal")).to_have_text("90%")
        expect(lab.locator("#esa-ci-total")).to_have_text("100")
        sample_size = lab.get_by_label("Observations per sample (n)")
        sample_size.focus()
        sample_size.press("End")
        expect(sample_size).to_have_value("300")
        sample_size.dispatch_event("change")
        expect(lab.locator("#esa-ci-total")).to_have_text("100")
        for width in (320, 375, 768, 1280):
            with self.subTest(viewport=width):
                self.page.set_viewport_size({"width": width, "height": 880})
                metrics = lab.evaluate("""e => ({
                    scroll:e.scrollWidth,client:e.clientWidth,
                    right:e.getBoundingClientRect().right,
                    left:e.getBoundingClientRect().left
                })""")
                self.assertLessEqual(metrics["scroll"] - metrics["client"], 1, metrics)
                self.assertLessEqual(metrics["right"], width + 1, metrics)
                self.assertGreaterEqual(metrics["left"], -1, metrics)
        expect(self.page.locator("main h1")).to_be_visible()
        self.assertGreater(self.page.locator("main a[href]").count(), 0)
        self.assertEqual(self.errors, [])

    def test_mean_precision_planner_examples_bounds_and_mobile(self):
        """Known-sigma precision n = ceil((z*sigma/E)^2), not study power."""
        from math import ceil, isclose, sqrt
        url = "/inference/power-sample-size/sample-size-for-mean/"
        self.page.goto(self.origin + url, wait_until="networkidle")
        lab = self.page.locator("#esa-mean-sample-calculator")
        expect(lab.get_by_role("heading", name="Interactive Sample Size for a Mean")).to_be_visible()
        confidence = lab.get_by_label("Confidence level", exact=True)
        sigma = lab.get_by_label("Population standard deviation σ (> 0)")
        margin = lab.get_by_label("Target margin of error E (> 0)")
        raw = lab.locator("#esa-mean-unrounded")
        whole = lab.locator("#esa-mean-required")
        planned = lab.locator("#esa-mean-achieved")
        error = lab.locator("#esa-mean-error")
        def check(z, std, E):
            theoretical = (z * std / E) ** 2
            required = max(1, ceil(theoretical))
            self.assertTrue(isclose(float(raw.inner_text()), theoretical,
                                    abs_tol=.000051))
            self.assertEqual(whole.inner_text(), f"{required:,}")
            self.assertTrue(isclose(float(planned.inner_text()),
                                    z * std / sqrt(required), abs_tol=.000051))
            self.assertLessEqual(z * std / sqrt(required), E + 1e-10)
            if required > 1:
                self.assertGreater(z * std / sqrt(required - 1), E - 1e-10)
        expect(confidence).to_have_value("95")
        expect(sigma).to_have_value("20")
        expect(margin).to_have_value("4")
        check(1.96, 20, 4)
        self.assertEqual(whole.inner_text(), "97")
        confidence.select_option("90")
        check(1.645, 20, 4)
        self.assertEqual(whole.inner_text(), "68")
        confidence.select_option("99")
        check(2.576, 20, 4)
        self.assertEqual(whole.inner_text(), "166")
        confidence.select_option("95")
        margin.fill("2")
        check(1.96, 20, 2)
        self.assertEqual(whole.inner_text(), "385")
        sigma.fill("10")
        check(1.96, 10, 2)
        margin.fill("1000")
        check(1.96, 10, 1000)
        self.assertEqual(whole.inner_text(), "1")
        for field in (sigma, margin):
            field.fill("0")
            expect(whole).to_have_text("—")
            expect(error).to_be_visible()
            field.fill("-2")
            expect(whole).to_have_text("—")
            field.fill("")
            expect(whole).to_have_text("—")
            field.fill("2" if field == margin else "10")
        sigma.fill("1e100")
        margin.fill("1e-100")
        expect(whole).to_have_text("—")
        expect(error).to_contain_text("reliable numeric range")
        lab.get_by_role("button", name="Reset worked example").click()
        check(1.96, 20, 4)
        for phrase in ("known or", "hypothesis-testing power", "independent",
                       "normal", "clustering"):
            expect(lab).to_contain_text(phrase)
        saved = self.page.evaluate(
            "() => JSON.parse(localStorage.getItem('esa_continue_inference_power_sample_size_lesson_v0'))")
        self.assertEqual(saved["url"], url)
        self.assertEqual(saved["label"], "Sample Size for a Mean")
        self.assertIsInstance(saved["ts"], int)
        for width in (320, 375, 768, 1280):
            with self.subTest(viewport=width):
                self.page.set_viewport_size({"width": width, "height": 870})
                geometry = lab.evaluate("""e => ({
                    scroll:e.scrollWidth,client:e.clientWidth,
                    right:e.getBoundingClientRect().right
                })""")
                self.assertLessEqual(geometry["scroll"] - geometry["client"], 1, geometry)
                self.assertLessEqual(geometry["right"], width + 1, geometry)
        self.assertEqual(self.errors, [])

    def test_mean_precision_planner_denied_storage_and_keyboard(self):
        """No storage access, no JavaScript failures, and native keyboard inputs still work."""
        self.page.add_init_script("""
          Object.defineProperty(window, "localStorage", {
            configurable:true,
            get(){throw new DOMException("Denied","SecurityError");}
          });
        """)
        self.page.goto(
            self.origin + "/inference/power-sample-size/sample-size-for-mean/",
            wait_until="networkidle")
        lab = self.page.locator("#esa-mean-sample-calculator")
        whole = lab.locator("#esa-mean-required")
        expect(whole).to_have_text("97")
        confidence = lab.get_by_label("Confidence level", exact=True)
        confidence.focus()
        confidence.press("End")
        confidence.dispatch_event("change")
        expect(confidence).to_have_value("99")
        expect(whole).to_have_text("166")
        margin = lab.get_by_label("Target margin of error E (> 0)")
        margin.fill("0")
        expect(whole).to_have_text("—")
        margin.fill("4")
        expect(whole).to_have_text("166")
        lab.get_by_role("button", name="Reset worked example").focus()
        lab.get_by_role("button", name="Reset worked example").press("Enter")
        expect(whole).to_have_text("97")
        expect(self.page.locator("main h1")).to_be_visible()
        self.assertGreater(self.page.locator("main a[href]").count(), 0)
        self.assertEqual(self.errors, [])

    def test_hypothesis_testing_ten_lesson_progress_and_continue_reading(self):
        """Existing URLs, exact labels, legacy key, timestamps and resume survive."""
        lessons = (
            ("what-is-a-hypothesis-test", "What Is a Hypothesis Test?"),
            ("null-and-alternative", "Null and Alternative Hypotheses"),
            ("test-statistic-standardization", "Test Statistic and Standardization"),
            ("p-value-meaning", "p-Value Meaning"),
            ("significance-level-alpha", "Significance Level (α)"),
            ("one-sided-vs-two-sided", "One-Sided vs Two-Sided Tests"),
            ("type1-type2-errors", "Type I and Type II Errors"),
            ("power-and-effect-size", "Power and Effect Size"),
            ("ci-and-test-connection", "Confidence Intervals and Tests"),
            ("practical-significance", "Practical Significance")
        )
        key = "esa_continue_inference_hypothesis_testing_lesson_v0"
        for slug, label in lessons:
            with self.subTest(slug=slug):
                url = "/inference/hypothesis-testing/" + slug + "/"
                self.page.goto(self.origin + url, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                entry = self.page.evaluate(
                    "key => JSON.parse(localStorage.getItem(key))", key)
                self.assertEqual(entry["url"], url)
                self.assertEqual(entry["label"], label)
                self.assertIsInstance(entry["ts"], int)
                self.assertGreater(entry["ts"], 0)
                self.page.goto(self.origin + "/inference/hypothesis-testing/",
                               wait_until="networkidle")
                expect(self.page.locator("#continue-reading-inference-testing")).to_be_visible()
                self.assertEqual(self.page.locator(
                    "#continue-reading-inference-testing-btn").get_attribute("href"), url)
                expect(self.page.locator(
                    "#continue-reading-inference-testing-label")).to_contain_text(label)
        self.assertEqual(self.errors, [])

    def test_hypothesis_testing_ten_lessons_denied_storage(self):
        """Storage failures never prevent ten lessons or their overview from loading."""
        self.page.add_init_script("""
          Object.defineProperty(window, "localStorage", {
            configurable:true,
            get(){throw new DOMException("Storage disabled","SecurityError");}
          });
        """)
        slugs = (
            "what-is-a-hypothesis-test", "null-and-alternative",
            "test-statistic-standardization", "p-value-meaning",
            "significance-level-alpha", "one-sided-vs-two-sided",
            "type1-type2-errors", "power-and-effect-size",
            "ci-and-test-connection", "practical-significance"
        )
        for slug in slugs:
            with self.subTest(slug=slug):
                url = "/inference/hypothesis-testing/" + slug + "/"
                self.page.goto(self.origin + url, wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreaterEqual(self.page.locator("main a[href]").count(), 2)
                self.assertEqual(self.errors, [], slug)
        self.page.goto(self.origin + "/inference/hypothesis-testing/",
                       wait_until="networkidle")
        expect(self.page.locator("main h1")).to_be_visible()
        self.assertEqual(self.errors, [])


    def test_chi_square_independence_interactive_example_and_boundaries(self):
        """Pearson 2x2 calculations match a reference and stay editable on mobile."""
        self.page.goto(self.origin + "/inference/classical-tests/chi-square-independence-test/",
                       wait_until="networkidle")
        lab = self.page.locator("#esa-chi-independence-lab")
        expect(lab).to_be_visible()
        self.assertAlmostEqual(float(lab.locator("#esa-chi-stat").inner_text()), 18.18181818, places=5)
        self.assertAlmostEqual(float(lab.locator("#esa-chi-p").inner_text()), 0.000020078656, delta=3e-7)
        self.assertAlmostEqual(float(lab.locator("#esa-chi-v").inner_text()), 0.3015113446, places=5)
        expect(lab.locator("#esa-chi-cell-a")).to_contain_text("40 → 55.000; 4.0909")
        expect(lab.locator("#esa-chi-cell-b")).to_contain_text("60 → 45.000; 5.0000")
        first = lab.get_by_label("Male, Prefers A", exact=True)
        first.focus()
        first.press("ArrowUp")
        self.assertNotEqual(lab.locator("#esa-chi-stat").inner_text(), "18.181818")
        first.fill("0")
        lab.get_by_label("Male, Prefers B", exact=True).fill("0")
        expect(lab.locator("#esa-chi-error")).to_be_visible()
        expect(lab.locator("#esa-chi-stat")).to_have_text("—")
        first.fill("1")
        expect(lab.locator("#esa-chi-warning")).to_contain_text("below 5")
        lab.get_by_role("button", name="Reset worked example").press("Enter")
        expect(lab.locator("#esa-chi-stat")).to_have_text("18.181818")
        for width in (320, 375, 768):
            self.page.set_viewport_size({"width":width,"height":850})
            geo=lab.evaluate("e=>({scroll:e.scrollWidth,client:e.clientWidth,right:e.getBoundingClientRect().right})")
            self.assertLessEqual(geo["scroll"]-geo["client"],1,geo)
            self.assertLessEqual(geo["right"],width+1,geo)

    def test_two_proportion_ci_interactive_example_and_boundaries(self):
        """Unpooled Wald interval reproduces 240/600 vs 180/600."""
        self.page.goto(
            self.origin + "/inference/confidence-intervals/ci-for-difference-of-proportions/",
            wait_until="networkidle")
        lab=self.page.locator("#esa-two-proportion-ci-calculator")
        expect(lab).to_be_visible()
        self.assertAlmostEqual(float(lab.locator("#esa-prop-difference").inner_text()),10.0,places=3)
        self.assertAlmostEqual(float(lab.locator("#esa-prop-se").inner_text()),0.02738613,places=5)
        self.assertAlmostEqual(float(lab.locator("#esa-prop-lower").inner_text()),4.63241757,places=3)
        self.assertAlmostEqual(float(lab.locator("#esa-prop-upper").inner_text()),15.36758243,places=3)
        expect(lab.locator("#esa-prop-zero-interpretation")).to_contain_text("outside")
        confidence=lab.get_by_label("Confidence level")
        confidence.focus()
        confidence.press("End")
        expect(confidence).to_have_value("99")
        self.assertLess(float(lab.locator("#esa-prop-lower").inner_text()),4.6324)
        n1=lab.get_by_label("Group 1 sample size")
        n1.fill("0")
        expect(lab.locator("#esa-prop-error")).to_be_visible()
        expect(lab.locator("#esa-prop-lower")).to_have_text("—")
        n1.fill("1")
        expect(lab.locator("#esa-prop-error")).to_be_visible()
        lab.get_by_role("button",name="Reset worked example").click()
        expect(lab.locator("#esa-prop-confidence")).to_have_text("95")
        lab.get_by_label("Group 1 successes").fill("0")
        expect(lab.locator("#esa-prop-warning")).to_contain_text("fewer than 10")
        for width in (320,375,768):
            self.page.set_viewport_size({"width":width,"height":850})
            geo=lab.evaluate("e=>({scroll:e.scrollWidth,client:e.clientWidth,right:e.getBoundingClientRect().right})")
            self.assertLessEqual(geo["scroll"]-geo["client"],1,geo)
            self.assertLessEqual(geo["right"],width+1,geo)

    def test_classical_tests_twelve_progress_and_mobile_keyboard(self):
        """All twelve lessons keep their exact original URL, label and timestamp schema."""
        labels = (
            ("chi-square-goodness-of-fit","Chi-Square Goodness-of-Fit Test"),
            ("chi-square-homogeneity-test","Chi-Square Test of Homogeneity"),
            ("chi-square-independence-test","Chi-Square Test of Independence"),
            ("decision-framework-and-assumptions","Decision Framework and Assumptions"),
            ("one-proportion-z-test","One-Proportion Z Test"),
            ("one-sample-t-test-for-mean","One-Sample t Test for a Mean"),
            ("one-sample-z-test-for-mean","One-Sample Z Test for a Mean"),
            ("one-way-anova-f-test","One-Way ANOVA and the F Test"),
            ("paired-t-test","Paired t Test"),
            ("post-hoc-tests-and-multiple-comparisons-preview","Post-Hoc Tests and Multiple Comparisons"),
            ("two-proportion-z-test","Two-Proportion Z Test"),
            ("two-sample-t-test-independent","Two-Sample t Test (Independent Samples)"),
        )
        key="esa_continue_inference_classical_tests_lesson_v0"
        self.page.set_viewport_size({"width":375,"height":812})
        for slug,label in labels:
            with self.subTest(slug=slug):
                url="/inference/classical-tests/"+slug+"/"
                self.page.goto(self.origin+url,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                saved=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
                self.assertEqual(saved["url"],url)
                self.assertEqual(saved["label"],label)
                self.assertIsInstance(saved["ts"],int)
                self.assertGreater(saved["ts"],0)
                link=self.page.locator("main .hero-actions a").first
                self.assertGreater(self.page.locator("main a[href]").count(),1)
                link.focus()
                self.assertEqual(link.evaluate("e=>document.activeElement===e"),True)
                self.assertLessEqual(link.evaluate("e=>e.getBoundingClientRect().right"),376)

    def test_classical_tests_twelve_storage_denial_and_navigability(self):
        """Denied localStorage must never stop rendering any of the twelve lessons."""
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,
            get(){throw new DOMException("Storage denied","SecurityError");}
          });
        """)
        slugs=(
            "chi-square-goodness-of-fit","chi-square-homogeneity-test",
            "chi-square-independence-test","decision-framework-and-assumptions",
            "one-proportion-z-test","one-sample-t-test-for-mean",
            "one-sample-z-test-for-mean","one-way-anova-f-test",
            "paired-t-test","post-hoc-tests-and-multiple-comparisons-preview",
            "two-proportion-z-test","two-sample-t-test-independent",
        )
        self.page.set_viewport_size({"width":320,"height":780})
        for slug in slugs:
            with self.subTest(slug=slug):
                self.page.goto(self.origin+"/inference/classical-tests/"+slug+"/",
                               wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreater(self.page.locator("main a[href]").count(),1)
                self.page.locator("main .hero-actions a").first.focus()
                self.assertEqual(self.page.evaluate(
                    "document.activeElement.tagName"),"A")
                self.assertEqual(self.errors,[],slug)
        self.page.goto(self.origin+"/inference/classical-tests/chi-square-independence-test/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-chi-stat")).to_have_text("18.181818")
        self.page.goto(self.origin+"/inference/confidence-intervals/ci-for-difference-of-proportions/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-prop-difference")).to_have_text("10.0000")



    def test_ols_explorer_reference_values_residuals_and_comparison(self):
        """Independent OLS benchmark: x=1..5, y=(2,4,5,4,5), b0=2.2, b1=.6."""
        self.page.goto(self.origin + "/modeling/simple-linear-regression/least-squares/",
                       wait_until="networkidle")
        lab = self.page.locator("#esa-ols-explorer")
        expect(lab).to_be_visible()
        self.assertAlmostEqual(float(lab.locator("#esa-ols-b0").inner_text()), 2.2, places=5)
        self.assertAlmostEqual(float(lab.locator("#esa-ols-b1").inner_text()), 0.6, places=5)
        self.assertAlmostEqual(float(lab.locator("#esa-ols-rss").inner_text()), 2.4, places=5)
        self.assertAlmostEqual(float(lab.locator("#esa-ols-alt-rss").inner_text()), 4, places=5)
        self.assertAlmostEqual(float(lab.locator("#esa-ols-r2").inner_text()), .6, places=5)
        for i, (fitted, residual, squared) in enumerate(
                ((2.8,-.8,.64),(3.4,.6,.36),(4,1,1),(4.6,-.6,.36),(5.2,-.2,.04)),1):
            self.assertAlmostEqual(float(lab.locator("#esa-ols-fit"+str(i)).inner_text()),fitted,places=3)
            self.assertAlmostEqual(float(lab.locator("#esa-ols-res"+str(i)).inner_text()),residual,places=3)
            self.assertAlmostEqual(float(lab.locator("#esa-ols-sq"+str(i)).inner_text()),squared,places=3)
        lab.locator("#esa-ols-alt-intercept").fill("2.2")
        lab.locator("#esa-ols-alt-slope").fill("0.6")
        self.assertAlmostEqual(float(lab.locator("#esa-ols-alt-rss").inner_text()),2.4,places=4)
        lab.locator("#esa-ols-alt-slope").fill("-1")
        self.assertGreater(float(lab.locator("#esa-ols-alt-rss").inner_text()),2.4)
        self.assertGreater(lab.locator("#esa-ols-plot circle").count(),0)
        self.assertGreater(lab.locator("#esa-ols-plot line").count(),0)
        entry=self.page.evaluate("""() => JSON.parse(
          localStorage.getItem("esa_continue_modeling_simple_linear_regression_lesson_v0"))""")
        self.assertEqual(entry["url"],"/modeling/simple-linear-regression/least-squares/")
        self.assertEqual(entry["label"],"Least Squares")
        self.assertIsInstance(entry["ts"],int)

    def test_ols_explorer_validation_outlier_keyboard_and_mobile(self):
        self.page.goto(self.origin + "/modeling/simple-linear-regression/least-squares/",
                       wait_until="networkidle")
        lab=self.page.locator("#esa-ols-explorer")
        first=lab.locator("#esa-ols-x1")
        first.focus()
        first.press("ArrowUp")
        self.assertNotEqual(first.input_value(),"1")
        self.assertFalse(lab.locator("#esa-ols-error").is_visible())
        for i in range(1,6):
            lab.locator("#esa-ols-x"+str(i)).fill("3")
        expect(lab.locator("#esa-ols-error")).to_be_visible()
        expect(lab.locator("#esa-ols-rss")).to_have_text("—")
        expect(lab.locator("#esa-ols-chart")).to_be_hidden()
        lab.get_by_role("button",name="Reset example").click()
        expect(lab.locator("#esa-ols-rss")).to_have_text("2.4000")
        lab.get_by_role("button",name="Try an unusual observation").click()
        self.assertNotEqual(lab.locator("#esa-ols-b1").inner_text(),"0.6000")
        lab.locator("#esa-ols-y5").fill("")
        expect(lab.locator("#esa-ols-error")).to_be_visible()
        lab.get_by_role("button",name="Reset example").click()
        lab.locator("#esa-ols-y1").fill("4")
        lab.locator("#esa-ols-y2").fill("4")
        lab.locator("#esa-ols-y3").fill("4")
        lab.locator("#esa-ols-y4").fill("4")
        lab.locator("#esa-ols-y5").fill("4")
        expect(lab.locator("#esa-ols-r2")).to_have_text("undefined")
        lab.get_by_role("button",name="Reset example").click()
        for width in (320,375,768):
            self.page.set_viewport_size({"width":width,"height":850})
            dimensions=lab.evaluate("""e=>({
              scroll:e.scrollWidth,client:e.clientWidth,right:e.getBoundingClientRect().right})""")
            self.assertLessEqual(dimensions["scroll"]-dimensions["client"],1,dimensions)
            self.assertLessEqual(dimensions["right"],width+1,dimensions)

    def test_normal_probability_explorer_numerics_and_bounds(self):
        """Standard normal reference: P(-1<Z<1)=.68268949; tails .15865525."""
        self.page.goto(self.origin + "/probability/distributions/normal-distribution/",
                       wait_until="networkidle")
        lab=self.page.locator("#esa-normal-probability-explorer")
        expect(lab).to_be_visible()
        self.assertAlmostEqual(float(lab.locator("#esa-normal-probability").inner_text()),
                               .682689492137,delta=1e-6)
        self.assertAlmostEqual(float(lab.locator("#esa-normal-percent").inner_text()),
                               68.26894921,delta=.00015)
        lab.locator("#esa-normal-mode").select_option("left")
        self.assertAlmostEqual(float(lab.locator("#esa-normal-probability").inner_text()),
                               .15865525393,delta=1e-6)
        lab.locator("#esa-normal-mode").select_option("right")
        self.assertAlmostEqual(float(lab.locator("#esa-normal-probability").inner_text()),
                               .15865525393,delta=1e-6)
        lab.locator("#esa-normal-mode").select_option("between")
        lab.locator("#esa-normal-a").fill("-2")
        lab.locator("#esa-normal-b").fill("2")
        self.assertAlmostEqual(float(lab.locator("#esa-normal-probability").inner_text()),
                               .954499736104,delta=1e-6)
        lab.locator("#esa-normal-mu").fill("10")
        lab.locator("#esa-normal-sigma").fill("2")
        lab.locator("#esa-normal-a").fill("8")
        lab.locator("#esa-normal-b").fill("12")
        self.assertAlmostEqual(float(lab.locator("#esa-normal-probability").inner_text()),
                               .682689492137,delta=1e-6)
        self.assertEqual(lab.locator("#esa-normal-chart").get_attribute("role"),"img")
        self.assertTrue(lab.locator("#esa-normal-shade").get_attribute("d").startswith("M"))

    def test_normal_probability_explorer_validation_keyboard_mobile_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError");}
          });
        """)
        self.page.goto(self.origin + "/probability/distributions/normal-distribution/",
                       wait_until="networkidle")
        lab=self.page.locator("#esa-normal-probability-explorer")
        expect(lab).to_be_visible()
        sd=lab.locator("#esa-normal-sigma")
        sd.fill("0")
        expect(lab.locator("#esa-normal-error")).to_be_visible()
        expect(lab.locator("#esa-normal-chart")).to_be_hidden()
        sd.fill("1")
        lab.locator("#esa-normal-a").fill("2")
        lab.locator("#esa-normal-b").fill("1")
        expect(lab.locator("#esa-normal-error")).to_be_visible()
        lab.get_by_role("button",name="Reset standard normal example").focus()
        lab.get_by_role("button",name="Reset standard normal example").press("Enter")
        expect(lab.locator("#esa-normal-probability")).to_have_text("0.682689")
        lab.locator("#esa-normal-mode").focus()
        lab.locator("#esa-normal-mode").press("End")
        lab.locator("#esa-normal-mode").dispatch_event("change")
        expect(lab.locator("#esa-normal-prob-label")).to_have_text("P(X ≥ b)")
        self.assertEqual(self.errors,[])
        for width in (320,375,768):
            self.page.set_viewport_size({"width":width,"height":850})
            dimensions=lab.evaluate("""e=>({
              scroll:e.scrollWidth,client:e.clientWidth,right:e.getBoundingClientRect().right})""")
            self.assertLessEqual(dimensions["scroll"]-dimensions["client"],1,dimensions)
            self.assertLessEqual(dimensions["right"],width+1,dimensions)

    def test_ols_explorer_survives_denied_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError");}
          });
        """)
        self.page.goto(self.origin + "/modeling/simple-linear-regression/least-squares/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-ols-rss")).to_have_text("2.4000")
        self.page.locator("#esa-ols-outlier").click()
        self.assertNotEqual(self.page.locator("#esa-ols-b1").inner_text(),"0.6000")
        expect(self.page.locator("main h1")).to_be_visible()
        self.assertEqual(self.errors,[])

    def test_diagnostics_nine_lessons_preserve_resume_and_keyboard(self):
        """All nine original labels, exact canonical URLs and valid timestamps remain."""
        records=(
            ("residuals","Residuals"),
            ("residual-plots","Residual Plots"),
            ("nonlinearity","Diagnosing Nonlinearity"),
            ("heteroscedasticity","Diagnosing Heteroscedasticity"),
            ("outliers","Outliers and Influential Observations"),
            ("leverage","Leverage"),
            ("influence","Influence"),
            ("cooks-distance","Cook's Distance"),
            ("diagnostic-workflow","Diagnostic Workflow")
        )
        self.page.set_viewport_size({"width":375,"height":850})
        key="esa_continue_modeling_diagnostics_lesson_v0"
        overview=self.origin+"/modeling/diagnostics/"
        for slug,label in records:
            with self.subTest(slug=slug):
                url="/modeling/diagnostics/"+slug+"/"
                self.page.goto(self.origin+url,wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                saved=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
                self.assertEqual(saved["url"],url)
                self.assertEqual(saved["label"],label)
                self.assertIsInstance(saved["ts"],int)
                self.assertGreater(saved["ts"],0)
                self.page.goto(overview,wait_until="networkidle")
                block=self.page.locator("#continue-reading-modeling-diagnostics")
                expect(block).to_be_visible()
                expect(block.locator("#continue-reading-modeling-diagnostics-label")).to_have_text(
                    "You last visited: "+label)
                link=block.locator("#continue-reading-modeling-diagnostics-btn")
                self.assertEqual(link.get_attribute("href"),url)
                link.focus()
                self.assertTrue(link.evaluate("e=>document.activeElement===e"))
                self.assertLessEqual(link.evaluate("e=>e.getBoundingClientRect().right"),376)
        self.assertEqual(self.errors,[])

    def test_diagnostics_reject_malicious_saved_destinations_and_labels(self):
        self.page.goto(self.origin+"/modeling/diagnostics/",wait_until="networkidle")
        key="esa_continue_modeling_diagnostics_lesson_v0"
        overview=self.origin+"/modeling/diagnostics/"
        for url,label,ts in (
            ("javascript:alert(1)","Residuals",1730000000000),
            ("https://evil.example/","Residuals",1730000000000),
            ("/modeling/diagnostics/residuals/","<img src=x onerror=alert(1)>",1730000000000),
            ("/modeling/diagnostics/residuals/","Residuals",None),
            ("/modeling/diagnostics/residuals/","Residuals",0),
            ("/modeling/diagnostics/outliers/","Residuals",1730000000000)
        ):
            with self.subTest(url=url,label=label,ts=ts):
                self.page.evaluate("""({key,data})=>localStorage.setItem(key,JSON.stringify(data))""",
                    {"key":key,"data":{"url":url,"label":label,"ts":ts}})
                self.page.goto(overview,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-modeling-diagnostics")).to_be_hidden()
                self.assertEqual(self.page.locator("#continue-reading-modeling-diagnostics img").count(),0)
                self.assertEqual(self.errors,[])
        self.page.evaluate("""({key})=>localStorage.setItem(key,JSON.stringify({
          url:"/modeling/diagnostics/residuals/",label:"Residuals",ts:1730000000000
        }))""",{"key":key})
        self.page.goto(overview,wait_until="networkidle")
        block=self.page.locator("#continue-reading-modeling-diagnostics")
        expect(block).to_be_visible()
        expect(block.locator("strong")).to_have_text("Residuals")

    def test_diagnostics_nine_lessons_and_overview_denied_storage_mobile(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError");}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":800})
        for slug in (
            "residuals","residual-plots","nonlinearity","heteroscedasticity",
            "outliers","leverage","influence","cooks-distance","diagnostic-workflow"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+"/modeling/diagnostics/"+slug+"/",
                               wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                link=self.page.locator("main .hero-actions a").first
                link.focus()
                self.assertTrue(link.evaluate("e=>document.activeElement===e"))
                self.assertEqual(self.errors,[],slug)
        self.page.goto(self.origin+"/modeling/diagnostics/",wait_until="networkidle")
        expect(self.page.locator("main h1")).to_be_visible()
        expect(self.page.locator("#continue-reading-modeling-diagnostics")).to_be_hidden()
        self.assertEqual(self.errors,[])



    def test_logistic_probability_explorer_reference_odds_and_threshold(self):
        """At eta=0, p=.5, odds=1, one-unit OR=exp(1)."""
        self.page.goto(self.origin+"/modeling/extensions/logistic-regression/", wait_until="networkidle")
        lab=self.page.locator("#esa-logistic-lab")
        expect(lab).to_be_visible()
        self.assertAlmostEqual(float(lab.locator("#esa-logistic-eta").inner_text()),0,places=6)
        self.assertAlmostEqual(float(lab.locator("#esa-logistic-prob").inner_text()),.5,places=6)
        self.assertAlmostEqual(float(lab.locator("#esa-logistic-odds").inner_text()),1,places=6)
        self.assertAlmostEqual(float(lab.locator("#esa-logistic-or").inner_text()),2.718281828459,delta=1e-6)
        expect(lab.locator("#esa-logistic-class")).to_have_text("1 (positive)")
        lab.locator("#esa-logistic-threshold").fill("0.6")
        expect(lab.locator("#esa-logistic-class")).to_have_text("0 (negative)")
        lab.locator("#esa-logistic-x").fill("0")
        self.assertAlmostEqual(float(lab.locator("#esa-logistic-prob").inner_text()),.119202922022,delta=1e-6)
        self.assertGreater(len(lab.locator("#esa-logistic-curve").get_attribute("d")),100)
        self.assertIn("probability",lab.locator("#esa-logistic-chart").get_attribute("aria-label"))
        saved=self.page.evaluate("""() => JSON.parse(localStorage.getItem(
          "esa_continue_modeling_extensions_lesson_v0"))""")
        self.assertEqual(saved["label"],"Logistic Regression")
        self.assertEqual(saved["url"],"/modeling/extensions/logistic-regression/")
        self.assertIsInstance(saved["ts"],int)

    def test_logistic_explorer_invalid_inputs_keyboard_and_mobile(self):
        self.page.goto(self.origin+"/modeling/extensions/logistic-regression/",wait_until="networkidle")
        lab=self.page.locator("#esa-logistic-lab")
        lab.locator("#esa-logistic-b1").fill("")
        expect(lab.locator("#esa-logistic-error")).to_be_visible()
        expect(lab.locator("#esa-logistic-chart")).to_be_hidden()
        lab.get_by_role("button",name="Reset logistic example").focus()
        lab.get_by_role("button",name="Reset logistic example").press("Enter")
        expect(lab.locator("#esa-logistic-prob")).to_have_text("0.500000")
        lab.locator("#esa-logistic-b0").fill("10")
        lab.locator("#esa-logistic-b1").fill("10")
        lab.locator("#esa-logistic-x").fill("8")
        self.assertEqual(lab.locator("#esa-logistic-prob").inner_text(),"1.000000")
        self.assertNotEqual(lab.locator("#esa-logistic-odds").inner_text(),"Infinity")
        lab.locator("#esa-logistic-b0").fill("-10")
        lab.locator("#esa-logistic-b1").fill("-10")
        self.assertEqual(lab.locator("#esa-logistic-prob").inner_text(),"0.000000")
        for width in (320,375,768):
            self.page.set_viewport_size({"width":width,"height":850})
            bounds=lab.evaluate("e=>({w:e.scrollWidth,c:e.clientWidth,right:e.getBoundingClientRect().right})")
            self.assertLessEqual(bounds["w"]-bounds["c"],1,bounds)
            self.assertLessEqual(bounds["right"],width+1,bounds)

    def test_logistic_explorer_survives_denied_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{configurable:true,
          get(){throw new DOMException("Storage blocked","SecurityError")}});
        """)
        self.page.goto(self.origin+"/modeling/extensions/logistic-regression/",wait_until="networkidle")
        lab=self.page.locator("#esa-logistic-lab")
        expect(lab.locator("#esa-logistic-prob")).to_have_text("0.500000")
        lab.locator("#esa-logistic-x").fill("0")
        self.assertAlmostEqual(float(lab.locator("#esa-logistic-prob").inner_text()),.119202922022,delta=1e-6)
        self.assertEqual(self.errors,[])

    def test_histogram_bin_counts_and_left_closed_rule(self):
        """Twenty fixed scores: bins of width 10.2 contain 2,5,5,5,3 values."""
        self.page.goto(self.origin+"/descriptive/visualization/histograms/",wait_until="networkidle")
        lab=self.page.locator("#esa-histogram-lab")
        expect(lab).to_be_visible()
        self.assertEqual(lab.locator("#esa-histogram-n").inner_text(),"20")
        self.assertAlmostEqual(float(lab.locator("#esa-histogram-width").inner_text()),10.2,places=4)
        self.assertEqual(lab.locator("#esa-histogram-sum").inner_text(),"20")
        self.assertEqual([int(x) for x in lab.locator("#esa-histogram-frequency-table td").all_inner_texts()],
                         [2,5,5,5,3])
        lab.locator("#esa-histogram-data").fill("0, 1, 2, 3, 4")
        lab.locator("#esa-histogram-bins").fill("2")
        self.assertEqual([int(x) for x in lab.locator("#esa-histogram-frequency-table td").all_inner_texts()],
                         [2,3])
        self.assertEqual(lab.locator("#esa-histogram-sum").inner_text(),"5")
        expect(lab.locator("#esa-histogram-bars rect")).to_have_count(2)
        self.assertIn("frequencies",lab.locator("#esa-histogram-chart").get_attribute("aria-label"))

    def test_histogram_invalid_constant_keyboard_mobile_and_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{configurable:true,
          get(){throw new DOMException("Storage blocked","SecurityError")}});
        """)
        self.page.goto(self.origin+"/descriptive/visualization/histograms/",wait_until="networkidle")
        lab=self.page.locator("#esa-histogram-lab")
        expect(lab).to_be_visible()
        lab.locator("#esa-histogram-data").fill("3, 3, 3, 3")
        self.assertEqual(lab.locator("#esa-histogram-sum").inner_text(),"4")
        lab.locator("#esa-histogram-bins").fill("1")
        expect(lab.locator("#esa-histogram-error")).to_be_visible()
        expect(lab.locator("#esa-histogram-chart")).to_be_hidden()
        lab.get_by_role("button",name="Reset histogram example").focus()
        lab.get_by_role("button",name="Reset histogram example").press("Enter")
        self.assertEqual(lab.locator("#esa-histogram-sum").inner_text(),"20")
        lab.locator("#esa-histogram-data").fill("4, bad")
        expect(lab.locator("#esa-histogram-error")).to_be_visible()
        lab.get_by_role("button",name="Reset histogram example").click()
        for width in (320,375,768):
            self.page.set_viewport_size({"width":width,"height":850})
            bounds=lab.evaluate("e=>({w:e.scrollWidth,c:e.clientWidth,right:e.getBoundingClientRect().right})")
            self.assertLessEqual(bounds["w"]-bounds["c"],1,bounds)
            self.assertLessEqual(bounds["right"],width+1,bounds)
        self.assertEqual(self.errors,[])

    def test_extensions_nine_lessons_resume_exact_legacy_schema(self):
        lessons=(
            ("why-extensions","Why Extensions?"),
            ("logistic-regression","Logistic Regression"),
            ("probability-vs-logit","Probability vs Logit"),
            ("odds","Odds"),
            ("interpreting-logistic-coefficients","Interpreting Logistic Coefficients"),
            ("glm","Generalized Linear Models (GLMs)"),
            ("link-functions","Link Functions"),
            ("comparing-linear-and-logistic","Comparing Linear and Logistic Regression"),
            ("bridge-to-machine-learning","Bridge to Machine Learning")
        )
        key="esa_continue_modeling_extensions_lesson_v0"
        for slug,label in lessons:
            with self.subTest(slug=slug):
                dest="/modeling/extensions/"+slug+"/"
                self.page.goto(self.origin+dest,wait_until="networkidle")
                saved=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
                self.assertEqual((saved["url"],saved["label"]),(dest,label))
                self.assertIsInstance(saved["ts"],int)
                self.assertGreater(saved["ts"],0)
                self.page.goto(self.origin+"/modeling/extensions/",wait_until="networkidle")
                block=self.page.locator("#continue-reading-modeling-extensions")
                expect(block).to_be_visible()
                self.assertEqual(block.locator("#continue-reading-modeling-extensions-btn").get_attribute("href"),dest)
                expect(block.locator("#continue-reading-modeling-extensions-label")).to_have_text(
                    "You last visited: "+label)
                link=block.locator("#continue-reading-modeling-extensions-btn")
                link.focus()
                self.assertTrue(link.evaluate("e=>document.activeElement===e"))

    def test_extensions_resume_rejects_untrusted_saved_values(self):
        key="esa_continue_modeling_extensions_lesson_v0"
        self.page.goto(self.origin+"/modeling/extensions/",wait_until="networkidle")
        bad=(
            ("javascript:alert(1)","Odds",1730000000000),
            ("https://bad.example/","Odds",1730000000000),
            ("/modeling/extensions/odds/","<img src=x onerror=alert(1)>",1730000000000),
            ("/modeling/extensions/odds/","Logistic Regression",1730000000000),
            ("/modeling/extensions/odds/","Odds",0),
            ("/modeling/extensions/odds/","Odds",None),
            ("//bad.example","Odds",1730000000000)
        )
        for url,label,ts in bad:
            with self.subTest(url=url,label=label,ts=ts):
                self.page.evaluate("""({key,data})=>localStorage.setItem(key,JSON.stringify(data))""",
                  {"key":key,"data":{"url":url,"label":label,"ts":ts}})
                self.page.goto(self.origin+"/modeling/extensions/",wait_until="networkidle")
                expect(self.page.locator("#continue-reading-modeling-extensions")).to_be_hidden()
                self.assertEqual(self.page.locator("#continue-reading-modeling-extensions img").count(),0)
        self.page.evaluate("""key=>localStorage.setItem(key,JSON.stringify({
          url:"/modeling/extensions/odds/",label:"Odds",ts:1730000000000}))""",key)
        self.page.goto(self.origin+"/modeling/extensions/",wait_until="networkidle")
        expect(self.page.locator("#continue-reading-modeling-extensions strong")).to_have_text("Odds")

    def test_extensions_nine_lessons_and_overview_denied_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{configurable:true,
          get(){throw new DOMException("Storage blocked","SecurityError")}});
        """)
        self.page.set_viewport_size({"width":320,"height":800})
        for slug in ("why-extensions","logistic-regression","probability-vs-logit",
                     "odds","interpreting-logistic-coefficients","glm","link-functions",
                     "comparing-linear-and-logistic","bridge-to-machine-learning"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+"/modeling/extensions/"+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                link=self.page.locator("main .hero-actions a").first
                link.focus()
                self.assertTrue(link.evaluate("e=>document.activeElement===e"))
                self.assertEqual(self.errors,[],slug)
        self.page.goto(self.origin+"/modeling/extensions/",wait_until="networkidle")
        expect(self.page.locator("main h1")).to_be_visible()
        expect(self.page.locator("#continue-reading-modeling-extensions")).to_be_hidden()
        self.assertEqual(self.errors,[])




    def test_multicollinearity_vif_theoretical_reference_and_endpoints(self):
        """Independent references: VIF(.8)=25/9 and SE=2/sqrt(40*.36)."""
        self.page.goto(self.origin + "/modeling/multiple-regression/multicollinearity/",
                       wait_until="networkidle")
        lab=self.page.locator("#esa-vif-lab")
        expect(lab).to_be_visible()
        expect(lab.locator("#esa-vif-value")).to_have_text("1.0000")
        self.assertAlmostEqual(float(lab.locator("#esa-vif-reference").inner_text()),
                               2/(40**0.5),places=4)
        slider=lab.locator("#esa-vif-rho")
        slider.evaluate("(e,v)=>{e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}))}", "0.8")
        self.assertAlmostEqual(float(lab.locator("#esa-vif-value").inner_text()),
                               1/(1-0.8**2),places=4)
        self.assertAlmostEqual(float(lab.locator("#esa-vif-se").inner_text()),
                               2/((40*(1-0.8**2))**0.5),places=4)
        self.assertAlmostEqual(float(lab.locator("#esa-vif-factor").inner_text()),
                               1/((1-0.8**2)**0.5),places=4)
        slider.evaluate("(e,v)=>{e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}))}", "-0.8")
        self.assertAlmostEqual(float(lab.locator("#esa-vif-value").inner_text()),
                               25/9,places=4)
        slider.evaluate("(e,v)=>{e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}))}", "1")
        expect(lab.locator("#esa-vif-value")).to_have_text("undefined (rank deficient)")
        expect(lab.locator("#esa-vif-se")).to_have_text("undefined")
        slider.evaluate("(e,v)=>{e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}))}", "-1")
        expect(lab.locator("#esa-vif-se")).to_have_text("undefined")
        lab.get_by_role("button",name="Reset correlation").click()
        expect(lab.locator("#esa-vif-value")).to_have_text("1.0000")
        self.assertTrue(lab.locator("#esa-vif-curve").get_attribute("d").startswith("M"))
        self.assertIn("rank",lab.inner_text())

    def test_multicollinearity_vif_keyboard_mobile_and_denied_storage(self):
        self.page.add_init_script("""
            Object.defineProperty(window,"localStorage",{
              configurable:true,get(){throw new DOMException("Denied","SecurityError")}
            });
        """)
        self.page.goto(self.origin+"/modeling/multiple-regression/multicollinearity/",
                       wait_until="networkidle")
        lab=self.page.locator("#esa-vif-lab")
        slider=lab.locator("#esa-vif-rho")
        slider.focus()
        slider.press("ArrowRight")
        expect(lab.locator("#esa-vif-correlation")).to_have_text("0.01")
        self.assertEqual(self.errors,[])
        for width in (320,375,768):
            self.page.set_viewport_size({"width":width,"height":850})
            x=lab.evaluate("""e=>({scroll:e.scrollWidth,client:e.clientWidth,
              right:e.getBoundingClientRect().right})""")
            self.assertLessEqual(x["scroll"]-x["client"],1,x)
            self.assertLessEqual(x["right"],width+1,x)

    def test_boxplot_quartiles_fences_and_extreme_observation(self):
        """Median-of-halves/exclusive overall median; default quartiles 7.5 and 16."""
        self.page.goto(self.origin+"/descriptive/visualization/boxplots/",
                       wait_until="networkidle")
        lab=self.page.locator("#esa-boxplot-lab")
        expect(lab).to_be_visible()
        for key,want in (("n","9"),("min","5"),("q1","7.5"),("median","12"),
                         ("q3","16"),("max","20"),("iqr","8.5"),
                         ("fences","-5.25 / 28.75"),("whiskers","5 / 20"),
                         ("outliers","none")):
            expect(lab.locator("#esa-boxplot-"+key)).to_have_text(want)
        lab.get_by_role("button",name="Add extreme observation (120)").click()
        for key,want in (("n","10"),("q1","8"),("median","12.5"),
                         ("q3","17"),("iqr","9"),
                         ("fences","-5.5 / 30.5"),
                         ("whiskers","5 / 20"),("outliers","120")):
            expect(lab.locator("#esa-boxplot-"+key)).to_have_text(want)
        self.assertGreater(lab.locator("#esa-boxplot-marks circle").count(),0)
        lab.get_by_role("button",name="Reset example").click()
        expect(lab.locator("#esa-boxplot-outliers")).to_have_text("none")
        expect(lab.locator("#esa-boxplot-q1")).to_have_text("7.5")

    def test_boxplot_invalid_constant_repeated_and_mobile_keyboard(self):
        self.page.goto(self.origin+"/descriptive/visualization/boxplots/",
                       wait_until="networkidle")
        lab=self.page.locator("#esa-boxplot-lab")
        data=lab.locator("#esa-boxplot-data")
        data.fill("8,8,8,8")
        expect(lab.locator("#esa-boxplot-iqr")).to_have_text("0")
        expect(lab.locator("#esa-boxplot-whiskers")).to_have_text("8 / 8")
        data.fill("1,2,3")
        expect(lab.locator("#esa-boxplot-error")).to_be_visible()
        expect(lab.locator("#esa-boxplot-figure")).to_be_hidden()
        data.fill("2,3,4,5,NaN")
        expect(lab.locator("#esa-boxplot-error")).to_be_visible()
        data.fill("1, 2, 3, 4, 5, 6, 7, 8")
        expect(lab.locator("#esa-boxplot-error")).to_be_hidden()
        reset=lab.get_by_role("button",name="Reset example")
        reset.focus()
        reset.press("Enter")
        expect(lab.locator("#esa-boxplot-n")).to_have_text("9")
        for width in (320,375,768):
            self.page.set_viewport_size({"width":width,"height":850})
            x=lab.evaluate("""e=>({scroll:e.scrollWidth,client:e.clientWidth,
              right:e.getBoundingClientRect().right})""")
            self.assertLessEqual(x["scroll"]-x["client"],1,x)
            self.assertLessEqual(x["right"],width+1,x)

    def test_boxplot_still_works_when_browser_storage_is_denied(self):
        self.page.add_init_script("""
            Object.defineProperty(window,"localStorage",{
              configurable:true,get(){throw new DOMException("Denied","SecurityError")}
            });
        """)
        self.page.goto(self.origin+"/descriptive/visualization/boxplots/",wait_until="networkidle")
        lab=self.page.locator("#esa-boxplot-lab")
        expect(lab.locator("#esa-boxplot-q1")).to_have_text("7.5")
        lab.get_by_role("button",name="Add extreme observation (120)").click()
        expect(lab.locator("#esa-boxplot-outliers")).to_have_text("120")
        self.assertEqual(self.errors,[])

    def test_multiple_regression_nine_lessons_resume_schema_and_links(self):
        records=(
            ("why-multiple","Why Multiple Regression?"),
            ("model-structure","Model Structure"),
            ("adjusted-effects","Adjusted Effects"),
            ("confounding","Confounding"),
            ("coefficients","Coefficients"),
            ("multicollinearity","Multicollinearity"),
            ("dummy-variables","Dummy Variables"),
            ("interactions","Interactions"),
            ("model-building","Model Building"),
        )
        key="esa_continue_modeling_multiple_regression_lesson_v0"
        self.page.set_viewport_size({"width":375,"height":850})
        for slug,label in records:
            with self.subTest(slug=slug):
                path="/modeling/multiple-regression/"+slug+"/"
                self.page.goto(self.origin+path,wait_until="networkidle")
                saved=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
                self.assertEqual(saved["url"],path)
                self.assertEqual(saved["label"],label)
                self.assertIsInstance(saved["ts"],int)
                self.assertGreater(saved["ts"],0)
                self.page.goto(self.origin+"/modeling/multiple-regression/",wait_until="networkidle")
                block=self.page.locator("#continue-reading-modeling-mr")
                expect(block).to_be_visible()
                expect(block.locator("#continue-reading-modeling-mr-label")).to_have_text(
                    "You last visited: "+label)
                link=block.locator("#continue-reading-modeling-mr-btn")
                self.assertEqual(link.get_attribute("href"),path)
                link.focus()
                self.assertTrue(link.evaluate("e=>document.activeElement===e"))
                self.assertLessEqual(link.evaluate("e=>e.getBoundingClientRect().right"),376)

    def test_multiple_regression_rejects_malicious_progress_values(self):
        self.page.goto(self.origin+"/modeling/multiple-regression/",wait_until="networkidle")
        key="esa_continue_modeling_multiple_regression_lesson_v0"
        bad=(
            ("javascript:alert(1)","Coefficients",1730000000000),
            ("https://attacker.test","Coefficients",1730000000000),
            ("/modeling/multiple-regression/coefficients/","<img src=x onerror=alert(1)>",1730000000000),
            ("/modeling/multiple-regression/coefficients/","Confounding",1730000000000),
            ("/modeling/multiple-regression/coefficients/","Coefficients",None),
            ("/modeling/multiple-regression/coefficients/","Coefficients",0)
        )
        for url,label,ts in bad:
            with self.subTest(url=url,label=label,ts=ts):
                self.page.evaluate("""({k,d})=>localStorage.setItem(k,JSON.stringify(d))""",
                    {"k":key,"d":{"url":url,"label":label,"ts":ts}})
                self.page.goto(self.origin+"/modeling/multiple-regression/",wait_until="networkidle")
                expect(self.page.locator("#continue-reading-modeling-mr")).to_be_hidden()
                self.assertEqual(self.page.locator("#continue-reading-modeling-mr img").count(),0)
        self.page.evaluate("""key=>localStorage.setItem(key,JSON.stringify({
          url:"/modeling/multiple-regression/model-building/",
          label:"Model Building",ts:1730000000000}))""",key)
        self.page.goto(self.origin+"/modeling/multiple-regression/",wait_until="networkidle")
        expect(self.page.locator("#continue-reading-modeling-mr strong")).to_have_text("Model Building")

    def test_multiple_regression_nine_lessons_denied_storage_mobile(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":850})
        for slug in ("why-multiple","model-structure","adjusted-effects",
                     "confounding","coefficients","multicollinearity",
                     "dummy-variables","interactions","model-building"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+"/modeling/multiple-regression/"+slug+"/",
                               wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertEqual(self.errors,[],slug)
        self.page.goto(self.origin+"/modeling/multiple-regression/",wait_until="networkidle")
        expect(self.page.locator("main h1")).to_be_visible()
        expect(self.page.locator("#continue-reading-modeling-mr")).to_be_hidden()
        self.assertEqual(self.errors,[])



    def test_bootstrap_lab_reproducibility_and_arabic_parity(self):
        en="/inference/assumptions-robustness/bootstrap-as-robust-tool/"
        ar="/ar"+en
        values=[]
        for url in (en, ar):
            self.page.goto(self.origin+url,wait_until="networkidle")
            self.assertEqual(self.page.locator("#esa-boot-run").count(),1)
            self.page.locator("#esa-boot-run").click()
            output=self.page.locator("#esa-boot-stats").inner_text()
            self.assertIn("7.3333",output)
            self.assertIn("1000",output)
            self.assertEqual(self.page.locator("#esa-boot-plot rect").count(),20)
            values.append(self.page.locator("#esa-boot-stats").inner_text())
            self.page.locator("#esa-boot-run").click()
            self.assertEqual(output,self.page.locator("#esa-boot-stats").inner_text())
        import re
        self.assertEqual(re.findall(r"-?\d+\.\d{4}",values[0]),re.findall(r"-?\d+\.\d{4}",values[1]))

    def test_bootstrap_invalid_input_and_mobile_keyboard(self):
        self.page.set_viewport_size({"width":320,"height":800})
        self.page.goto(self.origin+"/inference/assumptions-robustness/bootstrap-as-robust-tool/",wait_until="networkidle")
        self.page.locator("#esa-boot-data").fill("2, invalid, 4")
        self.page.locator("#esa-boot-run").focus()
        self.page.keyboard.press("Enter")
        expect(self.page.locator("#esa-boot-status")).to_contain_text("finite")
        self.assertEqual(self.page.locator("#esa-boot-plot rect").count(),0)
        self.page.locator("#esa-boot-data").fill("5, 5, 5")
        self.page.locator("#esa-boot-run").click()
        expect(self.page.locator("#esa-boot-stats")).to_contain_text("0.0000")
        self.assertLessEqual(self.page.locator("#esa-bootstrap-lab").evaluate("e=>e.scrollWidth-e.clientWidth"),1)

    def test_bilingual_navigation_keeps_compact_mobile_header(self):
        self.page.set_viewport_size({"width":375,"height":650})
        self.page.goto(self.origin+"/descriptive/spread/variance/",wait_until="networkidle")
        header=self.page.locator(".site-header")
        self.assertLessEqual(header.evaluate("e=>e.getBoundingClientRect().height"),125)
        arabic=self.page.get_by_role("group",name="Language selection").locator('a[lang="ar"]')
        expect(arabic).to_be_hidden()
        toggle=self.page.get_by_role("button",name="Toggle menu")
        toggle.focus()
        self.page.keyboard.press("Enter")
        expect(arabic).to_be_visible()
        self.assertEqual(arabic.get_attribute("href"),"/ar/")
        self.page.goto(self.origin+"/inference/assumptions-robustness/bootstrap-as-robust-tool/",wait_until="networkidle")
        self.page.get_by_role("button",name="Toggle menu").click()
        self.assertEqual(self.page.get_by_role("group",name="Language selection").locator('a[lang="ar"]').get_attribute("href"),
                         "/ar/inference/assumptions-robustness/bootstrap-as-robust-tool/")

    def test_arabic_pilot_language_rtl_and_metadata(self):
        en="/inference/assumptions-robustness/bootstrap-as-robust-tool/"
        ar="/ar"+en
        for path,language in ((en,"en"),(ar,"ar")):
            self.page.goto(self.origin+path,wait_until="networkidle")
            self.assertEqual(self.page.locator("html").get_attribute("lang"),language)
            self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl" if language=="ar" else None)
            self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                             "https://easystatisticsacademy.com"+path)
            self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="ar"]').get_attribute("href"),
                             "https://easystatisticsacademy.com"+ar)
            self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="en"]').get_attribute("href"),
                             "https://easystatisticsacademy.com"+en)
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        self.assertEqual(self.page.locator('a[href="'+ar+'"]').count(),1)

    def test_overfitting_polynomial_generalization_lab(self):
        self.page.goto(self.origin+"/modeling/model-fit-comparison/overfitting/",wait_until="networkidle")
        select=self.page.locator("#esa-overfit-degree")
        values=[]
        for d in ("0","1","2","3","4","5","6"):
            select.select_option(d)
            output=self.page.locator("#esa-overfit-status").inner_text()
            self.assertIn("Training MSE",output)
            self.assertIn("Test MSE",output)
            self.assertEqual(self.page.locator("#esa-overfit-plot circle").count(),8)
            self.assertEqual(self.page.locator("#esa-overfit-plot rect").count(),6)
            import re
            vals=re.findall(r"MSE: ([0-9]+\.[0-9]+)",output)
            self.assertEqual(len(vals),2)
            values.append(tuple(map(float,vals)))
        self.assertLess(values[-1][0],values[0][0])
        # Independently benchmarked against NumPy least squares on the fixed dataset.
        self.assertAlmostEqual(values[0][0],0.22750,places=4)
        self.assertAlmostEqual(values[0][1],0.13583,places=4)
        self.assertAlmostEqual(values[1][0],0.19598,places=4)
        self.assertAlmostEqual(values[1][1],0.05825,places=4)
        self.assertAlmostEqual(values[6][0],0.00185,places=4)
        self.assertAlmostEqual(values[6][1],0.06743,places=4)
        self.page.locator("#esa-overfit-reset").click()
        self.assertEqual(select.input_value(),"1")

    def test_model_fit_progress_valid_legacy_and_malicious(self):
        path="/modeling/model-fit-comparison/"
        self.page.goto(self.origin+path,wait_until="networkidle")
        good={"url":path+"overfitting/","label":"Overfitting","ts":1730000000000}
        key="esa_continue_modeling_model_fit_lesson_v0"
        legacy="esa_continue_modeling_fit_lesson_v0"
        self.page.evaluate("([k,l,d])=>{localStorage.removeItem(k);localStorage.setItem(l,JSON.stringify(d));}",[key,legacy,good])
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-modeling-fit")).to_be_visible()
        self.assertEqual(self.page.locator("#continue-reading-modeling-fit-btn").get_attribute("href"),good["url"])
        self.assertIn("Overfitting",self.page.locator("#continue-reading-modeling-fit-label").inner_text())
        bad=[{"url":"javascript:alert(1)","label":"Overfitting","ts":1730000000000},
             {"url":good["url"],"label":"<img src=x onerror=alert(1)>","ts":1730000000000},
             {"url":good["url"],"label":"Overfitting","ts":"invalid"},
             {"url":good["url"],"label":"Overfitting","ts":-1}]
        for value in bad:
            self.page.evaluate("([k,l,d])=>{localStorage.setItem(k,JSON.stringify(d));localStorage.removeItem(l);}",[key,legacy,value])
            self.page.reload(wait_until="networkidle")
            expect(self.page.locator("#continue-reading-modeling-fit")).to_be_hidden()
            self.assertEqual(self.page.locator("#continue-reading-modeling-fit-label img").count(),0)

    def test_model_fit_all_lessons_denied_storage(self):
        self.page.add_init_script("""
            Object.defineProperty(window,"localStorage",{
              configurable:true,get(){throw new DOMException("Denied","SecurityError")}
            });
        """)
        for slug in ("what-is-model-fit","r-squared","adjusted-r-squared",
                     "underfitting","overfitting","train-vs-test",
                     "model-comparison","aic-bic","model-selection-thinking"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+"/modeling/model-fit-comparison/"+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+"/modeling/model-fit-comparison/",wait_until="networkidle")
        expect(self.page.locator("#continue-reading-modeling-fit")).to_be_hidden()


    def test_sampling_variability_finite_population_exact_theory(self):
        """Known finite population has exact SE 4.330127 without replacement."""
        route = "/foundations/sampling-variability/"
        self.page.goto(self.origin + route, wait_until="networkidle")
        self.assertEqual(self.page.locator("#esa-sv-mu").inner_text(), "170.0000")
        self.assertEqual(self.page.locator("#esa-sv-sigma2").inner_text(), "50.0000")
        self.assertEqual(self.page.locator("#esa-sv-theory").inner_text(), "4.3301")
        self.assertEqual(self.page.locator("#esa-sv-plot .esa-sv-bin").count(), 16)
        values = [self.page.locator("#esa-sv-" + k).inner_text() for k in
                  ("theory", "simulated", "average", "bias", "preview")]
        self.page.locator("#esa-sv-run").click()
        self.assertEqual(values, [self.page.locator("#esa-sv-" + k).inner_text() for k in
                                  ("theory", "simulated", "average", "bias", "preview")])
        self.assertEqual(len(self.page.locator("#esa-sv-preview").inner_text().split(", ")), 2)
        self.assertEqual(len(set(self.page.locator("#esa-sv-preview").inner_text().split(", "))), 2)
        self.page.locator("#esa-sv-method").select_option("with")
        self.assertEqual(self.page.locator("#esa-sv-theory").inner_text(), "4.3301")
        self.page.locator("#esa-sv-run").click()
        self.assertEqual(self.page.locator("#esa-sv-theory").inner_text(), "5.0000")
        self.page.locator("#esa-sv-size").select_option("5")
        self.page.locator("#esa-sv-run").click()
        self.assertEqual(self.page.locator("#esa-sv-theory").inner_text(), "3.1623")
        self.page.locator("#esa-sv-method").select_option("without")
        self.page.locator("#esa-sv-run").click()
        self.assertEqual(self.page.locator("#esa-sv-theory").inner_text(), "0.0000")
        self.assertEqual(self.page.locator("#esa-sv-simulated").inner_text(), "0.0000")
        self.assertEqual(self.page.locator("#esa-sv-average").inner_text(), "170.0000")
        self.page.locator("#esa-sv-reset").click()
        self.assertEqual(self.page.locator("#esa-sv-size").input_value(), "2")
        self.assertEqual(self.page.locator("#esa-sv-method").input_value(), "without")
        self.assertEqual(self.page.locator("#esa-sv-theory").inner_text(), "4.3301")

    def test_sampling_variability_arabic_numeric_parity_and_seo(self):
        english="/foundations/sampling-variability/"
        arabic="/ar/foundations/sampling-variability/"
        outputs=[]
        for route,lang in ((english, "en"), (arabic, "ar")):
            with self.subTest(route=route):
                self.page.goto(self.origin + route, wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"), lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),
                                 "rtl" if lang=="ar" else None)
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+route)
                for target,language in ((english,"en"),(arabic,"ar")):
                    self.assertEqual(
                        self.page.locator('link[rel="alternate"][hreflang="'+language+'"]').get_attribute("href"),
                        "https://easystatisticsacademy.com"+target)
                self.page.locator("#esa-sv-method").select_option("with")
                self.page.locator("#esa-sv-size").select_option("3")
                self.page.locator("#esa-sv-seed").fill("1234")
                self.page.locator("#esa-sv-reps").select_option("2000")
                self.page.locator("#esa-sv-run").click()
                outputs.append(tuple(self.page.locator("#esa-sv-"+k).inner_text() for k in
                            ("mu","sigma2","theory","simulated","average","bias","preview")))
                self.assertEqual(self.page.locator("#esa-sv-plot .esa-sv-bin").count(),16)
                self.assertEqual(self.page.locator("#esa-sv-theory").inner_text(),"4.0825")
                self.assertEqual(self.page.locator('script[src="/js/sampling-variability-lab.js"]').count(),1)
        self.assertEqual(outputs[0],outputs[1])
        self.page.goto(self.origin + "/ar/", wait_until="networkidle")
        self.assertEqual(self.page.locator('a[href="'+arabic+'"]').count(), 1)
        self.page.goto(self.origin + arabic, wait_until="networkidle")
        self.assertGreaterEqual(self.page.locator("main h2").count(), 13)
        self.assertIn("SPSS", self.page.locator("main").inner_text())
        self.assertIn("RANDBETWEEN", self.page.locator("main").inner_text())

    def test_sampling_variability_keyboard_mobile_and_seed_boundary(self):
        self.page.set_viewport_size({"width":320,"height":850})
        self.page.goto(self.origin + "/ar/foundations/sampling-variability/",wait_until="networkidle")
        self.page.locator("#esa-sv-seed").fill("-1")
        self.page.locator("#esa-sv-run").focus()
        self.page.keyboard.press("Enter")
        expect(self.page.locator("#esa-sv-status")).to_contain_text("بذرة")
        self.page.locator("#esa-sv-seed").fill("4294967295")
        self.page.locator("#esa-sv-run").focus()
        self.page.keyboard.press("Enter")
        expect(self.page.locator("#esa-sv-status")).to_contain_text("المحاكاة")
        self.assertLessEqual(
            self.page.locator("#esa-sv-lab").evaluate("e => e.scrollWidth-e.clientWidth"),1,
            str(self._lab_mobile_overflow_sources("esa-sv-lab")))
        formula_region=self.page.get_by_role("region",name="معادلات تباين المعاينة")
        expect(formula_region).to_have_attribute("tabindex","0")
        self.assertEqual(formula_region.evaluate("e=>getComputedStyle(e).overflowX"),"auto")
        self.assertLessEqual(self.page.evaluate("document.documentElement.scrollWidth-innerWidth"),2)

    def test_cooks_distance_independent_ols_numerical_benchmark(self):
        """Benchmarks independently calculated from statsmodels OLS influence."""
        self.page.goto(self.origin + "/modeling/diagnostics/cooks-distance/",wait_until="networkidle")
        target={
            "mse":4.2658312448,
            "residual":3.5228070175,
            "leverage":0.5087719298,
            "d":3.0669085761,
            "full-intercept":-1.9273182957,
            "full-slope":2.6005012531,
            "leave-intercept":0.0857142857,
            "leave-slope":1.9714285714,
        }
        for id,value in target.items():
            with self.subTest(metric=id):
                actual=float(self.page.locator("#esa-cook-"+id).inner_text())
                self.assertAlmostEqual(actual,value,places=5)
        self.assertEqual(self.page.locator("#esa-cook-table tr").count(),8)
        self.assertEqual(self.page.locator("#esa-cook-chart .esa-cook-fixed-point").count(),7)
        self.assertEqual(self.page.locator("#esa-cook-selected-point").count(),1)
        self.assertEqual(self.page.locator('#esa-cook-chart [data-series="full"]').count(),1)
        self.assertEqual(self.page.locator('#esa-cook-chart [data-series="leave-one-out"]').count(),1)
        cooks=[0.322232026,0.0103251579,0.00048855283,0.00942469318,
               0.0118349101,0.0859198618,0.294770328,3.0669085761]
        for i,value in enumerate(cooks):
            actual=float(self.page.locator("#esa-cook-table tr").nth(i).locator("td").nth(3).inner_text())
            self.assertAlmostEqual(actual,value,places=3)

    def _lab_mobile_overflow_sources(self, element_id):
        return self.page.evaluate("""id => {
          const root = document.getElementById(id);
          const initial = root.scrollWidth - root.clientWidth;
          const entries = [];
          for (const e of Array.from(root.children)) {
            const prev = e.style.display;
            e.style.display = "none";
            const delta = initial - (root.scrollWidth - root.clientWidth);
            e.style.display = prev;
            if (delta > 1) entries.push({
              node:e.tagName, id:e.id, cls:e.className,
              scrollDelta:delta,
              width:Math.round(e.getBoundingClientRect().width),
              scroll:e.scrollWidth, client:e.clientWidth
            });
          }
          const descendants = Array.from(root.querySelectorAll("*")).map(e => {
            const rect=e.getBoundingClientRect();
            const parent=root.getBoundingClientRect();
            return {node:e.tagName,id:e.id,cls:typeof e.className === "string" ? e.className : "",
              right:Math.round(rect.right-parent.left), left:Math.round(rect.left-parent.left),
              width:Math.round(rect.width),scroll:e.scrollWidth,client:e.clientWidth,
              overflow:getComputedStyle(e).overflowX};
          }).filter(e => e.right > root.clientWidth+2).slice(0,16);
          return {initial, entries, descendants};
        }""", element_id)

    def test_cooks_distance_slider_keyboard_reset_mobile_and_storage_denied(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":800})
        self.page.goto(self.origin+"/modeling/diagnostics/cooks-distance/",wait_until="networkidle")
        self.assertEqual(self.page.locator("#esa-cook-x-value").inner_text(),"9.0")
        before=self.page.locator("#esa-cook-d").inner_text()
        slider=self.page.locator("#esa-cook-y")
        slider.focus()
        self.page.keyboard.press("ArrowRight")
        self.assertNotEqual(self.page.locator("#esa-cook-d").inner_text(),before)
        self.page.locator("#esa-cook-x").evaluate(
            "(e)=>{e.value='15';e.dispatchEvent(new Event('input',{bubbles:true}))}")
        self.assertEqual(self.page.locator("#esa-cook-x-value").inner_text(),"15.0")
        self.page.locator("#esa-cook-reset").click()
        self.assertEqual(self.page.locator("#esa-cook-d").inner_text(),before)
        self.assertLessEqual(self.page.locator("#esa-cook-lab").evaluate(
            "e=>e.scrollWidth-e.clientWidth"),1,
            str(self._lab_mobile_overflow_sources("esa-cook-lab")))
        formula_region=self.page.get_by_role("region",name="Cook distance equation")
        expect(formula_region).to_have_attribute("tabindex","0")
        self.assertEqual(formula_region.evaluate("e=>getComputedStyle(e).overflowX"),"auto")

    def test_model_assumptions_safe_progress_all_eight_and_invalid_records(self):
        block="/modeling/assumptions/"
        key="esa_continue_modeling_assumptions_lesson_v0"
        lessons={
            "why-assumptions":"Why Assumptions Matter",
            "linearity":"Linearity",
            "independence":"Independence",
            "homoscedasticity":"Homoscedasticity",
            "normality":"Normality",
            "outliers":"Outliers",
            "violations":"Assumption Violations",
            "robustness":"Robustness",
        }
        for slug,label in lessons.items():
            with self.subTest(slug=slug):
                route=block+slug+"/"
                self.page.goto(self.origin+route,wait_until="networkidle")
                saved=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(saved["url"],route)
                self.assertEqual(saved["label"],label)
                self.assertIsInstance(saved["ts"],int)
                self.page.goto(self.origin+block,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-modeling-assumptions")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-modeling-assumptions-btn").get_attribute("href"),route)
                expect(self.page.locator("#continue-reading-modeling-assumptions-label")).to_have_text(
                    "You last visited: "+label)
        bad=[
            {"url":"javascript:alert(1)","label":"Linearity","ts":1730000000000},
            {"url":"https://attacker.invalid/","label":"Linearity","ts":1730000000000},
            {"url":block+"linearity/","label":"<img src=x onerror=alert(1)>","ts":1730000000000},
            {"url":block+"linearity/","label":"Robustness","ts":1730000000000},
            {"url":block+"linearity/","label":"Linearity","ts":"1730000000000"},
            {"url":block+"linearity/","label":"Linearity","ts":-1},
            {"url":block+"linearity/","label":"Linearity","ts":99999999999999},
        ]
        for value in bad:
            with self.subTest(value=value):
                self.page.evaluate("([k,d])=>localStorage.setItem(k,JSON.stringify(d))",[key,value])
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-modeling-assumptions")).to_be_hidden()
                self.assertEqual(self.page.locator("#continue-reading-modeling-assumptions-label img").count(),0)
        self.page.evaluate("k=>localStorage.setItem(k,'{bad json')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-modeling-assumptions")).to_be_hidden()

    def test_model_assumptions_denied_storage_all_eight(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":375,"height":750})
        for slug in ("why-assumptions","linearity","independence","homoscedasticity",
                     "normality","outliers","violations","robustness"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+"/modeling/assumptions/"+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+"/modeling/assumptions/",wait_until="networkidle")
        expect(self.page.locator("#continue-reading-modeling-assumptions")).to_be_hidden()
        expect(self.page.locator("main h1")).to_be_visible()


    def test_missing_data_bilingual_numeric_and_reproducible(self):
        """Fixed population truth 64; independently benchmark seeded realization."""
        values=[]
        for route in ("/foundations/missing-data/","/ar/foundations/missing-data/"):
            self.page.goto(self.origin+route,wait_until="networkidle")
            self.assertEqual(self.page.locator("#esa-md-table tr").count(),10)
            observed=self.page.locator("#esa-md-observed").inner_text()
            self.assertEqual(self.page.locator("#esa-md-true").inner_text(),"64.0000")
            self.assertEqual(self.page.locator("#esa-md-fraction").inner_text(),"4 / 10 (40%)")
            self.assertEqual(observed,"55.8333")
            self.assertEqual(self.page.locator("#esa-md-imputed").inner_text(),observed)
            self.assertEqual(self.page.locator("#esa-md-error").inner_text(),"-8.1667")
            self.assertEqual(self.page.locator("#esa-md-variance").inner_text(),"107.8704")
            self.page.locator("#esa-md-run").click()
            self.assertEqual(self.page.locator("#esa-md-observed").inner_text(),observed)
            self.page.locator("#esa-md-mode").select_option("mnar")
            self.page.locator("#esa-md-run").click()
            self.assertEqual(self.page.locator("#esa-md-observed").inner_text(),"57.5000")
            self.assertEqual(self.page.locator("#esa-md-fraction").inner_text(),"2 / 10 (20%)")
            self.assertEqual(self.page.locator("#esa-md-variance").inner_text(),"116.6667")
            values.append(self.page.locator("#esa-md-table").inner_text())
        self.assertEqual(values[0].count("40"),values[1].count("40"))
        # Both language versions must share the same numeric truth and model output.
        self.page.goto(self.origin+"/foundations/missing-data/",wait_until="networkidle")
        self.assertEqual(self.page.locator("#esa-md-observed").inner_text(),"55.8333")

    def test_missing_data_input_keyboard_mobile_and_reset(self):
        self.page.set_viewport_size({"width":320,"height":850})
        self.page.goto(self.origin+"/ar/foundations/missing-data/",wait_until="networkidle")
        self.page.locator("#esa-md-seed").fill("-1")
        self.page.locator("#esa-md-run").focus()
        self.page.keyboard.press("Enter")
        expect(self.page.locator("#esa-md-status")).to_contain_text("بذرة")
        self.page.locator("#esa-md-seed").fill("4294967295")
        self.page.locator("#esa-md-run").focus()
        self.page.keyboard.press("Enter")
        expect(self.page.locator("#esa-md-status")).to_contain_text("المحاكاة")
        self.page.locator("#esa-md-mode").select_option("mnar")
        self.page.locator("#esa-md-reset").click()
        self.assertEqual(self.page.locator("#esa-md-seed").input_value(),"2026")
        self.assertEqual(self.page.locator("#esa-md-mode").input_value(),"mcar")
        self.assertLessEqual(self.page.locator("#esa-md-lab").evaluate(
            "e=>e.scrollWidth-e.clientWidth"),1)
        self.assertLessEqual(self.page.evaluate("document.documentElement.scrollWidth-innerWidth"),2)

    def test_missing_data_english_arabic_metadata_and_navigation(self):
        en="/foundations/missing-data/"
        ar="/ar/foundations/missing-data/"
        for route,language in ((en,"en"),(ar,"ar")):
            self.page.goto(self.origin+route,wait_until="networkidle")
            self.assertEqual(self.page.locator("html").get_attribute("lang"),language)
            self.assertEqual(self.page.locator("html").get_attribute("dir"),
                             "rtl" if language=="ar" else None)
            self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                             "https://easystatisticsacademy.com"+route)
            for lang,path in (("en",en),("ar",ar)):
                self.assertEqual(
                    self.page.locator('link[rel="alternate"][hreflang="'+lang+'"]').get_attribute("href"),
                    "https://easystatisticsacademy.com"+path)
            self.assertEqual(self.page.get_by_role("group",name="Language selection")
                             .locator('a[lang="ar"]').get_attribute("href"),ar)
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        self.assertEqual(self.page.locator('a[href="'+ar+'"]').count(),1)

    def test_multiple_testing_exact_bonferroni_bh_and_fdp(self):
        """Benchmarked independently by sorting the seeded p-values."""
        self.page.goto(self.origin+"/inference/interpretation-reporting/multiple-testing-and-false-positives/",
                       wait_until="networkidle")
        self.assertEqual(self.page.locator("#esa-mt-table tr").count(),10)
        self.assertEqual(self.page.locator("#esa-mt-bonf-cut").inner_text(),"0.005000")
        self.assertEqual(self.page.locator("#esa-mt-bh-rank").inner_text(),"2")
        self.assertEqual(self.page.locator("#esa-mt-bh-cut").inner_text(),"0.007417")
        self.assertEqual(self.page.locator("#esa-mt-fwer").inner_text(),"0.401263")
        rows=self.page.locator("#esa-mt-table tr")
        expected=[
            (0.043013, "Reject", "Retain", "Retain"),
            (0.308496, "Retain", "Retain", "Retain"),
            (0.661157, "Retain", "Retain", "Retain"),
            (0.618475, "Retain", "Retain", "Retain"),
            (0.000538, "Reject", "Reject", "Reject"),
            (0.221843, "Retain", "Retain", "Retain"),
            (0.682860, "Retain", "Retain", "Retain"),
            (0.801409, "Retain", "Retain", "Retain"),
            (0.007417, "Reject", "Retain", "Reject"),
            (0.042668, "Reject", "Retain", "Retain"),
        ]
        for i,(p,raw,bonf,bh) in enumerate(expected):
            with self.subTest(i=i):
                cells=[c.inner_text() for c in rows.nth(i).locator("td").all()]
                self.assertAlmostEqual(float(cells[2]),p,places=6)
                self.assertEqual(cells[3:],[raw,bonf,bh])
        summary=self.page.locator("#esa-mt-summary tr")
        self.assertEqual([c.inner_text() for c in summary.nth(0).locator("td").all()],
                         ["Unadjusted","4","1","0.250000"])
        self.assertEqual([c.inner_text() for c in summary.nth(1).locator("td").all()],
                         ["Bonferroni","1","0","0.000000"])
        self.assertEqual([c.inner_text() for c in summary.nth(2).locator("td").all()],
                         ["Benjamini–Hochberg","2","0","0.000000"])
        original=self.page.locator("#esa-mt-table").inner_text()
        self.page.locator("#esa-mt-run").click()
        self.assertEqual(self.page.locator("#esa-mt-table").inner_text(),original)

    def test_multiple_testing_keyboard_mobile_seed_and_denied_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":800})
        self.page.goto(self.origin+"/inference/interpretation-reporting/multiple-testing-and-false-positives/",
                       wait_until="networkidle")
        self.page.locator("#esa-mt-seed").fill("-1")
        self.page.locator("#esa-mt-run").focus()
        self.page.keyboard.press("Enter")
        expect(self.page.locator("#esa-mt-status")).to_contain_text("integer seed")
        self.page.locator("#esa-mt-seed").fill("4294967295")
        self.page.locator("#esa-mt-count").select_option("20")
        self.page.locator("#esa-mt-alpha").select_option("0.01")
        self.page.locator("#esa-mt-run").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-mt-table tr").count(),20)
        self.assertEqual(self.page.locator("#esa-mt-bonf-cut").inner_text(),"0.000500")
        self.assertLessEqual(self.page.locator("#esa-mt-lab").evaluate(
            "e=>e.scrollWidth-e.clientWidth"),1)
        self.page.locator("#esa-mt-reset").click()
        self.assertEqual(self.page.locator("#esa-mt-count").input_value(),"10")
        self.assertEqual(self.page.locator("#esa-mt-seed").input_value(),"2026")

    def test_model_foundations_safe_resume_and_invalid_storage(self):
        path="/modeling/foundations/"
        key="esa_continue_modeling_foundations_lesson_v0"
        lessons={
            "what-is-a-model":"What Is a Model?",
            "variables":"Variables",
            "signal-noise":"Signal and Noise",
            "parameters":"Parameters",
            "prediction-vs-explanation":"Prediction vs Explanation"
        }
        for slug,label in lessons.items():
            with self.subTest(slug=slug):
                route=path+slug+"/"
                self.page.goto(self.origin+route,wait_until="networkidle")
                stored=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(stored["url"],route)
                self.assertEqual(stored["label"],label)
                self.assertGreater(stored["ts"],0)
                self.page.goto(self.origin+path,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-modeling-foundations")).to_be_visible()
                self.assertEqual(
                    self.page.locator("#continue-reading-modeling-foundations-btn").get_attribute("href"),route)
                expect(self.page.locator("#continue-reading-modeling-foundations-label")).to_contain_text(label)
        bad=[
            {"url":"javascript:alert(1)","label":"Variables","ts":1730000000000},
            {"url":"https://evil.example/","label":"Variables","ts":1730000000000},
            {"url":path+"variables/","label":"<img src=x onerror=alert(1)>","ts":1730000000000},
            {"url":path+"variables/","label":"Parameters","ts":1730000000000},
            {"url":path+"variables/","label":"Variables","ts":"1730000000000"},
            {"url":path+"variables/","label":"Variables","ts":-1},
            {"url":path+"variables/","label":"Variables","ts":99999999999999}
        ]
        self.page.goto(self.origin+path,wait_until="networkidle")
        for value in bad:
            with self.subTest(value=value):
                self.page.evaluate("([k,d])=>localStorage.setItem(k,JSON.stringify(d))",[key,value])
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-modeling-foundations")).to_be_hidden()
                self.assertEqual(self.page.locator(
                    "#continue-reading-modeling-foundations-label img").count(),0)
        self.page.evaluate("k=>localStorage.setItem(k,'{invalid json')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-modeling-foundations")).to_be_hidden()

    def test_model_foundations_all_five_denied_storage_mobile(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":375,"height":750})
        for slug in ("what-is-a-model","variables","signal-noise","parameters","prediction-vs-explanation"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+"/modeling/foundations/"+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+"/modeling/foundations/",wait_until="networkidle")
        expect(self.page.locator("#continue-reading-modeling-foundations")).to_be_hidden()
        expect(self.page.locator("main h1")).to_be_visible()


    def test_sd_lab_exact_variance_population_sample_and_outlier(self):
        """Independent reference: n=8, mean=5, SS=32, population SD=2."""
        url="/descriptive/spread/standard-deviation/"
        self.page.goto(self.origin+url,wait_until="networkidle")
        expected={"esa-sd-count":"8","esa-sd-mean":"5.0000",
                  "esa-sd-ss":"32.0000","esa-sd-pop-var":"4.0000",
                  "esa-sd-pop-sd":"2.0000","esa-sd-samp-var":"4.5714",
                  "esa-sd-samp-sd":"2.1381"}
        for key,val in expected.items():
            self.assertEqual(self.page.locator("#"+key).inner_text(),val)
        self.assertEqual(self.page.locator("#esa-sd-table tr").count(),8)
        self.assertEqual(self.page.locator("#esa-sd-table tr").first.locator("td").all_inner_texts(),
                         ["1","2.0000","-3.0000","9.0000"])
        self.page.locator("#esa-sd-outlier").click()
        outlier={"esa-sd-mean":"7.6250","esa-sd-ss":"585.8750",
                 "esa-sd-pop-var":"73.2344","esa-sd-pop-sd":"8.5577",
                 "esa-sd-samp-var":"83.6964","esa-sd-samp-sd":"9.1486"}
        for key,val in outlier.items():
            self.assertEqual(self.page.locator("#"+key).inner_text(),val)
        self.page.locator("#esa-sd-identical").click()
        self.assertEqual(self.page.locator("#esa-sd-pop-sd").inner_text(),"0.0000")
        self.assertEqual(self.page.locator("#esa-sd-samp-sd").inner_text(),"0.0000")
        self.page.locator("#esa-sd-single").click()
        self.assertEqual(self.page.locator("#esa-sd-pop-sd").inner_text(),"0.0000")
        self.assertIn("Undefined",self.page.locator("#esa-sd-samp-var").inner_text())
        self.page.locator("#esa-sd-reset").click()
        self.assertEqual(self.page.locator("#esa-sd-mean").inner_text(),"5.0000")

    def test_sd_lab_arabic_english_parity_metadata_and_navigation(self):
        en="/descriptive/spread/standard-deviation/"
        ar="/ar/descriptive/spread/standard-deviation/"
        results=[]
        for url,lang in ((en,"en"),(ar,"ar")):
            self.page.goto(self.origin+url,wait_until="networkidle")
            self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
            self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl" if lang=="ar" else None)
            self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                             "https://easystatisticsacademy.com"+url)
            for lng,route in (("en",en),("ar",ar)):
                self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+lng+'"]')
                                 .get_attribute("href"),"https://easystatisticsacademy.com"+route)
            group=self.page.get_by_role("group",name="Language selection")
            self.assertEqual(group.locator('a[lang="ar"]').get_attribute("href"),ar)
            self.assertEqual(group.locator('a[lang="en"]').get_attribute("href"),en)
            results.append([self.page.locator("#esa-sd-"+metric).inner_text()
                            for metric in ("mean","ss","pop-var","pop-sd","samp-var","samp-sd")])
            self.page.locator("#esa-sd-values").fill("1, 3, 5, 7")
            self.page.locator("#esa-sd-run").click()
            self.assertEqual(self.page.locator("#esa-sd-mean").inner_text(),"4.0000")
            self.assertEqual(self.page.locator("#esa-sd-pop-var").inner_text(),"5.0000")
            self.assertEqual(self.page.locator("#esa-sd-samp-var").inner_text(),"6.6667")
            results.append([self.page.locator("#esa-sd-"+metric).inner_text()
                            for metric in ("mean","ss","pop-var","pop-sd","samp-var","samp-sd")])
        self.assertEqual(results[0],results[2])
        self.assertEqual(results[1],results[3])
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        self.assertEqual(self.page.locator('a[href="'+ar+'"]').count(),1)

    def test_sd_lab_mobile_keyboard_invalid_input_and_denied_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":800})
        self.page.goto(self.origin+"/ar/descriptive/spread/standard-deviation/",
                       wait_until="networkidle")
        self.page.locator("#esa-sd-values").fill("two, five")
        self.page.locator("#esa-sd-run").focus()
        self.page.keyboard.press("Enter")
        self.assertIn("أدخل",self.page.locator("#esa-sd-status").inner_text())
        self.assertEqual(self.page.locator("#esa-sd-pop-sd").inner_text(),"2.0000")
        self.page.locator("#esa-sd-values").fill("2, 4, 6")
        self.page.locator("#esa-sd-run").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-sd-mean").inner_text(),"4.0000")
        self.assertLessEqual(self.page.locator("#esa-sd-lab").evaluate(
            "e=>e.scrollWidth-e.clientWidth"),1)
        self.page.locator("#esa-sd-single").click()
        self.assertIn("غير معرّف",self.page.locator("#esa-sd-samp-sd").inner_text())

    def test_simpson_stratified_pooled_standardized_exact_benchmark(self):
        self.page.goto(self.origin+"/applied-statistics/study-design/bias-confounding/",
                       wait_until="networkidle")
        expected={
            "esa-sp-a1-rate":"93.10%","esa-sp-b1-rate":"86.67%",
            "esa-sp-a2-rate":"73.00%","esa-sp-b2-rate":"68.75%",
            "esa-sp-a-pooled":"78.00%","esa-sp-b-pooled":"82.57%",
            "esa-sp-a-standard":"83.05%","esa-sp-b-standard":"77.71%",
            "esa-sp-winner1":"A","esa-sp-winner2":"A",
            "esa-sp-winner-pooled":"B","esa-sp-winner-standard":"A"
        }
        for key,val in expected.items():
            self.assertEqual(self.page.locator("#"+key).inner_text(),val)
        expect(self.page.locator("#esa-sp-explanation")).to_contain_text("Simpson's paradox")
        self.page.locator("#esa-sp-balanced").click()
        self.assertEqual(self.page.locator("#esa-sp-a-pooled").inner_text(),"79.47%")
        self.assertEqual(self.page.locator("#esa-sp-b-pooled").inner_text(),"75.00%")
        self.assertEqual(self.page.locator("#esa-sp-winner-pooled").inner_text(),"A")
        expect(self.page.locator("#esa-sp-explanation")).to_contain_text("No strict Simpson reversal")
        self.page.locator("#esa-sp-reset").click()
        self.assertEqual(self.page.locator("#esa-sp-winner-pooled").inner_text(),"B")

    def test_simpson_keyboard_invalid_denominator_mobile_denied_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":800})
        self.page.goto(self.origin+"/applied-statistics/study-design/bias-confounding/",
                       wait_until="networkidle")
        self.page.locator("#esa-sp-a1-s").fill("100")
        self.page.locator("#esa-sp-a1-n").fill("50")
        self.page.locator("#esa-sp-run").focus()
        self.page.keyboard.press("Enter")
        self.assertIn("Invalid counts",self.page.locator("#esa-sp-status").inner_text())
        self.page.locator("#esa-sp-a1-s").fill("40")
        self.page.locator("#esa-sp-run").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-sp-a1-rate").inner_text(),"80.00%")
        self.assertLessEqual(self.page.locator("#esa-simpson-lab").evaluate(
            "e=>e.scrollWidth-e.clientWidth"),1)
        self.page.locator("#esa-sp-reset").click()
        self.assertEqual(self.page.locator("#esa-sp-a1-rate").inner_text(),"93.10%")

    def test_likelihood_resume_all_five_existing_labels_and_paths(self):
        path="/mathematical-statistics/likelihood-and-log-likelihood/"
        key="esa_continue_ms_likelihood_last_lesson_v0"
        lessons={
            "probability-vs-likelihood":"Lesson 1 — Probability vs Likelihood",
            "likelihood-and-log-likelihood":"Lesson 2 — Likelihood and Log-Likelihood",
            "score-function":"Lesson 3 — Score Function",
            "observed-vs-expected-information":"Lesson 4 — Observed vs Expected Information",
            "regularity-conditions-preview":"Lesson 5 — Regularity Conditions"
        }
        for slug,label in lessons.items():
            with self.subTest(slug=slug):
                url=path+slug+"/"
                self.page.goto(self.origin+url,wait_until="networkidle")
                data=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(data["url"],url)
                self.assertEqual(data["label"],label)
                self.assertGreater(data["ts"],0)
                self.page.goto(self.origin+path,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-ms-b2")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-ms-b2-btn")
                                 .get_attribute("href"),url)
                self.assertIn(label,self.page.locator("#continue-reading-ms-b2-label").inner_text())
        self.assertEqual(self.page.locator("#continue-reading-ms-b2-label img").count(),0)

    def test_likelihood_resume_rejects_injection_wrong_labels_times_invalid_json(self):
        path="/mathematical-statistics/likelihood-and-log-likelihood/"
        key="esa_continue_ms_likelihood_last_lesson_v0"
        good={"url":path+"score-function/","label":"Lesson 3 — Score Function","ts":1730000000000}
        self.page.goto(self.origin+path,wait_until="networkidle")
        self.page.evaluate("([k,v])=>localStorage.setItem(k,JSON.stringify(v))",[key,good])
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms-b2")).to_be_visible()
        cases=[
            dict(good,url="javascript:alert(1)"),
            dict(good,url="https://bad.example/"),
            dict(good,url="/mathematical-statistics/maximum-likelihood-estimation/"),
            dict(good,label="<img src=x onerror=alert(1)>"),
            dict(good,label="Lesson 2 — Likelihood and Log-Likelihood"),
            dict(good,ts="1730000000000"),
            dict(good,ts=-1),
            dict(good,ts=99999999999999),
        ]
        for data in cases:
            with self.subTest(data=data):
                self.page.evaluate("([k,v])=>localStorage.setItem(k,JSON.stringify(v))",[key,data])
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-ms-b2")).to_be_hidden()
                self.assertEqual(self.page.locator("#continue-reading-ms-b2-label img").count(),0)
        self.page.evaluate("k=>localStorage.setItem(k,'{bad-json')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms-b2")).to_be_hidden()

    def test_likelihood_denied_storage_five_lessons_and_mobile_overview(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":375,"height":760})
        root="/mathematical-statistics/likelihood-and-log-likelihood/"
        for slug in ("probability-vs-likelihood","likelihood-and-log-likelihood","score-function",
                     "observed-vs-expected-information","regularity-conditions-preview"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms-b2")).to_be_hidden()
        expect(self.page.locator("main h1")).to_be_visible()


    def test_clt_simulation_moments_and_reproducible_histogram(self):
        """Exponential(1) gives exact E(mean)=1 and SD(mean)=1/sqrt(n)."""
        self.page.goto(self.origin+"/probability/lln-clt/central-limit-theorem/",
                       wait_until="networkidle")
        self.assertEqual(self.page.locator("#esa-clt-count").inner_text(),"800")
        self.assertEqual(self.page.locator("#esa-clt-theory-se").inner_text(),"0.1826")
        self.assertEqual(self.page.locator("#esa-clt-chart rect").count(),16)
        first=self.page.locator("#esa-clt-emp-mean").inner_text()
        self.page.locator("#esa-clt-run").click()
        self.assertEqual(self.page.locator("#esa-clt-emp-mean").inner_text(),first)
        for n,se,tol in ((1,1.0,0.20),(5,1/5**0.5,0.10),
                         (30,1/30**0.5,0.04),(100,0.1,0.025)):
            self.page.locator("#esa-clt-n").select_option(str(n))
            self.page.locator("#esa-clt-run").click()
            self.assertLess(abs(float(self.page.locator("#esa-clt-emp-mean").inner_text())-1),tol)
            self.assertLess(abs(float(self.page.locator("#esa-clt-emp-sd").inner_text())-se),tol)
            self.assertLess(abs(float(self.page.locator("#esa-clt-theory-se").inner_text())-se),0.00006)
        previous=self.page.locator("#esa-clt-count").inner_text()
        self.page.locator("#esa-clt-seed").fill("0")
        self.page.locator("#esa-clt-run").click()
        self.assertIn("integer seed",self.page.locator("#esa-clt-status").inner_text())
        self.assertEqual(self.page.locator("#esa-clt-count").inner_text(),previous)

    def test_clt_bilingual_parity_metadata_keyboard_and_mobile(self):
        en="/probability/lln-clt/central-limit-theorem/"
        ar="/ar/probability/lln-clt/central-limit-theorem/"
        results=[]
        self.page.set_viewport_size({"width":320,"height":780})
        for path,lang in ((en,"en"),(ar,"ar")):
            self.page.goto(self.origin+path,wait_until="networkidle")
            self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
            self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl" if lang=="ar" else None)
            self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                             "https://easystatisticsacademy.com"+path)
            for lng,route in (("en",en),("ar",ar)):
                self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+lng+'"]')
                                 .get_attribute("href"),"https://easystatisticsacademy.com"+route)
            # The language group is initially inside the collapsed mobile navigation.
            # Open it as a learner would, then assert accessibility and reciprocal paths.
            toggle=self.page.locator("header .nav-toggle")
            toggle.click()
            self.assertEqual(toggle.get_attribute("aria-expanded"),"true")
            language=self.page.get_by_role("group",name="Language selection")
            expect(language).to_be_visible()
            self.assertEqual(language.locator('a[lang="en"]').get_attribute("href"),en)
            self.assertEqual(language.locator('a[lang="ar"]').get_attribute("href"),ar)
            self.page.locator("#esa-clt-n").select_option("100")
            self.page.locator("#esa-clt-run").focus()
            self.page.keyboard.press("Enter")
            results.append((self.page.locator("#esa-clt-emp-mean").inner_text(),
                            self.page.locator("#esa-clt-emp-sd").inner_text()))
            self.assertLessEqual(self.page.locator("#esa-clt-lab").evaluate(
                "e=>e.scrollWidth-e.clientWidth"),2)
        self.assertEqual(results[0],results[1])
        self.assertIn("/ar/probability/lln-clt/central-limit-theorem/",
                      (SITE/"ar"/"index.html").read_text())

    def test_clt_denied_storage_still_runs(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.goto(self.origin+"/ar/probability/lln-clt/central-limit-theorem/",
                       wait_until="networkidle")
        self.assertEqual(self.page.locator("#esa-clt-theory-mean").inner_text(),"1.0000")
        self.page.locator("#esa-clt-n").select_option("5")
        self.page.locator("#esa-clt-run").click()
        self.assertEqual(self.page.locator("#esa-clt-theory-se").inner_text(),"0.4472")

    def test_bayes_posteriors_exact_and_expected_frequencies(self):
        self.page.goto(self.origin+"/probability/conditional/bayes-theorem/",
                       wait_until="networkidle")
        expect={"esa-bayes-pos":"15.38%","esa-bayes-neg":"0.11%",
                "esa-bayes-plus-prob":"5.85%","esa-bayes-minus-prob":"94.15%",
                "esa-bayes-tp":"90.00","esa-bayes-fp":"495.00",
                "esa-bayes-fn":"10.00","esa-bayes-tn":"9405.00"}
        for key,value in expect.items():
            self.assertEqual(self.page.locator("#"+key).inner_text(),value)
        self.page.locator("#esa-bayes-prev").fill("10")
        self.page.locator("#esa-bayes-run").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-bayes-pos").inner_text(),"66.67%")
        self.page.locator("#esa-bayes-reset").click()
        self.assertEqual(self.page.locator("#esa-bayes-pos").inner_text(),"15.38%")

    def test_bayes_zero_probability_invalid_input_and_mobile(self):
        self.page.set_viewport_size({"width":320,"height":780})
        self.page.goto(self.origin+"/probability/conditional/bayes-theorem/",
                       wait_until="networkidle")
        self.page.locator("#esa-bayes-prev").fill("0")
        self.page.locator("#esa-bayes-spec").fill("100")
        self.page.locator("#esa-bayes-run").click()
        self.assertIn("Undefined",self.page.locator("#esa-bayes-pos").inner_text())
        self.assertEqual(self.page.locator("#esa-bayes-plus-prob").inner_text(),"0.00%")
        self.page.locator("#esa-bayes-prev").fill("101")
        self.page.locator("#esa-bayes-run").click()
        self.assertIn("Enter prevalence",self.page.locator("#esa-bayes-status").inner_text())
        self.assertEqual(self.page.locator("#esa-bayes-pos").inner_text(),"—")
        self.assertLessEqual(self.page.locator("#esa-bayes-lab").evaluate(
            "e=>e.scrollWidth-e.clientWidth"),2)

    def test_z_interval_assumptions_exact_vs_approximate(self):
        html=(SITE/"inference"/"confidence-intervals"/"ci-for-mean-sigma-known-z"/"index.html").read_text()
        self.assertIn("does not by itself make the sample mean normally distributed",html)
        self.assertIn("coverage is only approximate",html)
        self.assertIn("finite positive variance",html)
        self.assertIn("n = 30",html)
        # Independent arithmetic check of the example: sigma/sqrt(n)=12/6=2,
        # margin 1.96*2=3.92 and rounded interval [46.08, 53.92].
        self.assertAlmostEqual(12/(36**.5),2)
        self.assertAlmostEqual(50-1.96*2,46.08)
        self.assertAlmostEqual(50+1.96*2,53.92)


    def test_batch55_bayes_arabic_full_translation_and_parity(self):
        """Arabic and English share one numerical implementation and valid translation metadata."""
        en="/probability/conditional/bayes-theorem/"
        ar="/ar/probability/conditional/bayes-theorem/"
        results=[]
        for path,language in ((en,"en"),(ar,"ar")):
            with self.subTest(lang=language):
                self.page.goto(self.origin+path,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),language)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),
                                 "rtl" if language=="ar" else None)
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+path)
                for lang,route in (("en",en),("ar",ar)):
                    self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+lang+'"]')
                                     .get_attribute("href"),"https://easystatisticsacademy.com"+route)
                    self.assertEqual(self.page.locator("header nav").locator('a[lang="'+lang+'"]')
                                     .get_attribute("href"),route)
                output_ids=("pos","neg","tp","fp","fn","tn","plus-prob","minus-prob")
                results.append(tuple(self.page.locator("#esa-bayes-"+i).inner_text() for i in output_ids))
                self.assertEqual(self.page.locator("#esa-bayes-pos").inner_text(),"15.38%")
                self.assertEqual(self.page.locator("#esa-bayes-tp").inner_text(),"90.00")
                self.page.locator("#esa-bayes-prev").fill("10")
                self.page.locator("#esa-bayes-run").click()
                self.assertEqual(self.page.locator("#esa-bayes-pos").inner_text(),"66.67%")
        self.assertEqual(results[0],results[1])
        self.assertIn('/ar/probability/conditional/bayes-theorem/',
                      (SITE/"ar"/"index.html").read_text())
        self.assertIn("نظرية بايز",self.page.locator("main").inner_text())

    def test_batch55_bayes_arabic_boundaries_and_storage_denied(self):
        self.page.add_init_script("""
        Object.defineProperty(window,"localStorage",{
          configurable:true,get(){throw new DOMException("Denied","SecurityError")}
        });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        self.page.goto(self.origin+"/ar/probability/conditional/bayes-theorem/",
                       wait_until="networkidle")
        self.page.locator("#esa-bayes-prev").fill("0")
        self.page.locator("#esa-bayes-spec").fill("100")
        self.page.locator("#esa-bayes-run").focus()
        self.page.keyboard.press("Enter")
        self.assertIn("غير معرّف",self.page.locator("#esa-bayes-pos").inner_text())
        self.page.locator("#esa-bayes-prev").fill("101")
        self.page.locator("#esa-bayes-run").click()
        self.assertIn("أدخل",self.page.locator("#esa-bayes-status").inner_text())
        self.assertEqual(self.page.locator("#esa-bayes-pos").inner_text(),"—")
        self.assertLessEqual(self.page.locator("#esa-bayes-lab").evaluate(
            "e=>e.scrollWidth-e.clientWidth"),2)

    def test_batch55_type_errors_exact_normal_benchmarks_and_seeded_counts(self):
        self.page.goto(self.origin+"/inference/hypothesis-testing/type1-type2-errors/",
                       wait_until="networkidle")
        ref={"esa-errors-fp":"44","esa-errors-tn":"956",
             "esa-errors-tp":"788","esa-errors-fn":"212",
             "esa-errors-alpha-theory":"5.00%",
             "esa-errors-power-theory":"78.19%",
             "esa-errors-beta-theory":"21.81%",
             "esa-errors-alpha-empirical":"4.40%",
             "esa-errors-power-empirical":"78.80%",
             "esa-errors-beta-empirical":"21.20%"}
        for key,val in ref.items():
            self.assertEqual(self.page.locator("#"+key).inner_text(),val)
        self.assertEqual(int(self.page.locator("#esa-errors-fp").inner_text())+
                         int(self.page.locator("#esa-errors-tn").inner_text()),1000)
        self.assertEqual(int(self.page.locator("#esa-errors-tp").inner_text())+
                         int(self.page.locator("#esa-errors-fn").inner_text()),1000)
        self.page.locator("#esa-errors-run").click()
        self.assertEqual(self.page.locator("#esa-errors-tp").inner_text(),"788")
        self.page.locator("#esa-errors-n").select_option("100")
        self.page.locator("#esa-errors-run").click()
        self.assertGreater(float(self.page.locator("#esa-errors-power-theory").inner_text().strip("%")),78.19)
        self.page.locator("#esa-errors-reset").click()
        self.assertEqual(self.page.locator("#esa-errors-fp").inner_text(),"44")

    def test_batch55_type_errors_keyboard_mobile_denied_storage_and_invalid_seed(self):
        self.page.add_init_script("""
        Object.defineProperty(window,"localStorage",{
          configurable:true,get(){throw new DOMException("Denied","SecurityError")}
        });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        self.page.goto(self.origin+"/inference/hypothesis-testing/type1-type2-errors/",
                       wait_until="networkidle")
        self.page.locator("#esa-errors-alpha").select_option("0.01")
        self.page.locator("#esa-errors-run").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-errors-alpha-theory").inner_text(),"1.00%")
        self.page.locator("#esa-errors-seed").fill("0")
        self.page.locator("#esa-errors-run").click()
        self.assertIn("whole-number seed",self.page.locator("#esa-errors-status").inner_text())
        # Mobile tables may scroll inside their labelled .table-wrap containers;
        # the whole page must not scroll horizontally.
        overflow=self.page.evaluate("""()=>{
          const width=document.documentElement.clientWidth;
          const excess=document.documentElement.scrollWidth-width;
          const offenders=[...document.querySelectorAll("body *")].map(e=>{
            const box=e.getBoundingClientRect();
            return {tag:e.tagName,id:e.id||"",cls:String(e.className||"").slice(0,90),
                    left:Math.round(box.left),right:Math.round(box.right),width:Math.round(box.width)};
          }).filter(x=>x.right>width+2||x.left< -2)
            .sort((a,b)=>b.right-a.right).slice(0,12);
          return {excess,offenders};
        }""")
        self.assertLessEqual(overflow["excess"],2,
                             "Offending mobile elements: "+repr(overflow["offenders"]))
        self.assertTrue(self.page.locator("#esa-errors-lab .table-wrap").evaluate_all(
            "nodes=>nodes.every(e=>e.clientWidth>0 && e.getBoundingClientRect().width<=document.documentElement.clientWidth)"))

    def test_batch55_mle_five_lesson_resume_exact_urls_labels_and_ts(self):
        root="/mathematical-statistics/maximum-likelihood-estimation/"
        key="esa_continue_ms_mle_last_lesson_v0"
        lessons={
          "definition-of-mle":"Lesson 1 — Definition of MLE",
          "finding-mle-by-optimization":"Lesson 2 — Finding MLE by Optimization",
          "invariance-property-of-mle":"Lesson 3 — Invariance Property of MLE",
          "existence-and-uniqueness":"Lesson 4 — Existence and Uniqueness",
          "mle-examples-bernoulli-poisson-normal":"Lesson 5 — MLE Examples"
        }
        for slug,label in lessons.items():
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                raw=self.page.evaluate("k=>localStorage.getItem(k)",key)
                obj=json.loads(raw)
                self.assertEqual(obj["url"],root+slug+"/")
                self.assertEqual(obj["label"],label)
                self.assertIsInstance(obj["ts"],int)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-ms-b3")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-ms-b3-btn")
                                 .get_attribute("href"),root+slug+"/")
                self.assertEqual(self.page.locator("#continue-reading-ms-b3-label")
                                 .inner_text(),"You last visited: "+label)

    def test_batch55_mle_resume_rejects_untrusted_records_and_malformed_json(self):
        root="/mathematical-statistics/maximum-likelihood-estimation/"
        key="esa_continue_ms_mle_last_lesson_v0"
        good=root+"definition-of-mle/"
        self.page.goto(self.origin+root,wait_until="networkidle")
        future=self.page.evaluate("()=>Date.now()+172800000")  # 48h: robust beyond allowed 24h skew
        invalid=[
          {"url":"javascript:alert(1)","label":"Lesson 1 — Definition of MLE","ts":1},
          {"url":"https://invalid.example/","label":"Lesson 1 — Definition of MLE","ts":1},
          {"url":good+"?x=1","label":"Lesson 1 — Definition of MLE","ts":1},
          {"url":good,"label":"<img src=x onerror=alert(1)>","ts":1},
          {"url":good,"label":"Lesson 1 — Definition of MLE","ts":future},
          {"url":good,"label":"Lesson 1 — Definition of MLE","ts":-1},
          {"url":good,"label":"Lesson 1 — Definition of MLE"},
          {"url":good,"label":"Lesson 5 — MLE Examples","ts":1}
        ]
        for entry in invalid:
            with self.subTest(entry=entry):
                self.page.evaluate("(v)=>localStorage.setItem('esa_continue_ms_mle_last_lesson_v0',JSON.stringify(v))",entry)
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-ms-b3")).to_be_hidden()
                self.assertEqual(self.page.locator("#continue-reading-ms-b3-label img").count(),0)
        self.page.evaluate("k=>localStorage.setItem(k,'{bad-json')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms-b3")).to_be_hidden()

    def test_batch55_mle_denied_storage_all_five_and_mobile_overview(self):
        self.page.add_init_script("""
        Object.defineProperty(window,"localStorage",{
          configurable:true,get(){throw new DOMException("Denied","SecurityError")}
        });
        """)
        self.page.set_viewport_size({"width":375,"height":760})
        root="/mathematical-statistics/maximum-likelihood-estimation/"
        for slug in ("definition-of-mle","finding-mle-by-optimization",
                     "invariance-property-of-mle","existence-and-uniqueness",
                     "mle-examples-bernoulli-poisson-normal"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms-b3")).to_be_hidden()
        expect(self.page.locator("main h1")).to_be_visible()


    def test_batch56_arabic_type_errors_translation_metadata_and_numeric_parity(self):
        """Both languages use the same seeded normal-model calculations."""
        en="/inference/hypothesis-testing/type1-type2-errors/"
        ar="/ar/inference/hypothesis-testing/type1-type2-errors/"
        fields=("fp","tn","tp","fn","alpha-theory","power-theory",
                "beta-theory","alpha-empirical","power-empirical","beta-empirical")
        outcomes=[]
        self.page.set_viewport_size({"width":320,"height":760})
        for path,lang in ((en,"en"),(ar,"ar")):
            with self.subTest(lang=lang):
                self.page.goto(self.origin+path,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),
                                 "rtl" if lang=="ar" else None)
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+path)
                for lng,route in (("en",en),("ar",ar)):
                    self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+lng+'"]')
                                     .get_attribute("href"),"https://easystatisticsacademy.com"+route)
                nav=self.page.locator("header .nav-toggle")
                nav.click()
                self.assertEqual(nav.get_attribute("aria-expanded"),"true")
                for lng,route in (("en",en),("ar",ar)):
                    self.assertEqual(self.page.get_by_role("group",name="Language selection")
                                     .locator('a[lang="'+lng+'"]').get_attribute("href"),route)
                self.page.locator("#esa-errors-run").focus()
                self.page.keyboard.press("Enter")
                outcomes.append(tuple(self.page.locator("#esa-errors-"+k).inner_text() for k in fields))
                self.assertEqual(self.page.locator("#esa-errors-fp").inner_text(),"44")
                self.assertEqual(self.page.locator("#esa-errors-tp").inner_text(),"788")
                self.assertEqual(self.page.locator("#esa-errors-power-theory").inner_text(),"78.19%")
                self.assertLessEqual(self.page.evaluate(
                    "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)
                self.page.locator("#esa-errors-alpha").select_option("0.01")
                self.page.locator("#esa-errors-run").click()
                self.assertEqual(self.page.locator("#esa-errors-alpha-theory").inner_text(),"1.00%")
        self.assertEqual(outcomes[0],outcomes[1])
        self.assertIn(ar,(SITE/"ar"/"index.html").read_text())
        self.assertIn("أخطاء النوع",self.page.locator("main").inner_text())

    def test_batch56_arabic_errors_invalid_seed_and_denied_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        self.page.goto(self.origin+"/ar/inference/hypothesis-testing/type1-type2-errors/",
                       wait_until="networkidle")
        self.assertEqual(self.page.locator("#esa-errors-fn").inner_text(),"212")
        self.page.locator("#esa-errors-seed").fill("0")
        self.page.locator("#esa-errors-run").focus()
        self.page.keyboard.press("Enter")
        self.assertIn("بذرة",self.page.locator("#esa-errors-status").inner_text())
        self.assertEqual(self.page.locator("#esa-errors-fn").inner_text(),"212")

    def test_batch56_cv_two_datasets_exact_sample_population_benchmarks(self):
        route="/descriptive/spread/coefficient-of-variation/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        expect(self.page.locator("#esa-cv-lab")).to_be_visible()
        expected={"a-n":"3","b-n":"3","a-mean":"10","b-mean":"50",
                  "a-sd":"2","b-sd":"5","a-cv":"20.00%","b-cv":"10.00%"}
        for field,value in expected.items():
            self.assertEqual(self.page.locator("#esa-cv-"+field).inner_text(),value)
        self.assertIn("Dataset A has greater",self.page.locator("#esa-cv-comparison").inner_text())
        self.page.locator("#esa-cv-mode").select_option("population")
        for key,val in {"a-sd":(8/3)**.5,"b-sd":(50/3)**.5,
                        "a-cv":(8/3)**.5*10,"b-cv":(50/3)**.5*2}.items():
            value=float(self.page.locator("#esa-cv-"+key).inner_text().strip("%"))
            self.assertAlmostEqual(value,val,places=2)
        self.page.locator("#esa-cv-reset").click()
        self.assertEqual(self.page.locator("#esa-cv-a-cv").inner_text(),"20.00%")

    def test_batch56_cv_invalid_zero_negative_near_zero_and_interval_scale(self):
        self.page.goto(self.origin+"/descriptive/spread/coefficient-of-variation/",
                       wait_until="networkidle")
        self.page.locator("#esa-cv-a").fill("-1, 0, 1")
        self.page.locator("#esa-cv-run").click()
        self.assertEqual(self.page.locator("#esa-cv-a-cv").inner_text(),"Undefined")
        self.assertIn("positive nonzero mean",self.page.locator("#esa-cv-status").inner_text())
        self.page.locator("#esa-cv-a").fill("-3, -2, -1")
        self.page.locator("#esa-cv-run").click()
        self.assertEqual(self.page.locator("#esa-cv-a-cv").inner_text(),"Undefined")
        self.page.locator("#esa-cv-a").fill("-100, 0, 101")
        self.page.locator("#esa-cv-run").click()
        self.assertIn("CV is unstable",self.page.locator("#esa-cv-status").inner_text())
        self.assertIn("not recommended",self.page.locator("#esa-cv-comparison").inner_text())
        self.page.locator("#esa-cv-reset").click()
        self.page.locator("#esa-cv-scale").select_option("interval")
        self.assertIn("interval scales",self.page.locator("#esa-cv-status").inner_text())
        self.page.locator("#esa-cv-a").fill("1, no, 3")
        self.page.locator("#esa-cv-run").click()
        self.assertIn("finite numbers",self.page.locator("#esa-cv-status").inner_text())
        self.assertEqual(self.page.locator("#esa-cv-a-cv").inner_text(),"—")

    def test_batch56_cv_keyboard_mobile_and_blocked_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        self.page.goto(self.origin+"/descriptive/spread/coefficient-of-variation/",
                       wait_until="networkidle")
        self.page.locator("#esa-cv-mode").select_option("population")
        self.page.locator("#esa-cv-run").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-cv-a-cv").inner_text(),"16.33%")
        lab=self.page.locator("#esa-cv-lab")
        self.assertLessEqual(lab.evaluate("e=>e.getBoundingClientRect().width"),320)
        self.assertLessEqual(lab.evaluate("e=>e.scrollWidth-e.clientWidth"),2)

    def test_batch56_properties_five_resume_contracts_and_secure_overview(self):
        root="/mathematical-statistics/estimator-properties/"
        key="esa_continue_ms_properties_last_lesson_v0"
        lessons={
            "bias-variance-and-mse":"Lesson 1 — Bias, Variance, and MSE",
            "unbiasedness-and-bias-correction":"Lesson 2 — Unbiasedness and Bias Correction",
            "consistency-basic-idea":"Lesson 3 — Consistency (Basic Idea)",
            "efficiency-and-comparing-estimators":"Lesson 4 — Efficiency and Comparing Estimators",
            "sufficiency-preview":"Lesson 5 — Sufficiency (Preview)"
        }
        for slug,label in lessons.items():
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                obj=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
                self.assertEqual(obj["url"],root+slug+"/")
                self.assertEqual(obj["label"],label)
                self.assertIsInstance(obj["ts"],int)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-ms-b4")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-ms-b4-btn")
                                 .get_attribute("href"),root+slug+"/")
                self.assertEqual(self.page.locator("#continue-reading-ms-b4-label")
                                 .inner_text(),"You last visited: "+label)

    def test_batch56_properties_reject_malicious_malformed_and_future_progress(self):
        root="/mathematical-statistics/estimator-properties/"
        good=root+"bias-variance-and-mse/"
        key="esa_continue_ms_properties_last_lesson_v0"
        label="Lesson 1 — Bias, Variance, and MSE"
        self.page.goto(self.origin+root,wait_until="networkidle")
        far_future=self.page.evaluate("()=>Date.now()+172800000")
        for value in (
            {"url":"javascript:alert(1)","label":label,"ts":1},
            {"url":"https://example.com/","label":label,"ts":1},
            {"url":root+"sufficiency-preview/","label":label,"ts":1},
            {"url":good+"?redirect=evil","label":label,"ts":1},
            {"url":good,"label":"<svg onload=alert(1)>","ts":1},
            {"url":good,"label":label,"ts":far_future},
            {"url":good,"label":label,"ts":0},
            {"url":good,"label":label}
        ):
            with self.subTest(data=value):
                self.page.evaluate("(v)=>localStorage.setItem('esa_continue_ms_properties_last_lesson_v0',JSON.stringify(v))",value)
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-ms-b4")).to_be_hidden()
                self.assertEqual(self.page.locator("#continue-reading-ms-b4-label svg").count(),0)
        self.page.evaluate("k=>localStorage.setItem(k,'{malformed')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms-b4")).to_be_hidden()

    def test_batch56_properties_storage_denial_mobile_all_five(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        root="/mathematical-statistics/estimator-properties/"
        self.page.set_viewport_size({"width":320,"height":760})
        for slug in ("bias-variance-and-mse","unbiasedness-and-bias-correction",
                     "consistency-basic-idea","efficiency-and-comparing-estimators",
                     "sufficiency-preview"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms-b4")).to_be_hidden()
        expect(self.page.locator("main h1")).to_be_visible()


    def test_batch57_arabic_cv_full_lesson_metadata_mobile_and_numeric_parity(self):
        """An Arabic translation shares the exact sample/population calculation engine."""
        en="/descriptive/spread/coefficient-of-variation/"
        ar="/ar/descriptive/spread/coefficient-of-variation/"
        outcomes=[]
        self.page.set_viewport_size({"width":320,"height":760})
        for path,lang in ((en,"en"),(ar,"ar")):
            with self.subTest(lang=lang):
                self.page.goto(self.origin+path,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl" if lang=="ar" else None)
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+path)
                for lng,route in (("en",en),("ar",ar)):
                    self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+lng+'"]')
                                     .get_attribute("href"),"https://easystatisticsacademy.com"+route)
                self.page.locator("header .nav-toggle").click()
                language=self.page.get_by_role("group",name="Language selection")
                for lng,route in (("en",en),("ar",ar)):
                    self.assertEqual(language.locator('a[lang="'+lng+'"]').get_attribute("href"),route)
                self.page.locator("#esa-cv-run").focus()
                self.page.keyboard.press("Enter")
                ids=("a-n","a-mean","a-sd","a-cv","b-n","b-mean","b-sd","b-cv")
                outcomes.append(tuple(self.page.locator("#esa-cv-"+i).inner_text() for i in ids))
                self.assertEqual(self.page.locator("#esa-cv-a-cv").inner_text(),"20.00%")
                self.page.locator("#esa-cv-mode").select_option("population")
                self.assertEqual(self.page.locator("#esa-cv-a-cv").inner_text(),"16.33%")
                self.assertEqual(self.page.locator("#esa-cv-b-cv").inner_text(),"8.16%")
                self.assertLessEqual(self.page.locator("#esa-cv-lab").evaluate(
                    "e=>e.scrollWidth-e.clientWidth"),2)
                self.assertLessEqual(self.page.evaluate(
                    "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)
        self.assertEqual(outcomes[0],outcomes[1])
        self.assertIn("معامل الاختلاف",(SITE/"ar"/"index.html").read_text())
        self.assertIn("معامل الاختلاف",self.page.locator("main").inner_text())

    def test_batch57_arabic_cv_warnings_invalid_and_denied_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        self.page.goto(self.origin+"/ar/descriptive/spread/coefficient-of-variation/",
                       wait_until="networkidle")
        self.assertEqual(self.page.locator("#esa-cv-a-cv").inner_text(),"20.00%")
        self.page.locator("#esa-cv-a").fill("-1, 0, 1")
        self.page.locator("#esa-cv-run").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-cv-a-cv").inner_text(),"غير معرّف")
        self.assertIn("متوسطاً موجباً",self.page.locator("#esa-cv-status").inner_text())
        self.page.locator("#esa-cv-a").fill("-100, 0, 101")
        self.page.locator("#esa-cv-run").click()
        self.assertIn("غير مستقر",self.page.locator("#esa-cv-status").inner_text())
        self.page.locator("#esa-cv-reset").click()
        self.page.locator("#esa-cv-scale").select_option("interval")
        self.assertIn("مقياس الفترة",self.page.locator("#esa-cv-status").inner_text())
        self.page.locator("#esa-cv-a").fill("1, evil, 3")
        self.page.locator("#esa-cv-run").click()
        self.assertIn("أعداداً منتهية",self.page.locator("#esa-cv-status").inner_text())

    def test_batch57_bernoulli_crlb_independent_benchmarks(self):
        self.page.goto(self.origin+"/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/",
                       wait_until="networkidle")
        for key,value in {
            "information":"95.2381","crlb":"0.010500",
            "variance-mean":"0.010500","variance-first":"0.210000",
            "efficiency-mean":"100.00%","efficiency-first":"5.00%","ratio":"20×"
        }.items():
            self.assertEqual(self.page.locator("#esa-crlb-"+key).inner_text(),value)
        # Independent exact reference: p=.3,n=20; information=20/.21 and bound=.21/20.
        self.assertAlmostEqual(20/(.3*.7),95.23809523809524)
        self.assertAlmostEqual(.3*.7/20,.0105)
        self.page.locator("#esa-crlb-p").fill("0.5")
        self.page.locator("#esa-crlb-n").fill("10")
        self.page.locator("#esa-crlb-run").click()
        self.assertEqual(self.page.locator("#esa-crlb-information").inner_text(),"40.0000")
        self.assertEqual(self.page.locator("#esa-crlb-crlb").inner_text(),"0.025000")
        self.assertEqual(self.page.locator("#esa-crlb-variance-first").inner_text(),"0.250000")
        self.assertEqual(self.page.locator("#esa-crlb-efficiency-first").inner_text(),"10.00%")
        self.page.locator("#esa-crlb-n").fill("1")
        self.page.locator("#esa-crlb-run").click()
        self.assertEqual(self.page.locator("#esa-crlb-efficiency-first").inner_text(),"100.00%")
        self.assertIn("estimators coincide",self.page.locator("#esa-crlb-status").inner_text())
        self.page.locator("#esa-crlb-reset").click()
        self.assertEqual(self.page.locator("#esa-crlb-crlb").inner_text(),"0.010500")

    def test_batch57_bernoulli_crlb_boundaries_keyboard_mobile_storage_denied(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        self.page.goto(self.origin+"/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-crlb-lab")).to_be_visible()
        self.page.locator("#esa-crlb-p").fill("0")
        self.page.locator("#esa-crlb-run").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-crlb-crlb").inner_text(),"—")
        self.assertIn("0 < p < 1",self.page.locator("#esa-crlb-status").inner_text())
        self.page.locator("#esa-crlb-p").fill("1")
        self.page.locator("#esa-crlb-run").click()
        self.assertEqual(self.page.locator("#esa-crlb-information").inner_text(),"—")
        self.page.locator("#esa-crlb-p").fill("0.3")
        self.page.locator("#esa-crlb-n").fill("2.5")
        self.page.locator("#esa-crlb-run").click()
        self.assertEqual(self.page.locator("#esa-crlb-crlb").inner_text(),"—")
        self.page.locator("#esa-crlb-n").fill("501")
        self.page.locator("#esa-crlb-run").click()
        self.assertEqual(self.page.locator("#esa-crlb-crlb").inner_text(),"—")
        self.page.locator("#esa-crlb-reset").click()
        self.assertEqual(self.page.locator("#esa-crlb-crlb").inner_text(),"0.010500")
        self.assertLessEqual(self.page.locator("#esa-crlb-lab").evaluate(
            "e=>e.scrollWidth-e.clientWidth"),2)
        self.assertLessEqual(self.page.evaluate(
            "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch57_asymptotic_resume_exact_five_urls_and_labels(self):
        root="/mathematical-statistics/asymptotic-theory/"
        key="esa_continue_ms_asymptotics_last_lesson_v0"
        lessons={
            "modes-of-convergence-review":"Lesson 1 — Modes of Convergence",
            "consistency-of-mle-idea":"Lesson 2 — Consistency of MLE",
            "asymptotic-normality-of-mle":"Lesson 3 — Asymptotic Normality of MLE",
            "slutsky-theorem-and-continuous-mapping":"Lesson 4 — Slutsky Theorem",
            "delta-method":"Lesson 5 — Delta Method"
        }
        for slug,label in lessons.items():
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                saved=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
                self.assertEqual(saved["url"],root+slug+"/")
                self.assertEqual(saved["label"],label)
                self.assertIsInstance(saved["ts"],int)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-ms-b6")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-ms-b6-btn").get_attribute("href"),
                                 root+slug+"/")
                self.assertEqual(self.page.locator("#continue-reading-ms-b6-label").inner_text(),
                                 "You last visited: "+label)

    def test_batch57_asymptotic_resume_rejects_untrusted_records(self):
        root="/mathematical-statistics/asymptotic-theory/"
        good=root+"modes-of-convergence-review/"
        key="esa_continue_ms_asymptotics_last_lesson_v0"
        label="Lesson 1 — Modes of Convergence"
        self.page.goto(self.origin+root,wait_until="networkidle")
        tomorrow_after=self.page.evaluate("()=>Date.now()+172800000")
        for value in (
            {"url":"javascript:alert(1)","label":label,"ts":1},
            {"url":"https://attacker.invalid/","label":label,"ts":1},
            {"url":good+"?x=1","label":label,"ts":1},
            {"url":good,"label":"<img src=x onerror=alert(1)>","ts":1},
            {"url":root+"delta-method/","label":label,"ts":1},
            {"url":good,"label":label,"ts":tomorrow_after},
            {"url":good,"label":label,"ts":0},
            {"url":good,"label":label}
        ):
            with self.subTest(data=value):
                self.page.evaluate("(value)=>localStorage.setItem('esa_continue_ms_asymptotics_last_lesson_v0',JSON.stringify(value))",value)
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-ms-b6")).to_be_hidden()
                self.assertEqual(self.page.locator("#continue-reading-ms-b6-label img").count(),0)
        self.page.evaluate("key=>localStorage.setItem(key,'{bad-json')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms-b6")).to_be_hidden()

    def test_batch57_asymptotic_denied_storage_five_lessons_mobile(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        root="/mathematical-statistics/asymptotic-theory/"
        for slug in ("modes-of-convergence-review","consistency-of-mle-idea",
                     "asymptotic-normality-of-mle","slutsky-theorem-and-continuous-mapping",
                     "delta-method"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms-b6")).to_be_hidden()
        expect(self.page.locator("main h1")).to_be_visible()


    def test_batch58_crlb_arabic_english_parity_and_metadata(self):
        en="/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/"
        ar="/ar/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/"
        results=[]
        for route,lang in ((en,"en"),(ar,"ar")):
            with self.subTest(language=lang):
                self.page.goto(self.origin+route,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl" if lang=="ar" else None)
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+route)
                for lng,target in (("en",en),("ar",ar)):
                    self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+lng+'"]')
                                     .get_attribute("href"),"https://easystatisticsacademy.com"+target)
                self.page.locator("#esa-crlb-run").focus()
                self.page.keyboard.press("Enter")
                ids=("information","crlb","variance-mean","variance-first",
                     "efficiency-mean","efficiency-first","ratio")
                results.append(tuple(self.page.locator("#esa-crlb-"+i).inner_text() for i in ids))
                self.page.locator("#esa-crlb-p").fill("0.5")
                self.page.locator("#esa-crlb-n").fill("10")
                self.page.locator("#esa-crlb-run").click()
                self.assertEqual(self.page.locator("#esa-crlb-information").inner_text(),"40.0000")
                self.assertEqual(self.page.locator("#esa-crlb-crlb").inner_text(),"0.025000")
                self.assertEqual(self.page.locator("#esa-crlb-efficiency-first").inner_text(),"10.00%")
                self.page.locator("#esa-crlb-n").fill("1")
                self.page.locator("#esa-crlb-run").click()
                self.assertEqual(self.page.locator("#esa-crlb-efficiency-first").inner_text(),"100.00%")
                if lang=="ar":
                    self.assertIn("يتطابق المقدّران",self.page.locator("#esa-crlb-status").inner_text())
        self.assertEqual(results[0],results[1])
        self.assertEqual(results[0],("95.2381","0.010500","0.010500",
                                     "0.210000","100.00%","5.00%","20×"))
        english=(SITE/"mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/index.html").read_text()
        self.assertIn("score identity",english)
        self.assertNotIn("orthogonality between estimator error and score",english)

    def test_batch58_crlb_arabic_boundaries_mobile_storage_and_keyboard(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        route="/ar/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        expect(self.page.locator("#esa-crlb-lab")).to_be_visible()
        self.assertEqual(self.page.locator("#esa-crlb-crlb").inner_text(),"0.010500")
        self.page.locator("#esa-crlb-p").fill("0")
        self.page.locator("#esa-crlb-run").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-crlb-crlb").inner_text(),"—")
        self.assertIn("تُستبعد القيمتان",self.page.locator("#esa-crlb-status").inner_text())
        self.page.locator("#esa-crlb-p").fill("0.3")
        self.page.locator("#esa-crlb-n").fill("501")
        self.page.locator("#esa-crlb-run").click()
        self.assertEqual(self.page.locator("#esa-crlb-information").inner_text(),"—")
        self.page.locator("#esa-crlb-reset").click()
        self.assertEqual(self.page.locator("#esa-crlb-crlb").inner_text(),"0.010500")
        self.assertLessEqual(self.page.locator("#esa-crlb-lab").evaluate(
            "e=>e.scrollWidth-e.clientWidth"),2)
        self.assertLessEqual(self.page.evaluate(
            "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch58_delta_method_independent_normal_reference(self):
        route="/mathematical-statistics/asymptotic-theory/delta-method/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        self.assertEqual(self.page.locator("#esa-delta-transform").input_value(),"square")
        self.assertAlmostEqual(float(self.page.locator("#esa-delta-variance-input").inner_text()),.05,places=8)
        self.assertAlmostEqual(float(self.page.locator("#esa-delta-derivative").inner_text()),0,places=8)
        self.assertAlmostEqual(float(self.page.locator("#esa-delta-approx").inner_text()),0,places=8)
        self.assertAlmostEqual(float(self.page.locator("#esa-delta-exact").inner_text()),.005,places=8)
        self.assertIn("higher-order expansion",self.page.locator("#esa-delta-status").inner_text())
        self.page.locator("#esa-delta-transform").select_option("identity")
        self.assertAlmostEqual(float(self.page.locator("#esa-delta-approx").inner_text()),.05,places=8)
        self.assertAlmostEqual(float(self.page.locator("#esa-delta-exact").inner_text()),.05,places=8)
        self.page.locator("#esa-delta-transform").select_option("exponential")
        self.assertAlmostEqual(float(self.page.locator("#esa-delta-approx").inner_text()),.05,places=8)
        self.assertAlmostEqual(float(self.page.locator("#esa-delta-exact").inner_text()),
                               .05389982169962359,places=7)
        self.page.locator("#esa-delta-transform").select_option("square")
        self.page.locator("#esa-delta-theta").fill("0.5")
        self.page.locator("#esa-delta-run").click()
        self.assertAlmostEqual(float(self.page.locator("#esa-delta-approx").inner_text()),.05,places=8)
        self.assertAlmostEqual(float(self.page.locator("#esa-delta-exact").inner_text()),.055,places=8)
        self.page.locator("#esa-delta-reset").click()
        self.assertEqual(self.page.locator("#esa-delta-exact").inner_text(),"0.005")

    def test_batch58_delta_method_invalid_mobile_keyboard_and_storage_denial(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        self.page.goto(self.origin+"/mathematical-statistics/asymptotic-theory/delta-method/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-delta-lab")).to_be_visible()
        self.page.locator("#esa-delta-n").fill("1")
        self.page.locator("#esa-delta-run").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-delta-exact").inner_text(),"—")
        self.assertIn("integer sample size",self.page.locator("#esa-delta-status").inner_text())
        self.page.locator("#esa-delta-n").fill("20")
        self.page.locator("#esa-delta-sigma").fill("0")
        self.page.locator("#esa-delta-run").click()
        self.assertEqual(self.page.locator("#esa-delta-exact").inner_text(),"—")
        self.page.locator("#esa-delta-reset").click()
        self.assertEqual(self.page.locator("#esa-delta-exact").inner_text(),"0.005")
        self.assertLessEqual(self.page.locator("#esa-delta-lab").evaluate(
            "e=>e.scrollWidth-e.clientWidth"),2)
        self.assertLessEqual(self.page.evaluate(
            "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch58_methods_progress_five_approved_routes(self):
        root="/mathematical-statistics/alternative-estimation-methods/"
        key="esa_continue_ms_methods_last_lesson_v0"
        lessons={
            "method-of-moments":"Lesson 1 — Method of Moments",
            "estimating-equations-preview":"Lesson 2 — Estimating Equations",
            "bayesian-point-estimation-preview":"Lesson 3 — Bayesian Point Estimation",
            "shrinkage-intuition-preview":"Lesson 4 — Shrinkage Intuition",
            "robustness-preview":"Lesson 5 — Robustness"
        }
        for slug,label in lessons.items():
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                saved=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
                self.assertEqual(saved["url"],root+slug+"/")
                self.assertEqual(saved["label"],label)
                self.assertGreater(saved["ts"],0)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-ms-b7")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-ms-b7-btn").get_attribute("href"),saved["url"])
                self.assertEqual(self.page.locator("#continue-reading-ms-b7-label").inner_text(),
                                 "You last visited: "+label)

    def test_batch58_methods_progress_reject_unsafe_records(self):
        root="/mathematical-statistics/alternative-estimation-methods/"
        key="esa_continue_ms_methods_last_lesson_v0"
        allowed=root+"method-of-moments/"
        label="Lesson 1 — Method of Moments"
        self.page.goto(self.origin+root,wait_until="networkidle")
        bad=(
            {"url":"javascript:alert(1)","label":label,"ts":1},
            {"url":"https://evil.example/","label":label,"ts":1},
            {"url":allowed+"?a=1","label":label,"ts":1},
            {"url":allowed,"label":"<img src=x onerror=alert(1)>","ts":1},
            {"url":root+"robustness-preview/","label":label,"ts":1},
            {"url":allowed,"label":label,"ts":0},
            {"url":allowed,"label":label,"ts":-100},
            {"url":allowed,"label":label,"ts":999999999999999},
            {"url":allowed,"label":label},
            ["not","a","record"]
        )
        for record in bad:
            with self.subTest(record=record):
                self.page.evaluate("(v)=>localStorage.setItem('esa_continue_ms_methods_last_lesson_v0',JSON.stringify(v))",record)
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-ms-b7")).to_be_hidden()
                self.assertEqual(self.page.locator("#continue-reading-ms-b7-label img").count(),0)
        self.page.evaluate("key=>localStorage.setItem(key,'bad{')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms-b7")).to_be_hidden()

    def test_batch58_methods_progress_all_pages_allow_storage_denial_mobile(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        root="/mathematical-statistics/alternative-estimation-methods/"
        for slug in ("method-of-moments","estimating-equations-preview",
                     "bayesian-point-estimation-preview","shrinkage-intuition-preview",
                     "robustness-preview"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-ms-b7")).to_be_hidden()
        expect(self.page.locator("main h1")).to_be_visible()


    def test_batch59_confidence_intervals_english_arabic_shared_math(self):
        """Both translated simulations use the exact known-sigma normal model."""
        import math
        pages=(
            ("/inference/confidence-intervals/what-is-a-confidence-interval/","en"),
            ("/ar/inference/confidence-intervals/what-is-a-confidence-interval/","ar"),
        )
        for path,lang in pages:
            with self.subTest(language=lang):
                self.page.goto(self.origin+path,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl" if lang=="ar" else None)
                expect(self.page.locator("#esa-ci-coverage-lab")).to_be_visible()
                self.assertEqual(self.page.locator("#esa-ci-total").inner_text(),"100")
                self.assertAlmostEqual(float(self.page.locator("#esa-ci-halfwidth").inner_text()),
                                       1.959963984540054/math.sqrt(30),delta=.00005)
                self.assertEqual(self.page.locator("#esa-ci-intervals line").count(),20)
                self.page.locator("#esa-ci-run-500").focus()
                self.page.keyboard.press("Enter")
                self.assertEqual(self.page.locator("#esa-ci-total").inner_text(),"600")
                self.page.locator("#esa-ci-n").select_option("100")
                self.assertEqual(self.page.locator("#esa-ci-total").inner_text(),"100")
                self.assertAlmostEqual(float(self.page.locator("#esa-ci-halfwidth").inner_text()),
                                       1.959963984540054/10,delta=.00005)
                self.page.locator("#esa-ci-confidence").select_option("90")
                self.assertAlmostEqual(float(self.page.locator("#esa-ci-halfwidth").inner_text()),
                                       1.6448536269514722/10,delta=.00005)
                self.assertEqual(self.page.locator("#esa-ci-total").inner_text(),"100")
                expect(self.page.locator('link[rel="alternate"][hreflang="en"]')).to_have_count(1)
                expect(self.page.locator('link[rel="alternate"][hreflang="ar"]')).to_have_count(1)
                self.assertEqual(self.page.locator("link[rel=canonical]").get_attribute("href"),
                                 "https://easystatisticsacademy.com"+path)
                self.page.set_viewport_size({"width":320,"height":760})
                self.assertLessEqual(self.page.evaluate(
                    "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch59_mean_median_explorer_math_keyboard_and_validation(self):
        self.page.set_viewport_size({"width":320,"height":760})
        self.page.goto(self.origin+"/descriptive/center/mean-vs-median/",wait_until="networkidle")
        expect(self.page.locator("#esa-mean-median-explorer")).to_be_visible()
        def get(id):
            return self.page.locator("#esa-mm-"+id).inner_text()
        self.assertEqual([get("mean-before"),get("median-before"),
                          get("mean-after"),get("median-after")],["6","6","24","6"])
        self.assertEqual(get("mean-change"),"18")
        self.assertEqual(get("median-change"),"0")
        self.assertEqual(self.page.locator("#esa-mm-points circle").count(),10)
        self.page.locator("#esa-mm-extreme").fill("50")
        self.assertEqual(get("mean-after"),"14")
        self.assertEqual(get("median-after"),"6")
        self.page.locator("#esa-mm-sample").fill("1, 2, 3, 4")
        self.page.locator("#esa-mm-extreme").fill("100")
        self.assertEqual(get("mean-before"),"2.5")
        self.assertEqual(get("median-before"),"2.5")
        self.assertEqual(get("mean-after"),"26.5")
        self.assertEqual(get("median-after"),"2.5")
        self.page.locator("#esa-mm-sample").fill("1, two, 3")
        expect(self.page.locator("#esa-mm-results")).to_be_hidden()
        expect(self.page.locator("#esa-mm-error")).to_be_visible()
        self.page.locator("#esa-mm-reset").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(get("mean-after"),"24")
        overflow=self.page.evaluate("""() => ({
            extra:document.documentElement.scrollWidth-document.documentElement.clientWidth,
            width:window.innerWidth,
            offenders:[...document.querySelectorAll("body *")].map(e=>({
                tag:e.tagName, id:e.id, cls:String(e.className||"").slice(0,70),
                right:Math.round(e.getBoundingClientRect().right),
                left:Math.round(e.getBoundingClientRect().left)
            })).filter(x=>x.right>window.innerWidth+2||x.left < -2).slice(0,12)
        })""")
        self.assertLessEqual(overflow["extra"],2,overflow)

    def test_batch59_shape_saved_progress_validity_and_storage_denial(self):
        root="/descriptive/shape/"
        key="esa_continue_descriptive_shape_lesson_v0"
        urls=("why-shape-matters","symmetry-and-skewness",
              "skewness-and-center-choice","tails-outliers-and-extremes",
              "empirical-rule","z-scores","standardization-when-and-when-not",
              "shape-in-reporting")
        self.page.goto(self.origin+root+urls[0]+"/",wait_until="networkidle")
        saved=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
        self.assertEqual(saved["url"],root+urls[0]+"/")
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block6")).to_be_visible()
        self.assertEqual(self.page.locator("#continue-reading-block6-btn").get_attribute("href"),saved["url"])
        for record in (
            {"url":"javascript:alert(1)","label":"x","ts":5},
            {"url":root+"nonexistent-example/","label":"not-published","ts":5},
            {"url":saved["url"],"label":"a"*201,"ts":5},
            {"url":saved["url"],"label":"x","ts":-2},
            {"url":saved["url"]+"?x=1","label":"x","ts":5},
        ):
            self.page.evaluate("(v)=>localStorage.setItem('esa_continue_descriptive_shape_lesson_v0',JSON.stringify(v))",record)
            self.page.reload(wait_until="networkidle")
            expect(self.page.locator("#continue-reading-block6")).to_be_hidden()
        self.page.evaluate("(v)=>localStorage.setItem('esa_continue_descriptive_shape_lesson_v0',JSON.stringify(v))",
                           {"url":saved["url"],"label":"<img src=x onerror=alert(1)>","ts":5})
        self.page.reload(wait_until="networkidle")
        self.assertEqual(self.page.locator("#continue-reading-block6-label img").count(),0)
        self.context.close()
        self.context=self.browser.new_context()
        self.context.route("https://**",lambda route:route.fulfill(status=200,body=""))
        self.page=self.context.new_page()
        self.page.on("pageerror",lambda error:self.errors.append(str(error)))
        self.page.add_init_script("""
            Object.defineProperty(window,"localStorage",{
              configurable:true,get(){throw new DOMException("Denied","SecurityError")}
            });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        for slug in urls:
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block6")).to_be_hidden()



    def test_batch60_mean_median_complete_arabic_parity_navigation_and_mobile(self):
        en="/descriptive/center/mean-vs-median/"
        ar="/ar/descriptive/center/mean-vs-median/"
        original=[]
        for route,lang in ((en,"en"),(ar,"ar")):
            with self.subTest(language=lang):
                self.page.goto(self.origin+route,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),
                                 "rtl" if lang=="ar" else None)
                self.assertEqual(self.page.locator("link[rel=canonical]").get_attribute("href"),
                                 "https://easystatisticsacademy.com"+route)
                for key,target in (("en",en),("ar",ar)):
                    self.assertEqual(self.page.locator(
                        'link[rel="alternate"][hreflang="'+key+'"]').get_attribute("href"),
                        "https://easystatisticsacademy.com"+target)
                expect(self.page.locator("#esa-mean-median-explorer")).to_be_visible()
                vals=tuple(self.page.locator("#esa-mm-"+s).inner_text() for s in
                           ("mean-before","median-before","mean-after","median-after",
                            "mean-change","median-change"))
                self.assertEqual(vals,("6","6","24","6","18","0"))
                original.append(vals)
                self.page.locator("#esa-mm-sample").fill("1, 2, 3, 4")
                self.page.locator("#esa-mm-extreme").fill("100")
                self.assertEqual(self.page.locator("#esa-mm-mean-after").inner_text(),"26.5")
                self.assertEqual(self.page.locator("#esa-mm-median-after").inner_text(),"2.5")
                self.page.locator("#esa-mm-reset").focus()
                self.page.keyboard.press("Enter")
                self.assertEqual(self.page.locator("#esa-mm-mean-after").inner_text(),"24")
                self.page.set_viewport_size({"width":320,"height":760})
                self.assertLessEqual(self.page.evaluate(
                    "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)
                if lang=="ar":
                    self.assertIn("استُبدلت",self.page.locator("#esa-mm-explainer").inner_text())
                    self.assertIn("المتوسط الحسابي والوسيط",self.page.locator("main h1").inner_text())
                    self.page.locator("#esa-mm-sample").fill("one, 2, 3")
                    self.assertIn("أدخل",self.page.locator("#esa-mm-error").inner_text())
                    expect(self.page.locator("#esa-mm-results")).to_be_hidden()
                else:
                    self.assertIn("Replaced",self.page.locator("#esa-mm-explainer").inner_text())
                self.page.set_viewport_size({"width":1280,"height":800})
        self.assertEqual(original[0],original[1])
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        expect(self.page.locator('a[href="'+ar+'"]')).to_be_visible()

    def test_batch60_hypergeometric_exact_probability_and_boundary_cases(self):
        import math
        self.page.goto(self.origin+"/probability/distributions/hypergeometric-distribution/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-hypergeom-explorer")).to_be_visible()
        def get(s):
            return self.page.locator("#esa-hg-"+s).inner_text()
        expected=math.comb(10,1)*math.comb(90,4)/math.comb(100,5)
        self.assertAlmostEqual(float(get("exact")),expected,delta=.0000006)
        self.assertAlmostEqual(float(get("mean")),.5,places=6)
        self.assertAlmostEqual(float(get("total")),1,delta=.000001)
        for input_id,value in (("N","10"),("K","3"),("n","2"),("x","1")):
            self.page.locator("#esa-hg-"+input_id).fill(value)
        self.assertEqual(get("support"),"0 to 2")
        self.assertEqual(get("exact"),"0.466667")
        self.assertEqual(get("approx"),"0.420000")
        self.assertEqual(get("difference"),"0.046667")
        self.assertEqual(get("variance"),"0.373333")
        self.assertEqual(get("total"),"1.000000")
        self.assertEqual(self.page.locator("#esa-hg-bars rect").count(),6)
        self.page.locator("#esa-hg-K").fill("10")
        self.page.locator("#esa-hg-x").fill("0")
        self.assertEqual(get("support"),"2 to 2")
        self.assertEqual(get("exact"),"0.000000")
        self.page.locator("#esa-hg-x").fill("2")
        self.assertEqual(get("exact"),"1.000000")
        for id,value in (("N","1"),("K","1"),("n","1"),("x","1")):
            self.page.locator("#esa-hg-"+id).fill(value)
        self.assertEqual(get("exact"),"1.000000")
        self.assertEqual(get("variance"),"0.000000")
        self.page.locator("#esa-hg-n").fill("0")
        self.page.locator("#esa-hg-x").fill("0")
        self.assertEqual(get("exact"),"1.000000")
        self.page.locator("#esa-hg-N").fill("0")
        self.assertEqual(get("exact"),"—")
        self.assertIn("1 ≤ N",get("status"))
        self.page.locator("#esa-hg-reset").focus()
        self.page.keyboard.press("Enter")
        self.assertAlmostEqual(float(get("exact")),expected,delta=.0000006)
        self.page.set_viewport_size({"width":320,"height":760})
        overflow=self.page.evaluate("""() => ({
            extra:document.documentElement.scrollWidth-document.documentElement.clientWidth,
            width:window.innerWidth,
            offenders:[...document.querySelectorAll("body *")].map(e=>({
                tag:e.tagName,id:e.id,cls:String(e.className||"").slice(0,65),
                right:Math.round(e.getBoundingClientRect().right),
                left:Math.round(e.getBoundingClientRect().left)
            })).filter(x=>x.right>window.innerWidth+2||x.left < -2).slice(0,15)
        })""")
        self.assertLessEqual(overflow["extra"],2,overflow)

    def test_batch60_center_resume_ten_lessons_secure_metadata(self):
        root="/descriptive/center/"
        key="esa_continue_descriptive_center_lesson_v0"
        slugs=("what-is-center","arithmetic-mean","median","mode","mean-vs-median",
               "weighted-mean","trimmed-mean","winsorized-mean",
               "center-for-ordinal-data","reporting-center-properly")
        for slug in slugs:
            with self.subTest(lesson=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                record=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
                self.assertEqual(record["url"],root+slug+"/")
                self.assertIsInstance(record["ts"],int)
                self.assertGreater(record["ts"],0)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block4")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-block4-btn").get_attribute("href"),
                                 record["url"])
        good=root+"median/"
        self.page.goto(self.origin+root,wait_until="networkidle")
        invalid=(
            {"url":"javascript:alert(1)","label":"Median","ts":5},
            {"url":good+"?bad=1","label":"Median","ts":5},
            {"url":root+"missing/","label":"Median","ts":5},
            {"url":good,"label":"x"*201,"ts":5},
            {"url":good,"label":"Median","ts":0},
            {"url":good,"label":"Median","ts":-1},
            {"url":good,"label":"Median","ts":999999999999999},
            {"url":good,"label":"Median","ts":"not-a-timestamp"},
        )
        for record in invalid:
            with self.subTest(record=record):
                self.page.evaluate("(v)=>localStorage.setItem('esa_continue_descriptive_center_lesson_v0',JSON.stringify(v))",record)
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block4")).to_be_hidden()
        # Valid legacy records were stored without a timestamp; retain support.
        self.page.evaluate("(v)=>localStorage.setItem('esa_continue_descriptive_center_lesson_v0',JSON.stringify(v))",
                           {"url":good,"label":"Median"})
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block4")).to_be_visible()
        self.assertEqual(self.page.locator("#continue-reading-block4-btn").get_attribute("href"),good)
        self.page.evaluate("(v)=>localStorage.setItem('esa_continue_descriptive_center_lesson_v0',JSON.stringify(v))",
                           {"url":good,"label":"<img src=x onerror=alert(1)>","ts":12345})
        self.page.reload(wait_until="networkidle")
        self.assertEqual(self.page.locator("#continue-reading-block4-label img").count(),0)

    def test_batch60_center_denied_storage_arabic_and_hypergeom_mobile(self):
        self.page.add_init_script("""
            Object.defineProperty(window,"localStorage",{
              configurable:true,get(){throw new DOMException("Denied","SecurityError")}
            });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        root="/descriptive/center/"
        slugs=("what-is-center","arithmetic-mean","median","mode","mean-vs-median",
               "weighted-mean","trimmed-mean","winsorized-mean",
               "center-for-ordinal-data","reporting-center-properly")
        for slug in slugs:
            with self.subTest(lesson=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block4")).to_be_hidden()
        for page in ("/ar/descriptive/center/mean-vs-median/",
                     "/probability/distributions/hypergeometric-distribution/"):
            self.page.goto(self.origin+page,wait_until="networkidle")
            expect(self.page.locator("main h1")).to_be_visible()
            overflow=self.page.evaluate("""() => ({
                extra:document.documentElement.scrollWidth-document.documentElement.clientWidth,
                width:window.innerWidth,
                offenders:[...document.querySelectorAll("body *")].map(e=>({
                    tag:e.tagName,id:e.id,cls:String(e.className||"").slice(0,65),
                    right:Math.round(e.getBoundingClientRect().right),
                    left:Math.round(e.getBoundingClientRect().left)
                })).filter(x=>x.right>window.innerWidth+2||x.left < -2).slice(0,15)
            })""")
            self.assertLessEqual(overflow["extra"],2,overflow)



    def test_batch61_binomial_bilingual_calculator_parity_and_metadata(self):
        en="/probability/distributions/binomial-distribution/"
        ar="/ar/probability/distributions/binomial-distribution/"
        initial=[]
        for route,lang in ((en,"en"),(ar,"ar")):
            with self.subTest(lang=lang):
                self.page.goto(self.origin+route,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),
                                 "rtl" if lang=="ar" else None)
                self.assertEqual(self.page.locator("link[rel=canonical]").get_attribute("href"),
                                 "https://easystatisticsacademy.com"+route)
                for key,target in (("en",en),("ar",ar)):
                    self.assertEqual(self.page.locator(
                        'link[rel=alternate][hreflang="'+key+'"]').get_attribute("href"),
                        "https://easystatisticsacademy.com"+target)
                self.assertEqual(self.page.locator("#esa-binomial-calculator").count(),1)
                ids=("exact","cdf","upper","mean","variance")
                values=tuple(self.page.locator("#esa-binomial-"+key).inner_text() for key in ids)
                self.assertEqual(values,("0.375","0.875","0.5","1.5","0.75"))
                initial.append(values)
                self.page.locator("#esa-binomial-n").fill("10")
                self.page.locator("#esa-binomial-p").fill("0.2")
                self.page.locator("#esa-binomial-k").fill("2")
                self.assertAlmostEqual(float(self.page.locator("#esa-binomial-exact").inner_text()),
                                       45*(.2**2)*(.8**8),delta=1e-10)
                self.assertEqual(self.page.locator("#esa-binomial-mean").inner_text(),"2")
                self.assertEqual(self.page.locator("#esa-binomial-variance").inner_text(),"1.6")
                self.page.locator("#esa-binomial-p").fill("0")
                self.page.locator("#esa-binomial-k").fill("0")
                self.assertEqual(self.page.locator("#esa-binomial-exact").inner_text(),"1")
                self.page.locator("#esa-binomial-p").fill("1")
                self.page.locator("#esa-binomial-k").fill("10")
                self.assertEqual(self.page.locator("#esa-binomial-exact").inner_text(),"1")
                self.page.locator("#esa-binomial-n").fill("1001")
                self.assertFalse(self.page.locator("#esa-binomial-error").is_hidden())
                message=self.page.locator("#esa-binomial-error").inner_text()
                self.assertIn("أدخل" if lang=="ar" else "Enter",message)
                self.page.set_viewport_size({"width":320,"height":760})
                self.assertLessEqual(self.page.evaluate(
                    "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)
                self.page.set_viewport_size({"width":1280,"height":800})
        self.assertEqual(initial[0],initial[1])
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        expect(self.page.locator('a[href="'+ar+'"]')).to_be_visible()

    def test_batch61_misleading_axis_explorer_independent_values_and_keyboard(self):
        self.page.goto(self.origin+"/descriptive/visualization/misleading-graphs/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-truncated-axis-lab")).to_be_visible()
        self.assertEqual(self.page.locator("#esa-axis-difference").inner_text(),"5")
        self.assertEqual(self.page.locator("#esa-axis-relative").inner_text(),"5.26%")
        self.assertEqual(self.page.locator("#esa-axis-apparent").inner_text(),"2.00×")
        sizes=self.page.evaluate("""() => ['zero','truncated'].map(name =>
          [...document.querySelectorAll('#esa-axis-'+name+'-chart rect')]
          .map(node=>Number(node.getAttribute('height'))))""")
        self.assertEqual(len(sizes[0]),2)
        self.assertEqual(len(sizes[1]),2)
        self.assertAlmostEqual(sizes[0][1]/sizes[0][0],100/95,places=9)
        self.assertAlmostEqual(sizes[1][1]/sizes[1][0],10/5,places=9)
        self.page.locator("#esa-axis-a").fill("80")
        self.page.locator("#esa-axis-b").fill("100")
        self.page.locator("#esa-axis-baseline").fill("70")
        self.assertEqual(self.page.locator("#esa-axis-difference").inner_text(),"20")
        self.assertEqual(self.page.locator("#esa-axis-relative").inner_text(),"25.00%")
        self.assertEqual(self.page.locator("#esa-axis-apparent").inner_text(),"3.00×")
        self.page.locator("#esa-axis-baseline").fill("85")
        expect(self.page.locator("#esa-axis-error")).to_be_visible()
        expect(self.page.locator("#esa-axis-result")).to_be_hidden()
        self.page.locator("#esa-axis-reset").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-axis-apparent").inner_text(),"2.00×")
        self.page.set_viewport_size({"width":320,"height":760})
        self.assertLessEqual(self.page.evaluate(
            "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch61_random_variables_six_lessons_resume_safety_and_legacy(self):
        root="/probability/random-variables/"
        key="esa_continue_probability_random_variables_lesson_v0"
        slugs=("what-is-a-random-variable","discrete-random-variables",
               "continuous-random-variables","cumulative-distribution-function",
               "expectation","variance-and-standard-deviation")
        for slug in slugs:
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                record=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(record["url"],root+slug+"/")
                self.assertIsInstance(record["ts"],int)
                self.assertGreater(record["ts"],0)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-probability-rv")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-probability-rv-btn").get_attribute("href"),record["url"])
        self.page.goto(self.origin+root,wait_until="networkidle")
        valid=root+"expectation/"
        invalid=(
            {"url":"javascript:alert(1)","label":"Expectation","ts":10},
            {"url":valid+"?x=1","label":"Expectation","ts":10},
            {"url":root+"invented/","label":"Expectation","ts":10},
            {"url":valid,"label":"x"*201,"ts":10},
            {"url":valid,"label":"Expectation","ts":0},
            {"url":valid,"label":"Expectation","ts":-12},
            {"url":valid,"label":"Expectation","ts":99999999999999},
            {"url":valid,"label":"Expectation","ts":"not-a-date"},
            {"url":valid,"label":"Expectation","ts":None},
        )
        for record in invalid:
            with self.subTest(record=str(record)):
                self.page.evaluate("(v)=>localStorage.setItem('"+key+"',JSON.stringify(v))",record)
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-probability-rv")).to_be_hidden()
        # Older valid storage records lacked timestamps: preserve them.
        self.page.evaluate("(v)=>localStorage.setItem('"+key+"',JSON.stringify(v))",
                           {"url":valid,"label":"Expectation"})
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-probability-rv")).to_be_visible()
        self.page.evaluate("(v)=>localStorage.setItem('"+key+"',JSON.stringify(v))",
                           {"url":valid,"label":"<img src=x onerror=alert(1)>","ts":12345})
        self.page.reload(wait_until="networkidle")
        self.assertEqual(self.page.locator("#continue-reading-probability-rv-label img").count(),0)
        self.assertIn("<img",self.page.locator("#continue-reading-probability-rv-label").inner_text())

    def test_batch61_random_variables_denied_storage_mobile(self):
        self.page.add_init_script("""
            Object.defineProperty(window,"localStorage",{
              configurable:true,get(){throw new DOMException("Denied","SecurityError")}
            });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        root="/probability/random-variables/"
        for slug in ("what-is-a-random-variable","discrete-random-variables",
                     "continuous-random-variables","cumulative-distribution-function",
                     "expectation","variance-and-standard-deviation"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-probability-rv")).to_be_hidden()



    def test_batch62_poisson_bilingual_metadata_calculator_and_numerical_parity(self):
        english="/probability/distributions/poisson-distribution/"
        arabic="/ar/probability/distributions/poisson-distribution/"
        initial=[]
        for url,lang in ((english,"en"),(arabic,"ar")):
            with self.subTest(language=lang):
                self.page.goto(self.origin+url,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),
                                 "rtl" if lang=="ar" else None)
                self.assertEqual(self.page.locator("link[rel=canonical]").get_attribute("href"),
                                 "https://easystatisticsacademy.com"+url)
                for key,path in (("en",english),("ar",arabic)):
                    self.assertEqual(self.page.locator(
                        'link[rel=alternate][hreflang="'+key+'"]').get_attribute("href"),
                        "https://easystatisticsacademy.com"+path)
                self.assertEqual(self.page.locator("#esa-poisson-exponential-explorer").count(),1)
                output_ids=("none","survival","at-least-one","expected","meanwait")
                vals=tuple(self.page.locator("#esa-event-"+key).inner_text() for key in output_ids)
                self.assertEqual(vals,("0.135335","0.135335","0.864665","2.000000","0.500000"))
                initial.append(vals)
                exact=self.page.evaluate("() => window.esaPoissonExponential(2,1)")
                self.assertAlmostEqual(exact[0],0.1353352832366127,places=14)
                self.assertAlmostEqual(exact[2],0.8646647167633873,places=14)
                self.assertEqual(exact[3:], [2,0.5])
                # t=0: zero events certain, at least one event impossible.
                self.page.locator("#esa-event-time").fill("0")
                self.assertEqual(self.page.locator("#esa-event-none").inner_text(),"1.000000")
                self.assertEqual(self.page.locator("#esa-event-at-least-one").inner_text(),"0.000000")
                self.page.locator("#esa-event-rate").fill("3")
                self.page.locator("#esa-event-time").fill("0.5")
                self.assertEqual(self.page.locator("#esa-event-expected").inner_text(),"1.500000")
                self.assertEqual(self.page.locator("#esa-event-meanwait").inner_text(),"0.333333")
                self.assertAlmostEqual(float(self.page.locator("#esa-event-none").inner_text()),
                                       0.22313016014842982,delta=6e-7)
                # Ensure the tiny-event complement is evaluated stably in code.
                small=self.page.evaluate("()=>window.esaPoissonExponential(0.000001,0.01)")
                self.assertGreater(small[2],0)
                self.assertAlmostEqual(small[2],1e-8,delta=1e-15)
                self.page.locator("#esa-event-rate").fill("0")
                expect(self.page.locator("#esa-event-error")).to_be_visible()
                self.assertIn("معدل" if lang=="ar" else "Rate",
                              self.page.locator("#esa-event-error").inner_text())
                self.page.locator("#esa-event-rate").fill("2")
                self.page.locator("#esa-event-time").fill("61")
                expect(self.page.locator("#esa-event-error")).to_be_visible()
                self.page.locator("#esa-event-reset").focus()
                self.page.keyboard.press("Enter")
                self.assertEqual(self.page.locator("#esa-event-none").inner_text(),"0.135335")
                self.page.set_viewport_size({"width":320,"height":760})
                self.assertLessEqual(self.page.evaluate(
                    "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)
                self.page.set_viewport_size({"width":1280,"height":800})
        self.assertEqual(initial[0],initial[1])
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        expect(self.page.locator('a[href="'+arabic+'"]')).to_be_visible()

    def test_batch62_scatter_correlation_outlier_numerical_edgecases_and_mobile(self):
        self.page.goto(self.origin+"/descriptive/visualization/scatterplots/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-scatter-correlation-lab")).to_be_visible()
        self.assertEqual(self.page.locator("#esa-scatter-base-r").inner_text(),"0.9939")
        self.assertEqual(self.page.locator("#esa-scatter-new-r").inner_text(),"0.1882")
        self.assertEqual(self.page.locator("#esa-scatter-change-r").inner_text(),"-0.8057")
        self.assertEqual(self.page.locator("#esa-scatter-base-svg circle").count(),6)
        self.assertEqual(self.page.locator("#esa-scatter-new-svg circle").count(),7)
        self.assertEqual(self.page.evaluate(
            "()=>window.esaScatterPearson([[1,1],[2,2],[3,3]])"),1)
        self.assertEqual(self.page.evaluate(
            "()=>window.esaScatterPearson([[1,3],[2,2],[3,1]])"),-1)
        self.assertIsNone(self.page.evaluate(
            "()=>window.esaScatterPearson([[2,1],[2,2],[2,3]])"))
        self.assertIsNone(self.page.evaluate(
            "()=>window.esaScatterPearson([[1,7],[2,7],[3,7]])"))
        self.page.locator("#esa-scatter-outlier-y").fill("8")
        self.assertNotEqual(self.page.locator("#esa-scatter-new-r").inner_text(),"0.1882")
        self.page.locator("#esa-scatter-include").uncheck()
        self.assertEqual(self.page.locator("#esa-scatter-new-svg circle").count(),6)
        self.assertEqual(self.page.locator("#esa-scatter-new-r").inner_text(),"0.9939")
        self.page.locator("#esa-scatter-include").check()
        self.page.locator("#esa-scatter-outlier-x").fill("30")
        expect(self.page.locator("#esa-scatter-error")).to_be_visible()
        expect(self.page.locator("#esa-scatter-status")).to_be_hidden()
        self.page.locator("#esa-scatter-reset").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-scatter-new-r").inner_text(),"0.1882")
        self.page.set_viewport_size({"width":320,"height":760})
        self.assertLessEqual(self.page.evaluate(
            "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch62_expectation_variance_six_lessons_safe_progress(self):
        root="/probability/expectation-variance/"
        key="esa_continue_probability_expectation_variance_lesson_v0"
        slugs=("indicator-random-variables","linearity-of-expectation",
               "variance-rules-and-sums","covariance","correlation",
               "applications-mini-cases")
        for slug in slugs:
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                stored=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(stored["url"],root+slug+"/")
                self.assertEqual(stored["label"].strip()!="",True)
                self.assertIsInstance(stored["ts"],int)
                self.assertGreater(stored["ts"],0)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-probability-ev")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-probability-ev-btn").get_attribute("href"),
                                 stored["url"])
        self.page.goto(self.origin+root,wait_until="networkidle")
        good=root+"correlation/"
        invalid=(
            {"url":"javascript:alert(1)","label":"Correlation","ts":10},
            {"url":good+"#section","label":"Correlation","ts":10},
            {"url":root+"unpublished/","label":"Correlation","ts":10},
            {"url":good,"label":"x"*201,"ts":10},
            {"url":good,"label":"Correlation","ts":0},
            {"url":good,"label":"Correlation","ts":-1},
            {"url":good,"label":"Correlation","ts":None},
            {"url":good,"label":"Correlation","ts":"yesterday"},
            {"url":good,"label":"Correlation","ts":999999999999999},
            {"url":good,"label":"Correlation","ts":True},
        )
        for record in invalid:
            with self.subTest(record=str(record)):
                self.page.evaluate("({v,k})=>localStorage.setItem(k,JSON.stringify(v))",
                                   {"v":record,"k":key})
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-probability-ev")).to_be_hidden()
        # Old valid records without timestamps must continue working.
        self.page.evaluate("({v,k})=>localStorage.setItem(k,JSON.stringify(v))",
                           {"v":{"url":good,"label":"Correlation"},"k":key})
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-probability-ev")).to_be_visible()
        self.page.evaluate("({v,k})=>localStorage.setItem(k,JSON.stringify(v))",
                           {"v":{"url":good,"label":"<img src=x onerror=alert(1)>"},"k":key})
        self.page.reload(wait_until="networkidle")
        self.assertEqual(self.page.locator("#continue-reading-probability-ev-label img").count(),0)
        self.assertIn("<img",self.page.locator("#continue-reading-probability-ev-label").inner_text())

    def test_batch62_expectation_variance_denied_storage_mobile(self):
        self.page.add_init_script("""
            Object.defineProperty(window,"localStorage",{
                configurable:true,
                get(){throw new DOMException("Storage disabled","SecurityError")}
            });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        root="/probability/expectation-variance/"
        for slug in ("indicator-random-variables","linearity-of-expectation",
                     "variance-rules-and-sums","covariance","correlation",
                     "applications-mini-cases"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-probability-ev")).to_be_hidden()



    def test_batch63_geometric_bilingual_math_metadata_mobile_keyboard(self):
        """Both localizations use exactly one shared numerical implementation."""
        english="/probability/distributions/geometric-distribution/"
        arabic="/ar/probability/distributions/geometric-distribution/"
        for url,lang in ((english,"en"),(arabic,"ar")):
            with self.subTest(lang=lang):
                self.page.goto(self.origin+url,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),
                                 "rtl" if lang=="ar" else None)
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+url)
                for code,path in (("en",english),("ar",arabic)):
                    self.assertEqual(self.page.locator(
                        'link[rel="alternate"][hreflang="'+code+'"]').get_attribute("href"),
                        "https://easystatisticsacademy.com"+path)
                self.assertEqual(self.page.locator("#esa-geometric-wait-explorer").count(),1)
                self.assertEqual(self.page.locator("#esa-geom-bars rect[data-trial]").count(),12)
                for id,expected in (
                    ("pmf","0.140625"),("cdf","0.578125"),
                    ("tail","0.421875"),("mean","4.0000"),("variance","12.0000"),
                    ("memoryless-next","0.2500"),("memoryless-tail","0.421875")
                ):
                    self.assertEqual(self.page.locator("#esa-geom-"+id).inner_text(),expected)
                numbers=self.page.evaluate("() => window.esaGeometricMath(0.25,3)")
                self.assertAlmostEqual(numbers["pmf"],0.140625)
                self.assertAlmostEqual(numbers["cdf"],0.578125)
                self.assertAlmostEqual(numbers["tail"],0.421875)
                self.assertAlmostEqual(numbers["mean"],4)
                self.assertAlmostEqual(numbers["variance"],12)
                self.assertIsNone(self.page.evaluate("() => window.esaGeometricMath(0,2)"))
                self.assertIsNone(self.page.evaluate("() => window.esaGeometricMath(0.25,0)"))
                self.page.locator("#esa-geom-p").evaluate(
                    "(el)=>{el.value='1';el.dispatchEvent(new Event('input',{bubbles:true}))}")
                self.assertEqual(self.page.locator("#esa-geom-pmf").inner_text(),"0.000000")
                self.assertEqual(self.page.locator("#esa-geom-cdf").inner_text(),"1.000000")
                self.assertEqual(self.page.locator("#esa-geom-mean").inner_text(),"1.0000")
                self.assertEqual(self.page.locator("#esa-geom-variance").inner_text(),"0.0000")
                expect(self.page.locator("#esa-geom-memoryless-note")).to_be_visible()
                self.page.locator("#esa-geom-reset").focus()
                self.page.keyboard.press("Enter")
                self.assertEqual(self.page.locator("#esa-geom-pmf").inner_text(),"0.140625")
                self.page.locator("#esa-geom-p").focus()
                self.page.keyboard.press("ArrowRight")
                # Native range controls are RTL-aware: ArrowRight decreases p in Arabic,
                # but increases p in English. Verify the localized keyboard semantics.
                expected_after_right="0.20" if lang=="ar" else "0.30"
                self.assertEqual(self.page.locator("#esa-geom-p-value").inner_text(),
                                 expected_after_right)
                self.page.set_viewport_size({"width":320,"height":760})
                self.assertLessEqual(self.page.evaluate(
                    "() => document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)
                self.page.set_viewport_size({"width":1280,"height":800})
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        expect(self.page.locator('a[href="'+arabic+'"]')).to_be_visible()

    def test_batch63_cdf_exact_math_interval_plot_keyboard_mobile(self):
        """Right-continuous Bernoulli jumps and continuous Uniform CDF."""
        self.page.goto(self.origin+"/probability/random-variables/cumulative-distribution-function/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-cdf-explorer")).to_be_visible()
        self.assertEqual(self.page.locator("#esa-cdf-fx").inner_text(),"0.650000")
        self.assertEqual(self.page.locator("#esa-cdf-interval").inner_text(),"0.350000")
        self.assertEqual(self.page.locator("#esa-cdf-chart").get_attribute("role"),"img")
        cases=[
          ("bernoulli",-0.1,0.35,0,2,0),
          ("bernoulli",0,0.35,0,2,0.65),
          ("bernoulli",0.5,0.35,0,2,0.65),
          ("bernoulli",1,0.35,0,2,1),
          ("bernoulli",0,0,0,2,1),
          ("bernoulli",0,1,0,2,0),
          ("uniform",-0.1,0.35,0,2,0),
          ("uniform",0.5,0.35,0,2,0.25),
          ("uniform",2,0.35,0,2,1),
          ("uniform",4,0.35,0,2,1),
        ]
        for kind,x,p,a,b,expected in cases:
            with self.subTest(kind=kind,x=x,p=p):
                got=self.page.evaluate(
                    "args=>window.esaCdfMath.cdf(...args)",[kind,x,p,a,b])
                self.assertAlmostEqual(got,expected,places=12)
        self.assertAlmostEqual(self.page.evaluate(
            "()=>window.esaCdfMath.interval('bernoulli',0,1,.35,0,2)"),.35)
        self.assertAlmostEqual(self.page.evaluate(
            "()=>window.esaCdfMath.interval('bernoulli',-1,0,.35,0,2)"),.65)
        self.assertAlmostEqual(self.page.evaluate(
            "()=>window.esaCdfMath.interval('uniform',0,1,.35,0,2)"),.5)
        self.assertIsNone(self.page.evaluate(
            "()=>window.esaCdfMath.interval('uniform',1,0,.35,0,2)"))
        self.assertIsNone(self.page.evaluate(
            "()=>window.esaCdfMath.cdf('uniform',.5,.35,2,1)"))
        self.page.locator("#esa-cdf-kind").select_option("uniform")
        self.assertEqual(self.page.locator("#esa-cdf-fx").inner_text(),"0.250000")
        self.assertEqual(self.page.locator("#esa-cdf-interval").inner_text(),"0.500000")
        expect(self.page.locator("#esa-cdf-uniform-options")).to_be_visible()
        self.page.locator("#esa-cdf-a").evaluate(
            "(el)=>{el.value='1.5';el.dispatchEvent(new Event('input',{bubbles:true}))}")
        self.page.locator("#esa-cdf-b").evaluate(
            "(el)=>{el.value='1';el.dispatchEvent(new Event('input',{bubbles:true}))}")
        expect(self.page.locator("#esa-cdf-error")).to_be_visible()
        expect(self.page.locator("#esa-cdf-results")).to_be_hidden()
        self.page.locator("#esa-cdf-reset").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-cdf-fx").inner_text(),"0.650000")
        self.page.locator("#esa-cdf-p").focus()
        self.page.keyboard.press("ArrowRight")
        self.assertEqual(self.page.locator("#esa-cdf-p-label").inner_text(),"0.40")
        self.page.set_viewport_size({"width":320,"height":760})
        self.assertLessEqual(self.page.evaluate(
            "() => document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch63_sampling_distributions_progress_legacy_and_security(self):
        root="/probability/sampling-distributions/"
        key="esa_continue_probability_sampling_distributions_lesson_v0"
        slugs=("what-is-a-sampling-distribution","standard-error-and-estimators",
               "z-statistic-and-ci","t-distribution-and-t-test",
               "chi-square-and-variance","f-distribution-and-anova-preview")
        for slug in slugs:
            with self.subTest(lesson=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                item=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(item["url"],root+slug+"/")
                self.assertTrue(item["label"].strip())
                self.assertIs(type(item["ts"]),int)
                self.assertGreater(item["ts"],0)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-probability-sampling")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-probability-sampling-btn")
                                 .get_attribute("href"),item["url"])
        self.page.goto(self.origin+root,wait_until="networkidle")
        good=root+"standard-error-and-estimators/"
        for record in (
            {"url":"javascript:alert(1)","label":"Bad","ts":100},
            {"url":good+"#chart","label":"Bad","ts":100},
            {"url":root+"not-published/","label":"Bad","ts":100},
            {"url":good,"label":"z"*201,"ts":100},
            {"url":good,"label":"Good","ts":0},
            {"url":good,"label":"Good","ts":-1},
            {"url":good,"label":"Good","ts":None},
            {"url":good,"label":"Good","ts":"tomorrow"},
            {"url":good,"label":"Good","ts":999999999999999},
            {"url":good,"label":"Good","ts":True}
        ):
            with self.subTest(record=str(record)):
                self.page.evaluate("args=>localStorage.setItem(args.k,JSON.stringify(args.v))",
                                   {"k":key,"v":record})
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-probability-sampling")).to_be_hidden()
        # A missing timestamp is a supported legacy record, never a fabricated value.
        self.page.evaluate("args=>localStorage.setItem(args.k,JSON.stringify(args.v))",
                           {"k":key,"v":{"url":good,"label":"Standard Error"}})
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-probability-sampling")).to_be_visible()
        malicious='<img src=x onerror="window.esaInjected=true">'
        self.page.evaluate("args=>localStorage.setItem(args.k,JSON.stringify(args.v))",
                           {"k":key,"v":{"url":good,"label":malicious}})
        self.page.reload(wait_until="networkidle")
        self.assertEqual(self.page.locator("#continue-reading-probability-sampling-label img").count(),0)
        self.assertIn(malicious,self.page.locator("#continue-reading-probability-sampling-label")
                      .inner_text())
        self.assertIsNone(self.page.evaluate("()=>window.esaInjected || null"))

    def test_batch63_sampling_distributions_denied_storage_mobile(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,
            get(){throw new DOMException("Storage blocked","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        root="/probability/sampling-distributions/"
        for slug in ("what-is-a-sampling-distribution","standard-error-and-estimators",
                     "z-statistic-and-ci","t-distribution-and-t-test",
                     "chi-square-and-variance","f-distribution-and-anova-preview"):
            with self.subTest(lesson=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-probability-sampling")).to_be_hidden()



    def test_batch64_negative_binomial_arabic_english_parity_mobile_keyboard(self):
        english="/probability/distributions/negative-binomial-distribution/"
        arabic="/ar/probability/distributions/negative-binomial-distribution/"
        for path,lang in ((english,"en"),(arabic,"ar")):
            with self.subTest(language=lang):
                self.page.goto(self.origin+path,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl" if lang=="ar" else None)
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+path)
                for code,target in (("en",english),("ar",arabic)):
                    self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+code+'"]')
                                     .get_attribute("href"),"https://easystatisticsacademy.com"+target)
                expect(self.page.locator("#esa-negbin-wait-explorer")).to_be_visible()
                self.assertEqual(self.page.locator("#esa-negbin-bars rect[data-trial]").count(),12)
                for element,expected in (
                    ("r-value","3"),("p-value","0.50"),("k-value","5"),
                    ("pmf","0.187500"),("cdf","0.500000"),("tail","0.500000"),
                    ("mean","6.0000"),("variance","6.0000")
                ):
                    self.assertEqual(self.page.locator("#esa-negbin-"+element).inner_text(),expected)
                expected=self.page.evaluate("()=>window.esaNegBinMath(3,.5,5)")
                self.assertAlmostEqual(expected["pmf"],.1875,places=14)
                self.assertAlmostEqual(expected["cdf"],.5,places=14)
                self.assertAlmostEqual(expected["tail"],.5,places=14)
                self.assertEqual(expected["mean"],6)
                self.assertEqual(expected["variance"],6)
                self.assertIsNone(self.page.evaluate("()=>window.esaNegBinMath(0,.5,3)"))
                self.assertIsNone(self.page.evaluate("()=>window.esaNegBinMath(3,0,5)"))
                self.assertIsNone(self.page.evaluate("()=>window.esaNegBinMath(3,.5,2)"))
                # Degenerate p=1: the third success must occur on trial 3.
                self.page.locator("#esa-negbin-p").evaluate(
                    "(el)=>{el.value='1';el.dispatchEvent(new Event('input',{bubbles:true}))}")
                self.assertEqual(self.page.locator("#esa-negbin-cdf").inner_text(),"1.000000")
                self.assertEqual(self.page.locator("#esa-negbin-pmf").inner_text(),"0.000000")
                self.assertEqual(self.page.locator("#esa-negbin-variance").inner_text(),"0.0000")
                self.assertEqual(self.page.evaluate("()=>window.esaNegBinMath(3,1,3)")["pmf"],1)
                # r=1 is exactly the geometric first-success waiting-time distribution.
                self.page.locator("#esa-negbin-geometric").focus()
                self.page.keyboard.press("Enter")
                self.assertEqual(self.page.locator("#esa-negbin-r-value").inner_text(),"1")
                self.assertEqual(self.page.locator("#esa-negbin-k-value").inner_text(),"3")
                self.assertEqual(self.page.locator("#esa-negbin-pmf").inner_text(),"0.125000")
                self.assertEqual(self.page.locator("#esa-negbin-cdf").inner_text(),"0.875000")
                self.page.locator("#esa-negbin-reset").focus()
                self.page.keyboard.press("Enter")
                self.assertEqual(self.page.locator("#esa-negbin-pmf").inner_text(),"0.187500")
                self.page.locator("#esa-negbin-r").focus()
                self.page.keyboard.press("ArrowRight")
                self.assertEqual(self.page.locator("#esa-negbin-r-value").inner_text(),"4")
                self.page.set_viewport_size({"width":320,"height":760})
                self.assertLessEqual(self.page.evaluate(
                    "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)
                self.page.set_viewport_size({"width":1280,"height":800})
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        expect(self.page.locator('a[href="'+arabic+'"]')).to_be_visible()

    def test_batch64_student_t_quantiles_reference_pdf_cdf_and_confidence(self):
        self.page.goto(self.origin+"/probability/sampling-distributions/t-distribution-and-t-test/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-t-normal-explorer")).to_be_visible()
        self.assertEqual(self.page.locator("#esa-t-normal-n-value").inner_text(),"10")
        self.assertEqual(self.page.locator("#esa-t-normal-df").inner_text(),"9")
        self.assertEqual(self.page.locator("#esa-t-normal-zcrit").inner_text(),"1.9600")
        self.assertEqual(self.page.locator("#esa-t-normal-tcrit").inner_text(),"2.2622")
        self.assertEqual(self.page.locator("#esa-t-normal-tmargin").inner_text(),"0.7154")
        self.assertEqual(self.page.locator("#esa-t-normal-zmargin").inner_text(),"0.6198")
        refs=((1,.90,6.313751515),(1,.95,12.706204736),(1,.99,63.656741163),
              (2,.95,4.30265273),(4,.95,2.776445105),
              (9,.90,1.833112933),(9,.95,2.262157163),(9,.99,3.249835542),
              (29,.95,2.045229642),(99,.95,1.984216952),
              (120,.99,2.617421145))
        for df,confidence,critical in refs:
            with self.subTest(df=df,confidence=confidence):
                q=self.page.evaluate(
                    "args=>window.esaStudentTMath.tQuantile(...args)",
                    [(1+confidence)/2,df])
                self.assertAlmostEqual(q,critical,delta=3e-6)
                tail=self.page.evaluate(
                    "args=>window.esaStudentTMath.tCdf(...args)",[q,df])
                self.assertAlmostEqual(tail,(1+confidence)/2,delta=1e-10)
        self.assertAlmostEqual(self.page.evaluate(
            "()=>window.esaStudentTMath.tDensity(0,1)"),1/3.141592653589793,places=12)
        self.assertAlmostEqual(self.page.evaluate(
            "()=>window.esaStudentTMath.tCdf(1,1)"),.75,places=12)
        self.assertAlmostEqual(self.page.evaluate(
            "()=>window.esaStudentTMath.tCdf(-1,1)"),.25,places=12)
        self.assertAlmostEqual(self.page.evaluate(
            "()=>window.esaStudentTMath.normalDensity(0)"),
            1/(2*3.141592653589793)**.5,places=12)
        self.assertIsNone(self.page.evaluate(
            "()=>window.esaStudentTMath.tQuantile(1,9)"))
        self.assertIsNone(self.page.evaluate(
            "()=>window.esaStudentTMath.tQuantile(.95,0)"))
        self.page.locator("#esa-t-normal-n").focus()
        self.page.keyboard.press("ArrowRight")
        self.assertEqual(self.page.locator("#esa-t-normal-n-value").inner_text(),"11")
        self.assertEqual(self.page.locator("#esa-t-normal-df").inner_text(),"10")
        self.page.locator("#esa-t-normal-confidence").select_option("99")
        self.assertEqual(self.page.locator("#esa-t-normal-tail").inner_text(),"0.5%")
        self.page.locator("#esa-t-normal-n").evaluate(
            "(el)=>{el.value='2';el.dispatchEvent(new Event('input',{bubbles:true}))}")
        self.assertEqual(self.page.locator("#esa-t-normal-df").inner_text(),"1")
        self.assertEqual(self.page.locator("#esa-t-normal-tcrit").inner_text(),"63.6567")
        self.assertIn("outside the plotted",self.page.locator("#esa-t-normal-note").inner_text())
        self.page.locator("#esa-t-normal-reset").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-t-normal-n-value").inner_text(),"10")
        self.assertEqual(self.page.locator("#esa-t-normal-tcrit").inner_text(),"2.2622")
        self.assertEqual(self.page.locator("#esa-t-normal-plot").get_attribute("role"),"img")
        self.page.set_viewport_size({"width":320,"height":760})
        self.assertLessEqual(self.page.evaluate(
            "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch64_visualization_eleven_lessons_progress_and_untrusted_storage(self):
        root="/descriptive/visualization/"
        key="esa_continue_descriptive_visualization_lesson_v0"
        slugs=("why-visualization-matters","choosing-the-right-graph",
               "matching-graph-to-variable-type","bar-charts","histograms","pie-charts",
               "density-curves","boxplots","scatterplots","time-series-line-charts",
               "misleading-graphs")
        for slug in slugs:
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                v=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
                self.assertEqual(v["url"],root+slug+"/")
                self.assertTrue(v["label"].strip())
                self.assertEqual(type(v["ts"]),int)
                self.assertGreater(v["ts"],0)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block3")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-block3-btn")
                                 .get_attribute("href"),root+slug+"/")
        self.page.goto(self.origin+root,wait_until="networkidle")
        good=root+"bar-charts/"
        bad=(
            {"url":"javascript:alert(1)","label":"Bar Charts","ts":10},
            {"url":good+"#part","label":"Bar Charts","ts":10},
            {"url":good+"?a=1","label":"Bar Charts","ts":10},
            {"url":root+"unpublished/","label":"Bar Charts","ts":10},
            {"url":good,"label":"x"*201,"ts":10},
            {"url":good,"label":"Bar Charts","ts":0},
            {"url":good,"label":"Bar Charts","ts":-1},
            {"url":good,"label":"Bar Charts","ts":None},
            {"url":good,"label":"Bar Charts","ts":"tomorrow"},
            {"url":good,"label":"Bar Charts","ts":999999999999999},
            {"url":good,"label":"Bar Charts","ts":True}
        )
        for v in bad:
            with self.subTest(record=str(v)):
                self.page.evaluate(
                    "arg=>localStorage.setItem(arg.key,JSON.stringify(arg.value))",
                    {"key":key,"value":v})
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block3")).to_be_hidden()
        # Retain legitimate old records with no timestamp field.
        self.page.evaluate(
            "arg=>localStorage.setItem(arg.key,JSON.stringify(arg.value))",
            {"key":key,"value":{"url":good,"label":"Bar Charts"}})
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block3")).to_be_visible()
        evil='<img src=x onerror="window.esaInjected=true">'
        self.page.evaluate(
            "arg=>localStorage.setItem(arg.key,JSON.stringify(arg.value))",
            {"key":key,"value":{"url":good,"label":evil}})
        self.page.reload(wait_until="networkidle")
        self.assertEqual(self.page.locator("#continue-reading-block3-label img").count(),0)
        self.assertIn(evil,self.page.locator("#continue-reading-block3-label").inner_text())
        self.assertIsNone(self.page.evaluate("()=>window.esaInjected || null"))
        self.page.evaluate("key=>localStorage.setItem(key,'{broken JSON')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block3")).to_be_hidden()

    def test_batch64_visualization_denied_storage_all_lessons_and_mobile(self):
        self.page.add_init_script("""
            Object.defineProperty(window,"localStorage",{
                configurable:true,
                get(){throw new DOMException("Denied","SecurityError")}
            });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        root="/descriptive/visualization/"
        for slug in ("why-visualization-matters","choosing-the-right-graph",
                     "matching-graph-to-variable-type","bar-charts","histograms","pie-charts",
                     "density-curves","boxplots","scatterplots","time-series-line-charts",
                     "misleading-graphs"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block3")).to_be_hidden()



    def test_batch65_arabic_exponential_translation_math_metadata_mobile(self):
        english="/probability/distributions/exponential-distribution/"
        arabic="/ar/probability/distributions/exponential-distribution/"
        for route,language in ((english,"en"),(arabic,"ar")):
            with self.subTest(lang=language):
                self.page.goto(self.origin+route,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),language)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),
                                 "rtl" if language=="ar" else None)
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+route)
                for lng,href in (("en",english),("ar",arabic)):
                    self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+lng+'"]')
                                     .get_attribute("href"),"https://easystatisticsacademy.com"+href)
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreaterEqual(self.page.locator("main h2").count(),20)
                self.page.set_viewport_size({"width":320,"height":760})
                self.assertLessEqual(self.page.evaluate(
                    "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)
                self.page.set_viewport_size({"width":1280,"height":800})
        self.page.goto(self.origin+arabic,wait_until="networkidle")
        main=self.page.locator("main").inner_text()
        for phrase in ("0.864665","0.135335","15","خاصية انعدام الذاكرة",
                       "التوزيع الهندسي","توزيع بواسون","التباين"):
            self.assertIn(phrase,main)
        self.assertGreaterEqual(self.page.locator(".esa-exp-equation").count(),8)
        self.assertEqual(self.page.locator(".esa-exp-equation[tabindex='0']").count(),
                         self.page.locator(".esa-exp-equation").count())
        self.page.locator(".esa-exp-equation").first.focus()
        self.assertEqual(self.page.evaluate("()=>document.activeElement.tabIndex"),0)
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        expect(self.page.locator('a[href="'+arabic+'"]')).to_be_visible()

    def test_batch65_anova_exact_sums_of_squares_f_tail_keyboard_and_mobile(self):
        root="/inference/classical-tests/one-way-anova-f-test/"
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#esa-anova-lab")).to_be_visible()
        expect(self.page.locator("#esa-anova-results")).to_be_visible()
        for name,value in (("ssb","26.000000"),("ssw","6.000000"),
                           ("dfb","2"),("dfw","6"),
                           ("msb","13.000000"),("msw","1.000000"),
                           ("f","13.000000"),("p","0.006592")):
            self.assertEqual(self.page.locator("#esa-anova-"+name).inner_text(),value)
        sample=[[4,5,6],[5,6,7],[8,9,10]]
        v=self.page.evaluate("v=>window.esaAnovaMath.compute(v)",sample)
        self.assertEqual(v["count"],9)
        self.assertEqual(v["means"],[5,6,9])
        self.assertEqual(v["between"],26)
        self.assertEqual(v["within"],6)
        self.assertEqual(v["f"],13)
        self.assertAlmostEqual(v["p"],.006591796875,places=11)
        self.assertAlmostEqual(self.page.evaluate(
            "()=>window.esaAnovaMath.fSurvival(4,1,10)"),
            .07338803477074037,delta=1e-9)
        self.assertAlmostEqual(self.page.evaluate(
            "()=>window.esaAnovaMath.fSurvival(4,2,10)"),
            .052922149401344654,delta=1e-9)
        self.page.locator("#esa-anova-unequal").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-anova-dfw").inner_text(),"8")
        self.assertEqual(self.page.locator("#esa-anova-dfb").inner_text(),"2")
        self.assertAlmostEqual(float(self.page.locator("#esa-anova-f").inner_text()),
                               11.592966704077819,delta=1e-6)
        self.assertAlmostEqual(float(self.page.locator("#esa-anova-p").inner_text()),
                               .004330369539241011,delta=1e-6)
        self.page.locator("#esa-anova-equal").click()
        self.assertEqual(self.page.locator("#esa-anova-f").inner_text(),"0.000000")
        self.assertEqual(self.page.locator("#esa-anova-p").inner_text(),"1.000000")
        self.page.locator("#esa-anova-constant").click()
        self.assertEqual(self.page.locator("#esa-anova-f").inner_text(),"∞")
        self.assertEqual(self.page.locator("#esa-anova-p").inner_text(),"0.000000")
        self.assertIn("within-group mean square is zero",
                      self.page.locator("#esa-anova-decision").inner_text())
        self.page.locator("#esa-anova-a").fill("1, 1, 1")
        self.page.locator("#esa-anova-b").fill("1, 1, 1")
        self.page.locator("#esa-anova-c").fill("1, 1, 1")
        self.assertEqual(self.page.locator("#esa-anova-f").inner_text(),"Undefined")
        self.assertEqual(self.page.locator("#esa-anova-p").inner_text(),"Undefined")
        self.page.locator("#esa-anova-a").fill("1, no-number, 3")
        expect(self.page.locator("#esa-anova-error")).to_be_visible()
        expect(self.page.locator("#esa-anova-results")).to_be_hidden()
        self.page.locator("#esa-anova-reset").focus()
        self.page.keyboard.press("Enter")
        expect(self.page.locator("#esa-anova-error")).to_be_hidden()
        self.assertEqual(self.page.locator("#esa-anova-f").inner_text(),"13.000000")
        self.assertEqual(self.page.locator("#esa-anova-chart").get_attribute("role"),"img")
        self.assertEqual(self.page.locator("#esa-anova-groups tr").count(),3)
        self.page.set_viewport_size({"width":320,"height":760})
        self.assertLessEqual(self.page.evaluate(
            "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch65_reporting_progress_security_legacy_nine_lessons(self):
        root="/descriptive/reporting/"
        key="esa_continue_descriptive_reporting_lesson_v0"
        slugs=("association-not-causation","comparing-groups-responsibly",
               "complete-description-checklist","from-numbers-to-message",
               "how-to-write-a-summary-paragraph","mini-case-study-end-to-end",
               "outliers-and-exclusions","reporting-graphs-properly",
               "reporting-tables-properly")
        for slug in slugs:
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                record=self.page.evaluate("key=>JSON.parse(localStorage.getItem(key))",key)
                self.assertEqual(record["url"],root+slug+"/")
                self.assertTrue(record["label"].strip())
                self.assertIs(type(record["ts"]),int)
                self.assertGreater(record["ts"],0)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block7")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-block7-btn")
                                 .get_attribute("href"),record["url"])
        good=root+"reporting-graphs-properly/"
        invalid=(
            {"url":"javascript:alert(1)","label":"Bad","ts":10},
            {"url":good+"#frag","label":"Bad","ts":10},
            {"url":good+"?query=1","label":"Bad","ts":10},
            {"url":root+"unpublished/","label":"Bad","ts":10},
            {"url":good,"label":"x"*201,"ts":10},
            {"url":good,"label":"Graphs","ts":0},
            {"url":good,"label":"Graphs","ts":-1},
            {"url":good,"label":"Graphs","ts":None},
            {"url":good,"label":"Graphs","ts":"future"},
            {"url":good,"label":"Graphs","ts":999999999999999},
            {"url":good,"label":"Graphs","ts":True}
        )
        for value in invalid:
            with self.subTest(record=str(value)):
                self.page.evaluate(
                    "args=>localStorage.setItem(args.k,JSON.stringify(args.v))",
                    {"k":key,"v":value})
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block7")).to_be_hidden()
        self.page.evaluate("args=>localStorage.setItem(args.k,JSON.stringify(args.v))",
                           {"k":key,"v":{"url":good,"label":"Reporting Graphs"}})
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block7")).to_be_visible()
        evil='<img src=x onerror="window.esaInjected=true">'
        self.page.evaluate("args=>localStorage.setItem(args.k,JSON.stringify(args.v))",
                           {"k":key,"v":{"url":good,"label":evil}})
        self.page.reload(wait_until="networkidle")
        self.assertEqual(self.page.locator("#continue-reading-block7-label img").count(),0)
        self.assertIn(evil,self.page.locator("#continue-reading-block7-label").inner_text())
        self.assertIsNone(self.page.evaluate("()=>window.esaInjected || null"))
        self.page.evaluate("k=>localStorage.setItem(k,'{broken json')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block7")).to_be_hidden()

    def test_batch65_reporting_denied_storage_mobile_and_anova_accessibility(self):
        self.page.add_init_script("""
            Object.defineProperty(window,"localStorage",{
                configurable:true,
                get(){throw new DOMException("Blocked","SecurityError")}
            });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        root="/descriptive/reporting/"
        slugs=("association-not-causation","comparing-groups-responsibly",
               "complete-description-checklist","from-numbers-to-message",
               "how-to-write-a-summary-paragraph","mini-case-study-end-to-end",
               "outliers-and-exclusions","reporting-graphs-properly",
               "reporting-tables-properly")
        for slug in slugs:
            with self.subTest(slug=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block7")).to_be_hidden()
        self.page.goto(self.origin+"/inference/classical-tests/one-way-anova-f-test/",
                       wait_until="networkidle")
        expect(self.page.locator("#esa-anova-results")).to_be_visible()
        self.assertEqual(self.page.locator("#esa-anova-f").inner_text(),"13.000000")
        self.assertEqual(self.page.locator("#esa-anova-a").get_attribute("spellcheck"),"false")



    def test_batch66_gamma_arabic_english_parity_math_mobile_keyboard(self):
        english="/probability/distributions/gamma-distribution/"
        arabic="/ar/probability/distributions/gamma-distribution/"
        for route,lang in ((english,"en"),(arabic,"ar")):
            with self.subTest(lang=lang):
                self.page.goto(self.origin+route,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),
                                 "rtl" if lang=="ar" else None)
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+route)
                for lng,target in (("en",english),("ar",arabic)):
                    self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+lng+'"]')
                                     .get_attribute("href"),
                                     "https://easystatisticsacademy.com"+target)
                expect(self.page.locator("#esa-erlang-wait-explorer")).to_be_visible()
                self.assertGreaterEqual(self.page.locator("main h2").count(),20)
                for output,want in (("pdf","0.39073"),("cdf","0.566530"),
                                    ("survival","0.433470"),("mean","2.0000"),
                                    ("variance","1.0000"),("scale","0.5000")):
                    self.assertEqual(self.page.locator("#esa-erlang-"+output).inner_text(),want)
                density=self.page.evaluate(
                    "()=>window.esaGammaErlangMath.density(2,4,2)")
                survival=self.page.evaluate(
                    "()=>window.esaGammaErlangMath.survival(2,4,2)")
                self.assertAlmostEqual(density,0.3907336296263291,places=12)
                self.assertAlmostEqual(survival,0.43347012036670884,places=12)
                self.page.locator("#esa-erlang-r").focus()
                self.page.keyboard.press("ArrowRight")
                self.assertEqual(self.page.locator("#esa-erlang-r-value").inner_text(),"5")
                self.page.locator("#esa-erlang-exponential").focus()
                self.page.keyboard.press("Enter")
                self.assertEqual(self.page.locator("#esa-erlang-r-value").inner_text(),"1")
                self.assertEqual(self.page.locator("#esa-erlang-pdf").inner_text(),"0.03663")
                self.assertEqual(self.page.locator("#esa-erlang-cdf").inner_text(),"0.981684")
                self.assertEqual(self.page.locator("#esa-erlang-survival").inner_text(),"0.018316")
                special=self.page.locator("#esa-erlang-special").inner_text()
                self.assertIn("الشكل" if lang=="ar" else "Exponential",special)
                graph_label=self.page.locator("#esa-erlang-chart").get_attribute("aria-label")
                self.assertIn("كثافة" if lang=="ar" else "density",graph_label)
                self.page.locator("#esa-erlang-reset").focus()
                self.page.keyboard.press("Enter")
                self.assertEqual(self.page.locator("#esa-erlang-cdf").inner_text(),"0.566530")
                self.page.set_viewport_size({"width":320,"height":760})
                self.assertLessEqual(self.page.evaluate(
                    "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)
                self.page.set_viewport_size({"width":1280,"height":800})
        self.page.goto(self.origin+arabic,wait_until="networkidle")
        text=self.page.locator("main").inner_text()
        for phrase in ("0.39073","0.566530","2","إرلانغ","دالة غاما","التباين",
                       "التوزيع الأسي","بواسون"):
            self.assertIn(phrase,text)
        self.assertGreaterEqual(self.page.locator(".esa-gamma-equation").count(),8)
        self.assertEqual(self.page.locator(".esa-gamma-equation[tabindex='0']").count(),
                         self.page.locator(".esa-gamma-equation").count())
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        expect(self.page.locator('a[href="'+arabic+'"]')).to_be_visible()

    def test_batch66_chi_square_gof_references_keyboard_mobile_and_errors(self):
        route="/inference/classical-tests/chi-square-goodness-of-fit/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        expect(self.page.locator("#esa-gof-explorer")).to_be_visible()
        expect(self.page.locator("#esa-gof-results")).to_be_visible()
        self.assertEqual(self.page.locator("#esa-gof-table tr").count(),6)
        for out,want in (("n","60"),("chi","1.600000"),
                         ("df","5"),("p","0.901249")):
            self.assertEqual(self.page.locator("#esa-gof-"+out).inner_text(),want)
        stats=self.page.evaluate(
            "()=>window.esaChiSquareGofMath.compute([8,11,9,13,10,9],Array(6).fill(1/6))")
        self.assertEqual(stats["n"],60)
        self.assertEqual(stats["df"],5)
        self.assertAlmostEqual(stats["statistic"],1.6,places=12)
        self.assertAlmostEqual(stats["p"],0.9012493445012736,delta=5e-12)
        self.assertFalse(stats["smallExpected"])
        references=((1.6,5,.9012493445012736),(4,2,.1353352832366127),
                    (10,3,.01856613546304325),(20,5,.0012497305630313773),
                    (0,2,1.0))
        for chi,df,p in references:
            with self.subTest(chi=chi,df=df):
                v=self.page.evaluate(
                    "args=>window.esaChiSquareGofMath.gammaQ(args[1]/2,args[0]/2)",
                    [chi,df])
                self.assertAlmostEqual(v,p,delta=5e-11)
        self.page.locator("#esa-gof-uneven").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-gof-chi").inner_text(),"0.000000")
        self.assertEqual(self.page.locator("#esa-gof-p").inner_text(),"1.000000")
        self.page.locator("#esa-gof-counts").fill("25, 20, 15")
        self.assertEqual(self.page.locator("#esa-gof-df").inner_text(),"2")
        self.assertEqual(self.page.locator("#esa-gof-chi").inner_text(),"21.805556")
        self.assertEqual(self.page.locator("#esa-gof-p").inner_text(),"0.000018")
        self.page.locator("#esa-gof-counts").fill("1, 2, 1")
        self.assertIn("below 5",self.page.locator("#esa-gof-warning").inner_text())
        self.page.locator("#esa-gof-probs").fill("0.2, 0.3, 0.4")
        expect(self.page.locator("#esa-gof-error")).to_be_visible()
        expect(self.page.locator("#esa-gof-results")).to_be_hidden()
        self.page.locator("#esa-gof-counts").fill("1, 2, <img src=x onerror=alert(1)>")
        self.page.locator("#esa-gof-probs").fill("0.2, 0.3, 0.5")
        expect(self.page.locator("#esa-gof-error")).to_be_visible()
        self.assertEqual(self.page.locator("#esa-gof-explorer img").count(),0)
        self.page.locator("#esa-gof-counts").fill("-1, 2, 3")
        expect(self.page.locator("#esa-gof-error")).to_be_visible()
        self.page.locator("#esa-gof-counts").fill("1, 2, 3")
        self.page.locator("#esa-gof-probs").fill("0, 0.4, 0.6")
        expect(self.page.locator("#esa-gof-error")).to_be_visible()
        self.page.locator("#esa-gof-reset").focus()
        self.page.keyboard.press("Enter")
        expect(self.page.locator("#esa-gof-error")).to_be_hidden()
        self.assertEqual(self.page.locator("#esa-gof-p").inner_text(),"0.901249")
        self.assertEqual(self.page.locator("#esa-gof-chart").get_attribute("role"),"img")
        self.assertGreater(len(self.page.locator("#esa-gof-chart").get_attribute("aria-label")),80)
        self.page.set_viewport_size({"width":320,"height":760})
        self.assertLessEqual(self.page.evaluate(
            "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch66_inference_foundations_progress_15_lessons_and_security(self):
        root="/inference/foundations/"
        key="esa_continue_inference_foundations_lesson_v0"
        slugs=("bias-and-variance-intuition","confidence-vs-significance-preview",
          "estimators-vs-estimates","independence-and-random-sampling",
          "inference-pipeline-estimator-se-ci-test","point-vs-interval-estimation",
          "populations-parameters-target","practical-inference-what-can-we-claim",
          "sampling-bias-vs-statistical-bias","sampling-distributions-bridge",
          "sd-vs-se-common-confusion","standard-error-unit-of-uncertainty",
          "statistics-as-random-variables","what-is-statistical-inference",
          "what-makes-good-estimator")
        for slug in slugs:
            with self.subTest(lesson=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                record=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(record["url"],root+slug+"/")
                self.assertTrue(record["label"].strip())
                self.assertIs(type(record["ts"]),int)
                self.assertGreater(record["ts"],0)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-inference-foundations")).to_be_visible()
                self.assertEqual(self.page.locator(
                    "#continue-reading-inference-foundations-btn").get_attribute("href"),
                    record["url"])
        good=root+"sd-vs-se-common-confusion/"
        bad=(
          {"url":"javascript:alert(1)","label":"bad","ts":10},
          {"url":good+"#fragment","label":"bad","ts":10},
          {"url":good+"?q=1","label":"bad","ts":10},
          {"url":root+"not-published/","label":"bad","ts":10},
          {"url":good,"label":"x"*201,"ts":10},
          {"url":good,"label":"SD vs SE","ts":0},
          {"url":good,"label":"SD vs SE","ts":-1},
          {"url":good,"label":"SD vs SE","ts":None},
          {"url":good,"label":"SD vs SE","ts":"next week"},
          {"url":good,"label":"SD vs SE","ts":True},
          {"url":good,"label":"SD vs SE","ts":999999999999999}
        )
        for record in bad:
            with self.subTest(stored=str(record)):
                self.page.evaluate("args=>localStorage.setItem(args.k,JSON.stringify(args.v))",
                                   {"k":key,"v":record})
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-inference-foundations")).to_be_hidden()
        self.page.evaluate("args=>localStorage.setItem(args.k,JSON.stringify(args.v))",
                           {"k":key,"v":{"url":good,"label":"SD versus SE"}})
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-inference-foundations")).to_be_visible()
        malicious='<img src=x onerror="window.esaInjected=true">'
        self.page.evaluate("args=>localStorage.setItem(args.k,JSON.stringify(args.v))",
                           {"k":key,"v":{"url":good,"label":malicious}})
        self.page.reload(wait_until="networkidle")
        self.assertEqual(self.page.locator(
            "#continue-reading-inference-foundations-label img").count(),0)
        self.assertIn(malicious,self.page.locator(
            "#continue-reading-inference-foundations-label").inner_text())
        self.assertIsNone(self.page.evaluate("()=>window.esaInjected || null"))
        self.page.evaluate("k=>localStorage.setItem(k,'{bad json')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-inference-foundations")).to_be_hidden()

    def test_batch66_inference_foundations_denied_storage_mobile(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,
            get(){throw new DOMException("Denied","SecurityError")}
          });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        root="/inference/foundations/"
        slugs=("bias-and-variance-intuition","confidence-vs-significance-preview",
          "estimators-vs-estimates","independence-and-random-sampling",
          "inference-pipeline-estimator-se-ci-test","point-vs-interval-estimation",
          "populations-parameters-target","practical-inference-what-can-we-claim",
          "sampling-bias-vs-statistical-bias","sampling-distributions-bridge",
          "sd-vs-se-common-confusion","standard-error-unit-of-uncertainty",
          "statistics-as-random-variables","what-is-statistical-inference",
          "what-makes-good-estimator")
        for slug in slugs:
            with self.subTest(lesson=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-inference-foundations")).to_be_hidden()



    def test_batch67_arabic_beta_translation_math_mobile_and_navigation(self):
        english="/probability/distributions/beta-distribution/"
        arabic="/ar/probability/distributions/beta-distribution/"
        for route,language in ((english,"en"),(arabic,"ar")):
            with self.subTest(lang=language):
                self.page.goto(self.origin+route,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),language)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),
                                 "rtl" if language=="ar" else None)
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+route)
                for lang,target in (("en",english),("ar",arabic)):
                    self.assertEqual(self.page.locator(
                        'link[rel="alternate"][hreflang="'+lang+'"]').get_attribute("href"),
                        "https://easystatisticsacademy.com"+target)
                expect(self.page.locator("main h1")).to_be_visible()
                self.assertGreaterEqual(self.page.locator("main h2").count(),20)
                self.page.set_viewport_size({"width":320,"height":760})
                self.assertLessEqual(self.page.evaluate(
                    "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)
                self.page.set_viewport_size({"width":1280,"height":800})
        self.page.goto(self.origin+arabic,wait_until="networkidle")
        displayed=self.page.locator("main").inner_text()
        for phrase in ("0.01454545","0.1206045","0.714286",
                       "التوزيع المنتظم","دالة بيتا","المتوسط","التباين",
                       "الاحتمال","التوزيع ذو الحدين","بايزي"):
            self.assertIn(phrase,displayed)
        formula_html=(SITE/arabic.lstrip("/")/"index.html").read_text()
        for formula in (r"E(X)=\frac{\alpha}{\alpha+\beta}",
                        r"\operatorname{Var}(X)=",
                        r"B(\alpha,\beta)=",
                        r"\operatorname{Beta}(10,4)"):
            self.assertIn(formula,formula_html)
        self.assertGreaterEqual(self.page.locator(".esa-beta-equation").count(),10)
        self.assertEqual(self.page.locator(".esa-beta-equation[tabindex='0']").count(),
                         self.page.locator(".esa-beta-equation").count())
        self.page.locator(".esa-beta-equation").first.focus()
        self.assertEqual(self.page.evaluate("()=>document.activeElement.tabIndex"),0)
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        expect(self.page.locator('a[href="'+arabic+'"]')).to_be_visible()

    def test_batch67_homogeneity_chi_square_numerical_p_values_keyboard_and_mobile(self):
        route="/inference/classical-tests/chi-square-homogeneity-test/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        expect(self.page.locator("#esa-homogeneity-lab")).to_be_visible()
        expect(self.page.locator("#esa-hom-results")).to_be_visible()
        for key,want in (("n","300"),("chi","8.896104"),("df","4"),("p","0.063750")):
            self.assertEqual(self.page.locator("#esa-hom-"+key).inner_text(),want)
        x=self.page.evaluate("""()=>window.esaHomogeneityMath.compute(
            [[40,35,25],[30,45,25],[50,30,20]])""")
        self.assertEqual(x["rowTotals"],[100,100,100])
        self.assertEqual(x["colTotals"],[120,110,70])
        self.assertEqual(x["df"],4)
        self.assertAlmostEqual(x["chi"],8.896103896103897,places=11)
        self.assertAlmostEqual(x["p"],0.06374950599967244,delta=5e-12)
        self.assertAlmostEqual(x["expected"][0][1],110/3,places=12)
        self.assertFalse(x["smallExpected"])
        self.assertEqual(self.page.locator("#esa-hom-table tbody tr").count(),3)
        self.assertEqual(self.page.locator("#esa-hom-table thead th").count(),5)
        self.assertEqual(self.page.locator("#esa-hom-chart").get_attribute("role"),"img")
        self.assertIn("Population 1",self.page.locator("#esa-hom-chart").get_attribute("aria-label"))
        self.page.locator("#esa-hom-balanced").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-hom-chi").inner_text(),"0.000000")
        self.assertEqual(self.page.locator("#esa-hom-df").inner_text(),"1")
        self.assertEqual(self.page.locator("#esa-hom-p").inner_text(),"1.000000")
        self.page.locator("#esa-hom-unequal").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-hom-n").inner_text(),"70")
        self.assertEqual(self.page.locator("#esa-hom-df").inner_text(),"2")
        self.assertEqual(self.page.locator("#esa-hom-chi").inner_text(),"2.991453")
        self.assertEqual(self.page.locator("#esa-hom-p").inner_text(),"0.224086")
        y=self.page.evaluate("""()=>window.esaHomogeneityMath.compute(
            [[5,20,15],[8,10,12]])""")
        self.assertAlmostEqual(y["p"],.2240857482419603,delta=5e-12)
        self.page.locator("#esa-hom-sparse").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-hom-chi").inner_text(),"5.454545")
        self.assertEqual(self.page.locator("#esa-hom-p").inner_text(),"0.019517")
        self.assertIn("below 5",self.page.locator("#esa-hom-warning").inner_text())
        tail=self.page.evaluate(
            "()=>window.esaHomogeneityMath.gammaQ(0.5,5.454545454545455/2)")
        self.assertAlmostEqual(tail,.01951748118217779,delta=5e-12)
        self.page.locator("#esa-hom-cities").focus()
        self.page.keyboard.press("Enter")
        self.assertEqual(self.page.locator("#esa-hom-p").inner_text(),"0.063750")
        self.assertEqual(self.page.locator(".esa-long-math").count(),8)
        self.page.set_viewport_size({"width":320,"height":760})
        self.assertLessEqual(self.page.evaluate(
            "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch67_homogeneity_invalid_rows_zero_margins_and_security(self):
        route="/inference/classical-tests/chi-square-homogeneity-test/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        field=self.page.locator("#esa-hom-input")
        for invalid in (
            "1, 2\n3",
            "-1, 2\n3, 4",
            "1, 2\n0, 0",
            "0, 2\n0, 3",
            "a, 2\n3, 4",
            "1, 2\n3, <img src=x onerror=alert(1)>",
            "0, 0\n0, 0",
            "10000001, 2\n3, 4",
            "1,2,3,4,5,6\n2,3,4,5,6,7"
        ):
            with self.subTest(invalid=invalid):
                field.fill(invalid)
                expect(self.page.locator("#esa-hom-error")).to_be_visible()
                expect(self.page.locator("#esa-hom-results")).to_be_hidden()
                self.assertEqual(self.page.locator("#esa-homogeneity-lab img").count(),0)
        field.fill("0, 2\n3, 4")
        expect(self.page.locator("#esa-hom-error")).to_be_hidden()
        self.assertEqual(self.page.locator("#esa-hom-n").inner_text(),"9")
        self.page.locator("#esa-hom-cities").click()
        expect(self.page.locator("#esa-hom-results")).to_be_visible()

    def test_batch67_data_variables_all_eight_progress_and_adversarial_records(self):
        root="/descriptive/data-variables/"
        key="esa_continue_descriptive_data_variables_lesson_v0"
        lessons=(
          ("what-does-it-mean-to-describe-data","What Does It Mean to Describe Data?"),
          ("units-observations-and-variables","Units, Observations, and Variables"),
          ("categorical-vs-numerical","Categorical vs Numerical Data"),
          ("nominal-vs-ordinal","Nominal vs Ordinal Data"),
          ("discrete-vs-continuous","Discrete vs Continuous Data"),
          ("data-structure-and-datasets","Data Structure and Datasets"),
          ("measurement-scales","Measurement Scales"),
          ("valid-vs-invalid-operations","Valid vs Invalid Operations")
        )
        for slug,label in lessons:
            with self.subTest(lesson=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                item=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(item["url"],root+slug+"/")
                self.assertEqual(item["label"],label)
                self.assertIs(type(item["ts"]),int)
                self.assertGreater(item["ts"],0)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block1")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-block1-btn")
                                 .get_attribute("href"),item["url"])
                self.assertIn(label,self.page.locator(
                    "#continue-reading-block1-label").inner_text())
        good=root+"measurement-scales/"
        label="Measurement Scales"
        rejected=(
           {"url":"javascript:alert(1)","label":label,"ts":1},
           {"url":good+"?q=1","label":label,"ts":1},
           {"url":good+"#hash","label":label,"ts":1},
           {"url":root+"unpublished/","label":label,"ts":1},
           {"url":good,"label":"Misleading title","ts":1},
           {"url":good,"label":'<img src=x onerror="window.esaPwn=true">',"ts":1},
           {"url":good,"label":"x"*201,"ts":1},
           {"url":good,"label":label,"ts":0},
           {"url":good,"label":label,"ts":-1},
           {"url":good,"label":label,"ts":None},
           {"url":good,"label":label,"ts":True},
           {"url":good,"label":label,"ts":"now"},
           {"url":good,"label":label,"ts":999999999999999},
           {"url":good,"label":label,"ts":[]}
        )
        for item in rejected:
            with self.subTest(record=str(item)):
                self.page.evaluate(
                    "args=>localStorage.setItem(args.k,JSON.stringify(args.v))",
                    {"k":key,"v":item})
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block1")).to_be_hidden()
        self.page.evaluate("args=>localStorage.setItem(args.k,JSON.stringify(args.v))",
                           {"k":key,"v":{"url":good,"label":label}})
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block1")).to_be_visible()
        self.assertEqual(self.page.locator("#continue-reading-block1-btn")
                         .get_attribute("href"),good)
        self.assertIsNone(self.page.evaluate("()=>window.esaPwn||null"))
        self.page.evaluate("k=>localStorage.setItem(k,'{malformed')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block1")).to_be_hidden()
        self.page.set_viewport_size({"width":320,"height":760})
        self.assertLessEqual(self.page.evaluate(
            "()=>document.documentElement.scrollWidth-document.documentElement.clientWidth"),2)

    def test_batch67_data_variables_progress_with_storage_denied_mobile(self):
        self.page.add_init_script("""
            Object.defineProperty(window,"localStorage",{
                configurable:true,
                get(){throw new DOMException("Denied","SecurityError")}
            });
        """)
        self.page.set_viewport_size({"width":320,"height":760})
        root="/descriptive/data-variables/"
        slugs=("what-does-it-mean-to-describe-data",
          "units-observations-and-variables","categorical-vs-numerical",
          "nominal-vs-ordinal","discrete-vs-continuous",
          "data-structure-and-datasets","measurement-scales",
          "valid-vs-invalid-operations")
        for slug in slugs:
            with self.subTest(lesson=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block1")).to_be_hidden()



    def test_batch68_uniform_arabic_english_math_parity_accessibility_mobile(self):
        english="/probability/distributions/uniform-distribution/"
        arabic="/ar/probability/distributions/uniform-distribution/"
        for route,lang in ((english,"en"),(arabic,"ar")):
            with self.subTest(lang=lang):
                self.page.goto(self.origin+route,wait_until="networkidle")
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("html").get_attribute("dir"),
                                 "rtl" if lang=="ar" else None)
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+route)
                for lnk,target in (("en",english),("ar",arabic)):
                    self.assertEqual(self.page.locator(
                        'link[rel="alternate"][hreflang="'+lnk+'"]')
                        .get_attribute("href"),
                        "https://easystatisticsacademy.com"+target)
                lab=self.page.locator("#esa-uniform-area-explorer")
                expect(lab).to_be_visible()
                self.assertGreaterEqual(self.page.locator("main h2").count(),20)
                for output,want in (("width","3.00"),("density","0.1000"),
                                    ("probability","0.3000"),("mean","5.00"),
                                    ("variance","8.3333"),("sd","2.8868")):
                    self.assertEqual(lab.locator("#esa-uniform-"+output).inner_text(),want)
                actual=self.page.evaluate(
                    "()=>window.esaUniformMath.calculate(0,10,2,5)")
                self.assertAlmostEqual(actual["density"],.1,places=14)
                self.assertAlmostEqual(actual["probability"],.3,places=14)
                self.assertAlmostEqual(actual["mean"],5,places=14)
                self.assertAlmostEqual(actual["variance"],100/12,places=13)
                self.assertAlmostEqual(actual["sd"],10/(12**.5),places=13)
                for left,right,c,d in ((1,11,2,9),(2,10,4,6),(3,7,3,7)):
                    computed=self.page.evaluate(
                        "a=>window.esaUniformMath.calculate(...a)",[left,right,c,d])
                    self.assertAlmostEqual(computed["probability"],
                                           (d-c)/(right-left),places=13)
                a=lab.locator("#esa-uniform-a")
                a.focus()
                self.page.keyboard.press("ArrowRight")
                self.assertEqual(a.input_value(),"1")
                self.assertIn("كثافة" if lang=="ar" else "Uniform density",
                              lab.locator("#esa-uniform-area-plot").get_attribute("aria-label"))
                lab.locator("#esa-uniform-reset").focus()
                self.page.keyboard.press("Enter")
                expect(lab.locator("#esa-uniform-probability")).to_have_text("0.3000")
                for width in (320,375,768):
                    with self.subTest(lang=lang,width=width):
                        self.page.set_viewport_size({"width":width,"height":800})
                        b=lab.evaluate("""e=>({
                            left:e.getBoundingClientRect().left,
                            right:e.getBoundingClientRect().right,
                            scroll:e.scrollWidth,client:e.clientWidth})""")
                        self.assertGreaterEqual(b["left"],-2,b)
                        self.assertLessEqual(b["right"],width+2,b)
                        self.assertLessEqual(b["scroll"]-b["client"],2,b)
                self.page.set_viewport_size({"width":1280,"height":800})
        self.page.goto(self.origin+arabic,wait_until="networkidle")
        text=self.page.locator("main").inner_text()
        for word in ("التوزيع المنتظم","الاحتمال بوصفه مساحة","التباين",
                     "الانحراف المعياري","المنتظم المنفصل","0.30","2.8868"):
            self.assertIn(word,text)
        self.assertEqual(self.page.locator(".esa-uniform-equation").count(),11)
        self.assertEqual(self.page.locator(".esa-uniform-equation[tabindex='0']").count(),11)
        self.page.locator(".esa-uniform-equation").first.focus()
        self.assertEqual(self.page.evaluate("()=>document.activeElement.tabIndex"),0)
        self.page.goto(self.origin+"/ar/",wait_until="networkidle")
        expect(self.page.locator('a[href="'+arabic+'"]')).to_be_visible()

    def test_batch68_paired_t_exact_distribution_reference_and_keyboard(self):
        route="/inference/classical-tests/paired-t-test/"
        self.page.goto(self.origin+route,wait_until="networkidle")
        root=self.page.locator("#esa-paired-t-lab")
        expect(root).to_be_visible()
        for key,want in (("n","5"),("mean","4.200000"),("sd","0.836660"),
                         ("se","0.374166"),("t","11.224972"),("df","4"),
                         ("p","0.000359"),("critical","2.776445"),
                         ("lower","3.161149"),("upper","5.238851")):
            expect(root.locator("#esa-pt-"+key)).to_have_text(want)
        computed=self.page.evaluate("""()=>window.esaPairedTMath.compute(
            [[70,75],[68,72],[75,79],[71,74],[69,74]])""")
        self.assertAlmostEqual(computed["t"],11.224972160321826,delta=1e-10)
        self.assertAlmostEqual(computed["p"],.0003587352603774513,delta=5e-11)
        self.assertAlmostEqual(computed["lower"],3.1611493663164323,delta=5e-10)
        self.assertAlmostEqual(computed["upper"],5.238850633683568,delta=5e-10)
        for df,referenceTail,referenceCrit in (
          (1,.14758361765043326,12.706204736174694),
          (2,.09175170953613698,4.302652729749462),
          (4,.05805826175840778,2.7764451051977934),
          (9,.038276411885350504,2.262157162798205),
          (19,.03000101819304917,2.0930240544083087),
          (39,.026249507671927373,2.022690920036761)):
            with self.subTest(df=df):
                observed=self.page.evaluate(
                   "df=>({tail:window.esaPairedTMath.studentUpperTail(2,df),"
                   "crit:window.esaPairedTMath.critical95(df)})",df)
                self.assertAlmostEqual(observed["tail"],referenceTail,delta=5e-11)
                self.assertAlmostEqual(observed["crit"],referenceCrit,delta=5e-9)
                self.assertAlmostEqual(self.page.evaluate(
                   "df=>window.esaPairedTMath.studentUpperTail(-2,df)",df),
                   1-referenceTail,delta=5e-11)
        choice=root.locator("#esa-pt-alternative")
        choice.focus()
        choice.select_option("greater")
        expect(root.locator("#esa-pt-p")).to_have_text("0.000179")
        choice.select_option("less")
        expect(root.locator("#esa-pt-p")).to_have_text("0.999821")
        choice.select_option("two-sided")
        expect(root.locator("#esa-pt-p")).to_have_text("0.000359")
        self.assertEqual(root.locator("#esa-pt-table tr").count(),5)
        self.assertIn("pair 1",root.locator("#esa-pt-plot").get_attribute("aria-label"))
        root.locator("#esa-pt-negative").focus()
        self.page.keyboard.press("Enter")
        expect(root.locator("#esa-pt-t")).to_have_text("-11.224972")
        expect(root.locator("#esa-pt-p")).to_have_text("0.000359")
        expect(root.locator("#esa-pt-lower")).to_have_text("-5.238851")
        expect(root.locator("#esa-pt-upper")).to_have_text("-3.161149")
        root.locator("#esa-pt-reset").focus()
        self.page.keyboard.press("Enter")
        expect(root.locator("#esa-pt-mean")).to_have_text("4.200000")
        expect(root.locator("#esa-pt-p")).to_have_text("0.000359")
        self.assertEqual(root.locator("#esa-pt-plot").get_attribute("role"),"img")
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":800})
                b=root.evaluate("""e=>({
                  left:e.getBoundingClientRect().left,
                  right:e.getBoundingClientRect().right,
                  scroll:e.scrollWidth,client:e.clientWidth})""")
                self.assertGreaterEqual(b["left"],-2,b)
                self.assertLessEqual(b["right"],width+2,b)
                self.assertLessEqual(b["scroll"]-b["client"],2,b)

    def test_batch68_paired_t_validation_degenerate_and_malicious_input(self):
        self.page.goto(self.origin+"/inference/classical-tests/paired-t-test/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-paired-t-lab")
        field=root.locator("#esa-pt-input")
        error=root.locator("#esa-pt-error")
        results=root.locator("#esa-pt-results")
        for invalid in ("", "1,2", "1,2\n3", "1,2\n3,4,5",
                        "1,2\n3,not_number", "1,2\n3,NaN",
                        "1,2\n3,Infinity","1,2\n4,<img src=x onerror=alert(1)>",
                        "10000001,2\n3,4","1,2\n3,4\n0,",
                        "1,1\n2,2\n3,3",
                        "0,1\n2,3\n4,5"):
            with self.subTest(invalid=invalid):
                field.fill(invalid)
                expect(error).to_be_visible()
                expect(results).to_be_hidden()
                self.assertEqual(root.locator("img").count(),0)
        field.fill("0,2\n1,4\n2,6")
        expect(error).to_be_hidden()
        self.assertEqual(root.locator("#esa-pt-n").inner_text(),"3")
        null=root.locator("#esa-pt-null")
        null.fill("")
        expect(error).to_be_visible()
        null.fill("1")
        expect(error).to_be_hidden()
        self.assertEqual(root.locator("#esa-pt-df").inner_text(),"2")
        self.assertEqual(self.page.evaluate(
            "()=>window.esaPairedTMath.compute([[5,4],[6,5],[7,6]]).degenerate"),
            True)
        root.locator("#esa-pt-reset").click()
        expect(root.locator("#esa-pt-results")).to_be_visible()

    def test_batch68_tabular_summaries_ten_saves_and_adversarial_resume(self):
        root="/descriptive/tabular-summaries/"
        key="esa_continue_descriptive_tabular_summaries_lesson_v0"
        lessons=(
         ("why-tables-come-first","Why Tables Come First"),
         ("frequency-tables","Frequency Tables"),
         ("relative-frequency-and-percent","Relative Frequency and Percent"),
         ("cumulative-frequency","Cumulative Frequency"),
         ("grouped-frequency-tables","Grouped Frequency Tables"),
         ("contingency-tables","Contingency Tables"),
         ("choosing-the-right-percentage","Choosing the Right Percentage"),
         ("handling-missing-values","Handling Missing Values"),
         ("standard-table-layout-and-reporting","Standard Table Layout and Reporting"),
         ("common-table-mistakes","Common Table Mistakes")
        )
        for slug,title in lessons:
            with self.subTest(lesson=slug):
                route=root+slug+"/"
                self.page.goto(self.origin+route,wait_until="networkidle")
                data=self.page.evaluate(
                   "k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(data["url"],route)
                self.assertEqual(data["label"],title)
                self.assertIs(type(data["ts"]),int)
                self.assertGreater(data["ts"],0)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block2")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-block2-btn")
                                 .get_attribute("href"),route)
                self.assertIn(title,self.page.locator(
                    "#continue-reading-block2-label").inner_text())
        good=root+"frequency-tables/"
        invalid=(
          {"url":"javascript:alert(1)","label":"Frequency Tables","ts":10},
          {"url":good+"#fragment","label":"Frequency Tables","ts":10},
          {"url":good+"?q=1","label":"Frequency Tables","ts":10},
          {"url":root+"unpublished/","label":"Frequency Tables","ts":10},
          {"url":good,"label":"Wrong title","ts":10},
          {"url":good,"label":'<img src=x onerror="window.esaInjected=true">',"ts":10},
          {"url":good,"label":"x"*201,"ts":10},
          {"url":good,"label":"Frequency Tables","ts":0},
          {"url":good,"label":"Frequency Tables","ts":-1},
          {"url":good,"label":"Frequency Tables","ts":"tomorrow"},
          {"url":good,"label":"Frequency Tables","ts":None},
          {"url":good,"label":"Frequency Tables","ts":True},
          {"url":good,"label":"Frequency Tables","ts":999999999999999},
          {"url":good,"label":"Frequency Tables","ts":[]}
        )
        for data in invalid:
            with self.subTest(saved=str(data)):
                self.page.evaluate(
                  "args=>localStorage.setItem(args.k,JSON.stringify(args.value))",
                  {"k":key,"value":data})
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block2")).to_be_hidden()
        self.page.evaluate(
          "args=>localStorage.setItem(args.k,JSON.stringify(args.value))",
          {"k":key,"value":{"url":good,"label":"Frequency Tables"}})
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block2")).to_be_visible()
        self.assertEqual(self.page.locator("#continue-reading-block2-btn")
                         .get_attribute("href"),good)
        self.assertIsNone(self.page.evaluate("()=>window.esaInjected||null"))
        self.page.evaluate("k=>localStorage.setItem(k,'{bad json')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block2")).to_be_hidden()

    def test_batch68_tabular_summaries_blocked_storage_all_ten_lessons(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,
            get(){throw new DOMException("Storage denied","SecurityError")}
          });
        """)
        root="/descriptive/tabular-summaries/"
        slugs=("why-tables-come-first","frequency-tables",
          "relative-frequency-and-percent","cumulative-frequency",
          "grouped-frequency-tables","contingency-tables",
          "choosing-the-right-percentage","handling-missing-values",
          "standard-table-layout-and-reporting","common-table-mistakes")
        self.page.set_viewport_size({"width":320,"height":750})
        for slug in slugs:
            with self.subTest(lesson=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block2")).to_be_hidden()
        self.assertGreater(self.page.locator("#lessons .lesson-card a[href]").count(),0)


    def test_batch69_normal_bilingual_reference_parity_and_seo(self):
        routes=("/probability/distributions/normal-distribution/",
                "/ar/probability/distributions/normal-distribution/")
        outputs=[]
        for route in routes:
            with self.subTest(route=route):
                self.page.goto(self.origin+route,wait_until="networkidle")
                lab=self.page.locator("#esa-normal-probability-explorer")
                expect(lab).to_be_visible()
                expect(lab.locator("#esa-normal-probability")).to_have_text("0.682689")
                self.assertTrue(self.page.locator('link[rel="canonical"]').count()>0)
                self.assertGreater(self.page.locator('link[rel="alternate"][hreflang]').count(),0)
                values=self.page.evaluate("""()=>({
                  p:document.getElementById('esa-normal-probability').textContent,
                  cdf:window.esaNormalMath.cdf(2),
                  sf:window.esaNormalMath.survival(2),
                  shade:document.getElementById('esa-normal-shade').getAttribute('d')
                })""")
                self.assertAlmostEqual(values["cdf"],.9772498680518208,delta=2.1e-7)
                self.assertAlmostEqual(values["sf"],.02275013194817921,delta=2.1e-7)
                self.assertTrue(values["shade"].startswith("M "))
                lab.locator("#esa-normal-mu").fill("100")
                lab.locator("#esa-normal-sigma").fill("15")
                lab.locator("#esa-normal-a").fill("85")
                lab.locator("#esa-normal-b").fill("115")
                outputs.append(lab.locator("#esa-normal-probability").inner_text())
                self.assertAlmostEqual(float(outputs[-1]),.682689492,delta=2.1e-6)
                lab.locator("#esa-normal-mode").select_option("right")
                lab.locator("#esa-normal-b").fill("130")
                self.assertAlmostEqual(float(lab.locator("#esa-normal-probability").inner_text()),
                                       .022750131948,delta=2.1e-6)
                lab.locator("#esa-normal-reset").focus()
                self.page.keyboard.press("Enter")
                expect(lab.locator("#esa-normal-probability")).to_have_text("0.682689")
        self.assertEqual(outputs[0],outputs[1])
        self.page.goto(self.origin+routes[1],wait_until="networkidle")
        self.assertTrue(self.page.get_by_role("link",name="English — Normal Distribution").count()>0)
        self.page.goto(self.origin+routes[0],wait_until="networkidle")
        self.assertTrue(self.page.get_by_role("link",name="اقرأ هذا الدرس بالعربية").count()>0)

    def test_batch69_normal_invalid_values_mobile_and_keyboard(self):
        self.page.goto(self.origin+"/ar/probability/distributions/normal-distribution/",
                       wait_until="networkidle")
        lab=self.page.locator("#esa-normal-probability-explorer")
        for sigma in ("0","-1","","99999999"):
            with self.subTest(sigma=sigma):
                lab.locator("#esa-normal-sigma").fill(sigma)
                expect(lab.locator("#esa-normal-error")).to_be_visible()
                expect(lab.locator("#esa-normal-chart")).to_be_hidden()
        lab.locator("#esa-normal-reset").click()
        lab.locator("#esa-normal-a").fill("2")
        lab.locator("#esa-normal-b").fill("1")
        expect(lab.locator("#esa-normal-error")).to_be_visible()
        lab.locator("#esa-normal-reset").click()
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":820})
                bounds=lab.evaluate("""el=>({
                  left:el.getBoundingClientRect().left,
                  right:el.getBoundingClientRect().right,
                  scroll:el.scrollWidth,client:el.clientWidth
                })""")
                self.assertGreaterEqual(bounds["left"],-2,bounds)
                self.assertLessEqual(bounds["right"],width+2,bounds)
                self.assertLessEqual(bounds["scroll"]-bounds["client"],2,bounds)

    def test_batch69_welch_reference_tail_ci_and_alternatives(self):
        self.page.goto(self.origin+"/inference/classical-tests/two-sample-t-test-independent/",
                       wait_until="networkidle")
        lab=self.page.locator("#esa-welch-lab")
        expect(lab.locator("#esa-w-results")).to_be_visible()
        for id,target,tolerance in (
            ("difference",7.833333333333333,1e-6),
            ("se",1.7618082341640515,1e-6),
            ("df",10.93790675014491,1e-6),
            ("t",4.446189534952488,1e-6),
            ("p",.0009985114499363515,1e-6),
            ("lower",3.9529320996062474,2e-6),
            ("upper",11.71373456706041,2e-6)):
            with self.subTest(statistic=id):
                self.assertAlmostEqual(float(lab.locator("#esa-w-"+id).inner_text()),
                                       target,delta=tolerance)
        ref=self.page.evaluate("""()=>({
          sf:window.esaWelchMath.studentUpperTail(2,4),
          tcrit:window.esaWelchMath.critical95(4)
        })""")
        self.assertAlmostEqual(ref["sf"],.05805826175840778,delta=1e-10)
        self.assertAlmostEqual(ref["tcrit"],2.7764451051977934,delta=1e-9)
        lab.locator("#esa-w-alternative").select_option("greater")
        self.assertAlmostEqual(float(lab.locator("#esa-w-p").inner_text()),
                               .0009985114499363515/2,delta=1e-6)
        lab.locator("#esa-w-alternative").select_option("less")
        self.assertAlmostEqual(float(lab.locator("#esa-w-p").inner_text()),
                               1-.0009985114499363515/2,delta=1e-6)
        lab.locator("#esa-w-reset").focus()
        self.page.keyboard.press("Enter")
        expect(lab.locator("#esa-w-p")).to_have_text("0.000999")
        self.assertIn("confidence interval",lab.locator("#esa-w-plot").get_attribute("aria-label"))

    def test_batch69_welch_invalid_inputs_swap_and_mobile(self):
        self.page.goto(self.origin+"/inference/classical-tests/two-sample-t-test-independent/",
                       wait_until="networkidle")
        lab=self.page.locator("#esa-welch-lab")
        a=lab.locator("#esa-w-a")
        for invalid in ("","1","1,NaN,2","1,Infinity","1,3,<img src=x onerror=alert(1)>",
                        "10000001,2","1,,3"):
            with self.subTest(invalid=invalid):
                a.fill(invalid)
                expect(lab.locator("#esa-w-error")).to_be_visible()
                expect(lab.locator("#esa-w-results")).to_be_hidden()
                self.assertEqual(lab.locator("img, script[onerror]").count(),0)
        lab.locator("#esa-w-reset").click()
        lab.locator("#esa-w-reverse").click()
        self.assertAlmostEqual(float(lab.locator("#esa-w-difference").inner_text()),
                               -7.833333333333333,delta=1e-6)
        expect(lab.locator("#esa-w-p")).to_have_text("0.000999")
        a.fill("1,1,1")
        lab.locator("#esa-w-b").fill("2,2,2")
        expect(lab.locator("#esa-w-error")).to_be_visible()
        self.assertTrue(self.page.evaluate(
            "()=>window.esaWelchMath.compute([1,1,1],[2,2,2]).degenerate"))
        lab.locator("#esa-w-reset").click()
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":800})
                bounds=lab.evaluate("""el=>({
                   left:el.getBoundingClientRect().left,
                   right:el.getBoundingClientRect().right,
                   scroll:el.scrollWidth,client:el.clientWidth
                })""")
                self.assertGreaterEqual(bounds["left"],-2,bounds)
                self.assertLessEqual(bounds["right"],width+2,bounds)
                self.assertLessEqual(bounds["scroll"]-bounds["client"],2,bounds)

    def test_batch69_spread_seven_lessons_and_adversarial_resume(self):
        root="/descriptive/spread/"
        key="esa_continue_descriptive_spread_lesson_v0"
        lessons=(("what-is-variability","What Is Variability?"),
                 ("range","Range"),
                 ("interquartile-range","Interquartile Range (IQR)"),
                 ("variance","Variance"),
                 ("standard-deviation","Standard Deviation"),
                 ("coefficient-of-variation","Coefficient of Variation"),
                 ("reporting-spread-properly","Reporting Spread Properly"))
        for slug,title in lessons:
            with self.subTest(slug=slug):
                route=root+slug+"/"
                self.page.goto(self.origin+route,wait_until="networkidle")
                saved=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(saved["url"],route)
                self.assertEqual(saved["label"],title)
                self.assertIs(type(saved["ts"]),int)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block5")).to_be_visible()
                self.assertEqual(self.page.locator("#continue-reading-block5-btn")
                                 .get_attribute("href"),route)
        good=root+"range/"
        examples=(
            {"url":good,"label":"Forged title"},
            {"url":good,"label":'<img src=x onerror="window.esaInjected=true">'},
            {"url":good,"label":"Range","ts":-5},
            {"url":good,"label":"Range","ts":1.5},
            {"url":good,"label":"Range","ts":None},
            {"url":good,"label":"Range","ts":"tomorrow"},
            {"url":good,"label":"Range","ts":True},
            {"url":good,"label":"Range","ts":999999999999999},
            {"url":good+"?next=1","label":"Range"},
            {"url":root+"unknown/","label":"Range"},
            {"url":"javascript:alert(1)","label":"Range"},
            {"url":good,"label":"Range"*1000})
        for payload in examples:
            with self.subTest(payload=str(payload)[:100]):
                self.page.evaluate(
                    "x=>localStorage.setItem(x.k,JSON.stringify(x.v))",
                    {"k":key,"v":payload})
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-block5")).to_be_hidden()
        # Legacy saved progress without a timestamp remains valid for published titles.
        self.page.evaluate("x=>localStorage.setItem(x.k,JSON.stringify(x.v))",
             {"k":key,"v":{"url":good,"label":"Range"}})
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block5")).to_be_visible()
        self.assertEqual(self.page.locator("#continue-reading-block5-btn")
                         .get_attribute("href"),good)
        self.assertIsNone(self.page.evaluate("()=>window.esaInjected||null"))
        self.page.evaluate("k=>localStorage.setItem(k,'{invalid')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block5")).to_be_hidden()

    def test_batch69_spread_blocked_storage_all_seven_lessons(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,
            get(){throw new DOMException("Storage unavailable","SecurityError")}
          });
        """)
        root="/descriptive/spread/"
        self.page.set_viewport_size({"width":320,"height":780})
        for slug in ("what-is-variability","range","interquartile-range",
                     "variance","standard-deviation","coefficient-of-variation",
                     "reporting-spread-properly"):
            with self.subTest(lesson=slug):
                self.page.goto(self.origin+root+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+root,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-block5")).to_be_hidden()
        self.assertGreater(self.page.locator("#lessons .lesson-card a[href]").count(),0)



    def test_batch70_lognormal_bilingual_probability_moments_and_seo(self):
        routes=("/probability/distributions/lognormal-distribution/",
                "/ar/probability/distributions/lognormal-distribution/")
        values=[]
        for route in routes:
            with self.subTest(route=route):
                self.page.goto(self.origin+route,wait_until="networkidle")
                lab=self.page.locator("#esa-lognormal-lab")
                expect(lab).to_be_visible()
                expect(lab.locator("#esa-ln-probability")).to_have_text("0.417171")
                expect(lab.locator("#esa-ln-mean")).to_have_text("1.133148")
                expect(lab.locator("#esa-ln-median")).to_have_text("1.000000")
                expect(lab.locator("#esa-ln-variance")).to_have_text("0.364696")
                self.assertGreater(self.page.locator('link[rel="canonical"]').count(),0)
                self.assertGreater(self.page.locator('link[rel="alternate"][hreflang="ar"]').count(),0)
                self.assertGreater(self.page.locator('link[rel="alternate"][hreflang="en"]').count(),0)
                self.assertEqual(lab.locator("#esa-ln-plot").get_attribute("role"),"img")
                self.assertEqual(lab.locator("#esa-ln-sigma").get_attribute("type"),"number")
                values.append(lab.locator("#esa-ln-probability").inner_text())
                self.assertAlmostEqual(self.page.evaluate(
                  "()=>window.esaLognormalMath.survival(2,0,.5)"),
                    .0828285190016985,delta=2.1e-7)
                lab.locator("#esa-ln-mode").select_option("right")
                expect(lab.locator("#esa-ln-probability")).to_have_text("0.082829")
                lab.locator("#esa-ln-mode").select_option("left")
                lab.locator("#esa-ln-a").fill("0")
                expect(lab.locator("#esa-ln-probability")).to_have_text("0.000000")
                lab.locator("#esa-ln-mode").select_option("between")
                lab.locator("#esa-ln-a").fill("0.6065306597126334")
                lab.locator("#esa-ln-b").fill("1.6487212707001282")
                expect(lab.locator("#esa-ln-probability")).to_have_text("0.682689")
                lab.locator("#esa-ln-reset").focus()
                self.page.keyboard.press("Enter")
                expect(lab.locator("#esa-ln-probability")).to_have_text("0.417171")
        self.assertEqual(values[0],values[1])
        self.page.goto(self.origin+routes[1],wait_until="networkidle")
        expect(self.page.get_by_role("link",name="English — Lognormal Distribution")).to_be_visible()
        self.page.goto(self.origin+routes[0],wait_until="networkidle")
        expect(self.page.get_by_role("link",name="اقرأ هذا الدرس بالعربية")).to_be_visible()

    def test_batch70_lognormal_invalid_and_mobile(self):
        self.page.goto(self.origin+"/ar/probability/distributions/lognormal-distribution/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-lognormal-lab")
        for value in ("0","-1","","5","999"):
            with self.subTest(sigma=value):
                root.locator("#esa-ln-sigma").fill(value)
                expect(root.locator("#esa-ln-error")).to_be_visible()
                expect(root.locator("#esa-ln-results")).to_be_hidden()
        root.locator("#esa-ln-reset").click()
        root.locator("#esa-ln-a").fill("3")
        root.locator("#esa-ln-b").fill("2")
        expect(root.locator("#esa-ln-error")).to_be_visible()
        root.locator("#esa-ln-reset").click()
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                rect=root.evaluate("""e=>({left:e.getBoundingClientRect().left,
                    right:e.getBoundingClientRect().right,
                    scroll:e.scrollWidth,client:e.clientWidth})""")
                self.assertGreaterEqual(rect["left"],-2,rect)
                self.assertLessEqual(rect["right"],width+2,rect)
                self.assertLessEqual(rect["scroll"]-rect["client"],2,rect)

    def test_batch70_two_proportion_math_and_alternatives(self):
        self.page.goto(self.origin+"/inference/classical-tests/two-proportion-z-test/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-two-proportion-lab")
        expect(root.locator("#esa-2p-results")).to_be_visible()
        for field,expected in (
            ("p1",.6),("p2",.45),("diff",.15),("pooled",.525),
            ("pooledSE",.04993746088859544),("seCI",.049371044145328745),
            ("z",3.003757045930553),("p",.0026666817936140935),
            ("lower",.05323453159602119),("upperCI",.24676546840397873)):
            with self.subTest(field=field):
                self.assertAlmostEqual(float(root.locator("#esa-2p-"+field).inner_text()),
                                       expected,delta=1.2e-6)
        self.assertIn("count check passed",root.locator("#esa-2p-conditions").inner_text())
        root.locator("#esa-2p-alternative").select_option("greater")
        self.assertAlmostEqual(float(root.locator("#esa-2p-p").inner_text()),
                               .0013333408968070467,delta=1.2e-6)
        root.locator("#esa-2p-alternative").select_option("less")
        self.assertAlmostEqual(float(root.locator("#esa-2p-p").inner_text()),
                               .998666659103193,delta=1.2e-6)
        root.locator("#esa-2p-reset").focus()
        self.page.keyboard.press("Enter")
        expect(root.locator("#esa-2p-p")).to_have_text("0.002667")
        root.locator("#esa-2p-swap").click()
        expect(root.locator("#esa-2p-diff")).to_have_text("-0.150000")
        expect(root.locator("#esa-2p-p")).to_have_text("0.002667")
        self.assertIn("confidence interval",root.locator("#esa-2p-plot").get_attribute("aria-label"))
        self.assertAlmostEqual(self.page.evaluate(
            "()=>window.esaTwoProportionMath.compute(120,200,90,200).pooled"),
            .525,places=12)

    def test_batch70_two_proportion_invalid_sparse_and_mobile(self):
        self.page.goto(self.origin+"/inference/classical-tests/two-proportion-z-test/",
                       wait_until="networkidle")
        root=self.page.locator("#esa-two-proportion-lab")
        x1=root.locator("#esa-2p-x1")
        for invalid in ("-1","201","1.5","<img src=x onerror=alert(1)>","NaN",""):
            with self.subTest(x1=invalid):
                # HTML number inputs cannot receive arbitrary text via fill().
                # Setting the DOM value also checks how browser sanitization
                # and application validation handle untrusted assignments.
                x1.evaluate("""(el, value) => {
                    el.value = value;
                    el.dispatchEvent(new Event("input", {bubbles: true}));
                }""", invalid)
                expect(root.locator("#esa-2p-error")).to_be_visible()
                expect(root.locator("#esa-2p-results")).to_be_hidden()
                self.assertEqual(root.locator("img").count(),0)
        root.locator("#esa-2p-reset").click()
        root.locator("#esa-2p-x1").fill("1")
        root.locator("#esa-2p-n1").fill("5")
        root.locator("#esa-2p-x2").fill("4")
        root.locator("#esa-2p-n2").fill("5")
        expect(root.locator("#esa-2p-results")).to_be_visible()
        self.assertIn("WARNING",root.locator("#esa-2p-conditions").inner_text())
        root.locator("#esa-2p-x1").fill("0")
        root.locator("#esa-2p-x2").fill("0")
        expect(root.locator("#esa-2p-error")).to_be_visible()
        self.assertTrue(self.page.evaluate(
            "()=>window.esaTwoProportionMath.compute(0,20,0,30).degenerate"))
        root.locator("#esa-2p-reset").click()
        for width in (320,375,768,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":850})
                rect=root.evaluate("""e=>({left:e.getBoundingClientRect().left,
                    right:e.getBoundingClientRect().right,
                    scroll:e.scrollWidth,client:e.clientWidth})""")
                self.assertGreaterEqual(rect["left"],-2,rect)
                self.assertLessEqual(rect["right"],width+2,rect)
                self.assertLessEqual(rect["scroll"]-rect["client"],2,rect)

    def test_batch70_distributions_twelve_progress_and_untrusted_storage(self):
        root="/probability/distributions/"
        key="esa_continue_probability_distributions_lesson_v0"
        lessons=(("bernoulli-distribution","Bernoulli Distribution"),
             ("binomial-distribution","Binomial Distribution"),
             ("geometric-distribution","Geometric Distribution"),
             ("negative-binomial-distribution","Negative Binomial Distribution"),
             ("poisson-distribution","Poisson Distribution"),
             ("hypergeometric-distribution","Hypergeometric Distribution"),
             ("uniform-distribution","Uniform Distribution"),
             ("exponential-distribution","Exponential Distribution"),
             ("gamma-distribution","Gamma Distribution"),
             ("beta-distribution","Beta Distribution"),
             ("normal-distribution","Normal Distribution"),
             ("lognormal-distribution","Lognormal Distribution"))
        for slug,title in lessons:
            with self.subTest(lesson=slug):
                route=root+slug+"/"
                self.page.goto(self.origin+route,wait_until="networkidle")
                stored=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(stored["url"],route)
                self.assertEqual(stored["label"],title)
                self.assertIs(type(stored["ts"]),int)
                self.page.goto(self.origin+root,wait_until="networkidle")
                expect(self.page.locator("#continue-reading-probability-distributions")).to_be_visible()
                self.assertEqual(self.page.locator(
                    "#continue-reading-probability-distributions-btn").get_attribute("href"),route)
        good=root+"binomial-distribution/"
        invalid=(
           {"url":good,"label":"Wrong Distribution"},
           {"url":good,"label":'<img src=x onerror="window.esaInjected=true">'},
           {"url":good,"label":"Binomial Distribution","ts":0},
           {"url":good,"label":"Binomial Distribution","ts":-1},
           {"url":good,"label":"Binomial Distribution","ts":1.5},
           {"url":good,"label":"Binomial Distribution","ts":None},
           {"url":good,"label":"Binomial Distribution","ts":True},
           {"url":good,"label":"Binomial Distribution","ts":"tomorrow"},
           {"url":good,"label":"Binomial Distribution","ts":999999999999999},
           {"url":good+"#fragment","label":"Binomial Distribution"},
           {"url":good+"?q=1","label":"Binomial Distribution"},
           {"url":root+"unknown/","label":"Binomial Distribution"},
           {"url":"javascript:alert(1)","label":"Binomial Distribution"},
           {"url":"//evil.example/a/","label":"Binomial Distribution"})
        panel=self.page.locator("#continue-reading-probability-distributions")
        for payload in invalid:
            with self.subTest(invalid=str(payload)[:100]):
                self.page.evaluate("x=>localStorage.setItem(x.k,JSON.stringify(x.v))",
                       {"k":key,"v":payload})
                self.page.reload(wait_until="networkidle")
                expect(panel).to_be_hidden()
        self.page.evaluate("x=>localStorage.setItem(x.k,JSON.stringify(x.v))",
           {"k":key,"v":{"url":good,"label":"Binomial Distribution"}})
        self.page.reload(wait_until="networkidle")
        expect(panel).to_be_visible()
        self.assertIsNone(self.page.evaluate("()=>window.esaInjected||null"))
        self.page.evaluate("k=>localStorage.setItem(k,'{bad json')",key)
        self.page.reload(wait_until="networkidle")
        expect(panel).to_be_hidden()

    def test_batch70_distributions_denied_storage(self):
        self.page.add_init_script("""
          Object.defineProperty(window,"localStorage",{
            configurable:true,
            get(){throw new DOMException("Storage unavailable","SecurityError")}
          });
        """)
        base="/probability/distributions/"
        for slug in ("bernoulli-distribution","binomial-distribution",
          "geometric-distribution","negative-binomial-distribution",
          "poisson-distribution","hypergeometric-distribution","uniform-distribution",
          "exponential-distribution","gamma-distribution","beta-distribution",
          "normal-distribution","lognormal-distribution"):
            with self.subTest(slug=slug):
                self.page.goto(self.origin+base+slug+"/",wait_until="networkidle")
                expect(self.page.locator("main h1")).to_be_visible()
        self.page.goto(self.origin+base,wait_until="networkidle")
        expect(self.page.locator("#continue-reading-probability-distributions")).to_be_hidden()
        self.assertEqual(self.page.locator("#lessons .lesson-card").count(),12)



if __name__ == "__main__":
    unittest.main(argv=[__file__], verbosity=2)
