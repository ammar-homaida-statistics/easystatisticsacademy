"""Batch #101: confidence-interval ↔ test duality lab (z and t, two-sided and one-sided);
Arabic lessons on null/alternative hypotheses, power and effect size, and outliers and
influence; and a guard that keeps long words in page headings breakable on 320 px
screens. References: SciPy 1.18.1 (norm, t, nct) and closed forms."""
import json
import math
import re
import subprocess
import unittest
from pathlib import Path
from statistics import NormalDist

ROOT=Path(__file__).resolve().parents[2]
CID="js/ci-test-duality-lab.js"

def js(expression):
    runner='''const fs=require("fs"),vm=require("vm"),window={},document={getElementById:()=>null};
vm.runInNewContext(fs.readFileSync(process.argv[1],"utf8"),{window,document});
console.log(JSON.stringify(%s));'''%expression
    p=subprocess.run(["node","-e",runner,str(ROOT/CID)],text=True,capture_output=True,check=True)
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

# (method, side, mean, sd, n, mu0, alpha) -> SciPy critical value, lower, upper, p
REF=[(("t","two-sided",104.2,8.5,25,100,.05),2.063898561628026,100.69137244523236,107.70862755476765,0.02098078526987131),
     (("t","two-sided",102.1,8.5,25,100,.05),2.063898561628026,98.59137244523235,105.60862755476764,0.22867750910451892),
     (("z","greater",51.3,4,16,50,.05),1.6448536269514729,49.655146373048524,None,0.0968004845856108),
     (("z","less",49.1,4,16,50,.01),2.3263478740408408,None,51.42634787404084,0.18406012534675986),
     (("t","greater",3.2,2.5,8,1.5,.1),1.4149239276505083,1.9493721198690273,None,0.04792938601041935),
     (("t","two-sided",10,3,2,0,.05),12.706204736174705,-16.95393059628128,36.95393059628128,0.13307473124860075)]

def case(t):
    return dict(zip(("method","side","mean","sd","n","mu0","alpha"),t))

class Duality(unittest.TestCase):
    def test_matches_scipy(self):
        out=js("%s.map(c=>window.esaCiTestDuality.compute(c))"%json.dumps([case(c) for c,*_ in REF]))
        for (c,crit,lo,hi,p),r in zip(REF,out):
            with self.subTest(case=c):
                self.assertAlmostEqual(r["crit"]/crit,1,delta=1e-9)
                self.assertAlmostEqual(r["p"],p,delta=1e-10)
                if lo is not None:self.assertAlmostEqual(r["lower"],lo,delta=1e-8)
                else:self.assertIsNone(r["lower"])  # −∞ serialises as null
                if hi is not None:self.assertAlmostEqual(r["upper"],hi,delta=1e-8)
                else:self.assertIsNone(r["upper"])
                inside=(lo is None or lo<=c[5]) and (hi is None or c[5]<=hi)
                self.assertEqual(r["inside"],inside);self.assertEqual(r["reject"],p<c[6])

    def test_closed_form_quantiles(self):
        # t with 1 df is Cauchy: q = tan(π(1/2 − tail)); with 2 df: q = (1−2a)·sqrt(2/(4a(1−a))) for a=tail.
        for tail in (0.25,0.05,0.025,0.005):
            q1=js("window.esaCiTestDuality.quantile(%r,'t',1)"%tail)
            self.assertAlmostEqual(q1/math.tan(math.pi*(0.5-tail)),1,delta=1e-10)
            q2=js("window.esaCiTestDuality.quantile(%r,'t',2)"%tail)
            self.assertAlmostEqual(q2/((1-2*tail)*math.sqrt(2/(4*tail*(1-tail)))),1,delta=1e-10)
            qz=js("window.esaCiTestDuality.quantile(%r,'z',1)"%tail)
            self.assertAlmostEqual(qz,NormalDist().inv_cdf(1-tail),delta=1e-9)

    def test_duality_holds_everywhere(self):
        import random
        random.seed(101);cases=[]
        for _ in range(400):
            cases.append({"method":random.choice("zt"),"side":random.choice(["two-sided","greater","less"]),
                "mean":random.uniform(-50,50),"sd":10**random.uniform(-2,2),"n":random.choice([2,3,6,30,500]),
                "mu0":random.uniform(-60,60),"alpha":random.choice([0.001,0.01,0.05,0.1,0.5])})
        out=js("%s.map(c=>window.esaCiTestDuality.compute(c))"%json.dumps(cases))
        for c,r in zip(cases,out):
            lo=-math.inf if r["lower"] is None else r["lower"];hi=math.inf if r["upper"] is None else r["upper"]
            self.assertEqual(r["inside"],lo<=c["mu0"]<=hi)
            if r["inside"]:self.assertGreaterEqual(r["p"],c["alpha"]*(1-1e-8))
            else:self.assertLess(r["p"],c["alpha"])

    def test_boundary_counts_as_inside_with_p_equal_alpha(self):
        for side in ("two-sided","greater","less"):
            for m in ("z","t"):
                base={"method":m,"side":side,"mean":104.2,"sd":8.5,"n":25,"mu0":100,"alpha":0.05}
                r=js("window.esaCiTestDuality.compute(%s)"%json.dumps(base))
                base["mu0"]=r["upper"] if side=="less" else r["lower"]
                b=js("window.esaCiTestDuality.compute(%s)"%json.dumps(base))
                with self.subTest(side=side,method=m):
                    self.assertTrue(b["inside"]);self.assertFalse(b["reject"])
                    self.assertAlmostEqual(b["p"],0.05,delta=1e-10)

    def test_invalid_inputs(self):
        bad=[{"n":1},{"n":2.5},{"sd":0},{"sd":-1},{"alpha":0},{"alpha":0.6},{"mean":float("nan")},{"method":"x"},{"side":"both"},{"n":2000000}]
        for b in bad:
            c={"method":"t","side":"two-sided","mean":1,"sd":1,"n":5,"mu0":0,"alpha":0.05};c.update(b)
            payload=json.dumps(c).replace("NaN","NaN")
            self.assertIsNone(js("window.esaCiTestDuality.compute(%s)"%payload),b)

    def test_page_wiring(self):
        t=(ROOT/"inference/hypothesis-testing/ci-and-test-connection/index.md").read_text(encoding="utf-8")
        self.assertIn('<script defer src="/js/ci-test-duality-lab.js"></script>',t)
        self.assertEqual(t.count("{% include lab-noscript.html %}"),1)
        for i in ("method","side","mean","sd","n","mu0","alpha","error","results","crit","ci","inside","stat","p","decision","agree","example","inside-ex","boundary"):
            self.assertEqual(t.count('id="esa-cid-%s"'%i),1,i)
        self.assertLess(t.index('id="esa-cid-lab"'),t.index("<h2>The Relationship to p-Values</h2>"))
        r=js("window.esaCiTestDuality.compute(%s)"%json.dumps(case(REF[0][0])))
        for v in ("t(24) = %.4f"%r["crit"],"95%%: [%.4f, %.4f]"%(r["lower"],r["upper"]),"t = %.4f"%r["stat"],">%.6f<"%r["p"]):
            self.assertIn(v,t)

