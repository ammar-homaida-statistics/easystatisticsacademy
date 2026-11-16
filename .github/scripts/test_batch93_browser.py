"""Batch #93: bilingual 2x2 independence explorer, adjusted residuals,
Continue Reading tampering, hreflang output and sitemap alternates."""
import argparse
import re
import threading
import unittest
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from xml.etree import ElementTree
from playwright.sync_api import sync_playwright, expect

ap=argparse.ArgumentParser()
ap.add_argument("--site",type=Path,default=Path("_site"))
args,_=ap.parse_known_args()
ROOT=Path(__file__).resolve().parents[2]
BASE="https://easystatisticsacademy.com"
EN="/inference/classical-tests/chi-square-independence-test/"
AR="/ar/inference/classical-tests/chi-square-independence-test/"

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*a):pass

class Browser93(unittest.TestCase):
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

    def test_bilingual_independence_explorer_parity(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            for lang,route in (("en",EN),("ar",AR)):
                with self.subTest(width=width,lang=lang):
                    self.visit(route)
                    expect(self.page.locator("html")).to_have_attribute("lang",lang)
                    if lang=="ar":expect(self.page.locator("html")).to_have_attribute("dir","rtl")
                    for locale,path in (("en",EN),("ar",AR),("x-default",EN)):
                        expect(self.page.locator('link[rel="alternate"][hreflang="'+locale+'"]')).to_have_attribute("href",BASE+path)
                    lab=self.page.locator("#esa-chi-independence-lab")
                    self.fit("#esa-chi-independence-lab",width)
                    expect(lab.locator("#esa-chi-stat")).to_have_text("18.181818")
                    expect(lab.locator("#esa-chi-p")).to_have_text("2.008e-5")
                    expect(lab.locator("#esa-chi-v")).to_have_text("0.301511")
                    expect(lab.locator("#esa-chi-cell-a")).to_have_text("40 → 55.000; 4.0909")
                    lab.locator("#esa-chi-a").fill("1.5")
                    expect(lab.locator("#esa-chi-error")).to_be_visible()
                    expect(lab.locator("#esa-chi-a")).to_have_attribute("aria-invalid","true")
                    expect(lab.locator("#esa-chi-stat")).to_have_text("—")
                    lab.locator("#esa-chi-a").fill("0");lab.locator("#esa-chi-c").fill("0")
                    err=lab.locator("#esa-chi-error").inner_text()
                    self.assertIn("الهوامش" if lang=="ar" else "zero margins",err)
                    lab.locator("#esa-chi-reset").focus();self.page.keyboard.press("Enter")
                    expect(lab.locator("#esa-chi-error")).to_be_hidden()
                    expect(lab.locator("#esa-chi-a")).to_have_attribute("aria-invalid","false")
                    lab.locator("#esa-chi-a").fill("2");lab.locator("#esa-chi-b").fill("3")
                    warn=lab.locator("#esa-chi-warning").inner_text()
                    self.assertIn("فيشر" if lang=="ar" else "Fisher",warn)
                    if lang=="ar":
                        self.assertIn("كرامر",self.page.locator("main").inner_text())

    def test_homogeneity_adjusted_residuals_table(self):
        for width in (320,375):
            self.page.set_viewport_size({"width":width,"height":820})
            self.visit("/inference/classical-tests/chi-square-homogeneity-test/")
            self.fit("#esa-homogeneity-lab",width)
            table=self.page.locator("#esa-hom-residuals")
            expect(table.locator("caption")).to_contain_text("Adjusted standardized residuals")
            expect(table.locator("tbody tr")).to_have_count(3)
            self.assertIn("-2.500",table.inner_text())
            self.assertEqual(table.locator("td.esa-hom-flag").count(),3)
            expect(self.page.locator("#esa-hom-residual-note")).to_contain_text("3 of 9 cells")
            self.page.locator("#esa-hom-balanced").focus();self.page.keyboard.press("Enter")
            expect(self.page.locator("#esa-hom-residual-note")).to_contain_text("No cell has |r| > 2")
            self.page.locator("#esa-hom-input").fill("0, 0\n3, 4")
            expect(self.page.locator("#esa-hom-error")).to_be_visible()

    def test_hardened_readers_reject_tampering(self):
        readers=["modeling/assumptions/index.md","modeling/model-fit-comparison/index.md",
          "modeling/foundations/index.md","mathematical-statistics/alternative-estimation-methods/index.md",
          "mathematical-statistics/estimator-properties/index.md","mathematical-statistics/asymptotic-theory/index.md",
          "mathematical-statistics/likelihood-and-log-likelihood/index.md",
          "mathematical-statistics/maximum-likelihood-estimation/index.md"]
        for f in readers:
            src=(ROOT/f).read_text(encoding="utf-8")
            route=re.search(r"^permalink:\s*(\S+)",src,re.M).group(1)
            key=[k for k in re.findall(r'(?:KEY|key)\s*=\s*"([^"]+)"',src) if "last_block" not in k][0]
            allowed=dict(re.findall(r'"(/[^"]+/)"\s*:\s*"([^"]+)"',
                re.search(r'(?:ALLOWED|lessons|allowed)\s*=\s*\{(.*?)\};',src,re.S).group(1)))
            wrap=[w for w in re.findall(r'getElementById\("(continue-reading-[^"]+)"\)',src)
                  if not w.endswith(("-label","-btn"))][0]
            url,label=next(iter(allowed.items()))
            with self.subTest(reader=f):
                self.visit(route)
                pane=self.page.locator("#"+wrap)
                now=self.page.evaluate("Date.now()")
                valid={"url":url,"label":label,"ts":now}
                def save(value):
                    self.page.evaluate("([k,v])=>{for(const x of Object.keys(localStorage))if(x.startsWith('esa_continue_'))localStorage.removeItem(x);localStorage.setItem(k,JSON.stringify(v))}",[key,value])
                    self.page.reload(wait_until="networkidle")
                save(valid)
                expect(pane).to_be_visible()
                for bad in ({**valid,"ts":now+2*3600*1000},{**valid,"ts":now+0.5},{**valid,"ts":-1},
                            {**valid,"ts":0},{**valid,"ts":"1"},{**valid,"url":"javascript:alert(1)"},
                            {**valid,"url":url+"?x=1"},{**valid,"label":"<img src=x onerror=alert(1)>"}):
                    save(bad)
                    expect(pane).to_be_hidden()

    def test_previously_missing_hreflang_and_sitemap_alternates(self):
        for en,ar in (("/probability/conditional/tree-diagrams/","/ar/probability/conditional/tree-diagrams/"),
                      ("/probability/conditional/base-rate-neglect-and-fallacies/","/ar/probability/conditional/base-rate-neglect-and-fallacies/")):
            for route in (en,ar):
                with self.subTest(route=route):
                    html=(args.site/route.strip("/")/"index.html").read_text(encoding="utf-8")
                    for locale,path in (("en",en),("ar",ar),("x-default",en)):
                        self.assertIn('<link rel="alternate" hreflang="%s" href="%s%s" />'%(locale,BASE,path),html)
        root=ElementTree.fromstring((args.site/"sitemap.xml").read_text(encoding="utf-8"))
        ns={"s":"http://www.sitemaps.org/schemas/sitemap/0.9","x":"http://www.w3.org/1999/xhtml"}
        alt={}
        for u in root.findall("s:url",ns):
            loc=u.find("s:loc",ns).text
            links={l.get("hreflang"):l.get("href") for l in u.findall("x:link",ns)}
            if links:alt[loc]=links
        self.assertGreaterEqual(len(alt),86)
        for loc,links in alt.items():
            self.assertEqual(set(links),{"en","ar","x-default"},loc)
            self.assertIn(loc,(links["en"],links["ar"]))
            self.assertEqual(links["x-default"],links["en"])
            self.assertEqual(alt.get(links["en"]),links,loc)
            self.assertEqual(alt.get(links["ar"]),links,loc)

if __name__=="__main__":unittest.main(argv=[__file__])
