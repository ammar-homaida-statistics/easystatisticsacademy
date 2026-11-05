"""Batch #81 independent normal-Z power, PDF, bilingual and metadata benchmarks."""
import json
import math
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def node_math(path,expression):
    src="""const fs=require('fs'),vm=require('vm');const w={};
vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),{window:w,document:{getElementById:()=>null}});
console.log(JSON.stringify(%s));"""%expression
    p=subprocess.run(["node","-e",src,str(ROOT/path)],capture_output=True,text=True,check=True)
    return json.loads(p.stdout)

def phi(x):
    return (1+math.erf(x/math.sqrt(2)))/2

class Batch81Benchmarks(unittest.TestCase):
    def test_independent_power_values_and_two_sided_symmetry(self):
        critical={.01:2.5758293035489004,.05:1.959963984540054,.1:1.6448536269514722}
        for alpha,c in critical.items():
            for delta,n in [(0,40),(.2,20),(.5,40),(1,40),(-.5,40),(0,2)]:
                with self.subTest(alpha=alpha,delta=delta,n=n):
                    z=delta*math.sqrt(n)
                    expected=phi(-c-z)+phi(z-c)
                    q=node_math("js/z-test-power-curve.js",f"w.esaPowerCurveMath.power({delta},{n},{alpha})")
                    self.assertAlmostEqual(q["critical"],c,delta=2e-6)
                    self.assertAlmostEqual(q["power"],expected,delta=3e-7)
                    self.assertAlmostEqual(q["power"]+q["beta"],1,delta=1e-12)
                    if delta==0:self.assertAlmostEqual(q["power"],alpha,delta=3e-7)

    def test_power_invalid_cases(self):
        for args in ["0,1,.05","0,40,.02","4,40,.05","0,10001,.05","0,2.2,.05"]:
            self.assertIsNone(node_math("js/z-test-power-curve.js","w.esaPowerCurveMath.power("+args+")"))

    def test_reused_uniform_pdf_arabic_lesson(self):
        ar=(ROOT/"ar/probability/random-variables/continuous-random-variables/index.md").read_text()
        en=(ROOT/"probability/random-variables/continuous-random-variables/index.md").read_text()
        self.assertIn("translation_pair: continuous-random-variables",ar)
        self.assertIn("translation_pair: continuous-random-variables",en)
        self.assertIn("lang: ar",ar)
        for s in (ar,en):self.assertIn("/js/uniform-pdf-interval-explorer.js",s)
        q=node_math("js/uniform-pdf-interval-explorer.js","w.esaUniformPDFMath.calculate(0,4,1,3)")
        self.assertEqual(q["probability"],.5)
        self.assertEqual(q["integral"],1)
        self.assertAlmostEqual(q["variance"],16/12)

    def test_bilingual_seo_branches(self):
        layout=(ROOT/"_layouts/default.html").read_text()
        for name in ["what-is-a-random-variable","discrete-random-variables","continuous-random-variables"]:
            self.assertIn('page.translation_pair == "'+name+'"',layout)
            self.assertIn('/probability/random-variables/'+name+'/',layout)
            self.assertIn('/ar/probability/random-variables/'+name+'/',layout)
        self.assertIn('/ar/probability/random-variables/continuous-random-variables/',
            (ROOT/"ar/index.md").read_text())

if __name__=="__main__":
    unittest.main()
