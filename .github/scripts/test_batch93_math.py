"""Batch #93: independent chi-square references, translation-pair consistency,
Continue Reading hardening and Node 24 Pages actions."""
import json
import math
import re
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def js(expression,files):
    runner='''const fs=require("fs"),vm=require("vm"),window={},document={getElementById:()=>null};
for(const f of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(f,"utf8"),{window,document});
console.log(JSON.stringify(%s));'''%expression
    p=subprocess.run(["node","-e",runner,*[str(ROOT/f) for f in files]],text=True,capture_output=True,check=True)
    return json.loads(p.stdout)

def chi2_sf_df1(x):
    # Independent reference: P(chi2_1 >= x) = erfc(sqrt(x/2)).
    return math.erfc(math.sqrt(x/2))

def front_matter(path):
    text=path.read_text(encoding="utf-8")
    if not text.startswith("---"):return {}
    head=text.split("---",2)[1]
    out={}
    for line in head.splitlines():
        m=re.match(r'^([A-Za-z_]+):\s*"?(.*?)"?\s*$',line)
        if m:out[m.group(1)]=m.group(2)
    return out

def translations():
    # Minimal parser for the flat list in _data/translations.yml.
    items=[];cur=None
    for line in (ROOT/"_data/translations.yml").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):continue
        m=re.match(r'^-\s+id:\s*(\S+)\s*$',line)
        if m:
            cur={"id":m.group(1)};items.append(cur);continue
        m=re.match(r'^\s+(en|ar):\s*(\S+)\s*$',line)
        assert m and cur is not None,line
        cur[m.group(1)]=m.group(2)
    return items

ENGINE="js/chi-square-independence-2x2.js"

