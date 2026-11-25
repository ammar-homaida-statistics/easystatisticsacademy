"""Batch #102: Arabic lessons "What is a hypothesis test?", "Confidence intervals and tests"
(with the interval/test lab in Arabic), "Heteroscedasticity" (with the Levene/Brown–Forsythe
lab in Arabic) and "Critical values for z and t"; an llms.txt index generated at build time.
References: SciPy 1.18.1 (binom, norm, t) and closed forms."""
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

NEW={"what-is-a-hypothesis-test":"/inference/hypothesis-testing/what-is-a-hypothesis-test/",
     "ci-and-test-connection":"/inference/hypothesis-testing/ci-and-test-connection/",
     "heteroscedasticity-variance-issues":"/inference/assumptions-robustness/heteroscedasticity-variance-issues/",
     "critical-values-z-and-t":"/inference/confidence-intervals/critical-values-z-and-t/"}

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
        chain={"/ar/inference/hypothesis-testing/null-and-alternative/":"/ar/inference/hypothesis-testing/what-is-a-hypothesis-test/",
               "/ar/inference/hypothesis-testing/one-sided-vs-two-sided/":"/ar/inference/hypothesis-testing/ci-and-test-connection/",
               "/ar/inference/assumptions-robustness/outliers-and-influence/":"/ar/inference/assumptions-robustness/heteroscedasticity-variance-issues/"}
        for src,target in chain.items():
            t=page(src);self.assertIn('href="%s"'%target,t);self.assertNotIn('href="%s"'%target[3:],t)

    def test_coin_example(self):
        # scipy.stats.binom.sf(89, 100, 0.5) = 1.5316450877189923e-17; exact sum below.
        tail=sum(math.comb(100,k) for k in range(90,101))/2**100
        self.assertAlmostEqual(tail/1.5316450877189923e-17,1,delta=1e-12)
        self.assertIn("1.5 × 10⁻¹⁷",page("/ar/inference/hypothesis-testing/what-is-a-hypothesis-test/"))

    def test_critical_value_table(self):
        t=page("/ar/inference/confidence-intervals/critical-values-z-and-t/")
        rows={r[0]:r[1:] for r in re.findall(r'<tr><td>([^<]+)</td><td>([\d.]+)</td><td>([\d.]+)</td><td>([\d.]+)</td></tr>',t)}
        # scipy.stats.t.ppf(1 - (1 - c) / 2, df) for c = 0.90, 0.95, 0.99.
        ref={"1":(6.313751514675037,12.706204736174694,63.656741162871526),
             "2":(2.9199855803537242,4.302652729749462,9.924843200918287),
             "5":(2.0150483733330233,2.5705818356363146,4.032142983555228),
             "10":(1.8124611228116756,2.228138851986274,3.16927267261695),
             "30":(1.697260886593957,2.0422724563012378,2.7499956535672254),
             "100":(1.6602343260853392,1.9839715185235518,2.6258905214380173)}
        for df,vals in ref.items():
            self.assertEqual(rows[df],tuple("%.3f"%v for v in vals),df)
        # Closed forms: df=1 (Cauchy) q = tan(πc/2); df=2 q = (1−2a)·sqrt(2/(4a(1−a))) with a=(1−c)/2.
        for c,v in zip((0.90,0.95,0.99),ref["1"]):self.assertAlmostEqual(math.tan(math.pi*c/2),v,delta=1e-9)
        for c,v in zip((0.90,0.95,0.99),ref["2"]):
            a=(1-c)/2;self.assertAlmostEqual((1-2*a)*math.sqrt(2/(4*a*(1-a))),v,delta=1e-9)
        N=NormalDist()
        self.assertEqual(rows["∞ (z)"],tuple("%.3f"%N.inv_cdf(1-(1-c)/2) for c in (0.90,0.95,0.99)))
        self.assertAlmostEqual(N.cdf(1.96)-N.cdf(-1.96),0.950004209703559,delta=1e-12)
        self.assertEqual("%.5f"%N.inv_cdf(0.975),"1.95996");self.assertIn("1.95996",t)
        self.assertAlmostEqual(1.96*2,3.92);self.assertIn("3.92",t)
        self.assertAlmostEqual(ref["1"][1]/N.inv_cdf(0.975),6.48,delta=0.01)  # "about six and a half times"

