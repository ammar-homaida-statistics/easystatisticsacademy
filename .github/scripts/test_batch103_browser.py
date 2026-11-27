"""Batch #103: AR(1) dependence lab (English and Arabic), Arabic practical-significance
explorer, and new Arabic lessons and links at 320/375 px."""
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
IND="/inference/assumptions-robustness/independence-and-dependence/"
PRAC="/ar/inference/hypothesis-testing/practical-significance/"
BLUE="/ar/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/"
ZCI="/ar/inference/confidence-intervals/ci-for-mean-sigma-known-z/"

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

class Browser103(unittest.TestCase):
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

    def test_ar1_lab_both_languages(self):
        for route,lang in ((IND,"en"),("/ar"+IND,"ar")):
            for width in (320,375):
                with self.subTest(route=route,width=width):
                    self.page.set_viewport_size({"width":width,"height":820})
                    self.visit(route)
                    lab=self.page.locator("#esa-ar1-lab")
                    expect(lab.locator("#esa-ar1-vif")).to_have_text("2.9600")
                    expect(lab.locator("#esa-ar1-neff")).to_have_text("33.8")
                    expect(lab.locator("#esa-ar1-typeI")).to_have_text("0.254617")
                    expect(lab.locator("#esa-ar1-note")).to_contain_text("0.254617")
                    self.fit("#esa-ar1-lab",width)
                    lab.locator("#esa-ar1-neg").click()
                    expect(lab.locator("#esa-ar1-vif")).to_have_text("0.3378")
                    expect(lab.locator("#esa-ar1-typeI")).to_have_text("0.000745")
                    expect(lab.locator("#esa-ar1-note")).to_contain_text("محافظ" if lang=="ar" else "conservative")
                    lab.locator("#esa-ar1-ind").click()
                    expect(lab.locator("#esa-ar1-typeI")).to_have_text("0.050000")
                    expect(lab.locator("#esa-ar1-note")).to_contain_text("ρ = 0")
                    lab.locator("#esa-ar1-rho").fill("0.99")
                    expect(lab.locator("#esa-ar1-error")).to_be_visible()
                    expect(lab.locator("#esa-ar1-rho")).to_have_attribute("aria-invalid","true")
                    expect(lab.locator("#esa-ar1-results")).to_be_hidden()
                    self.fit("main",width)

    def test_arabic_practical_lab(self):
        for width in (320,375):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":820})
                self.visit(PRAC)
                lab=self.page.locator("#esa-practical-significance-lab")
                expect(lab.locator("#esa-ps-effect")).to_have_text("0.200000")
                expect(lab.locator("#esa-ps-t")).to_have_text("4.000000")
                expect(lab.locator("#esa-ps-statistical")).to_contain_text("دالّ إحصائيًا")
                expect(lab.locator("#esa-ps-practical")).to_contain_text("أقل من العتبة")
                self.fit("#esa-practical-significance-lab",width)
                lab.locator("#esa-ps-threshold").fill("-1")
                expect(lab.locator("#esa-ps-error")).to_contain_text("أدخل")
                lab.locator("#esa-ps-reset").click()
                expect(lab.locator("#esa-ps-error")).to_be_hidden()
                self.fit("main",width)

    def test_new_arabic_lessons_and_chain(self):
        for route,nav in ((PRAC,"/ar/inference/classical-tests/"),
                          (BLUE,"/ar/inference/confidence-intervals/critical-values-z-and-t/"),
                          (ZCI,"/ar/inference/confidence-intervals/critical-values-z-and-t/"),
                          ("/ar"+IND,"/ar/inference/assumptions-robustness/heteroscedasticity-variance-issues/")):
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
        for src,target in (("/ar/inference/hypothesis-testing/ci-and-test-connection/",PRAC),
                           ("/ar/inference/confidence-intervals/what-is-a-confidence-interval/",BLUE),
                           ("/ar/inference/confidence-intervals/critical-values-z-and-t/",ZCI),
                           ("/ar/inference/assumptions-robustness/heteroscedasticity-variance-issues/","/ar"+IND)):
            self.visit(src)
            self.assertGreaterEqual(self.page.locator('main .lesson-nav a[href="%s"]'%target).count(),1,src)

if __name__=="__main__":
    import sys
    unittest.main(argv=[sys.argv[0]])
