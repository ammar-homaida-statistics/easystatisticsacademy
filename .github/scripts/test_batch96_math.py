"""Batch #96: Arabic one-way ANOVA and Cohen's kappa, weighted kappa, a header
language switcher generated from _data/translations.yml, and no-JavaScript
coverage for every interactive lesson page (external or inline scripts)."""
import json
import math
import re
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
KAPPA="js/cohens-kappa-lab.js"
ANOVA="js/one-way-anova-explorer.js"

def js(expression,files):
    runner='''const fs=require("fs"),vm=require("vm"),window={},document={getElementById:()=>null};
for(const f of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(f,"utf8"),{window,document});
console.log(JSON.stringify(%s));'''%expression
    p=subprocess.run(["node","-e",runner,*[str(ROOT/f) for f in files]],text=True,capture_output=True,check=True)
    return json.loads(p.stdout)

def front_matter(path):
    text=path.read_text(encoding="utf-8")
    head=text.split("---",2)[1] if text.startswith("---") else ""
    return dict(re.findall(r'^([A-Za-z_]+):\s*"?(.*?)"?\s*$',head,re.M))

def pairs():
    """Minimal parser for the flat list in _data/translations.yml (no PyYAML needed)."""
    out=[];cur=None
    for line in (ROOT/"_data/translations.yml").read_text(encoding="utf-8").splitlines():
        m=re.match(r'^- id:\s*(\S+)\s*$',line)
        if m: cur={"id":m.group(1)};out.append(cur);continue
        m=re.match(r'^\s+(en|ar):\s*(\S+)\s*$',line)
        if m and cur is not None: cur[m.group(1)]=m.group(2)
    return out

# ---------------------------------------------------------------------------
# Independent references (pure Python; not derived from the JavaScript).
def weights(k,scheme):
    if scheme=="none": return [[1.0 if i==j else 0.0 for j in range(k)] for i in range(k)]
    if scheme=="linear": return [[1-abs(i-j)/(k-1) for j in range(k)] for i in range(k)]
    return [[1-((i-j)/(k-1))**2 for j in range(k)] for i in range(k)]

def kappa_w(P,w):
    k=len(P);r=[sum(row) for row in P];c=[sum(P[i][j] for i in range(k)) for j in range(k)]
    po=sum(w[i][j]*P[i][j] for i in range(k) for j in range(k))
    pe=sum(w[i][j]*r[i]*c[j] for i in range(k) for j in range(k))
    return (po-pe)/(1-pe)

def delta_method_se(table,scheme):
    """SE from the multinomial delta method with a central-difference gradient.
    This is an independent derivation of the asymptotic variance, not the
    Fleiss-Cohen-Everitt closed form used by the lab."""
    k=len(table);N=sum(map(sum,table));P=[[v/N for v in row] for row in table]
    w=weights(k,scheme);flat=[x for row in P for x in row];h=1e-6;g=[]
    for m in range(k*k):
        up=flat[:];dn=flat[:];up[m]+=h;dn[m]-=h
        g.append((kappa_w([up[i*k:(i+1)*k] for i in range(k)],w)-kappa_w([dn[i*k:(i+1)*k] for i in range(k)],w))/(2*h))
    gp=sum(gi*pi for gi,pi in zip(g,flat))
    var=(sum(gi*gi*pi for gi,pi in zip(g,flat))-gp*gp)/N
    return math.sqrt(var)

TABLES=[[[22,3,1],[4,18,2],[0,3,17]],[[20,5],[10,15]],[[10,4,1,0],[3,12,5,1],[0,4,15,3],[1,0,2,9]],
        [[5,2,0,0,1],[1,7,2,0,0],[0,2,9,3,0],[0,0,1,8,2],[1,0,0,2,6]],[[0,5,7],[6,0,4],[8,3,0]]]
# scikit-learn 1.9.1 cohen_kappa_score(a, b, weights=...) on the expanded ratings.
SKLEARN={0:(0.7198275862068966,0.771455223880597,0.8241206030150754),
         1:(0.4,0.4,0.4),
         2:(0.5343680709534369,0.6436363636363637,0.7342657342657343),
         3:(0.5880708294501398,0.6987405541561713,0.7334205933682374),
         4:(-0.5125,-0.5745526838966204,-0.6311787072243344)}

