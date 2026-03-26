---
layout: default
title: 2. Model Structure
permalink: /modeling/multiple-regression/model-structure/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding the structure of multiple regression models.
      Estimation and interpretation details will follow.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_mr_lesson_v0", JSON.stringify({
    url: "/modeling/multiple-regression/model-structure/",
    label: "Lesson 2 — Model Structure",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 3</span>
      <span class="badge">Lesson 2</span>
      <span class="badge">Model Structure</span>
      <span class="badge">Multiple Predictors</span>
    </div>

    <h1>2. Model Structure</h1>

    <p class="lead">
      Multiple regression extends the simple regression model by including
      multiple predictors in a single equation.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/multiple-regression/">Back to Block 3</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: structure and interpretation without heavy notation.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand how a multiple regression model is structured
    and how multiple predictors enter the equation.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Multiple regression models the response variable as a function of several predictors.
    </p>
  </div>

  <h2>1) From simple to multiple regression</h2>
  <div class="card">
    <p>
      Simple regression:
    </p>
    <p><strong>Y = β₀ + β₁X</strong></p>

    <p>
      Multiple regression:
    </p>
    <p><strong>Y = β₀ + β₁X₁ + β₂X₂ + β₃X₃ + ...</strong></p>
  </div>

  <h2>2) Components of the model</h2>
  <div class="card">
    <ul>
      <li><strong>Y</strong> → response variable</li>
      <li><strong>X₁, X₂, ...</strong> → predictors</li>
      <li><strong>β₀</strong> → intercept</li>
      <li><strong>β₁, β₂, ...</strong> → coefficients</li>
    </ul>
  </div>

  <h2>3) Interpretation of coefficients (preview)</h2>
  <div class="card">
    <p>
      Each coefficient represents the effect of a predictor on Y,
      holding other variables constant.
    </p>
  </div>

  <h2>4) Why “holding others constant” matters</h2>
  <div class="card">
    <p>
      In multiple regression, predictors may be related to each other.
      The model separates their individual contributions.
    </p>
  </div>

  <h2>5) Linear structure</h2>
  <div class="card">
    <p>
      The model is linear in the coefficients (β's),
      even if predictors themselves are transformed.
    </p>
  </div>

  <h2>6) Flexibility of the model</h2>
  <div class="card">
    <ul>
      <li>Can include many predictors</li>
      <li>Can include transformed variables</li>
      <li>Can represent complex relationships</li>
    </ul>
  </div>

  <h2>7) Limitations</h2>
  <div class="card">
    <ul>
      <li>Too many predictors can lead to overfitting</li>
      <li>Interpretation becomes more complex</li>
      <li>Requires careful variable selection</li>
    </ul>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Understanding the model structure is essential before interpreting coefficients
      or making conclusions.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Write the multiple regression equation</li>
      <li>Identify model components</li>
      <li>Understand how predictors enter the model</li>
      <li>Understand the role of coefficients</li>
      <li>Prepare for adjusted effects interpretation</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we interpret coefficients correctly in the presence of multiple predictors.
    </p>
    <a class="btn" href="/modeling/multiple-regression/adjusted-effects/">
      Next lesson: Adjusted Effects →
    </a>
  </div>

</section>