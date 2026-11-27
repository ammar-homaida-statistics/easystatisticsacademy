"""Batch #104: exact coverage of Wald, Wilson and Clopper–Pearson proportion intervals
(exact binomial sums verified against SciPy-derived references and closed forms); Arabic
lessons on the t interval, checking normality, width and precision (explorer in Arabic) and
the proportion interval (both labs in Arabic). References: SciPy 1.18.1 (binom, beta, t,
norm) and closed forms."""
import json
import math
import re
import subprocess
import unittest
from pathlib import Path
from statistics import NormalDist

ROOT=Path(__file__).resolve().parents[2]

def js(expression,f):
    runner='''const fs=require("fs"),vm=require("vm"),window={},document={getElementById:()=>null};
vm.runInNewContext(fs.readFileSync(process.argv[1],"utf8"),{window,document});
console.log(JSON.stringify(%s));'''%expression
    p=subprocess.run(["node","-e",runner,str(ROOT/f)],text=True,capture_output=True,check=True)
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

def page(rel):return (ROOT/rel.strip("/")/"index.md").read_text(encoding="utf-8")
PC="js/proportion-coverage-lab.js"

# Exact coverage from scipy.stats.binom.pmf with Clopper–Pearson limits from scipy.stats.beta.ppf.
REF={(30,0.1,95):(0.8085213615694749,0.9741732113380898,0.9922163807620783),
     (50,0.1,95):(0.8789166420663242,0.9703082890880887,0.9703082890880887),
     (100,0.5,95):(0.943112066359019,0.943112066359019,0.9647997997822949),
     (20,0.05,95):(0.6389401372568057,0.9245163262115039,0.9840984739802368),
     (50,0.5,95):(0.9350913529277274,0.9350913529277274,0.9671608624357311)}
Z={90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004}

def coverage_py(n,p,level):
    """Independent pure-Python exact coverage for Wald and Wilson (CP via closed forms below)."""
    z=Z[level];cov={"wald":0.0,"wilson":0.0}
    for x in range(n+1):
        w=math.comb(n,x)*p**x*(1-p)**(n-x);ph=x/n
        m=z*math.sqrt(ph*(1-ph)/n)
        den=1+z*z/n;c=(ph+z*z/(2*n))/den;r=z*math.sqrt(ph*(1-ph)/n+z*z/(4*n*n))/den
        if ph-m<=p+1e-12 and p<=ph+m+1e-12:cov["wald"]+=w
        if max(0,c-r)<=p+1e-12 and p<=min(1,c+r)+1e-12:cov["wilson"]+=w
    return cov

class Coverage(unittest.TestCase):
    def test_matches_scipy_references(self):
        out=js("%s.map(c=>window.esaPropCoverage.compute(...c))"%json.dumps([list(k) for k in REF]),PC)
        for (k,(w,wi,cp)),o in zip(REF.items(),out):
            with self.subTest(case=k):
                self.assertAlmostEqual(o["wald"],w,delta=1e-10)
                self.assertAlmostEqual(o["wilson"],wi,delta=1e-10)
                self.assertAlmostEqual(o["cp"],cp,delta=1e-10)

    def test_independent_python_sum(self):
        cases=[(n,p,l) for n in (1,7,40,200) for p in (0.003,0.1,0.37,0.5,0.9) for l in (90,95,99)]
        out=js("%s.map(c=>window.esaPropCoverage.compute(...c))"%json.dumps(cases),PC)
        for (n,p,l),o in zip(cases,out):
            ref=coverage_py(n,p,l)
            self.assertAlmostEqual(o["wald"],ref["wald"],delta=1e-11,msg=(n,p,l))
            self.assertAlmostEqual(o["wilson"],ref["wilson"],delta=1e-11,msg=(n,p,l))

    def test_clopper_pearson_closed_forms(self):
        a=0.05;iv=js("window.esaPropCoverage.intervals(10,95)",PC)
        # x=0: U = 1 − (α/2)^(1/n); x=n: L = (α/2)^(1/n); beta(1,1) quantiles are linear.
        self.assertAlmostEqual(iv[0]["cp"][1],1-(a/2)**(1/10),delta=1e-13)
        self.assertAlmostEqual(iv[10]["cp"][0],(a/2)**(1/10),delta=1e-13)
        self.assertEqual((iv[0]["cp"][0],iv[10]["cp"][1]),(0,1))
        one=js("window.esaPropCoverage.intervals(1,90)",PC)
        self.assertAlmostEqual(one[0]["cp"][1],0.95,delta=1e-13);self.assertAlmostEqual(one[1]["cp"][0],0.05,delta=1e-13)
        # Clopper–Pearson is conservative: coverage ≥ nominal at every p.
        for n in (5,23,60):
            for o in js("window.esaPropCoverage.curve(%d,95,49)"%n,PC):
                self.assertGreaterEqual(o["cp"],0.95-1e-12,(n,o["p"]))
        # Endpoint at n = 1: p = 0.05 lies on the CP lower limit of x = 1 → covered (closed interval).
        self.assertAlmostEqual(js("window.esaPropCoverage.compute(1,0.05,90)",PC)["cp"],1.0,delta=1e-12)

    def test_invalid_inputs(self):
        for args in ("0,0.5,95","1001,0.5,95","2.5,0.5,95","30,0,95","30,1,95","30,0.5,80","30,NaN,95"):
            self.assertIsNone(js("window.esaPropCoverage.compute(%s)"%args,PC),args)

    def test_pages(self):
        en=page("/inference/confidence-intervals/ci-for-proportion/");ar=page("/ar/inference/confidence-intervals/ci-for-proportion/")
        ids=lambda s,pre:sorted(re.findall(r'id="(%s[^"]*)"'%pre,s))
        for pre in ("esa-pcov-","esa-sp-"):
            self.assertEqual(ids(en,pre),ids(ar,pre),pre)
        self.assertIn('id="esa-pcov-lab" data-locale="ar"',ar);self.assertIn('id="esa-single-proportion-lab" data-locale="ar"',ar)
        for t in (en,ar):
            self.assertIn('<script defer src="/js/proportion-coverage-lab.js"></script>',t)
            for v in (">0.8085<",">0.9742<",">0.9922<"):self.assertIn(v,t)
        self.assertEqual(ar.count("{% include lab-noscript.html %}"),1)
        self.assertLess(en.index('id="esa-pcov-lab"'),en.index("<h2>The Confidence Interval Blueprint Still Applies</h2>"))
        # The English page gained exactly one display formula (test_search now expects 16).
        self.assertEqual(en.count("\\["),16)

