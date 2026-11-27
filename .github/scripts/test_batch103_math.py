"""Batch #103: AR(1) dependence laboratory (variance inflation, effective sample size, real
type I error of a naive z test) verified against direct covariance sums and a seeded
simulation; Arabic lessons on practical significance (with the explorer in Arabic), the
interval blueprint, the z interval for a mean, and independence (with the AR(1) lab).
References: NumPy covariance sums, SciPy 1.18.1 (norm, t) and closed forms."""
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
AR1="js/ar1-dependence-lab.js"

def vif_closed(n,r):
    """Closed form of 1+2Σ(1−k/n)ρ^k, derived independently of the summation in the lab."""
    if r==0:return 1.0
    return 1+2*(r/(1-r)-r*(1-r**n)/(n*(1-r)**2))

def vif_matrix(n,r):
    return sum(r**abs(i-j) for i in range(n) for j in range(n))/n

class AR1Lab(unittest.TestCase):
    def test_inflation_matches_covariance_sum(self):
        cases=[(n,r) for n in (2,3,7,25,100) for r in (-0.95,-0.5,-0.1,0.0,0.3,0.5,0.9,0.95)]
        out=js("%s.map(c=>window.esaAR1.inflation(c[0],c[1]))"%json.dumps(cases),AR1)
        for (n,r),v in zip(cases,out):
            self.assertAlmostEqual(v/vif_matrix(n,r),1,delta=1e-12,msg=(n,r))
            self.assertAlmostEqual(v/vif_closed(n,r),1,delta=1e-10,msg=(n,r))
        # Large n: VIF → (1+ρ)/(1−ρ).
        self.assertAlmostEqual(js("window.esaAR1.inflation(100000,0.5)",AR1),3,delta=1e-4)

    def test_type_one_error_and_defaults(self):
        N=NormalDist()
        for n,r,a in ((100,0.5,0.05),(100,-0.5,0.05),(100,0,0.05),(10,0.9,0.01),(2,0.3,0.5)):
            o=js("window.esaAR1.compute(%d,%r,%r)"%(n,r,a),AR1)
            v=vif_closed(n,r);z=N.inv_cdf(1-a/2)
            self.assertAlmostEqual(o["vif"]/v,1,delta=1e-10)
            self.assertAlmostEqual(o["neff"],n/v,delta=1e-9)
            expected=2*(1-N.cdf(z/math.sqrt(v)))
            self.assertAlmostEqual(o["typeI"]/expected,1,delta=1e-9)
            self.assertAlmostEqual(o["coverage"],1-o["typeI"],delta=1e-15)
        d=js("window.esaAR1.compute(100,0.5,0.05)",AR1)
        self.assertEqual(("%.4f"%d["vif"],"%.1f"%d["neff"],"%.4f"%d["ratio"],"%.6f"%d["typeI"],"%.6f"%d["coverage"]),
                         ("2.9600","33.8","1.7205","0.254617","0.745383"))
        self.assertAlmostEqual(js("window.esaAR1.compute(100,0,0.05)",AR1)["typeI"],0.05,delta=1e-12)

    def test_seeded_simulation_agrees(self):
        import random
        rng=random.Random(103);n,r,R=100,0.5,4000;rej=0;s2=0.0
        for _ in range(R):
            x=rng.gauss(0,1);tot=x
            for _ in range(n-1):
                x=r*x+math.sqrt(1-r*r)*rng.gauss(0,1);tot+=x
            z=tot/math.sqrt(n);s2+=z*z;rej+=abs(z)>1.959963984540054
        p=js("window.esaAR1.compute(100,0.5,0.05)",AR1)["typeI"]
        se=math.sqrt(p*(1-p)/R)
        self.assertLess(abs(rej/R-p),4*se)            # 4 Monte Carlo SEs
        self.assertLess(abs(s2/R/2.96-1),0.1)

    def test_invalid_inputs(self):
        for args in ("1,0.5,0.05","2.5,0.5,0.05","100,0.96,0.05","100,-1,0.05","100,0.5,0","100,0.5,0.6","100,NaN,0.05","200000,0.5,0.05"):
            self.assertIsNone(js("window.esaAR1.compute(%s)"%args,AR1),args)

    def test_pages(self):
        ids=lambda s:sorted(re.findall(r'id="(esa-ar1-[^"]*)"',s))
        en=page("/inference/assumptions-robustness/independence-and-dependence/")
        ar=page("/ar/inference/assumptions-robustness/independence-and-dependence/")
        self.assertEqual(ids(en),ids(ar));self.assertEqual(len(ids(en)),len(set(ids(en))))
        self.assertIn('id="esa-ar1-lab" data-locale="ar"',ar)
        for t in (en,ar):
            self.assertEqual(t.count("{% include lab-noscript.html %}"),1)
            self.assertIn('<script defer src="/js/ar1-dependence-lab.js"></script>',t)
            for v in (">2.9600<",">33.8<",">1.7205<",">0.254617<",">0.745383<"):self.assertIn(v,t)
        self.assertLess(en.index('id="esa-ar1-lab"'),en.index("<h2>Clustered Data</h2>"))
        src=(ROOT/AR1).read_text(encoding="utf-8")
        self.assertIn('root.dataset.locale==="ar"',src)

