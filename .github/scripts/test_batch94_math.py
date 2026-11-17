"""Batch #94: McNemar references, bilingual homogeneity, hardened readers,
LearningResource coverage and no-JavaScript notices."""
import json
import math
import re
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
MCN="js/mcnemar-test-lab.js"
HOM="js/chi-square-homogeneity-explorer.js"

def js(expression,files):
    runner='''const fs=require("fs"),vm=require("vm"),window={},document={getElementById:()=>null};
for(const f of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(f,"utf8"),{window,document});
console.log(JSON.stringify(%s));'''%expression
    p=subprocess.run(["node","-e",runner,*[str(ROOT/f) for f in files]],text=True,capture_output=True,check=True)
    return json.loads(p.stdout)

def exact_mcnemar(b,c):
    # Independent reference: exact rational binomial tail with math.comb.
    n=b+c;m=min(b,c)
    return min(1.0,2*sum(math.comb(n,k) for k in range(m+1))/2**n)

def front_matter(path):
    text=path.read_text(encoding="utf-8")
    head=text.split("---",2)[1] if text.startswith("---") else ""
    return dict(re.findall(r'^([A-Za-z_]+):\s*"?(.*?)"?\s*$',head,re.M))

class McNemar(unittest.TestCase):
    def test_worked_example_matches_scipy(self):
        r=js("window.esaMcNemar.compute([45,5,20,30])",[MCN])
        self.assertEqual((r["n"],r["nd"]),(100,25))
        self.assertAlmostEqual(r["chi"],9,places=12)
        self.assertAlmostEqual(r["chiCC"],7.84,places=12)
        # scipy.stats.chi2.sf(9,1), chi2.sf(7.84,1), binomtest(5,25,.5).pvalue
        self.assertAlmostEqual(r["p"],0.0026997960632601883,delta=1e-14)
        self.assertAlmostEqual(r["pCC"],0.005110260660855866,delta=1e-14)
        self.assertAlmostEqual(r["pExact"],0.004077315330505371,delta=1e-14)
        self.assertAlmostEqual(r["p"],math.erfc(math.sqrt(9/2)),delta=1e-15)
        self.assertAlmostEqual(r["diff"],-0.15,places=12)
    def test_exact_tail_against_rational_reference(self):
        for b,c in [(0,1),(0,3),(1,6),(4,4),(3,10),(7,30),(40,61),(250,300),(1,0)]:
            with self.subTest(b=b,c=c):
                r=js("window.esaMcNemar.compute([3,%d,%d,2])"%(b,c),[MCN])
                self.assertAlmostEqual(r["pExact"],exact_mcnemar(b,c),delta=1e-12)
                self.assertAlmostEqual(r["chi"],(b-c)**2/(b+c),places=12)
                self.assertAlmostEqual(r["chiCC"],max(abs(b-c)-1,0)**2/(b+c),places=12)
                self.assertAlmostEqual(r["p"],math.erfc(math.sqrt(r["chi"]/2)),delta=1e-13)
    def test_concordant_cells_do_not_change_tests(self):
        a=js("window.esaMcNemar.compute([1,7,30,1])",[MCN]);b=js("window.esaMcNemar.compute([900,7,30,4000])",[MCN])
        for k in ("chi","p","chiCC","pCC","pExact"):self.assertEqual(a[k],b[k])
    def test_boundaries(self):
        none=js("window.esaMcNemar.compute([40,0,0,60])",[MCN])
        self.assertTrue(none["noDiscordant"]);self.assertEqual(none["pExact"],1);self.assertIsNone(none["chi"])
        eq=js("window.esaMcNemar.compute([0,4,4,0])",[MCN])
        self.assertEqual((eq["chi"],eq["p"],eq["chiCC"],eq["pExact"]),(0,1,0,1))
        big=js("window.esaMcNemar.compute([0,9999999,10000000,0])",[MCN])
        self.assertEqual(big["pExact"],1);self.assertTrue(0.999<big["p"]<=1)
        huge=js("window.esaMcNemar.compute([0,3000000,3100000,0])",[MCN])
        self.assertLess(huge["pExact"],1e-12)
        for bad in ("[0,0,0,0]","[-1,1,1,1]","[1.5,1,1,1]","[10000001,1,1,1]","[1,2,3]","['1',2,3,4]"):
            self.assertIn("error",js("window.esaMcNemar.compute(%s)"%bad,[MCN]),bad)
        self.assertEqual(js("window.esaMcNemar.compute([0,0,0,0])",[MCN])["error"],"empty")
    def test_lesson_and_links(self):
        page=ROOT/"inference/classical-tests/mcnemar-test/index.md"
        fm=front_matter(page);t=page.read_text()
        self.assertEqual(fm["permalink"],"/inference/classical-tests/mcnemar-test/")
        self.assertEqual(fm["learning_resource"],"true")
        self.assertIn("/js/mcnemar-test-lab.js",t)
        self.assertIn("<noscript>",t)
        self.assertNotIn("innerHTML",(ROOT/MCN).read_text())
        for f in ("inference/classical-tests/paired-t-test/index.md","inference/classical-tests/two-proportion-z-test/index.md",
                  "inference/classical-tests/chi-square-independence-test/index.md","ar/inference/classical-tests/chi-square-independence-test/index.md"):
            # Batch #95 published the Arabic McNemar lesson, so the Arabic page
            # must now link to the Arabic route instead of the English one.
            expected="/ar/inference/classical-tests/mcnemar-test/" if f.startswith("ar/") else "/inference/classical-tests/mcnemar-test/"
            self.assertIn('href="%s"'%expected,(ROOT/f).read_text(),f)

