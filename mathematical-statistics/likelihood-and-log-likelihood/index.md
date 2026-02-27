---
layout: default
title: Likelihood & Log-Likelihood
description: Likelihood functions, log-likelihood, score function, and interpretation.
permalink: /mathematical-statistics/likelihood-and-log-likelihood/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#f3f6ff; border:2px solid #3f51b5; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.6rem;">🚧 This Block Is Under Construction</h2>
      <p style="margin:0; color:#283593; line-height:1.6;">
        This block develops the likelihood framework—the core object used to construct and analyze estimators.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-lesson">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Likelihood</span>
        <span class="badge">Log-likelihood</span>
        <span class="badge">Score</span>
        <span class="badge">Information</span>
      </div>

      <h1>Block 2 — Likelihood & Log-Likelihood</h1>
      <p class="lead">
        Learn likelihood as a function of parameters, and why log-likelihood, score, and information appear naturally.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/">Back: Mathematical Statistics</a>
        <a class="btn" href="/mathematical-statistics/maximum-likelihood-estimation/">Next block: MLE</a>
      </div>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">Recommended lesson order</h2>
        <ol class="quickstart">
          <li><a href="#lessons">Probability vs likelihood</a><span class="meta">Key distinction</span></li>
          <li><a href="#lessons">Likelihood and log-likelihood</a><span class="meta">Practical form</span></li>
          <li><a href="#lessons">Score function</a><span class="meta">Derivative object</span></li>
          <li><a href="#lessons">Observed vs expected information</a><span class="meta">Curvature</span></li>
          <li><a href="#lessons">Regularity preview</a><span class="meta">When theory works</span></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons</h2>
    <p>Lessons are published in order. “Continue reading” resumes your last visited lesson in this block.</p>
  </div>

  <div id="continue-reading-ms-b2" style="display:none; margin-top:0.75rem;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p class="muted-mini" id="continue-reading-ms-b2-label" style="margin:0 0 .75rem 0;"></p>
        <a class="btn" id="continue-reading-ms-b2-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/likelihood-and-log-likelihood/probability-vs-likelihood/">Probability vs likelihood</a></h3>
      <p>Fix the core conceptual confusion: what is random, what is fixed, what changes.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/likelihood-and-log-likelihood/probability-vs-likelihood/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/likelihood-and-log-likelihood/likelihood-and-log-likelihood/">Likelihood and log-likelihood</a></h3>
      <p>Why we work with logs; interpretation via shape and curvature.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/likelihood-and-log-likelihood/likelihood-and-log-likelihood/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/likelihood-and-log-likelihood/score-function/">Score function</a></h3>
      <p>Derivative of log-likelihood and its role in estimation.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/likelihood-and-log-likelihood/score-function/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/likelihood-and-log-likelihood/observed-vs-expected-information/">Observed vs expected information</a></h3>
      <p>Curvature, precision, and the link to Fisher information.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/likelihood-and-log-likelihood/observed-vs-expected-information/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/likelihood-and-log-likelihood/regularity-conditions-preview/">Regularity conditions (preview)</a></h3>
      <p>Why theorems need assumptions; where things break.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/likelihood-and-log-likelihood/regularity-conditions-preview/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<script>
  (function () {
    try {
      localStorage.setItem("esa_continue_ms_last_block_v0", JSON.stringify({
        label: "Block 2 — Likelihood & Log-Likelihood",
        url: "/mathematical-statistics/likelihood-and-log-likelihood/"
      }));
    } catch (e) {}

    var KEY = "esa_continue_ms_likelihood_last_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-ms-b2");
      var label = document.getElementById("continue-reading-ms-b2-label");
      var btn = document.getElementById("continue-reading-ms-b2-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>