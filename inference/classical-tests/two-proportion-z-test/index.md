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

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/two-proportion-z-test/",
    label: "Two-Proportion Z Test",
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

    0

    <p>
      represent the population proportion for Group 1 and:
    </p>

    1

    <p>
      represent the population proportion for Group 2.
    </p>

    <p>
      The parameter of interest is:
    </p>

    2

    <h2>The Hypotheses</h2>

    <p>
      The standard two-sided hypotheses are:
    </p>

    3

    <br><br>

    4

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

    5

    <br><br>

    6

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

    7

    <p>
      is:
    </p>

    8

    <h2>Why a Pooled Proportion?</h2>

    <p>
      Under:
    </p>

    9

    <p>
      both samples are assumed to come from populations with the same proportion.
    </p>

    <p>
      Therefore, information from both samples is combined into a pooled estimate.
    </p>

    <h2>The Pooled Proportion</h2>

    10

    <p>
      This pooled estimate is used only for hypothesis testing.
    </p>

    <h2>The Standard Error Under H₀</h2>

    <p>
      Using the pooled proportion:
    </p>

    11

    <p>
      This measures expected variability when the null hypothesis is true.
    </p>

    <h2>The Test Statistic</h2>

    <p>
      The two-proportion Z statistic is:
    </p>

    12

    <p>
      Large absolute values indicate stronger evidence against:
    </p>

    13

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

    14

    <br><br>

    15

    <p>
      Therefore:
    </p>

    16

    <h2>Compute the Pooled Proportion</h2>

    17

    <h2>Compute the Standard Error</h2>

    <p>
      Substituting into the formula yields:
    </p>

    18

    <h2>Compute the Z Statistic</h2>

    19

    <h2>The p-Value</h2>

    <p>
      Using the standard normal distribution:
    </p>

    <div class="example-box">

      <p>
        Two-sided p-value ≈ 0.003
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

    20

    <p>
      so we reject:
    </p>

    21

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

      <li>n₁p̂ ≥ 10</li>

      <li>n₁(1−p̂) ≥ 10</li>

      <li>n₂p̂ ≥ 10</li>

      <li>n₂(1−p̂) ≥ 10</li>

    </ul>

    <h2>Confidence Interval Difference</h2>

    <p>
      For confidence intervals, a pooled proportion is not used.
    </p>

    <p>
      Instead, the standard error is:
    </p>

    22

    <p>
      This distinction is important.
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