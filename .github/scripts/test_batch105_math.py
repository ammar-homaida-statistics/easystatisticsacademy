"""Batch #105: seeded CLT / t-interval coverage laboratory (engine replicated exactly by an
independent Python port of its generator, and checked against large independent NumPy
simulations within Monte Carlo error); Arabic lessons on CI conditions, the difference of
proportions (Wald + Newcombe), the difference of means (Welch) and model vs design
assumptions. References: SciPy 1.18.1 (t, ttest_ind_from_stats) and closed forms."""
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
CLT="js/clt-coverage-lab.js"

def mulberry32(seed):
    a=seed&0xFFFFFFFF
    def nxt():
        nonlocal a
        a=(a+0x6D2B79F5)&0xFFFFFFFF;t=a
        t=((t^(t>>15))*(t|1))&0xFFFFFFFF
        t^=(t+(((t^(t>>7))*(t|61))&0xFFFFFFFF))&0xFFFFFFFF
        return ((t^(t>>14))&0xFFFFFFFF)/4294967296
    return nxt

def port(pop,n,level,reps,q,seed=20261127):
    u=mulberry32(seed);spare=[None]
    def g():
        if spare[0] is not None:
            s=spare[0];spare[0]=None;return s
        a=u()
        while a<=0:a=u()
        b=u();r=math.sqrt(-2*math.log(a));spare[0]=r*math.sin(2*math.pi*b);return r*math.cos(2*math.pi*b)
    draw={"normal":g,"uniform":u,"exponential":lambda:-math.log(1-u()),"lognormal":lambda:math.exp(g())}[pop]
    mu={"normal":0,"uniform":.5,"exponential":1,"lognormal":math.exp(.5)}[pop]
    c=b=a=0
    for _ in range(reps):
        x=[draw() for _ in range(n)];m=sum(x)/n;h=q*math.sqrt(sum((v-m)**2 for v in x)/(n-1)/n)
        if m+h<mu:b+=1
        elif m-h>mu:a+=1
        else:c+=1
    return c/reps,b/reps,a/reps

# Independent NumPy references (default_rng(105), 200,000 samples each, 95% t interval):
# coverage, P(interval below μ), P(interval above μ)
NUMPY={("normal",10):(0.949695,0.024985,0.02532),("exponential",10):(0.90072,0.09528,0.004),
       ("exponential",100):(0.94169,0.045515,0.012795),("lognormal",30):(0.88228,0.115525,0.002195),
       ("uniform",5):(0.934095,0.03292,0.032985)}

class CLTLab(unittest.TestCase):
    def test_engine_matches_python_port_exactly(self):
        cases=[("normal",10,95,1500),("exponential",10,95,1500),("lognormal",5,90,1000),("uniform",3,99,1000)]
        out=js("%s.map(c=>{const r=window.esaCLTCoverage.simulate(...c);return [r.coverage,r.missBelow,r.missAbove,r.q]})"%json.dumps(cases),CLT)
        for c,o in zip(cases,out):
            p=port(c[0],c[1],c[2],c[3],o[3])
            for x,y in zip(o[:3],p):self.assertEqual(x,y,c)

    def test_t_quantiles(self):
        # scipy.stats.t.ppf(0.975, 9), t.ppf(0.95, 4), t.ppf(0.995, 2) and closed form for df=1,2.
        for tail,df,ref in ((0.025,9,2.2621571627982053),(0.05,4,2.1318467863266504),(0.005,2,9.924843200918287)):
            self.assertAlmostEqual(js("window.esaCLTCoverage.tQuantile(%r,%d)"%(tail,df),CLT),ref,delta=1e-9)
        self.assertAlmostEqual(js("window.esaCLTCoverage.tQuantile(0.025,1)",CLT),math.tan(math.pi*0.475),delta=1e-9)

    def test_agrees_with_independent_simulation(self):
        cases=[[p,n,95,20000] for p,n in NUMPY]
        out=js("%s.map(c=>{const r=window.esaCLTCoverage.simulate(...c);return [r.coverage,r.missBelow,r.missAbove,r.se]})"%json.dumps(cases),CLT)
        for (k,ref),o in zip(NUMPY.items(),out):
            for x,y in zip(o[:3],ref):
                se=math.sqrt(y*(1-y)/20000+y*(1-y)/200000)
                self.assertLess(abs(x-y),4*se+1e-4,(k,x,y))
        normal=out[0];self.assertLess(abs(normal[0]-0.95),4*normal[3])  # exact for normal data
        exp10=out[1];self.assertGreater(exp10[1],10*exp10[2])           # lopsided misses under skew

    def test_population_means_and_invalid_inputs(self):
        P=js("Object.fromEntries(Object.entries(window.esaCLTCoverage.POP).map(([k,v])=>[k,v.mean]))",CLT)
        self.assertEqual(P,{"normal":0,"uniform":0.5,"exponential":1,"lognormal":math.exp(0.5)})
        for args in ('"normal",1,95,1000','"normal",201,95,1000','"cauchy",10,95,1000','"normal",10,80,1000','"normal",10,95,50','"normal",2.5,95,1000'):
            self.assertIsNone(js("window.esaCLTCoverage.simulate(%s)"%args,CLT),args)

    def test_pages(self):
        en=page("/inference/confidence-intervals/conditions-normality-clt-independence/")
        ar=page("/ar/inference/confidence-intervals/conditions-normality-clt-independence/")
        ids=lambda s:sorted(re.findall(r'id="(esa-clt-[^"]*)"',s))
        self.assertEqual(ids(en),ids(ar));self.assertIn('id="esa-clt-lab" data-locale="ar"',ar)
        d=js('(()=>{const r=window.esaCLTCoverage.simulate("exponential",10,95,20000);return [r.coverage,r.se,r.missBelow,r.missAbove,r.q]})()',CLT)
        for t in (en,ar):
            self.assertEqual(t.count("{% include lab-noscript.html %}"),1)
            self.assertIn('<script defer src="/js/clt-coverage-lab.js"></script>',t)
            for v in d:self.assertIn(">%.4f<"%v,t)
        self.assertLess(en.index('id="esa-clt-lab"'),en.index("<h2>Is n = 30 a Magic Number?</h2>"))
        self.assertIn("التباين المنتهي",ar)  # CLT requires finite variance

