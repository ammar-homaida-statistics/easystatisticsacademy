---
layout: default
title: Block 6 — Model Fit & Comparison
permalink: /modeling/model-fit-comparison/
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
        This block focuses on evaluating and comparing models.
        It explains how to measure model quality, avoid overfitting,
        and choose models that generalize well.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_last_block_v0", JSON.stringify({
    url: "/modeling/model-fit-comparison/",
    label: "Block 6 — Model Fit & Comparison",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Model Fit</span>
        <span class="badge">Comparison</span>
        <span class="badge">Overfitting</span>
      </div>

      <h1>Block 6 — Model Fit & Comparison</h1>

      <p class="lead">
        A model is only useful if it fits the data well and generalizes to new data.
        This block teaches how to evaluate model quality, compare competing models,
        and avoid common pitfalls such as overfitting.
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

          <li><strong>Model fit</strong><span class="meta">How well the model explains data</span></li>
          <li><strong>R² and adjusted R²</strong><span class="meta">Explained variation</span></li>
          <li><strong>Overfitting</strong><span class="meta">Too complex models</span></li>
          <li><strong>Underfitting</strong><span class="meta">Too simple models</span></li>
          <li><strong>Model comparison</strong><span class="meta">Choosing between alternatives</span></li>
          <li><strong>AIC / BIC</strong><span class="meta">Balancing fit and complexity</span></li>
          <li><strong>Generalization</strong><span class="meta">Performance on new data</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-fit" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-fit-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-fit-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      This block moves from understanding model fit to making informed decisions
      between competing models.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/modeling/model-fit-comparison/what-is-model-fit/">1. What Is Model Fit?</a></h3>
      <p>Understanding what it means for a model to “fit” data.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/model-fit-comparison/what-is-model-fit/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/model-fit-comparison/r-squared/">2. R² (Coefficient of Determination)</a></h3>
      <p>Measuring explained variation and its interpretation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/model-fit-comparison/r-squared/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/model-fit-comparison/adjusted-r-squared/">3. Adjusted R²</a></h3>
      <p>Correcting R² for model complexity.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/model-fit-comparison/adjusted-r-squared/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/model-fit-comparison/overfitting/">4. Overfitting</a></h3>
      <p>When models fit training data too closely and fail elsewhere.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/model-fit-comparison/overfitting/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/model-fit-comparison/underfitting/">5. Underfitting</a></h3>
      <p>When models are too simple to capture real structure.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/model-fit-comparison/underfitting/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/model-fit-comparison/train-vs-test/">6. Training vs Test Performance</a></h3>
      <p>Evaluating models on unseen data.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/model-fit-comparison/train-vs-test/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/model-fit-comparison/model-comparison/">7. Comparing Models</a></h3>
      <p>Choosing between competing models systematically.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/model-fit-comparison/model-comparison/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/model-fit-comparison/aic-bic/">8. AIC and BIC</a></h3>
      <p>Balancing model fit and complexity.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/model-fit-comparison/aic-bic/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/model-fit-comparison/model-selection-thinking/">9. Model Selection Thinking</a></h3>
      <p>Practical decision-making beyond formulas and metrics.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/model-fit-comparison/model-selection-thinking/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 6</h2>
      <ul class="bullets">
        <li>Understand what model fit means</li>
        <li>Interpret R² and adjusted R² correctly</li>
        <li>Recognize overfitting and underfitting</li>
        <li>Compare models using principled criteria</li>
        <li>Make informed model selection decisions</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/modeling/extensions/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 7 — Extensions</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_modeling_fit_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-fit");
    var label = document.getElementById("continue-reading-fit-label");
    var btn = document.getElementById("continue-reading-fit-btn");

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>