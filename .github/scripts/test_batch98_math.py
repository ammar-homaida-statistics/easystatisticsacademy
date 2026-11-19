"""Batch #98: Arabic p-value, statistical power and exact-binomial lessons;
bilingual p-value and exact-binomial engines; accurate one-proportion Z tails;
a Kruskal–Wallis laboratory; and a guard against stale English links on
Arabic pages. References: SciPy 1.18.1 (binomtest, norm, kruskal), Python's
math.erfc, and exact enumeration of rank relabelings."""
import itertools
import json
import math
import re
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
PV="js/pvalue-interpretation-explorer.js";OP="js/one-proportion-z-explorer.js"
EB="js/exact-binomial-vs-z.js";KW="js/kruskal-wallis-lab.js"

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
    yml=(ROOT/"_data/translations.yml").read_text(encoding="utf-8")
    return dict(re.findall(r'^\s+en:\s*(\S+)\n\s+ar:\s*(\S+)',yml,re.M))

BINOM=[(2,10,.5,"two-sided",0.109375),(0,10,.5,"two-sided",0.001953125),(10,10,.5,"greater",0.0009765625),
       (3,40,.02,"two-sided",0.04567023044071665),(7,12,.2,"less",0.99941875712),
       (1990,2000,.99,"two-sided",0.02358184655960595),(500,2000,.25,"greater",0.5085832112651493)]
KRUSKAL=[([[2.1,3.4,1.9,5.6,2.8],[4.2,6.1,5.5,7.3,4.9],[8.8,6.7,9.4,7.9,12.5]],10.640000000000015,0.004892753725239441),
         ([[1,2,2,3,3,3],[2,3,3,4,4,5],[3,4,5,5,5,6]],9.18977438136826,0.010103360469876454),
         ([[1.2,3.1,2.2],[2.8,4.0,3.6],[5.1,4.4]],5.361111111111107,0.06852507409185578),
         ([[0.3,-1.2,2.5,0.8],[1.1,1.9],[3.3,2.0,4.1,2.2,5.0],[-0.5,0.1,0.0]],8.974285714285713,0.029634732843749425)]

def normal_tail(z,side):
    up=0.5*math.erfc(z/math.sqrt(2));lo=0.5*math.erfc(-z/math.sqrt(2))
    return {"two-sided":min(1,2*min(up,lo)),"right":up,"greater":up,"left":lo,"less":lo}[side]

class PValueEngine(unittest.TestCase):
    def test_matches_normal_tails_with_relative_accuracy(self):
        cases=[(z,s) for z in (0,0.5,1.645,1.96,2,3.5,8,20,35,-0.5,-2,-8,-35) for s in ("left","right","two-sided")]
        got=js("%s.map(([z,s])=>window.esaPvalueMath.pvalue(z,s))"%json.dumps(cases),[PV])
        for (z,s),g in zip(cases,got):
            ref=normal_tail(z,s)
            with self.subTest(z=z,side=s):self.assertLessEqual(abs(g-ref),1e-12*max(ref,1e-300)+1e-300)
        self.assertEqual(js('[36,-36,NaN].map(z=>window.esaPvalueMath.pvalue(z,"two-sided"))',[PV]),[None]*3)
        self.assertIsNone(js('window.esaPvalueMath.pvalue(1,"both")',[PV]))
    def test_bilingual_strings_without_forking_the_math(self):
        src=(ROOT/PV).read_text(encoding="utf-8")
        self.assertIn('root.dataset.locale==="ar"',src);self.assertEqual(src.count("function pvalue("),1)
        for s in ('"Reject":"Do not reject"','" the null at α = "',"لا نرفض","ليست احتمال أن تكون الفرضية الصفرية صحيحة"):
            self.assertTrue(s in src,s)

