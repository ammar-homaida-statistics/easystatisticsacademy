"""Batch #95: Cohen's kappa references, bilingual McNemar, classical-tests hubs
and site-wide no-JavaScript coverage for lab pages."""
import json
import math
import re
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
KAPPA="js/cohens-kappa-lab.js"
MCN="js/mcnemar-test-lab.js"

def js(expression,files):
    runner='''const fs=require("fs"),vm=require("vm"),window={},document={getElementById:()=>null};
for(const f of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(f,"utf8"),{window,document});
console.log(JSON.stringify(%s));'''%expression
    p=subprocess.run(["node","-e",runner,*[str(ROOT/f) for f in files]],text=True,capture_output=True,check=True)
    return json.loads(p.stdout)

def kappa_reference(t):
    """Independent pure-Python Cohen's kappa and Fleiss-Cohen-Everitt SE."""
    k=len(t);N=sum(map(sum,t));p=[[v/N for v in row] for row in t]
    r=[sum(row) for row in p];c=[sum(p[i][j] for i in range(k)) for j in range(k)]
    po=sum(p[i][i] for i in range(k));pe=sum(r[i]*c[i] for i in range(k))
    kap=(po-pe)/(1-pe)
    A=sum(p[i][i]*(1-(r[i]+c[i])*(1-kap))**2 for i in range(k))
    B=(1-kap)**2*sum(p[i][j]*(c[i]+r[j])**2 for i in range(k) for j in range(k) if i!=j)
    C=(kap-pe*(1-kap))**2
    return po,pe,kap,math.sqrt((A+B-C)/(N*(1-pe)**2))

def front_matter(path):
    text=path.read_text(encoding="utf-8")
    head=text.split("---",2)[1] if text.startswith("---") else ""
    return dict(re.findall(r'^([A-Za-z_]+):\s*"?(.*?)"?\s*$',head,re.M))

class CohensKappa(unittest.TestCase):
    def test_worked_examples_match_scikit_learn(self):
        # sklearn.metrics.cohen_kappa_score on the expanded rating vectors.
        for table,ref in (([[20,5],[10,15]],0.4),([[85,5],[5,5]],0.4444444444444444),
                          ([[22,3,1],[4,18,2],[0,3,17]],0.7198275862068966)):
            with self.subTest(table=table):
                r=js("window.esaCohensKappa.compute(%s)"%json.dumps(table),[KAPPA])
                self.assertAlmostEqual(r["kappa"],ref,places=12)
                po,pe,kap,se=kappa_reference(table)
                self.assertAlmostEqual(r["po"],po,places=12)
                self.assertAlmostEqual(r["pe"],pe,places=12)
                self.assertAlmostEqual(r["se"],se,places=12)
                self.assertAlmostEqual(r["lower"],max(-1,kap-1.959963984540054*se),places=12)
        x=js("window.esaCohensKappa.compute([[20,5],[10,15]])",[KAPPA])
        self.assertAlmostEqual(x["kappaMax"],0.8,places=12)
        # Multinomial Monte Carlo (20,000 draws, seed 1) gave SD 0.1272 and 0.0708
        # for the 2x2 and 3x3 examples; the delta-method SE must be close.
        self.assertAlmostEqual(x["se"],0.1272,delta=0.003)
        self.assertAlmostEqual(js("window.esaCohensKappa.compute([[22,3,1],[4,18,2],[0,3,17]])",[KAPPA])["se"],0.0708,delta=0.003)
    def test_boundaries(self):
        perfect=js("window.esaCohensKappa.compute([[10,0],[0,10]])",[KAPPA])
        self.assertEqual((perfect["kappa"],perfect["se"]),(1,0))
        degenerate=js("window.esaCohensKappa.compute([[5,0],[0,0]])",[KAPPA])
        self.assertTrue(degenerate["degenerate"]);self.assertIsNone(degenerate["kappa"])
        disagree=js("window.esaCohensKappa.compute([[0,10],[10,0]])",[KAPPA])
        self.assertAlmostEqual(disagree["kappa"],-1,places=12)
        for bad in ("[[1,2],[3]]","[[1]]","[[1,2,3],[4,5,6]]","[[-1,2],[3,4]]","[[1.5,2],[3,4]]",
                    "[[10000001,0],[0,1]]","[[0,0],[0,0]]",json.dumps([[1]*6]*6)):
            self.assertIn("error",js("window.esaCohensKappa.compute(%s)"%bad,[KAPPA]),bad)
    def test_lesson(self):
        page=ROOT/"inference/classical-tests/cohens-kappa/index.md";t=page.read_text()
        self.assertEqual(front_matter(page)["permalink"],"/inference/classical-tests/cohens-kappa/")
        self.assertIn("/js/cohens-kappa-lab.js",t);self.assertIn("<noscript>",t)
        self.assertNotIn("innerHTML",(ROOT/KAPPA).read_text())
        self.assertIn('href="/inference/classical-tests/cohens-kappa/"',(ROOT/"inference/classical-tests/mcnemar-test/index.md").read_text())