class WeightedKappa(unittest.TestCase):
    def test_matches_scikit_learn(self):
        for idx,table in enumerate(TABLES):
            for scheme,ref in zip(("none","linear","quadratic"),SKLEARN[idx]):
                with self.subTest(table=idx,scheme=scheme):
                    r=js("window.esaCohensKappa.compute(%s,%s)"%(json.dumps(table),json.dumps(scheme)),[KAPPA])
                    self.assertAlmostEqual(r["kappa"],ref,places=12)
                    P=[[v/sum(map(sum,table)) for v in row] for row in table]
                    self.assertAlmostEqual(r["kappa"],kappa_w(P,weights(len(table),scheme)),places=12)

    def test_standard_error_equals_delta_method(self):
        for idx,table in enumerate(TABLES):
            for scheme in ("none","linear","quadratic"):
                with self.subTest(table=idx,scheme=scheme):
                    r=js("window.esaCohensKappa.compute(%s,%s)"%(json.dumps(table),json.dumps(scheme)),[KAPPA])
                    self.assertAlmostEqual(r["se"],delta_method_se(table,scheme),delta=2e-6)
                    self.assertAlmostEqual(r["lower"],max(-1,r["kappa"]-1.959963984540054*r["se"]),places=12)

    def test_lesson_values_and_unweighted_path_unchanged(self):
        three=[[22,3,1],[4,18,2],[0,3,17]]
        got={s:js("window.esaCohensKappa.compute(%s,%s)"%(json.dumps(three),json.dumps(s)),[KAPPA]) for s in ("linear","quadratic")}
        self.assertEqual(round(got["linear"]["kappa"],3),0.771);self.assertEqual(round(got["quadratic"]["kappa"],3),0.824)
        default=js("window.esaCohensKappa.compute([[20,5],[10,15]])",[KAPPA])
        explicit=js('window.esaCohensKappa.compute([[20,5],[10,15]],"none")',[KAPPA])
        self.assertEqual(default,explicit)
        self.assertEqual((round(default["kappa"],4),round(default["se"],4)),(0.4,0.127))
        for s in ("linear","quadratic"):
            two=js('window.esaCohensKappa.compute([[20,5],[10,15]],"%s")'%s,[KAPPA])
            self.assertAlmostEqual(two["kappa"],default["kappa"],places=14)
            self.assertAlmostEqual(two["se"],default["se"],places=12)
            self.assertIsNone(two["kappaMax"])  # NaN serializes as null: not reported for weights

    def test_boundaries_and_invalid_weighting(self):
        perfect=js('window.esaCohensKappa.compute([[5,0,0],[0,6,0],[0,0,7]],"quadratic")',[KAPPA])
        self.assertAlmostEqual(perfect["kappa"],1,places=14);self.assertAlmostEqual(perfect["se"],0,places=7)
        degenerate=js('window.esaCohensKappa.compute([[0,0,0],[0,9,0],[0,0,0]],"linear")',[KAPPA])
        self.assertTrue(degenerate["degenerate"]);self.assertIsNone(degenerate["kappa"])
        for bad in ('"Linear"','"cubic"','1','null','"__proto__"','"toString"'):
            with self.subTest(bad=bad):
                self.assertEqual(js("window.esaCohensKappa.compute([[1,2],[3,4]],%s)"%bad,[KAPPA]),{"error":"weights"})
        self.assertEqual(js('window.esaCohensKappa.compute([[1,-2],[3,4]],"linear")',[KAPPA]),{"error":"range"})
        w=js('window.esaCohensKappa.weightMatrix(5,"quadratic")',[KAPPA])
        self.assertEqual(w[0],[1,0.9375,0.75,0.4375,0]);self.assertEqual([w[i][i] for i in range(5)],[1]*5)

# scipy.stats.f_oneway(...) — SciPy 1.x reference values.
ANOVA_CASES=[([[4,5,6],[5,6,7],[8,9,10]],13.0,0.006591796875),
             ([[2,3,6,7],[3,4],[8,8,9,10,11]],11.592966704077819,0.004330369539241011),
             ([[1.2,3.4,2.2,5.1],[2.0,2.5,2.9],[3.3,4.1,6.0,5.5,4.4],[0.4,1.1,2.6]],5.107512645199997,0.018676636281011353)]

