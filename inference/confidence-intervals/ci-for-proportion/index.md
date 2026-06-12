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
      Many statistical questions involve proportions rather than means.
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
         href="/inference/confidence-intervals/ci-for-difference-of-mean-independent/">
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
      Suppose a population contains individuals who either possess or do not possess some characteristic.
    </p>

    <div class="example-box">

      <p>
        Supports a candidate
      </p>

      <p>
        Purchased a product
      </p>

      <p>
        Has a disease
      </p>

      <p>
        Passed an exam
      </p>

    </div>

    <p>
      The population proportion is denoted by:
    </p>

    0

    <h2>The Sample Proportion</h2>

    <p>
      Since the true population proportion is unknown,
      we estimate it using the sample proportion:
    </p>

    1

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>x = number of successes</li>

      <li>n = sample size</li>

    </ul>

    <p>
      The sample proportion serves as the point estimate.
    </p>

    <h2>An Example</h2>

    <p>
      Suppose a survey of:
    </p>

    <div class="example-box">

      <p>
        n = 500 voters
      </p>
    </div>

    <p>
      finds:
    </p>

    <div class="example-box">

      <p>
        310 support a proposal
      </p>
    </div>

    <p>
      Then:
    </p>

    2

    <p>
      The estimated support level is 62%.
    </p>

    <h2>The Sampling Distribution of p̂</h2>

    <p>
      Like the sample mean,
      the sample proportion varies from sample to sample.
    </p>

    <p>
      Therefore:
    </p>

    3

    <p>
      has a sampling distribution.
    </p>

    <p>
      Confidence intervals are built from that sampling distribution.
    </p>

    <h2>The Standard Error of a Proportion</h2>

    <p>
      The standard error of a sample proportion is:
    </p>

    4

    <p>
      Because the true proportion is unknown,
      we estimate it using:
    </p>

    5

    <h2>The Confidence Interval Formula</h2>

    <p>
      Using the standard confidence interval blueprint:
    </p>

    6

    <p>
      This is the traditional confidence interval for a population proportion.
    </p>

    <h2>Why z Critical Values Are Used</h2>

    <p>
      Under appropriate conditions,
      the sampling distribution of:
    </p>

    7

    <p>
      is approximately normal.
    </p>

    <p>
      Therefore z critical values are used.
    </p>

    <h2>Conditions for a Proportion Interval</h2>

    <p>
      Three conditions are commonly checked:
    </p>

    <ol>

      <li>Random sampling</li>

      <li>Independence (often via the 10% condition)</li>

      <li>Large-count condition</li>

    </ol>

    <h2>The Large-Count Condition</h2>

    <p>
      The normal approximation works best when there are enough expected successes and failures.
    </p>

    <div class="concept-box">

      <strong>Rule of thumb:</strong>

      <p>
        n·p̂ ≥ 10 and n·(1 − p̂) ≥ 10
      </p>

    </div>

    <p>
      This helps ensure the sampling distribution is reasonably normal.
    </p>

    <h2>Example Setup</h2>

    <p>
      Using the earlier survey:
    </p>

    <div class="example-box">

      <p>
        n = 500
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

    8

    <p>
      gives approximately:
    </p>

    <div class="example-box">

      <p>
        SE ≈ 0.0217
      </p>

    </div>

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
      giving:
    </p>

    <div class="example-box">

      <p>
        (0.578, 0.663)
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
        The procedure used to generate this interval captures the true population proportion about 95% of the time in repeated sampling.
      </p>
    </div>

    <p>
      The interval suggests plausible values for the population proportion lie between 57.8% and 66.3%.
    </p>

    <h2>What Affects Interval Width?</h2>

    <p>
      The width depends on:
    </p>

    <ul class="bullets">

      <li>Confidence level</li>

      <li>Sample size</li>

      <li>The estimated proportion itself</li>

    </ul>

    <h2>Effect of Sample Size</h2>

    <p>
      Larger samples reduce:
    </p>

    11

    <p>
      producing narrower confidence intervals.
    </p>

    <div class="example-box">

      <p>
        Larger sample → smaller SE → narrower interval
      </p>
    </div>

    <h2>When Is Variability Largest?</h2>

    <p>
      The quantity:
    </p>

    12

    <p>
      is largest when:
    </p>

    13

    <p>
      Therefore proportions near 50% typically produce the widest intervals.
    </p>

    <h2>Polling and Margins of Error</h2>

    <p>
      Election polling frequently reports:
    </p>

    <div class="example-box">

      <p>
        Support = 52%
      </p>

      <p>
        Margin of Error = ±3%
      </p>

    </div>

    <p>
      This is simply a confidence interval written in abbreviated form.
    </p>

    <h2>Limitations of the Traditional Formula</h2>

    <p>
      For small samples or proportions near 0 or 1,
      the traditional interval may perform poorly.
    </p>

    <p>
      More advanced alternatives include:
    </p>

    <ul class="bullets">

      <li>Wilson intervals</li>

      <li>Agresti–Coull intervals</li>

      <li>Exact binomial intervals</li>

    </ul>

    <p>
      However,
      the traditional interval remains important for learning core concepts.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Confidence intervals for proportions follow exactly the same logic as confidence intervals for means.
    </p>

    <p>
      The estimate changes,
      the standard error changes,
      but the inferential blueprint remains identical.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A confidence interval for a population proportion combines a sample proportion, a standard error, and a z critical value to quantify uncertainty about the true population proportion.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Many studies compare two groups rather than estimating a single parameter.
    </p>

    <p>
      The next lesson extends confidence interval ideas to differences between independent means, allowing direct comparison of populations.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The population proportion is denoted by p</li>

        <li>The sample proportion p̂ serves as the point estimate</li>

        <li>The standard error depends on p̂ and sample size</li>

        <li>The interval formula is p̂ ± z*SE</li>

        <li>Random sampling and independence remain important assumptions</li>

        <li>The large-count condition supports the normal approximation</li>

        <li>Larger samples produce narrower intervals</li>

        <li>Confidence intervals for proportions follow the same blueprint as mean intervals</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/conditions-normality-clt-independence/">
         ← Previous: Conditions — Normality, CLT, and Independence
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-difference-of-mean-independent/">
         Next: CI for Difference of Means →
      </a>

    </div>

  </div>

</section>