NEW={"null-and-alternative":"/inference/hypothesis-testing/null-and-alternative/",
     "power-and-effect-size":"/inference/hypothesis-testing/power-and-effect-size/",
     "outliers-and-influence":"/inference/assumptions-robustness/outliers-and-influence/"}

class ArabicLessons(unittest.TestCase):
    def test_pairs_and_links(self):
        pr=pairs();layout=(ROOT/"_layouts/default.html").read_text(encoding="utf-8")
        home=(ROOT/"ar/index.md").read_text(encoding="utf-8")
        for pid,en in NEW.items():
            ar="/ar"+en
            with self.subTest(pid=pid):
                self.assertEqual(pr[pid],{"en":en,"ar":ar})
                fa=front_matter(ROOT/ar.strip("/")/"index.md");fe=front_matter(ROOT/en.strip("/")/"index.md")
                self.assertEqual((fa["permalink"],fa["lang"],fa["translation_pair"],fa["learning_resource"]),(ar,"ar",pid,"true"))
                self.assertEqual((fe["translation_pair"],fe["learning_resource"]),(pid,"true"))
                self.assertIn('page.translation_pair == "%s"'%pid,layout)
                self.assertIn('href="%s"'%ar,(ROOT/en.strip("/")/"index.md").read_text(encoding="utf-8"))
                self.assertIn('href="%s"'%ar,home)

    def test_arabic_chain_links(self):
        chain={"ar/inference/hypothesis-testing/test-statistic-standardization/index.md":"/ar/inference/hypothesis-testing/null-and-alternative/",
               "ar/inference/hypothesis-testing/one-sided-vs-two-sided/index.md":"/ar/inference/hypothesis-testing/power-and-effect-size/",
               "ar/inference/hypothesis-testing/type1-type2-errors/index.md":"/ar/inference/hypothesis-testing/power-and-effect-size/",
               "ar/inference/assumptions-robustness/robust-alternatives-nonparametric/index.md":"/ar/inference/assumptions-robustness/outliers-and-influence/"}
        for f,target in chain.items():
            t=(ROOT/f).read_text(encoding="utf-8")
            self.assertIn('href="%s"'%target,t,f);self.assertNotIn('href="%s"'%target[3:],t,f)

    def test_power_numbers(self):
        t=(ROOT/"ar/inference/hypothesis-testing/power-and-effect-size/index.md").read_text(encoding="utf-8")
        N=NormalDist()
        def power(d,n,a):
            z=N.inv_cdf(1-a/2);return N.cdf(d*math.sqrt(n)-z)+N.cdf(-d*math.sqrt(n)-z)
        rows=re.findall(r'<tr><td>(\d+)</td><td>([\d.]+)</td><td>([\d.]+)</td><td>([\d.]+)</td></tr>',t)
        self.assertEqual([r[0] for r in rows],["10","20","32","50","100"])
        for n,a,b,c in rows:
            n=int(n)
            self.assertEqual(a,"%.3f"%power(.5,n,.05));self.assertEqual(b,"%.3f"%power(.5,n,.01));self.assertEqual(c,"%.3f"%power(.2,n,.05))
        for d,a,pw,raw,ceil in ((.5,.05,.8,"31.40",32),(.5,.05,.9,"42.03",43),(.5,.01,.8,"46.72",47),(.2,.05,.8,"196.22",197)):
            n=((N.inv_cdf(1-a/2)+N.inv_cdf(pw))/d)**2
            self.assertEqual("%.2f"%n,raw);self.assertEqual(math.ceil(n),ceil)
            self.assertIn("⌈%s⌉ = %d"%(raw,ceil),t)
        self.assertIn("n = 34",t)  # exact noncentral-t sample size (SciPy nct): power 0.8078 at 34, 0.7954 at 33

    def test_outlier_numbers(self):
        t=(ROOT/"ar/inference/assumptions-robustness/outliers-and-influence/index.md").read_text(encoding="utf-8")
        from statistics import mean,median,stdev
        x=[5,6,7,8,100]
        self.assertEqual((mean(x),median(x),"%.2f"%stdev(x)),(25.2,7,"41.83"))
        self.assertEqual((mean(x[:4]),median(x[:4]),"%.2f"%stdev(x[:4])),(6.5,6.5,"1.29"))
        z=(100-mean(x))/stdev(x);bound=4/math.sqrt(5)
        self.assertEqual("%.3f"%z,"1.788");self.assertEqual("%.3f"%bound,"1.789");self.assertLess(z,bound)
        for s in ("25.2","41.83","1.29","1.788","1.789"):self.assertIn(s,t)
        # Shiffler's bound: |z_i| ≤ (n−1)/√n for every sample, attained by one extreme value.
        for n in (3,5,10):
            y=[0]*(n-1)+[1];zz=(1-mean(y))/stdev(y)
            self.assertAlmostEqual(zz,(n-1)/math.sqrt(n),delta=1e-12)

