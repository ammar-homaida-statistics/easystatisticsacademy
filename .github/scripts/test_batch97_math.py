"""Batch #97: Arabic post-hoc and Fisher lessons, Welch's ANOVA, a Tukey–Kramer
lab with an in-browser studentized range distribution, an accurate erfc in
the Fisher–Pearson lab with Yates' correction, and Arabic home completeness.
Reference values come from SciPy 1.18.1 (f_oneway(equal_var=False),
studentized_range, tukey_hsd, chi2_contingency, ttest_ind)."""
import json
import math
import re
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
ANOVA="js/one-way-anova-explorer.js";TUKEY="js/tukey-hsd-lab.js"
FISHER="js/fisher-chi-square-2x2.js";MC="js/multiple-comparisons-explorer.js"
POSTHOC="inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview"
FISHER_PAGE="inference/classical-tests/fisher-exact-vs-chi-square"

def js(expression,files):
    runner='''const fs=require("fs"),vm=require("vm"),window={},document={getElementById:()=>null};
for(const f of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(f,"utf8"),{window,document});
console.log(JSON.stringify(%s));'''%expression
    p=subprocess.run(["node","-e",runner,*[str(ROOT/f) for f in files]],text=True,capture_output=True,check=True)
    return json.loads(p.stdout)

def front_matter(path):
    text=path.read_text(encoding="utf-8");head=text.split("---",2)[1] if text.startswith("---") else ""
    return dict(re.findall(r'^([A-Za-z_]+):\s*"?(.*?)"?\s*$',head,re.M))

WELCH=[([[4,5,6],[5,6,7],[8,9,10]],11.142857142857142,0.023156899810964086),
       ([[2,3,6,7],[3,4],[8,8,9,10,11]],24.517732673187357,0.003899111040941173),
       ([[1.2,3.4,2.2,5.1],[2.0,2.5,2.9],[3.3,4.1,6.0,5.5,4.4],[0.4,1.1,2.6]],5.667095804926844,0.040616971574685974),
       ([[1,2],[1,9]],0.7538461538461538,0.5412492992483426)]
PT_REF=[(0.5,2,1,0.7836531040612145),(3,3,1,0.41033295547761817),(20,6,1,0.10074415645247037),
        (200,6,1,0.010110478016628677),(3.5,3,6,0.10539962552471227),(4.339,3,6,0.05000850982561411),
        (2,4,10,0.5189626756123746),(5,5,30,0.01089001881367857),(3,6,120,0.28347999609061036),
        (8,3,3,0.02218827912027277),(1,2,1000,0.4796648624378571),(4,6,594,0.05442430958302724)]
Q_REF=[(0.05,3,6,4.3391954765202785),(0.05,2,1,17.969287064187434),(0.01,6,1,202.20971938676414),
       (0.05,4,12,4.198660231300105),(0.1,5,30,3.647891607281081),(0.05,6,594,4.043301976612626)]
TUKEY_REF=[([[4,5,6],[5,6,7],[8,9,10]],[(0,1,0.48272727950311844,-3.505235676435389,1.505235676435389),
             (0,2,0.006493721153864596,-6.5052356764353885,-1.494764323564611),(1,2,0.024229053412424206,-5.5052356764353885,-0.4947643235646111)]),
           ([[2,3,6,7],[3,4],[8,8,9,10,11]],[(0,1,0.7907892945157978,-3.312871783759289,5.312871783759289),
             (0,2,0.009530059209792663,-8.040736118565519,-1.359263881434479),(1,2,0.011096662388447531,-9.866629991764395,-1.5333700082356048)]),
           ([[1.2,3.4,2.2,5.1],[2.0,2.5,2.9],[3.3,4.1,6.0,5.5,4.4],[0.4,1.1,2.6]],
            [(0,1,0.9446446186736879,-2.2736162909447897,3.2902829576114554),(0,2,0.22014125091835712,-4.128414357144948,0.7584143571449489),
             (0,3,0.35018084684366635,-1.1736162909447894,4.390282957611456),(1,2,0.11831801097682904,-4.853385957864756,0.4667192911980913),
             (1,3,0.6893398275150464,-1.8740292460894932,4.074029246089494),(2,3,0.015098864466910222,0.6332807088019092,5.953385957864757)])]
