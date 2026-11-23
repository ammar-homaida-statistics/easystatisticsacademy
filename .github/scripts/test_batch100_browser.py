"""Batch #100: Arabic robust-methods lesson with both rank labs, Levene/Brown–Forsythe
lab, Arabic test-statistic and one/two-sided lessons, and inline formulas that fit
320 px screens."""
import argparse
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
ROOT=Path(__file__).resolve().parents[2]
ROB="/ar/inference/assumptions-robustness/robust-alternatives-nonparametric/"
LEV="/inference/assumptions-robustness/heteroscedasticity-variance-issues/"
TS="/ar/inference/hypothesis-testing/test-statistic-standardization/"
SIDES="/ar/inference/hypothesis-testing/one-sided-vs-two-sided/"

def pairs():
    out=[];cur=None
    for line in (ROOT/"_data/translations.yml").read_text(encoding="utf-8").splitlines():
        m=re.match(r'^- id:\s*(\S+)\s*$',line)
        if m: cur={"id":m.group(1)};out.append(cur);continue
        m=re.match(r'^\s+(en|ar):\s*(\S+)\s*$',line)
        if m and cur is not None: cur[m.group(1)]=m.group(2)
    return out

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*a):pass

class Browser100(unittest.TestCase):
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
        doc=self.page.evaluate("()=>document.documentElement.scrollWidth")
        wide=self.page.evaluate("""w=>[...document.querySelectorAll('body *')].filter(e=>{if(e.getBoundingClientRect().right<=w+1)return false;
            for(let a=e.parentElement;a&&a!==document.body;a=a.parentElement){const o=getComputedStyle(a).overflowX;
              if(o!=="visible"&&o!=="clip"&&a.getBoundingClientRect().right<=w+1)return false;}return true;})
          .slice(0,12).map(e=>e.tagName+'#'+e.id+'.'+String(e.className).slice(0,40)+' r='+Math.round(e.getBoundingClientRect().right)+' '+(e.textContent||'').trim().slice(0,50))""",width)
        text=self.page.evaluate("""()=>[...document.querySelectorAll('main *')].filter(e=>e.scrollWidth>e.clientWidth+2&&getComputedStyle(e).overflowX==='visible')
          .slice(0,8).map(e=>e.tagName+'#'+e.id+'.'+String(e.className).slice(0,30)+' sw='+e.scrollWidth+' cw='+e.clientWidth+' '+(e.textContent||'').trim().slice(0,60))""")
        self.assertLessEqual(doc,width+1,{"outside":wide,"text_overflow":text})

    def test_arabic_robust_labs(self):
        for width in (320,375):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":820})
                self.visit(ROB)
                expect(self.page.locator("html")).to_have_attribute("lang","ar")
                rt=self.page.locator("#esa-rt-lab")
                expect(rt.locator("#esa-rt-u1")).to_have_text("1")
                expect(rt.locator("#esa-rt-pexact")).to_have_text("0.008658")
                expect(rt.locator("#esa-rt-papprox")).to_have_text("0.013711")
                expect(rt.locator("#esa-rt-note")).to_contain_text("تُفضَّل القيمة الدقيقة")
                self.fit("#esa-rt-lab",width)
                rt.locator("#esa-rt-wx").click()
                expect(rt.locator("#esa-rt-tplus")).to_have_text("35")
                expect(rt.locator("#esa-rt-pexact")).to_have_text("0.015625")
                rt.locator("#esa-rt-ties").click()
                expect(rt.locator("#esa-rt-pexact")).to_have_text("غير متاح مع القيم المتساوية أو الفروق الصفرية")
                rt.locator("#esa-rt-y").fill("1, x")
                expect(rt.locator("#esa-rt-error")).to_contain_text("أدخل")
                expect(rt.locator("#esa-rt-results")).to_be_hidden()
                kw=self.page.locator("#esa-kw-lab")
                expect(kw.locator("#esa-kw-h")).to_have_text("10.6400")
                expect(kw.locator("#esa-kw-p")).to_have_text("0.004893")
                expect(kw.locator("#esa-kw-rows tr")).to_have_count(3)
                expect(kw.locator("#esa-kw-decision")).to_contain_text("عند α = 0.05 نرفض")
                self.fit("#esa-kw-lab",width)
                kw.locator("#esa-kw-input").fill("1, 2\n3")
                expect(kw.locator("#esa-kw-error")).to_be_hidden()
                kw.locator("#esa-kw-input").fill("1, a")
                expect(kw.locator("#esa-kw-error")).to_be_visible()
                self.fit("main",width)

    def test_levene_lab(self):
        for width in (320,375):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":820})
                self.visit(LEV)
                lab=self.page.locator("#esa-lv-lab")
                expect(lab.locator("#esa-lv-w")).to_have_text("16.2618")
                expect(lab.locator("#esa-lv-df")).to_have_text("2, 15")
                expect(lab.locator("#esa-lv-p")).to_have_text("0.000175")
                expect(lab.locator("#esa-lv-decision")).to_contain_text("there is evidence that the variances differ")
                self.fit("#esa-lv-lab",width)
                lab.locator("#esa-lv-center").select_option("mean")
                expect(lab.locator("#esa-lv-w")).to_have_text("16.9239")
                expect(lab.locator("#esa-lv-p")).to_have_text("0.000143")
                lab.locator("#esa-lv-outlier").click()
                expect(lab.locator("#esa-lv-w")).to_have_text("4.6904")
                expect(lab.locator("#esa-lv-p")).to_have_text("0.031257")
                lab.locator("#esa-lv-center").select_option("median")
                expect(lab.locator("#esa-lv-w")).to_have_text("0.8164")
                expect(lab.locator("#esa-lv-p")).to_have_text("0.465129")
                expect(lab.locator("#esa-lv-decision")).to_contain_text("not enough evidence")
                lab.locator("#esa-lv-equal").click()
                expect(lab.locator("#esa-lv-p")).to_have_text("0.903972")
                lab.locator("#esa-lv-input").fill("1, 3\n5, 9")
                expect(lab.locator("#esa-lv-decision")).to_contain_text("undefined")
                lab.locator("#esa-lv-input").fill("1\n2, 3")
                expect(lab.locator("#esa-lv-error")).to_be_visible()
                expect(lab.locator("#esa-lv-input")).to_have_attribute("aria-invalid","true")
                expect(lab.locator("#esa-lv-results")).to_be_hidden()
                self.fit("main",width)

    def test_new_arabic_lessons(self):
        for route,nav in ((TS,"/ar/inference/hypothesis-testing/p-value-meaning/"),
                          (SIDES,"/inference/hypothesis-testing/ci-and-test-connection/"),
                          (ROB,"/ar/inference/assumptions-robustness/bootstrap-as-robust-tool/")):
            for width in (320,375):
                with self.subTest(route=route,width=width):
                    self.page.set_viewport_size({"width":width,"height":820})
                    self.visit(route)
                    self.page.evaluate("()=>window.MathJax&&window.MathJax.startup&&window.MathJax.startup.promise")
                    expect(self.page.locator("html")).to_have_attribute("dir","rtl")
                    expect(self.page.locator('main .lesson-nav a[href="%s"]'%nav)).to_have_count(1)
                    group=self.page.locator('[role="group"][aria-label*="Language selection"]')
                    expect(group.locator('a[lang="en"]')).to_have_attribute("href",route[3:])
                    self.assertTrue(self.page.locator('link[rel="alternate"][hreflang="en"]').get_attribute("href").endswith(route[3:]))
                    self.fit("main",width)
        self.visit("/ar/inference/hypothesis-testing/p-value-meaning/")
        expect(self.page.locator('main .lesson-nav a[href="%s"]'%TS)).to_have_count(1)
        for en in (TS[3:],SIDES[3:],ROB[3:]):
            self.visit(en)
            expect(self.page.locator('main a[href="/ar%s"]'%en).first).to_be_visible()

    def test_fixed_inline_formulas_fit(self):
        self.page.set_viewport_size({"width":320,"height":820})
        for route in ("/ar/inference/classical-tests/paired-t-test/",
                      "/ar/probability/random-variables/discrete-random-variables/",
                      "/inference/classical-tests/two-sample-t-test-independent/",
                      "/inference/confidence-intervals/ci-for-proportion/",LEV):
            with self.subTest(route=route):
                self.visit(route)
                self.page.evaluate("()=>window.MathJax&&window.MathJax.startup&&window.MathJax.startup.promise")
                self.page.wait_for_timeout(300)
                self.assertEqual(self.page.locator("mjx-merror").count(),0)
                self.fit("main",320)

if __name__=="__main__":
    import sys
    unittest.main(argv=[sys.argv[0]])
