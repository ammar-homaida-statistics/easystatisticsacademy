"""Independent Batch #84 affine-variance, bilingual metadata, progress and chi-square benchmarks."""
from pathlib import Path
import json
import math
import subprocess
import unittest
ROOT=Path(__file__).resolve().parents[2]

def affine(x,p,a,b):
    source=(ROOT/"js/affine-variance-lab.js").as_posix()
    script="""const fs=require('fs'),vm=require('vm'),w={};
vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),{window:w,document:{getElementById:()=>null}});
console.log(JSON.stringify(w.esaAffineVarianceMath.calculate(%s,%s,%s,%s)));"""%(json.dumps(x),json.dumps(p),json.dumps(a),json.dumps(b))
    out=subprocess.run(["node","-e",script,source],capture_output=True,text=True,check=True)
    return json.loads(out.stdout)

class Batch84Tests(unittest.TestCase):
    def test_independent_affine_reference_cases(self):
        cases=[([0,1,2],[.2,.5,.3],3,-2),
               ([-3,0,8],[.25,.5,.25],0,0),
               ([7,7,7],[.2,.3,.5],-10,4),
               ([0,1,2],[.2,.5,.3],-2,1)]
        for x,p,a,b in cases:
            with self.subTest(x=x,a=a,b=b):
                got=affine(x,p,a,b)
                mean=math.fsum(w*v for w,v in zip(p,x))
                variance=math.fsum(w*(v-mean)**2 for w,v in zip(p,x))
                y=[a+b*v for v in x]
                mean_y=math.fsum(w*v for w,v in zip(p,y))
                var_y=math.fsum(w*(v-mean_y)**2 for w,v in zip(p,y))
                for key,value in [("mean",mean),("variance",variance),("meanY",mean_y),
                                  ("varianceY",var_y),("rule",b*b*variance),("sdY",math.sqrt(var_y))]:
                    self.assertAlmostEqual(got[key],value,places=9)
    def test_invalid_probabilities(self):
        self.assertIsNone(affine([0,1,2],[.2,.2,.2],1,2))
        self.assertIsNone(affine([0,1,2],[-.1,.5,.6],1,2))
        self.assertIsNone(affine([0,1,2],[.2,.5,.3],1,1e8))
    def test_arabic_and_english_metadata(self):
        ar=(ROOT/"ar/probability/random-variables/variance-and-standard-deviation/index.md").read_text()
        en=(ROOT/"probability/random-variables/variance-and-standard-deviation/index.md").read_text()
        layout=(ROOT/"_layouts/default.html").read_text()
        self.assertIn("lang: ar",ar)
        self.assertIn("translation_pair: random-variable-variance",ar)
        self.assertIn("translation_pair: random-variable-variance",en)
        self.assertIn("learning_resource: true",ar)
        self.assertIn("learning_resource: true",en)
        self.assertIn('page.translation_pair == "random-variable-variance"',layout)
        self.assertIn('hreflang="ar"',layout)
        self.assertIn("/ar/probability/random-variables/variance-and-standard-deviation/",layout)
        self.assertIn("1.7-1.1^2=0.49",ar)
        self.assertIn("(b-a)^2",ar)
        self.assertIn("/ar/probability/random-variables/variance-and-standard-deviation/",(ROOT/"ar/index.md").read_text())
    def test_static_progress_security(self):
        txt=(ROOT/"probability/random-variables/index.md").read_text().split("<!-- CONTINUE READING SCRIPT -->")[-1]
        self.assertIn("const published = new Set([",txt)
        self.assertEqual(txt.split("const published = new Set([")[1].split("]);")[0].count('"/probability/random-variables/'),6)
        for fragment in ("published.has(data.url)","Number.isSafeInteger(data.ts)","label.replaceChildren","btn.href = data.url"):
            self.assertIn(fragment,txt)
    def test_independent_chi_square_reference(self):
        txt=(ROOT/"inference/classical-tests/chi-square-independence-test/index.md").read_text()
        self.assertIn("const p=chi===0?1:",txt)
        self.assertIn('aria-describedby="esa-chi-error esa-chi-warning"',txt)
        self.assertIn('input.setAttribute("aria-invalid","true")',txt)
        self.assertIn("rows.some(n=>n===0)||cols.some(n=>n===0)",txt)
        observed=[40,60,70,30]
        expected=[55,45,55,45]
        chi=math.fsum((o-e)**2/e for o,e in zip(observed,expected))
        self.assertAlmostEqual(chi,18.18181818181818)
        self.assertAlmostEqual(math.erfc(math.sqrt(chi/2)),2.008e-5,delta=5e-9)
        self.assertAlmostEqual(math.sqrt(chi/200),0.30151134457776363)
if __name__=="__main__":
    unittest.main()
