"""Independent, fixed-reference Batch #76 numerical and implementation guards."""
import math, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class Batch76References(unittest.TestCase):
 def test_two_coin_tosses(self):
  paths=[.25]*4
  self.assertAlmostEqual(sum(paths),1)
  self.assertAlmostEqual(sum(paths[:3]),.75)
 def test_dependent_cards(self):
  self.assertAlmostEqual((4/52)*(3/51),1/221)
 def test_tree_complete(self):
  p=.6;q=.9;r=.4
  paths=[p*q,p*(1-q),(1-p)*r,(1-p)*(1-r)]
  self.assertAlmostEqual(sum(paths),1)
  self.assertAlmostEqual(paths[0]+paths[2],.7)
 def test_welch_reference_scipy(self):
  a=100/40;b=144/35
  df=(a+b)**2/(a*a/39+b*b/34)
  se=math.sqrt(a+b)
  # Independently computed using scipy.stats.t.ppf(0.975,df).
  critical=1.9962979294604513
  self.assertAlmostEqual(df,66.47542250283321,places=10)
  self.assertAlmostEqual(se,2.5718253662108777,places=10)
  self.assertAlmostEqual(6-critical*se,.8658703464993582,places=10)
  self.assertAlmostEqual(6+critical*se,11.134129653500642,places=10)
 def test_assets_are_wired(self):
  html=(ROOT/'inference/confidence-intervals/ci-for-difference-of-means-independent/index.md').read_text()
  js=(ROOT/'js/welch-ci-explorer.js').read_text()
  self.assertIn('esa-welch-explorer',html)
  self.assertIn('function welch(',js)
  self.assertIn('tQuantile(',js)
  ar=(ROOT/'ar/probability/conditional/tree-diagrams/index.md').read_text()
  en=(ROOT/'probability/conditional/tree-diagrams/index.md').read_text()
  self.assertIn('conditional-tree-explorer.js',ar)
  self.assertIn('translation_pair: tree-diagrams',en)
if __name__=='__main__':unittest.main()
