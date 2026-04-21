---
layout: default
title: Statistical Modeling
description: Learn statistical modeling correctly: regression, assumptions, diagnostics, interpretation, model comparison, and responsible modeling practice.
permalink: /modeling/
sidebar: false
---

<!-- HERO -->
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
        Learn how statistical models represent relationships in data — using regression,
        assumptions, diagnostics, and correct interpretation.
      </p>

      <p class="muted-mini">
        7 structured blocks • Concept-first • Built on inference
      </p>

      <div class="hero-actions">
        <a class="btn" href="#blocks">Start Learning</a>
        <a class="btn btn-outline" href="/software/">Next: Software</a>
      </div>

      <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
        <strong>🚧 Under Construction</strong> — This unit is being developed block-by-block
        with strong emphasis on interpretation and correct modeling practice.
      </div>

    </div>

    <div class="hero-panel">
      <div class="panel-card">

        <h2 class="panel-title">Suggested learning order</h2>

        <ol class="quickstart">
          <li>Modeling foundations</li>
          <li>Simple regression</li>
          <li>Multiple regression</li>
          <li>Model assumptions</li>
          <li>Diagnostics</li>
          <li>Model evaluation</li>
          <li>Extensions</li>
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
      Follow the blocks in order. Each block builds your ability to model
      relationships and interpret them correctly.
    </p>
  </div>

  <!-- CONTINUE READING -->
  <div id="continue-reading-modeling" style="display:none; margin-bottom:20px;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p id="continue-reading-modeling-label" class="muted-mini"></p>
        <a class="btn" id="continue-reading-modeling-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <!-- BLOCK 1 -->
    <div class="card lesson-card">
      <h3><a href="/modeling/foundations/">Block 1 — Modeling Foundations</a></h3>
      <p>What models are: structure vs noise and real-world interpretation.</p>
      <a class="btn btn-outline" href="/modeling/foundations/">Open block</a>
    </div>

    <!-- BLOCK 2 -->
    <div class="card lesson-card">
      <h3><a href="/modeling/simple-linear-regression/">Block 2 — Simple Linear Regression</a></h3>
      <p>Basic regression, slope, and interpretation.</p>
      <a class="btn btn-outline" href="/modeling/simple-linear-regression/">Open block</a>
    </div>

    <!-- BLOCK 3 -->
    <div class="card lesson-card">
      <h3><a href="/modeling/multiple-regression/">Block 3 — Multiple Regression</a></h3>
      <p>Multiple predictors, adjusted effects, and confounding.</p>
      <a class="btn btn-outline" href="/modeling/multiple-regression/">Open block</a>
    </div>

    <!-- BLOCK 4 -->
    <div class="card lesson-card">
      <h3><a href="/modeling/assumptions/">Block 4 — Model Assumptions</a></h3>
      <p>Linearity, independence, variance, and residual behavior.</p>
      <a class="btn btn-outline" href="/modeling/assumptions/">Open block</a>
    </div>

    <!-- BLOCK 5 -->
    <div class="card lesson-card">
      <h3><a href="/modeling/diagnostics/">Block 5 — Diagnostics</a></h3>
      <p>Residuals, influence, and model validation.</p>
      <a class="btn btn-outline" href="/modeling/diagnostics/">Open block</a>
    </div>

    <!-- BLOCK 6 -->
    <div class="card lesson-card">
      <h3><a href="/modeling/model-fit-comparison/">Block 6 — Model Fit & Comparison</a></h3>
      <p>Model evaluation and overfitting vs generalization.</p>
      <a class="btn btn-outline" href="/modeling/model-fit-comparison/">Open block</a>
    </div>

    <!-- BLOCK 7 -->
    <div class="card lesson-card">
      <h3><a href="/modeling/extensions/">Block 7 — Extensions</a></h3>
      <p>Logistic regression and beyond linear models.</p>
      <a class="btn btn-outline" href="/modeling/extensions/">Open block</a>
    </div>

  </div>
</section>

<!-- GOAL -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Goal of this unit</h2>
      <ul class="bullets">
        <li>Understand models as representations of relationships</li>
        <li>Interpret coefficients correctly</li>
        <li>Diagnose assumptions and model validity</li>
        <li>Avoid overfitting and misuse</li>
        <li>Prepare for applied analysis and machine learning</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Next</div>
        <div class="mini-body">
          Continue to <strong>Software</strong>
        </div>
      </div>
      <div class="mini">
        <div class="mini-title">Note</div>
        <div class="mini-body">
          Focus on interpretation, not just equations
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  try {
    const KEY = "esa_continue_modeling_last_block_v0";
    const raw = localStorage.getItem(KEY);
    if (!raw) return;

    const data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    const wrap = document.getElementById("continue-reading-modeling");
    const label = document.getElementById("continue-reading-modeling-label");
    const btn = document.getElementById("continue-reading-modeling-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML = "You last visited: <strong>" + data.label + "</strong>";
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>

<!-- SAVE LAST BLOCK -->
<script>
(function () {
  const KEY = "esa_continue_modeling_last_block_v0";

  const links = document.querySelectorAll('.lesson-card h3 a');

  links.forEach(function(link) {
    link.addEventListener("click", function () {
      localStorage.setItem(KEY, JSON.stringify({
        url: link.getAttribute("href"),
        label: link.textContent.trim()
      }));
    });
  });
})();
</script>