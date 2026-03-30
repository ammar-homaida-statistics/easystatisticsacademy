---
layout: default
title: 1. Residuals
permalink: /modeling/diagnostics/residuals/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces residuals as the central tool for diagnosing regression models.
      Visualization and formal diagnostics will follow in the next lessons.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_diagnostics_lesson_v0", JSON.stringify({
    url: "/modeling/diagnostics/residuals/",
    label: "Lesson 1 — Residuals",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 5</span>
      <span class="badge">Lesson 1</span>
      <span class="badge">Residuals</span>
      <span class="badge">Diagnostics</span>
    </div>

    <h1>1. Residuals</h1>

    <p class="lead">
      Residuals are the foundation of regression diagnostics.
      They represent the difference between observed and predicted values,
      revealing how well the model captures the data.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/diagnostics/">Back to Block 5</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding before visual diagnostics.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what residuals are,
    how they are computed, and why they are essential for model evaluation.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A residual is the difference between the observed value and the predicted value:
    </p>
    <p><strong>Residual = Observed − Predicted</strong></p>
  </div>

  <h2>1) What is a residual?</h2>
  <div class="card">
    <p>
      For each observation:
    </p>
    <p><strong>e = y − ŷ</strong></p>
    <p>
      It measures how far the model's prediction is from the actual value.
    </p>
  </div>

  <h2>2) Interpretation</h2>
  <div class="card">
    <ul>
      <li>Positive residual → model underestimates</li>
      <li>Negative residual → model overestimates</li>
      <li>Zero residual → perfect prediction</li>
    </ul>
  </div>

  <h2>3) Why residuals matter</h2>
  <div class="card">
    <p>
      Residuals contain the information not explained by the model.
      They reveal whether the model assumptions are satisfied.
    </p>
  </div>

  <h2>4) Residuals vs errors</h2>
  <div class="card">
    <p>
      Residuals are estimates of the true errors.
      True errors are unobservable; residuals are what we can compute.
    </p>
  </div>

  <h2>5) Good model behavior</h2>
  <div class="card">
    <ul>
      <li>Residuals are centered around zero</li>
      <li>No clear patterns</li>
      <li>Constant spread</li>
    </ul>
  </div>

  <h2>6) Bad model behavior</h2>
  <div class="card">
    <ul>
      <li>Systematic patterns</li>
      <li>Trends or curves</li>
      <li>Unequal spread</li>
    </ul>
  </div>

  <h2>7) Residuals and assumptions</h2>
  <div class="card">
    <ul>
      <li>Linearity → no pattern</li>
      <li>Independence → no structure</li>
      <li>Homoscedasticity → constant spread</li>
      <li>Normality → symmetric distribution</li>
    </ul>
  </div>

  <h2>8) Residuals and model fit</h2>
  <div class="card">
    <p>
      Residuals help evaluate how well the model captures the underlying relationship,
      beyond summary statistics like R².
    </p>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Residuals are the primary tool for diagnosing model problems
      and improving model quality.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define residuals clearly</li>
      <li>Interpret residual values</li>
      <li>Distinguish residuals vs errors</li>
      <li>Understand their diagnostic role</li>
      <li>Prepare for residual plots</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now visualize residuals using residual plots,
      the most important diagnostic tool in regression.
    </p>
    <a class="btn" href="/modeling/diagnostics/residual-plots/">
      Next lesson: Residual Plots →
    </a>
  </div>

</section>