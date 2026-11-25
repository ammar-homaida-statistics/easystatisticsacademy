"""Batch #102: Arabic CI–test and heteroscedasticity labs, new Arabic lessons, and the
built llms.txt index."""
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
CID="/ar/inference/hypothesis-testing/ci-and-test-connection/"
HET="/ar/inference/assumptions-robustness/heteroscedasticity-variance-issues/"
WHAT="/ar/inference/hypothesis-testing/what-is-a-hypothesis-test/"
CRIT="/ar/inference/confidence-intervals/critical-values-z-and-t/"

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

class Browser102(unittest.TestCase):
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

    def test_arabic_duality_lab(self):
        for width in (320,375):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":820})
                self.visit(CID)
                lab=self.page.locator("#esa-cid-lab")
                expect(lab.locator("#esa-cid-crit")).to_have_text("t(24) = 2.0639")
                expect(lab.locator("#esa-cid-p")).to_have_text("0.020981")
                expect(lab.locator("#esa-cid-inside")).to_have_text("لا — μ₀ خارج الفترة")
                expect(lab.locator("#esa-cid-decision")).to_have_text("نرفض H₀ عند α = 0.05 (p < α)")
                expect(lab.locator("#esa-cid-agree")).to_have_text("الفترة والاختبار متفقان.")
                self.fit("#esa-cid-lab",width)
                lab.locator("#esa-cid-inside-ex").click()
                expect(lab.locator("#esa-cid-inside")).to_have_text("نعم — μ₀ داخل الفترة")
                expect(lab.locator("#esa-cid-p")).to_have_text("0.228678")
                lab.locator("#esa-cid-example").click()
                lab.locator("#esa-cid-boundary").click()
                expect(lab.locator("#esa-cid-p")).to_have_text("0.050000")
                expect(lab.locator("#esa-cid-decision")).to_contain_text("لا نرفض")
                lab.locator("#esa-cid-n").fill("1")
                expect(lab.locator("#esa-cid-error")).to_contain_text("أدخل")
                expect(lab.locator("#esa-cid-results")).to_be_hidden()
                self.fit("main",width)

    def test_arabic_levene_lab(self):
        for width in (320,375):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":820})
                self.visit(HET)
                lab=self.page.locator("#esa-lv-lab")
                expect(lab.locator("#esa-lv-w")).to_have_text("16.2618")
                expect(lab.locator("#esa-lv-p")).to_have_text("0.000175")
                expect(lab.locator("#esa-lv-decision")).to_contain_text("توجد أدلة على اختلاف التباينات")
                self.fit("#esa-lv-lab",width)
                lab.locator("#esa-lv-outlier").click()
                lab.locator("#esa-lv-center").select_option("mean")
                expect(lab.locator("#esa-lv-w")).to_have_text("4.6904")
                expect(lab.locator("#esa-lv-p")).to_have_text("0.031257")
                lab.locator("#esa-lv-input").fill("1\n2, 3")
                expect(lab.locator("#esa-lv-error")).to_contain_text("أدخل")
                self.fit("main",width)

    def test_new_arabic_lessons(self):
        for route,nav in ((WHAT,"/ar/inference/hypothesis-testing/null-and-alternative/"),
                          (CID,"/ar/inference/hypothesis-testing/one-sided-vs-two-sided/"),
                          (HET,"/ar/inference/assumptions-robustness/outliers-and-influence/"),
                          (CRIT,"/inference/confidence-intervals/ci-for-mean-sigma-known-z/")):
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
        for src,target in (("/ar/inference/hypothesis-testing/null-and-alternative/",WHAT),
                           ("/ar/inference/hypothesis-testing/one-sided-vs-two-sided/",CID),
                           ("/ar/inference/assumptions-robustness/outliers-and-influence/",HET)):
            self.visit(src)
            self.assertGreaterEqual(self.page.locator('main a[href="%s"]'%target).count(),1,src)

    def test_llms_txt_built(self):
        path=args.site/"llms.txt"
        text=path.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Easy Statistics Academy\n"))
        self.assertNotIn("{%",text);self.assertNotIn("{{",text)
        links=re.findall(r'^- \[([^\]]+)\]\((https://easystatisticsacademy\.com(/[^)]*))\)',text,re.M)
        self.assertGreater(len(links),300)
        en=text.split("## الدروس العربية")[0];ar=text.split("## الدروس العربية")[1]
        self.assertTrue(all(not u.startswith("/ar/") for _,_,u in re.findall(r'^- \[([^\]]+)\]\((https://easystatisticsacademy\.com(/[^)]*))\)',en,re.M)))
        self.assertTrue(all(u.startswith("/ar/") for _,_,u in re.findall(r'^- \[([^\]]+)\]\((https://easystatisticsacademy\.com(/[^)]*))\)',ar,re.M)))
        urls=[u for _,_,u in links]
        self.assertEqual(len(urls),len(set(urls)))
        for u in urls:
            self.assertFalse(u.startswith(("/courses/","/code-lab/","/ar/courses/","/ar/code-lab/")),u)
            self.assertTrue((args.site/u.strip("/")/"index.html").is_file(),u)
        for u in (CID,HET,WHAT,CRIT,"/inference/hypothesis-testing/ci-and-test-connection/"):self.assertIn(u,urls)
        for line in text.splitlines():
            if line.strip():self.assertRegex(line,r'^(# |> |- |## |### )',line)
        r=self.page.request.get(self.origin+"/llms.txt")
        self.assertEqual(r.status,200)

if __name__=="__main__":
    import sys
    unittest.main(argv=[sys.argv[0]])
