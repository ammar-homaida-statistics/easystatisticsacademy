---
layout: default
title: Two-Proportion Z Test
description: Learn how the two-proportion Z test compares population proportions from two independent groups and evaluates whether they differ.
permalink: /inference/classical-tests/two-proportion-z-test/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/two-proportion-z-test/",
    label: "Two-Proportion Z Test",
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
      <span class="badge">Comparing Proportions</span>
    </div>

    <h1>Two-Proportion Z Test</h1>

    <p class="lead">
      Many studies compare success rates, approval rates, conversion rates, or other proportions between two groups.
    </p>

    <p class="lead">
      The two-proportion Z test evaluates whether two population proportions differ significantly.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/one-proportion-z-test/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/chi-square-goodness-of-fit/">
         Next: Chi-Square Goodness-of-Fit Test →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Research Question</h2>

    <p>
      Suppose a company tests two versions of a website.
    </p>

    <p>
      The goal is to determine whether the conversion rate differs between Version A and Version B.
    </p>

    <p>
      Similar questions arise in many fields:
    </p>

    <ul class="bullets">

      <li>Treatment success rates</li>

      <li>Product approval rates</li>

      <li>Election support rates</li>

      <li>Defect rates</li>

      <li>Customer retention rates</li>

    </ul>

    <h2>The Population Proportions</h2>

    <p>
      Let:
    </p>

    \[
p_1
\]

    <p>
      represent the population proportion for Group 1 and:
    </p>

    \[
p_2
\]

    <p>
      represent the population proportion for Group 2.
    </p>

    <p>
      The parameter of interest is:
    </p>

    \[
p_1-p_2
\]

    <h2>The Hypotheses</h2>

    <p>
      The standard two-sided hypotheses are:
    </p>

    \[
H_0:p_1=p_2
\]

    <br><br>

    \[
H_1:p_1\ne p_2
\]

    <p>
      Under the null hypothesis, both population proportions are equal.
    </p>

    <h2>Alternative Hypotheses</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Alternative</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>p₁ − p₂ ≠ 0</td>
            <td>Proportions differ</td>
          </tr>

          <tr>
            <td>p₁ − p₂ &gt; 0</td>
            <td>Group 1 has higher proportion</td>
          </tr>

          <tr>
            <td>p₁ − p₂ &lt; 0</td>
            <td>Group 1 has lower proportion</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Sample Proportions</h2>

    <p>
      From the two samples we compute:
    </p>

    \[
\hat p_1=\frac{x_1}{n_1}
\]

    <br><br>

    \[
\hat p_2=\frac{x_2}{n_2}
\]

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>x₁ = successes in sample 1</li>

      <li>x₂ = successes in sample 2</li>

      <li>n₁ = sample size of group 1</li>

      <li>n₂ = sample size of group 2</li>

    </ul>

    <h2>The Observed Difference</h2>

    <p>
      The observed estimate of:
    </p>

    \[
p_1-p_2
\]

    <p>
      is:
    </p>

    \[
\hat p_1-\hat p_2
\]

    <!-- Batch #70: independent-group two-proportion Z laboratory -->
