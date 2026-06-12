---
layout: default
title: Test Statistic and Standardization
description: Learn what a test statistic is, why standardization is essential in hypothesis testing, and how observed results are converted into evidence.
permalink: /inference/hypothesis-testing/test-statistic-standardization/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_hypothesis_testing_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/hypothesis-testing/test-statistic-standardization/",
    label: "Test Statistic and Standardization",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 3</span>
      <span class="badge">Hypothesis Testing</span>
      <span class="badge">Core Mechanics</span>
    </div>

    <h1>Test Statistic and Standardization</h1>

    <p class="lead">
      Once hypotheses are defined, we need a way to measure how far the observed data depart from the null hypothesis.
    </p>

    <p class="lead">
      Test statistics provide that measurement by converting observed differences into standardized units that can be evaluated using probability models.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/hypothesis-testing/null-and-alternative/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/p-value-meaning/">
         Next: p-Value Meaning →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Problem We Need to Solve</h2>

    <p>
      Suppose a manufacturer claims:
    </p>

    0

    <p>
      and a sample produces:
    </p>

    1

    <p>
      The sample mean differs from the claimed value by:
    </p>

    2

    <p>
      Is a difference of 8 large?
    </p>

    <p>
      The answer depends on the amount of natural variability in the sampling process.
    </p>

    <h2>Why Raw Differences Are Not Enough</h2>

    <p>
      A difference of 8 units may be:
    </p>

    <ul class="bullets">

      <li>Huge in one situation</li>

      <li>Tiny in another</li>

    </ul>

    <p>
      The interpretation depends on how much random variation is expected.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Evidence is determined not by the size of a difference alone, but by its size relative to expected sampling variability.
      </p>

    </div>

    <h2>The Need for Standardization</h2>

    <p>
      To evaluate evidence fairly,
      we compare the observed difference to the amount of variation expected under the null hypothesis.
    </p>

    <p>
      This process is called standardization.
    </p>

    <h2>The General Formula</h2>

    <p>
      Most test statistics have the form:
    </p>

    3

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>Observed = estimate from the sample</li>

      <li>Expected = value predicted by the null hypothesis</li>

      <li>SE = standard error</li>

    </ul>

    <h2>Interpreting the Formula</h2>

    <p>
      The numerator measures departure from the null hypothesis.
    </p>

    <p>
      The denominator measures expected random variability.
    </p>

    <p>
      Together they tell us:
    </p>

    <div class="example-box">

      <p>
        How many standard errors away from the null expectation the observation lies.
      </p>

    </div>

    <h2>The z Statistic</h2>

    <p>
      When population variability is known,
      a common test statistic is:
    </p>

    4

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>x̄ = observed sample mean</li>

      <li>μ₀ = null-hypothesis value</li>

      <li>SE = standard error</li>

    </ul>

    <h2>An Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Sample mean = 492
      </p>

      <p>
        Null value = 500
      </p>

      <p>
        Standard error = 2
      </p>

    </div>

    <p>
      Then:
    </p>

    5

    <p>
      The observed mean is four standard errors below the null expectation.
    </p>

    <h2>Why Standard Errors Matter</h2>

    <p>
      Consider the same observed difference:
    </p>

    6

    <p>
      but now suppose:
    </p>

    <div class="example-box">

      <p>
        SE = 20
      </p>

    </div>

    <p>
      Then:
    </p>

    7

    <p>
      Suddenly the same difference appears quite ordinary.
    </p>

    <p>
      The evidence changes because the expected variability changed.
    </p>

    <h2>Large vs Small Test Statistics</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Statistic Magnitude</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Near 0</td>
            <td>Data consistent with H₀</td>
          </tr>

          <tr>
            <td>Moderate</td>
            <td>Some departure from H₀</td>
          </tr>

          <tr>
            <td>Large absolute value</td>
            <td>Strong departure from H₀</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Direction Matters Too</h2>

    <p>
      Test statistics contain information about direction.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Value</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Positive</td>
            <td>Observed value exceeds null expectation</td>
          </tr>

          <tr>
            <td>Negative</td>
            <td>Observed value falls below null expectation</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The sign becomes especially important for one-sided tests.
    </p>

    <h2>The t Statistic</h2>

    <p>
      When population variability is unknown,
      statisticians replace σ with the sample standard deviation.
    </p>

    <p>
      This produces the t statistic:
    </p>

    8

    <p>
      The logic remains identical.
    </p>

    <p>
      Only the probability distribution changes.
    </p>

    <h2>A Universal Idea</h2>

    <p>
      Nearly every classical test statistic follows the same blueprint:
    </p>

    9

    <p>
      This pattern appears throughout statistics.
    </p>

    <h2>Why Standardization Is Powerful</h2>

    <p>
      Raw measurements may use different units:
    </p>

    <ul class="bullets">

      <li>Points</li>

      <li>Dollars</li>

      <li>Milliliters</li>

      <li>Percentages</li>

    </ul>

    <p>
      Standardization converts them into a common scale measured in standard errors.
    </p>

    <p>
      This allows probability calculations to be performed consistently.
    </p>

    <h2>The Sampling Distribution Connection</h2>

    <p>
      Under the null hypothesis,
      the test statistic has a known sampling distribution.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Standard normal distribution</li>

      <li>t distribution</li>

      <li>Chi-square distribution</li>

      <li>F distribution</li>

    </ul>

    <p>
      These distributions determine how unusual the observed statistic is.
    </p>

    <h2>What Counts as Unusual?</h2>

    <p>
      A test statistic near the center of its distribution is unsurprising.
    </p>

    <p>
      A statistic far into the tails is unusual under the null hypothesis.
    </p>

    <p>
      The more unusual the statistic,
      the stronger the evidence against the null.
    </p>

    <h2>The Missing Piece</h2>

    <p>
      We now know how to quantify departure from the null hypothesis.
    </p>

    <p>
      But we still need a way to convert that departure into a probability statement.
    </p>

    <p>
      That probability is called the p-value.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A test statistic standardizes the difference between observed data and the null hypothesis by expressing that difference in units of standard error. Larger absolute test statistics indicate stronger evidence against the null hypothesis.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Once a test statistic is computed,
      statisticians evaluate how unusual it would be if the null hypothesis were true.
    </p>

    <p>
      The probability of observing evidence at least this extreme is called the p-value.
    </p>

    <p>
      The next lesson introduces p-values, one of the most important—and most misunderstood—concepts in statistics.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Raw differences must be evaluated relative to expected variability</li>

        <li>Standardization converts differences into standard-error units</li>

        <li>Most test statistics follow (Observed − Expected)/SE</li>

        <li>Large absolute statistics indicate stronger departures from H₀</li>

        <li>The sign indicates the direction of departure</li>

        <li>z and t statistics are common examples</li>

        <li>Standardization allows probability calculations across different scales</li>

        <li>Test statistics are the bridge between data and p-values</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/hypothesis-testing/null-and-alternative/">
         ← Previous: Null and Alternative Hypotheses
      </a>

      <a class="btn"
         href="/inference/hypothesis-testing/p-value-meaning/">
         Next: p-Value Meaning →
      </a>

    </div>

  </div>

</section>