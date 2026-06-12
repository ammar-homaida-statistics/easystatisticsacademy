---
layout: default
title: Critical Values — z and t
description: Learn what critical values are, where z and t critical values come from, and how they determine the width of confidence intervals.
permalink: /inference/confidence-intervals/critical-values-z-and-t/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_confidence_intervals_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/critical-values-z-and-t/",
    label: "Critical Values — z and t",
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
      <span class="badge">Critical Values</span>
    </div>

    <h1>Critical Values — z and t</h1>

    <p class="lead">
      Every confidence interval needs a margin of error.
    </p>

    <p class="lead">
      One component of that margin is the standard error. The other is the critical value, which determines how much uncertainty must be captured to achieve a desired confidence level.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/">
         Next: CI for Mean (σ Known) →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Recall the Confidence Interval Blueprint</h2>

    <p>
      In the previous lesson we learned that confidence intervals generally follow:
    </p>

    0

    <p>
      The standard error measures uncertainty.
    </p>

    <p>
      The critical value determines how much of that uncertainty is included in the interval.
    </p>

    <h2>What Is a Critical Value?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A critical value is a cutoff taken from a probability distribution that determines how far an interval extends from its estimate.
      </p>

    </div>

    <p>
      It acts as a multiplier on the standard error.
    </p>

    <h2>Why We Need Critical Values</h2>

    <p>
      Suppose an estimate has:
    </p>

    <div class="example-box">

      <p>
        Standard Error = 2
      </p>
    </div>

    <p>
      Knowing the uncertainty alone is not enough.
    </p>

    <p>
      We must decide how much of the sampling distribution we want the interval to cover.
    </p>

    <p>
      That choice determines the critical value.
    </p>

    <h2>The Confidence Level Connection</h2>

    <p>
      Confidence levels and critical values are directly connected.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Confidence Level</th>
            <th>Coverage Goal</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>90%</td>
            <td>Capture the middle 90%</td>
          </tr>

          <tr>
            <td>95%</td>
            <td>Capture the middle 95%</td>
          </tr>

          <tr>
            <td>99%</td>
            <td>Capture the middle 99%</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Higher confidence requires covering more of the sampling distribution.
    </p>

    <h2>The Standard Normal Distribution</h2>

    <p>
      Many confidence intervals use the standard normal distribution.
    </p>

    <p>
      This distribution is centered at zero and has standard deviation one.
    </p>

    <p>
      Critical values from this distribution are called z critical values.
    </p>

    <h2>The Famous 95% Critical Value</h2>

    <p>
      For a 95% confidence interval,
      the middle 95% of the standard normal distribution lies approximately between:
    </p>

    1

    <p>
      Therefore the critical value is:
    </p>

    <div class="example-box">

      <p>
        z* = 1.96
      </p>
    </div>

    <h2>Common z Critical Values</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Confidence Level</th>
            <th>z Critical Value</th>
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

    <h2>What These Numbers Mean</h2>

    <p>
      Larger critical values extend the interval farther from the estimate.
    </p>

    <p>
      This increases the probability that the interval procedure captures the true parameter.
    </p>

    <div class="concept-box">

      <strong>Tradeoff:</strong>

      <p>
        More confidence requires a wider interval.
      </p>

    </div>

    <h2>A Margin of Error Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        SE = 2
      </p>

      <p>
        95% confidence
      </p>
    </div>

    <p>
      Then:
    </p>

    2

    <p>
      The interval extends 3.92 units above and below the estimate.
    </p>

    <h2>When z Is Used</h2>

    <p>
      z critical values are typically used when:
    </p>

    <ul class="bullets">

      <li>Population standard deviation is known</li>

      <li>Large-sample approximations apply</li>

      <li>Normal-theory assumptions justify their use</li>

    </ul>

    <p>
      However,
      another distribution is often needed in practice.
    </p>

    <h2>The Problem With Unknown Population Variability</h2>

    <p>
      In real applications,
      the population standard deviation:
    </p>

    3

    <p>
      is usually unknown.
    </p>

    <p>
      Instead,
      we estimate it using sample data.
    </p>

    <p>
      This introduces additional uncertainty.
    </p>

    <h2>Enter the t Distribution</h2>

    <p>
      The t distribution was developed specifically to account for uncertainty arising from estimating population variability.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        The t distribution resembles the normal distribution but has heavier tails.
      </p>

    </div>

    <h2>Why Heavier Tails Matter</h2>

    <p>
      Heavier tails allocate more probability to extreme values.
    </p>

    <p>
      As a result,
      t critical values are larger than corresponding z critical values.
    </p>

    <p>
      This produces wider intervals.
    </p>

    <h2>The Role of Degrees of Freedom</h2>

    <p>
      Unlike z critical values,
      t critical values depend on:
    </p>

    <div class="example-box">

      <p>
        Degrees of Freedom (df)
      </p>
    </div>

    <p>
      For one-sample mean intervals:
    </p>

    4

    <h2>How Sample Size Changes t</h2>

    <p>
      Small samples produce larger t critical values.
    </p>

    <p>
      Large samples make the t distribution increasingly similar to the normal distribution.
    </p>

    <div class="concept-box">

      <strong>Important fact:</strong>

      <p>
        As sample size grows, t critical values approach z critical values.
      </p>

    </div>

    <h2>An Example Comparison</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>95% Confidence</th>
            <th>Critical Value</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>z</td>
            <td>1.96</td>
          </tr>

          <tr>
            <td>t (df = 10)</td>
            <td>≈ 2.228</td>
          </tr>

          <tr>
            <td>t (df = 30)</td>
            <td>≈ 2.042</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Notice how the t critical value decreases toward 1.96 as sample size increases.
    </p>

    <h2>Choosing Between z and t</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Situation</th>
            <th>Use</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>σ known</td>
            <td>z critical value</td>
          </tr>

          <tr>
            <td>σ unknown</td>
            <td>t critical value</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      In practice,
      t methods are often more common because population standard deviations are rarely known.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Critical values determine how much uncertainty is included in a confidence interval.
    </p>

    <p>
      They translate confidence levels into numerical multipliers.
    </p>

    <p>
      Combined with standard errors,
      they create the margin of error that defines interval width.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Critical values determine how many standard errors are needed to achieve a desired confidence level. z values come from the normal distribution, while t values account for additional uncertainty when population variability is unknown.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Now that we understand the confidence interval blueprint and critical values,
      we can construct our first complete confidence interval.
    </p>

    <p>
      The next lesson develops the confidence interval for a population mean when the population standard deviation is known using the z distribution.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Critical values determine interval width</li>

        <li>Confidence levels correspond to specific critical values</li>

        <li>95% confidence corresponds to z* ≈ 1.96</li>

        <li>Margin of error equals critical value times standard error</li>

        <li>Higher confidence requires larger critical values</li>

        <li>The t distribution accounts for uncertainty in estimating variability</li>

        <li>t critical values depend on degrees of freedom</li>

        <li>As sample size increases, t critical values approach z critical values</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/">
         ← Previous: Interval Blueprint
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/">
         Next: CI for Mean (σ Known) →
      </a>

    </div>

  </div>

</section>