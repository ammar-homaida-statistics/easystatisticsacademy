"""Independent Batch #68 reference benchmarks.

Numeric targets cross-checked against scipy.stats.t (SciPy 1.17.0);
this CI module uses only Python's standard library.
"""
import math
import statistics
import unittest


def uniform(a,b,c,d):
    assert a < b and a <= c <= d <= b
    density=1/(b-a)
    return density,(d-c)*density,(a+b)/2,(b-a)**2/12,(b-a)/math.sqrt(12)


def paired(pairs):
    differences=[after-before for before,after in pairs]
    n=len(differences)
    mean=statistics.mean(differences)
    sd=statistics.stdev(differences)
    se=sd/math.sqrt(n)
    return mean,sd,se,mean/se,n-1


class Batch68ReferenceBenchmarks(unittest.TestCase):
    def test_uniform_area_and_moments(self):
        density,p,mean,var,sd=uniform(0,10,2,5)
        self.assertAlmostEqual(density,.1,places=15)
        self.assertAlmostEqual(p,.3,places=15)
        self.assertAlmostEqual(mean,5,places=15)
        self.assertAlmostEqual(var,100/12,places=14)
        self.assertAlmostEqual(sd,2.886751345948129,places=13)
        self.assertAlmostEqual(p,density*(5-2),places=15)

    def test_uniform_endpoints_and_translation_invariance(self):
        for a,b in ((0,1),(3,7),(1.5,9),(-5,-1)):
            with self.subTest(a=a,b=b):
                self.assertEqual(uniform(a,b,a,a)[1],0)
                self.assertEqual(uniform(a,b,a,b)[1],1)
                self.assertAlmostEqual(uniform(a,b,a,b)[3],(b-a)**2/12)
                self.assertAlmostEqual(uniform(a,b,a,b)[2],(a+b)/2)
        self.assertAlmostEqual(uniform(0,10,2,5)[1],uniform(7,17,9,12)[1])

    def test_paired_training_five_person_reference(self):
        obs=((70,75),(68,72),(75,79),(71,74),(69,74))
        mean,sd,se,t,df=paired(obs)
        self.assertEqual(df,4)
        self.assertAlmostEqual(mean,4.2,places=15)
        self.assertAlmostEqual(sd,math.sqrt(.7),places=14)
        self.assertAlmostEqual(se,.3741657386773941,places=14)
        self.assertAlmostEqual(t,11.224972160321826,places=12)
        # SciPy t.sf(|t|, 4) * 2 = 0.0003587352603774513
        # For df=4, I_x(2, 1/2) = 1 - (3/2)s + (1/2)s³,
        # with s=|t|/sqrt(4+t²); this is the exact two-sided tail.
        s=abs(t)/math.sqrt(4+t*t)
        two_sided_p=1-1.5*s+.5*s**3
        self.assertAlmostEqual(two_sided_p,.0003587352603774513,places=13)

    def test_paired_training_exact_two_sided_95_ci(self):
        _,_,se,_,df=paired(((70,75),(68,72),(75,79),(71,74),(69,74)))
        self.assertEqual(df,4)
        t975=2.7764451051977934 # scipy.stats.t.ppf(.975,4)
        self.assertAlmostEqual(4.2-t975*se,3.1611493663164323,places=12)
        self.assertAlmostEqual(4.2+t975*se,5.238850633683568,places=12)

    def test_student_t_upper_tail_and_critical_reference_constants(self):
        # scipy.stats.t.sf(2,df), scipy.stats.t.ppf(.975,df)
        table=[
           (1,.14758361765043326,12.706204736174694),
           (2,.09175170953613698,4.302652729749462),
           (4,.05805826175840778,2.7764451051977934),
           (9,.038276411885350504,2.262157162798205),
           (19,.03000101819304917,2.0930240544083087),
           (39,.026249507671927373,2.022690920036761),
        ]
        for df,tail,quantile in table:
            with self.subTest(df=df):
                self.assertGreater(tail,0)
                self.assertLess(tail,.5)
                self.assertGreater(quantile,1.95)
                self.assertLess(quantile,13)
        # Verify exact Cauchy(df=1) tail formula against SciPy.
        self.assertAlmostEqual(.5-math.atan(2)/math.pi,table[0][1],places=14)

    def test_pair_reversal_and_zero_variance(self):
        before_after=[(70,75),(68,72),(75,79),(71,74),(69,74)]
        reversed_pairs=[(after,before) for before,after in before_after]
        mean1,sd1,se1,t1,_=paired(before_after)
        mean2,sd2,se2,t2,_=paired(reversed_pairs)
        self.assertAlmostEqual(mean2,-mean1,places=14)
        self.assertAlmostEqual(t2,-t1,places=12)
        self.assertAlmostEqual(sd2,sd1,places=14)
        self.assertAlmostEqual(se2,se1,places=14)
        self.assertEqual(statistics.stdev([2,2,2,2]),0)


if __name__=="__main__":
    unittest.main()
