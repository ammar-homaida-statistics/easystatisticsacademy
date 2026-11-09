"""Batch #85: independent Wilson/Newcombe, chi-square, metadata and progress benchmarks."""
from pathlib import Path
import json
import math
import re
import subprocess
import unittest

ROOT=Path(__file__).resolve().parents[2]
def run_js(path,expression):
    script="""const fs=require('fs'),vm=require('vm'),w={};
vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),{
 window:w,document:{getElementById:()=>null}
});
console.log(JSON.stringify(%s));"""%expression
    result=subprocess.run(["node","-e",script,str(ROOT/path)],
                          capture_output=True,text=True,check=True)
    return json.loads(result.stdout)

def wilson_python(x,n,z):
    p=x/n
    denom=1+z*z/n
    middle=(p+z*z/(2*n))/denom
    half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/denom
    return max(0,middle-half),min(1,middle+half)

def newcombe_python(x1,n1,x2,n2,z):
    a,b=x1/n1,x2/n2
    left1,right1=wilson_python(x1,n1,z)
    left2,right2=wilson_python(x2,n2,z)
    d=a-b
    return (d-math.hypot(a-left1,right2-b),d+math.hypot(right1-a,b-left2))

class Batch85MathTests(unittest.TestCase):
    def test_newcombe_independent_reference(self):
        z={90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004}
        for x1,n1,x2,n2 in [(240,600,180,600),(0,10,2,10),(10,10,0,10),
                             (0,10,0,10),(5,5,5,5),(1,3,2,7),(50,100,50,100)]:
            for level,critical in z.items():
                with self.subTest(x1=x1,n1=n1,x2=x2,n2=n2,level=level):
                    result=run_js("js/newcombe-two-proportion.js",
                                  "w.esaNewcombeMath.compare(%d,%d,%d,%d,%d)"%
                                  (x1,n1,x2,n2,level))
                    reference=newcombe_python(x1,n1,x2,n2,critical)
                    for got,want in zip(result["newcombe"],reference):
                        self.assertAlmostEqual(got,want,places=12)
                    p1,p2=x1/n1,x2/n2
                    se=math.sqrt(p1*(1-p1)/n1+p2*(1-p2)/n2)
                    self.assertAlmostEqual(result["wald"][0],p1-p2-critical*se,places=12)
                    self.assertAlmostEqual(result["wald"][1],p1-p2+critical*se,places=12)
    def test_newcombe_invalid(self):
        for expr in ("w.esaNewcombeMath.compare(11,10,2,10,95)",
                     "w.esaNewcombeMath.compare(0,0,1,10,95)",
                     "w.esaNewcombeMath.compare(1,10,2,10,91)"):
            self.assertIsNone(run_js("js/newcombe-two-proportion.js",expr))
    def test_homogeneity_independent_pearson_reference(self):
        for rows in ([[40,35,25],[30,45,25],[50,30,20]],
                     [[10,10],[10,10]],[[5,20,15],[8,10,12]],[[0,10],[8,12]]):
            with self.subTest(rows=rows):
                data=run_js("js/chi-square-homogeneity-explorer.js",
                            "w.esaHomogeneityMath.compute("+json.dumps(rows)+")")
                N=sum(map(sum,rows))
                row=[sum(a) for a in rows]
                col=[sum(a[j] for a in rows) for j in range(len(rows[0]))]
                e=[[r*c/N for c in col] for r in row]
                chi=math.fsum((rows[i][j]-e[i][j])**2/e[i][j]
                    for i in range(len(rows)) for j in range(len(col)))
                self.assertAlmostEqual(data["chi"],chi,places=11)
                self.assertEqual(data["df"],(len(row)-1)*(len(col)-1))
                self.assertEqual(data["smallExpected"],min(sum(e,[]))<5)
                if data["df"]==1:
                    p=math.erfc(math.sqrt(chi/2))
                elif data["df"]==4:
                    half=chi/2
                    p=math.exp(-half)*(1+half)
                else:
                    continue
                self.assertAlmostEqual(data["p"],p,places=10)
        self.assertEqual(run_js("js/chi-square-homogeneity-explorer.js",
                         "w.esaHomogeneityMath.gammaQ(1,0)"),1)
    def test_homogeneity_rejects_zero_margins(self):
        for rows in ([[0,0],[10,20]],[[0,10],[0,20]],[[10,0],[0,0]]):
            self.assertIsNone(run_js("js/chi-square-homogeneity-explorer.js",
                                   "w.esaHomogeneityMath.compute("+json.dumps(rows)+")"))
    def test_ci_progress_exact_map_and_safe_time(self):
        page=(ROOT/"inference/confidence-intervals/index.md").read_text()
        chunk=page.split("<!-- CONTINUE READING SCRIPT -->")[-1]
        self.assertIn("Object.prototype.hasOwnProperty.call(titles,data.url)",chunk)
        self.assertIn("data.label !== titles[data.url]",chunk)
        self.assertIn("Number.isSafeInteger(data.ts)",chunk)
        self.assertIn("label.replaceChildren",chunk)
        self.assertIn("localStorage.getItem(KEY)",chunk)
        self.assertIn("catch (e)",chunk)
        routes=re.findall(r'"/inference/confidence-intervals/([a-z0-9-]+)/": "([^"]+)"',chunk)
        self.assertEqual(len(routes),12)
        for suffix,label in routes:
            text=(ROOT/"inference/confidence-intervals"/suffix/"index.md").read_text()
            self.assertIn('label: "'+label+'"',text)
    def test_bilingual_metadata(self):
        ar="/ar/inference/classical-tests/decision-framework-and-assumptions/"
        en="/inference/classical-tests/decision-framework-and-assumptions/"
        a=(ROOT/(ar.strip("/")+"/index.md")).read_text()
        e=(ROOT/(en.strip("/")+"/index.md")).read_text()
        layout=(ROOT/"_layouts/default.html").read_text()
        for page in (a,e):
            self.assertIn("translation_pair: classical-tests-framework",page)
            self.assertIn("learning_resource: true",page)
        self.assertIn("lang: ar",a)
        self.assertIn("classical-tests-framework",layout)
        self.assertIn(ar,layout)
        self.assertIn(en,layout)
        self.assertIn(ar,(ROOT/"ar/index.md").read_text())
        self.assertIn("t=\\frac{18-20}",a)
    def test_labs_accessibility_sources(self):
        hom=(ROOT/"inference/classical-tests/chi-square-homogeneity-test/index.md").read_text()
        code=(ROOT/"js/chi-square-homogeneity-explorer.js").read_text()
        prop=(ROOT/"inference/confidence-intervals/ci-for-difference-of-proportions/index.md").read_text()
        self.assertIn('aria-describedby="esa-hom-error esa-hom-warning"',hom)
        self.assertIn('aria-invalid="false"',hom)
        self.assertIn('input.setAttribute("aria-invalid","true")',code)
        self.assertIn('input.setAttribute("aria-invalid","false")',code)
        self.assertIn('id="esa-prop-compare-chart"',prop)
        self.assertIn('src="/js/newcombe-two-proportion.js"',prop)

if __name__=="__main__":unittest.main()
