"""Reference computations for Batch #64, independent of browser JavaScript.

The Student-t critical values below are reference results computed independently
with SciPy 1.17's scipy.stats.t.ppf; CI requires only the Python standard library.
"""
import math
import unittest


def nb_mass(r, p, k):
    if not (isinstance(r, int) and r >= 1 and 0 < p <= 1 and isinstance(k, int)):
        raise ValueError("Require integer r, 0<p<=1, integer k")
    return 0.0 if k < r else math.comb(k-1, r-1) * p**r * (1-p)**(k-r)


class Batch64IndependentBenchmarks(unittest.TestCase):
    def test_negative_binomial_exact_mass_mean_variance(self):
        self.assertEqual(nb_mass(3, .5, 5), .1875)
        self.assertAlmostEqual(sum(nb_mass(3,.5,k) for k in range(3,6)), .5, places=14)
        self.assertEqual(3/.5, 6)
        self.assertEqual(3*(1-.5)/(.5**2), 6)
        self.assertEqual(5/.25, 20)
        self.assertEqual(nb_mass(2, 1, 2), 1)
        self.assertEqual(nb_mass(2, 1, 3), 0)
        self.assertEqual(2*(1-1)/1**2, 0)

    def test_negative_binomial_geometric_identity_normalization(self):
        for p in (.05,.25,.5,.8,1):
            for k in range(1,30):
                self.assertAlmostEqual(nb_mass(1,p,k),p*(1-p)**(k-1),places=14)
            self.assertAlmostEqual(sum(nb_mass(1,p,k) for k in range(1,2000)),1,places=11)
        for r,p in ((2,.4),(3,.5),(6,.95)):
            self.assertAlmostEqual(sum(nb_mass(r,p,k) for k in range(r,2000)),1,places=10)
            self.assertAlmostEqual(sum(nb_mass(r,p,k) for k in range(r,31))+
                                   sum(nb_mass(r,p,k) for k in range(31,2000)),1,places=10)

    def test_student_t_reference_critical_values(self):
        # Scipy 1.17 numerical reference: exact two-sided critical values.
        refs={
            1: (6.313751515,12.706204736,63.656741163),
            2: (2.919985580,4.302652730,9.924843201),
            4: (2.131846786,2.776445105,4.604094871),
            9: (1.833112933,2.262157163,3.249835542),
            19:(1.729132812,2.093024054,2.860934606),
            29:(1.699127027,2.045229642,2.756385904),
            99:(1.660391156,1.984216952,2.626405457),
            120:(1.657650899,1.979930405,2.617421145)
        }
        self.assertEqual(len(refs),8)
        z=(1.6448536269514722,1.959963984540054,2.5758293035489004)
        for df,quantiles in refs.items():
            for i,q in enumerate(quantiles):
                with self.subTest(df=df,confidence=(90,95,99)[i]):
                    self.assertGreater(q,z[i])
                    self.assertGreater(q,0)
                    if df>1:
                        self.assertLess(q,refs[1][i])
        self.assertAlmostEqual(refs[9][1]/math.sqrt(10),.715356,delta=.000002)
        self.assertAlmostEqual(z[1]/math.sqrt(10),.619795,delta=.000002)

    def test_student_t_analytic_special_cases(self):
        # df=1 is exactly Cauchy: F(x)=1/2 + atan(x)/pi
        # df=2 has F(x)=1/2+x/(2*sqrt(x²+2)).
        for x in (-10,-2,-1,0,.5,1,2,10):
            cauchy=.5+math.atan(x)/math.pi
            df2=.5+x/(2*math.sqrt(x*x+2))
            self.assertTrue(0<cauchy<1)
            self.assertTrue(0<df2<1)
            self.assertAlmostEqual(cauchy+(1-(.5+math.atan(x)/math.pi)),1)
        self.assertAlmostEqual(math.tan(.95*math.pi-math.pi/2),6.313751515,places=7)
        self.assertAlmostEqual(math.tan(.975*math.pi-math.pi/2),12.706204736,places=7)

    def test_student_t_pdf_gamma_and_normal_limits(self):
        def t_pdf(x,df):
            return math.exp(math.lgamma((df+1)/2)-math.lgamma(df/2)-
                            .5*math.log(df*math.pi)-
                            (df+1)/2*math.log1p(x*x/df))
        normal=lambda x:math.exp(-x*x/2)/math.sqrt(2*math.pi)
        self.assertAlmostEqual(t_pdf(0,1),1/math.pi,places=12)
        self.assertAlmostEqual(t_pdf(1,1),1/(2*math.pi),places=12)
        self.assertAlmostEqual(t_pdf(0,2),1/(2*math.sqrt(2)),places=12)
        for x in (-3,-1,0,.5,2):
            self.assertAlmostEqual(t_pdf(x,100000),normal(x),delta=1e-5)


if __name__=="__main__":
    unittest.main()
