---
layout: default
title: 5. Outliers (Diagnostics)
permalink: /modeling/diagnostics/outliers/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on identifying outliers using residuals and plots.
      Influence measures will be developed in the following lessons.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_diagnostics_lesson_v0", JSON.stringify({
    url: "/modeling/diagnostics/outliers/",
    label: "Lesson 5 — Outliers (Diagnostics)",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 5</span>
      <span class="badge">Lesson 5</span>
      <span class="badge">Outliers</span>
      <span class="badge">Diagnostics</span>
    </div>

    <h1>5. Outliers (Diagnostics)</h1>

    <p class="lead">
      Outliers are observations with large residuals.
      Detecting them is essential for understanding model behavior and avoiding misleading conclusions.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/diagnostics/">Back to Block 5</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: identifying outliers before influence analysis.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should be able to detect outliers using residuals
    and understand their role in regression diagnostics.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Outliers are observations with unusually large residuals compared to the rest of the data.
    </p>
  </div>

  <h2>1) What is an outlier in diagnostics?</h2>
  <div class="card">
    <p>
      An outlier is an observation where the predicted value is far from the observed value.
    </p>
  </div>

  <h2>2) Residual-based detection</h2>
  <div class="card">
    <ul>
      <li>Large absolute residuals indicate potential outliers</li>
      <li>Compare residuals across observations</li>
    </ul>
  </div>

  <h2>3) Standardized residuals</h2>
  <div class="card">
    <p>
      Residuals are often scaled to detect extreme values more clearly.
    </p>
    <ul>
      <li>|standardized residual| > 2 → potential outlier</li>
      <li>|standardized residual| > 3 → strong outlier</li>
    </ul>
  </div>

  <h2>4) Visual detection</h2>
  <div class="card">
    <ul>
      <li>Residual plots</li>
      <li>Scatter plots with regression line</li>
      <li>Residual vs fitted plots</li>
    </ul>
  </div>

  <h2>5) Important distinction</h2>
  <div class="card">
    <p>
      An outlier has a large residual, but it may not strongly affect the model.
    </p>
  </div>

  <h2>6) Outliers vs influence</h2>
  <div class="card">
    <ul>
      <li>Outlier → large error</li>
      <li>Influential point → changes the model</li>
    </ul>
  </div>

  <h2>7) Why outliers matter</h2>
  <div class="card">
    <ul>
      <li>Can distort interpretation</li>
      <li>Can affect model fit</li>
      <li>Can impact inference</li>
    </ul>
  </div>

  <h2>8) What to do when detected</h2>
  <div class="card">
    <ul>
      <li>Investigate the observation</li>
      <li>Check for data errors</li>
      <li>Assess influence (next lesson)</li>
    </ul>
  </div>

  <h2>9) Common mistake</h2>
  <div class="card">
    <p>
      Removing outliers without justification can bias results.
    </p>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      Outliers provide important information about model fit and data structure.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Detect outliers using residuals</li>
      <li>Use standardized residuals</li>
      <li>Distinguish outliers from influence</li>
      <li>Interpret their impact</li>
      <li>Prepare for leverage analysis</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now examine leverage,
      which identifies points that have unusual predictor values.
    </p>
    <a class="btn" href="/modeling/diagnostics/leverage/">
      Next lesson: Leverage →
    </a>
  </div>

</section>