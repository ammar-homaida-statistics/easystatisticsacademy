---
layout: default
title: Mathematical Statistics
description: The theory of estimation: statistical models, likelihood, estimator properties, Fisher information, and asymptotic results.
permalink: /mathematical-statistics/
sidebar: false
---

<!-- HERO -->
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
        Develop the formal theory behind statistical estimation.
        Learn how estimators are constructed, evaluated, and justified
        through likelihood, efficiency, and asymptotic arguments.
      </p>

      <p class="muted-mini">
        7 structured blocks • Theory-focused • Bridge to inference
      </p>

      <div class="hero-actions">
        <a class="btn" href="#blocks">Start Learning</a>
        <a class="btn btn-outline" href="/inference/">Next: Statistical Inference</a>
      </div>

      <div style="background:#eef5ff; border:1px solid #c5cae9; padding:12px 14px; margin:14px 0; border-radius:8px;">
        <strong>📐 Advanced Track</strong> — This unit is mathematically rigorous.
        It focuses on theory, derivations, and formal justification of estimation methods.
      </div>

    </div>

    <div class="hero-panel">
      <div class="panel-card">

        <h2 class="panel-title">Suggested learning order</h2>

        <ol class="quickstart">
          <li>Statistical models</li>
          <li>Likelihood framework</li>
          <li>Maximum likelihood estimation</li>
          <li>Estimator properties</li>
          <li>Fisher information</li>
          <li>Asymptotic theory</li>
          <li>Alternative estimators</li>
        </ol>

      </div>
    </div>

  </div>
</section>

<!-- BLOCKS -->
<section class="section" id="blocks">

  <div class="section-head">
    <h2>Blocks (Unit Structure)</h2>
    <p>
      This unit builds the theoretical foundation of statistical inference.
      Each block develops formal tools used to justify estimation procedures.
    </p>
  </div>

  <!-- CONTINUE READING -->
  <div id="continue-reading-ms" style="display:none; margin-bottom:20px;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p id="continue-reading-ms-label" class="muted-mini"></p>
        <a class="btn" id="continue-reading-ms-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <!-- BLOCK 1 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/statistical-models/">Block 1 — Statistical Models</a></h3>
      <p>
        Formalize parametric models, parameter spaces, identifiability,
        and the assumptions that define a statistical experiment.
      </p>
      <a class="btn btn-outline" href="/mathematical-statistics/statistical-models/">Open block</a>
    </div>

    <!-- BLOCK 2 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/likelihood-and-log-likelihood/">Block 2 — Likelihood Framework</a></h3>
      <p>
        Define likelihood, log-likelihood, score functions,
        and information as the core structure of estimation.
      </p>
      <a class="btn btn-outline" href="/mathematical-statistics/likelihood-and-log-likelihood/">Open block</a>
    </div>

    <!-- BLOCK 3 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/maximum-likelihood-estimation/">Block 3 — Maximum Likelihood Estimation</a></h3>
      <p>
        Derive estimators via likelihood equations and study their theoretical properties.
      </p>
      <a class="btn btn-outline" href="/mathematical-statistics/maximum-likelihood-estimation/">Open block</a>
    </div>

    <!-- BLOCK 4 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/estimator-properties/">Block 4 — Estimator Properties</a></h3>
      <p>
        Analyze bias, variance, mean squared error, consistency,
        and efficiency of estimators.
      </p>
      <a class="btn btn-outline" href="/mathematical-statistics/estimator-properties/">Open block</a>
    </div>

    <!-- BLOCK 5 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/fisher-information-and-efficiency/">Block 5 — Fisher Information & Efficiency</a></h3>
      <p>
        Study Fisher information and the Cramér–Rao lower bound
        as limits of estimator performance.
      </p>
      <a class="btn btn-outline" href="/mathematical-statistics/fisher-information-and-efficiency/">Open block</a>
    </div>

    <!-- BLOCK 6 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/asymptotic-theory/">Block 6 — Asymptotic Theory</a></h3>
      <p>
        Develop large-sample results: consistency, asymptotic normality,
        Slutsky’s theorem, and the delta method.
      </p>
      <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/">Open block</a>
    </div>

    <!-- BLOCK 7 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/alternative-estimation-methods/">Block 7 — Alternative Estimation Methods</a></h3>
      <p>
        Explore method of moments and alternative approaches to estimation.
      </p>
      <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/">Open block</a>
    </div>

  </div>
</section>

<!-- GOAL -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Goal of this unit</h2>
      <ul class="bullets">
        <li>Formalize statistical models and parameter spaces</li>
        <li>Understand likelihood as the core estimation principle</li>
        <li>Evaluate estimators using rigorous criteria</li>
        <li>Derive asymptotic results that justify inference</li>
        <li>Prepare for advanced inference and research work</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Prerequisite</div>
        <div class="mini-body">
          Strong understanding of <strong>Probability</strong>
        </div>
      </div>
      <div class="mini">
        <div class="mini-title">Next</div>
        <div class="mini-body">
          Continue to <strong>Statistical Inference</strong>
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE SCRIPT -->
<script>
(function () {
  try {
    const KEY = "esa_continue_ms_last_block_v0";
    const raw = localStorage.getItem(KEY);
    if (!raw) return;

    const data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    const wrap = document.getElementById("continue-reading-ms");
    const label = document.getElementById("continue-reading-ms-label");
    const btn = document.getElementById("continue-reading-ms-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML = "You last visited: <strong>" + data.label + "</strong>";
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>