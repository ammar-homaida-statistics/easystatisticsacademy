---
layout: default
title: 4. Heteroscedasticity
permalink: /modeling/diagnostics/heteroscedasticity/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on detecting heteroscedasticity using residual plots.
      Formal tests and corrections will be developed later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_diagnostics_lesson_v0", JSON.stringify({
    url: "/modeling/diagnostics/heteroscedasticity/",
    label: "Lesson 4 — Heteroscedasticity",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 5</span>
      <span class="badge">Lesson 4</span>
      <span class="badge">Heteroscedasticity</span>
      <span class="badge">Variance</span>
    </div>

    <h1>4. Heteroscedasticity</h1>

    <p class="lead">
      Heteroscedasticity occurs when the variability of residuals changes across levels of the predictors.
      It is one of the most common problems detected using residual plots.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/diagnostics/">Back to Block 5</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: visual detection before formal testing.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should be able to identify heteroscedasticity
    and understand its impact on regression models.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Residual spread should be constant. If it changes, the model violates a key assumption.
    </p>
  </div>

  <h2>1) What is heteroscedasticity?</h2>
  <div class="card">
    <p>
      Heteroscedasticity means that the variance of residuals is not constant:
    </p>
    <p><strong>Var(ε | X) ≠ constant</strong></p>
  </div>

  <h2>2) How to detect it</h2>
  <div class="card">
    <p>
      Use a residual plot:
    </p>
    <ul>
      <li>Look for changing spread</li>
      <li>Check if variability increases or decreases</li>
    </ul>
  </div>

  <h2>3) Typical patterns</h2>
  <div class="card">
    <ul>
      <li>Funnel shape (increasing variance)</li>
      <li>Reverse funnel (decreasing variance)</li>
      <li>Uneven scatter</li>
    </ul>
  </div>

  <h2>4) Why it is a problem</h2>
  <div class="card">
    <ul>
      <li>Standard errors become unreliable</li>
      <li>Confidence intervals become incorrect</li>
      <li>Hypothesis tests may be misleading</li>
    </ul>
  </div>

  <h2>5) What is NOT affected</h2>
  <div class="card">
    <p>
      Coefficient estimates may still be unbiased,
      but their uncertainty is misestimated.
    </p>
  </div>

  <h2>6) Common causes</h2>
  <div class="card">
    <ul>
      <li>Scale effects (larger values → more variability)</li>
      <li>Missing variables</li>
      <li>Incorrect model form</li>
    </ul>
  </div>

  <h2>7) Fixing heteroscedasticity</h2>
  <div class="card">
    <ul>
      <li>Transform variables (log, sqrt)</li>
      <li>Use weighted regression</li>
      <li>Use robust standard errors</li>
    </ul>
  </div>

  <h2>8) Common mistake</h2>
  <div class="card">
    <p>
      Ignoring changing variance because the model “looks fine”.
    </p>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Heteroscedasticity directly affects the reliability of statistical conclusions.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Detect heteroscedasticity visually</li>
      <li>Recognize common patterns</li>
      <li>Understand its effect on inference</li>
      <li>Know basic correction methods</li>
      <li>Prepare for outlier diagnostics</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now examine outliers in a diagnostic context,
      focusing on how they appear and affect models.
    </p>
    <a class="btn" href="/modeling/diagnostics/outliers/">
      Next lesson: Outliers →
    </a>
  </div>

</section>