---
layout: default
title: 2. The Regression Equation
permalink: /modeling/simple-linear-regression/regression-equation/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding the structure of the regression equation.
      Estimation and computation will be developed in later lessons.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_slr_lesson_v0", JSON.stringify({
    url: "/modeling/simple-linear-regression/regression-equation/",
    label: "Lesson 2 — Regression Equation",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 2</span>
      <span class="badge">Lesson 2</span>
      <span class="badge">Equation</span>
      <span class="badge">Model Structure</span>
    </div>

    <h1>2. The Regression Equation</h1>

    <p class="lead">
      The regression equation formalizes the relationship between variables.
      It combines structure (signal) and randomness (noise) into a single model.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/simple-linear-regression/">Back to Block 2</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: structure and interpretation first.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand the regression equation,
    its components, and how it represents both signal and noise.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A regression model combines a deterministic part (signal)
      and a random part (noise).
    </p>
  </div>

  <h2>1) The regression equation</h2>
  <div class="card">
    <p><strong>Y = β₀ + β₁X + ε</strong></p>
    <p>
      This is the basic form of simple linear regression.
    </p>
  </div>

  <h2>2) Components of the equation</h2>
  <div class="card">
    <ul>
      <li><strong>Y</strong> — response variable</li>
      <li><strong>X</strong> — predictor variable</li>
      <li><strong>β₀</strong> — intercept</li>
      <li><strong>β₁</strong> — slope</li>
      <li><strong>ε</strong> — random error (noise)</li>
    </ul>
  </div>

  <h2>3) Signal vs noise in the equation</h2>
  <div class="card">
    <p>
      The equation separates the predictable and unpredictable parts:
    </p>
    <ul>
      <li><strong>β₀ + β₁X</strong> — signal (systematic part)</li>
      <li><strong>ε</strong> — noise (random variation)</li>
    </ul>
  </div>

  <h2>4) Deterministic vs random parts</h2>
  <div class="card">
    <p>
      The model consists of:
    </p>
    <ul>
      <li>A deterministic component (relationship between X and Y)</li>
      <li>A random component (unexplained variation)</li>
    </ul>
  </div>

  <h2>5) Expected value interpretation</h2>
  <div class="card">
    <p>
      The expected value of Y given X is:
    </p>
    <p><strong>E(Y | X) = β₀ + β₁X</strong></p>
    <p>
      This represents the average outcome for a given X.
    </p>
  </div>

  <h2>6) Why the error term matters</h2>
  <div class="card">
    <p>
      Without ε, the model would assume perfect prediction.
      The error term reflects uncertainty and variability in real data.
    </p>
  </div>

  <h2>7) Example</h2>
  <div class="card">
    <p>
      Suppose we model exam score using study hours:
    </p>
    <p><strong>Score = β₀ + β₁ × Hours + ε</strong></p>
    <p>
      The model predicts score based on hours,
      but acknowledges randomness through ε.
    </p>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      The regression equation is the foundation of all regression models.
      Understanding it correctly is essential for interpretation and inference.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Write the regression equation correctly</li>
      <li>Identify all components of the model</li>
      <li>Distinguish signal and noise in the equation</li>
      <li>Understand the role of the error term</li>
      <li>Interpret the expected value function</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we interpret one of the most important parameters:
      the slope.
    </p>
    <a class="btn" href="/modeling/simple-linear-regression/slope/">
      Next lesson: Slope →
    </a>
  </div>

</section>