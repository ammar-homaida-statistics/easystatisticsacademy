"""Batch #99: Arabic significance-level and effect-size lessons, Mann–Whitney and
Wilcoxon signed-rank laboratory, accurate normal tails in the last four
approximate-erfc engines, and a site-wide rule that lets display formulas
scroll on narrow screens. References: SciPy 1.18.1 (mannwhitneyu, wilcoxon,
norm, lognorm, ttest_ind_from_stats), math.erfc and brute-force enumeration."""
import itertools
import json
import math
import re
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RT="js/rank-tests-lab.js";TP="js/two-proportion-z-explorer.js"

def js(expression,files):
    runner='''const fs=require("fs"),vm=require("vm"),window={},document={getElementById:()=>null};
for(const f of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(f,"utf8"),{window,document});
console.log(JSON.stringify(%s));'''%expression
    p=subprocess.run(["node","-e",runner,*[str(ROOT/f) for f in files]],text=True,capture_output=True,check=True)
    return json.loads(p.stdout)

def front_matter(path):
    text=path.read_text(encoding="utf-8");head=text.split("---",2)[1] if text.startswith("---") else ""
    return dict(re.findall(r'^([A-Za-z_]+):\s*"?(.*?)"?\s*$',head,re.M))

MW_X=[12.1,14.3,11.8,15.2,13.9,12.7];MW_Y=[15.8,16.4,14.9,17.2,18.1]
MW_REF={"two-sided":(0.008658008658008658,0.01371083007813322),"greater":(0.9978354978354979,0.9959434413672171),
        "less":(0.004329004329004329,0.00685541503906661)}
TIES_A=[3,4,4,5,6,6,7,8,9,9];TIES_B=[5,6,7,7,8,9,10,10,11,12]
TIES_REF={"two-sided":0.036490193433198544,"greater":0.9849006495737658,"less":0.018245096716599272}
WX_X=[142,151,138,160,147,156,149,163];WX_Y=[135,149,132,151,144,146,150,152]
WX_REF={"two-sided":(0.015625,0.017290280592906253),"greater":(0.0078125,0.008645140296453127),"less":(0.99609375,0.9913548597035469)}

def mw_brute(x,y,side):
    pool=x+y;n1=len(x);order={v:i+1 for i,v in enumerate(sorted(pool))}
    u1=sum(order[v] for v in x)-n1*(n1+1)/2;u2=n1*len(y)-u1
    us=[sum(order[pool[i]] for i in c)-n1*(n1+1)/2 for c in itertools.combinations(range(len(pool)),n1)]
    ge=lambda k:sum(u>=k for u in us)/len(us)
    return {"greater":ge(u1),"less":ge(u2),"two-sided":min(1,2*ge(max(u1,u2)))}[side]

def wx_brute(d,side):
    n=len(d);order=sorted(range(n),key=lambda i:abs(d[i]));rk=[0]*n
    for k,i in enumerate(order):rk[i]=k+1
    tp=sum(rk[i] for i in range(n) if d[i]>0);ts=[sum(rk[i] for i in range(n) if m>>i&1) for m in range(2**n)]
    ge=sum(t>=tp for t in ts)/2**n;le=sum(t<=tp for t in ts)/2**n
    return {"greater":ge,"less":le,"two-sided":min(1,2*min(ge,le))}[side]