class OneProportionAndExactBinomial(unittest.TestCase):
    FILES=[OP,EB]
    def test_exact_binomial_matches_scipy(self):
        got=js("%s.map(a=>window.esaExactBinomial.compute(...a).exact)"%json.dumps([list(c[:4]) for c in BINOM]),self.FILES)
        for c,g in zip(BINOM,got):
            with self.subTest(case=c[:4]):self.assertAlmostEqual(g,c[4],delta=1e-11)
    def test_z_tails_have_relative_accuracy(self):
        cases=[(120,200,.5,"two-sided"),(40,300,.2,"less"),(10,300,.2,"less"),(290,300,.8,"greater"),
               (1,2000,.5,"two-sided"),(0,500,.3,"less"),(500,500,.7,"greater"),(7,12,.2,"less")]
        got=js("%s.map(a=>window.esaOneProportionMath.compute(...a))"%json.dumps([list(c) for c in cases]),self.FILES)
        for (x,n,p,s),g in zip(cases,got):
            z=(x/n-p)/math.sqrt(p*(1-p)/n);ref=normal_tail(z,s)
            with self.subTest(case=(x,n,p,s)):
                self.assertAlmostEqual(g["z"],z,places=10)
                self.assertLessEqual(abs(g["pvalue"]-ref),1e-11*ref+1e-300)
        self.assertEqual(round(got[0]["pvalue"],6),0.004678)
        src=(ROOT/OP).read_text(encoding="utf-8");self.assertNotIn("0.3275911",src)
    def test_binomial_lab_is_bilingual_and_english_unchanged(self):
        src=(ROOT/EB).read_text(encoding="utf-8")
        self.assertIn('root.dataset.locale==="ar"',src)
        for s in ("Warning: at least one expected count is below 10","0 (below display precision)","تقريب Z الطبيعي غير موثوق","الحدّاني الدقيق"):
            self.assertTrue(s in src,s)

def exact_kw_pvalue(groups):
    """Exact permutation p-value by enumerating every relabeling of the pooled ranks."""
    pool=[x for g in groups for x in g];order=sorted(range(len(pool)),key=lambda i:pool[i])
    ranks=[0.0]*len(pool);i=0
    while i<len(order):
        j=i
        while j+1<len(order) and pool[order[j+1]]==pool[order[i]]:j+=1
        for m in range(i,j+1):ranks[order[m]]=(i+j)/2+1
        i=j+1
    n=[len(g) for g in groups];N=len(pool)
    def S(assign):return sum(sum(ranks[i] for i in idx)**2/len(idx) for idx in assign)
    start=0;obs_assign=[]
    for ni in n:obs_assign.append(list(range(start,start+ni)));start+=ni
    obs=S(obs_assign);hit=tot=0
    def rec(rem,gi,acc):
        nonlocal hit,tot
        if gi==len(n)-1:
            tot+=1
            if S(acc+[rem])>=obs-1e-9*max(1,obs):hit+=1
            return
        for c in itertools.combinations(rem,n[gi]):
            rec([i for i in rem if i not in c],gi+1,acc+[list(c)])
    rec(list(range(N)),0,[])
    return hit/tot

class KruskalWallis(unittest.TestCase):
    def test_h_and_chi_square_p_match_scipy(self):
        for groups,h,p in KRUSKAL:
            with self.subTest(groups=groups):
                r=js("window.esaKruskal.compute(%s,{permutations:0})"%json.dumps(groups),[KW])
                self.assertTrue(r["defined"])
                self.assertAlmostEqual(r["Hc"],h,delta=1e-10);self.assertAlmostEqual(r["p"],p,delta=1e-12)
                self.assertAlmostEqual(r["epsilon2"],h/(sum(map(len,groups))-1),delta=1e-12)
        ties=js("window.esaKruskal.compute(%s,{permutations:0})"%json.dumps(KRUSKAL[1][0]),[KW])
        self.assertAlmostEqual(ties["H"],8.687134502923968,delta=1e-9);self.assertAlmostEqual(ties["C"],0.9453044375644994,delta=1e-12)

    def test_permutation_p_within_monte_carlo_error_of_exact(self):
        for groups in ([[1.2,3.1,2.2],[2.8,4.0,3.6],[5.1,4.4]],[[1,2,2,3],[2,3,4],[3,4,5,5]],[[3,1,2,2],[2,5,4],[6,6,1]]):
            exact=exact_kw_pvalue(groups)
            r=js("window.esaKruskal.compute(%s,{permutations:20000,seed:98})"%json.dumps(groups),[KW])
            se=math.sqrt(exact*(1-exact)/20000)
            with self.subTest(groups=groups,exact=exact):
                self.assertLessEqual(abs(r["pPerm"]-exact),4*se+1/20001)
                self.assertAlmostEqual(r["sePerm"],math.sqrt(r["pPerm"]*(1-r["pPerm"])/20000),places=12)
        a=js("window.esaKruskal.compute([[1,2],[3,4],[5,6]])",[KW]);b=js("window.esaKruskal.compute([[1,2],[3,4],[5,6]])",[KW])
        self.assertEqual(a["pPerm"],b["pPerm"])  # fixed seed: reproducible

    def test_boundaries_and_invalid_input(self):
        tied=js("window.esaKruskal.compute([[1,1,1],[1,1]])",[KW])
        self.assertFalse(tied["defined"]);self.assertIsNone(tied["Hc"]);self.assertIsNone(tied["p"])
        sep=js("window.esaKruskal.compute([[1,2,3],[4,5,6]],{permutations:20000})",[KW])
        self.assertAlmostEqual(sep["pPerm"],0.1,delta=4*math.sqrt(.09/20000))  # exact 2/20
        for bad in ("[[1,2]]","[[1],[2]]",json.dumps([[1]]*7),"[[1,2],[3,NaN]]","[[1,2],[3,2e6]]",
                    "[[1,2],[3,4]],{permutations:-1}","[[1,2],[3,4]],{permutations:1.5}"):
            with self.subTest(bad=bad):self.assertIsNone(js("window.esaKruskal.compute(%s)"%bad,[KW]))
        self.assertNotIn("innerHTML",(ROOT/KW).read_text(encoding="utf-8"))

