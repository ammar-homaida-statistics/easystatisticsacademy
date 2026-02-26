---
layout: default
title: Mathematical Statistics
description: The theory of estimation: statistical models, likelihood, estimator properties, Fisher information, and asymptotic results.
permalink: /mathematical-statistics/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#eef5ff; border:2px solid #3f51b5; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.8rem; letter-spacing:0.5px;">
        📐 Mathematical Statistics — Theory of Estimation
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#283593; line-height:1.6;">
        This unit develops the formal theory behind statistical estimation.
        We move from statistical models to likelihood, study properties of estimators,
        and derive asymptotic results that power modern inference and machine learning.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Estimation theory</span>
        <span class="badge">Likelihood</span>
        <span class="badge">Fisher information</span>
        <span class="badge">Asymptotics</span>
      </div>

      <h1>Mathematical Statistics</h1>
      <p class="lead">
        Learn how estimators are constructed, evaluated, and justified.
        Understand likelihood, efficiency, and asymptotic normality —
        the theoretical backbone of statistical inference.
      </p>

      <div class="hero-actions">
        <a class="btn" href="/probability/">Prerequisite: Probability</a>
        <a class="btn btn-outline" href="/inference/">Next: Statistical Inference</a>
      </div>

      <p class="muted-mini">
        This unit focuses strictly on estimation theory.
        Hypothesis testing and confidence intervals are developed in the Inference section.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">Suggested learning order</h2>
        <ol class="quickstart">
          <li><a href="#blocks">Statistical models</a><span class="meta">Parametric structure</span></li>
          <li><a href="#blocks">Likelihood framework</a><span class="meta">Core estimation engine</span></li>
          <li><a href="#blocks">Maximum likelihood estimation</a><span class="meta">Constructing estimators</span></li>
          <li><a href="#blocks">Estimator properties</a><span class="meta">Bias, variance, MSE</span></li>
          <li><a href="#blocks">Fisher information & efficiency</a><span class="meta">Efficiency bounds</span></li>
          <li><a href="#blocks">Asymptotic theory</a><span class="meta">Large-sample behavior</span></li>
          <li><a href="#blocks">Alternative estimation methods</a><span class="meta">Beyond MLE</span></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="blocks">
  <div class="section-head">
    <h2>Blocks (Unit Structure)</h2>
    <p>
      Mathematical Statistics is organized into seven structured blocks.
      Each block builds formally on the previous one and prepares you
      for full statistical inference.
    </p>
  </div>

  <!-- ✅ Continue reading (Mathematical Statistics home → last visited BLOCK) -->
  <div id="continue-reading-ms" style="display:none; margin-top:0.75rem;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p class="muted-mini" id="continue-reading-ms-label" style="margin:0 0 .75rem 0;"></p>
        <a class="btn" id="continue-reading-ms-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <!-- Block 1 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/statistical-models/">Block 1 — Statistical Models</a>
      </h3>
      <p>
        Define statistical models rigorously: parametric families,
        parameter spaces, identifiability, and modeling assumptions.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/statistical-models/">Open block</a>
      </div>
    </div>

    <!-- Block 2 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/likelihood-and-log-likelihood/">Block 2 — Likelihood & Log-Likelihood</a>
      </h3>
      <p>
        Develop likelihood, log-likelihood, score function,
        and information concepts central to estimation.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/likelihood-and-log-likelihood/">Open block</a>
      </div>
    </div>

    <!-- Block 3 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/maximum-likelihood-estimation/">Block 3 — Maximum Likelihood Estimation</a>
      </h3>
      <p>
        Construct estimators using likelihood equations and study their properties.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/maximum-likelihood-estimation/">Open block</a>
      </div>
    </div>

    <!-- Block 4 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/estimator-properties/">Block 4 — Estimator Properties</a>
      </h3>
      <p>
        Evaluate estimators using bias, variance, MSE, consistency, and efficiency.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/estimator-properties/">Open block</a>
      </div>
    </div>

    <!-- Block 5 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/fisher-information-and-efficiency/">Block 5 — Fisher Information & Efficiency</a>
      </h3>
      <p>
        Study Fisher information, Cramér–Rao lower bound, and efficiency.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/fisher-information-and-efficiency/">Open block</a>
      </div>
    </div>

    <!-- Block 6 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/asymptotic-theory/">Block 6 — Asymptotic Theory</a>
      </h3>
      <p>
        Analyze consistency, asymptotic normality, Slutsky’s theorem, and delta method.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/">Open block</a>
      </div>
    </div>

    <!-- Block 7 -->
    <div class="card lesson-card">
      <h3>
        <a href="/mathematical-statistics/alternative-estimation-methods/">Block 7 — Alternative Estimation Methods</a>
      </h3>
      <p>
        Explore method of moments and alternative estimation frameworks.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/">Open block</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Goal of this unit</h2>
      <ul class="bullets">
        <li>Formalize statistical models and parameters</li>
        <li>Understand likelihood as the core estimation principle</li>
        <li>Evaluate estimators using rigorous criteria</li>
        <li>Derive asymptotic results that justify inference procedures</li>
        <li>Prepare cleanly for Statistical Inference</li>
      </ul>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_ms_last_block_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-ms");
      var label = document.getElementById("continue-reading-ms-label");
      var btn = document.getElementById("continue-reading-ms-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>