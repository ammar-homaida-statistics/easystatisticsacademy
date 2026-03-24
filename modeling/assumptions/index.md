---
layout: default
title: Block 4 — Model Assumptions
permalink: /modeling/assumptions/
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
        This block explains the assumptions behind regression models.
        These are not technical details—they determine whether results
        can be trusted and interpreted correctly.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_last_block_v0", JSON.stringify({
    url: "/modeling/assumptions/",
    label: "Block 4 — Model Assumptions",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Assumptions</span>
        <span class="badge">Validity</span>
        <span class="badge">Diagnostics</span>
      </div>

      <h1>Block 4 — Model Assumptions</h1>

      <p class="lead">
        Regression models rely on assumptions. When these assumptions fail,
        interpretation breaks. This block teaches what assumptions mean,
        why they matter, and what happens when they are violated.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/modeling/">Back to Statistical Modeling</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is fixed. Lessons will expand without changing order.
      </p>

    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0;">

          <li><strong>Why assumptions exist</strong><span class="meta">Validity of interpretation</span></li>
          <li><strong>Linearity</strong><span class="meta">Correct functional form</span></li>
          <li><strong>Independence</strong><span class="meta">No dependence between observations</span></li>
          <li><strong>Homoscedasticity</strong><span class="meta">Constant variance of errors</span></li>
          <li><strong>Normality</strong><span class="meta">Distribution of residuals (for inference)</span></li>
          <li><strong>Violations</strong><span class="meta">What breaks and why</span></li>
          <li><strong>Robust thinking</strong><span class="meta">What to do in practice</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-assumptions" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-assumptions-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-assumptions-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Assumptions are introduced conceptually first, then examined one-by-one,
      followed by consequences and practical handling.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/modeling/assumptions/why-assumptions/">1. Why Assumptions Matter</a></h3>
      <p>Why regression requires assumptions and what “valid model” means.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/assumptions/why-assumptions/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/assumptions/linearity/">2. Linearity</a></h3>
      <p>The relationship must be correctly modeled as linear (or transformed).</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/assumptions/linearity/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/assumptions/independence/">3. Independence</a></h3>
      <p>Observations must not influence each other.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/assumptions/independence/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/assumptions/homoscedasticity/">4. Homoscedasticity</a></h3>
      <p>Variance of errors should remain constant across predictor values.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/assumptions/homoscedasticity/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/assumptions/normality/">5. Normality of Residuals</a></h3>
      <p>Required mainly for inference (not for estimation itself).</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/assumptions/normality/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/assumptions/outliers/">6. Outliers and Their Impact</a></h3>
      <p>Extreme points can distort model estimates and interpretation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/assumptions/outliers/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/assumptions/violations/">7. Violations and Consequences</a></h3>
      <p>What goes wrong when assumptions fail.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/assumptions/violations/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/assumptions/robustness/">8. Robustness and Practical Thinking</a></h3>
      <p>Which assumptions matter most and when models still work.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/assumptions/robustness/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 4</h2>
      <ul class="bullets">
        <li>Understand why regression assumptions exist</li>
        <li>Explain each assumption conceptually</li>
        <li>Recognize violations and their consequences</li>
        <li>Distinguish critical vs less critical assumptions</li>
        <li>Think practically about model validity</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/modeling/diagnostics/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 5 — Diagnostics</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_modeling_assumptions_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-assumptions");
    var label = document.getElementById("continue-reading-assumptions-label");
    var btn = document.getElementById("continue-reading-assumptions-btn");

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>