class RankTests(unittest.TestCase):
    def test_mann_whitney_matches_scipy(self):
        for side,(pe,pa) in MW_REF.items():
            r=js("window.esaRankTests.mannWhitney(%s,%s,%s)"%(MW_X,MW_Y,json.dumps(side)),[RT])
            with self.subTest(side=side):
                self.assertEqual((r["U1"],r["U2"]),(1,29))
                self.assertAlmostEqual(r["pExact"],pe,delta=1e-15);self.assertAlmostEqual(r["pApprox"],pa,delta=1e-14)
            t=js("window.esaRankTests.mannWhitney(%s,%s,%s)"%(TIES_A,TIES_B,json.dumps(side)),[RT])
            with self.subTest(ties=side):
                self.assertFalse(t["exactAvailable"]);self.assertIsNone(t["pExact"])
                self.assertAlmostEqual(t["pApprox"],TIES_REF[side],delta=1e-14)
        r=js("window.esaRankTests.mannWhitney(%s,%s)"%(MW_X,MW_Y),[RT])
        diffs=sorted(a-b for a in MW_X for b in MW_Y)
        self.assertAlmostEqual(r["hodgesLehmann"],(diffs[14]+diffs[15])/2,places=12)
        self.assertAlmostEqual(r["rankBiserial"],2*1/30-1,places=14)

    def test_wilcoxon_matches_scipy(self):
        for side,(pe,pa) in WX_REF.items():
            r=js("window.esaRankTests.wilcoxon(%s,%s,%s)"%(WX_X,WX_Y,json.dumps(side)),[RT])
            with self.subTest(side=side):
                self.assertEqual((r["tPlus"],r["tMinus"],r["n"]),(35,1,8))
                self.assertAlmostEqual(r["pExact"],pe,delta=1e-15);self.assertAlmostEqual(r["pApprox"],pa,delta=1e-14)
        t=js("window.esaRankTests.wilcoxon([1,2,2,0,-3,4,5,5,0,6,7],null)",[RT])
        self.assertEqual((t["zeros"],t["n"],t["exactAvailable"]),(2,9,False))
        self.assertAlmostEqual(t["pApprox"],0.028124450117384896,delta=1e-14)
        self.assertAlmostEqual(t["rankBiserial"],(t["tPlus"]-t["tMinus"])/(t["tPlus"]+t["tMinus"]),places=14)

    def test_exact_distributions_against_brute_force(self):
        import random
        rnd=random.Random(99);cases=[];ref=[]
        for _ in range(12):
            x=rnd.sample(range(100),rnd.randint(1,6));y=rnd.sample([v for v in range(100) if v not in x],rnd.randint(1,6))
            for s in ("two-sided","greater","less"):cases.append(["mannWhitney",x,y,s]);ref.append(mw_brute(x,y,s))
        for _ in range(12):
            n=rnd.randint(1,11);d=[v*rnd.choice([-1,1]) for v in rnd.sample(range(1,60),n)]
            for s in ("two-sided","greater","less"):cases.append(["wilcoxon",d,None,s]);ref.append(wx_brute(d,s))
        got=js("%s.map(([f,...a])=>window.esaRankTests[f](...a).pExact)"%json.dumps(cases),[RT])
        for c,g,r in zip(cases,got,ref):
            with self.subTest(case=c):self.assertAlmostEqual(g,r,delta=1e-14)
        # Distribution totals: C(m+n, m) arrangements and 2^n sign patterns.
        self.assertEqual(sum(js("window.esaRankTests.mwuCounts(7,9)",[RT])),math.comb(16,7))
        self.assertEqual(sum(js("window.esaRankTests.wilcoxonCounts(15)",[RT])),2**15)

    def test_boundaries_and_invalid_input(self):
        z=js("window.esaRankTests.wilcoxon([0,0,0],null)",[RT])
        self.assertFalse(z["defined"]);self.assertIsNone(z["pApprox"])
        one=js("window.esaRankTests.mannWhitney([1],[2])",[RT]);self.assertAlmostEqual(one["pExact"],1.0)
        for bad in ("mannWhitney([],[1])","mannWhitney([1],[NaN])","mannWhitney([1],[2],'both')",
                    "wilcoxon([1,2],[1])","mannWhitney(%s,[1])"%json.dumps(list(range(51))),"mannWhitney([2e6],[1])"):
            with self.subTest(bad=bad):self.assertIsNone(js("window.esaRankTests.%s"%bad,[RT]))
        src=(ROOT/RT).read_text(encoding="utf-8");self.assertNotIn("innerHTML",src)
        self.assertIn('root.dataset.locale==="ar"',src)

class AccurateNormalTails(unittest.TestCase):
    def test_no_approximate_erfc_left_in_any_lab(self):
        offenders=[p.name for p in (ROOT/"js").glob("*.js") if "0.3275911" in p.read_text(encoding="utf-8") or ".3275911" in p.read_text(encoding="utf-8")]
        self.assertEqual(offenders,[])
    def test_two_proportion_tails_have_relative_accuracy(self):
        cases=[[120,200,90,200,"two-sided"],[1,500,60,500,"less"],[400,500,10,500,"greater"],[5,40,30,40,"two-sided"]]
        got=js("%s.map(a=>window.esaTwoProportionMath.compute(...a))"%json.dumps(cases),[TP])
        for (x1,n1,x2,n2,s),g in zip(cases,got):
            pp=(x1+x2)/(n1+n2);z=(x1/n1-x2/n2)/math.sqrt(pp*(1-pp)*(1/n1+1/n2))
            up=0.5*math.erfc(z/math.sqrt(2));lo=0.5*math.erfc(-z/math.sqrt(2))
            ref={"two-sided":min(1,2*min(up,lo)),"greater":up,"less":lo}[s]
            with self.subTest(case=(x1,n1,x2,n2,s)):self.assertLessEqual(abs(g["p"]-ref),1e-12*ref+1e-300)
        r=js("window.esaTwoProportionMath.compute(120,200,90,200)",[TP])
        self.assertEqual(round(r["p"],6),0.002667)  # z = 0.15 / sqrt(0.525 * 0.475 * 0.01) = 3.0038
    def test_errors_lab_power_uses_direct_tail(self):
        src=(ROOT/"js/type1-type2-errors-lab.js").read_text(encoding="utf-8")
        self.assertIn("const power=cdf(-c-shift)+cdf(shift-c);",src)
        c=1.959963984540054;s=0.5*math.sqrt(30);Phi=lambda x:0.5*math.erfc(-x/math.sqrt(2))
        self.assertEqual(f"{100*(Phi(-c-s)+Phi(s-c)):.2f}%","78.19%")

