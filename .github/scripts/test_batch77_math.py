"""Batch #77 independent fixed-reference probability and normal-tail benchmarks."""
import json, math, subprocess, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class Batch77Math(unittest.TestCase):
 def test_medical_bayes_by_counts(self):
  prevalence,sensitivity,specificity=.01,.90,.95
  true_positive=10000*prevalence*sensitivity
  false_positive=10000*(1-prevalence)*(1-specificity)
  self.assertEqual(true_positive,90)
  self.assertAlmostEqual(false_positive,495)
  self.assertAlmostEqual(true_positive/(true_positive+false_positive),2/13,places=13)
  self.assertEqual(sum([true_positive,10,495,9405]),10000)
 def test_zero_evidence_undefined(self):
  prevalence,sensitivity,specificity=0,0,1
  positive=prevalence*sensitivity+(1-prevalence)*(1-specificity)
  self.assertEqual(positive,0)
 def test_independent_gaussian_z_references(self):
  # Precomputed using scipy.stats.norm.sf, not the site's gamma implementation.
  checks=[(0,'two-sided',1.),(2,'two-sided',.04550026389635842),
    (2,'right',.02275013194817921),(2,'left',.9772498680518208),
    (-2,'left',.02275013194817921),(-2,'right',.9772498680518208),
    (3,'two-sided',.0026997960632601866),(8,'two-sided',1.244192114854348e-15),
    (10,'right',7.61985302416047e-24)]
  program="const fs=require('fs'),vm=require('vm');const w={};vm.runInNewContext(fs.readFileSync(process.argv[1],'utf8'),{window:w,document:{getElementById:()=>null}});for(const [z,side] of JSON.parse(process.argv[2])) console.log(w.esaPvalueMath.pvalue(z,side));"
  proc=subprocess.run(['node','-e',program,str(ROOT/'js/pvalue-interpretation-explorer.js'),json.dumps([[z,side] for z,side,_ in checks])],capture_output=True,text=True,check=True)
  values=[float(v) for v in proc.stdout.splitlines()]
  for (z,side,reference),value in zip(checks,values):
   with self.subTest(z=z,side=side):
    self.assertAlmostEqual(value/reference,1,delta=2e-10)
 def test_relevant_files_and_shared_engine(self):
  ar=(ROOT/'ar/probability/conditional/base-rate-neglect-and-fallacies/index.md').read_text()
  en=(ROOT/'probability/conditional/base-rate-neglect-and-fallacies/index.md').read_text()
  self.assertIn('translation_pair: base-rate-neglect-and-fallacies',ar)
  self.assertIn('translation_pair: base-rate-neglect-and-fallacies',en)
  self.assertIn('/js/bayes-evidence-lab.js',ar)
  self.assertIn('esa-pvalue-explorer',(ROOT/'inference/hypothesis-testing/p-value-meaning/index.md').read_text())
if __name__=="__main__": unittest.main()
