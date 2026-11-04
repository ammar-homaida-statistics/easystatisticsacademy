"""Independent reference checks for Batch #80 discrete PMF and uniform PDF."""
import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def js_compute(path, expression):
    js = """const fs=require('fs'),vm=require('vm');const w={};
vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),
 {window:w,document:{getElementById:()=>null}});
console.log(JSON.stringify(%s));""" % expression
    completed = subprocess.run(["node", "-e", js, str(ROOT/path)],
                               capture_output=True, text=True, check=True)
    return json.loads(completed.stdout)


class Batch80Math(unittest.TestCase):
    def test_pmf_expected_mean_variance(self):
        cases = [([.2,.5,.3],1.1,.49),([0,1,0],1,0),([1,0,0],0,0),
                 ([.25,.5,.25],1,.5),([.1,.1,.8],1.7,.41)]
        for probs,mean,var in cases:
            with self.subTest(probs=probs):
                result=js_compute("js/three-point-pmf-explorer.js",
                                  "w.esaThreePointPMFMath.compute("+json.dumps(probs)+")")
                self.assertAlmostEqual(result["total"],1,places=12)
                self.assertAlmostEqual(result["mean"],mean,places=12)
                self.assertAlmostEqual(result["variance"],var,places=12)

    def test_pmf_bad_distribution_rejected(self):
        for probs in ([.2,.3,.3],[-.1,.7,.4],[.2,.5,1.3],[0,0,0],[1,1,-1]):
            self.assertIsNone(js_compute("js/three-point-pmf-explorer.js",
                "w.esaThreePointPMFMath.compute("+json.dumps(probs)+")"))

    def test_uniform_exact_areas(self):
        cases = [(0,4,1,3,.5,.25), (0,4,-10,10,1,.25),
                 (0,4,6,8,0,.25),(0,4,2,2,0,.25),
                 (-2,2,-3,0,.5,.25),(0,.25,0,.125,.5,4)]
        for a,b,c,d,prob,height in cases:
            with self.subTest(bounds=(a,b,c,d)):
                v=js_compute("js/uniform-pdf-interval-explorer.js",
                    f"w.esaUniformPDFMath.calculate({a},{b},{c},{d})")
                self.assertAlmostEqual(v["probability"],prob,places=12)
                self.assertAlmostEqual(v["density"],height,places=12)
                self.assertEqual(v["integral"],1)
                self.assertEqual(v["pointProbability"],0)
        # independent analytic integral of constant 1/(b-a) over [c,d] ∩ [a,b]
        v=js_compute("js/uniform-pdf-interval-explorer.js",
                     "w.esaUniformPDFMath.calculate(2,5,3,4)")
        self.assertAlmostEqual(v["probability"],1/3,places=12)
        self.assertAlmostEqual(v["mean"],3.5,places=12)
        self.assertAlmostEqual(v["variance"],.75,places=12)

    def test_uniform_invalid_bounds(self):
        for a,b,c,d in [(1,1,0,1),(2,1,0,1),(0,1,2,1),(0,0.0000001,0,1)]:
            self.assertIsNone(js_compute("js/uniform-pdf-interval-explorer.js",
                               f"w.esaUniformPDFMath.calculate({a},{b},{c},{d})"))

    def test_translation_pairs_and_assets(self):
        en=(ROOT/"probability/random-variables/discrete-random-variables/index.md").read_text()
        ar=(ROOT/"ar/probability/random-variables/discrete-random-variables/index.md").read_text()
        self.assertIn("translation_pair: discrete-random-variables",en)
        self.assertIn("translation_pair: discrete-random-variables",ar)
        self.assertIn("/ar/probability/random-variables/discrete-random-variables/",en)
        self.assertIn("/probability/random-variables/discrete-random-variables/",ar)
        self.assertIn("/js/three-point-pmf-explorer.js",ar)
        self.assertIn("esa-uniform-pdf-lab",(ROOT/"probability/random-variables/continuous-random-variables/index.md").read_text())


if __name__ == "__main__":
    unittest.main()