class DisplayMathOverflow(unittest.TestCase):
    def test_screen_rule_present_and_print_rule_kept(self):
        css=(ROOT/"css/style.css").read_text(encoding="utf-8")
        m=re.search(r'@media screen\{\s*mjx-container\[display="true"\]\{([^}]*)\}',css)
        self.assertIsNotNone(m)
        for prop in ("display:block","max-width:100%","overflow-x:auto"):self.assertIn(prop,m.group(1))
        self.assertIn("mjx-container { max-width: 100% !important; overflow: visible !important; }",css)

class ArabicLessons(unittest.TestCase):
    def check(self,section,slug,pair,values):
        url="/%s/%s/"%(section,slug);en=ROOT/section/slug/"index.md";ar=ROOT/"ar"/section/slug/"index.md"
        fe,fa=front_matter(en),front_matter(ar)
        self.assertEqual((fe["translation_pair"],fa["translation_pair"]),(pair,pair))
        self.assertEqual((fe.get("learning_resource"),fa["learning_resource"],fa["lang"]),("true","true","ar"))
        e=en.read_text(encoding="utf-8");a=ar.read_text(encoding="utf-8")
        self.assertIn('href="/ar%s"'%url,e);self.assertIn('href="%s"'%url,a)
        yml=(ROOT/"_data/translations.yml").read_text(encoding="utf-8")
        self.assertIn("- id: %s\n  en: %s\n  ar: /ar%s"%(pair,url,url),yml)
        self.assertIn('page.translation_pair == "%s"'%pair,(ROOT/"_layouts/default.html").read_text(encoding="utf-8"))
        self.assertIn('href="/ar%s"'%url,(ROOT/"ar/index.md").read_text(encoding="utf-8"))
        for v in values:self.assertIn(v,a)
        return e,a
    def test_significance_level(self):
        e,a=self.check("inference/hypothesis-testing","significance-level-alpha","significance-level-alpha",
                       [r"\sup_{\theta\in\Theta_0}P_\theta(\text{reject }H_0)\le0.05","p ≤ α"])
        pv=(ROOT/"ar/inference/hypothesis-testing/p-value-meaning/index.md").read_text(encoding="utf-8")
        self.assertIn('href="/ar/inference/hypothesis-testing/significance-level-alpha/"',pv)
        self.assertIn('href="/ar/inference/hypothesis-testing/type1-type2-errors/"',a)
    def test_effect_size_and_worked_example(self):
        e,a=self.check("inference/power-sample-size","effect-size-and-practical-importance","effect-size",
                       [r"\sqrt{122}\approx11.045","0.543","1.921","0.061","0.535"])
        for v in (r"\sqrt{122}\approx11.045","0.543","1.921","0.061","0.535"):self.assertIn(v,e)
        sp=math.sqrt((24*100+24*144)/48);d=6/sp;t=6/(sp*math.sqrt(2/25))
        self.assertEqual((round(sp,3),round(d,3),round(t,3)),(11.045,0.543,1.921))
        self.assertEqual(round(d*(1-3/(4*48-1)),3),0.535)
        # Two-sided t p-value with 48 df by Simpson integration of the t density
        # (SciPy ttest_ind_from_stats gives 0.060739540825732664).
        df=48;c=math.exp(math.lgamma((df+1)/2)-math.lgamma(df/2))/math.sqrt(df*math.pi)
        f=lambda x:c*(1+x*x/df)**(-(df+1)/2);m=20000;h=t/m
        cdf_mid=h/3*(f(0)+f(t)+sum((4 if k%2 else 2)*f(k*h) for k in range(1,m)))
        self.assertAlmostEqual(1-2*cdf_mid,0.060739540825732664,delta=1e-9)
        pw=(ROOT/"ar/inference/power-sample-size/what-is-statistical-power/index.md").read_text(encoding="utf-8")
        self.assertIn('href="/ar/inference/power-sample-size/effect-size-and-practical-importance/"',pw)

if __name__=="__main__":unittest.main()