class ArabicMcNemar(unittest.TestCase):
    def test_pair_and_shared_engine(self):
        src=(ROOT/MCN).read_text()
        self.assertIn('const ar = root.dataset.locale === "ar";',src)
        self.assertNotIn("innerHTML",src)
        ar=ROOT/"ar/inference/classical-tests/mcnemar-test/index.md";en=ROOT/"inference/classical-tests/mcnemar-test/index.md"
        self.assertEqual(front_matter(ar)["translation_pair"],"mcnemar-test")
        self.assertEqual(front_matter(en)["translation_pair"],"mcnemar-test")
        self.assertEqual(front_matter(ar)["lang"],"ar")
        a=ar.read_text()
        self.assertIn('data-locale="ar"',a)
        for i in "abcd":self.assertIn('id="esa-mcn-%s" dir="ltr"'%i,a)
        ind=(ROOT/"ar/inference/classical-tests/chi-square-independence-test/index.md").read_text()
        self.assertIn('href="/ar/inference/classical-tests/mcnemar-test/"',ind)
        self.assertNotIn("اختبار ماكنمار (بالإنجليزية)",ind)


class Hubs(unittest.TestCase):
    def test_english_chooser_routes_paired_binary_to_mcnemar(self):
        s=(ROOT/"inference/classical-tests/index.md").read_text()
        self.assertIn('"binary-paired": ["McNemar Test for Paired Proportions", "mcnemar-test/"',s)
        lab=s.split("<!-- COMPANION LABS -->")[1].split("<!-- BLOCK MAP -->")[0]
        for slug in ("fisher-exact-vs-chi-square","exact-binomial-vs-z-test","welch-pooled-monte-carlo","mcnemar-test","cohens-kappa"):
            self.assertIn('href="/inference/classical-tests/%s/"'%slug,lab)
            self.assertTrue((ROOT/"inference/classical-tests"/slug/"index.md").is_file())
        self.assertNotIn("lesson-card",lab)  # does not change the 12-lesson progress list
    def test_arabic_hub_matches_english_recommendations(self):
        en=(ROOT/"inference/classical-tests/index.md").read_text()
        en_map=dict(re.findall(r'"([a-z]+-[a-z]+(?:-(?:known|unknown))?)": \["[^"]+", "([a-z0-9-]+)/"',en))
        ar=(ROOT/"ar/inference/classical-tests/index.md").read_text()
        ar_map=json.loads(re.search(r"const methods = (\{.*?\n\});",ar,re.S).group(1))
        self.assertEqual(set(ar_map),set(en_map))
        for key,(url,name,note,arabic) in ar_map.items():
            with self.subTest(key=key):
                slug=en_map[key]
                self.assertTrue(url.endswith("/"+slug+"/"))
                exists=(ROOT/"ar/inference/classical-tests"/slug/"index.md").is_file()
                self.assertEqual(arabic,exists)
                self.assertEqual(url,("/ar" if exists else "")+"/inference/classical-tests/"+slug+"/")
        fm=front_matter(ROOT/"ar/inference/classical-tests/index.md")
        self.assertEqual((fm["lang"],fm["translation_pair"]),("ar","classical-tests-hub"))
        self.assertEqual(front_matter(ROOT/"inference/classical-tests/index.md")["translation_pair"],"classical-tests-hub")
        for href in re.findall(r'href="(/[^"]+)"',ar):
            target=ROOT/href.strip("/")/"index.md"
            self.assertTrue(target.is_file() or (ROOT/href.strip("/")/"index.html").is_file() or href=="/ar/",href)
        self.assertIn('href="/ar/inference/classical-tests/"',(ROOT/"ar/index.md").read_text())
        self.assertNotIn("innerHTML",ar)

LAB_SCRIPT=re.compile(r'<script[^>]*src="[^"]*/js/[^"]*(?:lab|explorer|calculator|simulator|laboratory)[^"]*\.js"')

class NoScriptCoverage(unittest.TestCase):
    def test_every_lab_page_has_a_noscript_notice(self):
        pages=[p for p in ROOT.rglob("index.md") if LAB_SCRIPT.search(p.read_text(encoding="utf-8"))]
        self.assertGreaterEqual(len(pages),60)
        for p in pages:
            t=p.read_text(encoding="utf-8")
            with self.subTest(page=str(p.relative_to(ROOT))):
                self.assertTrue("<noscript" in t or "{% include lab-noscript.html %}" in t)
                self.assertLessEqual(t.count("{% include lab-noscript.html %}"),1)
        inc=(ROOT/"_includes/lab-noscript.html").read_text()
        self.assertIn('page.lang == "ar"',inc);self.assertIn("JavaScript",inc)

if __name__=="__main__":unittest.main()
