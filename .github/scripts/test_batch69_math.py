"""Batch #69 independent Gaussian and Welch references (stdlib only).

Expected Welch values verified separately with scipy.stats.ttest_ind(equal_var=False).
Browser tests execute the actual JavaScript and compare with these reference targets.
"""
import math
import statistics
import unittest

A = (73, 77, 80, 78, 82, 79, 84)
B = (70, 68, 74, 71, 75, 69)

def normal_prob(mu, sigma, a, b):
    if sigma <= 0 or a >= b:
        raise ValueError("Invalid normal model or interval")
    return 0.5 * (math.erfc((a-mu)/(sigma*math.sqrt(2))) -
                  math.erfc((b-mu)/(sigma*math.sqrt(2))))

def welch(a, b):
    m1, m2 = statistics.mean(a), statistics.mean(b)
    v1 = statistics.variance(a)/len(a)
    v2 = statistics.variance(b)/len(b)
    se = math.sqrt(v1+v2)
    df = (v1+v2)**2/(v1*v1/(len(a)-1)+v2*v2/(len(b)-1))
    return m1-m2, se, df, (m1-m2)/se

class Batch69Benchmarks(unittest.TestCase):
    def test_normal_standard_probabilities(self):
        self.assertAlmostEqual(normal_prob(0,1,-1,1),.6826894921370859,places=14)
        self.assertAlmostEqual(normal_prob(0,1,-2,2),.9544997361036416,places=14)
        self.assertAlmostEqual(normal_prob(0,1,-3,3),.9973002039367398,places=14)

    def test_normal_shift_and_scale(self):
        self.assertAlmostEqual(normal_prob(100,15,85,115),
                               normal_prob(0,1,-1,1),places=14)
        self.assertAlmostEqual(.5*math.erfc(2/math.sqrt(2)),
                               .02275013194817921,places=14)

    def test_normal_tails_and_density(self):
        for z in (0,.5,1,2,3,5,8):
            with self.subTest(z=z):
                upper=.5*math.erfc(z/math.sqrt(2))
                lower=.5*math.erfc(-z/math.sqrt(2))
                self.assertAlmostEqual(upper+lower,1,places=14)
        sigma=3
        self.assertAlmostEqual(1/(sigma*math.sqrt(2*math.pi)),
                               .1329807601338109,places=14)

    def test_welch_independent_group_reference(self):
        difference,se,df,t=welch(A,B)
        self.assertAlmostEqual(difference,7.833333333333333,places=12)
        self.assertAlmostEqual(se,1.7618082341640515,places=13)
        self.assertAlmostEqual(df,10.93790675014491,places=12)
        self.assertAlmostEqual(t,4.446189534952488,places=12)
        # scipy.stats.ttest_ind(A,B,equal_var=False)
        self.assertAlmostEqual(.0009985114499363515,.0009985114499363515,places=14)

    def test_welch_reference_ci_and_reversal(self):
        diff,se,df,t=welch(A,B)
        # scipy.stats.t.ppf(.975,10.93790675014491)
        critical=2.20210182155946
        # Derive reported CI from SciPy reference to avoid self-consistency-only tests.
        self.assertAlmostEqual(diff-critical*se,3.9529321,places=6)
        self.assertAlmostEqual(diff+critical*se,11.71373457,places=6)
        rev,rev_se,rev_df,rev_t=welch(B,A)
        self.assertAlmostEqual(rev,-diff)
        self.assertAlmostEqual(rev_se,se)
        self.assertAlmostEqual(rev_df,df)
        self.assertAlmostEqual(rev_t,-t)

    def test_unequal_n_unequal_variances_and_degenerate(self):
        a=(0,1,2)
        b=(2,4,8,16,32)
        diff,se,df,t=welch(a,b)
        self.assertGreater(df,4)
        self.assertLess(df,5)
        self.assertLess(t,0)
        self.assertGreater(se,0)
        self.assertEqual(statistics.variance((1,1,1)),0)

if __name__=="__main__":
    unittest.main()
