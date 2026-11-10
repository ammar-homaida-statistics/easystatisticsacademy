"""Batch #88 generated-site Playwright: paired Arabic, Welch/pooled, Shape progress, mobile accessibility."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import threading
import unittest
from playwright.sync_api import sync_playwright,expect
p=argparse.ArgumentParser()
p.add_argument("--site",type=Path,default=Path("_site"))
cfg=p.parse_args()
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
class Browser88(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(("127.0.0.1",0),partial(Quiet,directory=str(cfg.site.resolve())))
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True);cls.thread.start()
        cls.url="http://127.0.0.1:"+str(cls.server.server_port)
        cls.playwright=sync_playwright().start();cls.browser=cls.playwright.chromium.launch(headless=True)
    @classmethod
    def tearDownClass(cls):
        cls.browser.close();cls.playwright.stop()
        cls.server.shutdown();cls.server.server_close();cls.thread.join()
    def setUp(self):
        self.ctx=self.browser.new_context(viewport={"width":320,"height":780})
        self.ctx.route("https://**",lambda route:route.fulfill(status=200,body=""))
        self.page=self.ctx.new_page();self.errors=[]
        self.page.on("pageerror",lambda e:self.errors.append(str(e)))
    def tearDown(self):
        self.assertFalse(self.errors,self.errors);self.ctx.close()
    def visit(self,path):self.page.goto(self.url+path,wait_until="networkidle")
    def test_paired_ar_en_mobile_reciprocal_and_keyboard(self):
        ar="/ar/inference/classical-tests/paired-t-test/"
        en="/inference/classical-tests/paired-t-test/"
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            for route,lang in ((ar,"ar"),(en,"en")):
                self.visit(route)
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                if lang=="ar":self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl")
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),"https://easystatisticsacademy.com"+route)
                for code,uri in (("ar",ar),("en",en)):
                    self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+code+'"]').get_attribute("href"),"https://easystatisticsacademy.com"+uri)
                self.assertTrue(any('"LearningResource"' in x for x in self.page.locator('script[type="application/ld+json"]').all_text_contents()))
                lab=self.page.locator("#esa-paired-t-lab")
                expect(lab).to_be_visible()
                self.assertLessEqual(lab.evaluate("(e)=>e.getBoundingClientRect().right"),width+1)
                expect(lab.locator("#esa-pt-n")).to_have_text("5")
                expect(lab.locator("#esa-pt-mean")).to_have_text("4.200000")
                expect(lab.locator("#esa-pt-p")).to_have_text("0.000359")
                lab.locator("#esa-pt-input").fill("70,75\n68")
                expect(lab.locator("#esa-pt-error")).to_be_visible()
                expect(lab.locator("#esa-pt-input")).to_have_attribute("aria-invalid","true")
                lab.locator("#esa-pt-reset").focus();self.page.keyboard.press("Enter")
                expect(lab.locator("#esa-pt-error")).to_be_hidden()
                expect(lab.locator("#esa-pt-input")).to_have_attribute("aria-invalid","false")
                lab.locator("#esa-pt-negative").focus();self.page.keyboard.press("Enter")
                expect(lab.locator("#esa-pt-mean")).to_have_text("-4.200000")
                expect(lab.locator("#esa-pt-p")).to_have_text("0.000359")
                lab.locator("#esa-pt-input").fill("1,2\n3,4")
                expect(lab.locator("#esa-pt-error")).to_be_visible()
                self.assertIn("plot",lab.locator("#esa-pt-plot").get_attribute("id"))
    def test_welch_pooled_interactive_mobile(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            self.visit("/inference/classical-tests/two-sample-t-test-independent/")
            lab=self.page.locator("#esa-welch-lab")
            expect(lab).to_be_visible()
            self.assertLessEqual(lab.evaluate("(e)=>e.getBoundingClientRect().right"),width+1)
            expect(lab.locator("#esa-w-df")).to_have_text("10.937907")
            expect(lab.locator("#esa-w-pool-df")).to_have_text("11.000000")
            expect(lab.locator("#esa-w-pool-t")).to_have_text("4.357746")
            expect(lab.locator("#esa-w-pool-p")).to_have_text("0.001141")
            self.assertIn("Welch",lab.locator("#esa-w-pool-plot").get_attribute("aria-label"))
            lab.locator("#esa-w-a").fill("1,2,3")
            lab.locator("#esa-w-b").fill("10,20,30,40,50")
            expect(lab.locator("#esa-w-pool-df")).to_have_text("6.000000")
            expect(lab.locator("#esa-w-pool-p")).to_have_text("0.025058")
            lab.locator("#esa-w-a").fill("1")
            expect(lab.locator("#esa-w-pool-results")).to_be_hidden()
            lab.locator("#esa-w-reset").focus();self.page.keyboard.press("Enter")
            expect(lab.locator("#esa-w-pool-results")).to_be_visible()
    def test_shape_secure_valid_and_malicious(self):
        route="/descriptive/shape/"
        key="esa_continue_descriptive_shape_lesson_v0"
        canonical=route+"why-shape-matters/"
        self.visit(route)
        panel=self.page.locator("#continue-reading-block6")
        def save(record):
            self.page.evaluate("([k,v])=>localStorage.setItem(k,JSON.stringify(v))",[key,record])
            self.page.reload(wait_until="networkidle")
        save({"url":canonical,"label":"Why Shape Matters"})
        expect(panel).to_be_visible()
        save({"url":canonical,"label":"Why Shape Matters","ts":1730000000000})
        expect(panel).to_be_visible()
        for invalid in ({"url":canonical,"label":"Why Distribution Shape Matters"},
                        {"url":canonical,"label":"<img src=x onerror=alert(1)>"},
                        {"url":"javascript:alert(1)","label":"Why Shape Matters"},
                        {"url":canonical+"?x=1","label":"Why Shape Matters"},
                        {"url":route+"normal-distribution-concept/","label":"The Normal Distribution (Conceptual)"},
                        {"url":canonical,"label":"Why Shape Matters","ts":False},
                        {"url":canonical,"label":"Why Shape Matters","ts":9999999999999999}):
            save(invalid);expect(panel).to_be_hidden()
        self.assertEqual(panel.locator("img,script").count(),0)

if __name__=="__main__":unittest.main(argv=[__file__],verbosity=2)
