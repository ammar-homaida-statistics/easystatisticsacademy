"""Batch #96: Arabic ANOVA and kappa labs, weighted kappa in both languages,
header language switcher for every published pair, the Arabic header, and
rendered no-JavaScript notices."""
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
EN_KAPPA="/inference/classical-tests/cohens-kappa/"
EN_ANOVA="/inference/classical-tests/one-way-anova-f-test/"

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

class Browser96(unittest.TestCase):
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

    def test_language_switcher_for_every_pair(self):
        """Static HTML: every published pair links to its exact counterpart, both directions."""
        data=pairs();self.assertGreaterEqual(len(data),48)
        for p in data:
            for lang in ("en","ar"):
                html=(args.site/p[lang].strip("/")/"index.html").read_text(encoding="utf-8")
                group=re.search(r'<div role="group" aria-label="([^"]+)"[^>]*>(.*?)</div>',html,re.S)
                with self.subTest(pair=p["id"],lang=lang):
                    self.assertIsNotNone(group)
                    links=dict((l,h) for h,l in re.findall(r'<a href="([^"]+)" lang="(en|ar)"',group.group(2)))
                    self.assertEqual(links,{"en":p["en"],"ar":p["ar"]})
                    self.assertIn('aria-current="true"',group.group(2))
                    self.assertIn("Language selection",group.group(1))

    def test_switcher_and_arabic_header_in_browser(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            self.visit("/ar"+EN_KAPPA)
            self.page.get_by_role("button",name="فتح القائمة أو إغلاقها").click()
            nav=self.page.get_by_role("navigation",name="التنقل الرئيسي")
            expect(nav.get_by_role("link",name="الرئيسية")).to_have_attribute("href","/ar/")
            group=self.page.get_by_role("group",name="Language selection")
            expect(group.locator('a[lang="en"]')).to_have_attribute("href",EN_KAPPA)
            expect(self.page.get_by_role("searchbox",name="ابحث في دروس الإحصاء")).to_have_attribute("placeholder","ابحث في الموضوعات…")
            expect(self.page.locator(".skip-link")).to_have_text("انتقل إلى المحتوى الرئيسي")
            self.fit(".site-header",width)
            group.locator('a[lang="en"]').click()
            self.page.wait_for_load_state("networkidle")
            self.assertTrue(self.page.url.endswith(EN_KAPPA))
            expect(self.page.locator("html")).to_have_attribute("lang","en")
            expect(self.page.get_by_role("navigation",name="Primary navigation").get_by_role("link",name="Home")).to_have_attribute("href","/")
            # A pair outside the nine hand-written branches that existed before Batch #96.
            self.visit("/inference/classical-tests/mcnemar-test/")
            expect(self.page.get_by_role("group",name="Language selection").locator('a[lang="ar"]')).to_have_attribute("href","/ar/inference/classical-tests/mcnemar-test/")
            # An English page without a pair keeps the old behaviour.
            self.visit("/descriptive/spread/variance/")
            expect(self.page.get_by_role("group",name="Language selection").locator("a")).to_have_count(1)

    def test_arabic_toc_and_search_messages(self):
        self.visit("/ar/inference/classical-tests/one-way-anova-f-test/")
        toc=self.page.get_by_role("navigation",name="في هذه الصفحة")
        expect(toc).to_have_count(1)
        box=self.page.locator("#site-search")
        self.page.get_by_role("button",name="فتح القائمة أو إغلاقها").evaluate("e=>e.offsetParent")  # header rendered
        box.fill("zzqqxxnotaword")
        expect(self.page.locator("#search-status")).to_have_text("لم يُعثر على نتائج.")

    def test_arabic_anova_lab(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            self.visit("/ar"+EN_ANOVA)
            lab=self.page.locator("#esa-anova-lab")
            expect(lab.locator("#esa-anova-f")).to_have_text("13.000000")
            expect(lab.locator("#esa-anova-p")).to_have_text("0.006592")
            expect(lab.locator("#esa-anova-decision")).to_contain_text("نرفض تساوي")
            expect(lab.locator("#esa-anova-chart text").first).to_contain_text("المجموعة")
            self.fit("#esa-anova-lab",width)
            lab.locator("#esa-anova-constant").click()
            expect(lab.locator("#esa-anova-f")).to_have_text("∞")
            lab.locator("#esa-anova-equal").click()
            expect(lab.locator("#esa-anova-f")).to_have_text("0.000000")
            expect(lab.locator("#esa-anova-decision")).to_contain_text("لا نرفض")
            lab.locator("#esa-anova-a").fill("1, x")
            expect(lab.locator("#esa-anova-error")).to_be_visible()
            expect(lab.locator("#esa-anova-error")).to_contain_text("أدخل")
            expect(lab.locator("#esa-anova-a")).to_have_attribute("aria-invalid","true")
        self.visit(EN_ANOVA)  # English output is unchanged by the shared strings
        expect(self.page.locator("#esa-anova-decision")).to_contain_text("At α=0.05, reject equality")
        expect(self.page.locator("#esa-anova-chart text").first).to_have_text("Group A")

    def test_weighted_kappa_both_languages(self):
        for route,undefined in ((EN_KAPPA,"Not defined for weighted kappa"),("/ar"+EN_KAPPA,"لا ينطبق على كابا الموزونة")):
            for width in (320,375):
                with self.subTest(route=route,width=width):
                    self.page.set_viewport_size({"width":width,"height":820})
                    self.visit(route)
                    lab=self.page.locator("#esa-kappa-lab")
                    expect(lab.locator("#esa-kappa-ci")).to_have_text("[0.1511, 0.6489]")
                    lab.locator("#esa-kappa-three").click()
                    expect(lab.locator("#esa-kappa-kappa")).to_have_text("0.7198")
                    lab.locator("#esa-kappa-weights").select_option("linear")
                    expect(lab.locator("#esa-kappa-kappa")).to_have_text("0.7715")
                    expect(lab.locator("#esa-kappa-se")).to_have_text("0.0609")
                    expect(lab.locator("#esa-kappa-kmax")).to_have_text(undefined)
                    lab.locator("#esa-kappa-weights").select_option("quadratic")
                    expect(lab.locator("#esa-kappa-kappa")).to_have_text("0.8241")
                    expect(lab.locator("#esa-kappa-ci")).to_have_text("[0.7136, 0.9347]")
                    lab.locator("#esa-kappa-example").click()  # two categories: weights coincide
                    expect(lab.locator("#esa-kappa-kappa")).to_have_text("0.4000")
                    lab.locator("#esa-kappa-weights").select_option("none")
                    expect(lab.locator("#esa-kappa-kmax")).to_have_text("0.8000")
                    self.fit("#esa-kappa-lab",width)

    def test_noscript_notices_render_once(self):
        ctx=self.browser.new_context(java_script_enabled=False,viewport={"width":320,"height":820})
        page=ctx.new_page()
        try:
            for route,needle in (("/descriptive/visualization/histograms/","JavaScript"),
                                 ("/inference/classical-tests/paired-t-test/","JavaScript"),
                                 ("/ar/probability/distributions/binomial-distribution/","JavaScript"),
                                 ("/ar"+EN_ANOVA,"JavaScript")):
                page.goto(self.origin+route)
                note=page.locator("p.esa-noscript")
                expect(note).to_have_count(1)
                expect(note).to_be_visible()
                expect(note).to_contain_text(needle)
                if route.startswith("/ar/"):expect(note).to_contain_text("مختبر تفاعلي")
        finally:
            ctx.close()

if __name__=="__main__":
    import sys
    unittest.main(argv=[sys.argv[0]])
