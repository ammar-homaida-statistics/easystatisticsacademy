"""Batch #82 independently calculated CDF and sensitivity references."""
import json
import math
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def js_math(path,expr):
    source="""const fs=require("fs"),vm=require("vm");const w={};
vm.runInNewContext(fs.readFileSync(process.argv[1],"utf8"),
  {window:w,document:{getElementById:()=>null}});
console.log(JSON.stringify(%s));"""%expr
    result=subprocess.run(["node","-e",source,str(ROOT/path)],check=True,capture_output=True,text=True)
    return json.loads(result.stdout)

class Batch82Benchmarks(unittest.TestCase):
    def test_bernoulli_cdf_boundaries(self):
        for p in (0,.35,1):
            for x,expected in ((-1,0),(0,1-p),(.5,1-p),(1,1),(5,1)):
                with self.subTest(p=p,x=x):
                    q=js_math("js/cdf-bernoulli-uniform-explorer.js",
                              f"w.esaCdfMath.cdf('bernoulli',{x},{p},0,2)")
                    self.assertAlmostEqual(q,expected,places=12)

    def test_uniform_cdf_and_open_left_interval(self):
        for x,expected in ((-1,0),(0,0),(.5,.25),(1,.5),(2,1),(4,1)):
            with self.subTest(x=x):
                q=js_math("js/cdf-bernoulli-uniform-explorer.js",
                          f"w.esaCdfMath.cdf('uniform',{x},.35,0,2)")
                self.assertAlmostEqual(q,expected,places=12)
        for kind,p,expected in (("bernoulli",.35,.35),("bernoulli",0,0),
                                ("bernoulli",1,1),("uniform",.35,.5)):
            q=js_math("js/cdf-bernoulli-uniform-explorer.js",
                      f"w.esaCdfMath.interval('{kind}',0,1,{p},0,2)")
            self.assertAlmostEqual(q,expected,places=12)

    def test_sensitivity_independent_sorted_references(self):
        sample=[2,4,5,6,8,9,10,12,14,15]
        for x in (-1000,0,11,1000):
            q=js_math("js/sensitivity-summary-lab.js",f"w.esaSensitivityMath.summarize({x})")
            sorted_sample=sorted(sample+[x])
            self.assertEqual(q["n"],11)
            self.assertAlmostEqual(q["mean"],sum(sorted_sample)/11,places=11)
            self.assertEqual(q["median"],sorted_sample[5])
            self.assertAlmostEqual(q["trimmed"],sum(sorted_sample[1:-1])/9,places=11)
        for v in (float("nan"),1001,-1001):
            arg="NaN" if math.isnan(v) else str(v)
            self.assertIsNone(js_math("js/sensitivity-summary-lab.js",
                                      f"w.esaSensitivityMath.summarize({arg})"))

    def test_arabic_pair_and_learningresource_scoping(self):
        en=(ROOT/"probability/random-variables/cumulative-distribution-function/index.md").read_text()
        ar=(ROOT/"ar/probability/random-variables/cumulative-distribution-function/index.md").read_text()
        layout=(ROOT/"_layouts/default.html").read_text()
        for page in (en,ar):
            self.assertIn("learning_resource: true",page)
            self.assertIn("translation_pair: cumulative-distribution-function",page)
            self.assertIn("cdf-bernoulli-uniform-explorer.js",page)
        self.assertIn("lang: ar",ar)
        self.assertIn('page.translation_pair == "cumulative-distribution-function"',layout)
        self.assertIn('"@type": "LearningResource"',layout)
        self.assertIn("{% if page.learning_resource == true %}",layout)
        self.assertIn("/ar/probability/random-variables/cumulative-distribution-function/",
                      (ROOT/"ar/index.md").read_text())

if __name__=="__main__":
    unittest.main()
