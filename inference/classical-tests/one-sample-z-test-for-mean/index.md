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

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/one-sample-z-test-for-mean/",
    label: "One-Sample Z Test for a Mean",
    ts: Date.now()
  }));

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

    0

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

    1

    <br><br>

    2

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

    3

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

    4

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

    5

    <p>
      gives:
    </p>

    6

    <h2>Step 2: Compute the Test Statistic</h2>

    <p>
      Substitute into the formula:
    </p>

    7

    <p>
      Therefore:
    </p>

    8

    <h2>Step 3: Compute the p-Value</h2>

    <p>
      Under:
    </p>

    9

    <p>
      the statistic follows the standard normal distribution.
    </p>

    <p>
      For a two-sided test:
    </p>

    <div class="example-box">

      <p>
        p-value &lt; 0.001
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
        p &lt; 0.001
      </p>

      <p>
        α = 0.05
      </p>

    </div>

    <p>
      Since:
    </p>

    10

    <p>
      we reject:
    </p>

    11

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

    12

    <p>
      and a two-sided test:
    </p>

    13

    <p>
      Since:
    </p>

    14

    <p>
      the statistic falls inside the rejection region.
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

    15

    <p>
      is usually unknown.
    </p>

    <p>
      Instead,
      researchers estimate variability using the sample standard deviation:
    </p>

    16

    <p>
      This leads to the one-sample t test,
      which is far more common.
    </p>

    <h2>Z Test and Confidence Intervals</h2>

    <p>
      The corresponding confidence interval is:
    </p>

    17

    <p>
      As discussed previously,
      the confidence interval and hypothesis test produce equivalent conclusions at matching confidence levels and significance levels.
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