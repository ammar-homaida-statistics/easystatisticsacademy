---
layout: default
title: Estimator Properties
description: Bias, variance, mean squared error, consistency, and comparing estimators.
permalink: /mathematical-statistics/estimator-properties/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#f3f6ff; border:2px solid #3f51b5; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.6rem;">🚧 This Block Is Under Construction</h2>
      <p style="margin:0; color:#283593; line-height:1.6;">
        This block formalizes how we evaluate estimators: bias, variance, MSE, consistency,
        and principled ways to compare estimators.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-lesson">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Bias</span>
        <span class="badge">Variance</span>
        <span class="badge">MSE</span>
        <span class="badge">Consistency</span>
      </div>

      <h1>Block 4 — Estimator Properties</h1>
      <p class="lead">
        Learn the standard criteria for “good estimation” and how estimator quality is assessed formally.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/">Back: Mathematical Statistics</a>
        <a class="btn" href="/mathematical-statistics/fisher-information-and-efficiency/">Next block: Fisher Information</a>
      </div>

      <p class="muted-mini">
        This block is finite-sample focused; asymptotic properties are developed in Block 6.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">Recommended lesson order</h2>
        <ol class="quickstart">
          <li><a href="#lessons">Bias, variance, and MSE</a><span class="meta">Core evaluation criteria</span></li>
          <li><a href="#lessons">Unbiasedness and bias correction</a><span class="meta">When bias matters</span></li>
          <li><a href="#lessons">Consistency (basic idea)</a><span class="meta">Stabilization with n</span></li>
          <li><a href="#lessons">Efficiency and comparison</a><span class="meta">Choosing between estimators</span></li>
          <li><a href="#lessons">Sufficiency (preview)</a><span class="meta">Information compression</span></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons</h2>
    <p>Lessons will become clickable as they are published. “Continue reading” resumes your last visited lesson in this block.</p>
  </div>

  <!-- ✅ Continue reading (Block → last visited LESSON) -->
  <div id="continue-reading-ms-b4" style="display:none; margin-top:0.75rem;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p class="muted-mini" id="continue-reading-ms-b4-label" style="margin:0 0 .75rem 0;"></p>
        <a class="btn" id="continue-reading-ms-b4-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/estimator-properties/bias-variance-and-mse/">Bias, variance, and MSE</a></h3>
      <p>Decompose error and understand trade-offs between systematic and random error.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/estimator-properties/unbiasedness-and-bias-correction/">Unbiasedness and bias correction</a></h3>
      <p>When unbiasedness is useful, when it is misleading, and how bias correction works.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/estimator-properties/consistency-basic-idea/">Consistency (basic idea)</a></h3>
      <p>Why “converging to the truth” is the key large-n requirement for estimation.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/estimator-properties/efficiency-and-comparing-estimators/">Efficiency and comparing estimators</a></h3>
      <p>How to compare estimators using variance/MSE and formal efficiency notions.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/estimator-properties/sufficiency-preview/">Sufficiency (preview)</a></h3>
      <p>Why some statistics preserve all information about the parameter (preview only).</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>
  </div>
</section>

<script>
  (function () {
    // ✅ Save last visited BLOCK for MS home
    try {
      localStorage.setItem("esa_continue_ms_last_block_v0", JSON.stringify({
        label: "Block 4 — Estimator Properties",
        url: "/mathematical-statistics/estimator-properties/"
      }));
    } catch (e) {}

    // ✅ Block continues last visited LESSON
    var KEY = "esa_continue_ms_properties_last_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-ms-b4");
      var label = document.getElementById("continue-reading-ms-b4-label");
      var btn = document.getElementById("continue-reading-ms-b4-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>