CHI_REF=[([1,9,11,3],0.000925274037119762,0.00375221010087385),([50,5,5,50],9.39184360617324e-18,4.841992505721753e-17),
         ([0,5,5,0],0.001565402258002549,0.01141203638600166),([30,10,12,40],7.176912617245018e-07,2.0809119932452127e-06),
         ([120,80,60,140],1.6372964502968553e-09,3.0344594161766796e-09)]

class WelchAnova(unittest.TestCase):
    def test_matches_scipy(self):
        for groups,f,p in WELCH:
            with self.subTest(groups=groups):
                r=js("window.esaAnovaMath.welch(%s)"%json.dumps(groups),[ANOVA])
                self.assertTrue(r["defined"]);self.assertEqual(r["df1"],len(groups)-1)
                self.assertAlmostEqual(r["f"],f,delta=1e-10*f);self.assertAlmostEqual(r["p"],p,delta=1e-12)
    def test_two_groups_equal_welch_t_squared(self):
        r=js("window.esaAnovaMath.welch([[3.1,4.7,5.2,6.0],[5.5,6.1,7.4,8.2,6.6]])",[ANOVA])
        self.assertAlmostEqual(r["f"],6.724907063197024,places=10);self.assertAlmostEqual(r["p"],0.04062964433542555,places=12)
    def test_undefined_with_a_constant_group_and_classical_unchanged(self):
        self.assertFalse(js("window.esaAnovaMath.welch([[1,1,1],[2,3,4],[5,6,8]])",[ANOVA])["defined"])
        self.assertIsNone(js("window.esaAnovaMath.welch([[1],[2,3]])",[ANOVA]))
        r=js("window.esaAnovaMath.compute([[4,5,6],[5,6,7],[8,9,10]])",[ANOVA])
        self.assertEqual((r["f"],round(r["p"],6)),(13,0.006592))

class StudentizedRange(unittest.TestCase):
    def test_upper_tail_matches_scipy(self):
        got=js("%s.map(([q,k,nu])=>window.esaTukey.ptukeyUpper(q,k,nu))"%json.dumps([c[:3] for c in PT_REF]),[TUKEY])
        for (q,k,nu,ref),g in zip(PT_REF,got):
            with self.subTest(q=q,k=k,nu=nu):self.assertAlmostEqual(g,ref,delta=1e-9)
    def test_quantiles_match_scipy(self):
        got=js("%s.map(([a,k,nu])=>window.esaTukey.qtukey(a,k,nu))"%json.dumps([c[:3] for c in Q_REF]),[TUKEY])
        for (a,k,nu,ref),g in zip(Q_REF,got):
            with self.subTest(a=a,k=k,nu=nu):self.assertAlmostEqual(g/ref,1,delta=1e-8)
    def test_boundaries(self):
        self.assertEqual(js("[0,-1,Infinity].map(q=>window.esaTukey.ptukeyUpper(q,3,6))",[TUKEY]),[1,1,0])
        self.assertEqual(js("[window.esaTukey.ptukeyUpper(2,1,6),window.esaTukey.ptukeyUpper(2,3,0),window.esaTukey.qtukey(0,3,6),window.esaTukey.qtukey(1,3,6)]",[TUKEY]),[None]*4)
        # Monotone decreasing in q.
        tail=js("[1,2,3,4,5,6,8].map(q=>window.esaTukey.ptukeyUpper(q,4,9))",[TUKEY])
        self.assertTrue(all(a>b for a,b in zip(tail,tail[1:])))
    def test_infinite_df_limit(self):
        # k=2, nu=infinity: Q = sqrt(2)|Z|, so P(Q >= q) = 2(1 - Phi(q / sqrt 2)) = erfc(q / 2).
        for q in (0.5,2.0,4.0):
            self.assertAlmostEqual(js("window.esaTukey.ptukeyUpper(%r,2,Infinity)"%q,[TUKEY]),math.erfc(q/2),delta=1e-12)

