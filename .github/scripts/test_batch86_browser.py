"""Batch #86 dedicated Playwright tests: RTL Z, Wilson, secure resume, ANOVA mobile."""
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
    def log_message(self,*args):pass

class Browser86(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(("127.0.0.1",0),partial(Quiet,directory=str(args.site.resolve())))
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()
        cls.url="http://127.0.0.1:"+str(cls.server.server_port)
        cls.playwright=sync_playwright().start()
        cls.browser=cls.playwright.chromium.launch(headless=True)
    @classmethod
    def tearDownClass(cls):
        cls.browser.close();cls.playwright.stop()
        cls.server.shutdown();cls.server.server_close();cls.thread.join()
    def setUp(self):
        self.ctx=self.browser.new_context(viewport={"width":320,"height":780})
        self.ctx.route("https://**",lambda route:route.fulfill(status=200,body=""))
        self.page=self.ctx.new_page()
        self.errors=[]
        self.page.on("pageerror",lambda e:self.errors.append(str(e)))
    def tearDown(self):
        self.assertEqual(self.errors,[])
        self.ctx.close()
    def open(self,route):
        self.page.goto(self.url+route,wait_until="networkidle")

    def test_arabic_z_math_live_320_and_375(self):
        ar="/ar/inference/classical-tests/one-sample-z-test-for-mean/"
        en="/inference/classical-tests/one-sample-z-test-for-mean/"
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            for route,lang in ((ar,"ar"),(en,"en")):
                self.open(route)
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                self.assertEqual(self.page.locator("link[rel=canonical]").get_attribute("href"),"https://easystatisticsacademy.com"+route)
                for code,url in (("ar",ar),("en",en)):
                    self.assertEqual(self.page.locator('link[rel=alternate][hreflang="'+code+'"]').get_attribute("href"),"https://easystatisticsacademy.com"+url)
                structured=self.page.locator('script[type="application/ld+json"]').all_text_contents()
                self.assertTrue(any('"LearningResource"' in item for item in structured))
                if lang=="ar":self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl")
                lab=self.page.locator("#esa-one-mean-z-lab")
                expect(lab).to_be_visible()
                expect(lab.locator("#esa-omz-z")).to_have_text("-4.000000")
                expect(lab.locator("#esa-omz-pvalue")).to_have_text("0.000063")
                self.assertLessEqual(lab.evaluate("(e)=>e.getBoundingClientRect().right"),width+1)
                lab.locator("#esa-omz-sigma").fill("0")
                expect(lab.locator("#esa-omz-error")).to_be_visible()
                expect(lab.locator("#esa-omz-sigma")).to_have_attribute("aria-invalid","true")
                lab.locator("#esa-omz-reset").focus();self.page.keyboard.press("Enter")
                expect(lab.locator("#esa-omz-error")).to_be_hidden()
                expect(lab.locator("#esa-omz-sigma")).to_have_attribute("aria-invalid","false")
                lab.locator("#esa-omz-side").select_option("greater")
                expect(lab.locator("#esa-omz-pvalue")).to_have_text("0.999968")
                self.assertIn("Z=",lab.locator("#esa-omz-plot").get_attribute("aria-label"))

    def test_single_proportion_wald_wilson_extremes_mobile(self):
        route="/inference/confidence-intervals/ci-for-proportion/"
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            self.open(route)
            lab=self.page.locator("#esa-single-proportion-lab")
            expect(lab).to_be_visible()
            self.assertLessEqual(lab.evaluate("(e)=>e.getBoundingClientRect().right"),width+1)
            expect(lab.locator("#esa-sp-estimate")).to_have_text("62.0000")
            lab.locator("#esa-sp-x").fill("0")
            expect(lab.locator("#esa-sp-waldlo")).to_have_text("0.0000")
            expect(lab.locator("#esa-sp-waldhi")).to_have_text("0.0000")
            self.assertGreater(float(lab.locator("#esa-sp-wilsonhi").inner_text()),0)
            lab.locator("#esa-sp-x").fill("501")
            expect(lab.locator("#esa-sp-error")).to_be_visible()
            expect(lab.locator("#esa-sp-x")).to_have_attribute("aria-invalid","true")
            expect(lab.locator("#esa-sp-chart")).to_be_hidden()
            lab.locator("#esa-sp-reset").focus();self.page.keyboard.press("Enter")
            expect(lab.locator("#esa-sp-error")).to_be_hidden()
            expect(lab.locator("#esa-sp-x")).to_have_attribute("aria-invalid","false")
            self.assertIn("Wilson",lab.locator("#esa-sp-chart").get_attribute("aria-label"))

    def test_foundations_resume_injection_and_legacy_timestamp(self):
        route="/inference/foundations/"
        path=route+"what-is-statistical-inference/"
        key="esa_continue_inference_foundations_lesson_v0"
        self.open(route)
        panel=self.page.locator("#continue-reading-inference-foundations")
        def setprogress(value):
            self.page.evaluate("([k,v])=>localStorage.setItem(k,JSON.stringify(v))",[key,value])
            self.page.reload(wait_until="networkidle")
        title="What Is Statistical Inference?"
        setprogress({"url":path,"label":title})
        expect(panel).to_be_visible()
        setprogress({"url":path,"label":title,"ts":1730000000000})
        expect(panel).to_be_visible()
        for bad in ({"url":path,"label":"<img src=x onerror=alert(1)>"},
                    {"url":path,"label":"Forged heading"},
                    {"url":path+"?q=1","label":title},
                    {"url":"javascript:alert(1)","label":title},
                    {"url":path,"label":title,"ts":False},
                    {"url":path,"label":title,"ts":99999999999999999}):
            setprogress(bad);expect(panel).to_be_hidden()
        self.assertEqual(panel.locator("script,img").count(),0)

    def test_anova_invalid_recovery_and_zero_variation(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            self.open("/inference/classical-tests/one-way-anova-f-test/")
            lab=self.page.locator("#esa-anova-lab")
            self.assertLessEqual(lab.evaluate("(e)=>e.getBoundingClientRect().right"),width+1)
            expect(lab.locator("#esa-anova-f")).to_have_text("13.000000")
            lab.locator("#esa-anova-a").fill("invalid data")
            expect(lab.locator("#esa-anova-error")).to_be_visible()
            expect(lab.locator("#esa-anova-a")).to_have_attribute("aria-invalid","true")
            expect(lab.locator("#esa-anova-b")).to_have_attribute("aria-invalid","false")
            lab.locator("#esa-anova-reset").focus();self.page.keyboard.press("Enter")
            expect(lab.locator("#esa-anova-error")).to_be_hidden()
            expect(lab.locator("#esa-anova-a")).to_have_attribute("aria-invalid","false")
            lab.locator("#esa-anova-constant").click()
            expect(lab.locator("#esa-anova-f")).to_have_text("∞")
            expect(lab.locator("#esa-anova-p")).to_have_text("0.000000")

if __name__=="__main__":unittest.main(argv=[__file__],verbosity=2)
