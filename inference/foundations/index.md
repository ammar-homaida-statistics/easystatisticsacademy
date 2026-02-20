<!-- =========================================================
BLOCK 1 — INFERENCE FOUNDATIONS
File: /inference/foundations/index.md
========================================================= -->
---
layout: default
title: Block 1 — Inference Foundations
description: Build the core logic of inference: parameters vs statistics, estimators, sampling variability, and standard error as the unit of uncertainty.
permalink: /inference/foundations/
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
        This block builds the foundation of statistical inference: what we estimate, why estimates vary,
        and how uncertainty is quantified using sampling distributions and standard errors.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/",
      label: "Block 1 — Inference Foundations",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Estimation</span>
        <span class="badge">Uncertainty</span>
        <span class="badge">Standard error</span>
      </div>

      <h1>Block 1 — Inference Foundations</h1>
      <p class="lead">
        Inference is the logic of reasoning from a sample to a population under uncertainty.
        This block defines the key objects (parameters, statistics, estimators) and explains
        why estimates vary across samples—introducing standard error as the uncertainty scale.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">Back to Statistical Inference</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Content will expand without changing URLs or order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Parameter vs statistic</strong><span class="meta">Target vs observed quantity</span></li>
          <li style="margin:.35rem 0;"><strong>Estimator</strong><span class="meta">Rule that maps data → estimate</span></li>
          <li style="margin:.35rem 0;"><strong>Sampling variability</strong><span class="meta">Why estimates change across samples</span></li>
          <li style="margin:.35rem 0;"><strong>Standard error</strong><span class="meta">Uncertainty scale of estimators</span></li>
          <li style="margin:.35rem 0;"><strong>Bias/variance intuition</strong><span class="meta">Accuracy vs stability</span></li>
          <li style="margin:.35rem 0;"><strong>Inference pipeline</strong><span class="meta">Estimator → SE → CI/test</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading (lesson-level placeholder key for this block) -->
<section class="section" id="continue-reading-block1" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block1-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block1-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      This block will be expanded lesson-by-lesson. Links will appear when lessons are published.
      The order will remain stable.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3>Lesson placeholders</h3>
      <p>Coming soon. This area will contain the permanent lesson list for this block.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <div class="card lesson-card">
      <h3>Software examples later</h3>
      <p>SPSS / R / Python / Excel will be added after the conceptual core is stable.</p>
      <div class="pill-row"><span class="badge">Planned</span></div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 1</h2>
      <ul class="bullets">
        <li>Define parameters, statistics, and estimators precisely</li>
        <li>Explain why estimates vary across samples</li>
        <li>Interpret standard error as the uncertainty unit</li>
        <li>Describe the estimator → SE → CI/test pipeline</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/confidence-intervals/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 2 — Confidence Intervals</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading Script (lesson-level) -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block1");
      var label = document.getElementById("continue-reading-block1-label");
      var btn = document.getElementById("continue-reading-block1-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>