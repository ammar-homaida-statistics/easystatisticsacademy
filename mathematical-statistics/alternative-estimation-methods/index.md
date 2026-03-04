---
layout: default
title: Alternative Estimation Methods
description: Method of moments and estimation approaches beyond maximum likelihood.
permalink: /mathematical-statistics/alternative-estimation-methods/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#f3f6ff; border:2px solid #3f51b5; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.6rem;">🚧 This Block Is Under Construction</h2>
      <p style="margin:0; color:#283593; line-height:1.6;">
        This block introduces estimation approaches beyond MLE, starting with method of moments
        and leaving clean space for future additions (robust, Bayesian, shrinkage).
      </p>
    </div>
  </div>
</section>

<section class="hero hero-lesson">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Moments</span>
        <span class="badge">Estimating equations</span>
        <span class="badge">Bayesian preview</span>
        <span class="badge">Robust preview</span>
      </div>

      <h1>Block 7 — Alternative Estimation Methods</h1>
      <p class="lead">
        Expand your estimation toolbox beyond likelihood maximization, starting with method of moments.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/">Back: Mathematical Statistics</a>
        <a class="btn" href="/inference/">Next: Statistical Inference</a>
      </div>

      <p class="muted-mini">
        This block is intentionally designed as an expandable “methods shelf” for future growth.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">Recommended lesson order</h2>
        <ol class="quickstart">
          <li><a href="#lessons">Method of moments</a><span class="meta">Core alternative</span></li>
          <li><a href="#lessons">Estimating equations (preview)</a><span class="meta">Generalization</span></li>
          <li><a href="#lessons">Bayesian point estimation (preview)</a><span class="meta">Different paradigm</span></li>
          <li><a href="#lessons">Shrinkage intuition (preview)</a><span class="meta">Bias–variance tradeoff</span></li>
          <li><a href="#lessons">Robustness (preview)</a><span class="meta">When models fail</span></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons</h2>
    <p>Lessons are clickable. “Continue reading” resumes your last visited lesson in this block.</p>
  </div>

  <div id="continue-reading-ms-b7" style="display:none; margin-top:0.75rem;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p class="muted-mini" id="continue-reading-ms-b7-label" style="margin:0 0 .75rem 0;"></p>
        <a class="btn" id="continue-reading-ms-b7-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/alternative-estimation-methods/method-of-moments/">Method of moments</a></h3>
      <p>Construct estimators by matching theoretical and sample moments.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/method-of-moments/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/alternative-estimation-methods/estimating-equations-preview/">Estimating equations (preview)</a></h3>
      <p>Generalize estimation via equations; motivation and examples preview.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/estimating-equations-preview/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/alternative-estimation-methods/bayesian-point-estimation-preview/">Bayesian point estimation (preview)</a></h3>
      <p>MAP and posterior mean as estimation targets (conceptual preview).</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/bayesian-point-estimation-preview/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/alternative-estimation-methods/shrinkage-intuition-preview/">Shrinkage intuition (preview)</a></h3>
      <p>Why adding bias can reduce MSE; high-level preview for later modeling.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/shrinkage-intuition-preview/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/alternative-estimation-methods/robustness-preview/">Robustness (preview)</a></h3>
      <p>What happens when assumptions are violated and why robustness matters.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/robustness-preview/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<script>
  (function () {
    try {
      localStorage.setItem("esa_continue_ms_last_block_v0", JSON.stringify({
        label: "Block 7 — Alternative Estimation Methods",
        url: "/mathematical-statistics/alternative-estimation-methods/"
      }));
    } catch (e) {}

    var KEY = "esa_continue_ms_methods_last_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-ms-b7");
      var label = document.getElementById("continue-reading-ms-b7-label");
      var btn = document.getElementById("continue-reading-ms-b7-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>