class TukeyKramer(unittest.TestCase):
    def test_matches_scipy_tukey_hsd(self):
        for groups,ref in TUKEY_REF:
            r=js("window.esaTukey.compute(%s,0.05)"%json.dumps(groups),[TUKEY])
            self.assertEqual(len(r["pairs"]),len(ref))
            for pr,(i,j,p,lo,hi) in zip(r["pairs"],ref):
                with self.subTest(groups=groups,pair=(i,j)):
                    self.assertEqual((pr["i"],pr["j"]),(i,j))
                    self.assertAlmostEqual(pr["p"],p,delta=1e-9)
                    self.assertAlmostEqual(pr["lower"],lo,delta=1e-8);self.assertAlmostEqual(pr["upper"],hi,delta=1e-8)
    def test_two_groups_equal_pooled_t_test(self):
        r=js("window.esaTukey.compute([[3.1,4.7,5.2,6.0],[5.5,6.1,7.4,8.2,6.6]],0.05)",[TUKEY])
        self.assertAlmostEqual(r["pairs"][0]["p"],0.03345787996935352,delta=1e-9)
    def test_lesson_values_and_invalid_input(self):
        r=js("window.esaTukey.compute([[4,5,6],[5,6,7],[8,9,10]])",[TUKEY])
        self.assertEqual((r["k"],r["nu"],r["msw"],round(r["qcrit"],4)),(3,6,1,4.3392))
        for bad in ("[[1,2]]","[[1],[2,3]]","[[1,2],[3,NaN]]","[[1,2],[3,4]],1","[[1,2],[3,4]],0",
                    json.dumps([[1,2]]*7),"[[1,2],[3,4e7]]"):
            with self.subTest(bad=bad):self.assertIsNone(js("window.esaTukey.compute(%s)"%bad,[TUKEY]))
        flat=js("window.esaTukey.compute([[1,1],[2,2],[2,2]])",[TUKEY])
        self.assertTrue(flat["degenerate"])
        self.assertIsNone(flat["pairs"][1]["q"])  # equal means, MSW = 0: 0/0 is undefined
        self.assertIsNone(flat["pairs"][0]["q"])  # Infinity serializes as null
        self.assertEqual(flat["pairs"][0]["p"],0)

class FisherPearson(unittest.TestCase):
    def test_pearson_and_yates_match_scipy(self):
        for cells,p,py in CHI_REF:
            with self.subTest(cells=cells):
                r=js("window.esaFisherChiMath.compute(%s)"%",".join(map(str,cells)),[FISHER])
                self.assertAlmostEqual(r["chiP"]/p,1,delta=1e-9)
                self.assertAlmostEqual(r["yatesP"]/py,1,delta=1e-9)
        r=js("window.esaFisherChiMath.compute(1,9,11,3)",[FISHER])
        self.assertEqual(round(r["fisher"],8),0.00275946)

    def test_old_approximation_removed(self):
        src=(ROOT/FISHER).read_text(encoding="utf-8")
        self.assertNotIn(".3275911",src)
        self.assertIn('root.dataset.locale==="ar"',src)
        for s in ("بيرسون","فيشر","Pearson uses χ² with 1 df"):self.assertTrue(s in src,s)

