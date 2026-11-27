"""Batch #105: CLT / t-interval coverage lab (English and Arabic), Arabic two-proportion
and Welch labs, and new Arabic lessons and links at 320/375 px."""
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
COND="/inference/confidence-intervals/conditions-normality-clt-independence/"
DPROP="/ar/inference/confidence-intervals/ci-for-difference-of-proportions/"
DMEAN="/ar/inference/confidence-intervals/ci-for-difference-of-means-independent/"
MODEL="/ar/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/"

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

class Browser105(unittest.TestCase):
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

    def test_clt_lab_both_languages(self):
        for route,lang in ((COND,"en"),("/ar"+COND,"ar")):
            for width in (320,375):
                with self.subTest(route=route,width=width):
                    self.page.set_viewport_size({"width":width,"height":820})
                    self.visit(route)
                    lab=self.page.locator("#esa-clt-lab")
                    expect(lab.locator("#esa-clt-coverage")).to_have_text("0.8995")
                    expect(lab.locator("#esa-clt-below")).to_have_text("0.0959")
                    expect(lab.locator("#esa-clt-crit")).to_have_text("2.2622")
                    expect(lab.locator("#esa-clt-note")).to_contain_text("الأخطاء غير متوازنة" if lang=="ar" else "lopsided")
                    self.assertGreater(lab.locator("#esa-clt-chart rect").count(),10)
                    self.fit("#esa-clt-lab",width)
                    lab.locator("#esa-clt-norm10").click()
                    expect(lab.locator("#esa-clt-coverage")).to_have_text("0.9494")
                    expect(lab.locator("#esa-clt-note")).to_contain_text("متوازنة تقريبًا" if lang=="ar" else "roughly balanced")
                    lab.locator("#esa-clt-exp100").click()
                    expect(lab.locator("#esa-clt-coverage")).to_have_text("0.9420")
                    lab.locator("#esa-clt-n").fill("1")
                    expect(lab.locator("#esa-clt-error")).to_be_visible()
                    expect(lab.locator("#esa-clt-n")).to_have_attribute("aria-invalid","true")
                    expect(lab.locator("#esa-clt-results")).to_be_hidden()
                    self.fit("main",width)

    def test_arabic_two_group_labs(self):
        for width in (320,375):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":820})
                self.visit(DPROP)
                c=self.page.locator("#esa-two-proportion-ci-calculator")
                expect(c.locator("#esa-prop-lower")).to_have_text("4.6324")
                expect(c.locator("#esa-prop-newcombe-lower")).to_have_text("4.6054")
                expect(c.locator("#esa-prop-zero-interpretation")).to_contain_text("الصفر خارج")
                expect(c.locator("#esa-prop-newcombe-zero")).to_contain_text("نيوكومب")
                c.locator("#esa-prop-x1").fill("5");c.locator("#esa-prop-n1").fill("20")
                expect(c.locator("#esa-prop-warning")).to_contain_text("تنبيه")
                c.locator("#esa-prop-x1").fill("30")
                expect(c.locator("#esa-prop-error")).to_contain_text("استخدم")
                self.fit("#esa-two-proportion-ci-calculator",width)
                self.visit(DMEAN)
                w=self.page.locator("#esa-welch-explorer")
                expect(w.locator("#esa-welch-df")).to_have_text("66.4754")
                expect(w.locator("#esa-welch-lower")).to_have_text("0.8659")
                expect(w.locator("#esa-welch-upper")).to_have_text("11.1341")
                self.fit("main",width)

    def test_new_arabic_lessons_and_chain(self):
        for route,nav in (("/ar"+COND,"/ar/inference/confidence-intervals/ci-for-proportion/"),
                          (DPROP,"/ar/inference/confidence-intervals/ci-for-difference-of-means-independent/"),
                          (DMEAN,"/ar/inference/confidence-intervals/ci-for-difference-of-proportions/"),
                          (MODEL,"/ar/inference/assumptions-robustness/checking-normality-what-and-why/")):
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
        for src,target in (("/ar/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/","/ar"+COND),
                           ("/ar/inference/confidence-intervals/ci-for-proportion/",DMEAN),
                           ("/ar/inference/assumptions-robustness/checking-normality-what-and-why/",MODEL)):
            self.visit(src)
            self.assertGreaterEqual(self.page.locator('main .lesson-nav a[href="%s"]'%target).count(),1,src)

if __name__=="__main__":
    import sys
    unittest.main(argv=[sys.argv[0]])