NEW={"ci-for-mean-sigma-unknown-t":"/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/",
     "checking-normality-what-and-why":"/inference/assumptions-robustness/checking-normality-what-and-why/",
     "width-and-precision-what-controls":"/inference/confidence-intervals/width-and-precision-what-controls/",
     "ci-for-proportion":"/inference/confidence-intervals/ci-for-proportion/"}

class ArabicLessons(unittest.TestCase):
    def test_pairs_and_links(self):
        pr=pairs();layout=(ROOT/"_layouts/default.html").read_text(encoding="utf-8");home=page("/ar/")
        ids=[l.split(":",1)[1].strip() for l in (ROOT/"_data/translations.yml").read_text(encoding="utf-8").splitlines() if l.startswith("- id:")]
        self.assertEqual(len(ids),len(set(ids)))
        for pid,en in NEW.items():
            ar="/ar"+en
            with self.subTest(pid=pid):
                self.assertEqual(pr[pid],{"en":en,"ar":ar})
                fa=front_matter(ROOT/ar.strip("/")/"index.md");fe=front_matter(ROOT/en.strip("/")/"index.md")
                self.assertEqual((fa["permalink"],fa["lang"],fa["translation_pair"],fa["learning_resource"]),(ar,"ar",pid,"true"))
                self.assertEqual((fe["translation_pair"],fe["learning_resource"]),(pid,"true"))
                self.assertEqual(layout.count('page.translation_pair == "%s"'%pid),1)
                self.assertIn('href="%s"'%ar,page(en));self.assertIn('href="%s"'%ar,home)

    def test_arabic_chain(self):
        chain={"/ar/inference/confidence-intervals/ci-for-mean-sigma-known-z/":"/ar/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/",
               "/ar/inference/assumptions-robustness/independence-and-dependence/":"/ar/inference/assumptions-robustness/checking-normality-what-and-why/"}
        for src,target in chain.items():
            t=page(src);self.assertIn('href="%s"'%target,t);self.assertNotIn('href="%s"'%target[3:],t)

    def test_t_interval_numbers(self):
        t=page("/ar/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/")
        # scipy.stats.t.ppf(q, 24) for q = 0.95, 0.975, 0.995
        q={90:1.710882079909428,95:2.0638985616280245,99:2.796939504774456}
        for c,(qq,me,lo,hi) in {90:(q[90],"5.13","74.87","85.13"),95:(q[95],"6.19","73.81","86.19"),99:(q[99],"8.39","71.61","88.39")}.items():
            self.assertEqual(("%.3f"%qq,"%.2f"%(3*qq),"%.2f"%(80-3*qq),"%.2f"%(80+3*qq)),("%.3f"%qq,me,lo,hi))
            self.assertIn("<td>%.3f</td><td>%s</td><td>[%s, %s]</td>"%(qq,me,lo,hi),t)
        self.assertEqual("%.2f"%(NormalDist().inv_cdf(0.975)*3),"5.88");self.assertIn("5.88",t)
        self.assertEqual(15/math.sqrt(25),3)

    def test_proportion_numbers(self):
        t=page("/ar/inference/confidence-intervals/ci-for-proportion/")
        p,n=0.62,500;se=math.sqrt(p*(1-p)/n);z=1.959963984540054
        self.assertEqual(("%.7f"%se,"%.5f"%(1.96*se)),("0.0217071","0.04255"))
        den=1+z*z/n;c=(p+z*z/(2*n))/den;r=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
        self.assertEqual(("%.4f"%(c-r),"%.4f"%(c+r)),("0.5767","0.6615"))
        for s in ("0.0217071","0.04255","(0.5775, 0.6625)","(0.5767, 0.6615)"):self.assertIn(s,t)

    def test_precision_lab_arabic(self):
        t=page("/ar/inference/confidence-intervals/width-and-precision-what-controls/")
        e=page("/inference/confidence-intervals/width-and-precision-what-controls/")
        ids=lambda s:sorted(re.findall(r'id="(esa-pr-[^"]*)"',s))
        self.assertEqual(ids(t),ids(e));self.assertIn('id="esa-precision-lab" data-locale="ar"',t)
        self.assertEqual(math.ceil((1.959963984540054*20/3)**2),171);self.assertIn("171",t)
        for f in ("js/ci-precision-explorer.js","js/wald-wilson-one-proportion.js","js/newcombe-two-proportion.js","js/proportion-coverage-lab.js"):
            self.assertIn('root.dataset.locale==="ar"',(ROOT/f).read_text(encoding="utf-8"),f)

if __name__=="__main__":unittest.main()
