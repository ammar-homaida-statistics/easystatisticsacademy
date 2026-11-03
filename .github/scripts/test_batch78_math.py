"""Batch #78 independent mathematical references for two-coin distributions and paired Student-t confidence intervals."""
import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def call_node(source, expression):
    js = """const fs=require('fs'),vm=require('vm');
const w={};const doc={getElementById:()=>null};
vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),{window:w,document:doc});
console.log(JSON.stringify(%s));""" % expression
    result = subprocess.run(
        ["node", "-e", js, str(ROOT/source)],
        capture_output=True, text=True, check=True)
    return json.loads(result.stdout)

class Batch78Math(unittest.TestCase):
    def test_coin_distribution_exact_independent_enumeration(self):
        for p in [0, .05, .25, .5, .75, .95, 1]:
            with self.subTest(p=p):
                result=call_node("js/two-coin-random-variable.js",
                    "w.esaTwoCoinRVMath.distribution(%s)" % p)
                self.assertAlmostEqual(sum(result["probabilities"]),1,places=14)
                self.assertAlmostEqual(result["probabilities"][0],(1-p)**2,places=14)
                self.assertAlmostEqual(result["probabilities"][1],2*p*(1-p),places=14)
                self.assertAlmostEqual(result["probabilities"][2],p*p,places=14)
                self.assertAlmostEqual(result["expectation"],2*p,places=14)
                self.assertAlmostEqual(result["variance"],2*p*(1-p),places=14)
                self.assertEqual([x["x"] for x in result["rows"]],[0,1,1,2])
        result=call_node("js/two-coin-random-variable.js",
                         "w.esaTwoCoinRVMath.distribution(0.5)")
        self.assertEqual(result["probabilities"],[.25,.5,.25])

    def test_student_t_scipy_independent_reference(self):
        # Constants precomputed independently with scipy.stats.t.ppf and interval formula.
        checks=[
            (4.2,3,10,95,2.262157162798205,2.053929282088006,6.346070717911994),
            (1,2,6,99,4.032142983555228,-2.2922309598845643,4.292230959884565),
            (0,1,20,90,1.7291328115213682,-.38664585086871106,.38664585086871106)
        ]
        for mean,sd,n,level,tstar,low,high in checks:
            with self.subTest(n=n,level=level):
                v=call_node("js/paired-mean-ci-explorer.js",
                    "w.esaPairedCIMath.paired(%s,%s,%s,%s)" % (mean,sd,n,level))
                self.assertEqual(v["df"],n-1)
                self.assertAlmostEqual(v["critical"],tstar,delta=1e-9)
                self.assertAlmostEqual(v["lower"],low,delta=1e-8)
                self.assertAlmostEqual(v["upper"],high,delta=1e-8)
                self.assertEqual(v["includesZero"],low<=0<=high)

    def test_paired_input_guards(self):
        tests=["0,0,10,95","0,1,1,95","0,1,10,97",
               "0,1,10.5,95","1,1,1000001,95"]
        for args in tests:
            with self.subTest(args=args):
                self.assertIsNone(call_node("js/paired-mean-ci-explorer.js",
                                     "w.esaPairedCIMath.paired("+args+")"))

    def test_bilingual_links(self):
        ar=(ROOT/"ar/probability/random-variables/what-is-a-random-variable/index.md").read_text()
        en=(ROOT/"probability/random-variables/what-is-a-random-variable/index.md").read_text()
        self.assertIn("translation_pair: what-is-a-random-variable",ar)
        self.assertIn("translation_pair: what-is-a-random-variable",en)
        self.assertIn("/js/two-coin-random-variable.js",ar)
        self.assertIn("/ar/probability/random-variables/what-is-a-random-variable/",en)

if __name__=="__main__":
    unittest.main()
