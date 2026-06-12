---
layout: default
title: What Is a Confidence Interval?
description: Learn what a confidence interval is, why it exists, and how it helps quantify uncertainty in statistical estimation.
permalink: /inference/confidence-intervals/what-is-a-confidence-interval/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_confidence_intervals_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/what-is-a-confidence-interval/",
    label: "What Is a Confidence Interval?",
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
      <span class="badge">Core Concept</span>
    </div>

    <h1>What Is a Confidence Interval?</h1>

    <p class="lead">
      A point estimate gives a single best guess for an unknown parameter.
    </p>

    <p class="lead">
      A confidence interval goes further by providing a range of plausible values and explicitly acknowledging uncertainty.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/confidence-intervals/">
         ← Block Home
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/">
         Next: Interval Blueprint →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Point Estimates Are Not Enough</h2>

    <p>
      Suppose a survey estimates that 62% of voters support a policy.
    </p>

    <div class="example-box">

      <p>
        Point estimate = 62%
      </p>
    </div>

    <p>
      This provides a useful summary,
      but it hides an important fact:
    </p>

    <p>
      The estimate comes from a sample,
      and different samples would produce different results.
    </p>

    <p>
      Therefore uncertainty exists.
    </p>

    <h2>The Need for a Range</h2>

    <p>
      Instead of reporting only one value,
      statisticians often report a range of plausible values for the population parameter.
    </p>

    <div class="example-box">

      <p>
        62% (95% CI: 58% to 66%)
      </p>
    </div>

    <p>
      This range is called a confidence interval.
    </p>

    <h2>Definition</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A confidence interval is an interval constructed from sample data that is designed to contain the true population parameter with a specified long-run success rate.
      </p>

    </div>

    <h2>The Basic Idea</h2>

    <p>
      Confidence intervals acknowledge that estimates are uncertain.
    </p>

    <p>
      Instead of saying:
    </p>

    <div class="example-box">

      <p>
        The parameter equals exactly 62%.
      </p>
    </div>

    <p>
      We say:
    </p>

    <div class="example-box">

      <p>
        Values between 58% and 66% are plausible given the observed data.
      </p>
    </div>

    <h2>Where Confidence Intervals Come From</h2>

    <p>
      Confidence intervals are built using:
    </p>

    <ul class="bullets">

      <li>A point estimate</li>

      <li>A sampling distribution</li>

      <li>A standard error</li>

      <li>A confidence level</li>

    </ul>

    <p>
      These ingredients were developed throughout the Foundations block.
    </p>

    <h2>An Intuitive Picture</h2>

    <p>
      Imagine repeatedly collecting random samples from the same population.
    </p>

    <p>
      For each sample,
      construct a confidence interval.
    </p>

    <p>
      Some intervals will miss the true parameter,
      but most will capture it.
    </p>

    <div class="concept-box">

      <strong>Core idea:</strong>

      <p>
        Confidence intervals are designed to capture the true parameter repeatedly across many samples.
      </p>

    </div>

    <h2>What Does 95% Confidence Mean?</h2>

    <p>
      The most common confidence level is 95%.
    </p>

    <p>
      This does not mean:
    </p>

    <div class="example-box">

      <p>
        There is a 95% probability that the parameter is inside the interval.
      </p>
    </div>

    <p>
      Instead,
      it means:
    </p>

    <div class="example-box">

      <p>
        The interval-generating procedure captures the true parameter about 95% of the time in repeated sampling.
      </p>
    </div>

    <h2>The Parameter Is Fixed</h2>

    <p>
      A common misunderstanding arises because people imagine the parameter moving around.
    </p>

    <p>
      In classical inference:
    </p>

    <ul class="bullets">

      <li>The parameter is fixed.</li>

      <li>The interval is random before sampling.</li>

      <li>The observed interval is fixed after sampling.</li>

    </ul>

    <p>
      The randomness comes from the sampling process.
    </p>

    <h2>A Survey Example</h2>

    <p>
      Suppose a poll estimates support for a proposal at:
    </p>

    <div class="example-box">

      <p>
        p̂ = 0.62
      </p>
    </div>

    <p>
      A confidence interval might be:
    </p>

    <div class="example-box">

      <p>
        (0.58, 0.66)
      </p>
    </div>

    <p>
      The interval suggests the true support level is plausibly somewhere within that range.
    </p>

    <h2>Why Wider Intervals Exist</h2>

    <p>
      Some studies produce wide intervals.
    </p>

    <p>
      This usually happens when:
    </p>

    <ul class="bullets">

      <li>Sample sizes are small</li>

      <li>Data are highly variable</li>

      <li>Uncertainty is large</li>

    </ul>

    <p>
      Wide intervals communicate lower precision.
    </p>

    <h2>Why Narrow Intervals Exist</h2>

    <p>
      Narrow intervals typically occur when:
    </p>

    <ul class="bullets">

      <li>Sample sizes are large</li>

      <li>Variability is smaller</li>

      <li>Standard errors are smaller</li>

    </ul>

    <p>
      Narrow intervals indicate greater precision.
    </p>

    <h2>Confidence Intervals vs Point Estimates</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Point Estimate</th>
            <th>Confidence Interval</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Single value</td>
            <td>Range of values</td>
          </tr>

          <tr>
            <td>Best guess</td>
            <td>Best guess + uncertainty</td>
          </tr>

          <tr>
            <td>Less informative</td>
            <td>More informative</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Why Researchers Prefer Confidence Intervals</h2>

    <p>
      Confidence intervals reveal:
    </p>

    <ul class="bullets">

      <li>Estimated effect size</li>

      <li>Precision</li>

      <li>Uncertainty</li>

      <li>Plausible parameter values</li>

    </ul>

    <p>
      This often makes them more useful than point estimates alone.
    </p>

    <h2>Confidence Intervals and Decision Making</h2>

    <p>
      Decision makers rarely care only about the most likely value.
    </p>

    <p>
      They also care about uncertainty.
    </p>

    <p>
      Confidence intervals help communicate both.
    </p>

    <h2>The Confidence Interval Mindset</h2>

    <p>
      A confidence interval shifts the question from:
    </p>

    <div class="example-box">

      <p>
        What is the exact parameter value?
      </p>
    </div>

    <p>
      to:
    </p>

    <div class="example-box">

      <p>
        What values are reasonably consistent with the observed data?
      </p>
    </div>

    <p>
      This is often a more realistic way to think about uncertainty.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Confidence intervals are one of the most important tools in statistical inference.
    </p>

    <p>
      They combine estimates and uncertainty into a single interpretable result.
    </p>

    <p>
      Throughout this block,
      we will learn how they are constructed,
      interpreted,
      and applied in practice.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A confidence interval provides a range of plausible values for an unknown parameter while explicitly accounting for sampling uncertainty.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Every confidence interval follows a common structure.
    </p>

    <p>
      Understanding that structure makes nearly every interval formula easier to learn.
    </p>

    <p>
      The next lesson introduces the universal confidence interval blueprint.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Confidence intervals quantify uncertainty around estimates</li>

        <li>They provide ranges of plausible parameter values</li>

        <li>Confidence intervals are built from estimates and standard errors</li>

        <li>95% confidence refers to long-run procedure performance</li>

        <li>The parameter is fixed; the interval is random before sampling</li>

        <li>Wide intervals indicate lower precision</li>

        <li>Narrow intervals indicate greater precision</li>

        <li>Confidence intervals are generally more informative than point estimates alone</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/">
         ← Confidence Intervals Block Home
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/">
         Next: Interval Blueprint →
      </a>

    </div>

  </div>

</section>