NEW={"practical-significance":"/inference/hypothesis-testing/practical-significance/",
     "interval-blueprint-estimate-plus-minus":"/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/",
     "ci-for-mean-sigma-known-z":"/inference/confidence-intervals/ci-for-mean-sigma-known-z/",
     "independence-and-dependence":"/inference/assumptions-robustness/independence-and-dependence/"}

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
        chain={"/ar/inference/hypothesis-testing/ci-and-test-connection/":"/ar/inference/hypothesis-testing/practical-significance/",
               "/ar/inference/confidence-intervals/what-is-a-confidence-interval/":"/ar/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/",
               "/ar/inference/confidence-intervals/critical-values-z-and-t/":"/ar/inference/confidence-intervals/ci-for-mean-sigma-known-z/",
               "/ar/inference/assumptions-robustness/heteroscedasticity-variance-issues/":"/ar/inference/assumptions-robustness/independence-and-dependence/"}
        for src,target in chain.items():
            t=page(src);self.assertIn('href="%s"'%target,t);self.assertNotIn('href="%s"'%target[3:],t)
        crit=page("/ar/inference/confidence-intervals/critical-values-z-and-t/")
        self.assertIn('href="/ar/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/"',crit)

    def test_z_interval_numbers(self):
        t=page("/ar/inference/confidence-intervals/ci-for-mean-sigma-known-z/");N=NormalDist()
        self.assertEqual(12/math.sqrt(36),2)
        for c,me,lo,hi in ((0.90,"3.29","46.71","53.29"),(0.95,"3.92","46.08","53.92"),(0.99,"5.15","44.85","55.15")):
            q=N.inv_cdf(1-(1-c)/2)
            self.assertEqual(("%.2f"%(q*2),"%.2f"%(50-q*2),"%.2f"%(50+q*2)),(me,lo,hi))
            self.assertIn("<td>%s</td><td>[%s, %s]</td>"%(me,lo,hi),t)
        self.assertEqual("%.6f"%(N.cdf(1.96)-N.cdf(-1.96)),"0.950004");self.assertIn("0.950004",t)

    def test_blueprint_examples(self):
        t=page("/ar/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/")
        self.assertEqual((62-4,62+4,52-3,52+3),(58,66,49,55))
        for s in ("4 نقاط مئوية","58% إلى 66%","49% إلى 55%"):self.assertIn(s,t)
        self.assertEqual(t.count("\\["),3)

    def test_practical_lab_arabic(self):
        t=page("/ar/inference/hypothesis-testing/practical-significance/")
        e=page("/inference/hypothesis-testing/practical-significance/")
        ids=lambda s:sorted(re.findall(r'id="(esa-ps-[^"]*)"',s))
        self.assertEqual(ids(t),ids(e))
        self.assertIn('id="esa-practical-significance-lab" data-locale="ar"',t)
        self.assertEqual(t.count("{% include lab-noscript.html %}"),1)
        src=(ROOT/"js/practical-significance-explorer.js").read_text(encoding="utf-8")
        self.assertIn('root.dataset.locale==="ar"',src)
        for s in ("دالّ إحصائيًا عند 5%","الفرق المطلق المرصود أقل من العتبة العملية المختارة."):self.assertIn(s,src)
        # Default example: n=400, mean 0.2, sd 1 → t=4, df=399.
        # scipy.stats.t.sf(4, 399)*2 = 7.549295214159842e-05; t.ppf(0.975, 399) CI = [0.10170, 0.29830].
        self.assertIn("0.0000755",t);self.assertIn("[0.102, 0.298]",t)

if __name__=="__main__":unittest.main()
