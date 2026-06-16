---
layout: default
title: Confidence Interval for a Mean (σ Unknown) — t Interval
description: Learn how to construct and interpret a confidence interval for a population mean when the population standard deviation is unknown.
permalink: /inference/confidence-intervals/ci-for-mean-sigma-unknown-t/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_confidence_intervals_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/",
    label: "Confidence Interval for a Mean (σ Unknown) — t Interval",
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
      <span class="badge">Most Common CI</span>
    </div>

    <h1>Confidence Interval for a Mean (σ Unknown) — t Interval</h1>

    <p class="lead">
      In real statistical work, the population standard deviation is almost never known.
    </p>

    <p class="lead">
      Instead, we estimate it from the sample. This introduces additional uncertainty, which is why the t distribution is used instead of the normal distribution.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/conditions-normality-clt-independence/">
         Next: Conditions — Normality, CLT, Independence →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why the z Interval Is Usually Unrealistic</h2>

    <p>
      The z interval assumes the population standard deviation:
    </p>

    0

    <p>
      is known.
    </p>

    <p>
      In practice, this is rarely true.
    </p>

    <p>
      Most of the time we only have sample data, so population variability must be estimated.
    </p>

    <h2>Replacing σ with s</h2>

    <p>
      Since σ is unknown, we replace it with the sample standard deviation:
    </p>

    1

    <p>
      This estimate introduces additional uncertainty because:
    </p>

    <ul class="bullets">

      <li>The sample mean varies from sample to sample.</li>

      <li>The sample standard deviation varies from sample to sample.</li>

    </ul>

    <p>
      Both sources of uncertainty must now be considered.
    </p>

    <h2>Why the t Distribution Appears</h2>

    <p>
      When σ is replaced by s,
      the standardized statistic no longer follows the standard normal distribution.
    </p>

    <p>
      Instead it follows a t distribution.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The t distribution accounts for uncertainty introduced by estimating population variability.
      </p>

    </div>

    <h2>The t Distribution Revisited</h2>

    <p>
      The t distribution resembles the normal distribution but has heavier tails.
    </p>

    <p>
      Heavier tails allow more probability for extreme values.
    </p>

    <p>
      This extra probability reflects the added uncertainty from estimating σ.
    </p>

    <h2>The Standard Error</h2>

    <p>
      When σ is unknown, the estimated standard error becomes:
    </p>

    2

    <p>
      This is the estimated variability of the sample mean.
    </p>

    <h2>The t Confidence Interval Formula</h2>

    <p>
      Applying the confidence interval blueprint gives:
    </p>

    3

    <p>
      This is the one-sample t confidence interval for a population mean.
    </p>

    <h2>Understanding the Components</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Symbol</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>x̄</td>
            <td>Sample mean</td>
          </tr>

          <tr>
            <td>t*</td>
            <td>t critical value</td>
          </tr>

          <tr>
            <td>s</td>
            <td>Sample standard deviation</td>
          </tr>

          <tr>
            <td>n</td>
            <td>Sample size</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Degrees of Freedom</h2>

    <p>
      Unlike z critical values,
      t critical values depend on degrees of freedom.
    </p>

    <p>
      For a one-sample mean interval:
    </p>

    4

    <p>
      The degrees of freedom determine the exact shape of the t distribution.
    </p>

    <h2>Why Degrees of Freedom Matter</h2>

    <p>
      Small samples provide less information about population variability.
    </p>

    <p>
      Therefore:
    </p>

    <ul class="bullets">

      <li>Small df → larger t critical values</li>

      <li>Large df → t approaches z</li>

    </ul>

    <p>
      This automatically adjusts interval width based on sample size.
    </p>

    <h2>Example Setup</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Sample mean = 80
      </p>

      <p>
        Sample standard deviation = 15
      </p>

      <p>
        Sample size = 25
      </p>

      <p>
        Confidence level = 95%
      </p>

    </div>

    <h2>Step 1: Compute the Standard Error</h2>

    <p>
      Using:
    </p>

    5

    <p>
      gives:
    </p>

    6

    <h2>Step 2: Determine Degrees of Freedom</h2>

    <p>
      Since:
    </p>

    7

    <p>
      we use a t critical value based on 24 degrees of freedom.
    </p>

    <h2>Step 3: Find the Critical Value</h2>

    <p>
      For:
    </p>

    <div class="example-box">

      <p>
        95% confidence
      </p>

      <p>
        df = 24
      </p>

    </div>

    <p>
      the critical value is approximately:
    </p>

    <div class="example-box">

      <p>
        t* ≈ 2.064
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
      giving:
    </p>

    <div class="example-box">

      <p>
        (73.81, 86.19)
      </p>

    </div>

    <h2>Comparing z and t Intervals</h2>

    <p>
      Notice that t intervals are generally wider than comparable z intervals.
    </p>

    <p>
      This reflects the additional uncertainty from estimating σ.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>z Interval</th>
            <th>t Interval</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Population SD known?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Critical values</td>
            <td>z</td>
            <td>t</td>
          </tr>

          <tr>
            <td>Depends on df?</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Usually wider?</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>What Happens as Sample Size Grows?</h2>

    <p>
      Larger samples estimate population variability more accurately.
    </p>

    <p>
      As sample size increases:
    </p>

    <ul class="bullets">

      <li>Degrees of freedom increase</li>

      <li>t critical values decrease</li>

      <li>t approaches the normal distribution</li>

    </ul>

    <p>
      Eventually the distinction between z and t becomes very small.
    </p>

    <h2>Why This Is the Most Important Mean Interval</h2>

    <p>
      Because σ is rarely known,
      the t interval is the standard method for estimating population means.
    </p>

    <p>
      It is one of the most widely used confidence intervals in statistics.
    </p>

    <h2>When Is the t Interval Appropriate?</h2>

    <p>
      The method is appropriate when:
    </p>

    <ul class="bullets">

      <li>Data come from a random sample</li>

      <li>Observations are independent</li>

      <li>The sampling distribution is approximately normal</li>

    </ul>

    <p>
      The next lesson focuses entirely on these conditions.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        When population variability is unknown, confidence intervals for means use the sample standard deviation, a t critical value, and the estimated standard error s/√n.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Every confidence interval formula relies on assumptions.
    </p>

    <p>
      For mean intervals, the most important involve independence, normality, and the Central Limit Theorem.
    </p>

    <p>
      The next lesson examines when mean confidence intervals are trustworthy and when caution is needed.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The t interval is used when the population standard deviation is unknown</li>

        <li>The standard error is estimated using s/√n</li>

        <li>The interval formula is x̄ ± t*SE</li>

        <li>t critical values depend on degrees of freedom</li>

        <li>Degrees of freedom equal n − 1 for one-sample mean intervals</li>

        <li>t intervals are usually wider than z intervals</li>

        <li>As sample size increases, t approaches the normal distribution</li>

        <li>The t interval is the most commonly used confidence interval for means</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/">
         ← Previous: CI for Mean (σ Known)
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/conditions-normality-clt-independence/">
         Next: Conditions — Normality, CLT, Independence →
      </a>

    </div>

  </div>

</section>