<section class="concept-box" id="esa-two-proportion-lab" aria-labelledby="esa-2p-heading">
<h2 id="esa-2p-heading">Interactive Two-Proportion Z-Test Laboratory</h2>
<p>Enter independent success counts and group sample sizes. The primary test uses the <strong>pooled null proportion</strong> for H₀: p₁=p₂. The displayed 95% confidence interval uses the <strong>unpooled Wald standard error</strong> and is an approximate teaching example, not the recommended interval for sparse data.</p>
<div class="esa-2p-fields">
<label for="esa-2p-x1">Group A successes x₁ <input id="esa-2p-x1" type="number" min="0" step="1" value="120"></label>
<label for="esa-2p-n1">Group A sample size n₁ <input id="esa-2p-n1" type="number" min="1" step="1" value="200"></label>
<label for="esa-2p-x2">Group B successes x₂ <input id="esa-2p-x2" type="number" min="0" step="1" value="90"></label>
<label for="esa-2p-n2">Group B sample size n₂ <input id="esa-2p-n2" type="number" min="1" step="1" value="200"></label>
<label for="esa-2p-alternative">Alternative hypothesis
<select id="esa-2p-alternative"><option value="two-sided">Two-sided p₁ ≠ p₂</option>
<option value="greater">Group A greater p₁ &gt; p₂</option>
<option value="less">Group A less p₁ &lt; p₂</option></select></label>
</div>
<div class="esa-2p-controls"><button class="btn btn-outline" type="button" id="esa-2p-reset">Restore worked example</button>
<button class="btn btn-outline" type="button" id="esa-2p-swap">Swap group labels</button></div>
<p id="esa-2p-error" role="alert" hidden></p>
<div id="esa-2p-results" aria-live="polite" aria-atomic="true">
<div class="table-wrap"><table><caption>Two independent observed sample proportions</caption>
<thead><tr><th>Measure</th><th>Group A</th><th>Group B</th></tr></thead>
<tbody><tr><th scope="row">Observed proportion</th><td><output id="esa-2p-p1"></output></td><td><output id="esa-2p-p2"></output></td></tr></tbody>
</table></div>
<p><strong>Difference p̂₁−p̂₂:</strong> <output id="esa-2p-diff"></output>.
<strong>Pooled-null proportion:</strong> <output id="esa-2p-pooled"></output>.
<strong>Pooled-null SE:</strong> <output id="esa-2p-pooledSE"></output>.</p>
<p><strong>Z statistic:</strong> <output id="esa-2p-z"></output>.
<strong>Normal-approximation p-value:</strong> <output id="esa-2p-p"></output>.
<strong>Unpooled CI SE:</strong> <output id="esa-2p-seCI"></output>.</p>
<p><strong>Two-sided 95% unpooled Wald interval:</strong>
[<output id="esa-2p-lower"></output>, <output id="esa-2p-upperCI"></output>].</p>
<h3>Difference of proportions and 95% interval</h3>
<svg id="esa-2p-plot" viewBox="0 0 620 185" role="img" aria-label="Difference of proportions with interval and zero reference"></svg>
<p id="esa-2p-conditions"></p><p id="esa-2p-conclusion"></p><p id="esa-2p-interpretation"></p>
</div>
<p class="muted-mini">The two independent groups should be sampled appropriately; individual observations must not be paired or repeated across groups without accounting for dependence. Pooled expected success and failure counts should each be at least 10 for the conventional normal-approximation check. The uncorrected pooled Z test is not identical to an unpooled Wald confidence interval, and their conclusions can differ near the threshold. The result is approximate; no user data are stored.</p>
</section>
<style>
#esa-two-proportion-lab{max-width:100%;min-width:0;box-sizing:border-box;overflow-wrap:anywhere}
#esa-two-proportion-lab .esa-2p-fields{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:14px 0}
#esa-two-proportion-lab label{display:block;font-weight:600}
#esa-two-proportion-lab input,#esa-two-proportion-lab select{box-sizing:border-box;display:block;width:100%;min-width:0;max-width:100%;font:inherit;padding:10px;border:1px solid var(--border);border-radius:8px}
#esa-two-proportion-lab .esa-2p-controls{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
#esa-two-proportion-lab [hidden]{display:none!important}
#esa-two-proportion-lab svg{display:block;width:100%;height:auto;max-width:640px;margin:12px auto}
#esa-two-proportion-lab output{font-variant-numeric:tabular-nums}
#esa-two-proportion-lab :is(input,select,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
@media(max-width:650px){#esa-two-proportion-lab .esa-2p-fields{grid-template-columns:minmax(0,1fr)}}
@media print{#esa-two-proportion-lab .esa-2p-controls{display:none}}
</style>
<script defer src="/js/two-proportion-z-explorer.js"></script>

    <h2>Why a Pooled Proportion?</h2>

    <p>
      Under:
    </p>

    \[
H_0:p_1=p_2
\]

    <p>
      both samples are assumed to come from populations with the same proportion.
    </p>

    <p>
      Therefore, information from both samples is combined into a pooled estimate.
    </p>

    <h2>The Pooled Proportion</h2>

    \[
\hat p=\frac{x_1+x_2}{n_1+n_2}
\]

    <p>
      This pooled estimate is used for the standard uncorrected Z test of equality under the null; it is not used for the ordinary unpooled Wald confidence interval below.
    </p>

    <h2>The Standard Error Under H₀</h2>

    <p>
      Using the pooled proportion:
    </p>

    \[
\operatorname{SE}_0(\hat p_1-\hat p_2)=\sqrt{\hat p(1-\hat p)\left(\frac1{n_1}+\frac1{n_2}\right)}
\]

    <p>
      This measures expected variability when the null hypothesis is true.
    </p>

    <h2>The Test Statistic</h2>

    <p>
      The two-proportion Z statistic is:
    </p>

    \[
Z=\frac{\hat p_1-\hat p_2}{\sqrt{\hat p(1-\hat p)(1/n_1+1/n_2)}}
\]

    <p>
      Large absolute values indicate stronger evidence against:
    </p>

    \[
H_0
\]

    <h2>Worked Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>x₁ = 120</p>
      <p>n₁ = 200</p>
      <p>x₂ = 90</p>
      <p>n₂ = 200</p>

    </div>

    <h2>Compute the Sample Proportions</h2>

    \[
\hat p_1=\frac{120}{200}=0.60
\]

    <br><br>

    \[
\hat p_2=\frac{90}{200}=0.45
\]

    <p>
      Therefore:
    </p>

    \[
\hat p_1-\hat p_2=0.60-0.45=0.15
\]

    <h2>Compute the Pooled Proportion</h2>

    \[
\hat p=\frac{120+90}{200+200}=\frac{210}{400}=0.525
\]

    <h2>Compute the Standard Error</h2>

    <p>
      Substituting into the formula yields:
    </p>

    \[
\operatorname{SE}_0=\sqrt{0.525(0.475)\left(\frac1{200}+\frac1{200}\right)}\approx0.04994
\]

    <h2>Compute the Z Statistic</h2>

    \[
Z=\frac{0.15}{0.04993746\ldots}\approx3.0038
\]

    <h2>The p-Value</h2>

    <p>
      Using the standard normal distribution:
    </p>

    <div class="example-box">

      <p>
        Two-sided p-value ≈ 0.0027 (using the pooled-null Z statistic)
      </p>
    </div>

    <h2>The Decision</h2>

    <p>
      If:
    </p>

    <div class="example-box">

      <p>
        α = 0.05
      </p>
    </div>

    <p>
      then:
    </p>

    \[
0.0027<0.05
\]

    <p>
      so we reject:
    </p>

    \[
H_0
\]

    <h2>Interpretation</h2>

    <div class="example-box">

      <p>
        The data provide evidence that the population proportions differ.
      </p>
    </div>

    <h2>Conditions for the Test</h2>

    <p>
      The normal approximation requires sufficiently large counts.
    </p>

    <p>
      Using the pooled proportion:
    </p>

    <ul class="bullets">

      <li>\(n_1\hat p\ge10\)</li>

      <li>\(n_1(1-\hat p)\ge10\)</li>

      <li>\(n_2\hat p\ge10\)</li>

      <li>\(n_2(1-\hat p)\ge10\)</li>

    </ul>

    <h2>Confidence Interval Difference</h2>

    <p>
      For confidence intervals, a pooled proportion is not used.
    </p>

    <p>
      Instead, the standard error is:
    </p>

    \[
\operatorname{SE}_{\mathrm{CI}}=\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1}+\frac{\hat p_2(1-\hat p_2)}{n_2}}
\]

    <p>
      For a conventional Wald confidence interval, use \((\hat p_1-\hat p_2)\pm z_{1-\alpha/2}\operatorname{SE}_{\mathrm{CI}}\). This unpooled interval is not an exact inversion of the pooled-null test; score-based intervals for a difference in proportions can be more reliable, especially with small counts or boundary proportions. The two samples must be independent, with observations independent within each group.
    </p>

    <h2>Applications</h2>

    <div class="example-box">

      <p>
        A/B testing
      </p>

      <p>
        Clinical trials
      </p>

      <p>
        Marketing campaigns
      </p>

      <p>
        Election polling
      </p>

      <p>
        Quality improvement studies
      </p>

    </div>

    <h2>One-Proportion vs Two-Proportion Tests</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>One-Proportion Z</th>
            <th>Two-Proportion Z</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Groups compared</td>
            <td>One</td>
            <td>Two</td>
          </tr>

          <tr>
            <td>Parameter</td>
            <td>p</td>
            <td>p₁ − p₂</td>
          </tr>

          <tr>
            <td>Uses pooled estimate</td>
            <td>No</td>
            <td>Yes (for testing)</td>
          </tr>

          <tr>
            <td>Typical use</td>
            <td>Compare to claimed proportion</td>
            <td>Compare two groups</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      The two-proportion Z test extends hypothesis testing for proportions to comparisons between groups.
    </p>

    <p>
      It is one of the most important tools in modern experimentation, particularly in medicine, business analytics, and online experimentation.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The two-proportion Z test evaluates whether two population proportions differ. It compares the observed difference in sample proportions to the variability expected under the assumption that the population proportions are equal.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Many categorical-data problems involve more than two categories rather than simple success-failure outcomes.
    </p>

    <p>
      In such situations, chi-square methods become the standard inferential tools.
    </p>

    <p>
      The next lesson introduces the chi-square goodness-of-fit test.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The two-proportion Z test compares two population proportions</li>

        <li>The parameter of interest is p₁ − p₂</li>

        <li>The null hypothesis usually states p₁ = p₂</li>

        <li>A pooled proportion is used when computing the test statistic</li>

        <li>The test statistic follows an approximate standard normal distribution</li>

        <li>Large samples are required for the normal approximation</li>

        <li>The procedure is central to A/B testing and comparative studies</li>

        <li>Confidence intervals use a different standard error than hypothesis tests</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/one-proportion-z-test/">
         ← Previous: One-Proportion Z Test
      </a>

      <a class="btn"
         href="/inference/classical-tests/chi-square-goodness-of-fit/">
         Next: Chi-Square Goodness-of-Fit Test →
      </a>

    </div>

  </div>

</section>