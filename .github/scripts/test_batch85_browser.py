"""Batch 85 browser tests against generated Jekyll site, Playwright Chromium."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
import unittest
from playwright.sync_api import sync_playwright, expect

parser=argparse.ArgumentParser()
parser.add_argument("--site",type=Path,default=Path("_site"))
opts=parser.parse_args()
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args): pass

class Browser85(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(("127.0.0.1",0),partial(Quiet,directory=str(opts.site.resolve())))
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()
        cls.base="http://127.0.0.1:"+str(cls.server.server_port)
        cls.playwright=sync_playwright().start()
        cls.browser=cls.playwright.chromium.launch(headless=True)
    @classmethod
    def tearDownClass(cls):
        cls.browser.close();cls.playwright.stop();cls.server.shutdown();cls.server.server_close();cls.thread.join()
    def setUp(self):
        self.context=self.browser.new_context(viewport={"width":320,"height":780})
        self.context.route("https://**",lambda route:route.fulfill(status=200,body=""))
        self.page=self.context.new_page()
        self.errors=[]
        self.page.on("pageerror",lambda err:self.errors.append(str(err)))
    def tearDown(self):
        self.assertEqual(self.errors,[])
        self.context.close()
    def goto(self,route):
        self.page.goto(self.base+route,wait_until="networkidle")

    def test_bilingual_arabic_and_metadata_mobile(self):
        ar="/ar/inference/classical-tests/decision-framework-and-assumptions/"
        en="/inference/classical-tests/decision-framework-and-assumptions/"
        for route,lang in [(ar,"ar"),(en,"en")]:
            self.goto(route)
            self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
            if lang=="ar": self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl")
            self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),
                             "https://easystatisticsacademy.com"+route)
            for code,url in [("ar",ar),("en",en)]:
                self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+code+'"]').get_attribute("href"),
                                 "https://easystatisticsacademy.com"+url)
            structured=self.page.locator('script[type="application/ld+json"]').all_text_contents()
            self.assertTrue(any('"LearningResource"' in content for content in structured))
        self.goto(ar)
        expect(self.page.get_by_role("heading",name="إطار اتخاذ القرار والافتراضات في الاختبارات الإحصائية")).to_be_visible()
        self.assertLessEqual(self.page.locator("html").evaluate("(e)=>e.scrollWidth"),322)

    def test_newcombe_coverage_and_inputs_at_320_and_375(self):
        route="/inference/confidence-intervals/ci-for-difference-of-proportions/"
        for width in [320,375]:
            self.page.set_viewport_size({"width":width,"height":800})
            self.goto(route)
            panel=self.page.locator("#esa-prop-newcombe-panel")
            expect(panel).to_be_visible()
            self.assertLessEqual(panel.evaluate("(e)=>e.getBoundingClientRect().right"),width+1)
            self.assertLessEqual(float(panel.locator("#esa-prop-newcombe-lower").inner_text()),float(panel.locator("#esa-prop-newcombe-upper").inner_text()))
            chart=panel.locator("#esa-prop-compare-chart")
            self.assertIn("Newcombe",chart.get_attribute("aria-label"))
            count=self.page.locator("#esa-prop-x1")
            count.fill("0")
            expect(panel.locator("#esa-prop-newcombe-results")).to_be_visible()
            count.fill("601")
            expect(panel.locator("#esa-prop-newcombe-error")).to_be_visible()
            expect(count).to_have_attribute("aria-invalid","true")
            self.assertEqual(panel.locator("#esa-prop-compare-chart line").count(),0)
            count.fill("240")
            expect(panel.locator("#esa-prop-newcombe-error")).to_be_hidden()
            expect(count).to_have_attribute("aria-invalid","false")
            self.page.locator("#esa-prop-reset").focus()
            self.page.keyboard.press("Enter")
            expect(panel.locator("#esa-prop-newcombe-level")).to_have_text("95")
            expect(panel.locator("#esa-prop-newcombe-results")).to_be_visible()

    def test_confidence_progress_forged_label_and_timestamp(self):
        route="/inference/confidence-intervals/"
        url=route+"what-is-a-confidence-interval/"
        title="What Is a Confidence Interval?"
        key="esa_continue_inference_confidence_intervals_lesson_v0"
        self.goto(route)
        container=self.page.locator("#continue-reading-inference-ci")
        def save(entry):
            self.page.evaluate("([k,v])=>localStorage.setItem(k,JSON.stringify(v))",[key,entry])
            self.page.reload(wait_until="networkidle")
        save({"url":url,"label":title,"ts":1730000000000})
        expect(container).to_be_visible()
        for bad in [
            {"url":url,"label":"<img src=x onerror=alert(1)>"},
            {"url":url,"label":"Different lesson"},
            {"url":url+"?test=1","label":title},
            {"url":"javascript:alert(1)","label":title},
            {"url":url,"label":title,"ts":9999999999999999},
            {"url":url,"label":title,"ts":False},
        ]:
            save(bad)
            expect(container).to_be_hidden()
        self.assertEqual(container.locator("img,script").count(),0)

    def test_homogeneity_invalid_recovery_and_sparse_warning(self):
        self.goto("/inference/classical-tests/chi-square-homogeneity-test/")
        text=self.page.locator("#esa-hom-input")
        text.fill("0,0\n10,20")
        expect(self.page.locator("#esa-hom-error")).to_be_visible()
        expect(text).to_have_attribute("aria-invalid","true")
        text.fill("0,10\n8,12")
        expect(self.page.locator("#esa-hom-error")).to_be_hidden()
        expect(text).to_have_attribute("aria-invalid","false")
        self.assertIn("below 5",self.page.locator("#esa-hom-warning").inner_text())
        expect(self.page.locator("#esa-hom-chart")).to_have_attribute("role","img")

if __name__=="__main__":unittest.main(argv=[__file__],verbosity=2)
