---
layout: default
title: 5. Residuals
permalink: /modeling/simple-linear-regression/residuals/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding residuals conceptually.
      Visualization and diagnostics will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_slr_lesson_v0", JSON.stringify({
    url: "/modeling/simple-linear-regression/residuals/",
    label: "Lesson 5 — Residuals",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 2</span>
      <span class="badge">Lesson 5</span>
      <span class="badge">Residuals</span>
      <span class="badge">Model Error</span>
    </div>

    <h1>5. Residuals</h1>

    <p class="lead">
      Residuals measure the difference between observed and predicted values.
      They represent the part of the data that the model does not explain.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/simple-linear-regression/">Back to Block 2</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: intuition-first. Diagnostics come later.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what residuals are,
    how they are calculated, and why they are central to evaluating models.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Residual = observed value − predicted value.
      It represents unexplained variation (noise).
    </p>
  </div>

  <h2>1) Definition</h2>
  <div class="card">
    <p><strong>Residual = Y − Ŷ</strong></p>
    <p>
      Where:
    </p>
    <ul>
      <li><strong>Y</strong> — observed value</li>
      <li><strong>Ŷ</strong> — predicted value from the model</li>
    </ul>
  </div>

  <h2>2) Residuals vs error term</h2>
  <div class="card">
    <ul>
      <li><strong>Error (ε)</strong> — true, unobservable noise</li>
      <li><strong>Residual</strong> — estimated noise from data</li>
    </ul>
    <p>
      Residuals are our observable approximation of ε.
    </p>
  </div>

  <h2>3) Interpretation</h2>
  <div class="card">
    <ul>
      <li><strong>Residual = 0</strong> → perfect prediction</li>
      <li><strong>Positive residual</strong> → model underestimates</li>
      <li><strong>Negative residual</strong> → model overestimates</li>
    </ul>
  </div>

  <h2>4) Residuals on a graph</h2>
  <div class="card">
    <p>
      Residuals are vertical distances between observed points
      and the regression line.
    </p>
  </div>

  <h2>5) Residuals and model quality</h2>
  <div class="card">
    <p>
      Good models produce small and random residuals.
      Patterns in residuals indicate problems in the model.
    </p>
  </div>

  <h2>6) Residuals connect to signal vs noise</h2>
  <div class="card">
    <p>
      Residuals represent the noise that remains after extracting signal.
    </p>
  </div>

  <h2>7) Example</h2>
  <div class="card">
    <p>
      If predicted score = 80 and actual score = 85:
    </p>
    <p><strong>Residual = 85 − 80 = +5</strong></p>
    <p>
      The model underestimated the true value.
    </p>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Residuals are the foundation of:
    </p>
    <ul>
      <li>model evaluation</li>
      <li>diagnostics</li>
      <li>assumption checking</li>
    </ul>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define residuals correctly</li>
      <li>Calculate residuals</li>
      <li>Interpret positive and negative residuals</li>
      <li>Understand residuals as noise</li>
      <li>Recognize their role in model evaluation</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we learn how regression chooses the best line using residuals:
      least squares.
    </p>
    <a class="btn" href="/modeling/simple-linear-regression/least-squares/">
      Next lesson: Least Squares →
    </a>
  </div>

</section>