"""Independent mathematical benchmarks for Batch #63's geometric and CDF labs.

No JavaScript code is imported: compute the expected answers from probability
identities using Python's standard library. Browser tests compare site results.
"""
import math
import unittest


def geometric(p, k):
    if not (0 < p <= 1 and isinstance(k, int) and k >= 1):
        raise ValueError("Require 0<p<=1 and integer k>=1")
    q = 1 - p
    return (q ** (k - 1) * p, 1 - q ** k, q ** k, 1 / p, q / p ** 2)


def cdf(kind, x, *, p=.35, a=0, b=2):
    if kind == "bernoulli":
        return 0 if x < 0 else (1 - p if x < 1 else 1)
    if kind == "uniform" and a < b:
        return 0 if x <= a else (1 if x >= b else (x - a) / (b - a))
    raise ValueError("Invalid distribution or bounds")


class Batch63IndependentMathematics(unittest.TestCase):
    def test_geometric_reference_and_boundary(self):
        self.assertEqual(geometric(.25, 3), (.140625, .578125, .421875, 4, 12))
        self.assertEqual(geometric(1, 1), (1, 1, 0, 1, 0))
        self.assertEqual(geometric(1, 4), (0, 1, 0, 1, 0))
        self.assertAlmostEqual(geometric(.5, 3)[0], .125, places=15)
        self.assertAlmostEqual(geometric(.5, 10)[2], 2**-10, places=15)

    def test_geometric_normalization_and_memorylessness(self):
        for p in (.05, .1, .25, .5, .95, 1):
            with self.subTest(p=p):
                total = sum(geometric(p, k)[0] for k in range(1, 2000))
                self.assertAlmostEqual(total, 1, places=10)
                for k in (1, 3, 8, 20):
                    mass, cumulative, tail, mean, var = geometric(p, k)
                    self.assertAlmostEqual(cumulative + tail, 1, places=12)
                    self.assertAlmostEqual(mean, 1/p, places=12)
                    self.assertAlmostEqual(var, (1-p)/p**2, places=12)
                    if p < 1:
                        # For a conditional event of nonzero probability.
                        m, n = 2, 3
                        unconditional_survival = geometric(p, m+n)[2]
                        prior_survival = geometric(p, m)[2]
                        self.assertAlmostEqual(unconditional_survival/prior_survival,
                                               geometric(p, n)[2], places=12)

    def test_bernoulli_step_function_and_interval_endpoint(self):
        for p in (0, .25, .35, 1):
            self.assertEqual(cdf("bernoulli", -1, p=p), 0)
            self.assertAlmostEqual(cdf("bernoulli", 0, p=p), 1-p)
            self.assertAlmostEqual(cdf("bernoulli", .5, p=p), 1-p)
            self.assertEqual(cdf("bernoulli", 1, p=p), 1)
            # Lower-excluded: (0,1] contains X=1 but not X=0.
            self.assertAlmostEqual(cdf("bernoulli", 1, p=p) -
                                   cdf("bernoulli", 0, p=p), p)
            self.assertAlmostEqual(cdf("bernoulli", 0, p=p) -
                                   cdf("bernoulli", -.5, p=p), 1-p)

    def test_uniform_cdf_and_interval(self):
        for a, b in ((0,2), (-1,1),(.5,1.5)):
            self.assertEqual(cdf("uniform", a-1, a=a, b=b), 0)
            self.assertEqual(cdf("uniform", a, a=a, b=b), 0)
            self.assertEqual(cdf("uniform", b, a=a, b=b), 1)
            self.assertEqual(cdf("uniform", b+1, a=a, b=b), 1)
            self.assertAlmostEqual(cdf("uniform", (a+b)/2, a=a, b=b), .5)
            for x in (a-.1,a,(a+b)/2,b,b+.1):
                self.assertTrue(0 <= cdf("uniform", x, a=a, b=b) <= 1)
            self.assertAlmostEqual(
                cdf("uniform", b, a=a, b=b)-cdf("uniform", (a+b)/2, a=a, b=b),
                .5)


if __name__ == "__main__":
    unittest.main()
