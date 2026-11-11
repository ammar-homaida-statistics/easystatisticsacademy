"""Batch #89: independent SciPy-referenced t and Monte Carlo fixtures, Reporting and bilingual metadata."""
import json
import math
from pathlib import Path
import re
import subprocess
import unittest
ROOT=Path(__file__).resolve().parents[2]
SCRIPTS=["js/welch-two-sample-explorer.js","js/pooled-two-sample-comparison.js","js/welch-pooled-monte-carlo.js"]
def node(expression):
    code="""const fs=require('fs'),vm=require('vm'),w={};
const ctx={window:w,document:{getElementById:()=>null}};
for(const path of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(path,'utf8'),ctx);
console.log(JSON.stringify(%s));"""%expression
    p=subprocess.run(["node","-e",code,*[str(ROOT/x) for x in SCRIPTS]],check=True,capture_output=True,text=True)
    return json.loads(p.stdout)

class Batch89Math(unittest.TestCase):
    def test_welch_pooled_independent_scipy_references(self):
        a=[73,77,80,78,82,79,84];b=[70,68,74,71,75,69]
        arg=json.dumps(a)+","+json.dumps(b)
        w=node("w.esaWelchMath.compute("+arg+")")
        p=node("w.esaPooledTMath.compute("+arg+")")
        for name,actual,expected in [
          ("Welch t",w["t"],4.446189534952488),
          ("Welch df",w["df"],10.93790675014491),
          ("Welch p",w["p"],.0009985114499363515),
          ("Pooled t",p["t"],4.357746205649742),
          ("Pooled df",p["df"],11),
          ("Pooled p",p["p"],.0011405670691066125),
          ("Welch lower",w["lower"],3.9529320996062487),
          ("Pooled lower",p["lower"],3.8769187999754386)]:
            with self.subTest(name=name):self.assertAlmostEqual(actual,expected,delta=2e-9)
        # Both computations use fixed two-sided 95% intervals despite a one-sided p-value.
        greater=node("w.esaPooledTMath.compute("+arg+",'greater')")
        self.assertAlmostEqual(greater["p"],p["p"]/2,delta=1e-11)
        self.assertAlmostEqual(greater["lower"],p["lower"],delta=1e-10)
        self.assertIsNone(node("w.esaPooledTMath.compute([1],[2,3])"))
        self.assertTrue(node("w.esaWelchMath.compute([1,1],[2,2])")["degenerate"])
        self.assertTrue(node("w.esaPooledTMath.compute([1,1],[2,2])")["degenerate"])

    def test_independent_scipy_monte_carlo_reference(self):
        # Independent Python: xorshift32, Box-Muller and scipy.stats.ttest_ind
        # computed the fixed rejection-count vectors below, per selected seed.
        cases=[
         ({"n1":12,"n2":30,"sd1":1,"sd2":2,"effect":1,"reps":300,"seed":2026},[17,5,145,73]),
         ({"n1":10,"n2":10,"sd1":1,"sd2":1,"effect":0,"reps":100,"seed":5},[4,4,4,4]),
         ({"n1":6,"n2":20,"sd1":3,"sd2":1,"effect":0.5,"reps":120,"seed":19},[6,25,10,32])]
        for params,counts in cases:
            with self.subTest(seed=params["seed"]):
                expression="w.esaT89Simulation.simulate("+json.dumps(params)+")"
                r=node(expression)
                self.assertEqual(r["reps"],params["reps"])
                self.assertEqual([r[k]["count"] for k in ("nullWelch","nullPooled","altWelch","altPooled")],counts)
                self.assertEqual(r,node(expression))
                for key in ("nullWelch","nullPooled","altWelch","altPooled"):
                    x=r[key]
                    self.assertAlmostEqual(x["rate"],x["count"]/params["reps"],places=14)
                    self.assertAlmostEqual(x["mcse"],math.sqrt(x["rate"]*(1-x["rate"])/params["reps"]),places=14)
        for invalid in ({"n1":1,"n2":6,"sd1":1,"sd2":1,"effect":0,"reps":100,"seed":1},
                        {"n1":10,"n2":6,"sd1":1,"sd2":1,"effect":0,"reps":100000,"seed":1},
                        {"n1":10,"n2":6,"sd1":1,"sd2":1,"effect":0,"reps":100,"seed":0}):
            self.assertIsNone(node("w.esaT89Simulation.simulate("+json.dumps(invalid)+")"))

    def test_reporting_exact_nine_writer_labels(self):
        s=(ROOT/"descriptive/reporting/index.md").read_text()
        self.assertIn("const canonical = Object.freeze(",s)
        labels=dict(re.findall(r'"(/descriptive/reporting/[a-z0-9-]+/)": "([^"]+)"',s))
        self.assertEqual(len(labels),9)
        for url,label in labels.items():
            lesson=(ROOT/url.lstrip("/")/"index.md").read_text()
            self.assertIn('label: "'+label+'"',lesson.replace('label:"','label: "'))
        for marker in ("Object.prototype.hasOwnProperty.call(canonical,data.url)",
            "data.label !== canonical[data.url]","Number.isSafeInteger(data.ts)",
            "data.ts>Date.now()+5*60*1000"):
            self.assertIn(marker,s)

    def test_bilingual_parity_and_connected_navigation(self):
        en=ROOT/"inference/classical-tests/two-sample-t-test-independent/index.md"
        ar=ROOT/"ar/inference/classical-tests/two-sample-t-test-independent/index.md"
        for page in (en,ar):
            text=page.read_text()
            self.assertIn("translation_pair: independent-two-sample-t",text)
            self.assertIn("learning_resource: true",text)
            self.assertIn("math: true",text)
        arabic=ar.read_text()
        for marker in ("lang: ar",'data-locale="ar"',r"\nu_W",r"s_p^2",
            'id="esa-w-pool-results"','id="esa-w-plot"', 'id="esa-w-error"'):
            self.assertIn(marker,arabic)
        layout=(ROOT/"_layouts/default.html").read_text()
        self.assertIn('page.translation_pair == "independent-two-sample-t"',layout)
        self.assertIn("/ar/inference/classical-tests/two-sample-t-test-independent/",layout)
        self.assertIn("/ar/inference/classical-tests/two-sample-t-test-independent/",(ROOT/"ar/index.md").read_text())
        self.assertIn('src="/js/welch-pooled-monte-carlo.js"',(ROOT/"inference/classical-tests/welch-pooled-monte-carlo/index.md").read_text())
        for path in ("js/welch-two-sample-explorer.js","js/pooled-two-sample-comparison.js"):
            self.assertIn("data", (ROOT/path).read_text())
        self.assertIn('aria-invalid',(ROOT/"js/welch-two-sample-explorer.js").read_text())

if __name__=="__main__":unittest.main()
