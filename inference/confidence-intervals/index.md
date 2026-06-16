---
layout: default
title: Block 2 — Confidence Intervals
description: Build confidence intervals correctly: the logic of coverage, margin of error, critical values (z/t), and interval construction for means, proportions, and comparisons.
permalink: /inference/confidence-intervals/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_inference_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/",
    label: "Block 2 — Confidence Intervals",
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
        <span class="badge">Inference</span>
        <span class="badge">Block 2</span>
        <span class="badge">Intervals</span>
        <span class="badge">Coverage</span>
      </div>

      <h1>Block 2 — Confidence Intervals</h1>

      <p class="lead">
        Confidence intervals provide a structured way to quantify uncertainty
        around statistical estimates.
      </p>

      <p class="lead">
        This block develops interval estimation from first principles,
        showing how estimates,
        standard errors,
        and critical values combine to produce meaningful uncertainty statements.
      </p>

      <p class="muted-mini">
        12 lessons • Core inferential tools • Builds on Inference Foundations • Prepares for Hypothesis Testing
      </p>

      <div class="hero-actions">

        <a class="btn" href="#lessons">
          Open Lessons
        </a>

        <a class="btn btn-outline" href="/inference/">
          Back to Statistical Inference
        </a>

      </div>

      <div class="hero-highlight">

        <div class="hero-highlight-icon">
          📏
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Point estimates alone are incomplete.
            Confidence intervals provide the uncertainty context needed for
            responsible statistical conclusions and evidence-based decisions.
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
          <div class="mini-body">12 structured lessons</div>
        </div>

        <div class="mini">
          <div class="mini-title">Level</div>
          <div class="mini-body">Core statistical inference</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Build and interpret confidence intervals
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Hypothesis Testing
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-inference-ci"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-inference-ci-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-inference-ci-btn"
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
      These lessons develop interval estimation from conceptual foundations
      through practical construction and interpretation.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/what-is-a-confidence-interval/">
          What Is a Confidence Interval?
        </a>
      </h3>

      <p>
        Learn the meaning of confidence intervals,
        long-run coverage,
        and what “95% confidence” actually means.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Coverage</span>
        <span class="pill">Confidence</span>
        <span class="pill">Foundations</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/what-is-a-confidence-interval/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/">
          CI Blueprint: Estimate ± Margin of Error
        </a>
      </h3>

      <p>
        Learn the universal structure shared by nearly all confidence intervals.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Blueprint</span>
        <span class="pill">Margin of Error</span>
        <span class="pill">Structure</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/critical-values-z-and-t/">
          Critical Values: z and t
        </a>
      </h3>

      <p>
        Understand critical values,
        confidence levels,
        and why z and t distributions are used.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">z</span>
        <span class="pill">t</span>
        <span class="pill">Critical Values</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/critical-values-z-and-t/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/">
          CI for a Mean (σ Known): z-Interval
        </a>
      </h3>

      <p>
        Construct confidence intervals for a population mean
        when the population standard deviation is known.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Mean</span>
        <span class="pill">z-Interval</span>
        <span class="pill">Estimation</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">
          CI for a Mean (σ Unknown): t-Interval
        </a>
      </h3>

      <p>
        Use sample variability and t critical values
        to construct confidence intervals for means.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Mean</span>
        <span class="pill">t-Interval</span>
        <span class="pill">Degrees of Freedom</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 6 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/conditions-normality-clt-independence/">
          Conditions for Valid CIs
        </a>
      </h3>

      <p>
        Learn the assumptions required for confidence intervals
        and how to assess them in practice.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Conditions</span>
        <span class="pill">CLT</span>
        <span class="pill">Validity</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/conditions-normality-clt-independence/"
      >
        Open lesson
      </a>

    </div>

<!-- LESSON 7 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-proportion/">
          CI for a Proportion
        </a>
      </h3>

      <p>
        Construct confidence intervals for population proportions
        and understand the success–failure condition.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Proportion</span>
        <span class="pill">SE</span>
        <span class="pill">Conditions</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-proportion/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 8 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">
          CI for Difference of Means (Independent Samples)
        </a>
      </h3>

      <p>
        Compare two population means using confidence intervals
        for independent samples.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Two Samples</span>
        <span class="pill">Means</span>
        <span class="pill">Comparison</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-difference-of-means-independent/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 9 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-difference-of-proportions/">
          CI for Difference of Proportions
        </a>
      </h3>

      <p>
        Estimate and interpret differences between two population proportions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Proportions</span>
        <span class="pill">Comparison</span>
        <span class="pill">Inference</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-difference-of-proportions/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 10 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/ci-for-paired-mean-difference/">
          CI for Paired Data (Mean of Differences)
        </a>
      </h3>

      <p>
        Learn how paired designs are analyzed
        through intervals for difference scores.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Paired Data</span>
        <span class="pill">Differences</span>
        <span class="pill">t-Interval</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/ci-for-paired-mean-difference/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 11 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/width-and-precision-what-controls/">
          CI Width and Precision: What Controls It?
        </a>
      </h3>

      <p>
        Learn how sample size,
        variability,
        and confidence level affect interval width.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Precision</span>
        <span class="pill">Sample Size</span>
        <span class="pill">Width</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/width-and-precision-what-controls/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 12 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/inference/confidence-intervals/common-mistakes-and-interpretation/">
          Interpretation and Common Mistakes
        </a>
      </h3>

      <p>
        Learn correct interval interpretation
        and avoid common misconceptions about confidence.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Interpretation</span>
        <span class="pill">Mistakes</span>
        <span class="pill">Reporting</span>
      </div>

      <a
        class="btn btn-outline"
        href="/inference/confidence-intervals/common-mistakes-and-interpretation/"
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

      <h2>How this block fits into inference</h2>

      <p>
        Confidence intervals are the first major inferential tool.
        They combine estimation and uncertainty into a single framework,
        providing information about both plausible parameter values and estimation precision.
      </p>

      <div class="table-wrap">

        <table>

          <thead>

            <tr>
              <th>Concept</th>
              <th>Why it matters later</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>Confidence Level</td>
              <td>Controls long-run coverage of interval procedures</td>
            </tr>

            <tr>
              <td>Margin of Error</td>
              <td>Quantifies uncertainty around estimates</td>
            </tr>

            <tr>
              <td>Critical Values</td>
              <td>Connect sampling distributions to inference</td>
            </tr>

            <tr>
              <td>Standard Error</td>
              <td>Determines interval width and precision</td>
            </tr>

            <tr>
              <td>Interval Interpretation</td>
              <td>Foundation for correct statistical reporting</td>
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

        <li>Understand confidence intervals as long-run coverage procedures</li>

        <li>Use the universal estimate ± margin of error framework</li>

        <li>Choose appropriate z and t critical values</li>

        <li>Construct intervals for means, proportions, and comparisons</li>

        <li>Check assumptions required for valid confidence intervals</li>

        <li>Interpret interval width and statistical precision correctly</li>

        <li>Avoid common confidence interval misconceptions</li>

        <li>Prepare for Hypothesis Testing</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Hypothesis Testing</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Every confidence interval combines an estimate with a measure of uncertainty.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          The same sampling distributions used for intervals will power hypothesis tests.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/inference/foundations/">
      ← Previous Block: Inference Foundations
    </a>

    <a class="btn" href="/inference/hypothesis-testing/">
      Next Block: Hypothesis Testing →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_inference_confidence_intervals_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-inference-ci"
      );

    const label =
      document.getElementById(
        "continue-reading-inference-ci-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-inference-ci-btn"
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