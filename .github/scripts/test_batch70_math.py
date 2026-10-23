"""Batch #70 independent lognormal and two-proportion numerical benchmarks.
Reference values cross-checked using scipy.stats.lognorm, scipy.stats.norm,
scipy.stats.binomtest / manually computed pooled equality-null Z; runtime uses stdlib.
"""
import math
import unittest

class Batch70IndependentBenchmarks(unittest.TestCase):
    def test_lognormal_moments(self):
        mu,sigma=0,.5
        median=math.exp(mu)
        mode=math.exp(mu-sigma*sigma)
        mean=math.exp(mu+sigma*sigma/2)
        variance=math.expm1(sigma*sigma)*math.exp(2*mu+sigma*sigma)
        self.assertAlmostEqual(median,1.0,places=14)
        self.assertAlmostEqual(mode,.7788007830714049,places=14)
        self.assertAlmostEqual(mean,1.1331484530668263,places=14)
        self.assertAlmostEqual(variance,.3646958540123865,places=14)
        self.assertAlmostEqual(math.sqrt(variance),.603900533212,delta=2e-6)
        self.assertLess(mode,median)
        self.assertLess(median,mean)

    def test_lognormal_cdf_and_interval(self):
        def cdf(x,mu,sigma):
            return .5*math.erfc(-(math.log(x)-mu)/sigma/math.sqrt(2)) if x>0 else 0
        self.assertAlmostEqual(cdf(1,0,.5),.5,places=14)
        self.assertAlmostEqual(cdf(2,0,.5)-cdf(1,0,.5),
                               .4171714809983016,places=14)
        self.assertAlmostEqual(cdf(math.exp(.5),0,.5)-cdf(math.exp(-.5),0,.5),
                               .6826894921370859,places=14)
        self.assertAlmostEqual(1-cdf(2,0,.5),.0828285190016984,places=13)
        self.assertEqual(cdf(0,0,.5),0)
        self.assertEqual(cdf(-20,0,.5),0)

    def test_log_scale_parameter_shift(self):
        # Multiplying X by e^k shifts the log-location by k without changing log-scale SD.
        k=1.2
        self.assertAlmostEqual(math.exp(k+.5**2/2),
                               math.exp(k)*math.exp(.5**2/2),places=14)

    def test_two_proportion_pooled_equality_reference(self):
        x1,n1,x2,n2=120,200,90,200
        p1,p2=x1/n1,x2/n2
        pooled=(x1+x2)/(n1+n2)
        pooledSE=math.sqrt(pooled*(1-pooled)*(1/n1+1/n2))
        z=(p1-p2)/pooledSE
        p=math.erfc(abs(z)/math.sqrt(2))
        self.assertAlmostEqual(pooled,.525,places=14)
        self.assertAlmostEqual(pooledSE,.04993746088859544,places=14)
        self.assertAlmostEqual(z,3.003757045930553,places=12)
        self.assertAlmostEqual(p,.0026666817936140935,places=14)

    def test_unpooled_wald_ci_not_null_se(self):
        p1,p2=.6,.45
        se=math.sqrt(p1*(1-p1)/200+p2*(1-p2)/200)
        self.assertAlmostEqual(se,.049371044145328745,places=14)
        critical=1.959963984540054
        self.assertAlmostEqual(.15-critical*se,.05323453159602119,places=13)
        self.assertAlmostEqual(.15+critical*se,.24676546840397873,places=13)

    def test_small_sample_checks_and_zero_variance(self):
        self.assertFalse(all(v>=10 for v in (10*.5,10*.5,10*.5,10*.5)))
        p=(0+0)/(20+30)
        self.assertEqual(p*(1-p),0)
        self.assertTrue(all(v>=10 for v in (200*.525,200*.475,200*.525,200*.475)))
if __name__=="__main__":
    unittest.main()