class Anova(unittest.TestCase):
    def test_shared_engine_matches_scipy(self):
        for groups,f,p in ANOVA_CASES:
            with self.subTest(groups=groups):
                r=js("window.esaAnovaMath.compute(%s)"%json.dumps(groups),[ANOVA])
                self.assertAlmostEqual(r["f"],f,delta=1e-8*max(1,f))
                self.assertAlmostEqual(r["p"],p,delta=1e-9)
        r=js("window.esaAnovaMath.compute([[4,5,6],[5,6,7],[8,9,10]])",[ANOVA])
        self.assertEqual((r["between"],r["within"],r["df1"],r["df2"]),(26,6,2,6))
        self.assertAlmostEqual(r["between"]/(r["between"]+r["within"]),0.8125,places=12)  # eta squared in the lessons

    def test_two_groups_equal_pooled_t_squared(self):
        a=[3.1,4.7,5.2,6.0];b=[5.5,6.1,7.4,8.2,6.6]
        r=js("window.esaAnovaMath.compute(%s)"%json.dumps([a,b]),[ANOVA])
        ma,mb=sum(a)/len(a),sum(b)/len(b)
        sp=(sum((x-ma)**2 for x in a)+sum((x-mb)**2 for x in b))/(len(a)+len(b)-2)
        t=(ma-mb)/math.sqrt(sp*(1/len(a)+1/len(b)))
        self.assertAlmostEqual(r["f"],t*t,places=10)

    def test_strings_are_localized_without_forking_the_math(self):
        src=(ROOT/ANOVA).read_text(encoding="utf-8")
        self.assertIn('root.dataset.locale==="ar"',src)
        self.assertEqual(src.count("function compute("),1)
        self.assertNotIn("innerHTML",src)
        for phrase in ("غير معرّف","عند α=0.05","المجموعة "):self.assertIn(phrase,src)

class ArabicLessons(unittest.TestCase):
    def check_pair(self,slug,pair,script):
        en=ROOT/"inference/classical-tests"/slug/"index.md";ar=ROOT/"ar/inference/classical-tests"/slug/"index.md"
        fe,fa=front_matter(en),front_matter(ar)
        self.assertEqual((fe["translation_pair"],fa["translation_pair"]),(pair,pair))
        self.assertEqual((fa["lang"],fa["permalink"]),("ar","/ar/inference/classical-tests/%s/"%slug))
        t=ar.read_text(encoding="utf-8");e=en.read_text(encoding="utf-8")
        self.assertIn(script,t);self.assertIn('data-locale="ar"',t)
        self.assertIn('href="/inference/classical-tests/%s/"'%slug,t)
        self.assertIn('href="/ar/inference/classical-tests/%s/"'%slug,e)
        self.assertTrue("<noscript" in t or "lab-noscript.html" in t)
        # Same element IDs in both languages, so one engine drives both pages.
        ids=lambda s:sorted(set(re.findall(r'id="(esa-[a-z]+-[a-z0-9-]+)"',s)))
        self.assertEqual(ids(t),ids(e))
        return t

    def test_arabic_anova(self):
        t=self.check_pair("one-way-anova-f-test","one-way-anova","/js/one-way-anova-explorer.js")
        for value in ("0.006592","0.8125","1-0.95^6"):self.assertIn(value,t)

    def test_arabic_kappa(self):
        t=self.check_pair("cohens-kappa","cohens-kappa","/js/cohens-kappa-lab.js")
        for value in ("[0.1511, 0.6489]","0.771","0.824",'value="quadratic"'):self.assertIn(value,t)

    def test_links_point_to_arabic_lessons(self):
        hub=(ROOT/"ar/inference/classical-tests/index.md").read_text(encoding="utf-8")
        mcn=(ROOT/"ar/inference/classical-tests/mcnemar-test/index.md").read_text(encoding="utf-8")
        for slug in ("one-way-anova-f-test","cohens-kappa"):
            self.assertIn('"/ar/inference/classical-tests/%s/"'%slug if slug.startswith("one") else 'href="/ar/inference/classical-tests/%s/"'%slug,hub)
            self.assertNotIn('href="/inference/classical-tests/%s/" hreflang="en"'%slug,hub)
        self.assertIn('href="/ar/inference/classical-tests/cohens-kappa/"',mcn)
        self.assertNotIn('href="/inference/classical-tests/cohens-kappa/"',mcn)

