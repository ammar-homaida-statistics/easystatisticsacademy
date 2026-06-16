---
layout: default
title: Confidence Interval for Difference of Means (Independent Samples)
description: Learn how to construct and interpret confidence intervals for the difference between two independent population means.
permalink: /inference/confidence-intervals/ci-for-difference-of-means-independent/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_confidence_intervals_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/ci-for-difference-of-means-independent/",
    label: "Confidence Interval for Difference of Means (Independent Samples)",
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
      <span class="badge">Group Comparisons</span>
    </div>

    <h1>Confidence Interval for Difference of Means (Independent Samples)</h1>

    <p class="lead">
      Many research questions focus on comparing two groups rather than estimating a single mean.
    </p>

    <p class="lead">
      Confidence intervals for differences of means help quantify how much two populations differ and how uncertain that estimated difference is.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-proportion/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-difference-of-proportions/">
         Next: CI for Difference of Proportions →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Research Question</h2>

    <p>
      Instead of estimating a single population mean,
      we now compare two population means.
    </p>

    <div class="example-box">

      <p>
        Average exam score of Method A students versus Method B students
      </p>

      <p>
        Average blood pressure for treatment versus control groups
      </p>

      <p>
        Average income in two regions
      </p>

    </div>

    <p>
      The goal is to estimate how different the two population means are.
    </p>

    <h2>The Parameter of Interest</h2>

    <p>
      Let:
    </p>

    <ul class="bullets">

      <li>μ₁ = population mean for Group 1</li>

      <li>μ₂ = population mean for Group 2</li>

    </ul>

    <p>
      The parameter of interest is:
    </p>

    0

    <p>
      which represents the true difference between population means.
    </p>

    <h2>The Estimator</h2>

    <p>
      We estimate the population difference using:
    </p>

    1

    <p>
      the difference between the two sample means.
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
            <td>Group 1 mean exceeds Group 2 mean</td>
          </tr>

          <tr>
            <td>Negative</td>
            <td>Group 2 mean exceeds Group 1 mean</td>
          </tr>

          <tr>
            <td>Zero</td>
            <td>No mean difference</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Confidence Interval Blueprint Still Applies</h2>

    <p>
      The same confidence interval structure remains:
    </p>

    2

    <p>
      Only the estimate and standard error change.
    </p>

    <h2>The Standard Error of a Difference</h2>

    <p>
      When samples are independent,
      variability from both groups contributes to uncertainty.
    </p>

    <p>
      The estimated standard error is:
    </p>

    3

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>s₁ = sample standard deviation for Group 1</li>

      <li>s₂ = sample standard deviation for Group 2</li>

      <li>n₁ = sample size for Group 1</li>

      <li>n₂ = sample size for Group 2</li>

    </ul>

    <h2>Why Variances Add</h2>

    <p>
      Independent samples contribute uncertainty separately.
    </p>

    <p>
      Variance accumulates across the two estimates.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The uncertainty of the difference comes from both samples, not just one.
      </p>

    </div>

    <h2>The Confidence Interval Formula</h2>

    <p>
      The general t interval is:
    </p>

    4

    <p>
      This is the standard confidence interval for two independent population means.
    </p>

    <h2>Example Setup</h2>

    <p>
      Suppose researchers compare two teaching methods.
    </p>

    <div class="example-box">

      <p>
        Group 1 mean = 82
      </p>

      <p>
        Group 2 mean = 76
      </p>

      <p>
        s₁ = 10
      </p>

      <p>
        s₂ = 12
      </p>

      <p>
        n₁ = 40
      </p>

      <p>
        n₂ = 35
      </p>

    </div>

    <h2>Step 1: Compute the Estimated Difference</h2>

    <p>
      Difference:
    </p>

    5

    <p>
      The sample suggests Group 1 scores higher by 6 points.
    </p>

    <h2>Step 2: Compute the Standard Error</h2>

    <p>
      Using:
    </p>

    6

    <p>
      gives approximately:
    </p>

    7

    <h2>Step 3: Find the Critical Value</h2>

    <p>
      For a 95% confidence interval,
      a t critical value is used.
    </p>

    <p>
      Exact degrees of freedom are typically computed by software.
    </p>

    <p>
      For illustration:
    </p>

    <div class="example-box">

      <p>
        t* ≈ 2
      </p>

    </div>

    <h2>Step 4: Compute the Margin of Error</h2>

    <p>
      Margin of error:
    </p>

    8

    <h2>Step 5: Construct the Interval</h2>

    <p>
      Therefore:
    </p>

    9

    <p>
      yielding:
    </p>

    <div class="example-box">

      <p>
        (0.86, 11.14)
      </p>

    </div>

    <h2>Interpreting the Interval</h2>

    <p>
      The interval suggests plausible values for:
    </p>

    10

    <p>
      lie between approximately:
    </p>

    <div class="example-box">

      <p>
        0.86 and 11.14
      </p>

    </div>

    <p>
      The data suggest Group 1 may outperform Group 2 by somewhere between about 1 and 11 points.
    </p>

    <h2>The Importance of Zero</h2>

    <p>
      For difference intervals,
      zero has special meaning.
    </p>

    <div class="concept-box">

      <strong>Zero difference:</strong>

      <p>
        A difference of zero means the two population means are equal.
      </p>

    </div>

    <h2>When Zero Is Not in the Interval</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        (0.86, 11.14)
      </p>

    </div>

    <p>
      Since zero is not contained in the interval,
      the data provide evidence that the population means differ.
    </p>

    <h2>When Zero Is in the Interval</h2>

    <p>
      Suppose instead the interval were:
    </p>

    <div class="example-box">

      <p>
        (-3, 8)
      </p>

    </div>

    <p>
      Because zero lies inside the interval,
      equal population means remain plausible.
    </p>

    <p>
      Strong evidence of a difference is lacking.
    </p>

    <h2>Conditions for the Interval</h2>

    <p>
      Several assumptions should be checked.
    </p>

    <ul class="bullets">

      <li>Random sampling or random assignment</li>

      <li>Independence within each sample</li>

      <li>Independence between groups</li>

      <li>Reasonably normal sampling distributions</li>

    </ul>

    <p>
      The Central Limit Theorem often helps justify normal approximations when sample sizes are sufficiently large.
    </p>

    <h2>Independent vs Paired Samples</h2>

    <p>
      This lesson assumes the two samples are independent.
    </p>

    <div class="example-box">

      <p>
        Different students in two classrooms
      </p>

      <p>
        Different patients in treatment and control groups
      </p>

    </div>

    <p>
      Paired measurements require different methods that account for the matching structure.
    </p>

    <h2>Where These Intervals Are Used</h2>

    <ul class="bullets">

      <li>Clinical trials</li>

      <li>Education studies</li>

      <li>Business experiments</li>

      <li>Manufacturing comparisons</li>

      <li>Social science research</li>

    </ul>

    <p>
      Comparing group means is one of the most common inferential tasks.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Confidence intervals for independent mean differences estimate how far apart two population means are while accounting for uncertainty from both samples.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Researchers often compare percentages as well as means.
    </p>

    <p>
      Election polling, medical studies, and A/B testing frequently focus on differences between proportions.
    </p>

    <p>
      The next lesson develops confidence intervals for differences between two population proportions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The parameter of interest is μ₁ − μ₂</li>

        <li>The estimator is x̄₁ − x̄₂</li>

        <li>Uncertainty comes from both samples</li>

        <li>The standard error combines variability from both groups</li>

        <li>The interval uses a t critical value</li>

        <li>Zero represents no population mean difference</li>

        <li>If zero is outside the interval, a true difference is suggested</li>

        <li>Independent-sample mean intervals are widely used for comparing groups</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-proportion/">
         ← Previous: CI for a Proportion
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-difference-of-proportions/">
         Next: CI for Difference of Proportions →
      </a>

    </div>

  </div>

</section>