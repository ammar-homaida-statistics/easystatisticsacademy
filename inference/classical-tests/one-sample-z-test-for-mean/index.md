---
layout: default
title: One-Sample Z Test for a Mean
description: Learn how the one-sample Z test evaluates whether a population mean differs from a hypothesized value when the population standard deviation is known.
permalink: /inference/classical-tests/one-sample-z-test-for-mean/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/one-sample-z-test-for-mean/",
    label: "One-Sample Z Test for a Mean",
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
      <span class="badge">Z Test</span>
    </div>

    <h1>One-Sample Z Test for a Mean</h1>

    <p class="lead">
      The one-sample Z test evaluates whether a population mean differs from a hypothesized value when the population standard deviation is known.
    </p>

    <p class="lead">
      Although this situation is uncommon in practice, the Z test provides the foundation for understanding many other hypothesis-testing procedures.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/decision-framework-and-assumptions/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/one-sample-t-test-for-mean/">
         Next: One-Sample t Test for a Mean →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Research Question</h2>

    <p>
      Suppose a manufacturer claims that bottles contain an average of:
    </p>

    \[
\mu_0=500\ \text{mL}
\]

    <p>
      A quality-control analyst collects a sample and wants to determine whether the true population mean differs from that value.
    </p>

    <p>
      This is a one-sample mean-testing problem.
    </p>

    <h2>When Is a Z Test Appropriate?</h2>

    <div class="concept-box">

      <strong>Use a one-sample Z test when:</strong>

      <ul class="bullets">
        <li>The parameter of interest is a population mean.</li>
        <li>A single sample is observed.</li>
        <li>The population standard deviation is known.</li>
        <li>Observations are independent.</li>
        <li>The population is normal or the sample size is sufficiently large.</li>
      </ul>

    </div>

    <p>
      The known population standard deviation requirement is the key feature that distinguishes the Z test from the t test.
    </p>

    <h2>The Hypotheses</h2>

    <p>
      A typical two-sided test is:
    </p>

    \[
H_0:\mu=\mu_0
\]

    <br><br>

    \[
H_1:\mu\ne\mu_0
\]

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>μ = population mean</li>

      <li>μ₀ = hypothesized value</li>

    </ul>

    <h2>Possible Alternative Hypotheses</h2>

    <p>
      Depending on the research question:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Alternative</th>
            <th>Test Type</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>μ ≠ μ₀</td>
            <td>Two-sided</td>
          </tr>

          <tr>
            <td>μ &gt; μ₀</td>
            <td>Right-tailed</td>
          </tr>

          <tr>
            <td>μ &lt; μ₀</td>
            <td>Left-tailed</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Standard Error</h2>

    <p>
      Because the population standard deviation is assumed known:
    </p>

    \[
\operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt{n}}
\]

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>σ = population standard deviation</li>

      <li>n = sample size</li>

    </ul>

    <h2>The Test Statistic</h2>

    <p>
      The Z statistic standardizes the difference between the sample mean and the null value.
    </p>

    \[
Z=\frac{\bar X-\mu_0}{\sigma/\sqrt{n}}
\]

    <p>
      This tells us how many standard errors the sample mean lies from the null hypothesis.
    </p>

    <h2>Interpreting the Z Statistic</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>z Value</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Near 0</td>
            <td>Consistent with H₀</td>
          </tr>

          <tr>
            <td>Moderate</td>
            <td>Some departure from H₀</td>
          </tr>

          <tr>
            <td>Large |z|</td>
            <td>Strong departure from H₀</td>
          </tr>

        </tbody>

      </table>

    </div>

    <!-- Batch #73: Known-population-sigma interactive Z inference -->