NEW={"conditions-normality-clt-independence":"/inference/confidence-intervals/conditions-normality-clt-independence/",
     "ci-for-difference-of-proportions":"/inference/confidence-intervals/ci-for-difference-of-proportions/",
     "ci-for-difference-of-means-independent":"/inference/confidence-intervals/ci-for-difference-of-means-independent/",
     "model-assumptions-vs-design-assumptions":"/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/"}

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
        chain={"/ar/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/":"/ar/inference/confidence-intervals/conditions-normality-clt-independence/",
               "/ar/inference/confidence-intervals/ci-for-proportion/":"/ar/inference/confidence-intervals/ci-for-difference-of-means-independent/",
               "/ar/inference/assumptions-robustness/checking-normality-what-and-why/":"/ar/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/"}
        for src,target in chain.items():
            t=page(src);self.assertIn('href="%s"'%target,t);self.assertNotIn('href="%s"'%target[3:],t)
        prop=page("/ar/inference/confidence-intervals/ci-for-proportion/")
        self.assertIn('href="/ar/inference/confidence-intervals/conditions-normality-clt-independence/"',prop)

    def test_welch_numbers(self):
        W=js("window.esaWelchMath.welch(82,10,40,76,12,35,95)","js/welch-ci-explorer.js")
        v1,v2=100/40,144/35;se=math.sqrt(v1+v2);df=(v1+v2)**2/(v1**2/39+v2**2/34)
        self.assertAlmostEqual(W["se"],se,delta=1e-12);self.assertAlmostEqual(W["df"],df,delta=1e-10)
        # scipy.stats.t.ppf(0.975, 66.47542250283321) = 1.9962979294604513
        self.assertAlmostEqual(W["critical"],1.9962979294604513,delta=1e-9)
        t=page("/ar/inference/confidence-intervals/ci-for-difference-of-means-independent/")
        self.assertEqual(("%.4f"%se,"%.2f"%df,"%.4f"%W["critical"],"%.2f"%W["margin"],"%.2f"%W["lower"],"%.2f"%W["upper"]),("2.5718","66.48","1.9963","5.13","0.87","11.13"))
        for s in ("2.5718","66.48","1.9963","5.13","(0.87,\\,11.13)","(0.86, 11.14)","0.0227"):self.assertIn(s,t)
        # scipy.stats.ttest_ind_from_stats(..., equal_var=False).pvalue = 0.022684984111286475
        self.assertIn('id="esa-welch-explorer" data-locale="ar"',t)
        self.assertIn("root.dataset.locale==='ar'",(ROOT/"js/welch-ci-explorer.js").read_text(encoding="utf-8"))

    def test_difference_of_proportions_numbers(self):
        t=page("/ar/inference/confidence-intervals/ci-for-difference-of-proportions/")
        z=1.959963984540054;p1,p2,n=0.4,0.3,600
        def wilson(p,n):
            den=1+z*z/n;c=(p+z*z/(2*n))/den;r=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den;return c-r,c+r
        (l1,u1),(l2,u2)=wilson(p1,n),wilson(p2,n);d=p1-p2
        lo=d-math.hypot(p1-l1,u2-p2);hi=d+math.hypot(u1-p1,p2-l2)
        N=js("window.esaNewcombeMath.compare(240,600,180,600,95)","js/newcombe-two-proportion.js")
        self.assertAlmostEqual(N["newcombe"][0],lo,delta=1e-12);self.assertAlmostEqual(N["newcombe"][1],hi,delta=1e-12)
        self.assertEqual(("%.4f"%lo,"%.4f"%hi),("0.0461","0.1531"))
        se=math.sqrt(0.00075)
        for s in ("0.0273861","0.053676","(0.0463, 0.1537)","(0.0461, 0.1531)"):self.assertIn(s,t)
        self.assertEqual(("%.7f"%se,"%.6f"%(z*se)),("0.0273861","0.053676"))  # exact z; 1.96 gives 0.053677
        e=page("/inference/confidence-intervals/ci-for-difference-of-proportions/")
        ids=lambda s:sorted(set(re.findall(r'id="(esa-prop-[^"]*)"',s)))
        self.assertEqual(ids(t),ids(e))
        self.assertIn('id="esa-two-proportion-ci-calculator" data-locale="ar"',t)
        self.assertNotIn("percentage points",t)

if __name__=="__main__":unittest.main()
