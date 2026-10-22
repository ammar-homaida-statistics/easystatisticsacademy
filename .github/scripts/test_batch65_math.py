"""Independent reference checks for Batch #65 mathematics.

Expected F statistics and p-values were independently verified against
SciPy 1.17's scipy.stats.f_oneway. This test uses only Python stdlib.
"""
import math
import unittest


def one_way_stats(groups):
    sizes=[len(g) for g in groups]
    n=sum(sizes)
    k=len(groups)
    means=[math.fsum(g)/len(g) for g in groups]
    grand=math.fsum(map(math.fsum,groups))/n
    between=math.fsum(sizes[i]*(means[i]-grand)**2 for i in range(k))
    within=math.fsum((x-means[i])**2 for i,g in enumerate(groups) for x in g)
    if within==0:
        statistic=math.inf if between>0 else math.nan
    else:
        statistic=(between/(k-1))/(within/(n-k))
    return (between, within, k-1, n-k, statistic)


class Batch65ReferenceMathematics(unittest.TestCase):
    def test_exponential_pdf_cdf_survival_moments(self):
        for rate in (.2, .5, 1, 2, 4, 20):
            with self.subTest(rate=rate):
                self.assertAlmostEqual(
                    math.fsum(rate*math.exp(-rate*(j+.5)*.0005)*.0005
                              for j in range(100000)), 1,
                    places=3 if rate==.2 else 5)
                for t in (0,.25,1,3,7):
                    cdf=-math.expm1(-rate*t)
                    tail=math.exp(-rate*t)
                    self.assertAlmostEqual(cdf+tail,1,places=14)
                    self.assertGreaterEqual(cdf,0)
                    self.assertLessEqual(cdf,1)
                self.assertEqual(1/rate,math.sqrt(1/(rate*rate)))

    def test_exponential_reference_example_and_memoryless(self):
        self.assertAlmostEqual(1-math.exp(-2),0.8646647167633873,places=15)
        self.assertAlmostEqual(math.exp(-2),0.1353352832366127,places=15)
        self.assertAlmostEqual(1/4*60,15,places=15)
        for rate in (.1,.5,2.):
            for s,t in ((0,2),(.5,1),(2,3)):
                conditional=math.exp(-rate*(s+t))/math.exp(-rate*s)
                self.assertAlmostEqual(conditional,math.exp(-rate*t),places=13)

    def test_anova_equal_sizes_reference_f_and_p(self):
        groups=([4,5,6],[5,6,7],[8,9,10])
        ssb,ssw,dfb,dfw,f=one_way_stats(groups)
        self.assertEqual((ssb,ssw,dfb,dfw,f),(26,6,2,6,13))
        # Closed form F(d1=2,d2): SF(f)=(d2/(d2+2f))**(d2/2).
        p=(dfw/(dfw+2*f))**(dfw/2)
        self.assertAlmostEqual(p,0.006591796875,places=14)

    def test_anova_unequal_sample_sizes_reference(self):
        groups=([2,3,6,7],[3,4],[8,8,9,10,11])
        ssb,ssw,dfb,dfw,f=one_way_stats(groups)
        self.assertEqual((dfb,dfw),(2,8))
        self.assertAlmostEqual(f,11.592966704077819,places=12)
        self.assertAlmostEqual((dfw/(dfw+2*f))**(dfw/2),
                               0.004330369539241011,places=12)
        self.assertAlmostEqual(ssb+ssw,math.fsum((x-(math.fsum(
            map(math.fsum,groups))/11))**2 for g in groups for x in g),places=12)

    def test_anova_zero_within_and_all_equal(self):
        self.assertTrue(math.isinf(one_way_stats(
            ([1,1,1],[2,2,2],[3,3,3]))[4]))
        self.assertTrue(math.isnan(one_way_stats(
            ([2,2,2],[2,2,2],[2,2,2]))[4]))
        self.assertEqual(one_way_stats(
            ([3,5,7],[3,5,7],[3,5,7]))[4],0)

    def test_anova_f_distribution_reference_quantile_cases(self):
        # Independent SciPy reference SF values for F=4 at dfs (2,10), (1,10).
        self.assertAlmostEqual((10/(10+2*4))**(10/2),
                               0.05292214940134464,places=12)
        # For d1=2, the closed form follows from beta(1,d2/2).
        self.assertAlmostEqual((6/(6+2*13))**3,0.006591796875,places=15)


if __name__=="__main__":
    unittest.main()
