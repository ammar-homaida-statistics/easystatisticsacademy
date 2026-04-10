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
      Version 0 focuses on identifying heteroscedasticity using residual plots
      and understanding its consequences.
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
      Heteroscedasticity occurs when the spread of residuals changes across values.
      It is one of the most common violations revealed by residual plots.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/diagnostics/">Back to Block 5</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: visual diagnosis before formal testing.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should be able to detect heteroscedasticity
    and understand its impact on regression models.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Heteroscedasticity means that the variability of residuals is not constant.
    </p>
  </div>

  <h2>1) What is heteroscedasticity?</h2>
  <div class="card">
    <p>
      The variance of residuals changes depending on the level of the predictor or fitted values.
    </p>
  </div>

  <h2>2) How it appears in residual plots</h2>
  <div class="card">
    <ul>
      <li>Funnel shape (increasing spread)</li>
      <li>Reverse funnel (decreasing spread)</li>
      <li>Uneven clustering of points</li>
    </ul>
  </div>

  <h2>3) What causes it?</h2>
  <div class="card">
    <ul>
      <li>Scale effects (larger values → more variability)</li>
      <li>Missing variables</li>
      <li>Incorrect model form</li>
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
      but their reliability is compromised.
    </p>
  </div>

  <h2>6) Mild vs severe cases</h2>
  <div class="card">
    <ul>
      <li>Mild → results may still be usable</li>
      <li>Severe → inference becomes unreliable</li>
    </ul>
  </div>

  <h2>7) What to do when detected</h2>
  <div class="card">
    <ul>
      <li>Transform variables (e.g., log)</li>
      <li>Use robust standard errors</li>
      <li>Improve model specification</li>
    </ul>
  </div>

  <h2>8) Interpretation rule</h2>
  <div class="card">
    <p>
      If spread changes systematically, the model is not capturing the structure properly.
    </p>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Heteroscedasticity directly affects uncertainty estimates,
      making statistical conclusions unreliable.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Detect heteroscedasticity visually</li>
      <li>Interpret funnel patterns</li>
      <li>Understand its impact on inference</li>
      <li>Distinguish mild vs severe cases</li>
      <li>Know basic remedies</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now examine dependence patterns in residuals,
      which relate to the independence assumption.
    </p>
    <a class="btn" href="/modeling/diagnostics/dependence/">
      Next lesson: Dependence →
    </a>
  </div>

</section>