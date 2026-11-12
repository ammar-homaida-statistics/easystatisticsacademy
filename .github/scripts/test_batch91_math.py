"""Batch #91 independent SciPy Fisher, Pearson χ², two-proportion references and security metadata."""
import json
import math
from pathlib import Path
import subprocess
import unittest
ROOT=Path(__file__).resolve().parents[2]
SCRIPTS=["js/fisher-chi-square-2x2.js","js/two-proportion-z-explorer.js",
         "js/one-proportion-z-explorer.js","js/exact-binomial-vs-z.js"]
def node(expression):
    runner="""const fs=require("fs"),vm=require("vm"),window={},document={getElementById:()=>null};
for(const file of process.argv.slice(1))vm.runInNewContext(fs.readFileSync(file,"utf8"),{window,document});
console.log(JSON.stringify(%s));"""%expression
    result=subprocess.run(["node","-e",runner,*[str(ROOT/p) for p in SCRIPTS]],
                          capture_output=True,text=True,check=True)
    return json.loads(result.stdout)

class Batch91Math(unittest.TestCase):
    def test_independent_scipy_fisher_and_pearson(self):
        # Independent reference: scipy.stats.fisher_exact and
        # scipy.stats.chi2_contingency(table, correction=False).
        fixtures=[
         ((1,9,11,3),(.0027594561852200836,.9999663480953022,.0013797280926100418),10.971428571428572,.000925274037119762),
         ((40,60,70,30),(3.304592989272319e-05,.9999955575953163,1.6522964946361596e-05),18.18181818181818,2.0078656124264854e-05),
         ((0,10,5,5),(.032507739938080496,1.,.016253869969040248),6.666666666666667,.009823274507519235),
         ((2,7,8,2),(.02301413756522116,.9990149169715733,.01852172595206651),6.342716049382714,.01178642687562122),
         ((10,0,0,10),(1.082508822446903e-05,5.412544112234515e-06,1.),20.,7.744216431044088e-06),
         ((5,5,5,5),(1.,.6718591006516703,.6718591006516703),0.,1.),
        ]
        for cells,pvalues,chi,p in fixtures:
            for alt,reference in zip(("two-sided","greater","less"),pvalues):
                with self.subTest(cells=cells,alternative=alt):
                    out=node("window.esaFisherChiMath.compute("+",".join(map(str,cells))+","+json.dumps(alt)+")")
                    self.assertAlmostEqual(out["fisher"],reference,delta=max(5e-10*reference,2e-12))
                    self.assertAlmostEqual(out["chi"],chi,places=9)
                    # Abramowitz-Stegun erfc implementation has ~1.5e-7 absolute error.
                    self.assertAlmostEqual(out["chiP"],p,delta=2e-7)
                    self.assertEqual(out["small"],sum(v<5 for v in out["expected"]))
    def test_invalid_margins_and_extremes(self):
        bad=[(0,0,0,0),(0,0,2,1),(0,1,0,2),(-1,3,4,6),(1.5,3,4,5),(3000,2,4,5)]
        for cells in bad:
            with self.subTest(cells=cells):
                self.assertIsNone(node("window.esaFisherChiMath.compute("+",".join(map(str,cells))+")"))
        self.assertIsNone(node('window.esaFisherChiMath.compute(1,9,11,3,"invalid")'))
        self.assertAlmostEqual(node("window.esaOneProportionMath.compute(120,200,.5).z"),2.82842712474619,places=12)
        self.assertAlmostEqual(node("window.esaExactBinomial.compute(2,10,.5).exact"),.109375,places=12)
    def test_two_proportion_independent_scipy_reference(self):
        # scipy.stats.proportions_ztest can be replicated using the pooled null SE.
        r=node("window.esaTwoProportionMath.compute(120,200,90,200)")
        self.assertAlmostEqual(r["pooled"],.525,places=13)
        self.assertAlmostEqual(r["diff"],.15,places=13)
        self.assertAlmostEqual(r["z"],.15/math.sqrt(.525*.475*(1/200+1/200)),places=12)
        self.assertEqual(r["adequate"],True)
        self.assertTrue(node("window.esaTwoProportionMath.compute(0,10,0,10)")["degenerate"])
    def test_language_and_learning_resource(self):
        en=(ROOT/"inference/classical-tests/two-proportion-z-test/index.md").read_text()
        ar=(ROOT/"ar/inference/classical-tests/two-proportion-z-test/index.md").read_text()
        layout=(ROOT/"_layouts/default.html").read_text()
        for s in (en,ar):
            self.assertIn("translation_pair: two-proportion-z",s)
            self.assertIn("learning_resource: true",s)
        self.assertIn("lang: ar",ar)
        self.assertIn('data-locale="ar"',ar)
        self.assertIn("const ar=root.dataset.locale", (ROOT/"js/two-proportion-z-explorer.js").read_text())
        self.assertIn("/ar/inference/classical-tests/two-proportion-z-test/",layout)
        self.assertIn("/inference/classical-tests/two-proportion-z-test/",layout)
    def test_secure_multiple_regression_progress(self):
        s=(ROOT/"modeling/multiple-regression/index.md").read_text()
        self.assertIn("Date.now()+5*60*1000",s)
        self.assertIn("esa_continue_modeling_mr_lesson_v0",s)
        self.assertIn("esa_continue_modeling_multiple_regression_lesson_v0",s)
        self.assertEqual(s.count('["/modeling/multiple-regression/'),9)
        self.assertIn("lessons.get(data.url) !== data.label",s)

if __name__=="__main__":unittest.main()
