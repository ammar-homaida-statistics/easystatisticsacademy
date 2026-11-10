"""Batch #87 generated-site Playwright tests for RTL t, effect sizes, Center security and GOF."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
import threading
import unittest
from playwright.sync_api import sync_playwright,expect

p=argparse.ArgumentParser()
p.add_argument("--site",type=Path,default=Path("_site"))
opts=p.parse_args()
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
class Batch87Browser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server=ThreadingHTTPServer(("127.0.0.1",0),partial(Quiet,directory=str(opts.site.resolve())))
        cls.thread=threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start();cls.url="http://127.0.0.1:"+str(cls.server.server_port)
        cls.playwright=sync_playwright().start()
        cls.browser=cls.playwright.chromium.launch(headless=True)
    @classmethod
    def tearDownClass(cls):
        cls.browser.close();cls.playwright.stop()
        cls.server.shutdown();cls.server.server_close();cls.thread.join()
    def setUp(self):
        self.context=self.browser.new_context(viewport={"width":320,"height":780})
        self.context.route("https://**",lambda route:route.fulfill(status=200,body=""))
        self.page=self.context.new_page();self.errors=[]
        self.page.on("pageerror",lambda e:self.errors.append(str(e)))
    def tearDown(self):
        self.assertEqual(self.errors,[])
        self.context.close()
    def go(self,path):self.page.goto(self.url+path,wait_until="networkidle")
    def test_arabic_student_t_and_reciprocal_metadata(self):
        ar="/ar/inference/classical-tests/one-sample-t-test-for-mean/"
        en="/inference/classical-tests/one-sample-t-test-for-mean/"
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            for path,lang in ((ar,"ar"),(en,"en")):
                self.go(path)
                self.assertEqual(self.page.locator("html").get_attribute("lang"),lang)
                if lang=="ar":self.assertEqual(self.page.locator("html").get_attribute("dir"),"rtl")
                self.assertEqual(self.page.locator('link[rel="canonical"]').get_attribute("href"),"https://easystatisticsacademy.com"+path)
                for code,href in (("ar",ar),("en",en)):
                    self.assertEqual(self.page.locator('link[rel="alternate"][hreflang="'+code+'"]').get_attribute("href"),"https://easystatisticsacademy.com"+href)
                self.assertTrue(any('"LearningResource"' in s for s in self.page.locator('script[type="application/ld+json"]').all_text_contents()))
                root=self.page.locator("#esa-student-t-lab")
                expect(root).to_be_visible()
                self.assertLessEqual(root.evaluate("(e)=>e.getBoundingClientRect().right"),width+1)
                expect(root.locator("#esa-st-df")).to_have_text("9")
                expect(root.locator("#esa-st-t")).to_have_text("2.108185")
                root.locator("#esa-st-sd").fill("0")
                expect(root.locator("#esa-st-error")).to_be_visible()
                expect(root.locator("#esa-st-sd")).to_have_attribute("aria-invalid","true")
                root.locator("#esa-st-reset").focus();self.page.keyboard.press("Enter")
                expect(root.locator("#esa-st-sd")).to_have_attribute("aria-invalid","false")
                expect(root.locator("#esa-st-error")).to_be_hidden()
                root.locator("#esa-st-alternative").select_option("less")
                expect(root.locator("#esa-st-results")).to_be_visible()
    def test_practical_thresholds_and_validation_mobile(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            self.go("/inference/hypothesis-testing/practical-significance/")
            lab=self.page.locator("#esa-practical-significance-lab")
            expect(lab).to_be_visible()
            self.assertLessEqual(lab.evaluate("(e)=>e.getBoundingClientRect().right"),width+1)
            expect(lab.locator("#esa-ps-effect")).to_have_text("0.200000")
            expect(lab.locator("#esa-ps-d")).to_have_text("0.200000")
            expect(lab.locator("#esa-ps-statistical")).to_contain_text("Statistically significant")
            expect(lab.locator("#esa-ps-practical")).to_contain_text("below")
            lab.locator("#esa-ps-threshold").fill("-1")
            expect(lab.locator("#esa-ps-error")).to_be_visible()
            expect(lab.locator("#esa-ps-threshold")).to_have_attribute("aria-invalid","true")
            lab.locator("#esa-ps-reset").focus();self.page.keyboard.press("Enter")
            expect(lab.locator("#esa-ps-error")).to_be_hidden()
            expect(lab.locator("#esa-ps-threshold")).to_have_attribute("aria-invalid","false")
            self.assertIn("95%",lab.locator("#esa-ps-graph").get_attribute("aria-label"))
    def test_center_progress_attacks_and_valid_legacy(self):
        route="/descriptive/center/";key="esa_continue_descriptive_center_lesson_v0"
        url=route+"median/";label="Median"
        self.go(route)
        panel=self.page.locator("#continue-reading-block4")
        def save(data):
            self.page.evaluate("([k,obj])=>localStorage.setItem(k,JSON.stringify(obj))",[key,data])
            self.page.reload(wait_until="networkidle")
        save({"url":url,"label":label})
        expect(panel).to_be_visible()
        save({"url":url,"label":label,"ts":1730000000000})
        expect(panel).to_be_visible()
        for entry in ({"url":url,"label":"<img src=x onerror=alert(1)>"},
                      {"url":url,"label":"Forged heading"},
                      {"url":url+"?next=evil","label":label},
                      {"url":"javascript:alert(1)","label":label},
                      {"url":url,"label":label,"ts":False},
                      {"url":url,"label":label,"ts":9999999999999999}):
            save(entry);expect(panel).to_be_hidden()
        self.assertEqual(panel.locator("script,img").count(),0)
    def test_gof_expected_counts_sparse_and_invalid_recovery(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":800})
            self.go("/inference/classical-tests/chi-square-goodness-of-fit/")
            lab=self.page.locator("#esa-gof-explorer")
            self.assertLessEqual(lab.evaluate("(e)=>e.getBoundingClientRect().right"),width+1)
            expect(lab.locator("#esa-gof-df")).to_have_text("5")
            lab.locator("#esa-gof-probs").fill("0.2,0.2")
            expect(lab.locator("#esa-gof-error")).to_be_visible()
            expect(lab.locator("#esa-gof-probs")).to_have_attribute("aria-invalid","true")
            lab.locator("#esa-gof-uneven").click()
            expect(lab.locator("#esa-gof-error")).to_be_hidden()
            expect(lab.locator("#esa-gof-probs")).to_have_attribute("aria-invalid","false")
            lab.locator("#esa-gof-counts").fill("1,0,0")
            self.assertIn("below 5",lab.locator("#esa-gof-warning").inner_text())
            expect(lab.locator("#esa-gof-chart")).to_have_attribute("role","img")

if __name__=="__main__":unittest.main(argv=[__file__],verbosity=2)
