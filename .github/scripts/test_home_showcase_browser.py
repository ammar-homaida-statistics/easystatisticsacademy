"""Homepage Courses and Code Lab tabs: WAI-ARIA keyboard behaviour, the no-JavaScript
fallback, links that resolve, and no horizontal overflow from 320 px to desktop."""
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

class HomeShowcase(unittest.TestCase):
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

    def test_tabs_keyboard_and_mouse(self):
        for width in (320,375,1280):
            with self.subTest(width=width):
                self.page.set_viewport_size({"width":width,"height":900})
                self.visit("/")
                tabs=self.page.get_by_role("tablist",name="Courses and Code Lab")
                expect(tabs).to_be_visible()
                courses=self.page.get_by_role("tab",name="Courses")
                code=self.page.get_by_role("tab",name="Code Lab")
                expect(courses).to_have_attribute("aria-selected","true")
                expect(self.page.get_by_role("tabpanel")).to_have_count(1)
                expect(self.page.locator("#esa-home-panel-courses")).to_be_visible()
                expect(self.page.locator("#esa-home-panel-codelab")).to_be_hidden()
                expect(self.page.locator("#esa-home-panel-courses")).to_have_attribute("aria-labelledby","esa-home-tab-courses")
                courses.focus();self.page.keyboard.press("ArrowRight")
                expect(code).to_be_focused();expect(code).to_have_attribute("aria-selected","true")
                expect(code).to_have_attribute("tabindex","0");expect(courses).to_have_attribute("tabindex","-1")
                expect(self.page.locator("#esa-home-panel-codelab")).to_be_visible()
                expect(self.page.locator("#esa-home-panel-courses")).to_be_hidden()
                self.page.keyboard.press("ArrowRight")
                expect(courses).to_be_focused()
                self.page.keyboard.press("End");expect(code).to_be_focused()
                self.page.keyboard.press("Home");expect(courses).to_be_focused()
                self.page.keyboard.press("ArrowLeft");expect(code).to_be_focused()
                courses.click();expect(courses).to_have_attribute("aria-selected","true")
                expect(self.page.locator("#esa-home-panel-courses a.esa-home-action--dark")).to_have_attribute(
                    "href","/courses/regression/module-1/what-is-regression/")
                for key in ("courses","codelab"):
                    self.page.locator("#esa-home-tab-"+key).click()
                    width_now=self.page.evaluate("()=>document.documentElement.scrollWidth")
                    self.assertLessEqual(width_now,width+1,(key,width_now))

    def test_links_resolve(self):
        self.visit("/")
        hrefs=self.page.evaluate("()=>[...document.querySelectorAll('.esa-home-go a[href]')].map(a=>a.getAttribute('href'))")
        self.assertEqual(len(hrefs),18)  # 3 + 3 actions, 9 regression lessons + 3 Code Lab exercises
        for href in sorted(set(hrefs)):
            with self.subTest(href=href):
                status=self.page.evaluate("u=>fetch(u).then(r=>r.status)",href)
                self.assertEqual(status,200)

    def test_without_javascript_both_panels_show(self):
        ctx=self.browser.new_context(java_script_enabled=False,viewport={"width":320,"height":900})
        page=ctx.new_page()
        try:
            page.goto(self.origin+"/")
            expect(page.locator(".esa-home-tablist")).to_be_hidden()
            expect(page.get_by_role("tablist")).to_have_count(0)
            expect(page.locator("#esa-home-panel-courses")).to_be_visible()
            expect(page.locator("#esa-home-panel-codelab")).to_be_visible()
            expect(page.get_by_role("tabpanel")).to_have_count(0)
            self.assertLessEqual(page.evaluate("()=>document.documentElement.scrollWidth"),321)
        finally:
            ctx.close()

if __name__=="__main__":
    import sys
    unittest.main(argv=[sys.argv[0]])
