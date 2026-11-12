"""Batch #90 Playwright: exact binomial, bilingual Z, secure Diagnostics, proportion and χ² accessibility."""
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
    def log_message(self,*unused):pass
class Browser90(unittest.TestCase):
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
        self.context=self.browser.new_context(viewport={"width":320,"height":780})
        self.context.route("https://**",lambda r:r.fulfill(status=200,body=""))
        self.page=self.context.new_page()
        self.errors=[]
        self.page.on("pageerror",lambda err:self.errors.append(str(err)))
    def tearDown(self):
        self.assertFalse(self.errors,self.errors)
        self.context.close()
    def visit(self,route):
        self.page.goto(self.origin+route,wait_until="networkidle")
    def fit(self,node,width):
        rect=node.evaluate("""e=>({
         left:e.getBoundingClientRect().left,
         right:e.getBoundingClientRect().right,
         scroll:e.scrollWidth,client:e.clientWidth})""")
        self.assertGreaterEqual(rect["left"],-2,rect)
        self.assertLessEqual(rect["right"],width+2,rect)
        self.assertLessEqual(rect["scroll"]-rect["client"],2,rect)
    def test_bilingual_z_parity_metadata_keyboard_and_mobile(self):
        en="/inference/classical-tests/one-proportion-z-test/"
        ar="/ar/inference/classical-tests/one-proportion-z-test/"
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            for route,lang in ((en,"en"),(ar,"ar")):
                with self.subTest(width=width,lang=lang):
                    self.visit(route)
                    expect(self.page.locator("html")).to_have_attribute("lang",lang)
                    if lang=="ar":expect(self.page.locator("html")).to_have_attribute("dir","rtl")
                    expect(self.page.locator('link[rel="canonical"]')).to_have_attribute(
                        "href","https://easystatisticsacademy.com"+route)
                    for locale,link in (("en",en),("ar",ar)):
                        expect(self.page.locator('link[rel="alternate"][hreflang="'+locale+'"]')).to_have_attribute(
                            "href","https://easystatisticsacademy.com"+link)
                    self.assertTrue(any("LearningResource" in txt for txt in
                      self.page.locator('script[type="application/ld+json"]').all_text_contents()))
                    lab=self.page.locator("#esa-one-proportion-lab")
                    self.fit(lab,width)
                    expect(lab.locator("#esa-op-z")).to_have_text("2.828427")
                    expect(lab.locator("#esa-op-pvalue")).to_have_text("0.004678")
                    expect(lab.locator("#esa-op-wilsonLower")).to_have_text("0.530837")
                    lab.locator("#esa-op-x").fill("201")
                    expect(lab.locator("#esa-op-error")).to_be_visible()
                    expect(lab.locator("#esa-op-x")).to_have_attribute("aria-invalid","true")
                    expect(lab.locator("#esa-op-results")).to_be_hidden()
                    lab.locator("#esa-op-reset").focus()
                    self.page.keyboard.press("Enter")
                    expect(lab.locator("#esa-op-error")).to_be_hidden()
                    expect(lab.locator("#esa-op-x")).to_have_attribute("aria-invalid","false")
                    expect(lab.locator("#esa-op-z")).to_have_text("2.828427")
                    lab.locator("#esa-op-alternative").select_option("less")
                    self.assertAlmostEqual(float(lab.locator("#esa-op-pvalue").inner_text()),
                                           1-.00467786/2,delta=2e-6)
    def test_exact_comparator_tails_discrepancies_and_mobile(self):
        route="/inference/classical-tests/exact-binomial-vs-z-test/"
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            self.visit(route)
            lab=self.page.locator("#esa-exact-binomial-lab")
            self.fit(lab,width)
            expect(lab.locator("#esa-eb-exact")).to_have_text("0.109375")
            self.assertTrue(float(lab.locator("#esa-eb-approx").inner_text())>0.01)
            expect(lab.locator("#esa-eb-warning")).to_contain_text("below 10")
            lab.locator("#esa-eb-side").select_option("greater")
            expect(lab.locator("#esa-eb-exact")).to_have_text("0.989258")
            lab.locator("#esa-eb-side").select_option("less")
            expect(lab.locator("#esa-eb-exact")).to_have_text("0.054688")
            lab.locator("#esa-eb-n").fill("2001")
            expect(lab.locator("#esa-eb-error")).to_be_visible()
            expect(lab.locator("#esa-eb-n")).to_have_attribute("aria-invalid","true")
            expect(lab.locator("#esa-eb-results")).to_be_hidden()
            lab.locator("#esa-eb-reset").focus();self.page.keyboard.press("Enter")
            expect(lab.locator("#esa-eb-exact")).to_have_text("0.109375")
            expect(lab.locator("#esa-eb-n")).to_have_attribute("aria-invalid","false")
            self.assertIn("Exact binomial",lab.locator("#esa-eb-plot").get_attribute("aria-label"))
    def test_diagnostics_progress_security_all_writers(self):
        root="/modeling/diagnostics/"
        key="esa_continue_modeling_diagnostics_lesson_v0"
        for slug in ("residuals","residual-plots","nonlinearity","heteroscedasticity",
                     "outliers","leverage","influence","cooks-distance","diagnostic-workflow"):
            with self.subTest(slug=slug):
                self.visit(root+slug+"/")
                stored=self.page.evaluate("k=>JSON.parse(localStorage.getItem(k))",key)
                self.assertEqual(stored["url"],root+slug+"/")
                self.visit(root)
                expect(self.page.locator("#continue-reading-modeling-diagnostics")).to_be_visible()
                expect(self.page.locator("#continue-reading-modeling-diagnostics-btn")).to_have_attribute("href",stored["url"])
        valid={"url":root+"residuals/","label":"Residuals"}
        for bad in (
          {"url":"javascript:alert(1)","label":"Residuals"},
          {"url":root+"residuals/?x=1","label":"Residuals"},
          {"url":root+"residuals/","label":"<img src=x onerror=alert(1)>"},
          {**valid,"ts":-2},{**valid,"ts":1.5},{**valid,"ts":True},
          {**valid,"ts":9999999999999},
        ):
            with self.subTest(bad=str(bad)):
                self.page.evaluate("([k,v])=>localStorage.setItem(k,JSON.stringify(v))",[key,bad])
                self.page.reload(wait_until="networkidle")
                expect(self.page.locator("#continue-reading-modeling-diagnostics")).to_be_hidden()
        self.page.evaluate("([k,v])=>localStorage.setItem(k,JSON.stringify(v))",[key,{**valid,"ts":1700000000000}])
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-modeling-diagnostics")).to_be_visible()
        self.page.evaluate("k=>localStorage.setItem(k,'{bad json')",key)
        self.page.reload(wait_until="networkidle")
        expect(self.page.locator("#continue-reading-modeling-diagnostics")).to_be_hidden()
    def test_two_proportion_and_chi_square_mobile_aria_numeric(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            self.visit("/inference/classical-tests/two-proportion-z-test/")
            lab=self.page.locator("#esa-two-proportion-lab")
            self.fit(lab,width)
            self.assertAlmostEqual(float(lab.locator("#esa-2p-z").inner_text()),
                                   .15/(.525*.475*(1/200+1/200))**.5,delta=1e-5)
            lab.locator("#esa-2p-n1").fill("0")
            expect(lab.locator("#esa-2p-error")).to_be_visible()
            expect(lab.locator("#esa-2p-n1")).to_have_attribute("aria-invalid","true")
            lab.locator("#esa-2p-reset").focus();self.page.keyboard.press("Enter")
            expect(lab.locator("#esa-2p-n1")).to_have_attribute("aria-invalid","false")
            self.visit("/inference/classical-tests/chi-square-independence-test/")
            chi=self.page.locator("#esa-chi-independence-lab")
            self.fit(chi,width)
            expect(chi.locator("#esa-chi-stat")).to_have_text("18.181818")
            chi.locator("#esa-chi-a").fill("-1")
            expect(chi.locator("#esa-chi-error")).to_be_visible()
            expect(chi.locator("#esa-chi-a")).to_have_attribute("aria-invalid","true")
            chi.locator("#esa-chi-reset").focus();self.page.keyboard.press("Enter")
            expect(chi.locator("#esa-chi-a")).to_have_attribute("aria-invalid","false")

if __name__=="__main__":
    unittest.main()