class Batch93Math(unittest.TestCase):
    def test_shared_2x2_engine_matches_hand_calculation(self):
        r=js("window.esaChiIndependence2x2.compute([40,60,70,30])",[ENGINE])
        self.assertEqual(r["expected"],[55,45,55,45])
        self.assertAlmostEqual(r["chi"],200/11,places=12)
        self.assertEqual(r["df"],1)
        # scipy.stats.chi2.sf(200/11,1)=2.007865612426481e-05.
        self.assertAlmostEqual(r["p"],2.007865612426481e-05,delta=1e-15)
        self.assertAlmostEqual(r["p"],chi2_sf_df1(200/11),delta=1e-15)
        self.assertAlmostEqual(r["v"],math.sqrt(200/11/200),places=12)
        self.assertEqual(r["small"],0)
    def test_shared_engine_tail_accuracy_and_boundaries(self):
        for table in ([1,0,0,1],[500,10,10,500],[3,7,9,2],[10,10,10,10],[0,5,5,0],[10000000,1,1,10000000]):
            r=js("window.esaChiIndependence2x2.compute(%s)"%json.dumps(table),[ENGINE])
            a,b,c,d=table;n=a+b+c+d
            chi=n*(a*d-b*c)**2/((a+b)*(c+d)*(a+c)*(b+d))
            self.assertAlmostEqual(r["chi"],chi,delta=1e-9*max(1,chi))
            ref=chi2_sf_df1(chi)
            if ref>1e-300:
                self.assertLess(abs(r["p"]-ref),1e-12+1e-9*ref,(table,r["p"],ref))
            self.assertTrue(0<=r["p"]<=1)
        self.assertEqual(js("window.esaChiIndependence2x2.compute([5,5,5,5])",[ENGINE])["p"],1)
        for bad in ("[0,0,3,4]","[0,3,0,4]","[0,0,0,0]","[-1,2,3,4]","[1.5,2,3,4]",
                    "[10000001,1,1,1]","[1,2,3]","[1,2,3,NaN]","['1',2,3,4]"):
            self.assertIn("error",js("window.esaChiIndependence2x2.compute(%s)"%bad,[ENGINE]),bad)
        self.assertEqual(js("window.esaChiIndependence2x2.compute([0,0,3,4])",[ENGINE])["error"],"margin")
    def test_homogeneity_adjusted_residuals(self):
        r=js("window.esaHomogeneityMath.compute([[40,35,25],[30,45,25],[50,30,20]])",
             ["js/chi-square-homogeneity-explorer.js"])
        # Independent: scipy.stats.chi2_contingency expected E and
        # (O-E)/sqrt(E(1-R/N)(1-C/N)), computed separately in NumPy.
        ref=[[0.0,-0.423587,0.482617],[-2.5,2.117934,0.482617],[2.5,-1.694347,-0.965234]]
        for row,rr in zip(r["adjusted"],ref):
            for v,w in zip(row,rr):self.assertAlmostEqual(v,w,places=5)
        O=[[40,35,25],[30,45,25],[50,30,20]];N=300
        R=[sum(x) for x in O];C=[sum(col) for col in zip(*O)]
        for i in range(3):
            for j in range(3):
                E=R[i]*C[j]/N
                self.assertAlmostEqual(r["adjusted"][i][j],(O[i][j]-E)/math.sqrt(E*(1-R[i]/N)*(1-C[j]/N)),places=12)
        # In a 2x2 table every adjusted residual has |r| = sqrt(chi-square).
        t=js("window.esaHomogeneityMath.compute([[40,60],[70,30]])",["js/chi-square-homogeneity-explorer.js"])
        for v in sum(t["adjusted"],[]):self.assertAlmostEqual(abs(v),math.sqrt(t["chi"]),places=10)
        self.assertIsNone(js("window.esaHomogeneityMath.compute([[0,0],[3,4]])",["js/chi-square-homogeneity-explorer.js"]))
        page=(ROOT/"inference/classical-tests/chi-square-homogeneity-test/index.md").read_text()
        self.assertIn('id="esa-hom-residuals"',page)
        self.assertIn("not a set of independent tests",page)
    def test_arabic_independence_lesson_and_links(self):
        en=ROOT/"inference/classical-tests/chi-square-independence-test/index.md"
        ar=ROOT/"ar/inference/classical-tests/chi-square-independence-test/index.md"
        fen,far=front_matter(en),front_matter(ar)
        self.assertEqual(fen["translation_pair"],"chi-square-independence")
        self.assertEqual(far["translation_pair"],"chi-square-independence")
        self.assertEqual(far["lang"],"ar")
        self.assertEqual(far["permalink"],"/ar/inference/classical-tests/chi-square-independence-test/")
        a=ar.read_text();e=en.read_text()
        self.assertIn('data-locale="ar"',a)
        self.assertIn("/js/chi-square-independence-2x2.js",a)
        self.assertIn("chi-square-independence-2x2.js",e)
        self.assertNotIn("function erfc",e)
        for i in "abcd":self.assertIn('id="esa-chi-%s" dir="ltr"'%i,a)
        self.assertIn("/ar/inference/classical-tests/chi-square-independence-test/",e)
        self.assertIn("/ar/inference/classical-tests/chi-square-independence-test/",(ROOT/"ar/index.md").read_text())
        gof=(ROOT/"ar/inference/classical-tests/chi-square-goodness-of-fit/index.md").read_text()
        self.assertIn('href="/ar/inference/classical-tests/chi-square-independence-test/"',gof)
        self.assertNotIn("اختبار الاستقلال (بالإنجليزية)",gof)
        engine=(ROOT/ENGINE).read_text()
        self.assertIn('root.dataset.locale === "ar"',engine)
        self.assertNotIn("innerHTML",engine)

