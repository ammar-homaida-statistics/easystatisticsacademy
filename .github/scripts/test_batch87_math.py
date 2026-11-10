"""Independent Batch #87 Student-t, practical threshold, GOF, secure progress and bilingual benchmarks."""
from pathlib import Path
import json
import math
import re
import subprocess
import unittest

ROOT=Path(__file__).resolve().parents[2]

def node(paths,expression):
    script="""const fs=require('fs'),vm=require('vm'),w={};
const ctx={window:w,document:{getElementById:()=>null}};
for(const path of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(path,'utf8'),ctx);
console.log(JSON.stringify(%s));"""%expression
    p=subprocess.run(["node","-e",script,*[str(ROOT/x) for x in paths]],
                     text=True,capture_output=True,check=True)
    return json.loads(p.stdout)

class Batch87(unittest.TestCase):
    def test_student_t_independent_values(self):
        path=["js/student-t-one-sample-explorer.js"]
        for n,mean,sd,mu0,p,critical in [
            (2,1,math.sqrt(2),0,.5,12.706204736174694),
            (3,1,math.sqrt(3),0,.4226497308103742,4.302652729749462),
            (25,18,4,20,.019654175116578784,2.0638985616280245)]:
            with self.subTest(n=n):
                r=node(path,f"w.esaStudentTMath.compute({n},{mean},{sd},{mu0},'two-sided')")
                self.assertAlmostEqual(r["t"],(mean-mu0)/(sd/math.sqrt(n)),places=11)
                self.assertAlmostEqual(r["pvalue"],p,delta=2e-10)
                self.assertAlmostEqual(r["critical"],critical,delta=1e-8)
                self.assertEqual(r["df"],n-1)
        self.assertIsNone(node(path,"w.esaStudentTMath.compute(1,2,3,0,'two-sided')"))
    def test_effect_size_statistical_vs_practical(self):
        paths=["js/student-t-one-sample-explorer.js","js/practical-significance-explorer.js"]
        r=node(paths,"w.esaPracticalMath.compute(400,.2,1,0,.5)")
        self.assertAlmostEqual(r["difference"],.2,places=12)
        self.assertAlmostEqual(r["d"],.2,places=12)
        self.assertAlmostEqual(r["t"],4,places=12)
        self.assertTrue(r["statistical"])
        self.assertFalse(r["practical"])
        self.assertAlmostEqual((r["lower"]+r["upper"])/2,.2,delta=1e-10)
        r=node(paths,"w.esaPracticalMath.compute(10,1,3,0,.5)")
        self.assertFalse(r["statistical"])
        self.assertTrue(r["practical"])
        for expression in ["w.esaPracticalMath.compute(0,1,1,0,.5)",
                           "w.esaPracticalMath.compute(20,1,0,0,.5)",
                           "w.esaPracticalMath.compute(20,1,1,0,-.1)"]:
            self.assertIsNone(node(paths,expression))
    def test_chisquare_gof_independent_reference(self):
        path=["js/chi-square-gof-explorer.js"]
        for observed,probs,expected_stat,expected_p in (
            ([10,10],[.5,.5],0,1),
            ([15,5],[.5,.5],5,math.erfc(math.sqrt(5/2))),
            ([12,18,30],[.2,.3,.5],0,1),
            ([20,10,10],[.5,.25,.25],0,1)):
            r=node(path,"w.esaChiSquareGofMath.compute("+json.dumps(observed)+","+json.dumps(probs)+")")
            self.assertEqual(r["df"],len(observed)-1)
            reference=sum((o-sum(observed)*p)**2/(sum(observed)*p)
                          for o,p in zip(observed,probs))
            self.assertAlmostEqual(r["statistic"],reference,places=12)
            self.assertAlmostEqual(r["statistic"],expected_stat,places=12)
            self.assertAlmostEqual(r["p"],expected_p,delta=1e-10)
        sparse=node(path,"w.esaChiSquareGofMath.compute([1,0,0],[.5,.3,.2])")
        self.assertTrue(sparse["smallExpected"])
        for expression in ["w.esaChiSquareGofMath.compute([0,0],[.5,.5])",
                           "w.esaChiSquareGofMath.compute([2,3],[.2,.2])",
                           "w.esaChiSquareGofMath.compute([2,3],[0,1])"]:
            self.assertIsNone(node(path,expression))
    def test_center_route_labels_exact(self):
        page=(ROOT/"descriptive/center/index.md").read_text()
        section=page.split("const canonical = Object.freeze(")[1].split("if (!data")[0]
        pairs=re.findall(r'"/descriptive/center/([a-z0-9-]+)/": "([^"]+)"',section)
        self.assertEqual(len(pairs),10)
        for slug,title in pairs:
            writer=(ROOT/"descriptive/center"/slug/"index.md").read_text()
            self.assertIn('label: "'+title+'"',writer)
        for snippet in ["Object.prototype.hasOwnProperty.call(canonical,data.url)",
                        "data.label !== canonical[data.url]","Number.isSafeInteger(data.ts)",
                        "label.replaceChildren","data.ts>Date.now()+300000"]:
            self.assertIn(snippet,page)
    def test_bilingual_t_seo(self):
        arroute="/ar/inference/classical-tests/one-sample-t-test-for-mean/"
        enroute="/inference/classical-tests/one-sample-t-test-for-mean/"
        ar=(ROOT/(arroute.strip("/")+"/index.md")).read_text()
        en=(ROOT/(enroute.strip("/")+"/index.md")).read_text()
        layout=(ROOT/"_layouts/default.html").read_text()
        for doc in (ar,en):
            self.assertIn("translation_pair: one-sample-student-t-mean",doc)
            self.assertIn("learning_resource: true",doc)
            self.assertIn("math: true",doc)
        for link in (arroute,enroute):self.assertIn(link,layout)
        self.assertIn(arroute,(ROOT/"ar/index.md").read_text())
        self.assertIn('data-locale="ar"',ar)
        self.assertIn('src="/js/student-t-one-sample-explorer.js"',ar)
    def test_accessibility_source(self):
        g=(ROOT/"inference/classical-tests/chi-square-goodness-of-fit/index.md").read_text()
        js=(ROOT/"js/chi-square-gof-explorer.js").read_text()
        for id in ("counts","probs"):
            self.assertIn('id="esa-gof-'+id+'" rows="3" spellcheck="false" aria-invalid="false" aria-describedby="esa-gof-error esa-gof-warning"',g)
        self.assertIn('counts.setAttribute("aria-invalid"',js)
        self.assertIn('probs.setAttribute("aria-invalid"',js)
        self.assertIn('role="status" aria-live="polite"',g)

if __name__=="__main__":unittest.main()
