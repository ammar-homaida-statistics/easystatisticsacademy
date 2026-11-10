"""Batch #88 independent paired-t, Welch/pooled t, secure Shape and bilingual SEO tests."""
import json
import math
from pathlib import Path
import re
import subprocess
import unittest
ROOT=Path(__file__).resolve().parents[2]

def run_node(paths,expression):
    source="""const fs=require('fs'),vm=require('vm'),w={};
const ctx={window:w,document:{getElementById:()=>null}};
for(const p of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(p,'utf8'),ctx);
console.log(JSON.stringify(%s));"""%expression
    p=subprocess.run(["node","-e",source,*[str(ROOT/name) for name in paths]],
                     text=True,capture_output=True,check=True)
    return json.loads(p.stdout)

class Batch88Math(unittest.TestCase):
    def test_paired_t_reference_and_direction(self):
        p=["js/paired-t-explorer.js"]
        a=[[70,75],[68,72],[75,79],[71,74],[69,74]]
        result=run_node(p,"w.esaPairedTMath.compute("+json.dumps(a)+")")
        self.assertEqual(result["df"],4)
        self.assertAlmostEqual(result["mean"],4.2,places=12)
        self.assertAlmostEqual(result["sd"],math.sqrt(.7),places=12)
        self.assertAlmostEqual(result["t"],11.224972160321826,places=10)
        self.assertAlmostEqual(result["p"],.0003587352603774513,delta=3e-12)
        self.assertAlmostEqual(result["critical"],2.7764451051977934,places=9)
        self.assertAlmostEqual(result["lower"],3.1611493663164314,places=9)
        reverse=[[b,a] for a,b in a]
        r=run_node(p,"w.esaPairedTMath.compute("+json.dumps(reverse)+")")
        self.assertAlmostEqual(r["mean"],-result["mean"])
        self.assertAlmostEqual(r["t"],-result["t"])
        self.assertAlmostEqual(r["p"],result["p"],places=12)
        self.assertAlmostEqual(r["lower"],-result["upper"],places=11)
        self.assertAlmostEqual(r["upper"],-result["lower"],places=11)
        for expr in ("w.esaPairedTMath.compute([[1,2]])",
                     "w.esaPairedTMath.compute([[1,2],[3]])"):
            self.assertIsNone(run_node(p,expr))
        d=run_node(p,"w.esaPairedTMath.compute([[1,2],[2,3]])")
        self.assertTrue(d["degenerate"])

    def test_independent_welch_pooled_scipy_references(self):
        paths=["js/welch-two-sample-explorer.js","js/pooled-two-sample-comparison.js"]
        cases=[
         ([73,77,80,78,82,79,84],[70,68,74,71,75,69],
          (4.446189534952488,.0009985114499363515,10.93790675014491),
          (4.357746205649742,.0011405670691066125,11)),
         ([1,2,3],[10,20,30,40,50],
          (-3.9466642801734926,.01643969143145561,4.053150831037242),
          (-2.966883079863586,.025058463517772547,6)),
         ([1,2,3],[4,5,6],
          (-3.6742346141747673,.021311641128756713,4),
          (-3.6742346141747673,.021311641128756713,4)),
         ([4,4,4],[7,9,11,13],
          (-4.6475800154489,.018782784176974782,3),
          (-3.9279220242478634,.011093407615274987,5))
        ]
        for a,b,expected_w,expected_p in cases:
            with self.subTest(a=a,b=b):
                arg=json.dumps(a)+","+json.dumps(b)
                w=run_node(paths,"w.esaWelchMath.compute("+arg+")")
                p=run_node(paths,"w.esaPooledTMath.compute("+arg+")")
                for actual,expected in zip((w["t"],w["p"],w["df"]),expected_w):
                    self.assertAlmostEqual(actual,expected,delta=5e-10)
                for actual,expected in zip((p["t"],p["p"],p["df"]),expected_p):
                    self.assertAlmostEqual(actual,expected,delta=5e-10)
                self.assertEqual(p["df"],len(a)+len(b)-2)
                self.assertAlmostEqual((w["lower"]+w["upper"])/2,w["difference"],places=10)
                self.assertAlmostEqual((p["lower"]+p["upper"])/2,p["difference"],places=10)
                self.assertAlmostEqual(p["critical"],run_node(paths,
                         "w.esaWelchMath.critical95("+str(p["df"])+")"),places=11)
        for expr in ("w.esaPooledTMath.compute([1],[2,3])",
                     "w.esaPooledTMath.compute([4,4],[4,4])",
                     "w.esaPooledTMath.compute([1,2],[4,5],'bad')"):
            r=run_node(paths,expr)
            self.assertTrue(r is None or r.get("degenerate"))
        r=run_node(paths,"w.esaPooledTMath.compute([1,2,3],[4,5,6],'greater')")
        self.assertAlmostEqual(r["p"],1-.021311641128756713/2,delta=1e-10)

    def test_shape_exact_active_writers(self):
        page=(ROOT/"descriptive/shape/index.md").read_text()
        mapping=page.split("const canonical = Object.freeze(")[1].split("if (!data")[0]
        pairs=re.findall(r'"/descriptive/shape/([a-z0-9-]+)/": "([^"]+)"',mapping)
        self.assertEqual(len(pairs),8)
        for slug,label in pairs:
            self.assertIn('label: "'+label+'"',
                (ROOT/"descriptive/shape"/slug/"index.md").read_text())
        self.assertNotIn("normal-distribution-concept/",mapping)
        for term in ("Object.prototype.hasOwnProperty.call(canonical,data.url)",
                     "data.label !== canonical[data.url]","Number.isSafeInteger(data.ts)",
                     "data.ts>Date.now()+300000"):
            self.assertIn(term,page)

    def test_paired_bilingual_seo_and_accessibility(self):
        en="/inference/classical-tests/paired-t-test/"
        ar="/ar/inference/classical-tests/paired-t-test/"
        docs=[(ROOT/(p.strip("/")+"/index.md")).read_text() for p in (en,ar)]
        for d in docs:
            for marker in ("math: true","translation_pair: paired-student-t","learning_resource: true"):
                self.assertIn(marker,d)
        layout=(ROOT/"_layouts/default.html").read_text()
        for uri in (en,ar):self.assertIn(uri,layout)
        self.assertIn(ar,(ROOT/"ar/index.md").read_text())
        self.assertIn('data-locale="ar"',docs[1])
        for marker in ('id="esa-pt-input"','id="esa-pt-null"','role="alert"'):
            self.assertIn(marker,docs[1])
        self.assertIn('aria-describedby="esa-pt-error"',docs[0])
        self.assertIn('aria-invalid', (ROOT/"js/paired-t-explorer.js").read_text())
        lesson=(ROOT/"inference/classical-tests/two-sample-t-test-independent/index.md").read_text()
        self.assertLess(lesson.index('src="/js/welch-two-sample-explorer.js"'),
                        lesson.index('src="/js/pooled-two-sample-comparison.js"'))
        for marker in ('id="esa-w-pool-results"','id="esa-w-pool-plot"',
                       'id="esa-w-pool-warning"'):
            self.assertIn(marker,lesson)

if __name__=="__main__":unittest.main()
