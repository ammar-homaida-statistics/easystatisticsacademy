---
layout: default
title: 4. Homoscedasticity
permalink: /modeling/assumptions/homoscedasticity/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding constant variance of residuals.
      Diagnostics and remedies will be developed in later sections.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_assumptions_lesson_v0", JSON.stringify({
    url: "/modeling/assumptions/homoscedasticity/",
    label: "Lesson 4 — Homoscedasticity",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 4</span>
      <span class="badge">Lesson 4</span>
      <span class="badge">Homoscedasticity</span>
      <span class="badge">Variance</span>
    </div>

    <h1>4. Homoscedasticity</h1>

    <p class="lead">
      The homoscedasticity assumption requires that the variance of residuals
      is constant across all levels of the predictors.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/assumptions/">Back to Block 4</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding of variance consistency.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what homoscedasticity means,
    how violations occur, and why it matters.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      The spread of residuals should remain approximately constant across all predicted values.
    </p>
  </div>

  <h2>1) What is homoscedasticity?</h2>
  <div class="card">
    <p>
      Homoscedasticity means that the variance of the errors is constant:
    </p>
    <p><strong>Var(ε | X) = constant</strong></p>
  </div>

  <h2>2) What is heteroscedasticity?</h2>
  <div class="card">
    <p>
      When the variance changes across levels of X,
      the data exhibit heteroscedasticity.
    </p>
  </div>

  <h2>3) Example</h2>
  <div class="card">
    <p>
      In income data:
    </p>
    <ul>
      <li>Low-income observations → small variability</li>
      <li>High-income observations → large variability</li>
    </ul>
  </div>

  <h2>4) How violations appear</h2>
  <div class="card">
    <p>
      Residual plots show patterns such as:
    </p>
    <ul>
      <li>Funnel shape</li>
      <li>Increasing or decreasing spread</li>
    </ul>
  </div>

  <h2>5) Why it is a problem</h2>
  <div class="card">
    <ul>
      <li>Standard errors become unreliable</li>
      <li>Confidence intervals become inaccurate</li>
      <li>Hypothesis tests may be misleading</li>
    </ul>
  </div>

  <h2>6) What is NOT affected</h2>
  <div class="card">
    <p>
      Coefficient estimates themselves may still be unbiased,
      but their reliability is affected.
    </p>
  </div>

  <h2>7) Common causes</h2>
  <div class="card">
    <ul>
      <li>Scale effects (larger values → more variability)</li>
      <li>Missing variables</li>
      <li>Incorrect model form</li>
    </ul>
  </div>

  <h2>8) Fixing heteroscedasticity</h2>
  <div class="card">
    <ul>
      <li>Transform variables (e.g., log)</li>
      <li>Use weighted regression</li>
      <li>Improve model specification</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Homoscedasticity ensures that uncertainty is measured correctly,
      which is essential for reliable statistical conclusions.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define homoscedasticity</li>
      <li>Recognize heteroscedasticity</li>
      <li>Understand consequences of violations</li>
      <li>Interpret residual patterns</li>
      <li>Prepare for normality assumption</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now examine the normality assumption of residuals.
    </p>
    <a class="btn" href="/modeling/assumptions/normality/">
      Next lesson: Normality →
    </a>
  </div>

</section>