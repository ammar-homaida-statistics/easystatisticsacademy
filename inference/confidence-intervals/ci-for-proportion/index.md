---
layout: default
title: Confidence Interval for a Proportion
description: Learn how to construct and interpret confidence intervals for population proportions using sample proportions and normal approximations.
permalink: /inference/confidence-intervals/ci-for-proportion/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_confidence_intervals_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/ci-for-proportion/",
    label: "Confidence Interval for a Proportion",
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
      <span class="badge">Proportions</span>
    </div>

    <h1>Confidence Interval for a Proportion</h1>

    <p class="lead">
      Many real-world questions involve proportions rather than means.
    </p>

    <p class="lead">
      Polling results, approval ratings, defect rates, conversion rates, and disease prevalence are all examples where the parameter of interest is a population proportion.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/confidence-intervals/conditions-normality-clt-independence/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">
         Next: CI for Difference of Means →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Parameter of Interest</h2>

    <p>
      When studying proportions, the population parameter is:
    </p>

    0

    <p>
      representing the proportion of the population possessing a particular characteristic.
    </p>

    <div class="example-box">

      <p>
        Proportion supporting a candidate
      </p>

      <p>
        Proportion purchasing a product
      </p>

      <p>
        Proportion of defective items
      </p>

      <p>
        Proportion responding "Yes" to a survey question
      </p>

    </div>

    <h2>The Sample Proportion</h2>

    <p>
      Since the true population proportion is unknown,
      we estimate it using the sample proportion:
    </p>

    1

    <p>
      which equals:
    </p>

    2

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>x = number of successes</li>

      <li>n = sample size</li>

    </ul>

    <h2>Example of a Sample Proportion</h2>

    <p>
      Suppose a survey asks 500 people whether they support a policy.
    </p>

    <p>
      If 310 people support it:
    </p>

    3

    <p>
      The sample proportion estimates the population proportion.
    </p>

    <h2>The Confidence Interval Blueprint Still Applies</h2>

    <p>
      As always:
    </p>

    4

    <p>
      For proportions:
    </p>

    <ul class="bullets">

      <li>Estimate = p̂</li>

      <li>Margin of Error = Critical Value × Standard Error</li>

    </ul>

    <h2>The Standard Error of a Proportion</h2>

    <p>
      The estimated standard error is:
    </p>

    5

    <p>
      This measures how much sample proportions vary across repeated samples.
    </p>

    <h2>The Confidence Interval Formula</h2>

    <p>
      Combining the estimate,
      standard error,
      and z critical value gives:
    </p>

    6

    <p>
      This is the standard large-sample confidence interval for a population proportion.
    </p>

    <h2>Why z Critical Values Are Used</h2>

    <p>
      Unlike mean intervals,
      proportion intervals do not use the t distribution.
    </p>

    <p>
      Under appropriate conditions,
      the sampling distribution of the sample proportion is approximately normal.
    </p>

    <p>
      Therefore z critical values are used.
    </p>

    <h2>Example Setup</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        n = 500
      </p>

      <p>
        x = 310
      </p>

      <p>
        p̂ = 0.62
      </p>

      <p>
        Confidence level = 95%
      </p>

    </div>

    <h2>Step 1: Compute the Standard Error</h2>

    <p>
      Using:
    </p>

    7

    <p>
      gives approximately:
    </p>

    8

    <h2>Step 2: Find the Critical Value</h2>

    <p>
      For a 95% confidence interval:
    </p>

    <div class="example-box">

      <p>
        z* = 1.96
      </p>

    </div>

    <h2>Step 3: Compute the Margin of Error</h2>

    <p>
      Margin of error:
    </p>

    9

    <h2>Step 4: Construct the Interval</h2>

    <p>
      Therefore:
    </p>

    10

    <p>
      yielding:
    </p>

    <div class="example-box">

      <p>
        (0.5775, 0.6625)
      </p>

    </div>

    <p>
      or approximately:
    </p>

    <div class="example-box">

      <p>
        57.8% to 66.3%
      </p>

    </div>

    <h2>Interpreting the Interval</h2>

    <p>
      A correct interpretation is:
    </p>

    <div class="example-box">

      <p>
        We used a procedure that captures the true population proportion approximately 95% of the time in repeated sampling.
      </p>

    </div>

    <p>
      The interval suggests plausible values for the population proportion lie between about 57.8% and 66.3%.
    </p>

    <h2>Conditions for Proportion Intervals</h2>

    <p>
      Several assumptions should be checked before using the interval.
    </p>

    <h3>1. Random Sampling</h3>

    <p>
      The sample should be reasonably representative of the population.
    </p>

    <h3>2. Independence</h3>

    <p>
      Observations should be approximately independent.
    </p>

    <p>
      The 10% condition is often used:
    </p>

    <div class="example-box">

      <p>
        Sample size less than about 10% of the population.
      </p>

    </div>

    <h3>3. Success-Failure Condition</h3>

    <p>
      The normal approximation requires enough successes and failures.
    </p>

    <div class="concept-box">

      <strong>Success-Failure Condition:</strong>

      <p>
        n·p̂ ≥ 10 and n·(1 − p̂) ≥ 10
      </p>

    </div>

    <p>
      This ensures the sampling distribution is approximately normal.
    </p>

    <h2>Checking the Condition in Our Example</h2>

    <p>
      Successes:
    </p>

    11

    <p>
      Failures:
    </p>

    12

    <p>
      Both values exceed 10,
      so the condition is easily satisfied.
    </p>

    <h2>What Affects Interval Width?</h2>

    <p>
      The same factors appear again:
    </p>

    <ul class="bullets">

      <li>Confidence level</li>

      <li>Sample size</li>

      <li>Variability in the proportion</li>

    </ul>

    <h2>Effect of Sample Size</h2>

    <p>
      Larger samples reduce the standard error.
    </p>

    <p>
      Smaller standard errors create narrower intervals.
    </p>

    <div class="example-box">

      <p>
        Larger sample → greater precision
      </p>

    </div>

    <h2>When Variability Is Largest</h2>

    <p>
      The quantity:
    </p>

    13

    <p>
      reaches its maximum when:
    </p>

    14

    <p>
      This means proportions near 50% tend to produce the largest standard errors and widest intervals.
    </p>

    <h2>Why Proportion Intervals Matter</h2>

    <p>
      Confidence intervals for proportions appear everywhere:
    </p>

    <ul class="bullets">

      <li>Political polling</li>

      <li>Market research</li>

      <li>Medical studies</li>

      <li>Quality control</li>

      <li>A/B testing</li>

    </ul>

    <p>
      They are among the most frequently used inferential tools.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Confidence intervals for proportions estimate population percentages by combining a sample proportion with a normal-approximation margin of error based on its standard error.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      So far we have estimated a single mean and a single proportion.
    </p>

    <p>
      Many real research questions compare groups rather than describing one group.
    </p>

    <p>
      The next lesson develops confidence intervals for differences between two independent population means.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The parameter of interest is the population proportion p</li>

        <li>The estimator is the sample proportion p̂</li>

        <li>The standard error is √[p̂(1−p̂)/n]</li>

        <li>Proportion intervals use z critical values</li>

        <li>The confidence interval formula is p̂ ± z*SE</li>

        <li>The success-failure condition supports the normal approximation</li>

        <li>Larger samples produce narrower intervals</li>

        <li>Confidence intervals for proportions are widely used in surveys and polling</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/conditions-normality-clt-independence/">
         ← Previous: Conditions — Normality, CLT, and Independence
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">
         Next: CI for Difference of Means →
      </a>

    </div>

  </div>

</section>