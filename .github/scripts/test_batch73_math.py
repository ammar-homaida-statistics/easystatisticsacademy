"""Batch #73 independent references for frequency conditional probability and known-sigma Z inference."""
import math
import unittest

def conditional(ab, aonly, bonly, neither):
    counts=(ab,aonly,bonly,neither)
    if any(type(v) is not int or v<0 or v>1000000 for v in counts):
        return None
    n=sum(counts)
    if n==0:
        return None
    a=ab+aonly
    b=ab+bonly
    return {"total":n, "pa":a/n, "pb":b/n, "pab":ab/n,
            "agivenb":None if b==0 else ab/b,
            "bgivena":None if a==0 else ab/a}

def known_sigma_z(n, mean, sigma, null_mean):
    if n<1 or sigma<=0:
        return None
    se=sigma/math.sqrt(n)
    z=(mean-null_mean)/se
    upper=.5*math.erfc(z/math.sqrt(2))
    lower=.5*math.erfc(-z/math.sqrt(2))
    crit=1.959963984540054
    return (se,z, min(1,2*min(upper,lower)),upper,lower,
            mean-crit*se,mean+crit*se)

class IndependentBatch73Checks(unittest.TestCase):
    def test_conditional_frequency_reference(self):
        r=conditional(20,10,30,40)
        self.assertEqual(r["total"],100)
        self.assertAlmostEqual(r["pa"],.3,places=14)
        self.assertAlmostEqual(r["pb"],.5,places=14)
        self.assertAlmostEqual(r["pab"],.2,places=14)
        self.assertAlmostEqual(r["agivenb"],.4,places=14)
        self.assertAlmostEqual(r["bgivena"],2/3,places=14)
        self.assertNotAlmostEqual(r["pab"],r["pa"]*r["pb"])
    def test_zero_conditioning_event_is_undefined(self):
        self.assertIsNone(conditional(0,10,0,40)["agivenb"])
        self.assertIsNone(conditional(0,0,30,40)["bgivena"])
        self.assertIsNone(conditional(0,0,0,0))
        self.assertIsNone(conditional(-1,0,0,1))
    def test_independence_example(self):
        r=conditional(25,25,25,25)
        self.assertAlmostEqual(r["pab"],r["pa"]*r["pb"],places=14)
        self.assertAlmostEqual(r["agivenb"],r["pa"],places=14)
    def test_known_sigma_textbook_example(self):
        se,z,p,upper,lower,lo,hi=known_sigma_z(100,492.,20.,500.)
        self.assertEqual(se,2.)
        self.assertEqual(z,-4.)
        self.assertAlmostEqual(p,math.erfc(4/math.sqrt(2)),places=14)
        self.assertAlmostEqual(p,.00006334248366623957,places=14)
        self.assertAlmostEqual(lower,p/2,places=14)
        self.assertAlmostEqual(upper,1-p/2,places=14)
        self.assertAlmostEqual(lo,488.0800720309199,places=11)
        self.assertAlmostEqual(hi,495.9199279690801,places=11)
    def test_normal_one_and_two_sided(self):
        se,z,p,upper,lower,lo,hi=known_sigma_z(25,102.,10.,100.)
        self.assertEqual(se,2.)
        self.assertEqual(z,1.)
        self.assertAlmostEqual(upper,.15865525393145707,places=14)
        self.assertAlmostEqual(lower,.8413447460685429,places=14)
        self.assertAlmostEqual(p,.31731050786291415,places=14)
        self.assertAlmostEqual(lo,98.08007203091989,places=11)
        self.assertAlmostEqual(hi,105.91992796908011,places=11)
    def test_boundaries_and_null(self):
        self.assertIsNone(known_sigma_z(0,0.,1.,0.))
        self.assertIsNone(known_sigma_z(5,0.,0.,0.))
        r=known_sigma_z(1,3.,2.,3.)
        self.assertEqual(r[1],0.)
        self.assertEqual(r[2],1.)
        self.assertEqual(r[3],.5)

if __name__=="__main__":
    unittest.main()