class BilingualLabs(unittest.TestCase):
    def test_ci_lab_arabic(self):
        t=page("/ar/inference/hypothesis-testing/ci-and-test-connection/");e=page("/inference/hypothesis-testing/ci-and-test-connection/")
        self.assertIn('id="esa-cid-lab" data-locale="ar"',t)
        ids=lambda s:sorted(re.findall(r'id="(esa-cid-[^"]*)"',s))
        self.assertEqual(ids(t),ids(e));self.assertEqual(t.count("{% include lab-noscript.html %}"),1)
        self.assertIn('<script defer src="/js/ci-test-duality-lab.js"></script>',t)
        src=(ROOT/"js/ci-test-duality-lab.js").read_text(encoding="utf-8")
        self.assertIn('root.dataset.locale==="ar"',src)
        for s in ("نعم — μ₀ داخل الفترة","لا — μ₀ خارج الفترة","الفترة والاختبار متفقان."):self.assertIn(s,src)
        r=js('window.esaCiTestDuality.compute({method:"t",side:"two-sided",mean:104.2,sd:8.5,n:25,mu0:100,alpha:0.05})',"js/ci-test-duality-lab.js")
        for v in ("t(24) = %.4f"%r["crit"],"95%%: [%.4f, %.4f]"%(r["lower"],r["upper"]),"t = %.4f"%r["stat"],">%.6f<"%r["p"],"لا — μ₀ خارج الفترة"):
            self.assertIn(v,t)

    def test_levene_lab_arabic(self):
        t=page("/ar/inference/assumptions-robustness/heteroscedasticity-variance-issues/")
        e=page("/inference/assumptions-robustness/heteroscedasticity-variance-issues/")
        self.assertIn('id="esa-lv-lab" data-locale="ar"',t)
        ids=lambda s:sorted(re.findall(r'id="(esa-lv-[^"]*)"',s))
        self.assertEqual(ids(t),ids(e));self.assertEqual(t.count("{% include lab-noscript.html %}"),1)
        groups=[[12.1,13.4,11.8,12.9,13.1,12.4],[10.2,14.8,9.5,15.6,11.9,13.7],[12.5,12.8,13.0,12.2,12.6,12.9]]
        r=js('window.esaLevene.compute(%s,"median")'%json.dumps(groups),"js/levene-lab.js")
        self.assertIn(">%.4f</output>"%r["W"],t);self.assertIn(">%.6f</output>"%r["p"],t)
        self.assertAlmostEqual(r["W"],16.261753108886854,delta=1e-9)  # scipy.stats.levene(center="median")

class LlmsTxt(unittest.TestCase):
    def test_template(self):
        t=(ROOT/"llms.txt").read_text(encoding="utf-8")
        self.assertTrue(t.startswith("---\nlayout: null\npermalink: /llms.txt\n---\n"))
        self.assertIn("# Easy Statistics Academy",t);self.assertIn("## English lessons",t);self.assertIn("## الدروس العربية",t)
        self.assertIn('top != "courses" and top != "code-lab"',t)
        self.assertIn('parts[2] != "courses" and parts[2] != "code-lab"',t)
        self.assertIn("p.robots_noindex != true",t)

    def test_repository_robots_allows_all(self):
        lines=[l.strip() for l in (ROOT/"robots.txt").read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
        self.assertEqual(lines[:2],["User-agent: *","Allow: /"])
        self.assertFalse([l for l in lines if l.lower().startswith("disallow")])

if __name__=="__main__":unittest.main()