<section class="concept-box" id="esa-one-mean-z-lab" aria-labelledby="esa-omz-heading">
<h2 id="esa-omz-heading">Interactive One-Sample Z-Test for a Mean</h2>
<p>Use the <strong>known population standard deviation σ</strong> (not the sample standard deviation) to evaluate hypotheses about a population mean. The standard normal CDF is used for p-values, and the two-sided 95% confidence interval uses z=1.9599639845.</p>
<div class="esa-omz-grid">
<div><label for="esa-omz-n">Sample size n</label><input id="esa-omz-n" type="number" min="1" max="1000000" step="1" value="100"></div>
<div><label for="esa-omz-mean">Sample mean x̄</label><input id="esa-omz-mean" type="number" step="any" value="492"></div>
<div><label for="esa-omz-sigma">Known population standard deviation σ</label><input id="esa-omz-sigma" type="number" min="0" step="any" value="20"></div>
<div><label for="esa-omz-mu0">Hypothesized population mean μ₀</label><input id="esa-omz-mu0" type="number" step="any" value="500"></div>
<div><label for="esa-omz-side">Alternative hypothesis</label><select id="esa-omz-side">
<option value="two-sided">Two-sided μ ≠ μ₀</option>
<option value="greater">Greater μ &gt; μ₀</option>
<option value="less">Less μ &lt; μ₀</option></select></div>
</div>
<button type="button" class="btn btn-outline" id="esa-omz-reset">Restore worked example</button>
<p id="esa-omz-error" role="alert" hidden></p>
<section id="esa-omz-results" aria-live="polite" aria-label="One-sample Z inference results">
<div class="table-wrap"><table><caption>Z statistics and two-sided 95% confidence interval (six decimals)</caption><tbody>
<tr><th scope="row">Standard error σ/√n</th><td id="esa-omz-se">—</td></tr>
<tr><th scope="row">Z statistic (x̄−μ₀)/(σ/√n)</th><td id="esa-omz-z">—</td></tr>
<tr><th scope="row">Normal p-value for chosen alternative</th><td id="esa-omz-pvalue">—</td></tr>
<tr><th scope="row">95% CI lower bound</th><td id="esa-omz-lower">—</td></tr>
<tr><th scope="row">95% CI upper bound</th><td id="esa-omz-upper">—</td></tr>
</tbody></table></div>
<svg id="esa-omz-plot" role="img" viewBox="0 0 620 235" aria-label="Standard normal density and selected Z tail probability" style="display:block;width:100%;height:auto;max-width:100%"></svg>
<p id="esa-omz-decision"></p>
<p id="esa-omz-assumptions"></p>
<p id="esa-omz-interpretation"></p>
</section>
<p class="muted-mini">The Z distribution is exact for independent observations from a normal population with known σ. Otherwise, it may be approximate under sufficient CLT conditions. If σ must be estimated, use the <a href="/inference/classical-tests/one-sample-t-test-for-mean/">one-sample Student t-test</a>. The interval is for a population mean, not for a single future observation. No inputs are stored.</p>
</section>
<style>
#esa-one-mean-z-lab,#esa-one-mean-z-lab *{box-sizing:border-box}
#esa-one-mean-z-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-one-mean-z-lab .esa-omz-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,215px),1fr));gap:12px;margin:14px 0}
#esa-one-mean-z-lab label{display:block;font-weight:650;margin-bottom:6px}
#esa-one-mean-z-lab :is(input,select){display:block;width:100%;min-width:0;padding:10px;border:1px solid #777;border-radius:7px;font:inherit}
#esa-one-mean-z-lab [hidden]{display:none!important}
#esa-one-mean-z-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-one-mean-z-lab td{font-variant-numeric:tabular-nums}
#esa-one-mean-z-lab :is(input,select,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
@media(max-width:650px){#esa-one-mean-z-lab .esa-omz-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/one-mean-z-explorer.js"></script>
<h2>Example Setup</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>μ₀ = 500</p>
      <p>x̄ = 492</p>
      <p>σ = 20</p>
      <p>n = 100</p>
      <p>α = 0.05</p>

    </div>

    <h2>Step 1: Compute the Standard Error</h2>

    <p>
      Using:
    </p>

    \[
\operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt{n}}
\]

    <p>
      gives:
    </p>

    \[
\operatorname{SE}(\bar X)=\frac{20}{\sqrt{100}}=2\ \text{mL}
\]

    <h2>Step 2: Compute the Test Statistic</h2>

    <p>
      Substitute into the formula:
    </p>

    \[
Z=\frac{492-500}{20/\sqrt{100}}=\frac{-8}{2}
\]

    <p>
      Therefore:
    </p>

    \[
Z=-4
\]

    <h2>Step 3: Compute the p-Value</h2>

    <p>
      Under:
    </p>

    \[
H_0:\mu=500\ \text{mL}
\]

    <p>
      the statistic follows a standard normal distribution exactly for independent observations from a normal population (with known σ), or approximately for an adequately large independent sample under suitable Central Limit Theorem conditions.
    </p>

    <p>
      For a two-sided test:
    </p>

    <div class="example-box">

      <p>
        two-sided p-value ≈ 0.0000633 (&lt; 0.001)
      </p>
    </div>

    <p>
      This outcome would be extremely unusual if the null hypothesis were true.
    </p>

    <h2>Step 4: Make the Decision</h2>

    <p>
      Compare:
    </p>

    <div class="example-box">

      <p>
        p ≈ 0.0000633
      </p>

      <p>
        α = 0.05
      </p>

    </div>

    <p>
      Since:
    </p>

    \[
p\approx0.0000633<\alpha=0.05
\]

    <p>
      we reject:
    </p>

    \[
H_0
\]

    <h2>Step 5: Interpret the Result</h2>

    <p>
      Statistical conclusion:
    </p>

    <div class="example-box">

      <p>
        Reject the null hypothesis.
      </p>
    </div>

    <p>
      Practical conclusion:
    </p>

    <div class="example-box">

      <p>
        The data provide strong evidence that the population mean differs from 500 mL.
      </p>
    </div>

    <h2>Critical-Value Approach</h2>

    <p>
      Historically,
      hypothesis tests were often performed using critical values instead of p-values.
    </p>

    <p>
      For:
    </p>

    \[
\alpha=0.05
\]

    <p>
      and a two-sided test:
    </p>

    \[
z_{1-\alpha/2}=z_{0.975}\approx1.96
\]

    <p>
      Since:
    </p>

    \[
|Z|=4>1.96
\]

    <p>
      the statistic falls in the rejection region (outside the interval from −1.96 to +1.96).
    </p>

    <p>
      The same conclusion is reached.
    </p>

    <h2>The Assumptions Revisited</h2>

    <p>
      The Z test relies on:
    </p>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Independent observations</li>

      <li>Known population standard deviation</li>

      <li>Normal population or sufficiently large sample size</li>

    </ul>

    <h2>Why the Z Test Is Rare in Practice</h2>

    <p>
      In real applications,
      the population standard deviation:
    </p>

    \[
\sigma
\]

    <p>
      is usually unknown.
    </p>

    <p>
      Instead,
      researchers estimate variability using the sample standard deviation:
    </p>

    \[
s
\]

    <p>
      This leads to the one-sample t test,
      which is far more common.
    </p>

    <h2>Z Test and Confidence Intervals</h2>

    <p>
      The corresponding confidence interval is:
    </p>

    \[
\bar X\pm z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}
\]

    <p>
      As discussed previously,
      the two-sided Z test and this corresponding normal-theory interval give equivalent decisions at matching confidence levels and significance levels, under the same known-σ assumptions. In the example, the 95% interval is 492 ± 1.96 × 2 = [488.08, 495.92] mL; it excludes 500 mL.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      The one-sample Z test illustrates the fundamental structure of hypothesis testing.
    </p>

    <p>
      It combines hypotheses, standard errors, standardization, sampling distributions, p-values, and decision rules into a single inferential procedure.
    </p>

    <p>
      Most later tests follow exactly the same logic.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The one-sample Z test evaluates whether a population mean differs from a hypothesized value when the population standard deviation is known. It uses the standard normal distribution to measure how unusual the observed sample mean would be under the null hypothesis.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      In practice,
      population variability is rarely known.
    </p>

    <p>
      Statisticians therefore replace the known standard deviation with an estimate from the sample.
    </p>

    <p>
      This modification leads to the one-sample t test, one of the most important procedures in classical inference.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The one-sample Z test evaluates a population mean using a single sample</li>

        <li>The population standard deviation must be known</li>

        <li>The standard error is σ/√n</li>

        <li>The test statistic is z = (x̄ − μ₀)/(σ/√n)</li>

        <li>The standard normal distribution provides p-values</li>

        <li>Decisions are made by comparing p-values to α</li>

        <li>The Z test and corresponding confidence interval are closely connected</li>

        <li>The one-sample t test is usually preferred when σ is unknown</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/decision-framework-and-assumptions/">
         ← Previous: Decision Framework and Assumptions
      </a>

      <a class="btn"
         href="/inference/classical-tests/one-sample-t-test-for-mean/">
         Next: One-Sample t Test for a Mean →
      </a>

    </div>

  </div>

</section>