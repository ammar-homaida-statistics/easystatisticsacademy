---
layout: default
title: Sample Size for a Proportion
description: Learn how sample-size requirements are determined when estimating or testing population proportions and percentages.
permalink: /inference/power-sample-size/sample-size-for-proportion/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_power_sample_size_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/power-sample-size/sample-size-for-proportion/",
    label: "Sample Size for a Proportion",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 5</span>
      <span class="badge">Power & Sample Size</span>
      <span class="badge">Proportions</span>
    </div>

    <h1>Sample Size for a Proportion</h1>

    <p class="lead">
      Many studies focus on proportions rather than means.
    </p>

    <p class="lead">
      Polling, surveys, quality control, public-health studies, and A/B tests often require determining how many observations are needed to estimate or detect differences in population proportions.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/power-sample-size/sample-size-for-mean/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/power-sample-size/precision-vs-detectability/">
         Next: Precision vs Detectability →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Proportions Matter</h2>

    <p>
      Many important questions involve percentages or probabilities.
    </p>

    <ul class="bullets">

      <li>What proportion of voters support a candidate?</li>

      <li>What fraction of customers make a purchase?</li>

      <li>What percentage of patients respond to treatment?</li>

      <li>What proportion of manufactured items are defective?</li>

    </ul>

    <p>
      Accurate answers require adequate sample sizes.
    </p>

    <h2>Planning for Precision</h2>

    <p>
      Suppose we want to estimate a population proportion:
    </p>

    0

    <p>
      with a specified margin of error.
    </p>

    <p>
      The question becomes:
    </p>

    <div class="example-box">

      <p>
        How many observations are needed to estimate the proportion with sufficient precision?
      </p>
    </div>

    <h2>Recall the Confidence Interval</h2>

    <p>
      For large samples, a confidence interval for a proportion has the form:
    </p>

    1

    <p>
      The margin of error is therefore:
    </p>

    2

    <h2>Solving for Sample Size</h2>

    <p>
      Rearranging the margin-of-error formula gives:
    </p>

    3

    <p>
      This is the classic sample-size formula for estimating a population proportion.
    </p>

    <h2>The Unknown Proportion Problem</h2>

    <p>
      The formula requires a value of:
    </p>

    4

    <p>
      but the true population proportion is usually unknown before data collection.
    </p>

    <p>
      Researchers often use:
    </p>

    <ul class="bullets">

      <li>Pilot studies</li>

      <li>Historical data</li>

      <li>Expert knowledge</li>

    </ul>

    <p>
      to obtain an estimate.
    </p>

    <h2>The Conservative Choice</h2>

    <p>
      When no information is available, a common strategy is:
    </p>

    5

    <p>
      because:
    </p>

    6

    <p>
      is maximized at 0.5.
    </p>

    <p>
      This produces the largest required sample size and ensures adequate precision regardless of the true proportion.
    </p>

    <h2>The Conservative Formula</h2>

    <p>
      Substituting:
    </p>

    7

    <p>
      yields:
    </p>

    8

    <p>
      This is frequently used in survey design.
    </p>

    <h2>Example Calculation</h2>

    <p>
      Suppose we want:
    </p>

    <div class="example-box">

      <p>95% confidence</p>
      <p>Margin of error = 0.03</p>

    </div>

    <p>
      Using:
    </p>

    9

    <p>
      and the conservative assumption:
    </p>

    10

    <p>
      gives:
    </p>

    11

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        Required sample size = 1068
      </p>
    </div>

    <h2>Always Round Up</h2>

    <p>
      As with all sample-size calculations:
    </p>

    <div class="concept-box">

      <strong>Rule:</strong>

      <p>
        Always round upward to ensure the desired precision is achieved.
      </p>

    </div>

    <h2>Effect of Margin of Error</h2>

    <p>
      Notice that:
    </p>

    12

    <p>
      Just as with means, halving the margin of error approximately quadruples the required sample size.
    </p>

    <h2>A Precision Illustration</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Margin of Error</th>
            <th>Relative Sample Size</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>6%</td>
            <td>1×</td>
          </tr>

          <tr>
            <td>3%</td>
            <td>4×</td>
          </tr>

          <tr>
            <td>1.5%</td>
            <td>16×</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Small gains in precision can require substantial increases in sample size.
    </p>

    <h2>Planning for Hypothesis Testing</h2>

    <p>
      When testing hypotheses about proportions, sample-size determination depends on:
    </p>

    <ul class="bullets">

      <li>Desired power</li>

      <li>Significance level</li>

      <li>Target effect size</li>

      <li>Baseline proportion</li>

    </ul>

    <h2>The Role of Effect Size</h2>

    <p>
      Suppose a company wants to detect an increase in conversion rate.
    </p>

    <div class="example-box">

      <p>
        From 10% to 11%
      </p>
    </div>

    <p>
      This is a much smaller effect than:
    </p>

    <div class="example-box">

      <p>
        From 10% to 20%
      </p>
    </div>

    <p>
      Smaller effects require larger samples to detect reliably.
    </p>

    <h2>The Role of Baseline Proportion</h2>

    <p>
      Variability for proportions depends on:
    </p>

    13

    <p>
      Variability is highest near:
    </p>

    14

    <p>
      and decreases as proportions approach 0 or 1.
    </p>

    <p>
      Consequently, required sample sizes also depend on the expected baseline proportion.
    </p>

    <h2>Polling Example</h2>

    <p>
      National election polls often target margins of error around:
    </p>

    <div class="example-box">

      <p>
        ±3%
      </p>
    </div>

    <p>
      which explains why many polls collect roughly one thousand respondents.
    </p>

    <h2>A/B Testing Example</h2>

    <p>
      Online experiments frequently require thousands or even millions of observations because conversion-rate differences can be very small.
    </p>

    <p>
      Detecting tiny effects demands substantial sample sizes.
    </p>

    <h2>Balancing Precision and Cost</h2>

    <p>
      Larger samples improve precision and power, but they also increase:
    </p>

    <ul class="bullets">

      <li>Financial costs</li>

      <li>Time requirements</li>

      <li>Data collection effort</li>

      <li>Operational complexity</li>

    </ul>

    <p>
      Sample-size planning is therefore a balance between statistical goals and practical constraints.
    </p>

    <h2>Modern Software</h2>

    <p>
      Statistical software can compute sample sizes quickly.
    </p>

    <p>
      However, researchers must still choose meaningful targets for precision, effect size, confidence, and power.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Sample-size planning for proportions follows the same principles as planning for means.
    </p>

    <p>
      Researchers specify desired precision or power, then determine the number of observations needed to achieve those goals.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Sample-size calculations for proportions depend on confidence level, margin of error, baseline proportion, and desired power. Smaller margins of error and smaller detectable effects require substantially larger samples.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Precision and detectability are closely related but distinct study-design goals.
    </p>

    <p>
      Some studies aim for narrow confidence intervals, while others focus on detecting meaningful effects.
    </p>

    <p>
      The next lesson explores the difference between precision and detectability and explains how these goals influence study design.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Sample-size planning for proportions often focuses on confidence intervals or power</li>

        <li>The classic proportion formula is based on the desired margin of error</li>

        <li>When p is unknown, p = 0.5 provides a conservative sample-size estimate</li>

        <li>Smaller margins of error require much larger samples</li>

        <li>Required sample size depends on baseline proportion and variability</li>

        <li>Smaller effects require larger samples to detect</li>

        <li>Polling and A/B testing rely heavily on proportion-based sample-size calculations</li>

        <li>Effective study design balances statistical goals and practical limitations</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/power-sample-size/sample-size-for-mean/">
         ← Previous: Sample Size for a Mean
      </a>

      <a class="btn"
         href="/inference/power-sample-size/precision-vs-detectability/">
         Next: Precision vs Detectability →
      </a>

    </div>

  </div>

</section>