class ArabicHomogeneity(unittest.TestCase):
    def test_shared_engine_and_pair(self):
        src=(ROOT/HOM).read_text()
        self.assertIn('const ar=root.dataset.locale==="ar";',src)
        self.assertNotIn("innerHTML",src)
        r=js("window.esaHomogeneityMath.compute([[40,35,25],[30,45,25],[50,30,20]])",[HOM])
        self.assertAlmostEqual(r["chi"],8.896103896103897,places=12)
        self.assertEqual(r["df"],4)
        self.assertAlmostEqual(r["p"],0.06374950599967244,delta=1e-12)
        ar=ROOT/"ar/inference/classical-tests/chi-square-homogeneity-test/index.md"
        en=ROOT/"inference/classical-tests/chi-square-homogeneity-test/index.md"
        fa,fe=front_matter(ar),front_matter(en)
        self.assertEqual((fa["translation_pair"],fe["translation_pair"]),("chi-square-homogeneity",)*2)
        self.assertEqual(fa["lang"],"ar")
        a=ar.read_text()
        self.assertIn('data-locale="ar"',a)
        self.assertIn('id="esa-hom-input" dir="ltr"',a)
        self.assertIn("/ar/inference/classical-tests/chi-square-homogeneity-test/",(ROOT/"ar/index.md").read_text())
        self.assertIn("/ar/inference/classical-tests/chi-square-homogeneity-test/",en.read_text())
        ind=(ROOT/"ar/inference/classical-tests/chi-square-independence-test/index.md").read_text()
        self.assertIn('href="/ar/inference/classical-tests/chi-square-homogeneity-test/"',ind)
        self.assertNotIn("اختبار كاي تربيع للتجانس (بالإنجليزية)",ind)

READERS={
 "applied-statistics/reporting/index.md":"continue-reading-reporting",
 "applied-statistics/effect-sizes/index.md":"continue-reading-effect-sizes",
 "applied-statistics/common-mistakes/index.md":"continue-reading-common-mistakes",
 "applied-statistics/practice/index.md":"continue-reading-practice",
 "mathematical-statistics/fisher-information-and-efficiency/index.md":"continue-reading-ms-b5",
 "mathematical-statistics/statistical-models/index.md":"continue-reading-ms-b1"}

class HardenedReaders(unittest.TestCase):
    def test_no_html_injection_and_strict_validation(self):
        routes={}
        for path in ROOT.rglob("index.md"):
            fm=front_matter(path)
            if "permalink" in fm:routes[fm["permalink"]]=path.read_text(encoding="utf-8")
        for f,wid in READERS.items():
            with self.subTest(reader=f):
                s=(ROOT/f).read_text()
                self.assertNotIn("innerHTML",s)
                self.assertIn('label.textContent = "You last visited: " + data.label;',s)
                self.assertIn("Number.isSafeInteger(data.ts)",s)
                self.assertIn("Date.now()+5*60*1000",s)
                self.assertIn("Object.prototype.hasOwnProperty.call(ALLOWED, data.url)",s)
                self.assertIn("data.label !== ALLOWED[data.url]",s)
                self.assertIn('id="%s"'%wid,s)
                m=re.search(r"ALLOWED = (\{.*?\});",s,re.S)
                allowed=json.loads(m.group(1))
                key=re.search(r'KEY = "([^"]+)"',s).group(1)
                for url,label in allowed.items():
                    page=routes.get(url)
                    self.assertIsNotNone(page,url)
                    self.assertIn(key,page);self.assertIn(label,page)
                if f.startswith("applied-statistics/"):
                    self.assertEqual(allowed,{})  # no published lessons yet
                else:
                    self.assertEqual(len(allowed),5)

class LearningResourceAndNoscript(unittest.TestCase):
    def test_every_translation_pair_page_is_a_learning_resource(self):
        n=0
        for path in ROOT.rglob("*.md"):
            if any(p.startswith(("_",".")) for p in path.relative_to(ROOT).parts):continue
            fm=front_matter(path)
            if "translation_pair" in fm:
                n+=1
                with self.subTest(page=str(path.relative_to(ROOT))):
                    self.assertEqual(fm.get("learning_resource"),"true")
        self.assertGreaterEqual(n,88)
    def test_chi_square_labs_have_noscript(self):
        for f in ("inference/classical-tests/chi-square-goodness-of-fit/index.md","ar/inference/classical-tests/chi-square-goodness-of-fit/index.md",
                  "inference/classical-tests/chi-square-independence-test/index.md","ar/inference/classical-tests/chi-square-independence-test/index.md",
                  "inference/classical-tests/chi-square-homogeneity-test/index.md","ar/inference/classical-tests/chi-square-homogeneity-test/index.md",
                  "inference/classical-tests/mcnemar-test/index.md"):
            t=(ROOT/f).read_text()
            with self.subTest(page=f):
                self.assertEqual(t.count("<noscript>"),1)
                self.assertIn("JavaScript",t.split("<noscript>")[1].split("</noscript>")[0])

if __name__=="__main__":unittest.main()
