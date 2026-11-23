"""Batch #100: Levene/Brown–Forsythe equal-variance laboratory; Arabic lessons on
robust and nonparametric methods (with both rank laboratories), test statistics
and one- versus two-sided tests; and a static guard against inline formulas that
cannot fit a 320 px screen or contain doubled backslashes. References: SciPy
1.18.1 (levene, norm) and closed-form normal quantiles."""
import json
import math
import re
import subprocess
import unittest
from pathlib import Path
from statistics import NormalDist

ROOT=Path(__file__).resolve().parents[2]
LV="js/levene-lab.js";RT="js/rank-tests-lab.js";KW="js/kruskal-wallis-lab.js"

def js(expression,files):
    runner='''const fs=require("fs"),vm=require("vm"),window={},document={getElementById:()=>null};
for(const f of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(f,"utf8"),{window,document});
console.log(JSON.stringify(%s));'''%expression
    p=subprocess.run(["node","-e",runner,*[str(ROOT/f) for f in files]],text=True,capture_output=True,check=True)
    return json.loads(p.stdout)

def front_matter(path):
    text=path.read_text(encoding="utf-8");head=text.split("---",2)[1] if text.startswith("---") else ""
    return dict(re.findall(r'^([A-Za-z_]+):\s*"?(.*?)"?\s*$',head,re.M))

def pairs():
    out={};cur=None
    for line in (ROOT/"_data/translations.yml").read_text(encoding="utf-8").splitlines():
        m=re.match(r'^- id:\s*(\S+)\s*$',line)
        if m:cur=m.group(1);out[cur]={};continue
        m=re.match(r'^\s+(en|ar):\s*(\S+)\s*$',line)
        if m and cur:out[cur][m.group(1)]=m.group(2)
    return out

# scipy.stats.levene(*groups, center=...) -> (W, p)
PRESETS={
 "example":[[12.1,13.4,11.8,12.9,13.1,12.4],[10.2,14.8,9.5,15.6,11.9,13.7],[12.5,12.8,13.0,12.2,12.6,12.9]],
 "equal":[[4.1,5.3,3.8,6.0,4.9,5.5],[5.2,4.4,6.1,3.9,5.0,4.6],[4.8,5.9,4.0,5.4,4.3,5.7]],
 "outlier":[[10,11,12,13,40],[10,11,12,13,14],[9,11,12,14,15]]}
REF={("example","median"):(16.261753108886854,0.0001753359141427825),
     ("example","mean"):(16.92392676767676,0.00014267349731402759),
     ("equal","median"):(0.10163934426229529,0.9039720835335086),
     ("equal","mean"):(0.11199421965317938,0.8947899585911366),
     ("outlier","median"):(0.8164088769334231,0.46512930449074646),
     ("outlier","mean"):(4.690403877221323,0.03125667843742852)}

