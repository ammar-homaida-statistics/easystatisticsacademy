"""Batch #97: Tukey–Kramer and Bonferroni/Holm labs in both languages, Welch's
ANOVA output, the Arabic Fisher–Pearson lab with Yates' correction, and page
width at 320 px for every new or changed page."""
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
POSTHOC="/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/"
ANOVA="/inference/classical-tests/one-way-anova-f-test/"
FISHER="/inference/classical-tests/fisher-exact-vs-chi-square/"

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

class Browser97(unittest.TestCase):
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

    def test_tukey_lab_both_languages(self):
        for route,yes,undefined in ((POSTHOC,"Significant","Undefined"),("/ar"+POSTHOC,"دال","غير معرّف")):
            for width in (320,375):
                with self.subTest(route=route,width=width):
                    self.page.set_viewport_size({"width":width,"height":820})
                    self.visit(route)
                    lab=self.page.locator("#esa-tukey-lab")
                    expect(lab.locator("#esa-tukey-qcrit")).to_have_text("4.3392")
                    rows=lab.locator("#esa-tukey-rows tr")
                    expect(rows).to_have_count(3)
                    expect(rows.nth(0)).to_contain_text("0.482727")
                    expect(rows.nth(1)).to_contain_text("0.006494")
                    expect(rows.nth(1)).to_contain_text("[-6.5052, -1.4948]")
                    expect(rows.nth(1).locator("td").last).to_have_text(yes)
                    self.fit("#esa-tukey-lab",width)
                    lab.locator("#esa-tukey-four").click()
                    expect(rows).to_have_count(6)
                    expect(rows.nth(5)).to_contain_text("0.015099")
                    lab.locator("#esa-tukey-unequal").click()
                    expect(rows.nth(2)).to_contain_text("0.011097")
                    lab.locator("#esa-tukey-input").fill("1, 1\n2, 2\n2, 2")
                    expect(rows.nth(2)).to_contain_text(undefined)  # B − C: 0/0
                    lab.locator("#esa-tukey-input").fill("1, x\n2, 3")
                    expect(lab.locator("#esa-tukey-error")).to_be_visible()
                    expect(lab.locator("#esa-tukey-input")).to_have_attribute("aria-invalid","true")
                    expect(lab.locator("#esa-tukey-results")).to_be_hidden()

    def test_arabic_bonferroni_holm_lab(self):
        self.visit("/ar"+POSTHOC)
        lab=self.page.locator("#esa-multiple-comparisons-lab")
        expect(lab.locator("#esa-mc-rows tr")).to_have_count(4)
        expect(lab.locator("#esa-mc-fwer")).to_have_text("0.185494")
        expect(lab.locator("#esa-mc-summary")).to_contain_text("يرفض إجراء هولم 1 من أصل 4")
        expect(lab.locator("#esa-mc-rows tr").first).to_contain_text("نرفض H₀")
        lab.locator("#esa-mc-values").fill("0.5")
        expect(lab.locator("#esa-mc-error")).to_contain_text("أدخل من 2 إلى 12")
        self.visit(POSTHOC)
        expect(self.page.locator("#esa-mc-summary")).to_contain_text("Holm rejects 1 of 4 hypotheses")

    def test_welch_anova_both_languages(self):
        for route,undefined in ((ANOVA,"Undefined: every group"),("/ar"+ANOVA,"غير معرّف")):
            with self.subTest(route=route):
                self.visit(route)
                lab=self.page.locator("#esa-anova-lab")
                expect(lab.locator("#esa-anova-welch-f")).to_have_text("11.142857")
                expect(lab.locator("#esa-anova-welch-df")).to_have_text("2, 4.0000")
                expect(lab.locator("#esa-anova-welch-p")).to_have_text("0.023157")
                expect(lab.locator("#esa-anova-f")).to_have_text("13.000000")
                lab.locator("#esa-anova-unequal").click()
                expect(lab.locator("#esa-anova-welch-f")).to_have_text("24.517733")
                expect(lab.locator("#esa-anova-welch-df")).to_have_text("2, 4.4685")
                lab.locator("#esa-anova-constant").click()
                expect(lab.locator("#esa-anova-welch-f")).to_contain_text(undefined)
                expect(lab.locator("#esa-anova-welch-p")).to_have_text("—")

    def test_fisher_lab_both_languages(self):
        for route,word in ((FISHER,"expected cell counts"),("/ar"+FISHER,"التكرارات المتوقعة")):
            for width in (320,375):
                with self.subTest(route=route,width=width):
                    self.page.set_viewport_size({"width":width,"height":820})
                    self.visit(route)
                    lab=self.page.locator("#esa-fisher-chi-lab")
                    expect(lab.locator("#esa-fc-fisher")).to_have_text("0.002759")
                    expect(lab.locator("#esa-fc-pearson")).to_have_text("0.000925")
                    expect(lab.locator("#esa-fc-yates")).to_have_text("0.003752")
                    expect(lab.locator("#esa-fc-warning")).to_contain_text(word)
                    lab.locator("#esa-fc-a").fill("50");lab.locator("#esa-fc-b").fill("5")
                    lab.locator("#esa-fc-c").fill("5");lab.locator("#esa-fc-d").fill("50")
                    expect(lab.locator("#esa-fc-pearson")).to_have_text("9.3918e-18")
                    expect(lab.locator("#esa-fc-yates")).to_have_text("4.8420e-17")
                    lab.locator("#esa-fc-a").fill("-1")
                    expect(lab.locator("#esa-fc-error")).to_be_visible()
                    lab.locator("#esa-fc-reset").click()
                    expect(lab.locator("#esa-fc-fisher")).to_have_text("0.002759")
                    self.fit("#esa-fisher-chi-lab",width)

    def test_new_and_changed_pages_fit_320(self):
        self.page.set_viewport_size({"width":320,"height":820})
        for route in (POSTHOC,"/ar"+POSTHOC,ANOVA,"/ar"+ANOVA,FISHER,"/ar"+FISHER,"/ar/"):
            with self.subTest(route=route):
                self.visit(route)
                self.fit("main",320)

    def test_arabic_home_links_new_lessons(self):
        self.visit("/ar/")
        for slug in ("post-hoc-tests-and-multiple-comparisons-preview","one-way-anova-f-test","cohens-kappa","fisher-exact-vs-chi-square"):
            expect(self.page.locator('main a[href="/ar/inference/classical-tests/%s/"]'%slug)).to_have_count(1)

if __name__=="__main__":
    import sys
    unittest.main(argv=[sys.argv[0]])
