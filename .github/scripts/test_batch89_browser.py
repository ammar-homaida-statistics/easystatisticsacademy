"""Batch #89 end-to-end browser checks: bilingual Welch/pooled, Monte Carlo and Reporting security."""
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
class Browser89(unittest.TestCase):
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
        self.errors=[];self.page.on("pageerror",lambda err:self.errors.append(str(err)))
    def tearDown(self):
        self.assertFalse(self.errors,self.errors)
        self.ctx.close()
    def visit(self,path):
        self.page.goto(self.origin+path,wait_until="networkidle")
    def assert_no_overflow(self,locator,width):
        bounds=locator.evaluate("""el=>({
            left:el.getBoundingClientRect().left,right:el.getBoundingClientRect().right,
            width:el.clientWidth,scroll:el.scrollWidth})""")
        self.assertGreaterEqual(bounds["left"],-2,bounds)
        self.assertLessEqual(bounds["right"],width+2,bounds)
        self.assertLessEqual(bounds["scroll"]-bounds["width"],2,bounds)
    def test_independent_t_ar_en_math_rtl_mobile(self):
        ar="/ar/inference/classical-tests/two-sample-t-test-independent/"
        en="/inference/classical-tests/two-sample-t-test-independent/"
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            for route,lang in ((ar,"ar"),(en,"en")):
                with self.subTest(width=width,language=lang):
                    self.visit(route)
                    self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                    if lang=="ar":self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl")
                    expect(self.page.locator('link[rel="canonical"]')).to_have_attribute(
                        "href","https://easystatisticsacademy.com"+route)
                    for locale,url in (("ar",ar),("en",en)):
                        expect(self.page.locator('link[rel="alternate"][hreflang="'+locale+'"]')).to_have_attribute(
                            "href","https://easystatisticsacademy.com"+url)
                    self.assertTrue(any("LearningResource" in t for t in
                      self.page.locator('script[type="application/ld+json"]').all_text_contents()))
                    lab=self.page.locator("#esa-welch-lab")
                    expect(lab).to_be_visible()
                    self.assert_no_overflow(lab,width)
                    expect(lab.locator("#esa-w-t")).to_have_text("4.446190")
                    expect(lab.locator("#esa-w-df")).to_have_text("10.937907")
                    expect(lab.locator("#esa-w-p")).to_have_text("0.000999")
                    expect(lab.locator("#esa-w-pool-t")).to_have_text("4.357746")
                    expect(lab.locator("#esa-w-pool-df")).to_have_text("11.000000")
                    expect(lab.locator("#esa-w-pool-p")).to_have_text("0.001141")
                    lab.locator("#esa-w-a").fill("1")
                    expect(lab.locator("#esa-w-error")).to_be_visible()
                    expect(lab.locator("#esa-w-a")).to_have_attribute("aria-invalid","true")
                    expect(lab.locator("#esa-w-pool-results")).to_be_hidden()
                    lab.locator("#esa-w-reset").focus();self.page.keyboard.press("Enter")
                    expect(lab.locator("#esa-w-error")).to_be_hidden()
                    expect(lab.locator("#esa-w-a")).to_have_attribute("aria-invalid","false")
                    lab.locator("#esa-w-reverse").focus();self.page.keyboard.press("Enter")
                    expect(lab.locator("#esa-w-difference")).to_have_text("-7.833333")
                    expect(lab.locator("#esa-w-pool-p")).to_have_text("0.001141")
                    lab.locator("#esa-w-a").fill("1, 1")
                    lab.locator("#esa-w-b").fill("2, 2")
                    expect(lab.locator("#esa-w-error")).to_be_visible()
    def test_seeded_simulator_reproducible_and_mobile(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            self.visit("/inference/classical-tests/welch-pooled-monte-carlo/")
            lab=self.page.locator("#esa-t89-simulation")
            expect(lab).to_be_visible()
            self.assert_no_overflow(lab,width)
            expect(lab.locator("#esa-sim-nullWelch")).to_contain_text("5.67%")
            expect(lab.locator("#esa-sim-nullPooled")).to_contain_text("1.67%")
            expect(lab.locator("#esa-sim-altWelch")).to_contain_text("48.33%")
            expect(lab.locator("#esa-sim-altPooled")).to_contain_text("24.33%")
            lab.locator("#esa-sim-n1").fill("10")
            lab.locator("#esa-sim-n2").fill("10")
            lab.locator("#esa-sim-sd1").fill("1")
            lab.locator("#esa-sim-sd2").fill("1")
            lab.locator("#esa-sim-effect").fill("0")
            lab.locator("#esa-sim-reps").fill("100")
            lab.locator("#esa-sim-seed").fill("5")
            lab.locator("#esa-sim-run").focus();self.page.keyboard.press("Enter")
            for key in ("nullWelch","nullPooled","altWelch","altPooled"):
                expect(lab.locator("#esa-sim-"+key)).to_contain_text("4.00%")
            before=lab.locator("#esa-sim-nullWelch").inner_text()
            lab.locator("#esa-sim-run").click()
            self.assertEqual(before,lab.locator("#esa-sim-nullWelch").inner_text())
            lab.locator("#esa-sim-reps").fill("50000")
            lab.locator("#esa-sim-run").click()
            expect(lab.locator("#esa-sim-results")).to_be_hidden()
            expect(lab.locator("#esa-sim-reps")).to_have_attribute("aria-invalid","true")
            lab.locator("#esa-sim-reset").focus();self.page.keyboard.press("Enter")
            expect(lab.locator("#esa-sim-results")).to_be_visible()
            expect(lab.locator("#esa-sim-reps")).to_have_attribute("aria-invalid","false")
    def test_reporting_progress_exact_titles_and_safety(self):
        key="esa_continue_descriptive_reporting_lesson_v0"
        path="/descriptive/reporting/"
        self.visit(path)
        panel=self.page.locator("#continue-reading-block7")
        def save(v):
            self.page.evaluate("([k,record])=>localStorage.setItem(k,JSON.stringify(record))",[key,v])
            self.page.reload(wait_until="networkidle")
        valid={"url":path+"from-numbers-to-message/","label":"From Numbers to Message"}
        save(valid);expect(panel).to_be_visible()
        save({**valid,"ts":1730000000000});expect(panel).to_be_visible()
        for record in ({**valid,"label":"<img src=x onerror=alert(1)>"},
                       {**valid,"label":"Forged title"},
                       {**valid,"url":path+"other-lesson/"},
                       {**valid,"url":valid["url"]+"?x=1"},
                       {**valid,"ts":True},
                       {**valid,"ts":9999999999999999}):
            save(record)
            expect(panel).to_be_hidden()
        self.assertEqual(panel.locator("img,script").count(),0)
        self.visit(path+"comparing-groups-responsibly/")
        self.visit(path)
        expect(panel).to_be_visible()
        expect(self.page.locator("#continue-reading-block7-label strong")).to_have_text(
            "Lesson 6 — Comparing Groups Responsibly")

if __name__=="__main__":unittest.main(argv=[__file__],verbosity=2)
