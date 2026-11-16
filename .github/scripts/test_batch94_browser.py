"""Batch #94: McNemar lab, Arabic homogeneity, hardened readers, no-JS notices
and LearningResource output."""
import argparse
import json
import re
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
EN_HOM="/inference/classical-tests/chi-square-homogeneity-test/"
AR_HOM="/ar"+EN_HOM
MCN="/inference/classical-tests/mcnemar-test/"

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*a):pass

class Browser94(unittest.TestCase):
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

    def test_mcnemar_lab(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            self.visit(MCN)
            lab=self.page.locator("#esa-mcnemar-lab")
            self.fit("#esa-mcnemar-lab",width)
            expect(lab.locator("#esa-mcn-chi")).to_have_text("9.000000")
            expect(lab.locator("#esa-mcn-p")).to_have_text("0.002700")
            expect(lab.locator("#esa-mcn-pcc")).to_have_text("0.005110")
            expect(lab.locator("#esa-mcn-exact")).to_have_text("0.004077")
            lab.locator("#esa-mcn-a").fill("900")
            expect(lab.locator("#esa-mcn-exact")).to_have_text("0.004077")
            lab.locator("#esa-mcn-small").focus();self.page.keyboard.press("Enter")
            expect(lab.locator("#esa-mcn-exact")).to_have_text("0.125000")
            expect(lab.locator("#esa-mcn-advice")).to_contain_text("exact binomial")
            lab.locator("#esa-mcn-none").focus();self.page.keyboard.press("Space")
            expect(lab.locator("#esa-mcn-chi")).to_have_text("Undefined")
            expect(lab.locator("#esa-mcn-advice")).to_contain_text("no discordant pairs")
            lab.locator("#esa-mcn-b").fill("-2")
            expect(lab.locator("#esa-mcn-error")).to_be_visible()
            expect(lab.locator("#esa-mcn-b")).to_have_attribute("aria-invalid","true")
            lab.locator("#esa-mcn-example").focus();self.page.keyboard.press("Enter")
            expect(lab.locator("#esa-mcn-error")).to_be_hidden()
            expect(lab.locator("#esa-mcn-chi")).to_have_text("9.000000")

    def test_arabic_homogeneity_parity(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            for lang,route in (("en",EN_HOM),("ar",AR_HOM)):
                with self.subTest(width=width,lang=lang):
                    self.visit(route)
                    expect(self.page.locator("html")).to_have_attribute("lang",lang)
                    if lang=="ar":expect(self.page.locator("html")).to_have_attribute("dir","rtl")
                    for locale,path in (("en",EN_HOM),("ar",AR_HOM),("x-default",EN_HOM)):
                        expect(self.page.locator('link[rel="alternate"][hreflang="'+locale+'"]')).to_have_attribute("href",BASE+path)
                    self.fit("#esa-homogeneity-lab",width)
                    expect(self.page.locator("#esa-hom-chi")).to_have_text("8.896104")
                    expect(self.page.locator("#esa-hom-p")).to_have_text("0.063750")
                    self.assertEqual(self.page.locator("#esa-hom-residuals td.esa-hom-flag").count(),3)
                    note=self.page.locator("#esa-hom-residual-note")
                    expect(note).to_contain_text("3 من 9" if lang=="ar" else "3 of 9 cells")
                    if lang=="ar":
                        self.assertIn("المجتمع 1",self.page.locator("#esa-hom-table").inner_text())
                        self.assertIn("الفئة 1",self.page.locator("#esa-hom-chart").get_attribute("aria-label"))
                    self.page.locator("#esa-hom-input").fill("0, 0\n3, 4")
                    err=self.page.locator("#esa-hom-error")
                    expect(err).to_be_visible()
                    self.assertIn("أدخل" if lang=="ar" else "Enter a rectangular",err.inner_text())
                    self.page.locator("#esa-hom-cities").focus();self.page.keyboard.press("Enter")
                    expect(err).to_be_hidden()

    def test_hardened_readers(self):
        ms=[("/mathematical-statistics/fisher-information-and-efficiency/","esa_continue_ms_information_last_lesson_v0","continue-reading-ms-b5",
             "/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/","Lesson 2 — Cramér–Rao Lower Bound"),
            ("/mathematical-statistics/statistical-models/","esa_continue_ms_statistical_models_last_lesson_v0","continue-reading-ms-b1",
             "/mathematical-statistics/statistical-models/iid-and-modeling-assumptions/","Lesson 3 — IID and Modeling Assumptions")]
        applied=[("/applied-statistics/"+s+"/","esa_continue_applied_"+s+"_lesson_v0","continue-reading-"+s)
                 for s in ("reporting","effect-sizes","common-mistakes","practice")]
        def save(key,value):
            self.page.evaluate("([k,v])=>localStorage.setItem(k,JSON.stringify(v))",[key,value])
            self.page.reload(wait_until="networkidle")
        for route,key,wid,url,label in ms:
            with self.subTest(route=route):
                self.visit(route)
                now=self.page.evaluate("Date.now()")
                valid={"url":url,"label":label,"ts":now}
                save(key,valid)
                expect(self.page.locator("#"+wid)).to_be_visible()
                expect(self.page.locator("#"+wid+"-label")).to_have_text("You last visited: "+label)
                expect(self.page.locator("#"+wid+"-btn")).to_have_attribute("href",url)
                for bad in ({**valid,"url":"javascript:alert(1)"},{**valid,"label":"<img src=x onerror=alert(1)>"},
                            {**valid,"url":url+"?x"},{**valid,"ts":now+3600*1000},{**valid,"ts":now+0.5},
                            {**valid,"ts":-5},{"url":url,"label":label}):
                    save(key,bad)
                    expect(self.page.locator("#"+wid)).to_be_hidden()
                    self.assertEqual(self.page.locator("#"+wid+"-label img").count(),0)
        for route,key,wid in applied:
            with self.subTest(route=route):
                self.visit(route)
                now=self.page.evaluate("Date.now()")
                for bad in ({"url":route,"label":"<img src=x onerror=alert(1)>","ts":now},
                            {"url":"javascript:alert(1)","label":"x","ts":now}):
                    save(key,bad)
                    expect(self.page.locator("#"+wid)).to_be_hidden()
                    self.assertEqual(self.page.locator("#"+wid+" img").count(),0)
        self.page.add_init_script("""Object.defineProperty(window,"localStorage",{configurable:true,get(){throw new DOMException("denied","SecurityError");}});""")
        for route in [m[0] for m in ms]+[a[0] for a in applied]:
            self.visit(route)
            expect(self.page.locator("main h1")).to_be_visible()

    def test_noscript_notices(self):
        nojs=self.browser.new_context(java_script_enabled=False)
        try:
            p=nojs.new_page()
            for route in ("/inference/classical-tests/chi-square-goodness-of-fit/","/ar/inference/classical-tests/chi-square-goodness-of-fit/",
                          "/inference/classical-tests/chi-square-independence-test/","/ar/inference/classical-tests/chi-square-independence-test/",
                          EN_HOM,AR_HOM,MCN):
                with self.subTest(route=route):
                    p.goto(self.origin+route,wait_until="domcontentloaded")
                    note=p.locator("noscript .esa-noscript")
                    self.assertEqual(note.count(),1)
                    self.assertIn("JavaScript",note.inner_text())
        finally:nojs.close()

    def test_learning_resource_output(self):
        for route,lang in (("/probability/distributions/normal-distribution/","en"),("/ar/probability/distributions/normal-distribution/","ar"),
                           ("/probability/conditional/tree-diagrams/","en"),(AR_HOM,"ar"),(MCN,"en")):
            with self.subTest(route=route):
                html=(args.site/route.strip("/")/"index.html").read_text(encoding="utf-8")
                blocks=[json.loads(b) for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>',html,re.S)]
                lr=[b for b in blocks if b.get("@type")=="LearningResource"]
                self.assertEqual(len(lr),1)
                self.assertEqual(lr[0]["inLanguage"],lang)
                self.assertEqual(lr[0]["url"],BASE+route)

if __name__=="__main__":unittest.main(argv=[__file__])
