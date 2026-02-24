<!-- =========================================================
BLOCK 7 — ASSUMPTIONS & ROBUSTNESS
File: /inference/assumptions-robustness/index.md
========================================================= -->
---
layout: default
title: Block 7 — Assumptions & Robustness
description: Learn what can break inference and how to be robust: assumptions vs design, diagnostics (normality, independence, variance), outliers/influence, bootstrap, and sensitivity analysis.
permalink: /inference/assumptions-robustness/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block teaches the <strong>robustness mindset</strong>:
        inference depends on assumptions and design. You will learn how to identify
        what assumptions you are using, how to diagnose violations, and what alternatives
        to use when assumptions do not hold.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/",
      label: "Block 7 — Assumptions & Robustness",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Assumptions</span>
        <span class="badge">Diagnostics</span>
        <span class="badge">Robustness</span>
      </div>

      <h1>Block 7 — Assumptions &amp; Robustness</h1>
      <p class="lead">
        Good inference is not just formulas — it’s <strong>validity</strong>.
        This block shows what can break inference (dependence, non-normality, unequal variance,
        outliers, model misspecification) and how to respond using diagnostics and robust alternatives.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">Back to Statistical Inference</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will expand without changing URLs or order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Assumptions map</strong><span class="meta">What each method requires</span></li>
          <li style="margin:.35rem 0;"><strong>Design vs model</strong><span class="meta">Sampling/assignment vs distributional assumptions</span></li>
          <li style="margin:.35rem 0;"><strong>Diagnostics</strong><span class="meta">Normality, independence, variance structure</span></li>
          <li style="margin:.35rem 0;"><strong>Outliers & influence</strong><span class="meta">When a few points drive results</span></li>
          <li style="margin:.35rem 0;"><strong>Robust tools</strong><span class="meta">Nonparametric, robust SE, bootstrap</span></li>
          <li style="margin:.35rem 0;"><strong>Sensitivity</strong><span class="meta">How stable is your conclusion?</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-block7" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block7-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block7-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons are published in order to keep the robustness toolkit coherent.
      The list below is the permanent structure for this block.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/inference/assumptions-robustness/assumptions-vs-robustness-mindset/">1. Assumptions vs Robustness: The Mindset</a></h3>
      <p>Why assumptions exist, what “robust” means, and how to think when assumptions are only approximately true.</p>
      <div class="pill-row"><a class="btn btn-outline" href="/inference/assumptions-robustness/assumptions-vs-robustness-mindset/">Open lesson</a></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/">2. Model Assumptions vs Design Assumptions</a></h3>
      <p>What sampling/assignment guarantees vs what distributional/model assumptions add — and which is more important.</p>
      <div class="pill-row"><a class="btn btn-outline" href="/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/">Open lesson</a></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/assumptions-robustness/checking-normality-what-and-why/">3. Checking Normality: What and Why</a></h3>
      <p>What “normality” actually refers to (data vs residuals vs estimator), and how to check it responsibly.</p>
      <div class="pill-row"><a class="btn btn-outline" href="/inference/assumptions-robustness/checking-normality-what-and-why/">Open lesson</a></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/assumptions-robustness/independence-and-dependence/">4. Independence and Dependence</a></h3>
      <p>Why dependence breaks standard errors and how clustering/time/order create dependence.</p>
      <div class="pill-row"><a class="btn btn-outline" href="/inference/assumptions-robustness/independence-and-dependence/">Open lesson</a></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/assumptions-robustness/heteroscedasticity-variance-issues/">5. Heteroscedasticity and Variance Issues</a></h3>
      <p>Unequal variance patterns, what they do to inference, and the idea of robust standard errors.</p>
      <div class="pill-row"><a class="btn btn-outline" href="/inference/assumptions-robustness/heteroscedasticity-variance-issues/">Open lesson</a></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/assumptions-robustness/outliers-and-influence/">6. Outliers and Influence</a></h3>
      <p>Outliers vs leverage vs influence: when a small number of points controls the conclusion.</p>
      <div class="pill-row"><a class="btn btn-outline" href="/inference/assumptions-robustness/outliers-and-influence/">Open lesson</a></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/assumptions-robustness/robust-alternatives-nonparametric/">7. Robust Alternatives and Nonparametric Thinking</a></h3>
      <p>What to do when assumptions fail: rank-based methods, transformations, and robust summaries.</p>
      <div class="pill-row"><a class="btn btn-outline" href="/inference/assumptions-robustness/robust-alternatives-nonparametric/">Open lesson</a></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/assumptions-robustness/bootstrap-as-robust-tool/">8. Bootstrap as a Robust Tool</a></h3>
      <p>Bootstrap logic: using resampling to estimate uncertainty when formulas are fragile.</p>
      <div class="pill-row"><a class="btn btn-outline" href="/inference/assumptions-robustness/bootstrap-as-robust-tool/">Open lesson</a></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/assumptions-robustness/sensitivity-analysis-and-specification/">9. Sensitivity Analysis and Specification</a></h3>
      <p>How stable is your conclusion? Change reasonable choices and check whether results persist.</p>
      <div class="pill-row"><a class="btn btn-outline" href="/inference/assumptions-robustness/sensitivity-analysis-and-specification/">Open lesson</a></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/assumptions-robustness/reporting-assumptions-and-limitations/">10. Reporting Assumptions and Limitations</a></h3>
      <p>How to document assumptions, diagnostics, and robustness checks in a transparent scientific report.</p>
      <div class="pill-row"><a class="btn btn-outline" href="/inference/assumptions-robustness/reporting-assumptions-and-limitations/">Open lesson</a></div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 7</h2>
      <ul class="bullets">
        <li>Identify which assumptions your inference relies on</li>
        <li>Run basic diagnostics and understand their limits</li>
        <li>Use robust alternatives when assumptions fail</li>
        <li>Do sensitivity analysis and report limitations clearly</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next</div>
        <div class="mini-body">
          Return to
          <a href="/inference/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Statistical Inference home</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading Script (lesson-level) -->
<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block7");
      var label = document.getElementById("continue-reading-block7-label");
      var btn = document.getElementById("continue-reading-block7-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>