---
layout: default
title: Block 1 — Modeling Foundations
permalink: /modeling/foundations/
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
        This block builds the foundation of statistical modeling:
        what models represent, why we use them, and how relationships
        between variables are formalized.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_last_block_v0", JSON.stringify({
    url: "/modeling/foundations/",
    label: "Block 1 — Modeling Foundations",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Foundations</span>
        <span class="badge">Models</span>
        <span class="badge">Concepts</span>
      </div>

      <h1>Block 1 — Modeling Foundations</h1>

      <p class="lead">
        Statistical modeling is about representing relationships in data.
        This block introduces the core ideas behind models—what they are,
        how they connect variables, and how they differ from simple summaries.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/modeling/">Back to Statistical Modeling</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Content will expand without changing URLs.
      </p>

    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0;">

          <li><strong>What is a model?</strong><span class="meta">Representation of relationships</span></li>
          <li><strong>Variables</strong><span class="meta">Predictors vs outcomes</span></li>
          <li><strong>Signal vs noise</strong><span class="meta">Structure vs randomness</span></li>
          <li><strong>Parameters</strong><span class="meta">What the model estimates</span></li>
          <li><strong>Model purpose</strong><span class="meta">Prediction vs explanation</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-foundations" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-foundations-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-foundations-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons are published sequentially to build strong modeling intuition.
      This structure will not change.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/modeling/foundations/what-is-a-model/">1. What Is a Model?</a></h3>
      <p>Models as simplified representations of reality and relationships between variables.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/foundations/what-is-a-model/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/foundations/variables/">2. Variables and Relationships</a></h3>
      <p>Understanding predictors, outcomes, and how variables interact.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/foundations/variables/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/foundations/signal-noise/">3. Signal vs Noise</a></h3>
      <p>Distinguishing real structure from randomness in data.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/foundations/signal-noise/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/foundations/parameters/">4. Parameters and Estimation</a></h3>
      <p>What parameters represent and how models estimate them.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/foundations/parameters/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/foundations/prediction-vs-explanation/">5. Prediction vs Explanation</a></h3>
      <p>Different goals of modeling and why they matter.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/foundations/prediction-vs-explanation/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 1</h2>
      <ul class="bullets">
        <li>Understand what statistical models represent</li>
        <li>Distinguish predictors and outcomes clearly</li>
        <li>Recognize signal vs noise in data</li>
        <li>Interpret parameters conceptually</li>
        <li>Understand modeling goals (prediction vs explanation)</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/modeling/simple-linear-regression/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 2 — Simple Linear Regression</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_modeling_foundations_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-foundations");
    var label = document.getElementById("continue-reading-foundations-label");
    var btn = document.getElementById("continue-reading-foundations-btn");

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>