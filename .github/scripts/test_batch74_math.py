"""Independent reference tests for Batch #74. Standard library only."""
import math
import unittest

def total_probability(weights, conditionals):
    if len(weights)!=3 or len(conditionals)!=3:
        return None
    if any(not math.isfinite(x) or x<0 or x>1 for x in weights+conditionals):
        return None
    if abs(sum(weights)-1)>1e-9:
        return None
    return [weights[i]*conditionals[i] for i in range(3)]

def corrections(pvals, alpha):
    m=len(pvals)
    if not 2<=m<=12 or any(not math.isfinite(p) or p<0 or p>1 for p in pvals):
        return None
    if not 0<alpha<1: return None
    bonf=[min(1,m*p) for p in pvals]
    order=sorted(range(m), key=lambda i:(pvals[i],i))
    holm=[None]*m
    run=0
    for j,i in enumerate(order):
        run=max(run,(m-j)*pvals[i])
        holm[i]=min(1,run)
    return bonf,holm

class Batch74References(unittest.TestCase):
    def test_total_probability_example(self):
        contributions=total_probability([.2,.3,.5],[.1,.5,.8])
        self.assertIsNotNone(contributions)
        for x,y in zip(contributions,[.02,.15,.4]):
            self.assertAlmostEqual(x,y,places=14)
        self.assertAlmostEqual(sum(contributions),.57,places=14)
    def test_partition_boundaries(self):
        self.assertIsNone(total_probability([.2,.3,.4],[.1,.5,.8]))
        self.assertIsNone(total_probability([.2,.3,1],[.1,.5,.8]))
        self.assertIsNone(total_probability([-.1,.6,.5],[.1,.5,.8]))
        self.assertIsNone(total_probability([.2,.3,.5],[.1,1.1,.8]))
        self.assertIsNone(total_probability([0,0,0],[.1,.5,.8]))
        r=total_probability([0,1,0],[1,0,1])
        self.assertEqual(r,[0,0,0])
        self.assertEqual(sum(total_probability([0,1,0],[1,1,1])),1)
    def test_bonf_holm_reference_example(self):
        values=[.003,.018,.041,.22]
        bonf,holm=corrections(values,.05)
        for actual,reference in zip(bonf,[.012,.072,.164,.88]):
            self.assertAlmostEqual(actual,reference,places=12)
        for actual,reference in zip(holm,[.012,.054,.082,.22]):
            self.assertAlmostEqual(actual,reference,places=12)
        self.assertEqual(sum(v<=.05 for v in holm),1)
        self.assertEqual(sum(v<=.05 for v in bonf),1)
    def test_reordered_and_tied_pvalues(self):
        values=[.22,.041,.003,.018]
        bonf,holm=corrections(values,.05)
        for x,y in zip(holm,[.22,.082,.012,.054]):
            self.assertAlmostEqual(x,y,places=12)
        _,ties=corrections([.01,.01,.02],.05)
        for x,y in zip(ties,[.03,.03,.03]):
            self.assertAlmostEqual(x,y,places=12)
    def test_pvalue_bounds_monotonicity_and_decisions(self):
        for arr in ([0,0],[1,1],[0,.02,.5,1],[.5,.001,.04,.04,1]):
            corrected=corrections(list(arr),.05)
            self.assertIsNotNone(corrected)
            bonf,holm=corrected
            self.assertTrue(all(0<=v<=1 for v in bonf+holm))
            self.assertTrue(all(holm[i]<=bonf[i]+1e-12 for i in range(len(arr))))
            pairs=sorted(zip(arr,holm))
            self.assertTrue(all(pairs[i][1]<=pairs[i+1][1] for i in range(len(arr)-1)))
        self.assertIsNone(corrections([-.1,.1],.05))
        self.assertIsNone(corrections([.2,1.1],.05))
        self.assertIsNone(corrections([.2],.05))
    def test_familywise_independent_formula_and_union_bound(self):
        m,alpha=4,.05
        exact=1-(1-alpha)**m
        self.assertAlmostEqual(exact,.18549375,places=12)
        self.assertLessEqual(exact,m*alpha)
        self.assertAlmostEqual(min(1,m*alpha),.2,places=12)
        self.assertAlmostEqual(1-(1-.05)**2,.0975,places=12)

if __name__=="__main__":
    unittest.main()
