---
layout: default
title: One-Proportion Z Test
description: Learn how the one-proportion Z test evaluates whether a population proportion differs from a hypothesized value.
permalink: /inference/classical-tests/one-proportion-z-test/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/one-proportion-z-test/",
    label: "One-Proportion Z Test",
    ts: Date.now()
  }));
  } catch (_) {
    // Disabled browser storage must not interrupt the lesson.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 4</span>
      <span class="badge">Classical Tests</span>
      <span class="badge">Proportions</span>
    </div>

    <h1>One-Proportion Z Test</h1>

    <p class="lead">
      Many statistical questions involve proportions rather than means.
    </p>

    <p class="lead">
      The one-proportion Z test evaluates whether a population proportion differs from a hypothesized value using sample data and normal approximations.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/two-sample-t-test-independent/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/two-proportion-z-test/">
         Next: Two-Proportion Z Test →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>When Do We Use a Proportion Test?</h2>

    <p>
      Some variables have only two possible outcomes.
    </p>

    <div class="example-box">

      <p>
        Success / Failure
      </p>

      <p>
        Yes / No
      </p>

      <p>
        Purchased / Did Not Purchase
      </p>

      <p>
        Defective / Non-Defective
      </p>

    </div>

    <p>
      In these situations, the parameter of interest is often a population proportion.
    </p>

    <h2>The Population Proportion</h2>

    <p>
      The symbol:
    </p>

    \[
p\in[0,1]
\]

    <p>
      represents the true population proportion.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Proportion of voters supporting a candidate</li>

      <li>Proportion of customers who purchase a product</li>

      <li>Proportion of defective items produced</li>

      <li>Proportion of patients responding to treatment</li>

    </ul>

    <h2>The Research Question</h2>

    <p>
      Suppose a company claims:
    </p>

    \[
p_0=0.50
\]

    <p>
      meaning that 50% of customers prefer a new product design.
    </p>

    <p>
      A researcher wants to determine whether the true proportion differs from that claim.
    </p>

    <h2>The Hypotheses</h2>

    <p>
      The standard two-sided hypotheses are:
    </p>

    \[
H_0:p=p_0
\]

    <br><br>

    \[
H_1:p\ne p_0
\]

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>p = true population proportion</li>

      <li>p₀ = hypothesized proportion</li>

    </ul>

    <h2>One-Sided Alternatives</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Alternative Hypothesis</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>p ≠ p₀</td>
            <td>Proportion differs</td>
          </tr>

          <tr>
            <td>p &gt; p₀</td>
            <td>Proportion is larger</td>
          </tr>

          <tr>
            <td>p &lt; p₀</td>
            <td>Proportion is smaller</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Sample Proportion</h2>

    <p>
      The observed sample proportion is:
    </p>

    \[
\hat p=\frac{x}{n}
\]

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>x = number of successes</li>

      <li>n = sample size</li>

    </ul>

    <h2>Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        120 out of 200 customers prefer the product.
      </p>
    </div>

    <p>
      Then:
    </p>

    \[
\hat p=\frac{120}{200}=0.60
\]

    <h2>The Standard Error Under H₀</h2>

    <p>
      Under the null hypothesis:
    </p>

    \[
p=p_0
\]

    <p>
      the standard error becomes:
    </p>

    \[
\operatorname{SE}_0(\hat p)=\sqrt{\frac{p_0(1-p_0)}{n}}
\]

    <p>
      Notice that the null value:
    </p>

    \[
p_0
\]

    <p>
      appears in the formula.
    </p>

    <h2>The Z Statistic</h2>

    <p>
      The one-proportion Z statistic is:
    </p>

    \[
Z=\frac{\hat p-p_0}{\sqrt{p_0(1-p_0)/n}}
\]

    <p>
      This measures how many standard errors separate the observed sample proportion from the null value.
    </p>

    <!-- Batch #71: interactive one-proportion Z test and Wilson/Wald intervals -->
<section class="concept-box" id="esa-one-proportion-lab" aria-labelledby="esa-op-heading">
<h2 id="esa-op-heading">Interactive One-Proportion Z-Test Laboratory</h2>
<p>Enter a sample size, number of successes, and the hypothesized population proportion. The Z statistic uses the <strong>null-based</strong> standard error; compare the familiar Wald 95% confidence interval with the more reliable Wilson score interval.</p>
<div class="esa-op-grid">
<label for="esa-op-x">Successes x <input id="esa-op-x" type="number" min="0" max="1000000" step="1" value="120"></label>
<label for="esa-op-n">Sample size n <input id="esa-op-n" type="number" min="1" max="1000000" step="1" value="200"></label>
<label for="esa-op-p0">Null proportion p₀ <input id="esa-op-p0" type="number" min="0" max="1" step="any" value="0.50"></label>
<label for="esa-op-alternative">Alternative hypothesis
<select id="esa-op-alternative"><option value="two-sided">Two-sided p ≠ p₀</option>
<option value="greater">Greater p &gt; p₀</option><option value="less">Less p &lt; p₀</option></select></label>
</div>
<button type="button" class="btn btn-outline" id="esa-op-reset">Restore worked example</button>
<p id="esa-op-error" role="alert" hidden></p>
<section id="esa-op-results" aria-live="polite" aria-atomic="true" aria-label="One-proportion Z inference results">
<p><strong>Observed proportion p̂:</strong> <output id="esa-op-phat"></output>.
<strong>Null-based SE:</strong> <output id="esa-op-se0"></output>.
<strong>Z statistic:</strong> <output id="esa-op-z"></output>.
<strong>Normal p-value:</strong> <output id="esa-op-pvalue"></output>.</p>
<p><strong>Estimated (Wald) SE:</strong> <output id="esa-op-seWald"></output>.</p>
<div class="table-wrap"><table><caption>Approximate two-sided 95% confidence intervals for the population proportion</caption>
<thead><tr><th>Interval method</th><th>Lower limit</th><th>Upper limit</th></tr></thead>
<tbody>
<tr><th scope="row">Wald</th><td><output id="esa-op-waldLower"></output></td><td><output id="esa-op-waldUpper"></output></td></tr>
<tr><th scope="row">Wilson score</th><td><output id="esa-op-wilsonLower"></output></td><td><output id="esa-op-wilsonUpper"></output></td></tr>
</tbody></table></div>
<svg id="esa-op-plot" viewBox="0 0 620 185" role="img"
aria-label="Wald and Wilson 95 percent confidence intervals compared with null proportion"></svg>
<p id="esa-op-conditions"></p><p id="esa-op-decision"></p><p id="esa-op-interpretation"></p>
</section>
<p class="muted-mini">Assumptions: binary outcome, independent random or appropriately designed observations, and adequate success–failure counts under H₀. For finite populations sampled without replacement, assess the sampling fraction. The normal p-value is approximate; an exact binomial test may be preferable when counts are small. The confidence intervals are two-sided and do not change when selecting a one-sided test. Significance does not imply a causal effect, and failure to reject does not prove equality. No observations are stored.</p>
</section>
<style>
#esa-one-proportion-lab{max-width:100%;min-width:0;box-sizing:border-box;overflow-wrap:anywhere}
#esa-one-proportion-lab .esa-op-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:14px 0}
#esa-one-proportion-lab label{display:block;font-weight:600;min-width:0}
#esa-one-proportion-lab :is(input,select){display:block;box-sizing:border-box;width:100%;min-width:0;max-width:100%;padding:9px;font:inherit;border:1px solid var(--border);border-radius:8px}
#esa-one-proportion-lab [hidden]{display:none!important}
#esa-one-proportion-lab svg{display:block;width:100%;height:auto;max-width:640px;margin:10px auto}
#esa-one-proportion-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-one-proportion-lab output{font-variant-numeric:tabular-nums}
#esa-one-proportion-lab :is(input,select,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
@media(max-width:650px){#esa-one-proportion-lab .esa-op-grid{grid-template-columns:minmax(0,1fr)}}
@media print{#esa-one-proportion-lab .esa-op-grid,#esa-one-proportion-lab button{display:none}}
</style>
<script defer src="/js/one-proportion-z-explorer.js"></script>
<h2>Worked Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>n = 200</p>
      <p>x = 120</p>
      <p>p₀ = 0.50</p>

    </div>

    <p>
      The sample proportion is:
    </p>

    \[
\hat p=\frac{120}{200}=0.60
\]

    <h2>Compute the Standard Error</h2>

    <p>
      Using:
    </p>

    \[
\operatorname{SE}_0(\hat p)=\sqrt{\frac{0.50(1-0.50)}{200}}
\]

    <p>
      gives:
    </p>

    \[
\operatorname{SE}_0(\hat p)=\sqrt{0.00125}\approx0.03536
\]

    <h2>Compute the Test Statistic</h2>

    <p>
      Therefore:
    </p>

    \[
Z=\frac{0.60-0.50}{0.035355\ldots}
\]

    <p>
      which gives approximately:
    </p>

    \[
Z\approx2.8284
\]

    <h2>The p-Value</h2>

    <p>
      Under:
    </p>

    \[
H_0:p=p_0=0.50
\]

    <p>
      the statistic follows the standard normal distribution approximately.
    </p>

    <p>
      For a two-sided test:
    </p>

    <div class="example-box">

      <p>
        p-value ≈ 0.0047 (two-sided normal approximation)
      </p>
    </div>

    <h2>The Decision</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        α = 0.05
      </p>
    </div>

    <p>
      Since:
    </p>

    \[
0.0047<0.05
\]

    <p>
      we reject:
    </p>

    \[
H_0
\]

    <h2>Interpretation</h2>

    <div class="example-box">

      <p>
        The sample provides evidence that the population proportion differs from 50%.
      </p>
    </div>

    <h2>Why a Z Distribution?</h2>

    <p>
      The sampling distribution of:
    </p>

    \[
\hat p
\]

    <p>
      becomes approximately normal when the sample size is sufficiently large.
    </p>

    <p>
      This approximation comes from the Central Limit Theorem.
    </p>

    <h2>Success-Failure Condition</h2>

    <p>
      The normal approximation is generally considered reasonable when:
    </p>

    \[
np_0\ge10
\]

    <p>
      and:
    </p>

    \[
n(1-p_0)\ge10
\]

    <p>
      under the null hypothesis. Here, \(np_0=100\) and \(n(1-p_0)=100\), satisfying the usual rule of thumb.
    </p>

    <h2>Assumptions</h2>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Independent observations</li>

      <li>Binary outcomes</li>

      <li>Success-failure condition satisfied</li>

      <li>Sample size small relative to population size when sampling without replacement</li>

    </ul>

    <h2>Confidence Interval Connection</h2>

    <p>
      The corresponding confidence interval for a population proportion is:
    </p>

    \[
\hat p\pm z_{1-\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}
\]

    <p>
      This familiar unpooled Wald interval is an approximation, not the exact inversion of the null-pooled Z test above. Inverting the score test gives the Wilson score interval; Wald and score methods can differ, especially for small samples or proportions near 0 or 1. For this example, the Wald interval excludes 0.50 at 95% confidence.
    </p>

    <h2>Common Applications</h2>

    <div class="example-box">

      <p>
        Election polling
      </p>

      <p>
        Product approval studies
      </p>

      <p>
        Customer satisfaction surveys
      </p>

      <p>
        Quality-control inspections
      </p>

      <p>
        Medical response rates
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      The one-proportion Z test extends hypothesis testing from numerical measurements to binary outcomes.
    </p>

    <p>
      Instead of evaluating means, it evaluates population proportions using the sampling distribution of sample proportions.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The one-proportion Z test evaluates whether a population proportion differs from a hypothesized value. It uses the sample proportion, a null-based standard error, and a normal approximation to measure evidence against the null hypothesis.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Many practical studies compare proportions between two groups rather than testing a single proportion.
    </p>

    <p>
      Examples include comparing conversion rates, approval rates, treatment success rates, and defect rates.
    </p>

    <p>
      The next lesson introduces the two-proportion Z test for comparing population proportions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The one-proportion Z test evaluates a single population proportion</li>

        <li>The parameter of interest is p</li>

        <li>The sample proportion is x/n</li>

        <li>The null hypothesis usually states p = p₀</li>

        <li>The standard error is computed using p₀ under the null hypothesis</li>

        <li>The test statistic follows an approximate standard normal distribution</li>

        <li>The success-failure condition supports the normal approximation</li>

        <li>The test is widely used for binary-outcome data</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/two-sample-t-test-independent/">
         ← Previous: Two-Sample t Test
      </a>

      <a class="btn"
         href="/inference/classical-tests/two-proportion-z-test/">
         Next: Two-Proportion Z Test →
      </a>

    </div>

  </div>

</section>