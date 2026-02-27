---
layout: default
title: Maximum Likelihood Estimation
description: Constructing estimators via likelihood maximization.
permalink: /mathematical-statistics/maximum-likelihood-estimation/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#f3f6ff; border:2px solid #3f51b5; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.6rem;">🚧 This Block Is Under Construction</h2>
      <p style="margin:0; color:#283593; line-height:1.6;">
        This block develops maximum likelihood estimation (MLE): definition, computation, core properties, and standard examples.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-lesson">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">MLE</span>
        <span class="badge">Optimization</span>
        <span class="badge">Invariance</span>
        <span class="badge">Examples</span>
      </div>

      <h1>Block 3 — Maximum Likelihood Estimation</h1>
      <p class="lead">
        Learn how MLE is defined, how it is computed, and why it has strong theoretical justification.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/">Back: Mathematical Statistics</a>
        <a class="btn" href="/mathematical-statistics/estimator-properties/">Next block: Estimator Properties</a>
      </div>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">Recommended lesson order</h2>
        <ol class="quickstart">
          <li><a href="#lessons">Definition of MLE</a><span class="meta">Core concept</span></li>
          <li><a href="#lessons">Optimization & likelihood equations</a><span class="meta">How to compute</span></li>
          <li><a href="#lessons">Invariance property</a><span class="meta">Transformations</span></li>
          <li><a href="#lessons">Existence & uniqueness</a><span class="meta">When it fails</span></li>
          <li><a href="#lessons">Classic examples</a><span class="meta">Bernoulli/Poisson/Normal</span></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons</h2>
    <p>“Continue reading” resumes your last visited lesson in this block.</p>
  </div>

  <div id="continue-reading-ms-b3" style="display:none; margin-top:0.75rem;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p class="muted-mini" id="continue-reading-ms-b3-label" style="margin:0 0 .75rem 0;"></p>
        <a class="btn" id="continue-reading-ms-b3-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/maximum-likelihood-estimation/definition-of-mle/">Definition of MLE</a></h3>
      <p>MLE as an argmax of likelihood; interpretation and objective.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/maximum-likelihood-estimation/definition-of-mle/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/maximum-likelihood-estimation/finding-mle-by-optimization/">Finding MLE by optimization</a></h3>
      <p>Likelihood equations, derivatives, and numerical optimization.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/maximum-likelihood-estimation/finding-mle-by-optimization/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/maximum-likelihood-estimation/invariance-property-of-mle/">Invariance property of MLE</a></h3>
      <p>How transformations behave under MLE and why it matters.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/maximum-likelihood-estimation/invariance-property-of-mle/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/maximum-likelihood-estimation/existence-and-uniqueness/">Existence and uniqueness</a></h3>
      <p>Multiple maxima, boundary solutions, and non-regular cases.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/maximum-likelihood-estimation/existence-and-uniqueness/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/maximum-likelihood-estimation/mle-examples-bernoulli-poisson-normal/">MLE examples (Bernoulli, Poisson, Normal)</a></h3>
      <p>Compute MLEs and interpret them in standard parametric families.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/maximum-likelihood-estimation/mle-examples-bernoulli-poisson-normal/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<script>
  (function () {
    try {
      localStorage.setItem("esa_continue_ms_last_block_v0", JSON.stringify({
        label: "Block 3 — Maximum Likelihood Estimation",
        url: "/mathematical-statistics/maximum-likelihood-estimation/"
      }));
    } catch (e) {}

    var KEY = "esa_continue_ms_mle_last_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-ms-b3");
      var label = document.getElementById("continue-reading-ms-b3-label");
      var btn = document.getElementById("continue-reading-ms-b3-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>