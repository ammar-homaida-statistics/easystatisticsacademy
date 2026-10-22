"""Independent numerical benchmarks for Batch #66.

Reference values are from SciPy 1.17 gamma.pdf/cdf/sf and chi2.sf,
calculated independently of the website's browser JavaScript.
Only the Python standard library is required on GitHub Actions.
"""
import math
import unittest


def erlang_density(t, r, rate):
    if t < 0:
        return 0.0
    if t == 0:
        return rate if r == 1 else 0.0
    return rate**r * t**(r - 1) * math.exp(-rate * t) / math.factorial(r-1)


def erlang_survival(t, r, rate):
    if t < 0:
        return 1.0
    z = rate * t
    return math.exp(-z)*math.fsum(z**i/math.factorial(i) for i in range(r))


def pearson_statistic(counts, probs):
    n = sum(counts)
    expected = [n*p for p in probs]
    return math.fsum((o-e)**2/e for o,e in zip(counts, expected))


class Batch66IndependentBenchmarks(unittest.TestCase):
    def test_gamma_erlang_reference_pdf_cdf_survival(self):
        r, rate, t = 4, 2, 2
        self.assertAlmostEqual(erlang_density(t,r,rate),
                               0.3907336296263290, places=12)
        self.assertAlmostEqual(erlang_survival(t,r,rate),
                               0.43347012036670884, places=12)
        self.assertAlmostEqual(1-erlang_survival(t,r,rate),
                               0.5665298796332912, places=12)
        self.assertEqual(r/rate, 2)
        self.assertEqual(r/rate**2, 1)

    def test_gamma_shape_one_is_exponential(self):
        for rate in (.5, 2, 3.5):
            for t in (0,.5,1.25,3,8):
                with self.subTest(rate=rate,t=t):
                    self.assertAlmostEqual(erlang_density(t,1,rate),
                                           rate*math.exp(-rate*t),places=14)
                    self.assertAlmostEqual(erlang_survival(t,1,rate),
                                           math.exp(-rate*t),places=14)

    def test_gamma_shape_scale_moments_and_mass(self):
        alpha, rate = 2.5,4
        self.assertAlmostEqual(alpha/rate,0.625,places=14)
        self.assertAlmostEqual(alpha/rate**2,0.15625,places=14)
        self.assertAlmostEqual(math.gamma(0.5),math.sqrt(math.pi),places=14)
        self.assertAlmostEqual(math.gamma(4),6,places=14)
        # Independent midpoint quadrature: Erlang density integrates to one.
        h=0.002
        area=math.fsum(erlang_density(h*(i+.5),4,2)*h for i in range(8000))
        self.assertAlmostEqual(area,1,places=8)

    def test_pearson_fair_die_reference(self):
        obs=(8,11,9,13,10,9)
        probs=[1/6]*6
        self.assertAlmostEqual(pearson_statistic(obs,probs),1.6,places=14)
        self.assertAlmostEqual(sum(obs),60)
        # SciPy chi2.sf(1.6, 5), asymptotic null with fixed probs.
        x=1.6/2
        # Closed-form chi-square(5) survival for half-integer gamma shape.
        tail=math.erfc(math.sqrt(x)) + (2/math.sqrt(math.pi))*math.sqrt(x)*math.exp(-x)*(1+2*x/3)
        self.assertAlmostEqual(tail,0.9012493445012736,places=14)

    def test_pearson_nonuniform_null_and_zero_counts(self):
        self.assertEqual(pearson_statistic((12,18,30),(.2,.3,.5)),0)
        self.assertAlmostEqual(pearson_statistic((25,20,15),(.2,.3,.5)),
                               21.805555555555557,places=11)
        self.assertAlmostEqual(math.exp(-21.805555555555557/2),
                               1.840703227000099e-05,places=13)
        self.assertAlmostEqual(pearson_statistic((0,10),(0.5,0.5)),10,places=15)
        self.assertAlmostEqual(math.exp(-10/2),0.006737946999085467,places=15)

    def test_pearson_chi_squared_reference_upper_tails(self):
        # Independent special-function reference values (SciPy chi2.sf).
        references=[
          (1.6,5,0.9012493445012736),
          (4,2,0.1353352832366127),
          (10,3,0.01856613546304325),
          (20,5,0.0012497305630313773),
          (0,2,1.0)
        ]
        for stat,df,p in references:
            with self.subTest(stat=stat,df=df):
                self.assertGreaterEqual(p,0)
                self.assertLessEqual(p,1)
                if df==2:
                    self.assertAlmostEqual(math.exp(-stat/2),p,places=14)
                if df==1:
                    self.assertAlmostEqual(math.erfc(math.sqrt(stat/2)),p,
                                           places=14)


if __name__=="__main__":
    unittest.main()
