"""Independent Batch #83 mathematical, metadata and Pages-manifest references."""
from pathlib import Path
import json
import math
import subprocess
import unittest
ROOT=Path(__file__).resolve().parents[2]

def moment_math(values, probs):
    program="""const fs=require('fs'),vm=require('vm'),w={};
vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),{window:w,document:{getElementById:()=>null}});
console.log(JSON.stringify(w.esaThreePointMomentsMath.calculate(%s,%s)));"""%(json.dumps(values),json.dumps(probs))
    result=subprocess.run(["node","-e",program,str(ROOT/"js/three-point-moments-lab.js")],capture_output=True,text=True,check=True)
    return json.loads(result.stdout)

class Batch83Tests(unittest.TestCase):
    def test_independent_moments_and_negative_values(self):
        cases=[
            ([0,1,2],[.2,.5,.3]),
            ([-3,0,8],[.25,.5,.25]),
            ([7,7,7],[.2,.3,.5]),
            ([-1,1,3],[0,1,0]),
            ([1,2,3],[1,0,0]),
        ]
        for x,p in cases:
            with self.subTest(x=x,p=p):
                q=moment_math(x,p)
                mu=sum(v*w for v,w in zip(x,p))
                second=sum(v*v*w for v,w in zip(x,p))
                variance=sum(w*(v-mu)**2 for v,w in zip(x,p))
                self.assertAlmostEqual(q["sum"],1,places=12)
                self.assertAlmostEqual(q["mean"],mu,places=10)
                self.assertAlmostEqual(q["second"],second,places=10)
                self.assertAlmostEqual(q["variance"],variance,places=10)
                self.assertAlmostEqual(q["sd"],math.sqrt(variance),places=10)

    def test_invalid_probabilities_and_inputs(self):
        for x,p in [([0,1,2],[.2,.3,.4]),([0,1,2],[.5,-.1,.6]),([0,1,2],[.5,.6,.1]),([0,1,2],[1,0]),([0,1,2],[])]:
            self.assertIsNone(moment_math(x,p))
        self.assertIsNone(moment_math([0,1,1000001],[.2,.5,.3]))

    def test_bilingual_expected_value_metadata(self):
        en=(ROOT/"probability/random-variables/expectation/index.md").read_text()
        ar=(ROOT/"ar/probability/random-variables/expectation/index.md").read_text()
        layout=(ROOT/"_layouts/default.html").read_text()
        self.assertIn("translation_pair: random-variable-expectation",en)
        self.assertIn("translation_pair: random-variable-expectation",ar)
        self.assertIn("lang: ar",ar)
        self.assertIn('page.translation_pair == "random-variable-expectation"',layout)
        self.assertIn("/ar/probability/random-variables/expectation/",en)
        self.assertIn("/probability/random-variables/expectation/",ar)
        self.assertIn("/js/three-point-moments-lab.js",ar)

    def test_pages_workflow_revision_bound_to_commit(self):
        y=(ROOT/".github/workflows/publish-pages.yml").read_text()
        self.assertIn("_site/deployment-revision.txt",y)
        self.assertIn('--expected-sha "$GITHUB_SHA"',y)
        self.assertLess(y.index("actions/deploy-pages@v4"),y.index("Verify live pages and assets"))
        script=(ROOT/".github/scripts/check_live_pages.py").read_text()
        self.assertIn("expected_sha",script)
        self.assertIn("stale deployment revision",script)

if __name__=="__main__":
    unittest.main()
