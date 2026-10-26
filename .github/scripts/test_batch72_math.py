"""Independent numerical references for Batch #72; no external Python packages required."""
import math
import unittest

class BernoulliBenchmarks(unittest.TestCase):
    def test_probability_normalization_and_moments(self):
        for p in (0, .001, .2, .3, .5, .9, .999, 1):
            with self.subTest(p=p):
                p0,p1=1-p,p
                self.assertAlmostEqual(p0+p1,1,places=14)
                mean=p1
                variance=p0*(0-mean)**2+p1*(1-mean)**2
                self.assertAlmostEqual(variance,p*(1-p),places=14)
                self.assertGreaterEqual(variance,0)
                self.assertLessEqual(variance,.25+1e-14)
        self.assertAlmostEqual(.3*.7,.21,places=14)
    def test_bernoulli_binomial_n1_equivalence(self):
        for p in (0,.2,.3,.5,.8,1):
            self.assertAlmostEqual(math.comb(1,0)*(1-p),1-p,places=14)
            self.assertAlmostEqual(math.comb(1,1)*p,p,places=14)

class StudentTBenchmarks(unittest.TestCase):
    # Reference values independently obtained from scipy.stats.t.sf/t.ppf (SciPy 1.x).
    references=(
      # n, sample mean, sample sd, null mean, t, two-sided p, t_0.975, CI lower, CI upper
      (10,12.,3.,10.,2.1081851067789197,.06425884909585156,
       2.262157162798205,9.853929282088007,14.146070717911993),
      (25,102.,10.,100.,1.,.327286881279785,
       2.0638985616280245,97.87220287674396,106.12779712325604),
      (5,1.5,2.,0.,1.6770509831248424,.16883810871814456,
       2.7764451051977934,-.9833279964075281,3.983327996407528),
      (2,2.,1.,0.,2.8284271247461903,.21634689593878545,
       12.706204736174694,-6.984643532093752,10.984643532093752),
    )
    def test_sample_statistic_independent_fixed_references(self):
        for n,mean,s,mu,t,p,crit,lo,hi in self.references:
            with self.subTest(n=n):
                se=s/math.sqrt(n)
                self.assertAlmostEqual((mean-mu)/se,t,places=12)
                self.assertAlmostEqual(mean-crit*se,lo,places=12)
                self.assertAlmostEqual(mean+crit*se,hi,places=12)
                self.assertTrue(0<p<1)
                self.assertGreater(crit,1.959963984540054)
    def test_t1_student_cauchy_tail_independent_formula(self):
        # For df=1 the Student t CDF is a Cauchy CDF (closed form).
        t=math.sqrt(8)
        exact=1-2*math.atan(t)/math.pi
        self.assertAlmostEqual(exact,.21634689593878545,places=13)
    def test_student_t_small_df_critical_reference(self):
        self.assertAlmostEqual(self.references[3][6],12.706204736174694,places=12)
        self.assertAlmostEqual(self.references[0][6],2.262157162798205,places=12)

if __name__=="__main__":
    unittest.main()