class LanguageSwitcher(unittest.TestCase):
    def test_header_is_generated_from_translation_data(self):
        h=(ROOT/"_includes/header.html").read_text(encoding="utf-8")
        self.assertIn('site.data.translations | where: "id", page.translation_pair | first',h)
        self.assertIn("{{ esa_pair.en }}",h);self.assertIn("{{ esa_pair.ar }}",h)
        # No hand-maintained per-pair branches remain.
        self.assertNotIn('page.translation_pair ==',h)
        for phrase in ("الرئيسية","ابحث في الموضوعات…","التنقل الرئيسي","اختيار اللغة"):self.assertIn(phrase,h)
        self.assertIn("انتقل إلى المحتوى الرئيسي",(ROOT/"_layouts/default.html").read_text(encoding="utf-8"))
        self.assertIn("في هذه الصفحة",(ROOT/"js/lesson-toc.js").read_text(encoding="utf-8"))
        self.assertIn("لم يُعثر على نتائج.",(ROOT/"js/search.js").read_text(encoding="utf-8"))

    def test_every_pair_resolves_to_two_pages(self):
        data=pairs();self.assertGreaterEqual(len(data),48)
        self.assertEqual(len({p["id"] for p in data}),len(data))
        pages={}
        for path in ROOT.rglob("*.md"):
            if "_site" in path.parts or "node_modules" in path.parts: continue
            fm=front_matter(path)
            if fm.get("translation_pair"):pages.setdefault(fm["translation_pair"],[]).append(fm)
        for p in data:
            with self.subTest(pair=p["id"]):
                found=pages.get(p["id"],[])
                self.assertEqual(sorted(f.get("lang","en") for f in found),["ar","en"])
                self.assertEqual({f["permalink"] for f in found},{p["en"],p["ar"]})

# ---------------------------------------------------------------------------
# A page is interactive when it loads a script from /js/ (with or without
# relative_url) or runs inline DOM code, and contains form controls or a canvas.
# Batch #95 matched only literal src="/js/...lab|explorer|..." names and missed
# 34 pages; this scan has no name filter.
SRC=re.compile(r'<script\b[^>]*\bsrc=[^>]*?/js/([\w.-]+\.js)')
INLINE=re.compile(r'<script(?![^>]*\bsrc=)(?![^>]*application/ld)[^>]*>(.*?)</script>',re.S)
CONTROLS=re.compile(r'<(?:input|button|select|textarea|canvas)\b')
# Not laboratories: a section chooser and two multiple-choice knowledge checks.
EXEMPT={"probability/distributions","foundations/what-is-statistics","foundations/measurement-scales"}
NAMED=["probability/basics/independence-vs-disjointness","probability/expectation-variance/variance-rules-and-sums",
       "inference/power-sample-size/sample-size-for-mean","inference/power-sample-size/power-curve-and-tradeoffs",
       "inference/power-sample-size/sample-size-for-proportion","inference/assumptions-robustness/bootstrap-as-robust-tool",
       "ar/inference/assumptions-robustness/bootstrap-as-robust-tool","modeling/extensions/logistic-regression",
       "modeling/model-fit-comparison/overfitting","modeling/multiple-regression/multicollinearity",
       "modeling/simple-linear-regression/least-squares","descriptive/visualization/boxplots",
       "descriptive/visualization/histograms","inference/classical-tests/paired-t-test",
       "inference/classical-tests/one-way-anova-f-test","probability/distributions/binomial-distribution",
       "ar/probability/distributions/binomial-distribution","inference/confidence-intervals/what-is-a-confidence-interval"]

def interactive_pages():
    out=[]
    for p in sorted(ROOT.rglob("index.md")):
        if "_site" in p.parts or "node_modules" in p.parts: continue
        t=p.read_text(encoding="utf-8")
        dom=re.search(r"addEventListener|getElementById|querySelector"," ".join(INLINE.findall(t)))
        if (SRC.search(t) or dom) and CONTROLS.search(t):out.append(p)
    return out

class NoScriptCoverage(unittest.TestCase):
    def test_every_interactive_page_has_a_notice(self):
        pages=interactive_pages();self.assertGreaterEqual(len(pages),115)
        rel={str(p.parent.relative_to(ROOT)) for p in pages}
        for name in NAMED+sorted(EXEMPT):self.assertIn(name,rel)
        for p in pages:
            name=str(p.parent.relative_to(ROOT))
            if name in EXEMPT:continue
            t=p.read_text(encoding="utf-8")
            with self.subTest(page=name):
                self.assertTrue("<noscript" in t or "{% include lab-noscript.html %}" in t)
                self.assertLessEqual(t.count("{% include lab-noscript.html %}"),1)

    def test_include_is_after_the_page_heading(self):
        for name in NAMED:
            t=(ROOT/name/"index.md").read_text(encoding="utf-8")
            if "{% include lab-noscript.html %}" in t and "</h1>" in t:
                with self.subTest(page=name):
                    self.assertLess(t.index("</h1>"),t.index("{% include lab-noscript.html %}"))

if __name__=="__main__":unittest.main()