class ArabicLessons(unittest.TestCase):
    def check(self,section,slug,pair,values,scripts=()):
        en=ROOT/section/slug/"index.md";ar=ROOT/"ar"/section/slug/"index.md"
        fe,fa=front_matter(en),front_matter(ar)
        self.assertEqual((fe["translation_pair"],fa["translation_pair"]),(pair,pair))
        self.assertEqual((fe.get("learning_resource"),fa["learning_resource"],fa["lang"]),("true","true","ar"))
        e=en.read_text(encoding="utf-8");a=ar.read_text(encoding="utf-8")
        url="/%s/%s/"%(section,slug)
        self.assertIn('href="/ar%s"'%url,e);self.assertIn('href="%s"'%url,a)
        self.assertEqual(pairs().get(url),"/ar"+url)
        self.assertIn('page.translation_pair == "%s"'%pair,(ROOT/"_layouts/default.html").read_text(encoding="utf-8"))
        for s in scripts:self.assertIn(s,a);self.assertIn('data-locale="ar"',a)
        if scripts:
            self.assertEqual(a.count("{% include lab-noscript.html %}"),1)
            ids=lambda s:sorted(set(re.findall(r'id="(esa-[a-z]+-[a-z0-9-]+)"',s)))
            self.assertEqual(ids(a),ids(e))
        for v in values:self.assertIn(v,a)
        self.assertIn('href="/ar%s"'%url,(ROOT/"ar/index.md").read_text(encoding="utf-8"))
    def test_p_value(self):
        self.check("inference/hypothesis-testing","p-value-meaning","p-value-meaning",
                   [r"3.0632901754\times10^{-17}",r"1.5316450877\times10^{-17}","0.000465"],["/js/pvalue-interpretation-explorer.js"])
    def test_power(self):
        self.check("inference/power-sample-size","what-is-statistical-power","what-is-statistical-power",["0.269","0.804","87.2"])
        e=(ROOT/"inference/power-sample-size/what-is-statistical-power/index.md").read_text(encoding="utf-8")
        for v in ("0.269","0.804","87.2"):self.assertIn(v,e)
    def test_exact_binomial(self):
        self.check("inference/classical-tests","exact-binomial-vs-z-test","exact-binomial",["0.109375","112/1024","0.057780"],
                   ["/js/exact-binomial-vs-z.js","/js/one-proportion-z-explorer.js"])
        hub=(ROOT/"ar/inference/classical-tests/index.md").read_text(encoding="utf-8")
        self.assertIn('href="/ar/inference/classical-tests/exact-binomial-vs-z-test/"',hub)
    def test_worked_power_numbers(self):
        z=1.959963984540054;Phi=lambda x:0.5*math.erfc(-x/math.sqrt(2))
        power=lambda n:Phi(0.3*math.sqrt(n)-z)+Phi(-0.3*math.sqrt(n)-z)
        self.assertEqual((round(power(20),3),round(power(88),3)),(0.269,0.804));self.assertGreater(power(2000),1-1e-12)
        self.assertAlmostEqual(((z+0.8416212335729143)/0.3)**2,87.2,delta=0.01)
        self.assertLess(power(87),0.8);self.assertGreaterEqual(power(88),0.8)

class StaleEnglishLinks(unittest.TestCase):
    def test_arabic_pages_link_to_arabic_counterparts(self):
        en2ar=pairs();bad=[]
        for p in sorted((ROOT/"ar").rglob("index.md")):
            own="/"+p.parent.relative_to(ROOT/"ar").as_posix()+"/"
            for url in re.findall(r'<a\b[^>]*\bhref="(/[^"#?]*)"',p.read_text(encoding="utf-8")):
                if url in en2ar and url!=own:bad.append((p.parent.relative_to(ROOT).as_posix(),url))
        self.assertEqual(bad,[])

if __name__=="__main__":unittest.main()
