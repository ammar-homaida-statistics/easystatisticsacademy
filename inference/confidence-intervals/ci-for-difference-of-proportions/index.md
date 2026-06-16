---
layout: default
title: Confidence Interval for Difference of Proportions
description: Learn how to construct and interpret confidence intervals for the difference between two population proportions.
permalink: /inference/confidence-intervals/ci-for-difference-of-proportions/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_confidence_intervals_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/ci-for-difference-of-proportions/",
    label: "Confidence Interval for Difference of Proportions",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 2</span>
      <span class="badge">Confidence Intervals</span>
      <span class="badge">Comparing Percentages</span>
    </div>

    <h1>Confidence Interval for Difference of Proportions</h1>

    <p class="lead">
      Many important statistical questions compare percentages between two groups.
    </p>

    <p class="lead">
      Confidence intervals for differences in proportions help estimate how much two population proportions differ while accounting for sampling uncertainty.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-paired-mean-difference/">
         Next: CI for Paired Mean Difference →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Research Question</h2>

    <p>
      Instead of comparing averages,
      we now compare proportions.
    </p>

    <div class="example-box">

      <p>
        Approval rates for two political candidates
      </p>

      <p>
        Conversion rates for two website designs
      </p>

      <p>
        Recovery rates for two medical treatments
      </p>

      <p>
        Defect rates from two manufacturing processes
      </p>

    </div>

    <p>
      The goal is to estimate how different the population proportions are.
    </p>

    <h2>The Parameter of Interest</h2>

    <p>
      Let:
    </p>

    <ul class="bullets">

      <li>p₁ = population proportion for Group 1</li>

      <li>p₂ = population proportion for Group 2</li>

    </ul>

    <p>
      The parameter of interest is:
    </p>

    0

    <p>
      which represents the true difference between the two population proportions.
    </p>

    <h2>The Estimator</h2>

    <p>
      We estimate the population difference using:
    </p>

    1

    <p>
      where each sample proportion is calculated separately from its own sample.
    </p>

    <h2>Interpreting the Difference</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Difference</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Positive</td>
            <td>Group 1 has the larger proportion</td>
          </tr>

          <tr>
            <td>Negative</td>
            <td>Group 2 has the larger proportion</td>
          </tr>

          <tr>
            <td>Zero</td>
            <td>No population proportion difference</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Confidence Interval Blueprint</h2>

    <p>
      Once again:
    </p>

    2

    <p>
      The estimate becomes:
    </p>

    3

    <p>
      and the margin of error is based on the standard error of the difference.
    </p>

    <h2>The Standard Error</h2>

    <p>
      For independent samples:
    </p>

    4

    <p>
      This combines uncertainty from both sample proportions.
    </p>

    <h2>The Confidence Interval Formula</h2>

    <p>
      The standard confidence interval becomes:
    </p>

    5

    <p>
      This is the most common confidence interval for differences between two population proportions.
    </p>

    <h2>Why z Critical Values Are Used</h2>

    <p>
      The sampling distribution of the difference in sample proportions is approximately normal when sample sizes are sufficiently large.
    </p>

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        z critical values are used rather than t critical values.
      </p>

    </div>

    <h2>Example Setup</h2>

    <p>
      Suppose an A/B test compares two website versions.
    </p>

    <div class="example-box">

      <p>
        Version A: 240 conversions out of 600 visitors
      </p>

      <p>
        Version B: 180 conversions out of 600 visitors
      </p>

      <p>
        Confidence level = 95%
      </p>

    </div>

    <h2>Step 1: Compute the Sample Proportions</h2>

    <p>
      For Version A:
    </p>

    6

    <p>
      For Version B:
    </p>

    7

    <h2>Step 2: Compute the Estimated Difference</h2>

    <p>
      Difference:
    </p>

    8

    <p>
      The sample suggests a 10 percentage-point advantage for Version A.
    </p>

    <h2>Step 3: Compute the Standard Error</h2>

    <p>
      Using:
    </p>

    9

    <p>
      gives approximately:
    </p>

    10

    <h2>Step 4: Compute the Margin of Error</h2>

    <p>
      For 95% confidence:
    </p>

    <div class="example-box">

      <p>
        z* = 1.96
      </p>

    </div>

    <p>
      Therefore:
    </p>

    11

    <h2>Step 5: Construct the Interval</h2>

    <p>
      Therefore:
    </p>

    12

    <p>
      yielding:
    </p>

    <div class="example-box">

      <p>
        (0.0463, 0.1537)
      </p>

    </div>

    <h2>Interpreting the Interval</h2>

    <p>
      Plausible values for:
    </p>

    13

    <p>
      range from approximately:
    </p>

    <div class="example-box">

      <p>
        4.6% to 15.4%
      </p>

    </div>

    <p>
      The data suggest Version A's conversion rate exceeds Version B's by somewhere between about 5 and 15 percentage points.
    </p>

    <h2>The Importance of Zero</h2>

    <p>
      Just as with mean differences,
      zero has a special interpretation.
    </p>

    <div class="concept-box">

      <strong>Zero difference:</strong>

      <p>
        A difference of zero means the population proportions are equal.
      </p>

    </div>

    <h2>When Zero Is Not in the Interval</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        (0.046, 0.154)
      </p>

    </div>

    <p>
      Since zero is excluded,
      equal population proportions are not among the plausible values.
    </p>

    <p>
      Evidence suggests a genuine difference exists.
    </p>

    <h2>When Zero Is in the Interval</h2>

    <p>
      Suppose instead the interval were:
    </p>

    <div class="example-box">

      <p>
        (-0.04, 0.08)
      </p>

    </div>

    <p>
      Since zero lies inside the interval,
      equal population proportions remain plausible.
    </p>

    <p>
      Strong evidence for a difference is lacking.
    </p>

    <h2>Conditions for the Interval</h2>

    <p>
      Several assumptions should be checked.
    </p>

    <ul class="bullets">

      <li>Random sampling or random assignment</li>

      <li>Independent observations within each group</li>

      <li>Independent groups</li>

      <li>Large enough sample sizes for normal approximations</li>

    </ul>

    <h2>The Success-Failure Conditions</h2>

    <p>
      For each sample:
    </p>

    <div class="concept-box">

      <strong>Check both:</strong>

      <p>
        n₁p̂₁ ≥ 10 and n₁(1−p̂₁) ≥ 10
      </p>

      <p>
        n₂p̂₂ ≥ 10 and n₂(1−p̂₂) ≥ 10
      </p>

    </div>

    <p>
      These conditions support the normal approximation.
    </p>

    <h2>Where These Intervals Are Used</h2>

    <ul class="bullets">

      <li>Election polling</li>

      <li>A/B testing</li>

      <li>Clinical trials</li>

      <li>Marketing studies</li>

      <li>Quality-control comparisons</li>

    </ul>

    <p>
      Comparing percentages is one of the most common tasks in applied statistics.
    </p>

    <h2>Difference of Means vs Difference of Proportions</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Means</th>
            <th>Proportions</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Parameter</td>
            <td>μ₁ − μ₂</td>
            <td>p₁ − p₂</td>
          </tr>

          <tr>
            <td>Estimator</td>
            <td>x̄₁ − x̄₂</td>
            <td>p̂₁ − p̂₂</td>
          </tr>

          <tr>
            <td>Critical Value</td>
            <td>Usually t</td>
            <td>z</td>
          </tr>

        </tbody>

      </table>

    </div>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Confidence intervals for differences in proportions estimate how much two population percentages differ while accounting for uncertainty from both samples.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Not all comparisons involve independent groups.
    </p>

    <p>
      Many studies measure the same subjects twice, such as before-and-after experiments.
    </p>

    <p>
      The next lesson introduces confidence intervals for paired mean differences, where observations are naturally linked rather than independent.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The parameter of interest is p₁ − p₂</li>

        <li>The estimator is p̂₁ − p̂₂</li>

        <li>The standard error combines uncertainty from both samples</li>

        <li>The interval uses z critical values</li>

        <li>Zero represents equal population proportions</li>

        <li>If zero is outside the interval, evidence suggests a true difference</li>

        <li>Success-failure conditions should be checked in both groups</li>

        <li>Difference-of-proportion intervals are widely used in polling, experiments, and A/B testing</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">
         ← Previous: CI for Difference of Means
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-paired-mean-difference/">
         Next: CI for Paired Mean Difference →
      </a>

    </div>

  </div>

</section>