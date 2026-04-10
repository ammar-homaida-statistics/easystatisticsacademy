---
layout: default
title: 2. Residual Plots
permalink: /modeling/diagnostics/residual-plots/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces residual plots as the primary visual diagnostic tool.
      Advanced diagnostic techniques will follow in later lessons.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_diagnostics_lesson_v0", JSON.stringify({
    url: "/modeling/diagnostics/residual-plot/",
    label: "Lesson 2 — Residual Plots",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 5</span>
      <span class="badge">Lesson 2</span>
      <span class="badge">Residual Plot</span>
      <span class="badge">Diagnostics</span>
    </div>

    <h1>2. Residual Plots</h1>

    <p class="lead">
      Residual plots are the most important tool for diagnosing regression models.
      They reveal patterns, violations, and problems that are invisible in summary statistics.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/diagnostics/">Back to Block 5</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: core interpretation before advanced diagnostics.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should be able to read and interpret residual plots
    and identify key modeling problems.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A good model produces residuals that look random.
      Any visible pattern indicates a problem.
    </p>
  </div>

  <h2>1) What is a residual plot?</h2>
  <div class="card">
    <p>
      A residual plot shows residuals on the vertical axis
      and predicted values (or a predictor) on the horizontal axis.
    </p>
  </div>

  <h2>2) What we expect to see</h2>
  <div class="card">
    <ul>
      <li>Points scattered randomly</li>
      <li>No visible pattern</li>
      <li>Centered around zero</li>
      <li>Constant spread</li>
    </ul>
  </div>

  <h2>3) What indicates a good model</h2>
  <div class="card">
    <p>
      Residuals behave like random noise.
      There is no structure left unexplained by the model.
    </p>
  </div>

  <h2>4) What indicates problems</h2>
  <div class="card">
    <ul>
      <li>Curved patterns → nonlinearity</li>
      <li>Funnel shape → heteroscedasticity</li>
      <li>Clusters or trends → dependence</li>
      <li>Extreme points → outliers</li>
    </ul>
  </div>

  <h2>5) Why residual plots matter</h2>
  <div class="card">
    <p>
      Residual plots reveal issues that cannot be detected
      using R² or summary statistics alone.
    </p>
  </div>

  <h2>6) Residuals vs fitted values</h2>
  <div class="card">
    <p>
      The most common residual plot uses fitted values on the x-axis,
      showing how errors behave across predictions.
    </p>
  </div>

  <h2>7) Interpretation principle</h2>
  <div class="card">
    <p>
      If you can see a pattern, the model is missing something.
    </p>
  </div>

  <h2>8) Common mistake</h2>
  <div class="card">
    <p>
      A high R² does not guarantee a good model.
      Residual plots must always be checked.
    </p>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Residual plots are essential for validating model assumptions
      and ensuring reliable conclusions.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand residual plots</li>
      <li>Identify good vs bad patterns</li>
      <li>Link patterns to assumptions</li>
      <li>Detect modeling problems visually</li>
      <li>Prepare for specific violations</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now focus on nonlinearity,
      one of the most common issues revealed by residual plots.
    </p>
    <a class="btn" href="/modeling/diagnostics/nonlinearity/">
      Next lesson: Nonlinearity →
    </a>
  </div>

</section>