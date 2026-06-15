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

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/one-proportion-z-test/",
    label: "One-Proportion Z Test",
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

    0

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

    1

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

    2

    <br><br>

    3

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

    4

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

    5

    <h2>The Standard Error Under H₀</h2>

    <p>
      Under the null hypothesis:
    </p>

    6

    <p>
      the standard error becomes:
    </p>

    7

    <p>
      Notice that the null value:
    </p>

    8

    <p>
      appears in the formula.
    </p>

    <h2>The Z Statistic</h2>

    <p>
      The one-proportion Z statistic is:
    </p>

    9

    <p>
      This measures how many standard errors separate the observed sample proportion from the null value.
    </p>

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

    10

    <h2>Compute the Standard Error</h2>

    <p>
      Using:
    </p>

    11

    <p>
      gives:
    </p>

    12

    <h2>Compute the Test Statistic</h2>

    <p>
      Therefore:
    </p>

    13

    <p>
      which gives approximately:
    </p>

    14

    <h2>The p-Value</h2>

    <p>
      Under:
    </p>

    15

    <p>
      the statistic follows the standard normal distribution approximately.
    </p>

    <p>
      For a two-sided test:
    </p>

    <div class="example-box">

      <p>
        p-value ≈ 0.0046
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

    16

    <p>
      we reject:
    </p>

    17

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

    18

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

    19

    <p>
      and:
    </p>

    20

    <p>
      under the null hypothesis.
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

    21

    <p>
      As with other classical procedures,
      confidence intervals and hypothesis tests provide matching conclusions at corresponding confidence levels.
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