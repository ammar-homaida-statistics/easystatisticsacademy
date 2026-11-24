"""Batch #101: confidence-interval/test duality lab, Arabic null/alternative, power and
outlier lessons, and long heading words that fit 320 px screens."""
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
CID="/inference/hypothesis-testing/ci-and-test-connection/"
NULL="/ar/inference/hypothesis-testing/null-and-alternative/"
POW="/ar/inference/hypothesis-testing/power-and-effect-size/"
OUT="/ar/inference/assumptions-robustness/outliers-and-influence/"

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

class Browser101(unittest.TestCase):
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

    def test_duality_lab(self):
        for width in (320,375):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":820})
                self.visit(CID)
                lab=self.page.locator("#esa-cid-lab")
                expect(lab.locator("#esa-cid-crit")).to_have_text("t(24) = 2.0639")
                expect(lab.locator("#esa-cid-ci")).to_have_text("95%: [100.6914, 107.7086]")
                expect(lab.locator("#esa-cid-p")).to_have_text("0.020981")
                expect(lab.locator("#esa-cid-decision")).to_contain_text("Reject H₀")
                expect(lab.locator("#esa-cid-agree")).to_have_text("Interval and test agree.")
                self.fit("#esa-cid-lab",width)
                lab.locator("#esa-cid-inside-ex").click()
                expect(lab.locator("#esa-cid-inside")).to_contain_text("Yes")
                expect(lab.locator("#esa-cid-p")).to_have_text("0.228678")
                expect(lab.locator("#esa-cid-decision")).to_contain_text("Do not reject")
                lab.locator("#esa-cid-example").click()
                lab.locator("#esa-cid-boundary").click()
                expect(lab.locator("#esa-cid-p")).to_have_text("0.050000")
                expect(lab.locator("#esa-cid-inside")).to_contain_text("Yes")
                expect(lab.locator("#esa-cid-agree")).to_have_text("Interval and test agree.")
                lab.locator("#esa-cid-method").select_option("z")
                lab.locator("#esa-cid-side").select_option("greater")
                lab.locator("#esa-cid-mean").fill("51.3");lab.locator("#esa-cid-sd").fill("4")
                lab.locator("#esa-cid-n").fill("16");lab.locator("#esa-cid-mu0").fill("50")
                expect(lab.locator("#esa-cid-crit")).to_have_text("z = 1.6449")
                expect(lab.locator("#esa-cid-ci")).to_have_text("95%: [49.6551, ∞]")
                expect(lab.locator("#esa-cid-p")).to_have_text("0.096800")
                lab.locator("#esa-cid-n").fill("1")
                expect(lab.locator("#esa-cid-error")).to_be_visible()
                expect(lab.locator("#esa-cid-n")).to_have_attribute("aria-invalid","true")
                expect(lab.locator("#esa-cid-results")).to_be_hidden()
                self.fit("main",width)

    def test_new_arabic_lessons(self):
        for route,nav in ((NULL,"/ar/inference/hypothesis-testing/test-statistic-standardization/"),
                          (POW,"/ar/inference/hypothesis-testing/one-sided-vs-two-sided/"),
                          (OUT,"/ar/inference/assumptions-robustness/robust-alternatives-nonparametric/")):
            for width in (320,375):
                with self.subTest(route=route,width=width):
                    self.page.set_viewport_size({"width":width,"height":820})
                    self.visit(route)
                    expect(self.page.locator("html")).to_have_attribute("dir","rtl")
                    expect(self.page.locator('main .lesson-nav a[href="%s"]'%nav)).to_have_count(1)
                    group=self.page.locator('[role="group"][aria-label*="Language selection"]')
                    expect(group.locator('a[lang="en"]')).to_have_attribute("href",route[3:])
                    self.fit("main",width)
            self.visit(route[3:])
            expect(self.page.locator('main a[href="%s"]'%route).first).to_be_visible()
        for page,target in (("/ar/inference/hypothesis-testing/test-statistic-standardization/",NULL),
                            ("/ar/inference/hypothesis-testing/one-sided-vs-two-sided/",POW),
                            ("/ar/inference/hypothesis-testing/type1-type2-errors/",POW),
                            ("/ar/inference/assumptions-robustness/robust-alternatives-nonparametric/",OUT)):
            self.visit(page)
            self.assertGreaterEqual(self.page.locator('main a[href="%s"]'%target).count(),1,page)

    def test_long_headings_fit(self):
        self.page.set_viewport_size({"width":320,"height":820})
        for route in ("/applied-statistics/study-design/sampling-representativeness/",
                      "/modeling/diagnostics/heteroscedasticity/",
                      "/modeling/multiple-regression/multicollinearity/",
                      "/modeling/assumptions/homoscedasticity/",
                      "/descriptive/shape/standardization-when-and-when-not/",
                      "/inference/interpretation-reporting/reproducibility-and-analysis-checklist/",
                      "/mathematical-statistics/statistical-models/parameter-space-and-identifiability/",
                      "/ar/probability/distributions/hypergeometric-distribution/",
                      "/inference/assumptions-robustness/heteroscedasticity-variance-issues/"):
            with self.subTest(route=route):
                self.visit(route)
                h=self.page.locator("main h1").first
                sw,cw=h.evaluate("e=>[e.scrollWidth,e.clientWidth]")
                self.assertLessEqual(sw,cw+1,route)
                self.assertLessEqual(self.page.evaluate("()=>document.documentElement.scrollWidth"),321,route)

if __name__=="__main__":
    import sys
    unittest.main(argv=[sys.argv[0]])
