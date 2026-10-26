"""Batch #71 independent references for hypergeometric probabilities and one-proportion Z/Wilson inference.
Reference targets cross-checked against exact combinatorics and SciPy's normal distribution;
implementation uses Python standard library only.
"""
import math
import unittest
from statistics import NormalDist

def hyper(N,K,n,x):
    if x < max(0,n-(N-K)) or x > min(n,K):
        return 0.0
    return math.comb(K,x)*math.comb(N-K,n-x)/math.comb(N,n)

def score_intervals(x,n):
    p=x/n
    z=NormalDist().inv_cdf(.975)
    se=math.sqrt(p*(1-p)/n)
    wald=(p-z*se,p+z*se)
    denom=1+z*z/n
    center=(p+z*z/(2*n))/denom
    half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/denom
    return wald,(center-half,center+half)

class Batch71IndependentBenchmarks(unittest.TestCase):
    def test_hypergeometric_example_and_approximation(self):
        self.assertAlmostEqual(hyper(10,3,2,1),21/45,places=14)
        self.assertAlmostEqual(math.comb(2,1)*.3*.7,.42,places=14)
        self.assertAlmostEqual(2*.3*.7*(8/9),.3733333333333333,places=14)
    def test_hypergeometric_mass_and_support(self):
        for N,K,n in ((10,3,2),(20,8,10),(100,10,5),(1,0,1),(1,1,1),(8,0,3),(8,8,8)):
            with self.subTest(N=N,K=K,n=n):
                probs=[hyper(N,K,n,x) for x in range(n+1)]
                self.assertAlmostEqual(sum(probs),1.0,places=13)
                self.assertTrue(all(0<=v<=1 for v in probs))
        self.assertEqual(hyper(10,2,8,0),0)
        self.assertEqual(hyper(10,2,8,1),0)
    def test_hypergeometric_moments_edge_cases(self):
        for N,K,n in ((2,1,1),(10,3,2),(25,10,5),(100,50,1)):
            p=K/N
            exact_mean=sum(x*hyper(N,K,n,x) for x in range(n+1))
            exact_var=sum((x-exact_mean)**2*hyper(N,K,n,x) for x in range(n+1))
            self.assertAlmostEqual(exact_mean,n*p,places=12)
            self.assertAlmostEqual(exact_var,n*p*(1-p)*(N-n)/(N-1),places=12)
        self.assertEqual(hyper(1,1,1,1),1)
    def test_one_proportion_z_null_standard_error_and_tail(self):
        x,n,p0=120,200,.5
        ph=x/n
        se=math.sqrt(p0*(1-p0)/n)
        z=(ph-p0)/se
        pv=math.erfc(abs(z)/math.sqrt(2))
        self.assertAlmostEqual(ph,.6,places=14)
        self.assertAlmostEqual(se,.03535533905932738,places=14)
        self.assertAlmostEqual(z,2.8284271247461903,places=12)
        self.assertAlmostEqual(pv,.004677734981047266,places=14)
        self.assertAlmostEqual(0.5*pv,.002338867490523633,places=14)
    def test_wilson_and_wald_independent_95_percent_references(self):
        wald,wilson=score_intervals(120,200)
        self.assertAlmostEqual(wald[0],.5321048559554297,places=13)
        self.assertAlmostEqual(wald[1],.6678951440445703,places=13)
        self.assertAlmostEqual(wilson[0],.53083672039262,places=13)
        self.assertAlmostEqual(wilson[1],.6653942143319266,places=13)
        self.assertNotEqual(wald,wilson)
    def test_wilson_endpoint_coverage(self):
        for x,n in ((0,10),(10,10),(1,15),(15,15)):
            wald,wilson=score_intervals(x,n)
            self.assertLessEqual(0,wilson[0])
            self.assertLessEqual(wilson[1],1)
            self.assertLessEqual(wilson[0],wilson[1])
            if x in (0,n):
                self.assertEqual(wald[0],wald[1])

if __name__=="__main__":
    unittest.main()
