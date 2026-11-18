"""Batch #95: kappa lab, Arabic McNemar parity, English and Arabic hub test
choosers, and generated no-JavaScript notices."""
import argparse
import threading
import unittest
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

ap=argparse.ArgumentParser()
ap.add_argument("--site",type=Path,default=Path("_site"))
args,_=ap.parse_known_args()
BASE="https://easystatisticsacademy.com"
KAPPA="/inference/classical-tests/cohens-kappa/"
EN_MCN="/inference/classical-tests/mcnemar-test/"
AR_MCN="/ar"+EN_MCN
EN_HUB="/inference/classical-tests/"
AR_HUB="/ar"+EN_HUB

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*a):pass

class Browser95(unittest.TestCase):
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
        self.ctx=self.browser.new_context(viewport={"width":320,"height":820})
        self.ctx.route("https://**",lambda route:route.fulfill(status=200,body=""))
        self.page=self.ctx.new_page();self.errors=[]
        self.page.on("pageerror",lambda e:self.errors.append(str(e)))
    def tearDown(self):
        self.assertFalse(self.errors,self.errors)
        self.ctx.close()
    def visit(self,route):
        self.page.goto(self.origin+route,wait_until="networkidle")
    def fit(self,selector,width):
        rect=self.page.locator(selector).evaluate("""e=>({left:e.getBoundingClientRect().left,right:e.getBoundingClientRect().right,scroll:e.scrollWidth,client:e.clientWidth})""")
        self.assertGreaterEqual(rect["left"],-2,rect)
        self.assertLessEqual(rect["right"],width+2,rect)
        self.assertLessEqual(rect["scroll"]-rect["client"],2,rect)

    def test_kappa_lab(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            self.visit(KAPPA)
            lab=self.page.locator("#esa-kappa-lab")
            self.fit("#esa-kappa-lab",width)
            expect(lab.locator("#esa-kappa-kappa")).to_have_text("0.4000")
            expect(lab.locator("#esa-kappa-kmax")).to_have_text("0.8000")
            expect(lab.locator("#esa-kappa-se")).to_have_text("0.1270")
            expect(lab.locator("#esa-kappa-ci")).to_have_text("[0.1511, 0.6489]")
            lab.locator("#esa-kappa-paradox").focus();self.page.keyboard.press("Enter")
            expect(lab.locator("#esa-kappa-po")).to_have_text("0.9000")
            expect(lab.locator("#esa-kappa-kappa")).to_have_text("0.4444")
            expect(lab.locator("#esa-kappa-note")).to_contain_text("chance agreement is also high")
            lab.locator("#esa-kappa-three").focus();self.page.keyboard.press("Space")
            expect(lab.locator("#esa-kappa-kappa")).to_have_text("0.7198")
            lab.locator("#esa-kappa-input").fill("5, 0\n0, 0")
            expect(lab.locator("#esa-kappa-kappa")).to_have_text("Undefined")
            expect(lab.locator("#esa-kappa-note")).to_contain_text("undefined")
            lab.locator("#esa-kappa-input").fill("1, 2\n3")
            expect(lab.locator("#esa-kappa-error")).to_be_visible()
            expect(lab.locator("#esa-kappa-input")).to_have_attribute("aria-invalid","true")
            lab.locator("#esa-kappa-example").click()
            expect(lab.locator("#esa-kappa-error")).to_be_hidden()

    def test_arabic_mcnemar_parity(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            for lang,route in (("en",EN_MCN),("ar",AR_MCN)):
                with self.subTest(width=width,lang=lang):
                    self.visit(route)
                    expect(self.page.locator("html")).to_have_attribute("lang",lang)
                    if lang=="ar":expect(self.page.locator("html")).to_have_attribute("dir","rtl")
                    for locale,path in (("en",EN_MCN),("ar",AR_MCN),("x-default",EN_MCN)):
                        expect(self.page.locator('link[rel="alternate"][hreflang="'+locale+'"]')).to_have_attribute("href",BASE+path)
                    self.fit("#esa-mcnemar-lab",width)
                    for out,val in (("exact","0.004077"),("p","0.002700"),("pcc","0.005110"),("chi","9.000000")):
                        expect(self.page.locator("#esa-mcn-"+out)).to_have_text(val)
                    self.page.locator("#esa-mcn-small").focus();self.page.keyboard.press("Enter")
                    expect(self.page.locator("#esa-mcn-advice")).to_contain_text("الدقيقة" if lang=="ar" else "exact binomial")
                    self.page.locator("#esa-mcn-b").fill("-1")
                    err=self.page.locator("#esa-mcn-error")
                    expect(err).to_be_visible()
                    self.assertIn("أدخل" if lang=="ar" else "Enter a whole-number",err.inner_text())

    def test_hub_choosers(self):
        for route,prefix in ((EN_HUB,""),(AR_HUB,"esa-ar-")):
            with self.subTest(route=route):
                self.visit(route)
                outcome=self.page.locator("#"+prefix+"test-outcome" if prefix else "#esa-test-outcome")
                design=self.page.locator("#"+prefix+"test-design" if prefix else "#esa-test-design")
                status=self.page.locator("#"+prefix+"test-result" if prefix else "#esa-test-result")
                outcome.select_option("binary");design.select_option("paired")
                link=status.get_by_role("link")
                expected=("/ar" if prefix else "")+"/inference/classical-tests/mcnemar-test/"
                expect(link).to_have_attribute("href",expected)
                outcome.select_option("binary");design.select_option("multiple")
                expect(status.get_by_role("link")).to_have_count(0)
                if prefix:
                    expect(self.page.locator("html")).to_have_attribute("dir","rtl")
                    outcome.select_option("mean");design.select_option("multiple")
                    # Batch #96 published the Arabic ANOVA lesson, so the chooser now links to it.
                    expect(status.get_by_role("link")).to_have_attribute("href","/ar/inference/classical-tests/one-way-anova-f-test/")
                    expect(status).not_to_contain_text("بالإنجليزية")
                    for locale,path in (("en",EN_HUB),("ar",AR_HUB),("x-default",EN_HUB)):
                        expect(self.page.locator('link[rel="alternate"][hreflang="'+locale+'"]')).to_have_attribute("href",BASE+path)
                else:
                    labs=self.page.locator("#companion-labs a")
                    self.assertEqual(labs.count(),5)
                    expect(self.page.locator("#lessons .lesson-card")).to_have_count(12)
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            self.visit(AR_HUB)
            self.fit("#esa-ar-test-guide",width)
            hrefs=self.page.locator("#lessons a").evaluate_all("as=>as.map(a=>a.getAttribute('href'))")
            self.assertGreaterEqual(len(hrefs),17)
            for href in hrefs:
                self.assertTrue((args.site/href.strip("/")/"index.html").is_file(),href)

    def test_generated_noscript_notices(self):
        nojs=self.browser.new_context(java_script_enabled=False)
        try:
            p=nojs.new_page()
            for route,word in (("/probability/distributions/normal-distribution/","interactive laboratory"),
                               ("/ar/probability/distributions/normal-distribution/","مختبر تفاعلي"),
                               ("/probability/lln-clt/central-limit-theorem/","interactive laboratory"),
                               ("/modeling/diagnostics/cooks-distance/","interactive laboratory"),
                               ("/ar/inference/classical-tests/paired-t-test/","مختبر تفاعلي"),(KAPPA,"JavaScript"),(AR_MCN,"JavaScript")):
                with self.subTest(route=route):
                    p.goto(self.origin+route,wait_until="domcontentloaded")
                    note=p.locator("noscript .esa-noscript")
                    self.assertEqual(note.count(),1)
                    self.assertIn(word,note.inner_text())
        finally:nojs.close()

if __name__=="__main__":unittest.main(argv=[__file__])
