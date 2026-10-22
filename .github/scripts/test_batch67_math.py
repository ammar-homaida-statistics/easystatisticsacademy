"""Independent reference checks for Batch #67.

Numerical chi-square tail constants were checked separately with SciPy 1.17.
These CI tests depend only on Python's standard library.
"""
import math
import unittest


def pearson_homogeneity(matrix):
    R, C = len(matrix), len(matrix[0])
    totals = [math.fsum(row) for row in matrix]
    columns = [math.fsum(matrix[i][j] for i in range(R)) for j in range(C)]
    n = math.fsum(totals)
    expected = [[totals[i]*columns[j]/n for j in range(C)]
                for i in range(R)]
    chi = math.fsum(
        (matrix[i][j]-expected[i][j])**2/expected[i][j]
        for i in range(R) for j in range(C))
    return chi, (R-1)*(C-1), expected


class Batch67IndependentBenchmarks(unittest.TestCase):
    def test_beta_density_and_normalization(self):
        # The Beta(2,2) density is 6x(1-x), integrating to exactly one.
        self.assertAlmostEqual(6*.5*(1-.5),1.5,places=15)
        self.assertEqual(6*(.5**2/2-.5**3/3),.5)
        # B(a,b) is the gamma-function normalization.
        self.assertAlmostEqual(
            math.gamma(8)*math.gamma(2)/math.gamma(10),1/72,places=14)
        self.assertAlmostEqual(
            math.gamma(1)*math.gamma(1)/math.gamma(2),1,places=15)
        self.assertAlmostEqual(math.gamma(2)*math.gamma(2)/math.gamma(4),
                               1/6,places=15)

    def test_beta_eight_two_mean_variance_and_sd(self):
        a,b=8,2
        mean=a/(a+b)
        variance=a*b/((a+b)**2*(a+b+1))
        self.assertAlmostEqual(mean,.8,places=15)
        self.assertAlmostEqual(variance,16/1100,places=15)
        self.assertAlmostEqual(variance,.014545454545454545,places=15)
        self.assertAlmostEqual(math.sqrt(variance),.12060453783110545,places=14)

    def test_beta_uniform_symmetric_and_bayesian_posterior(self):
        self.assertAlmostEqual(1/(1+1),.5,places=15)
        self.assertAlmostEqual(2/(2+2),20/(20+20),places=15)
        self.assertLess(20*20/(40**2*41),2*2/(4**2*5))
        prior=(2,2)
        successes,failures=8,2
        posterior=(prior[0]+successes,prior[1]+failures)
        self.assertEqual(posterior,(10,4))
        self.assertAlmostEqual(posterior[0]/sum(posterior),10/14,places=15)
        self.assertNotEqual(posterior[0]/sum(posterior),successes/10)

    def test_homogeneity_three_populations_reference(self):
        obs=[[40,35,25],[30,45,25],[50,30,20]]
        chi,df,expected=pearson_homogeneity(obs)
        self.assertEqual(df,4)
        self.assertAlmostEqual(chi,8.896103896103897,places=12)
        self.assertEqual([sum(row) for row in obs],[100,100,100])
        self.assertAlmostEqual(expected[0][0],40,places=15)
        self.assertAlmostEqual(expected[0][1],110/3,places=12)
        self.assertAlmostEqual(expected[0][2],70/3,places=12)
        # For df=4, chi-square upper tail = exp(-chi/2)*(1+chi/2).
        p=math.exp(-chi/2)*(1+chi/2)
        self.assertAlmostEqual(p,.06374950599967244,places=13)

    def test_homogeneity_equal_proportions_and_unequal_sizes(self):
        chi,df,_=pearson_homogeneity([[10,10],[10,10]])
        self.assertEqual((chi,df),(0,1))
        self.assertEqual(math.erfc(math.sqrt(chi/2)),1)
        chi,df,expected=pearson_homogeneity([[5,20,15],[8,10,12]])
        self.assertEqual(df,2)
        self.assertAlmostEqual(chi,2.9914529914529924,places=12)
        self.assertAlmostEqual(math.exp(-chi/2),.2240857482419603,places=13)
        self.assertAlmostEqual(expected[0][0],40*13/70,places=14)

    def test_homogeneity_sparse_cells_reference(self):
        chi,df,expected=pearson_homogeneity([[0,10],[8,12]])
        self.assertEqual(df,1)
        self.assertAlmostEqual(chi,5.454545454545455,places=12)
        self.assertLess(min(map(min,expected)),5)
        # Chi-square(1) tail = erfc(sqrt(chi/2)).
        self.assertAlmostEqual(math.erfc(math.sqrt(chi/2)),
                               .01951748118217779,places=13)


if __name__=="__main__":
    unittest.main()
