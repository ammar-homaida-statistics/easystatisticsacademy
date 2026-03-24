---
layout: default
title: Block 2 — Simple Linear Regression
permalink: /modeling/simple-linear-regression/
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
        This block develops simple linear regression from first principles:
        how relationships are modeled, how coefficients are interpreted,
        and how variation is explained.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_last_block_v0", JSON.stringify({
    url: "/modeling/simple-linear-regression/",
    label: "Block 2 — Simple Linear Regression",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Regression</span>
        <span class="badge">Linear</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>Block 2 — Simple Linear Regression</h1>

      <p class="lead">
        Linear regression is the first full statistical model.
        It connects a predictor to an outcome and introduces
        the key ideas of slope, residuals, and explained variation.
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

          <li><strong>Regression idea</strong><span class="meta">Modeling relationships</span></li>
          <li><strong>Slope</strong><span class="meta">Effect of predictor</span></li>
          <li><strong>Intercept</strong><span class="meta">Baseline value</span></li>
          <li><strong>Residuals</strong><span class="meta">Errors and variation</span></li>
          <li><strong>Least squares</strong><span class="meta">Fitting principle</span></li>
          <li><strong>R²</strong><span class="meta">Explained variation</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-slr" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-slr-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-slr-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons are structured to build regression intuition step-by-step,
      from concept to interpretation.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/modeling/simple-linear-regression/what-is-regression/">1. What Is Regression?</a></h3>
      <p>Regression as modeling relationships, not just fitting a line.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/simple-linear-regression/what-is-regression/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/simple-linear-regression/regression-equation/">2. The Regression Equation</a></h3>
      <p>Understanding the structure: outcome = intercept + slope × predictor.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/simple-linear-regression/regression-equation/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/simple-linear-regression/slope/">3. Slope Interpretation</a></h3>
      <p>How to interpret the effect of one-unit change in the predictor.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/simple-linear-regression/slope/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/simple-linear-regression/intercept/">4. Intercept Interpretation</a></h3>
      <p>Meaning of the baseline value and when it is meaningful.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/simple-linear-regression/intercept/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/simple-linear-regression/residuals/">5. Residuals and Errors</a></h3>
      <p>Observed vs predicted values and the idea of model error.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/simple-linear-regression/residuals/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/simple-linear-regression/least-squares/">6. Least Squares Method</a></h3>
      <p>Why we minimize squared errors and how the line is fitted.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/simple-linear-regression/least-squares/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/simple-linear-regression/r-squared/">7. R² (Explained Variation)</a></h3>
      <p>How much variation the model explains and what R² really means.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/simple-linear-regression/r-squared/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/simple-linear-regression/correlation-vs-regression/">8. Correlation vs Regression</a></h3>
      <p>Relationship between correlation and slope.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/simple-linear-regression/correlation-vs-regression/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/simple-linear-regression/prediction/">9. Prediction Using the Model</a></h3>
      <p>Using regression for prediction and understanding its limits.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/simple-linear-regression/prediction/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 2</h2>
      <ul class="bullets">
        <li>Understand the structure of the regression model</li>
        <li>Interpret slope and intercept correctly</li>
        <li>Understand residuals and model error</li>
        <li>Explain least squares conceptually</li>
        <li>Interpret R² properly</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/modeling/multiple-regression/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 3 — Multiple Regression</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_modeling_slr_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-slr");
    var label = document.getElementById("continue-reading-slr-label");
    var btn = document.getElementById("continue-reading-slr-btn");

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>