class Batch93TranslationPairs(unittest.TestCase):
    def test_every_pair_is_complete_reciprocal_and_declared(self):
        pages={}
        for path in ROOT.rglob("*.md"):
            if any(part.startswith(("_",".")) for part in path.relative_to(ROOT).parts):continue
            fm=front_matter(path)
            if "translation_pair" in fm:
                pages.setdefault(fm["translation_pair"],[]).append(fm)
        data={item["id"]:item for item in translations()}
        self.assertEqual(len(data),len(translations()),"duplicate ids")
        self.assertEqual(set(pages),set(data))
        self.assertGreaterEqual(len(data),43)
        layout=(ROOT/"_layouts/default.html").read_text()
        for pid,item in data.items():
            with self.subTest(pair=pid):
                fms=pages[pid]
                self.assertEqual(len(fms),2)
                by_lang={fm.get("lang","en"):fm["permalink"] for fm in fms}
                self.assertEqual(by_lang,{"en":item["en"],"ar":item["ar"]})
                self.assertTrue(item["ar"].startswith("/ar/"))
                branch=re.search(r'translation_pair == "%s" %%\}\s*<link rel="alternate" hreflang="en" href="\{\{ site.url \}\}([^"]+)" />\s*<link rel="alternate" hreflang="ar" href="\{\{ site.url \}\}([^"]+)" />'%re.escape(pid),layout)
                self.assertIsNotNone(branch,"missing hreflang branch")
                self.assertEqual(branch.groups(),(item["en"],item["ar"]))
        self.assertIn('hreflang="x-default"',layout)
        sitemap=(ROOT/"sitemap.xml").read_text()
        self.assertIn('xmlns:xhtml="http://www.w3.org/1999/xhtml"',sitemap)
        self.assertIn("site.data.translations",sitemap)
    def test_previously_missing_pairs_now_have_hreflang(self):
        layout=(ROOT/"_layouts/default.html").read_text()
        for pid in ("tree-diagrams","base-rate-neglect-and-fallacies","chi-square-independence"):
            self.assertIn('page.translation_pair == "%s"'%pid,layout)

READERS=["modeling/assumptions/index.md","modeling/model-fit-comparison/index.md",
 "modeling/foundations/index.md","mathematical-statistics/alternative-estimation-methods/index.md",
 "mathematical-statistics/estimator-properties/index.md","mathematical-statistics/asymptotic-theory/index.md",
 "mathematical-statistics/likelihood-and-log-likelihood/index.md",
 "mathematical-statistics/maximum-likelihood-estimation/index.md"]

class Batch93ContinueReading(unittest.TestCase):
    def test_readers_require_safe_integer_non_future_timestamps(self):
        for f in READERS:
            with self.subTest(reader=f):
                s=(ROOT/f).read_text()
                self.assertRegex(s,r"Number\.isSafeInteger\((data|value)\.ts\)")
                self.assertNotRegex(s,r"Number\.isFinite\((data|value)\.ts\)")
                self.assertNotIn("86400000",s)
                self.assertRegex(s,r"(data|value)\.ts\s*<=\s*0")
                self.assertIn("Date.now()+5*60*1000",s)
                self.assertIn("textContent",s)
                self.assertNotRegex(s,r"label\.innerHTML")
    def test_every_allowlisted_lesson_writes_the_section_key(self):
        routes={}
        for path in ROOT.rglob("index.md"):
            fm=front_matter(path)
            if "permalink" in fm:routes[fm["permalink"]]=path.read_text(encoding="utf-8")
        for f in READERS:
            s=(ROOT/f).read_text()
            keys=[k for k in re.findall(r'(?:KEY|key)\s*=\s*"([^"]+)"',s) if "last_block" not in k]
            m=re.search(r'(?:ALLOWED|lessons|allowed)\s*=\s*\{(.*?)\};',s,re.S)
            self.assertIsNotNone(m,f)
            allowed=dict(re.findall(r'"(/[^"]+/)"\s*:\s*"([^"]+)"',m.group(1)))
            self.assertGreaterEqual(len(allowed),3,f)
            for url,label in allowed.items():
                with self.subTest(reader=f,lesson=url):
                    page=routes.get(url)
                    self.assertIsNotNone(page,"allowlisted route is not a published page")
                    self.assertTrue(any(k in page for k in keys),"lesson does not write the section key")
                    self.assertIn(label,page)
                    self.assertIn("Date.now()",page)

class Batch93PagesActions(unittest.TestCase):
    def test_pages_actions_use_node24_majors(self):
        y=(ROOT/".github/workflows/publish-pages.yml").read_text()
        for new in ("actions/configure-pages@v6","actions/upload-pages-artifact@v5","actions/deploy-pages@v5"):
            self.assertIn(new,y)
        for old in ("configure-pages@v5","upload-pages-artifact@v4","deploy-pages@v4"):
            self.assertNotIn(old,y)
        self.assertIn('--expected-sha "$GITHUB_SHA"',y)
        self.assertLess(y.index("actions/deploy-pages@v5"),y.index("Verify live pages and assets"))

if __name__=="__main__":unittest.main()
