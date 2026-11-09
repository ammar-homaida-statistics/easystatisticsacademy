"""Batch #86 independent Z, Wilson, Wald, ANOVA, 15-route progress and bilingual SEO benchmarks."""
from pathlib import Path
import json
import math
import re
import subprocess
import unittest

ROOT=Path(__file__).resolve().parents[2]
def node(files,expr):
    code="""const fs=require('fs'),vm=require('vm'),w={};
const ctx={window:w,document:{getElementById:()=>null},queueMicrotask:()=>{}};
for(const p of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(p,'utf8'),ctx);
console.log(JSON.stringify(%s));"""%expr
    result=subprocess.run(["node","-e",code,*[str(ROOT/p) for p in files]],
                          capture_output=True,text=True,check=True)
    return json.loads(result.stdout)

def wilson(x,n,z):
    p=x/n
    d=1+z*z/n
    c=(p+z*z/(2*n))/d
    h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return (max(0,c-h),min(1,c+h))

class Batch86Tests(unittest.TestCase):
    def test_known_sigma_z_independent_normal_survival(self):
        cases=[(100,492,20,500,"two-sided"),(100,492,20,500,"less"),
               (100,492,20,500,"greater"),(25,19,4,20,"two-sided"),
               (1,0,2,0,"two-sided"),(1000,1.7,2.5,1.7,"two-sided")]
        for n,x,sigma,mu,side in cases:
            with self.subTest(n=n,side=side):
                r=node(["js/one-mean-z-explorer.js"],
                      f"w.esaOneMeanZMath.compute({n},{x},{sigma},{mu},'{side}')")
                se=sigma/math.sqrt(n)
                z=(x-mu)/se
                right=lambda x:math.erfc(x/math.sqrt(2))/2
                p=math.erfc(abs(z)/math.sqrt(2)) if side=="two-sided" else (
                    right(z) if side=="greater" else right(-z))
                self.assertAlmostEqual(r["z"],z,places=12)
                self.assertAlmostEqual(r["se"],se,places=12)
                self.assertAlmostEqual(r["pvalue"],p,delta=2e-13)
                self.assertAlmostEqual(r["lower"],x-1.959963984540054*se,places=11)
                self.assertAlmostEqual(r["upper"],x+1.959963984540054*se,places=11)
        self.assertIsNone(node(["js/one-mean-z-explorer.js"],
            "w.esaOneMeanZMath.compute(12,20,0,20,'two-sided')"))

    def test_wald_vs_wilson_independent_benchmarks(self):
        scripts=["js/newcombe-two-proportion.js","js/wald-wilson-one-proportion.js"]
        zmap={90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004}
        for x,n in [(0,5),(5,5),(1,5),(310,500),(50,100),(0,100),(100,100)]:
            for level,z in zmap.items():
                with self.subTest(x=x,n=n,level=level):
                    r=node(scripts,f"w.esaWaldWilsonMath.calculate({x},{n},{level})")
                    p=x/n
                    h=z*math.sqrt(p*(1-p)/n)
                    for actual,expected in zip(r["wald"],(p-h,p+h)):
                        self.assertAlmostEqual(actual,expected,places=12)
                    for actual,expected in zip(r["wilson"],wilson(x,n,z)):
                        self.assertAlmostEqual(actual,expected,places=12)
                    self.assertGreaterEqual(r["wilson"][0],0)
                    self.assertLessEqual(r["wilson"][1],1)
        for expr in ("w.esaWaldWilsonMath.calculate(-1,10,95)",
                     "w.esaWaldWilsonMath.calculate(11,10,95)",
                     "w.esaWaldWilsonMath.calculate(1,0,95)",
                     "w.esaWaldWilsonMath.calculate(1,10,91)"):
            self.assertIsNone(node(scripts,expr))

    def test_independent_one_way_anova_reference(self):
        for groups in (
                [[4,5,6],[5,6,7],[8,9,10]],
                [[2,3,6,7],[3,4],[8,8,9,10,11]],
                [[3,5,7],[3,5,7],[3,5,7]],
                [[1,1,1],[2,2,2],[3,3,3]],
                [[1,1,1],[1,1,1],[1,1,1]]):
            with self.subTest(groups=groups):
                r=node(["js/one-way-anova-explorer.js"],
                       "w.esaAnovaMath.compute("+json.dumps(groups)+")")
                n=sum(map(len,groups))
                means=[sum(g)/len(g) for g in groups]
                grand=sum(map(sum,groups))/n
                ssb=math.fsum(len(g)*(mean-grand)**2 for g,mean in zip(groups,means))
                ssw=math.fsum((x-mean)**2 for g,mean in zip(groups,means) for x in g)
                self.assertAlmostEqual(r["between"],ssb,places=10)
                self.assertAlmostEqual(r["within"],ssw,places=10)
                self.assertEqual(r["df1"],len(groups)-1)
                self.assertEqual(r["df2"],n-len(groups))
                if ssw>0:
                    f=(ssb/(len(groups)-1))/(ssw/(n-len(groups)))
                    self.assertAlmostEqual(r["f"],f,places=10)
                    if len(groups)==3: # Closed form upper F_{2,df2} tail.
                        d=n-len(groups)
                        reference=(d/(d+2*f))**(d/2)
                        self.assertAlmostEqual(r["p"],reference,delta=2e-11)
                elif ssb>0:
                    self.assertIsNone(r["f"]) # infinity JSON serializes to null
                    self.assertEqual(r["p"],0)
                else:
                    self.assertIsNone(r["f"])
                    self.assertIsNone(r["p"])

    def test_foundations_exact_writer_allowlist(self):
        page=(ROOT/"inference/foundations/index.md").read_text()
        chunk=page.split("<!-- CONTINUE READING SCRIPT -->")[-1]
        mapping=chunk.split("const titles = Object.freeze(")[1].split("const legacyTitles")[0]
        matches=re.findall(r'"/inference/foundations/([a-z0-9-]+)/": "([^"]+)"',mapping)
        self.assertEqual(len(matches),15)
        for slug,label in matches:
            writer=(ROOT/"inference/foundations"/slug/"index.md").read_text()
            self.assertIn('label: "'+label+'"',writer)
        self.assertIn('"/inference/foundations/sd-vs-se-common-confusion/": "SD versus SE"',chunk)
        for rule in ("Object.prototype.hasOwnProperty.call(titles,data.url)",
                     "data.label !== titles[data.url]","Number.isSafeInteger(data.ts)",
                     "data.ts>Date.now()+300000","label.replaceChildren","btn.href = data.url"):
            self.assertIn(rule,chunk)

    def test_bilingual_z_metadata_and_numerical_parity(self):
        arroute="/ar/inference/classical-tests/one-sample-z-test-for-mean/"
        enroute="/inference/classical-tests/one-sample-z-test-for-mean/"
        ar=(ROOT/(arroute.strip("/")+"/index.md")).read_text()
        en=(ROOT/(enroute.strip("/")+"/index.md")).read_text()
        layout=(ROOT/"_layouts/default.html").read_text()
        for page in (ar,en):
            for field in ("translation_pair: one-sample-z-test-mean","learning_resource: true","math: true"):
                self.assertIn(field,page)
        for path in (arroute,enroute):self.assertIn(path,layout)
        self.assertIn(arroute,(ROOT/"ar/index.md").read_text())
        self.assertIn('data-locale="ar"',ar)
        self.assertIn('src="/js/one-mean-z-explorer.js"',ar)
        self.assertIn("Z=\\frac{492-500}",ar)
        self.assertIn("0.00006334",ar)
        self.assertIn("id=\"esa-omz-side\"",ar)
        self.assertIn('aria-invalid","true"',(ROOT/"js/one-mean-z-explorer.js").read_text())

    def test_accessible_laboratories(self):
        prop=(ROOT/"inference/confidence-intervals/ci-for-proportion/index.md").read_text()
        anova=(ROOT/"inference/classical-tests/one-way-anova-f-test/index.md").read_text()
        source=(ROOT/"js/one-way-anova-explorer.js").read_text()
        for x in ("a","b","c"):
            self.assertIn(f'id="esa-anova-{x}" rows="2" spellcheck="false" aria-invalid="false" aria-describedby="esa-anova-error"',anova)
        self.assertIn('field.setAttribute("aria-invalid","false")',source)
        for x in ("esa-sp-x","esa-sp-n","esa-sp-level","esa-sp-chart"):
            self.assertIn('id="'+x+'"',prop)
        self.assertIn('src="/js/wald-wilson-one-proportion.js"',prop)

if __name__=="__main__":unittest.main()