def levene_direct(groups,center):
    """Independent implementation: one-way ANOVA F on absolute deviations."""
    cen=(lambda g:sorted(g)[len(g)//2] if len(g)%2 else (sorted(g)[len(g)//2-1]+sorted(g)[len(g)//2])/2) if center=="median" else (lambda g:sum(g)/len(g))
    z=[[abs(x-cen(g)) for x in g] for g in groups];k=len(z);N=sum(map(len,z))
    zi=[sum(g)/len(g) for g in z];zb=sum(map(sum,z))/N
    between=sum(len(g)*(m-zb)**2 for g,m in zip(z,zi));within=sum((x-m)**2 for g,m in zip(z,zi) for x in g)
    return (N-k)/(k-1)*between/within

class Levene(unittest.TestCase):
    def test_matches_scipy(self):
        for (name,center),(w,p) in REF.items():
            r=js("window.esaLevene.compute(%s,%s)"%(json.dumps(PRESETS[name]),json.dumps(center)),[LV])
            with self.subTest(name=name,center=center):
                self.assertTrue(r["defined"])
                self.assertAlmostEqual(r["W"]/w,1,delta=1e-12)
                self.assertAlmostEqual(r["p"],p,delta=1e-12)
                self.assertAlmostEqual(r["W"]/levene_direct(PRESETS[name],center),1,delta=1e-12)
                self.assertEqual((r["df1"],r["df2"]),(len(PRESETS[name])-1,sum(map(len,PRESETS[name]))-len(PRESETS[name])))

    def test_f_survival_closed_forms(self):
        # F(2, ν) survival has the closed form (1 + 2x/ν)^(−ν/2).
        for x,nu in ((0.5,15),(3.0,12),(16.0,15)):
            got=js("window.esaLevene.fSurvival(%r,2,%r)"%(x,nu),[LV])
            self.assertAlmostEqual(got/(1+2*x/nu)**(-nu/2),1,delta=1e-11)
        # F(1, ν) = t_ν²; F(1,1) survival = 1 − (2/π)·atan(√x).
        self.assertAlmostEqual(js("window.esaLevene.fSurvival(1,1,1)",[LV]),0.5,delta=1e-13)
        self.assertAlmostEqual(js("window.esaLevene.fSurvival(3,1,1)",[LV]),1-2/math.pi*math.atan(math.sqrt(3)),delta=1e-13)

    def test_boundaries(self):
        same=js('window.esaLevene.compute([[1,3],[5,9]],"mean")',[LV])
        self.assertFalse(same["defined"])  # |x − mean| is constant within each group → zero within SS
        self.assertIsNone(js('window.esaLevene.compute([[1,2,3]],"median")',[LV]))
        self.assertIsNone(js('window.esaLevene.compute([[1],[2,3]],"median")',[LV]))
        self.assertIsNone(js('window.esaLevene.compute([[1,2],[3,1e7]],"median")',[LV]))
        self.assertIsNone(js('window.esaLevene.compute([[1,2],[3,4],[1,2],[3,4],[1,2],[3,4],[5,6]],"median")',[LV]))
        two=js('window.esaLevene.compute([[1,2,4,8],[3,3.5,4,9.5]],"median")',[LV])
        self.assertEqual((two["df1"],two["df2"]),(1,6))

    def test_page_wiring(self):
        page=ROOT/"inference/assumptions-robustness/heteroscedasticity-variance-issues/index.md"
        t=page.read_text(encoding="utf-8")
        self.assertIn('<script defer src="/js/levene-lab.js"></script>',t)
        self.assertEqual(t.count("{% include lab-noscript.html %}"),1)
        for i in ("center","input","error","results","w","df","p","sds","ratio","decision","example","equal","outlier"):
            self.assertEqual(t.count('id="esa-lv-%s"'%i),1,i)
        self.assertLess(t.index('id="esa-lv-lab"'),t.index("<h2>Limitations of Formal Tests</h2>"))
        self.assertIn("4.690",t);self.assertIn("0.816",t)

ARP={"robust-alternatives":"/inference/assumptions-robustness/robust-alternatives-nonparametric/",
     "test-statistic-standardization":"/inference/hypothesis-testing/test-statistic-standardization/",
     "one-sided-vs-two-sided":"/inference/hypothesis-testing/one-sided-vs-two-sided/"}

class ArabicLessons(unittest.TestCase):
    def test_pairs_front_matter_and_links(self):
        pr=pairs();layout=(ROOT/"_layouts/default.html").read_text(encoding="utf-8")
        home=(ROOT/"ar/index.md").read_text(encoding="utf-8")
        for pid,en in ARP.items():
            ar="/ar"+en
            with self.subTest(pid=pid):
                self.assertEqual(pr[pid],{"en":en,"ar":ar})
                fa=front_matter(ROOT/("ar"+en)/"index.md");fe=front_matter(ROOT/en.strip("/")/"index.md")
                self.assertEqual((fa["permalink"],fa["lang"],fa["translation_pair"],fa["learning_resource"]),(ar,"ar",pid,"true"))
                self.assertEqual((fe["translation_pair"],fe["learning_resource"]),(pid,"true"))
                self.assertIn('page.translation_pair == "%s"'%pid,layout)
                self.assertIn('hreflang="ar" href="{{ site.url }}%s"'%ar,layout)
                self.assertIn('href="%s"'%ar,(ROOT/en.strip("/")/"index.md").read_text(encoding="utf-8"))
                self.assertIn('href="%s"'%ar,home)

    def test_pvalue_previous_link_is_arabic(self):
        t=(ROOT/"ar/inference/hypothesis-testing/p-value-meaning/index.md").read_text(encoding="utf-8")
        self.assertNotIn('href="/inference/hypothesis-testing/test-statistic-standardization/"',t)
        self.assertEqual(t.count('href="/ar/inference/hypothesis-testing/test-statistic-standardization/"'),2)

    def test_robust_page_labs(self):
        t=(ROOT/"ar/inference/assumptions-robustness/robust-alternatives-nonparametric/index.md").read_text(encoding="utf-8")
        e=(ROOT/"inference/assumptions-robustness/robust-alternatives-nonparametric/index.md").read_text(encoding="utf-8")
        self.assertEqual(t.count("{% include lab-noscript.html %}"),1)
        self.assertIn('id="esa-rt-lab" data-locale="ar"',t);self.assertIn('id="esa-kw-lab" data-locale="ar"',t)
        self.assertIn('<script defer src="/js/rank-tests-lab.js"></script>',t)
        self.assertIn('<script defer src="/js/kruskal-wallis-lab.js"></script>',t)
        ids=lambda s,pre:sorted(re.findall(r'id="(%s[^"]*)"'%pre,s))
        for pre in ("esa-rt-","esa-kw-"):
            self.assertEqual(ids(t,pre),ids(e,pre),pre)
            self.assertEqual(len(ids(t,pre)),len(set(ids(t,pre))))
        # Static placeholders equal what the engines compute for the defaults.
        mw=js("window.esaRankTests.mannWhitney([12.1,14.3,11.8,15.2,13.9,12.7],[15.8,16.4,14.9,17.2,18.1],'two-sided')",[RT])
        for v in ("%.4f"%mw["z"],"%.6f"%mw["pApprox"],"%.6f"%mw["pExact"],"%.4f"%mw["rankBiserial"],"%.4f"%mw["hodgesLehmann"]):
            self.assertIn(">%s</output>"%v,t)
        kw=js("window.esaKruskal.compute([[2.1,3.4,1.9,5.6,2.8],[4.2,6.1,5.5,7.3,4.9],[8.8,6.7,9.4,7.9,12.5]])",[KW])
        for v in ("%.4f"%kw["H"],"%.6f"%kw["p"],"%.4f"%kw["epsilon2"]):
            self.assertIn(">%s</output>"%v,t)
        src=(ROOT/RT).read_text(encoding="utf-8")+(ROOT/KW).read_text(encoding="utf-8")
        self.assertEqual(src.count('root.dataset.locale==="ar"'),2)

    def test_one_sided_numbers(self):
        t=(ROOT/"ar/inference/hypothesis-testing/one-sided-vs-two-sided/index.md").read_text(encoding="utf-8")
        N=NormalDist()
        for q,s in ((.95,"1.645"),(.975,"1.960"),(.99,"2.326"),(.995,"2.576")):
            self.assertEqual("%.3f"%N.inv_cdf(q),s);self.assertIn(s,t)
        for v,s in ((1-N.cdf(2),"0.02275"),(N.cdf(2),"0.97725"),(2*(1-N.cdf(2)),"0.04550"),
                    (1-N.cdf(1.8),"0.0359"),(2*(1-N.cdf(1.8)),"0.0719")):
            self.assertEqual(("%."+str(len(s)-2)+"f")%v,s);self.assertIn(s,t)
        c1,c2=N.inv_cdf(.95),N.inv_cdf(.975)
        self.assertEqual("%.3f"%(1-N.cdf(c1-2.5)),"0.804");self.assertIn("0.804",t)
        self.assertEqual("%.3f"%(1-N.cdf(c2-2.5)+N.cdf(-c2-2.5)),"0.705");self.assertIn("0.705",t)
        self.assertEqual("%.6f"%(1-N.cdf(c1+2.5)),"0.000017");self.assertIn("0.000017",t)
        # Choosing the tail after seeing the sign doubles the type I error rate.
        self.assertAlmostEqual(2*(1-N.cdf(c1)),0.10,delta=1e-12)

    def test_test_statistic_numbers(self):
        t=(ROOT/"ar/inference/hypothesis-testing/test-statistic-standardization/index.md").read_text(encoding="utf-8")
        N=NormalDist()
        self.assertEqual((492-500)/2,-4);self.assertEqual(-8/20,-0.4)
        self.assertEqual("%.7f"%(2*N.cdf(-4)),"0.0000633");self.assertIn("0.0000633",t)
        self.assertEqual("%.3f"%(2*N.cdf(-0.4)),"0.689");self.assertIn("0.689",t)
        e=(ROOT/"inference/hypothesis-testing/test-statistic-standardization/index.md").read_text(encoding="utf-8")
        self.assertNotIn("Observed = estimate",e);self.assertIn("σ/√n = standard error of the sample mean",e)

# ---- Inline-formula guard -------------------------------------------------
SKIP={"courses","code-lab","_site","node_modules",".git","vendor"}

def visual_length(body):
    """Rough rendered width in characters: a fraction counts as its wider part,
    spacing/formatting commands count as nothing, other commands as one glyph."""
    b=body
    for _ in range(3):
        b=re.sub(r'\\(?:frac|dfrac|tfrac)\{([^{}]*)\}\{([^{}]*)\}',lambda m:max(m.group(1),m.group(2),key=len),b)
    b=re.sub(r'\\(?:left|right|mathrm|text|operatorname|mathbb|mathcal|bigl|bigr|Big|big|displaystyle|quad|qquad)(?![a-zA-Z])|\\[,;!]','',b)
    b=re.sub(r'\\[a-zA-Z]+','x',b);b=re.sub(r'[{}^_]','',b)
    return len(b.replace(' ',''))

def inline_formulas():
    for p in sorted(ROOT.rglob("index.*")):
        rel=p.relative_to(ROOT)
        if rel.parts[0] in SKIP or p.suffix not in (".md",".html"):continue
        t=p.read_text(encoding="utf-8")
        for m in re.finditer(r'(?<!\\)\\\((.*?)\\\)',t):
            yield rel.as_posix(),t.count("\n",0,m.start())+1,m.group(1)

class InlineFormulaGuard(unittest.TestCase):
    def test_estimator_calibration(self):
        # The Bayes formula that overflowed at 320 px in Batch #99 scored 36.
        self.assertGreaterEqual(visual_length(r"P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B\mid A)P(A)+P(B\mid A^c)P(A^c)}"),30)
        self.assertLess(visual_length(r"\hat p\pm z\sqrt{\hat p(1-\hat p)/n}"),30)

    def test_no_wide_inline_formulas(self):
        wide=[(f,l,b[:80]) for f,l,b in inline_formulas() if visual_length(b)>=30]
        self.assertEqual(wide,[],"Split long inline formulas or make them display formulas")

    def test_no_doubled_backslash_commands(self):
        bad=[(f,l,b[:80]) for f,l,b in inline_formulas() if re.search(r'(?<!\\)\\\\[a-zA-Z]',b)]
        self.assertEqual(bad,[])

    def test_scope_excludes_other_projects(self):
        self.assertTrue(all(not f.startswith(("courses/","code-lab/")) for f,_,_ in inline_formulas()))

if __name__=="__main__":unittest.main()
