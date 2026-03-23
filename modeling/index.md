---
layout: default
title: Statistical Modeling
description: Learn statistical modeling correctly: regression, assumptions, diagnostics, interpretation, model comparison, and responsible modeling practice.
permalink: /modeling/
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
        The Statistical Modeling unit is being developed in a structured, block-by-block format.
        Content is published in a fixed pedagogical order to ensure conceptual clarity,
        correct interpretation, and long-term academic stability.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Models</span>
        <span class="badge">Regression</span>
        <span class="badge">Assumptions</span>
        <span class="badge">Diagnostics</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>Statistical Modeling</h1>
      <p class="lead">
        Learn how to build, evaluate, and interpret statistical models correctly.
        Understand regression as a modeling framework—connecting data, assumptions,
        uncertainty, and real-world interpretation.
      </p>

      <div class="hero-actions">
        <a class="btn" href="/inference/">Prerequisite: Statistical inference</a>
        <a class="btn btn-outline" href="/applied-statistics/">Next: Applied Statistics</a>
      </div>

      <p class="muted-mini">
        This landing page is the permanent structure for the Statistical Modeling unit. Lessons are published block-by-block.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">Suggested learning order</h2>
        <ol class="quickstart">
          <li><a href="#blocks">Modeling foundations</a><span class="meta">What models are, why they exist</span></li>
          <li><a href="#blocks">Simple linear regression</a><span class="meta">Form, interpretation, assumptions</span></li>
          <li><a href="#blocks">Multiple regression</a><span class="meta">Confounding, adjusted effects</span></li>
          <li><a href="#blocks">Model assumptions</a><span class="meta">Linearity, independence, variance</span></li>
          <li><a href="#blocks">Diagnostics</a><span class="meta">Residuals, influence, validity</span></li>
          <li><a href="#blocks">Model fit & comparison</a><span class="meta">R², AIC/BIC, overfitting</span></li>
          <li><a href="#blocks">Extensions</a><span class="meta">Logistic regression, generalized models</span></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="blocks">
  <div class="section-head">
    <h2>Blocks (Unit Structure)</h2>
    <p>
      Statistical Modeling is organized into seven blocks. Each block has its own page and a growing set of lessons.
      This structure is stable and designed for long-term expansion without breaking URLs or learning flow.
    </p>
  </div>

  <!-- ✅ Continue reading (Modeling home → last visited BLOCK) -->
  <div id="continue-reading-modeling" style="display:none; margin-top:0.75rem;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p class="muted-mini" id="continue-reading-modeling-label" style="margin:0 0 .75rem 0;"></p>
        <a class="btn" id="continue-reading-modeling-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <!-- Block 1 -->
    <div class="card lesson-card">
      <h3>
        <a href="/modeling/foundations/">Block 1 — Modeling Foundations (What Is a Model?)</a>
      </h3>
      <p>
        Understand what statistical models are: relationships, structure vs noise, parameters,
        and how models connect data to real-world questions.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/foundations/">Open block</a>
      </div>
    </div>

    <!-- Block 2 -->
    <div class="card lesson-card">
      <h3>
        <a href="/modeling/simple-linear-regression/">Block 2 — Simple Linear Regression</a>
      </h3>
      <p>
        Learn the basic regression model: slope, intercept, interpretation,
        and how a single predictor explains variation in an outcome.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/simple-linear-regression/">Open block</a>
      </div>
    </div>

    <!-- Block 3 -->
    <div class="card lesson-card">
      <h3>
        <a href="/modeling/multiple-regression/">Block 3 — Multiple Regression</a>
      </h3>
      <p>
        Extend models to multiple predictors: adjusted effects, confounding,
        and correct interpretation of coefficients.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/multiple-regression/">Open block</a>
      </div>
    </div>

    <!-- Block 4 -->
    <div class="card lesson-card">
      <h3>
        <a href="/modeling/assumptions/">Block 4 — Model Assumptions</a>
      </h3>
      <p>
        Understand the assumptions behind regression models: linearity,
        independence, homoscedasticity, and normality of residuals.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/assumptions/">Open block</a>
      </div>
    </div>

    <!-- Block 5 -->
    <div class="card lesson-card">
      <h3>
        <a href="/modeling/diagnostics/">Block 5 — Model Diagnostics</a>
      </h3>
      <p>
        Diagnose model validity using residual plots, influence measures,
        and practical checks for violations.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/diagnostics/">Open block</a>
      </div>
    </div>

    <!-- Block 6 -->
    <div class="card lesson-card">
      <h3>
        <a href="/modeling/model-fit-comparison/">Block 6 — Model Fit & Comparison</a>
      </h3>
      <p>
        Evaluate models using R², adjusted R², AIC/BIC (conceptually),
        and understand overfitting vs generalization.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/model-fit-comparison/">Open block</a>
      </div>
    </div>

    <!-- Block 7 -->
    <div class="card lesson-card">
      <h3>
        <a href="/modeling/extensions/">Block 7 — Extensions (Beyond Linear Models)</a>
      </h3>
      <p>
        Introduce logistic regression and generalized models,
        preparing for Machine Learning without crossing into it.
      </p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/extensions/">Open block</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Goal of this unit</h2>
      <ul class="bullets">
        <li>Understand models as representations of relationships, not just equations</li>
        <li>Interpret regression coefficients correctly in real-world context</li>
        <li>Diagnose and validate model assumptions</li>
        <li>Compare models responsibly and avoid overfitting</li>
        <li>Prepare for Machine Learning with strong statistical foundations</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Publishing strategy</div>
        <div class="mini-body">Blocks are developed sequentially for conceptual coherence.</div>
      </div>
      <div class="mini">
        <div class="mini-title">Prerequisite</div>
        <div class="mini-body">Complete <strong>Inference</strong>.</div>
      </div>
      <div class="mini">
        <div class="mini-title">Software later</div>
        <div class="mini-body">Implementation will include SPSS/R/Python/Excel.</div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    // ✅ Modeling HOME continues the last visited BLOCK
    var KEY = "esa_continue_modeling_last_block_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-modeling");
      var label = document.getElementById("continue-reading-modeling-label");
      var btn = document.getElementById("continue-reading-modeling-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>