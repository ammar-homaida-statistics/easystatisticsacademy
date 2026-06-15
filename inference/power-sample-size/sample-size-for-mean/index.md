---
layout: default
title: Sample Size for a Mean
description: Learn how sample size requirements are determined for estimating and testing population means with desired precision and power.
permalink: /inference/power-sample-size/sample-size-for-mean/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_power_sample_size_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/power-sample-size/sample-size-for-mean/",
    label: "Sample Size for a Mean",
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
      <span class="badge">Study Planning</span>
    </div>

    <h1>Sample Size for a Mean</h1>

    <p class="lead">
      One of the most important questions in study design is determining how many observations are needed before collecting data.
    </p>

    <p class="lead">
      Sample-size calculations help researchers achieve desired precision and statistical power while using resources efficiently.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/power-sample-size/power-curve-and-tradeoffs/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/power-sample-size/sample-size-for-proportion/">
         Next: Sample Size for a Proportion →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Sample Size Matters</h2>

    <p>
      Sample size influences nearly every aspect of statistical inference.
    </p>

    <ul class="bullets">

      <li>Precision of estimates</li>

      <li>Width of confidence intervals</li>

      <li>Statistical power</li>

      <li>Reliability of conclusions</li>

    </ul>

    <p>
      Studies that are too small may miss important effects, while studies that are unnecessarily large may waste time and resources.
    </p>

    <div class="concept-box">

      <strong>Goal:</strong>

      <p>
        Choose a sample size that is large enough to answer the research question but not larger than necessary.
      </p>

    </div>

    <h2>Two Common Objectives</h2>

    <p>
      Sample-size calculations for means typically arise in two situations:
    </p>

    <ul class="bullets">

      <li>Estimating a population mean with desired precision</li>

      <li>Testing hypotheses with desired statistical power</li>

    </ul>

    <p>
      Although related, these objectives use slightly different approaches.
    </p>

    <h2>Precision-Based Planning</h2>

    <p>
      Suppose we want to estimate a population mean and construct a confidence interval.
    </p>

    <p>
      We may ask:
    </p>

    <div class="example-box">

      <p>
        How large should the sample be so the estimate is accurate within a desired margin of error?
      </p>
    </div>

    <h2>Recall the Confidence Interval Formula</h2>

    <p>
      For a mean with known population standard deviation:
    </p>

    0

    <p>
      The margin of error is:
    </p>

    1

    <h2>Solving for Sample Size</h2>

    <p>
      Rearranging the margin-of-error formula gives:
    </p>

    2

    <p>
      This is the classic sample-size formula for estimating a population mean.
    </p>

    <h2>Interpreting the Formula</h2>

    <p>
      The required sample size increases when:
    </p>

    <ul class="bullets">

      <li>Higher confidence is desired</li>

      <li>Population variability is larger</li>

      <li>Greater precision is required</li>

    </ul>

    <p>
      Smaller margins of error require substantially larger samples.
    </p>

    <h2>Example Calculation</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>95% confidence</p>
      <p>σ = 20</p>
      <p>Desired margin of error = 4</p>

    </div>

    <p>
      Using:
    </p>

    3

    <p>
      gives:
    </p>

    4

    <p>
      Since sample size must be an integer and rounding down could reduce precision:
    </p>

    <div class="example-box">

      <p>
        Required sample size = 97
      </p>
    </div>

    <h2>Always Round Up</h2>

    <p>
      Sample-size calculations are always rounded upward.
    </p>

    <p>
      Rounding down could fail to achieve the desired confidence or precision.
    </p>

    <h2>The Effect of Margin of Error</h2>

    <p>
      Notice that:
    </p>

    5

    <p>
      This means reducing the margin of error by half requires approximately four times the sample size.
    </p>

    <h2>A Practical Illustration</h2>

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
            <td>8</td>
            <td>1×</td>
          </tr>

          <tr>
            <td>4</td>
            <td>4×</td>
          </tr>

          <tr>
            <td>2</td>
            <td>16×</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Precision can be expensive.
    </p>

    <h2>Planning for Hypothesis Testing</h2>

    <p>
      Sample-size planning for hypothesis testing includes additional considerations.
    </p>

    <p>
      Researchers must specify:
    </p>

    <ul class="bullets">

      <li>Desired power</li>

      <li>Significance level</li>

      <li>Target effect size</li>

      <li>Population variability</li>

    </ul>

    <h2>The Role of Effect Size</h2>

    <p>
      Recall that larger effects are easier to detect.
    </p>

    <p>
      Therefore:
    </p>

    <div class="concept-box">

      <strong>General rule:</strong>

      <p>
        Smaller target effects require larger sample sizes.
      </p>

    </div>

    <h2>The Role of Variability</h2>

    <p>
      Greater variability creates more noise.
    </p>

    <p>
      More observations are needed to separate signal from noise.
    </p>

    <div class="concept-box">

      <strong>General rule:</strong>

      <p>
        Larger standard deviations require larger samples.
      </p>

    </div>

    <h2>The Role of Confidence Level</h2>

    <p>
      Higher confidence levels require larger critical values.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Confidence Level</th>
            <th>Critical Value</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>90%</td>
            <td>1.645</td>
          </tr>

          <tr>
            <td>95%</td>
            <td>1.96</td>
          </tr>

          <tr>
            <td>99%</td>
            <td>2.576</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      As confidence increases, sample-size requirements also increase.
    </p>

    <h2>Estimating σ in Practice</h2>

    <p>
      The population standard deviation is often unknown before a study begins.
    </p>

    <p>
      Researchers may use:
    </p>

    <ul class="bullets">

      <li>Pilot studies</li>

      <li>Historical studies</li>

      <li>Subject-matter expertise</li>

    </ul>

    <p>
      to obtain a reasonable estimate.
    </p>

    <h2>Balancing Resources and Precision</h2>

    <p>
      Larger samples improve statistical performance, but they also increase:
    </p>

    <ul class="bullets">

      <li>Cost</li>

      <li>Time requirements</li>

      <li>Data collection burden</li>

      <li>Operational complexity</li>

    </ul>

    <p>
      Study planning therefore involves balancing statistical goals against practical constraints.
    </p>

    <h2>When Very Large Samples Are Not Necessary</h2>

    <p>
      Researchers sometimes assume that larger samples are always better.
    </p>

    <p>
      In reality, once a study achieves adequate precision and power, additional observations may provide limited benefit.
    </p>

    <h2>Modern Software</h2>

    <p>
      Most sample-size calculations are performed using statistical software.
    </p>

    <p>
      However, understanding the underlying relationships remains important because software only automates calculations—it does not choose meaningful design goals.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Sample-size determination is one of the most important stages of study planning.
    </p>

    <p>
      It connects confidence intervals, statistical power, variability, and effect size into a single design decision.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Sample-size calculations for means help researchers achieve desired precision and power. Required sample size increases with confidence level, variability, and desired precision, and decreases when larger effects are acceptable.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Many real-world studies focus on proportions rather than means.
    </p>

    <p>
      Polling, surveys, clinical trials, and quality-control studies frequently estimate percentages and probabilities.
    </p>

    <p>
      The next lesson introduces sample-size calculations for population proportions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Sample-size planning can focus on precision or power</li>

        <li>The classic precision formula for means is based on the margin of error</li>

        <li>Required sample size increases as desired precision increases</li>

        <li>Higher confidence levels require larger samples</li>

        <li>Greater variability requires larger samples</li>

        <li>Smaller effects require larger samples to detect</li>

        <li>Sample sizes should always be rounded upward</li>

        <li>Sample-size planning balances statistical goals and practical constraints</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/power-sample-size/power-curve-and-tradeoffs/">
         ← Previous: Power Curves and Trade-Offs
      </a>

      <a class="btn"
         href="/inference/power-sample-size/sample-size-for-proportion/">
         Next: Sample Size for a Proportion →
      </a>

    </div>

  </div>

</section>