class SharedEngines(unittest.TestCase):
    def test_english_strings_are_unchanged(self):
        mc=(ROOT/MC).read_text(encoding="utf-8")
        for s in ('"Holm rejects "','"Reject H₀"','"Do not reject H₀"','root.dataset.locale==="ar"',"يرفض إجراء هولم"):
            self.assertIn(s,mc)
        self.assertNotIn("innerHTML",(ROOT/TUKEY).read_text(encoding="utf-8"))

class ArabicLessons(unittest.TestCase):
    def check(self,slug,pair,scripts,values):
        en=ROOT/"inference/classical-tests"/slug/"index.md";ar=ROOT/"ar/inference/classical-tests"/slug/"index.md"
        fe,fa=front_matter(en),front_matter(ar)
        self.assertEqual((fe["translation_pair"],fa["translation_pair"]),(pair,pair))
        self.assertEqual((fe["learning_resource"],fa["learning_resource"],fa["lang"]),("true","true","ar"))
        e=en.read_text(encoding="utf-8");a=ar.read_text(encoding="utf-8")
        self.assertIn('href="/ar/inference/classical-tests/%s/"'%slug,e);self.assertIn('href="/inference/classical-tests/%s/"'%slug,a)
        self.assertEqual(a.count("{% include lab-noscript.html %}"),1)
        for s in scripts:self.assertIn(s,a);self.assertIn(s,e)
        ids=lambda s:sorted(set(re.findall(r'id="(esa-[a-z]+-[a-z0-9-]+)"',s)))
        self.assertEqual(ids(a),ids(e))
        for v in values:self.assertIn(v,a)
        yml=(ROOT/"_data/translations.yml").read_text(encoding="utf-8")
        self.assertIn("- id: %s\n  en: /inference/classical-tests/%s/\n  ar: /ar/inference/classical-tests/%s/"%(pair,slug,slug),yml)
        self.assertIn('page.translation_pair == "%s"'%pair,(ROOT/"_layouts/default.html").read_text(encoding="utf-8"))
    def test_post_hoc(self):
        self.check("post-hoc-tests-and-multiple-comparisons-preview","post-hoc-tests",
                   ["/js/tukey-hsd-lab.js","/js/multiple-comparisons-explorer.js"],["0.642",'data-locale="ar"',"4.3392"])
    def test_fisher(self):
        self.check("fisher-exact-vs-chi-square","fisher-exact",["/js/fisher-chi-square-2x2.js"],["0.00275946","0.00375221"])
    def test_anova_next_lesson_and_hub_links_are_arabic(self):
        anova=(ROOT/"ar/inference/classical-tests/one-way-anova-f-test/index.md").read_text(encoding="utf-8")
        self.assertNotIn('href="/'+POSTHOC+'/"',anova);self.assertIn('href="/ar/'+POSTHOC+'/"',anova)
        hub=(ROOT/"ar/inference/classical-tests/index.md").read_text(encoding="utf-8")
        for slug in (POSTHOC,FISHER_PAGE):
            self.assertIn('href="/ar/%s/"'%slug,hub);self.assertNotIn('href="/%s/" hreflang="en"'%slug,hub)
        for page in ("chi-square-independence-test","chi-square-goodness-of-fit","two-proportion-z-test"):
            t=(ROOT/"ar/inference/classical-tests"/page/"index.md").read_text(encoding="utf-8")
            self.assertNotIn('href="/'+FISHER_PAGE+'/"',t);self.assertIn('href="/ar/'+FISHER_PAGE+'/"',t)

class ArabicHome(unittest.TestCase):
    def test_every_arabic_lesson_is_linked_from_arabic_home(self):
        home=(ROOT/"ar/index.md").read_text(encoding="utf-8")
        pages=[p.parent.relative_to(ROOT).as_posix() for p in (ROOT/"ar").rglob("index.md") if p.parent!=ROOT/"ar"]
        self.assertGreaterEqual(len(pages),50)
        for page in pages:
            with self.subTest(page=page):self.assertIn('href="/%s/"'%page,home)

if __name__=="__main__":unittest.main()
