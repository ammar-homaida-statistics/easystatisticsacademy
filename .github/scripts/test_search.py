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
        self.assertEqual(self.page.evaluate("window.MathJax.tex.inlineMath[0][0]"), "$")
        self.assertEqual(self.page.evaluate("window.MathJax.tex.displayMath[1][0]"), r"\[")
        self.assertEqual(self.page.evaluate("window.MathJax.tex.displayMath[1][1]"), r"\]")
        # The CDN is stubbed by this test suite, so these tests validate
        # loader selection and configuration, not live MathJax typesetting.

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
