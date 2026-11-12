"""Batch #90: independent SciPy exact-binomial benchmarks, one-proportion parity, SEO and Diagnostics security."""
import json
import math
from pathlib import Path
import subprocess
import unittest

ROOT=Path(__file__).resolve().parents[2]
SCRIPTS=("js/one-proportion-z-explorer.js","js/exact-binomial-vs-z.js",
         "js/two-proportion-z-explorer.js")
def js(expr):
    runner="""const fs=require('fs'),vm=require('vm');
const w={},ctx={window:w,document:{getElementById:()=>null}};
for(const p of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(p,'utf8'),ctx);
console.log(JSON.stringify(%s));"""%expr
    r=subprocess.run(["node","-e",runner,*[str(ROOT/p) for p in SCRIPTS]],
                     check=True,capture_output=True,text=True)
    return json.loads(r.stdout)

class Batch90Math(unittest.TestCase):
    def test_exact_binomial_independent_scipy_binomtest_references(self):
        # Values independently established by scipy.stats.binomtest with
        # its probability-ordering two-sided convention (not doubled tails).
        fixtures=(
          (0,10,.5,(.001953125,1.,.0009765625)),
          (2,10,.5,(.109375,.9892578125,.0546875)),
          (8,10,.5,(.109375,.0546875,.9892578125)),
          (12,20,.3,(.005936084198097523,.0051381615351214025,.9987211203957798)),
          (120,200,.5,(.005685155996750306,.002842577998375153,.998182526023735)),
          (1,100,.01,(1.,.6339676587267705,.7357619789229564)),
          (200,200,.5,(1.2446030555722283e-60,6.223015277861142e-61,1.)),
          (500,1000,.5,(1.,.5126125090891802,.5126125090891802)),
        )
        for x,n,p,ref in fixtures:
            for alternative,expected in zip(("two-sided","greater","less"),ref):
                with self.subTest(x=x,n=n,p=p,alternative=alternative):
                    r=js("w.esaExactBinomial.compute(%d,%d,%r,%s)"%
                         (x,n,p,json.dumps(alternative)))
                    self.assertTrue(0<=r["exact"]<=1)
                    self.assertAlmostEqual(r["exact"],expected,delta=max(2e-10*expected,2e-13))
                    self.assertEqual(r["adequate"], n*p>=10 and n*(1-p)>=10)
                    self.assertAlmostEqual(r["absDifference"],abs(r["exact"]-r["approx"]),places=14)
    def test_bad_exact_inputs_and_z_reuse(self):
        for args in ((-1,10,.5),(11,10,.5),(1,0,.5),(1,2001,.5),
                     (1,10,0),(1,10,1),(1,10,-.1),(1,10,1.1),(1.5,10,.5)):
            with self.subTest(args=args):
                self.assertIsNone(js("w.esaExactBinomial.compute("+",".join(map(str,args))+")"))
        self.assertAlmostEqual(js("w.esaOneProportionMath.compute(120,200,.5).z"),
                               2.82842712474619,places=12)
        self.assertAlmostEqual(js("w.esaExactBinomial.compute(120,200,.5).approx"),
                               js("w.esaOneProportionMath.compute(120,200,.5).pvalue"),places=14)
        # Source-level safeguard: no network calls / unsafe interpolation.
        for path in SCRIPTS:
            source=(ROOT/path).read_text()
            self.assertNotIn("eval(",source)
            self.assertNotIn("innerHTML =",source)
    def test_two_proportion_independent_reference_and_accessible_errors(self):
        r=js("w.esaTwoProportionMath.compute(120,200,90,200)")
        # Independently: p_pool=.525, difference=.15, SE=sqrt(.525*.475*(.01)).
        expected=.15/math.sqrt(.525*.475*(1/200+1/200))
        self.assertAlmostEqual(r["z"],expected,places=12)
        self.assertTrue(r["adequate"])
        self.assertTrue(js("w.esaTwoProportionMath.compute(0,20,0,30)")["degenerate"])
        code=(ROOT/"js/two-proportion-z-explorer.js").read_text()
        self.assertIn('field.setAttribute("aria-invalid","true")',code)
        self.assertIn('field.setAttribute("aria-invalid","false")',code)
    def test_translation_metadata_and_explanation(self):
        en=(ROOT/"inference/classical-tests/one-proportion-z-test/index.md").read_text()
        ar=(ROOT/"ar/inference/classical-tests/one-proportion-z-test/index.md").read_text()
        layout=(ROOT/"_layouts/default.html").read_text()
        for source in (ar,en):
            self.assertIn("translation_pair: one-proportion-z",source)
            self.assertIn("learning_resource: true",source)
        self.assertIn("lang: ar",ar)
        self.assertIn("data-locale=\"ar\"",ar)
        self.assertIn("np_0",ar)
        for path in ("/ar/inference/classical-tests/one-proportion-z-test/",
                     "/inference/classical-tests/one-proportion-z-test/"):
            self.assertIn(path,layout)
        for path in ("probability/random-variables/what-is-a-random-variable/index.md",
                     "ar/probability/random-variables/what-is-a-random-variable/index.md"):
            self.assertIn("learning_resource: true",(ROOT/path).read_text())
    def test_diagnostics_future_ts_rejection_and_writer_titles(self):
        source=(ROOT/"modeling/diagnostics/index.md").read_text()
        self.assertIn("data.ts > Date.now()+5*60*1000",source)
        self.assertIn('published.get(data.url) !== data.label',source)
        self.assertEqual(source.count('["/modeling/diagnostics/'),9)
        self.assertIn('strong.textContent = data.label',source)

if __name__=="__main__":
    unittest.main()