# ---- Heading guard -----------------------------------------------------------
SKIP={"courses","code-lab","_site","node_modules",".git","vendor"}
LONG=14

def headings():
    for p in sorted(ROOT.rglob("index.*")):
        rel=p.relative_to(ROOT)
        if rel.parts[0] in SKIP or p.suffix not in (".md",".html"):continue
        for m in re.finditer(r'<h1[^>]*>(.*?)</h1>',p.read_text(encoding="utf-8"),re.S):
            yield rel.as_posix(),m.group(1)

def unbreakable_words(inner):
    text=re.sub(r'<wbr\s*/?>|&shy;|­','​',inner)
    text=re.sub(r'<br\s*/?>',' ',text);text=re.sub(r'<[^>]+>','',text);text=re.sub(r'\{\{.*?\}\}|\{%.*?%\}','',text)
    return [w for w in re.split(r'[\s​\-–—/]+',text) if len(re.sub(r'[^\w]','',w))>=LONG]

class HeadingGuard(unittest.TestCase):
    def test_long_heading_words_have_break_points(self):
        bad=[(f,unbreakable_words(h)) for f,h in headings() if unbreakable_words(h)]
        self.assertEqual(bad,[],"Add <wbr> inside heading words of %d+ letters"%LONG)

    def test_guard_detects_and_accepts(self):
        self.assertEqual(unbreakable_words("Heteroscedasticity and Variance"),["Heteroscedasticity"])
        self.assertEqual(unbreakable_words("Hetero<wbr>scedasticity and Variance"),[])
        self.assertEqual(unbreakable_words("Understand statistics.<br><em>Use it</em>"),[])

    def test_css_safety_net_and_scope(self):
        self.assertIn("h1,h2,h3{overflow-wrap:break-word}",(ROOT/"css/style.css").read_text(encoding="utf-8"))
        self.assertTrue(all(not f.startswith(("courses/","code-lab/")) for f,_ in headings()))
        self.assertIn("Hetero<wbr>scedasticity",(ROOT/"inference/assumptions-robustness/heteroscedasticity-variance-issues/index.md").read_text(encoding="utf-8"))

if __name__=="__main__":unittest.main()
