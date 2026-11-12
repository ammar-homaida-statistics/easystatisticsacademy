"""Batch #92: Arabic GOF/OLS/security and Fisher/two-proportion accessibility."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
import unittest
from playwright.sync_api import sync_playwright,expect
ap=argparse.ArgumentParser()
ap.add_argument("--site",type=Path,default=Path("_site"))
args=ap.parse_args()
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*a):pass
class Browser92(unittest.TestCase):
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
    def test_arabic_gof_and_english_numeric_parity(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            for lang,route in (("en","/inference/classical-tests/chi-square-goodness-of-fit/"),("ar","/ar/inference/classical-tests/chi-square-goodness-of-fit/")):
                with self.subTest(width=width,lang=lang):
                    self.visit(route)
                    expect(self.page.locator("html")).to_have_attribute("lang",lang)
                    if lang=="ar":expect(self.page.locator("html")).to_have_attribute("dir","rtl")
                    for locale,path in (("en","/inference/classical-tests/chi-square-goodness-of-fit/"),("ar","/ar/inference/classical-tests/chi-square-goodness-of-fit/")):
                        expect(self.page.locator('link[rel="alternate"][hreflang="'+locale+'"]')).to_have_attribute("href","https://easystatisticsacademy.com"+path)
                    self.fit("#esa-gof-explorer",width)
                    expect(self.page.locator("#esa-gof-chi")).to_have_text("1.600000")
                    expect(self.page.locator("#esa-gof-df")).to_have_text("5")
                    self.page.locator("#esa-gof-probs").fill("0.2, 0.2")
                    expect(self.page.locator("#esa-gof-error")).to_be_visible()
                    self.page.locator("#esa-gof-die").focus();self.page.keyboard.press("Enter")
                    expect(self.page.locator("#esa-gof-error")).to_be_hidden()
                    if lang=="ar":self.assertIn("الفئة",self.page.locator("#esa-gof-table").inner_text())
    def test_ols_residuals_and_invalid_inputs(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            self.visit("/modeling/simple-linear-regression/residuals/")
            self.fit("#esa-residual-lab",width)
            expect(self.page.locator("#esa-residual-slope")).to_have_text("0.600000")
            expect(self.page.locator("#esa-residual-sse")).to_have_text("2.400000")
            expect(self.page.locator("#esa-residual-r2")).to_have_text("0.600000")
            self.page.locator("#esa-residual-y").fill("2, 4, 5")
            expect(self.page.locator("#esa-residual-error")).to_be_visible()
            self.page.locator("#esa-residual-outlier").focus();self.page.keyboard.press("Enter")
            expect(self.page.locator("#esa-residual-error")).to_be_hidden()
            self.assertNotEqual(self.page.locator("#esa-residual-slope").inner_text(),"0.600000")
    def test_slr_resume_tampering_and_legacy(self):
        route="/modeling/simple-linear-regression/"
        key="esa_continue_modeling_simple_linear_regression_lesson_v0"
        old="esa_continue_modeling_slr_lesson_v0"
        self.visit(route)
        pane=self.page.locator("#continue-reading-modeling-slr")
        valid={"url":"/modeling/simple-linear-regression/residuals/","label":"Residuals","ts":0}
        valid["ts"]=self.page.evaluate("Date.now()")
        def save(value,legacy=False):
            self.page.evaluate("([a,b,v,legacy])=>{localStorage.removeItem(a);localStorage.removeItem(b);localStorage.setItem(legacy?b:a,JSON.stringify(v))}",[key,old,value,legacy])
            self.page.reload(wait_until="networkidle")
        save(valid)
        expect(pane).to_be_visible()
        expect(self.page.locator("#continue-reading-modeling-slr-btn")).to_have_attribute("href",valid["url"])
        save(valid,True)
        expect(pane).to_be_visible()
        for bad in ({**valid,"label":"<img src=x onerror=alert(1)>"},{**valid,"url":"javascript:alert(1)"},
                    {**valid,"url":valid["url"]+"?foo"},{**valid,"ts":-1},
                    {**valid,"ts":9999999999999},{**valid,"ts":1.5},{**valid,"ts":True}):
            save(bad)
            expect(pane).to_be_hidden()
    def test_existing_labs_small_screen_keyboard_and_nojs(self):
        routes=[("/inference/classical-tests/fisher-exact-vs-chi-square/","#esa-fisher-chi-lab","#esa-fc-reset"),
                ("/inference/classical-tests/two-proportion-z-test/","#esa-two-proportion-lab","#esa-2p-reset")]
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            for route,lab,reset in routes:
                with self.subTest(route=route,width=width):
                    self.visit(route)
                    self.fit(lab,width)
                    expect(self.page.locator(reset)).to_be_visible()
                    self.page.locator(reset).focus();self.page.keyboard.press("Enter")
                    self.assertEqual(self.page.locator(reset).evaluate("e=>document.activeElement===e"),True)
        nojs=self.browser.new_context(java_script_enabled=False)
        try:
            p=nojs.new_page()
            for route,_,_ in routes:
                p.goto(self.origin+route,wait_until="domcontentloaded")
                self.assertIn("JavaScript",p.locator("noscript").inner_text())
        finally:nojs.close()
if __name__=="__main__":unittest.main(argv=[__file__])
