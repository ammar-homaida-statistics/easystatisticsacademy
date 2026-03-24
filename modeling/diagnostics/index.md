---
layout: default
title: Block 5 — Diagnostics
permalink: /modeling/diagnostics/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; line-height:1.6;">
        This block focuses on diagnosing regression models using visual tools
        and quantitative measures. Diagnostics connect assumptions to real data
        and reveal when models fail.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_last_block_v0", JSON.stringify({
    url: "/modeling/diagnostics/",
    label: "Block 5 — Diagnostics",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Diagnostics</span>
        <span class="badge">Residuals</span>
        <span class="badge">Influence</span>
      </div>

      <h1>Block 5 — Diagnostics</h1>

      <p class="lead">
        Diagnostics allow us to check whether a model is trustworthy.
        This block teaches how to use residuals, plots, and influence measures
        to evaluate model quality and detect problems.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/modeling/">Back to Statistical Modeling</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is fixed. Content will expand without changing order.
      </p>

    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0;">

          <li><strong>Residual analysis</strong><span class="meta">Core diagnostic tool</span></li>
          <li><strong>Diagnostic plots</strong><span class="meta">Visual model checking</span></li>
          <li><strong>Outliers</strong><span class="meta">Unusual observations</span></li>
          <li><strong>Leverage</strong><span class="meta">Extreme predictor values</span></li>
          <li><strong>Influence</strong><span class="meta">Impact on model estimates</span></li>
          <li><strong>Cook’s distance</strong><span class="meta">Combined influence measure</span></li>
          <li><strong>Practical workflow</strong><span class="meta">How to diagnose models step-by-step</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-diagnostics" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-diagnostics-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-diagnostics-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Diagnostics are introduced visually first, then refined into formal tools
      for identifying specific modeling problems.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/modeling/diagnostics/residuals/">1. Residuals: The Core Idea</a></h3>
      <p>What residuals represent and why they are central to diagnostics.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/diagnostics/residuals/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/diagnostics/residual-plots/">2. Residual Plots</a></h3>
      <p>Using residual plots to detect patterns and violations.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/diagnostics/residual-plots/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/diagnostics/nonlinearity/">3. Detecting Nonlinearity</a></h3>
      <p>How patterns in residuals reveal incorrect model form.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/diagnostics/nonlinearity/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/diagnostics/heteroscedasticity/">4. Detecting Heteroscedasticity</a></h3>
      <p>Identifying non-constant variance using residual plots.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/diagnostics/heteroscedasticity/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/diagnostics/outliers/">5. Outliers</a></h3>
      <p>Identifying observations with unusual response values.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/diagnostics/outliers/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/diagnostics/leverage/">6. Leverage</a></h3>
      <p>Points with extreme predictor values and their role.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/diagnostics/leverage/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/diagnostics/influence/">7. Influence</a></h3>
      <p>When observations strongly affect model estimates.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/diagnostics/influence/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/diagnostics/cooks-distance/">8. Cook’s Distance</a></h3>
      <p>A combined measure of leverage and residual size.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/diagnostics/cooks-distance/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/diagnostics/diagnostic-workflow/">9. Diagnostic Workflow</a></h3>
      <p>A practical step-by-step approach to checking models.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/diagnostics/diagnostic-workflow/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 5</h2>
      <ul class="bullets">
        <li>Use residuals to evaluate model quality</li>
        <li>Interpret diagnostic plots correctly</li>
        <li>Identify outliers, leverage, and influential points</li>
        <li>Understand how model problems appear in data</li>
        <li>Apply a structured diagnostic workflow</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/modeling/model-fit-comparison/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 6 — Model Fit & Comparison</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_modeling_diagnostics_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-diagnostics");
    var label = document.getElementById("continue-reading-diagnostics-label");
    var btn = document.getElementById("continue-reading-diagnostics-btn");

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>