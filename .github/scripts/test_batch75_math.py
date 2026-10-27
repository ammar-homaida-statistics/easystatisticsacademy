"""Independent Batch #75 mathematical references: multiplication tree and known-sigma CI precision."""
import math
import unittest

Z={90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004}

def tree(s,q1,q0):
    if not (0<s<1 and 0<=q1<=1 and 0<=q0<=1):return None
    leaves=(s*q1,s*(1-q1),(1-s)*q0,(1-s)*(1-q0))
    passing=leaves[0]+leaves[2]
    return leaves,passing,None if passing==0 else leaves[0]/passing

def precision(n,sigma,level,target):
    if not (isinstance(n,int) and 1<=n<=1_000_000_000 and
            math.isfinite(sigma) and sigma>0 and math.isfinite(target) and
            target>0 and level in Z):return None
    z=Z[level]
    margin=z*sigma/math.sqrt(n)
    n_required=math.ceil((z*sigma/target)**2)
    return margin,2*margin,max(1,n_required)

class Batch75IndependentBenchmarks(unittest.TestCase):
    def test_tree_main_example(self):
        leaves,total,bayes=tree(.6,.9,.4)
        for a,b in zip(leaves,(.54,.06,.16,.24)):
            self.assertAlmostEqual(a,b,places=14)
        self.assertAlmostEqual(sum(leaves),1,places=14)
        self.assertAlmostEqual(total,.7,places=14)
        self.assertAlmostEqual(bayes,27/35,places=14)
    def test_tree_boundaries_and_undefined(self):
        self.assertIsNone(tree(0,.9,.4))
        self.assertIsNone(tree(1,.9,.4))
        self.assertIsNone(tree(.6,-.1,.4))
        self.assertIsNone(tree(.6,.5,1.1))
        leaves,total,bayes=tree(.6,0,0)
        self.assertAlmostEqual(sum(leaves),1)
        self.assertEqual(total,0)
        self.assertIsNone(bayes)
        self.assertAlmostEqual(tree(.2,1,0)[1],.2,places=14)
    def test_draw_two_aces_without_replacement(self):
        self.assertAlmostEqual((4/52)*(3/51),1/221,places=14)
        self.assertNotAlmostEqual((4/52)**2,1/221,places=6)
    def test_known_sigma_default(self):
        moe,width,needed=precision(100,20,95,3)
        self.assertAlmostEqual(moe,3.919927969080108,places=12)
        self.assertAlmostEqual(width,7.839855938160216,places=12)
        self.assertEqual(needed,171)
        self.assertGreater(Z[95]*20/math.sqrt(170),3)
        self.assertLessEqual(Z[95]*20/math.sqrt(171),3)
    def test_fixed_confidence_critical_values_and_width(self):
        a=[precision(100,20,level,3)[0] for level in (90,95,99)]
        self.assertLess(a[0],a[1])
        self.assertLess(a[1],a[2])
        self.assertAlmostEqual(a[0],3.2897072539029444,places=12)
        self.assertAlmostEqual(a[2],5.151658607097801,places=12)
        self.assertAlmostEqual(precision(400,20,95,3)[1],
                               precision(100,20,95,3)[1]/2,places=12)
        self.assertEqual(precision(100,20,90,3)[2],121)
        self.assertEqual(precision(100,20,99,3)[2],295)
    def test_precision_edge_cases(self):
        for args in [(0,20,95,3),(100,0,95,3),(100,20,92,3),
                     (100,20,95,0),(100,-1,95,3)]:
            self.assertIsNone(precision(*args))
        self.assertEqual(precision(1,1,95,100)[2],1)
        margin,_,n=precision(100,20,95,Z[95]*20/10)
        self.assertAlmostEqual(margin,Z[95]*2,places=12)
        self.assertEqual(n,100)

if __name__=="__main__":
    unittest.main()
