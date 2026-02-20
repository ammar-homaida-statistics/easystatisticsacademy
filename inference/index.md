---
layout: default
title: Statistical Inference
description: Learn inference correctly: sampling distributions, estimation, confidence intervals, hypothesis tests, p-values, power, and interpretation.
permalink: /inference/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Section Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        The Statistical Inference unit is being developed in a structured, block-by-block format.
        Pages and lessons are published in a fixed pedagogical order to ensure clarity, stability,
        and long-term academic consistency.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Uncertainty</span>
        <span class="badge">Estimation</span>
        <span class="badge">Testing</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>Statistical Inference</h1>
      <p class="lead">
        Learn the logic of inference: how we reason from samples to populations. Build correct understanding of
        estimation, confidence intervals, hypothesis testing, p-values, power, and real interpretation—without ritual.
      </p>

      <div class="hero-actions">
        <a class="btn" href="/probability/">Prerequisite: Probability</a>
        <a class="btn btn-outline" href="/modeling/">Next: Statistical Modeling</a>
      </div>

      <p class="muted-mini">
        This landing page is the permanent structure for the Statistical Inference unit. Lessons are published block-by-block.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">Suggested learning order</h2>
        <ol class="quickstart">
          <li><a href="#blocks">Inference foundations</a><span class="meta">Parameters, estimators, SE, CI logic</span></li>
          <li><a href="#blocks">Confidence intervals</a><span class="meta">Interpretation, construction, misuse</span></li>
          <li><a href="#blocks">Hypothesis testing</a><span class="meta">H0/H1, errors, p-values, decisions</span></li>
          <li><a href="#blocks">Classical tests</a><span class="meta">t / chi-square / proportion tests</span></li>
          <li><a href="#blocks">Power &amp; sample size</a><span class="meta">Design thinking beyond “sig/non-sig”</span></li>
          <li><a href="#blocks">Practical interpretation</a><span class="meta">Effect sizes, CIs, reporting</span></li>
          <li><a href="#blocks">Assumptions &amp; robustness</a><span class="meta">When methods fail, what to do</span></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="blocks">
  <div class="section-head">
    <h2>Blocks (Unit Structure)</h2>
    <p>
      Statistical Inference is organized into seven blocks. Each block has its own page and a growing set of lessons.
      The blocks below are active; lessons inside each block will be marked as coming soon until published.
    </p>
  </div>

  <!-- ✅ Continue reading (Inference home → last visited BLOCK) -->
  <div id="continue-reading-inference" style="display:none; margin-top:0.75rem;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p class="muted-mini" id="continue-reading-inference-label" style="margin:0 0 .75rem 0;"></p>
        <a class="btn" id="continue-reading-inference-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <!-- Block 1 -->
    <div class="card lesson-card">
      <h3>
        <a href="/inference/foundations/">Block 1 — Inference Foundations (Estimation &amp; Uncertainty)</a>
      </h3>

      <p>
        Understand what inference is: parameters vs statistics, estimators, bias/variance intuition,
        standard error, and how uncertainty is quantified from sampling.
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/foundations/">Open block</a>
      </div>
    </div>

    <!-- Block 2 -->
    <div class="card lesson-card">
      <h3>
        <a href="/inference/confidence-intervals/">Block 2 — Confidence Intervals (Meaning &amp; Construction)</a>
      </h3>

      <p>
        Learn confidence intervals correctly: what they mean, what they do not mean, how they are built,
        and common interpretation mistakes (especially “probability the parameter is in the interval”).
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Open block</a>
      </div>
    </div>

    <!-- Block 3 -->
    <div class="card lesson-card">
      <h3>
        <a href="/inference/hypothesis-testing/">Block 3 — Hypothesis Testing (Logic, Errors, p-values)</a>
      </h3>

      <p>
        Learn the testing framework: null/alternative, test statistics, Type I/II errors, p-values,
        significance vs evidence, and why “fail to reject” is not “accept.”
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Open block</a>
      </div>
    </div>

    <!-- Block 4 -->
    <div class="card lesson-card">
      <h3>
        <a href="/inference/classical-tests/">Block 4 — Classical Tests (t, Proportions, Chi-square)</a>
      </h3>

      <p>
        Apply standard tests with assumptions and interpretation: one-sample/two-sample/paired t-tests,
        one/two-proportion tests, chi-square goodness-of-fit and independence, with practical reporting.
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/">Open block</a>
      </div>
    </div>

    <!-- Block 5 -->
    <div class="card lesson-card">
      <h3>
        <a href="/inference/power-sample-size/">Block 5 — Power &amp; Sample Size (Design Thinking)</a>
      </h3>

      <p>
        Understand power, effect size, detectable differences, and how sample size planning improves
        reliability. Think beyond “significant/non-significant.”
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/power-sample-size/">Open block</a>
      </div>
    </div>

    <!-- Block 6 -->
    <div class="card lesson-card">
      <h3>
        <a href="/inference/interpretation-reporting/">Block 6 — Interpretation &amp; Reporting (Evidence, Effect, Uncertainty)</a>
      </h3>

      <p>
        Convert output into correct conclusions: effect sizes, confidence intervals, p-values as graded evidence,
        multiple comparisons intuition, and how to write statistically correct statements.
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/">Open block</a>
      </div>
    </div>

    <!-- Block 7 -->
    <div class="card lesson-card">
      <h3>
        <a href="/inference/assumptions-robustness/">Block 7 — Assumptions &amp; Robustness (What Breaks and What to Do)</a>
      </h3>

      <p>
        Diagnose assumptions (normality, independence, equal variance), understand robustness,
        and learn practical alternatives (transformations, nonparametrics preview, resampling preview).
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/assumptions-robustness/">Open block</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Goal of this unit</h2>
      <ul class="bullets">
        <li>Understand inference as reasoning under uncertainty (not button-clicking)</li>
        <li>Interpret confidence intervals and p-values correctly</li>
        <li>Make statistically valid conclusions and avoid common misconceptions</li>
        <li>Prepare for Applied Statistics and Statistical Modeling</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Publishing strategy</div>
        <div class="mini-body">Lessons are published block-by-block to keep the unit coherent.</div>
      </div>
      <div class="mini">
        <div class="mini-title">Prerequisite</div>
        <div class="mini-body">Complete <strong>Probability</strong> (especially sampling distributions).</div>
      </div>
      <div class="mini">
        <div class="mini-title">Software later</div>
        <div class="mini-body">Examples will later include SPSS/R/Python/Excel workflows.</div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    // ✅ Inference HOME continues the last visited BLOCK (not lessons)
    // Separate key so it never affects other site sections
    var KEY = "esa_continue_inference_last_block_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-inference");
      var label = document.getElementById("continue-reading-inference-label");
      var btn = document.getElementById("continue-reading-inference-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>