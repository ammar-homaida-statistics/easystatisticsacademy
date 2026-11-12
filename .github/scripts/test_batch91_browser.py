"""Batch #91 browser: bilingual two-proportion Z, Fisher–Pearson, secure progress, mobile QA."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import threading
import unittest
from playwright.sync_api import sync_playwright,expect
parser=argparse.ArgumentParser()
parser.add_argument("--site",type=Path,default=Path("_site"))
args=parser.parse_args()
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*a):pass
class Browser91(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(("127.0.0.1",0),partial(Quiet,directory=str(args.site.resolve())))
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.origin="http://127.0.0.1:"+str(cls.server.server_port)
        cls.pw=sync_playwright().start()
        cls.browser=cls.pw.chromium.launch(headless=True)
    @classmethod
    def tearDownClass(cls):
        cls.browser.close();cls.pw.stop();cls.server.shutdown();cls.server.server_close();cls.thread.join()
    def setUp(self):
        self.ctx=self.browser.new_context(viewport={"width":320,"height":780})
        self.ctx.route("https://**",lambda route:route.fulfill(status=200,body=""))
        self.page=self.ctx.new_page()
        self.errors=[]
        self.page.on("pageerror",lambda e:self.errors.append(str(e)))
    def tearDown(self):
        self.assertFalse(self.errors,self.errors)
        self.ctx.close()
    def visit(self,path):
        self.page.goto(self.origin+path,wait_until="networkidle")
    def fit(self,lab,width):
        rect=lab.evaluate("""e=>({
          left:e.getBoundingClientRect().left,right:e.getBoundingClientRect().right,
          scroll:e.scrollWidth,client:e.clientWidth})""")
        self.assertGreaterEqual(rect["left"],-2,rect)
        self.assertLessEqual(rect["right"],width+2,rect)
        self.assertLessEqual(rect["scroll"]-rect["client"],2,rect)
    def test_two_proportion_arabic_english_parity_mobile(self):
        en="/inference/classical-tests/two-proportion-z-test/"
        ar="/ar/inference/classical-tests/two-proportion-z-test/"
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            for route,lang in ((en,"en"),(ar,"ar")):
                with self.subTest(width=width,lang=lang):
                    self.visit(route)
                    expect(self.page.locator("html")).to_have_attribute("lang",lang)
                    if lang=="ar":expect(self.page.locator("html")).to_have_attribute("dir","rtl")
                    expect(self.page.locator('link[rel="canonical"]')).to_have_attribute(
                        "href","https://easystatisticsacademy.com"+route)
                    for locale,destination in (("ar",ar),("en",en)):
                        expect(self.page.locator('link[rel="alternate"][hreflang="'+locale+'"]')).to_have_attribute(
                            "href","https://easystatisticsacademy.com"+destination)
                    self.assertTrue(any("LearningResource" in v for v in
                       self.page.locator('script[type="application/ld+json"]').all_text_contents()))
                    lab=self.page.locator("#esa-two-proportion-lab")
                    self.fit(lab,width)
                    expect(lab.locator("#esa-2p-p1")).to_have_text("0.600000")
                    expect(lab.locator("#esa-2p-p2")).to_have_text("0.450000")
                    expect(lab.locator("#esa-2p-pooled")).to_have_text("0.525000")
                    lab.locator("#esa-2p-n1").fill("0")
                    expect(lab.locator("#esa-2p-error")).to_be_visible()
                    expect(lab.locator("#esa-2p-n1")).to_have_attribute("aria-invalid","true")
                    lab.locator("#esa-2p-reset").focus();self.page.keyboard.press("Enter")
                    expect(lab.locator("#esa-2p-error")).to_be_hidden()
                    expect(lab.locator("#esa-2p-n1")).to_have_attribute("aria-invalid","false")
                    lab.locator("#esa-2p-swap").focus();self.page.keyboard.press("Enter")
                    expect(lab.locator("#esa-2p-diff")).to_have_text("-0.150000")
                    if lang=="ar":self.assertIn("فرق النسبتين",lab.locator("#esa-2p-plot").get_attribute("aria-label"))
    def test_fisher_scipy_reference_and_invalid_margins_mobile(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            self.visit("/inference/classical-tests/fisher-exact-vs-chi-square/")
            lab=self.page.locator("#esa-fisher-chi-lab")
            self.fit(lab,width)
            expect(lab.locator("#esa-fc-fisher")).to_have_text("0.002759")
            expect(lab.locator("#esa-fc-chi")).to_have_text("10.971429")
            expect(lab.locator("#esa-fc-warning")).to_contain_text("below 5")
            lab.locator("#esa-fc-side").select_option("less")
            expect(lab.locator("#esa-fc-fisher")).to_have_text("0.001380")
            lab.locator("#esa-fc-side").select_option("greater")
            expect(lab.locator("#esa-fc-fisher")).to_have_text("0.999966")
            lab.locator("#esa-fc-a").fill("-1")
            expect(lab.locator("#esa-fc-error")).to_be_visible()
            expect(lab.locator("#esa-fc-a")).to_have_attribute("aria-invalid","true")
            expect(lab.locator("#esa-fc-results")).to_be_hidden()
            lab.locator("#esa-fc-reset").focus();self.page.keyboard.press("Enter")
            expect(lab.locator("#esa-fc-fisher")).to_have_text("0.002759")
            expect(lab.locator("#esa-fc-a")).to_have_attribute("aria-invalid","false")
            lab.locator("#esa-fc-a").fill("0")
            lab.locator("#esa-fc-b").fill("10")
            lab.locator("#esa-fc-c").fill("5")
            lab.locator("#esa-fc-d").fill("5")
            expect(lab.locator("#esa-fc-fisher")).to_have_text("0.032508")
    def test_multiple_regression_secure_current_legacy_progress(self):
        root="/modeling/multiple-regression/"
        key="esa_continue_modeling_multiple_regression_lesson_v0"
        old="esa_continue_modeling_mr_lesson_v0"
        self.visit(root+"multicollinearity/")
        stored=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
        self.assertEqual(stored["url"],root+"multicollinearity/")
        self.visit(root)
        pane=self.page.locator("#continue-reading-modeling-mr")
        expect(pane).to_be_visible()
        def save(value,legacy=False):
            self.page.evaluate("([k1,k2,v])=>{localStorage.removeItem(k1);localStorage.removeItem(k2);localStorage.setItem(k2,JSON.stringify(v));}" if legacy else
                "([k1,k2,v])=>{localStorage.removeItem(k1);localStorage.removeItem(k2);localStorage.setItem(k1,JSON.stringify(v));}",
                [key,old,value])
            self.page.reload(wait_until="networkidle")
        save(stored,legacy=True)
        expect(pane).to_be_visible()
        for invalid in ({**stored,"label":"<img src=x onerror=alert(1)>"},
                        {**stored,"url":"javascript:alert(1)"},
                        {**stored,"url":stored["url"]+"?bad"},
                        {**stored,"ts":9999999999999},
                        {**stored,"ts":-1},
                        {**stored,"ts":1.5},
                        {**stored,"ts":True}):
            save(invalid)
            expect(pane).to_be_hidden()
        self.page.evaluate("k=>localStorage.setItem(k,'{bad json')",key)
        self.page.reload(wait_until="networkidle")
        expect(pane).to_be_hidden()

if __name__=="__main__":unittest.main(argv=[__file__])
