"""Batch #99: Mann–Whitney/Wilcoxon lab, accurate normal tails in four labs,
Arabic significance-level and effect-size lessons, and display formulas that
scroll instead of widening pages at 320 px."""
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
RT="/inference/assumptions-robustness/robust-alternatives-nonparametric/"
ALPHA="/inference/hypothesis-testing/significance-level-alpha/"
ES="/inference/power-sample-size/effect-size-and-practical-importance/"

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

class Browser99(unittest.TestCase):
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
        self.assertLessEqual(doc,width+1,wide)

    def test_rank_tests_lab(self):
        for width in (320,375):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":820})
                self.visit(RT)
                lab=self.page.locator("#esa-rt-lab")
                expect(lab.locator("#esa-rt-u1")).to_have_text("1")
                expect(lab.locator("#esa-rt-pexact")).to_have_text("0.008658")
                expect(lab.locator("#esa-rt-papprox")).to_have_text("0.013711")
                expect(lab.locator("#esa-rt-r")).to_have_text("-0.9333")
                expect(lab.locator("#esa-rt-hl")).to_have_text("-3.1000")
                expect(lab.locator("#esa-rt-row-wx")).to_be_hidden()
                self.fit("#esa-rt-lab",width)
                lab.locator("#esa-rt-side").select_option("less")
                expect(lab.locator("#esa-rt-pexact")).to_have_text("0.004329")
                lab.locator("#esa-rt-wx").click()
                expect(lab.locator("#esa-rt-row-wx")).to_be_visible()
                expect(lab.locator("#esa-rt-row-mw")).to_be_hidden()
                expect(lab.locator("#esa-rt-tplus")).to_have_text("35")
                expect(lab.locator("#esa-rt-pexact")).to_have_text("0.015625")
                expect(lab.locator("#esa-rt-papprox")).to_have_text("0.017290")
                lab.locator("#esa-rt-y").fill("1, 2")
                expect(lab.locator("#esa-rt-error")).to_be_visible()
                expect(lab.locator("#esa-rt-results")).to_be_hidden()
                lab.locator("#esa-rt-ties").click()
                expect(lab.locator("#esa-rt-pexact")).to_have_text("Not available with ties or zero differences")
                expect(lab.locator("#esa-rt-papprox")).to_have_text("0.036490")
                lab.locator("#esa-rt-x").fill("1, x")
                expect(lab.locator("#esa-rt-x")).to_have_attribute("aria-invalid","true")

    def test_corrected_normal_tails_in_browser(self):
        self.visit("/probability/distributions/normal-distribution/")
        v=self.page.evaluate("()=>[window.esaNormalMath.cdf(-8),window.esaNormalMath.survival(8),window.esaNormalMath.cdf(2)]")
        self.assertAlmostEqual(v[0]/6.22096057427174e-16,1,delta=1e-12)
        self.assertAlmostEqual(v[1]/6.22096057427174e-16,1,delta=1e-12)
        self.assertAlmostEqual(v[2],0.9772498680518208,delta=1e-15)
        self.visit("/probability/distributions/lognormal-distribution/")
        v=self.page.evaluate("()=>[window.esaLognormalMath.survival(2,0,.5),window.esaLognormalMath.cdf(0.001,0,.5)]")
        self.assertAlmostEqual(v[0],0.08282851900169846,delta=1e-15)
        self.assertAlmostEqual(v[1]/1.0274605390204012e-43,1,delta=1e-11)
        self.visit("/inference/classical-tests/two-proportion-z-test/")
        p=self.page.evaluate('()=>window.esaTwoProportionMath.compute(1,500,60,500,"less").p')
        self.assertGreater(p,0);self.assertLess(p,1e-14)
        self.visit("/inference/hypothesis-testing/type1-type2-errors/")
        expect(self.page.locator("#esa-errors-power-theory")).to_have_text("78.19%")

    def test_arabic_lessons_and_links(self):
        for route,next_href in (("/ar"+ALPHA,"/ar/inference/hypothesis-testing/type1-type2-errors/"),
                                ("/ar"+ES,"/inference/power-sample-size/power-curve-and-tradeoffs/")):
            for width in (320,375):
                with self.subTest(route=route,width=width):
                    self.page.set_viewport_size({"width":width,"height":820})
                    self.visit(route)
                    expect(self.page.locator("html")).to_have_attribute("lang","ar")
                    expect(self.page.locator('main .lesson-nav a[href="%s"]'%next_href)).to_have_count(1)
                    group=self.page.locator('[role="group"][aria-label*="Language selection"]')
                    expect(group.locator('a[lang="en"]')).to_have_attribute("href",route[3:])
                    self.fit("main",width)

    def test_display_formulas_do_not_widen_pages(self):
        self.page.set_viewport_size({"width":320,"height":820})
        for route in PAGES:
            with self.subTest(route=route):
                self.visit(route)
                self.page.evaluate("()=>window.MathJax&&window.MathJax.startup&&window.MathJax.startup.promise")
                overflow=self.page.evaluate("()=>document.documentElement.scrollWidth")
                wide=self.page.evaluate("""w=>[...document.querySelectorAll('body *')].filter(e=>{if(e.getBoundingClientRect().right<=w+1)return false;
                  for(let a=e.parentElement;a&&a!==document.body;a=a.parentElement){const o=getComputedStyle(a).overflowX;
                    if(o!=="visible"&&o!=="clip"&&a.getBoundingClientRect().right<=w+1)return false;}return true;})
                  .slice(0,8).map(e=>e.tagName+'#'+e.id+'.'+String(e.className).slice(0,30)+' r='+Math.round(e.getBoundingClientRect().right))""",320)
                self.assertLessEqual(overflow,321,wide)
                block=self.page.locator('mjx-container[display="true"]')
                if block.count():
                    self.assertEqual(block.first.evaluate("e=>getComputedStyle(e).overflowX"),"auto")

PAGES=[
 "/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/",
 "/inference/hypothesis-testing/one-sided-vs-two-sided/",
 "/inference/classical-tests/one-way-anova-f-test/",
 "/inference/classical-tests/cohens-kappa/",
 "/probability/basics/probability-axioms-and-basic-rules/",
 "/inference/hypothesis-testing/p-value-meaning/",
 "/inference/classical-tests/mcnemar-test/",
 "/probability/conditional/bayes-theorem/",
 "/inference/assumptions-robustness/robust-alternatives-nonparametric/",
 "/probability/lln-clt/weak-vs-strong-lln/",
 "/mathematical-statistics/estimator-properties/consistency-basic-idea/",
 "/mathematical-statistics/fisher-information-and-efficiency/information-and-mle-connection-preview/",
 "/probability/sampling-distributions/standard-error-and-estimators/",
 "/inference/classical-tests/fisher-exact-vs-chi-square/",
 "/inference/power-sample-size/what-is-statistical-power/",
 "/probability/expectation-variance/variance-rules-and-sums/",
 "/ar/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/",
 "/ar/inference/classical-tests/cohens-kappa/",
 "/ar/inference/classical-tests/one-way-anova-f-test/",
 "/ar/inference/classical-tests/mcnemar-test/",
 "/ar/probability/conditional/bayes-theorem/",
 "/ar/inference/classical-tests/two-sample-t-test-independent/",
 "/ar/inference/classical-tests/chi-square-independence-test/",
 "/ar/inference/classical-tests/chi-square-homogeneity-test/",
 "/ar/inference/classical-tests/fisher-exact-vs-chi-square/"
]

if __name__=="__main__":
    import sys
    unittest.main(argv=[sys.argv[0]])
