"""Batch #104: exact proportion-coverage lab (English and Arabic), Arabic Wald/Wilson and
precision explorers, and new Arabic lessons and links at 320/375 px."""
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
PROP="/inference/confidence-intervals/ci-for-proportion/"
TCI="/ar/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/"
NORM="/ar/inference/assumptions-robustness/checking-normality-what-and-why/"
PREC="/ar/inference/confidence-intervals/width-and-precision-what-controls/"

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

class Browser104(unittest.TestCase):
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

    def test_coverage_lab_both_languages(self):
        for route,lang in ((PROP,"en"),("/ar"+PROP,"ar")):
            for width in (320,375):
                with self.subTest(route=route,width=width):
                    self.page.set_viewport_size({"width":width,"height":820})
                    self.visit(route)
                    lab=self.page.locator("#esa-pcov-lab")
                    expect(lab.locator("#esa-pcov-wald")).to_have_text("0.8085")
                    expect(lab.locator("#esa-pcov-wilson")).to_have_text("0.9742")
                    expect(lab.locator("#esa-pcov-cp")).to_have_text("0.9922")
                    expect(lab.locator("#esa-pcov-wald-flag")).to_have_text("أقل من المستوى الاسمي" if lang=="ar" else "below the nominal level")
                    self.assertEqual(lab.locator("#esa-pcov-chart path").count(),3)
                    self.fit("#esa-pcov-lab",width)
                    lab.locator("#esa-pcov-rare").click()
                    expect(lab.locator("#esa-pcov-wald")).to_have_text("0.6389")
                    expect(lab.locator("#esa-pcov-cp")).to_have_text("0.9841")
                    lab.locator("#esa-pcov-half").click()
                    expect(lab.locator("#esa-pcov-wilson")).to_have_text("0.9431")
                    lab.locator("#esa-pcov-p").fill("1")
                    expect(lab.locator("#esa-pcov-error")).to_be_visible()
                    expect(lab.locator("#esa-pcov-p")).to_have_attribute("aria-invalid","true")
                    expect(lab.locator("#esa-pcov-results")).to_be_hidden()
                    self.fit("main",width)

    def test_arabic_wald_wilson_and_precision_labs(self):
        for width in (320,375):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":820})
                self.visit("/ar"+PROP)
                sp=self.page.locator("#esa-single-proportion-lab")
                expect(sp.locator("#esa-sp-estimate")).to_have_text("62.0000")
                expect(sp.locator("#esa-sp-waldlo")).to_have_text("57.7455")
                expect(sp.locator("#esa-sp-wilsonlo")).to_have_text("57.6692")
                expect(sp.locator("#esa-sp-warning")).to_contain_text("لا تُضمن التغطية")
                sp.locator("#esa-sp-x").fill("2");sp.locator("#esa-sp-n").fill("20")
                expect(sp.locator("#esa-sp-warning")).to_contain_text("والد")
                sp.locator("#esa-sp-x").fill("30")
                expect(sp.locator("#esa-sp-error")).to_contain_text("أدخل")
                self.fit("#esa-single-proportion-lab",width)
                self.visit(PREC)
                pr=self.page.locator("#esa-precision-lab")
                expect(pr.locator("#esa-pr-needed")).to_have_text("171")
                expect(pr.locator("#esa-pr-margin")).to_have_text("3.919928")
                expect(pr.locator("#esa-pr-explain")).to_contain_text("تنصيف")
                pr.locator("#esa-pr-sigma").fill("0")
                expect(pr.locator("#esa-pr-error")).to_contain_text("استخدم")
                self.fit("main",width)

    def test_new_arabic_lessons_and_chain(self):
        for route,nav in ((TCI,"/ar/inference/confidence-intervals/ci-for-mean-sigma-known-z/"),
                          (NORM,"/ar/inference/assumptions-robustness/independence-and-dependence/"),
                          (PREC,"/inference/confidence-intervals/common-mistakes-and-interpretation/"),
                          ("/ar"+PROP,"/ar/inference/confidence-intervals/ci-for-difference-of-means-independent/")):
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
        for src,target in (("/ar/inference/confidence-intervals/ci-for-mean-sigma-known-z/",TCI),
                           ("/ar/inference/assumptions-robustness/independence-and-dependence/",NORM)):
            self.visit(src)
            self.assertGreaterEqual(self.page.locator('main .lesson-nav a[href="%s"]'%target).count(),1,src)

if __name__=="__main__":
    import sys
    unittest.main(argv=[sys.argv[0]])
