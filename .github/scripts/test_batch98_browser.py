"""Batch #98: Arabic p-value, power and exact-binomial lessons, the Kruskal–Wallis
lab, fixed Arabic navigation links, and page width at 320 px."""
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
PV="/inference/hypothesis-testing/p-value-meaning/"
POWER="/inference/power-sample-size/what-is-statistical-power/"
EB="/inference/classical-tests/exact-binomial-vs-z-test/"
KW="/inference/assumptions-robustness/robust-alternatives-nonparametric/"

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

class Browser98(unittest.TestCase):
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

    def test_pvalue_lab_both_languages(self):
        for route,rej,keep in ((PV,"Reject the null","Do not reject"),("/ar"+PV,"نرفض الفرضية الصفرية","لا نرفض")):
            for width in (320,375):
                with self.subTest(route=route,width=width):
                    self.page.set_viewport_size({"width":width,"height":820})
                    self.visit(route)
                    lab=self.page.locator("#esa-pvalue-explorer")
                    expect(lab.locator("#esa-p-prob")).to_have_text("0.0455003")
                    expect(lab.locator("#esa-p-decision")).to_contain_text(rej)
                    lab.locator("#esa-p-side").select_option("left")
                    expect(lab.locator("#esa-p-prob")).to_have_text("0.9772499")
                    expect(lab.locator("#esa-p-decision")).to_contain_text(keep)
                    lab.locator("#esa-p-z").fill("8");lab.locator("#esa-p-side").select_option("two-sided")
                    expect(lab.locator("#esa-p-prob")).to_have_text("1.244192e-15")
                    lab.locator("#esa-p-z").fill("36")
                    expect(lab.locator("#esa-p-error")).to_be_visible()
                    lab.locator("#esa-p-reset").click()
                    expect(lab.locator("#esa-p-error")).to_be_hidden()
                    self.fit("#esa-pvalue-explorer",width)

    def test_exact_binomial_lab_both_languages(self):
        for route,warn in ((EB,"below 10"),("/ar"+EB,"أقل من 10")):
            for width in (320,375):
                with self.subTest(route=route,width=width):
                    self.page.set_viewport_size({"width":width,"height":820})
                    self.visit(route)
                    lab=self.page.locator("#esa-exact-binomial-lab")
                    expect(lab.locator("#esa-eb-exact")).to_have_text("0.109375")
                    expect(lab.locator("#esa-eb-approx")).to_have_text("0.057780")
                    expect(lab.locator("#esa-eb-warning")).to_contain_text(warn)
                    lab.locator("#esa-eb-side").select_option("greater")
                    expect(lab.locator("#esa-eb-exact")).to_have_text("0.989258")
                    lab.locator("#esa-eb-side").select_option("less")
                    expect(lab.locator("#esa-eb-exact")).to_have_text("0.054688")
                    lab.locator("#esa-eb-n").fill("2001")
                    expect(lab.locator("#esa-eb-error")).to_be_visible()
                    lab.locator("#esa-eb-reset").click()
                    expect(lab.locator("#esa-eb-exact")).to_have_text("0.109375")
                    self.fit("#esa-exact-binomial-lab",width)

    def test_kruskal_wallis_lab(self):
        for width in (320,375):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":820})
                self.visit(KW)
                lab=self.page.locator("#esa-kw-lab")
                expect(lab.locator("#esa-kw-rows tr")).to_have_count(3)
                expect(lab.locator("#esa-kw-hc")).to_have_text("10.6400")
                expect(lab.locator("#esa-kw-p")).to_have_text("0.004893")
                expect(lab.locator("#esa-kw-pperm")).to_contain_text(" ± ")
                expect(lab.locator("#esa-kw-eps")).to_have_text("0.7600")
                expect(lab.locator("#esa-kw-decision")).to_contain_text("reject the hypothesis")
                self.fit("#esa-kw-lab",width)
                lab.locator("#esa-kw-ties").click()
                expect(lab.locator("#esa-kw-c")).to_have_text("0.945304")
                expect(lab.locator("#esa-kw-hc")).to_have_text("9.1898")
                lab.locator("#esa-kw-small").click()
                expect(lab.locator("#esa-kw-p")).to_have_text("0.068525")
                expect(lab.locator("#esa-kw-note")).to_contain_text("fewer than 5")
                lab.locator("#esa-kw-input").fill("1, 1, 1\n1, 1")
                expect(lab.locator("#esa-kw-note")).to_contain_text("All observations are tied")
                expect(lab.locator("#esa-kw-hc")).to_have_text("Undefined")
                lab.locator("#esa-kw-input").fill("1, x\n2, 3")
                expect(lab.locator("#esa-kw-error")).to_be_visible()
                expect(lab.locator("#esa-kw-input")).to_have_attribute("aria-invalid","true")
                expect(lab.locator("#esa-kw-results")).to_be_hidden()

    def test_fixed_arabic_navigation_links(self):
        self.visit("/ar/probability/distributions/binomial-distribution/")
        main=self.page.locator("main")
        expect(main.locator('a[href="/ar/probability/distributions/geometric-distribution/"]').first).to_be_attached()
        expect(main.locator('a[href="/probability/distributions/geometric-distribution/"]')).to_have_count(0)
        self.visit("/ar/probability/conditional/bayes-theorem/")
        expect(self.page.locator('main a[href="/ar/probability/conditional/tree-diagrams/"]').first).to_be_attached()

    def test_new_and_changed_pages_fit_320(self):
        self.page.set_viewport_size({"width":320,"height":820})
        for route in (PV,"/ar"+PV,POWER,"/ar"+POWER,EB,"/ar"+EB,KW,"/ar/","/ar/probability/distributions/poisson-distribution/",
                      "/ar/probability/conditional/bayes-theorem/"):
            with self.subTest(route=route):
                self.visit(route)
                self.fit("main",320)

if __name__=="__main__":
    import sys
    unittest.main(argv=[sys.argv[0]])
