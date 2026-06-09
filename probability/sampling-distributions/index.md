---
layout: default
title: Block 7 — Sampling Distributions
description: Understand sampling distributions, standard error, z and t statistics, chi-square and F distributions, and how probability becomes statistical inference.
permalink: /probability/sampling-distributions/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_probability_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/sampling-distributions/",
    label: "Block 7 — Sampling Distributions",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card hero-split">

    <!-- LEFT -->

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Probability</span>
        <span class="badge">Block 7</span>
        <span class="badge">Sampling</span>
        <span class="badge">Inference Bridge</span>
      </div>

      <h1>Block 7 — Sampling Distributions</h1>

      <p class="lead">
        A statistic is a random variable.
      </p>

      <p class="lead">
        This block explains why sample statistics have distributions,
        how standard error measures estimator uncertainty,
        and how z, t, chi-square, and F distributions become the foundation
        of statistical inference.
      </p>

      <p class="muted-mini">
        6 lessons • Final probability block • Builds on LLN & CLT • Prepares for Statistical Inference
      </p>

      <div class="hero-actions">

        <a class="btn" href="#lessons">
          Open Lessons
        </a>

        <a class="btn btn-outline" href="/probability/">
          Back to Probability
        </a>

      </div>

      <div class="hero-highlight">

        <div class="hero-highlight-icon">
          🧪
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Sampling distributions explain how sample results vary from sample to sample.
            They are the mathematical bridge between probability theory and confidence intervals,
            hypothesis tests, regression, ANOVA, and statistical decision-making.
          </p>

        </div>

      </div>

    </div>

    <!-- RIGHT -->

    <div class="hero-panel">

      <div class="panel-card">

        <h2 class="panel-title">Block overview</h2>

        <div class="mini">
          <div class="mini-title">Lessons</div>
          <div class="mini-body">6 structured lessons</div>
        </div>

        <div class="mini">
          <div class="mini-title">Level</div>
          <div class="mini-body">Inference bridge</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Understand distributions of statistics
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next section</div>
          <div class="mini-body">
            Statistical Inference
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-probability-sampling"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-probability-sampling-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-probability-sampling-btn"
        href="#"
      >
        Continue
      </a>

    </div>

  </div>

</section>

<!-- LESSONS -->

<section class="section" id="lessons">

  <div class="section-head">

    <h2>Lessons</h2>

    <p>
      These lessons complete the Probability unit by showing how probability
      distributions become the working machinery of statistical inference.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/sampling-distributions/what-is-a-sampling-distribution/">
          What Is a Sampling Distribution?
        </a>
      </h3>

      <p>
        Learn why statistics vary from sample to sample
        and why every statistic has its own probability distribution.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Sampling</span>
        <span class="pill">Statistic</span>
        <span class="pill">Distribution</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/sampling-distributions/what-is-a-sampling-distribution/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/sampling-distributions/standard-error-and-estimators/">
          Standard Error & Estimators
        </a>
      </h3>

      <p>
        Understand standard error as the uncertainty scale of an estimator
        and connect it to bias, variability, and consistency.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Standard Error</span>
        <span class="pill">Estimators</span>
        <span class="pill">Uncertainty</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/sampling-distributions/standard-error-and-estimators/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/sampling-distributions/z-statistic-and-ci/">
          z-Statistic & Confidence Intervals
        </a>
      </h3>

      <p>
        Learn how normal logic creates z-statistics and confidence intervals
        when the population standard deviation is known.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">z-Statistic</span>
        <span class="pill">Confidence Interval</span>
        <span class="pill">Normal</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/sampling-distributions/z-statistic-and-ci/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/sampling-distributions/t-distribution-and-t-test/">
          t-Distribution & the t-Statistic
        </a>
      </h3>

      <p>
        Understand why the t distribution replaces the normal distribution
        when population variability is unknown.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">t Distribution</span>
        <span class="pill">Degrees of Freedom</span>
        <span class="pill">Unknown σ</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/sampling-distributions/t-distribution-and-t-test/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/sampling-distributions/chi-square-and-variance/">
          Chi-Square Distribution & Variance Inference
        </a>
      </h3>

      <p>
        Learn how the chi-square distribution arises from sample variance
        and supports inference about population variance.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Chi-Square</span>
        <span class="pill">Variance</span>
        <span class="pill">Inference</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/sampling-distributions/chi-square-and-variance/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 6 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/sampling-distributions/f-distribution-and-anova-preview/">
          F Distribution & ANOVA Preview
        </a>
      </h3>

      <p>
        Understand F distributions as ratios of variances
        and preview their role in ANOVA and regression testing.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">F Distribution</span>
        <span class="pill">ANOVA</span>
        <span class="pill">Ratios</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/sampling-distributions/f-distribution-and-anova-preview/"
      >
        Open lesson
      </a>

    </div>

  </div>

</section>

<!-- BLOCK MAP -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>How this block fits into probability</h2>

      <p>
        Probability studies random variables.
        Inference studies statistics computed from samples.
        Sampling distributions connect these two worlds by treating sample statistics
        as random variables with predictable behavior.
      </p>

      <div class="table-wrap">

        <table>

          <thead>

            <tr>
              <th>Concept</th>
              <th>Why it matters for inference</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>Sampling Distribution</td>
              <td>Describes how a statistic varies across repeated samples</td>
            </tr>

            <tr>
              <td>Standard Error</td>
              <td>Quantifies estimator uncertainty</td>
            </tr>

            <tr>
              <td>z Statistic</td>
              <td>Supports normal-based confidence intervals and tests</td>
            </tr>

            <tr>
              <td>t Distribution</td>
              <td>Handles unknown population variability</td>
            </tr>

            <tr>
              <td>Chi-Square Distribution</td>
              <td>Supports variance inference</td>
            </tr>

            <tr>
              <td>F Distribution</td>
              <td>Supports variance comparisons, ANOVA, and regression tests</td>
            </tr>

          </tbody>

        </table>

      </div>

    </div>

  </div>

</section>

<!-- GOALS -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>Goal of this block</h2>

      <ul class="bullets">

        <li>Explain what a sampling distribution is</li>

        <li>Understand why statistics vary from sample to sample</li>

        <li>Use standard error as the uncertainty scale of estimation</li>

        <li>Understand z and t statistics</li>

        <li>Understand chi-square logic for variance inference</li>

        <li>Understand F distributions as ratios of variances</li>

        <li>Prepare for confidence intervals and hypothesis testing</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next section</div>

        <div class="mini-body">
          Continue to <strong>Statistical Inference</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Statistics are random variables because samples are random.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          This block completes the bridge from probability to inference.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/probability/lln-clt/">
      ← Previous Block: Law of Large Numbers & CLT
    </a>

    <a class="btn" href="/inference/">
      Next Section: Statistical Inference →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_probability_sampling_distributions_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-probability-sampling"
      );

    const label =
      document.getElementById(
        "continue-reading-probability-sampling-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-probability-sampling-btn"
      );

    if (!wrap || !label || !btn) return;

    label.innerHTML =
      "You last visited: <strong>" +
      data.label +
      "</strong>";

    btn.href = data.url;

    wrap.style.display = "block";

  } catch (e) {}

})();
</script>