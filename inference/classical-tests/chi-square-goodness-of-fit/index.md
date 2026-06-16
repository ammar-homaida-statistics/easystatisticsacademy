---
layout: default
title: Chi-Square Goodness-of-Fit Test
description: Learn how the chi-square goodness-of-fit test evaluates whether observed categorical data match an expected distribution.
permalink: /inference/classical-tests/chi-square-goodness-of-fit/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/chi-square-goodness-of-fit/",
    label: "Chi-Square Goodness-of-Fit Test",
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
      <span class="badge">Categorical Data</span>
    </div>

    <h1>Chi-Square Goodness-of-Fit Test</h1>

    <p class="lead">
      Many statistical questions involve determining whether observed categorical data match an expected pattern.
    </p>

    <p class="lead">
      The chi-square goodness-of-fit test evaluates whether observed category frequencies are consistent with a specified distribution.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/two-proportion-z-test/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/chi-square-independence-test/">
         Next: Chi-Square Test of Independence →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Research Question</h2>

    <p>
      Suppose a six-sided die is rolled many times.
    </p>

    <p>
      We might ask:
    </p>

    <div class="example-box">

      <p>
        Are the outcomes consistent with a fair die?
      </p>
    </div>

    <p>
      Or suppose a company expects customer preferences to be distributed across several product categories in known proportions.
    </p>

    <p>
      We may ask:
    </p>

    <div class="example-box">

      <p>
        Do the observed preferences match the expected distribution?
      </p>
    </div>

    <p>
      These are goodness-of-fit problems.
    </p>

    <h2>What Does "Goodness of Fit" Mean?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A goodness-of-fit test evaluates how well observed frequencies agree with frequencies predicted by a hypothesized distribution.
      </p>

    </div>

    <p>
      The goal is to determine whether differences between observed and expected counts are larger than would be expected from random sampling alone.
    </p>

    <h2>Observed and Expected Counts</h2>

    <p>
      Every goodness-of-fit test compares:
    </p>

    <ul class="bullets">

      <li>Observed counts</li>

      <li>Expected counts</li>

    </ul>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Category</th>
            <th>Observed</th>
            <th>Expected</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>A</td>
            <td>O₁</td>
            <td>E₁</td>
          </tr>

          <tr>
            <td>B</td>
            <td>O₂</td>
            <td>E₂</td>
          </tr>

          <tr>
            <td>...</td>
            <td>...</td>
            <td>...</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Hypotheses</h2>

    <p>
      The null hypothesis states that the population follows the specified distribution.
    </p>

    <div class="example-box">

      <p>
        H₀: The category probabilities match the hypothesized values.
      </p>
    </div>

    <p>
      The alternative hypothesis states:
    </p>

    <div class="example-box">

      <p>
        Hₐ: The distribution differs from the hypothesized distribution.
      </p>
    </div>

    <h2>Example: Fair Die</h2>

    <p>
      For a fair six-sided die:
    </p>

    <p>
      Each face should occur with probability:
    </p>

    0

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        H₀: p₁ = p₂ = p₃ = p₄ = p₅ = p₆ = 1/6
      </p>
    </div>

    <h2>Computing Expected Counts</h2>

    <p>
      Expected counts are obtained from:
    </p>

    1

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>n = total sample size</li>

      <li>pᵢ = hypothesized probability for category i</li>

    </ul>

    <h2>Example Expected Counts</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        n = 120 die rolls
      </p>
    </div>

    <p>
      Then for each face:
    </p>

    2

    <p>
      Every category has an expected count of 20.
    </p>

    <h2>The Chi-Square Statistic</h2>

    <p>
      The goodness-of-fit test statistic is:
    </p>

    3

    <p>
      This formula measures total discrepancy between observed and expected counts.
    </p>

    <h2>Understanding the Formula</h2>

    <p>
      For each category:
    </p>

    <ul class="bullets">

      <li>Compute the difference between observed and expected counts</li>

      <li>Square the difference</li>

      <li>Scale by the expected count</li>

      <li>Add contributions across categories</li>

    </ul>

    <p>
      Larger discrepancies produce larger chi-square values.
    </p>

    <h2>Interpreting χ²</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>χ² Value</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Small</td>
            <td>Observed counts close to expected counts</td>
          </tr>

          <tr>
            <td>Large</td>
            <td>Observed counts differ substantially from expectations</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Example Calculation</h2>

    <p>
      Suppose a die is rolled 60 times.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Face</th>
            <th>Observed</th>
            <th>Expected</th>
          </tr>
        </thead>

        <tbody>

          <tr><td>1</td><td>8</td><td>10</td></tr>
          <tr><td>2</td><td>11</td><td>10</td></tr>
          <tr><td>3</td><td>9</td><td>10</td></tr>
          <tr><td>4</td><td>13</td><td>10</td></tr>
          <tr><td>5</td><td>10</td><td>10</td></tr>
          <tr><td>6</td><td>9</td><td>10</td></tr>

        </tbody>

      </table>

    </div>

    <p>
      The chi-square statistic summarizes the overall discrepancy across all categories.
    </p>

    <h2>The Chi-Square Distribution</h2>

    <p>
      Under:
    </p>

    4

    <p>
      the test statistic follows a chi-square distribution approximately.
    </p>

    <p>
      This distribution is:
    </p>

    <ul class="bullets">

      <li>Always positive</li>

      <li>Right-skewed</li>

      <li>Defined by degrees of freedom</li>

    </ul>

    <h2>Degrees of Freedom</h2>

    <p>
      For a goodness-of-fit test:
    </p>

    5

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>k = number of categories</li>

    </ul>

    <h2>Example Degrees of Freedom</h2>

    <p>
      For a six-sided die:
    </p>

    6

    <h2>The p-Value</h2>

    <p>
      Once:
    </p>

    7

    <p>
      and degrees of freedom are known, the p-value is obtained from the chi-square distribution.
    </p>

    <p>
      Large χ² values correspond to small p-values.
    </p>

    <h2>Decision Rule</h2>

    <div class="concept-box">

      <strong>Decision Rule:</strong>

      <p>
        Reject H₀ if p ≤ α.
      </p>

      <p>
        Fail to reject H₀ if p > α.
      </p>

    </div>

    <h2>Assumptions</h2>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Independent observations</li>

      <li>Categorical outcomes</li>

      <li>Expected counts sufficiently large</li>

    </ul>

    <h2>Expected Count Rule</h2>

    <p>
      A common guideline is:
    </p>

    <div class="example-box">

      <p>
        Every expected count should be at least 5.
      </p>
    </div>

    <p>
      This helps justify the chi-square approximation.
    </p>

    <h2>Common Applications</h2>

    <div class="example-box">

      <p>
        Testing fairness of dice or random generators
      </p>

      <p>
        Genetics and inheritance studies
      </p>

      <p>
        Market-share distributions
      </p>

      <p>
        Consumer preference categories
      </p>

      <p>
        Quality-control classification data
      </p>

    </div>

    <h2>Goodness-of-Fit vs Proportion Tests</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Proportion Tests</th>
            <th>Goodness-of-Fit Test</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Categories</td>
            <td>Usually 2</td>
            <td>2 or More</td>
          </tr>

          <tr>
            <td>Parameter</td>
            <td>Proportion(s)</td>
            <td>Entire distribution</td>
          </tr>

          <tr>
            <td>Data Type</td>
            <td>Binary</td>
            <td>Categorical</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      The chi-square goodness-of-fit test broadens statistical inference from binary outcomes to general categorical distributions.
    </p>

    <p>
      Instead of comparing means or proportions, it evaluates whether an entire pattern of observed frequencies matches theoretical expectations.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The chi-square goodness-of-fit test evaluates whether observed categorical frequencies match a hypothesized distribution. It measures discrepancies between observed and expected counts using the chi-square statistic and determines whether those discrepancies are larger than expected by chance.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Goodness-of-fit tests compare observed counts to a known distribution.
    </p>

    <p>
      Another important question is whether two categorical variables are related.
    </p>

    <p>
      The next lesson introduces the chi-square test of independence, which evaluates relationships between categorical variables.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The goodness-of-fit test compares observed and expected frequencies</li>

        <li>The null hypothesis specifies a categorical distribution</li>

        <li>Expected counts are computed as n × pᵢ</li>

        <li>The chi-square statistic measures overall discrepancy</li>

        <li>Large χ² values indicate stronger evidence against H₀</li>

        <li>Degrees of freedom equal k − 1</li>

        <li>Expected counts should generally be at least 5</li>

        <li>The test evaluates entire categorical distributions rather than single proportions</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/two-proportion-z-test/">
         ← Previous: Two-Proportion Z Test
      </a>

      <a class="btn"
         href="/inference/classical-tests/chi-square-independence-test/">
         Next: Chi-Square Test of Independence →
      </a>

    </div>

  </div>

</section>