"""Batch #92: independent residuals/GOF numerical references, route security and SEO."""
import json
import math
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
def js(expression,files):
    runner='''const fs=require("fs"),vm=require("vm"),window={},document={getElementById:()=>null};
for(const f of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(f,"utf8"),{window,document});
console.log(JSON.stringify(%s));'''%expression
    p=subprocess.run(["node","-e",runner,*[str(ROOT/f) for f in files]],text=True,capture_output=True,check=True)
    return json.loads(p.stdout)

class Batch92Math(unittest.TestCase):
    def test_ols_independent_hand_calculation(self):
        # x=(1,2,3,4,5), y=(2,4,5,4,5): xbar=3, ybar=4,
        # Sxx=10, Sxy=6 -> slope=.6, intercept=2.2.
        r=js("window.esaResidualOLS.compute([1,2,3,4,5],[2,4,5,4,5])",["js/ols-residual-explorer.js"])
        self.assertAlmostEqual(r["slope"],.6,places=12)
        self.assertAlmostEqual(r["intercept"],2.2,places=12)
        self.assertAlmostEqual(r["sse"],2.4,places=12)
        self.assertAlmostEqual(r["sst"],6,places=12)
        self.assertAlmostEqual(r["r2"],.6,places=12)
        self.assertAlmostEqual(sum(r["residuals"]),0,places=12)
        self.assertAlmostEqual(sum(x*e for x,e in zip(r["xs"],r["residuals"])),0,places=12)
    def test_ols_boundaries(self):
        file=["js/ols-residual-explorer.js"]
        cases=["([1,1,1],[2,3,4])","([1,2,3],[5,5,5])",
               "([1,2],[3,4])","([1,2,3],[3,4])","([1,2,1001],[3,4,5])"]
        for x in cases:
            self.assertIsNone(js("window.esaResidualOLS.compute"+x,file))
        r=js("window.esaResidualOLS.compute([-2,0,2],[-3,1,5])",file)
        self.assertAlmostEqual(r["slope"],2,places=12)
        self.assertAlmostEqual(r["intercept"],1,places=12)
        self.assertAlmostEqual(r["sse"],0,places=12)
        self.assertAlmostEqual(r["r2"],1,places=12)
    def test_shared_gof_reference(self):
        r=js("window.esaChiSquareGofMath.compute([8,11,9,13,10,9],[1/6,1/6,1/6,1/6,1/6,1/6])",["js/chi-square-gof-explorer.js"])
        self.assertAlmostEqual(r["statistic"],1.6,places=12)
        self.assertEqual(r["df"],5)
        # Reference: scipy.stats.chi2.sf(1.6,5) = 0.9012493445012737.
        self.assertAlmostEqual(r["p"],.9012493445012737,delta=2e-9)
        self.assertTrue(all(abs(v-10)<1e-12 for v in r["expected"]))
    def test_metadata_and_security(self):
        en=(ROOT/"inference/classical-tests/chi-square-goodness-of-fit/index.md").read_text()
        ar=(ROOT/"ar/inference/classical-tests/chi-square-goodness-of-fit/index.md").read_text()
        layout=(ROOT/"_layouts/default.html").read_text()
        index=(ROOT/"modeling/simple-linear-regression/index.md").read_text()
        for s in (en,ar):
            self.assertIn("translation_pair: chi-square-gof",s)
            self.assertIn("learning_resource: true",s)
        self.assertIn("lang: ar",ar)
        self.assertIn('data-locale="ar"',ar)
        self.assertIn("const ar=!!", (ROOT/"js/chi-square-gof-explorer.js").read_text())
        self.assertIn("/ar/inference/classical-tests/chi-square-goodness-of-fit/",layout)
        self.assertIn("/inference/classical-tests/chi-square-goodness-of-fit/",layout)
        self.assertIn("label.textContent",index)
        self.assertNotIn("label.innerHTML",index)
        self.assertIn("Date.now()+5*60*1000",index)
        self.assertIn("lessons.get(data.url)!==data.label",index)
        self.assertEqual(index.count('["/modeling/simple-linear-regression/'),9)
        for slug in ("what-is-regression","regression-equation","slope","intercept","residuals","least-squares","r-squared","correlation-vs-regression","prediction"):
            s=(ROOT/f"modeling/simple-linear-regression/{slug}/index.md").read_text()
            self.assertIn("try {",s)
            self.assertIn("esa_continue_modeling_simple_linear_regression_lesson_v0",s)

if __name__=="__main__":unittest.main()
