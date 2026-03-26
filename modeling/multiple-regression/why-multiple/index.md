---
layout: default
title: 1. Why Multiple Regression?
permalink: /modeling/multiple-regression/why-multiple/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding why multiple predictors are necessary.
      Formal structure and estimation details will follow.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_mr_lesson_v0", JSON.stringify({
    url: "/modeling/multiple-regression/why-multiple/",
    label: "Lesson 1 — Why Multiple Regression",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 3</span>
      <span class="badge">Lesson 1</span>
      <span class="badge">Multiple Regression</span>
      <span class="badge">Real Data</span>
    </div>

    <h1>1. Why Multiple Regression?</h1>

    <p class="lead">
      Real-world outcomes are influenced by multiple factors.
      Multiple regression allows us to model these effects simultaneously.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/multiple-regression/">Back to Block 3</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual motivation before formal model structure.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand why single-variable models are often insufficient,
    and why multiple predictors are needed in realistic settings.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Most real-world outcomes depend on multiple variables, not just one.
    </p>
  </div>

  <h2>1) Limitation of simple regression</h2>
  <div class="card">
    <p>
      Simple linear regression assumes that one predictor explains the outcome.
    </p>
    <p>
      In reality, this is rarely true.
    </p>
  </div>

  <h2>2) Real-world example</h2>
  <div class="card">
    <p>
      Exam score may depend on:
    </p>
    <ul>
      <li>Hours studied</li>
      <li>Prior knowledge</li>
      <li>Sleep quality</li>
      <li>Stress level</li>
    </ul>
    <p>
      A single predictor cannot capture all these influences.
    </p>
  </div>

  <h2>3) Omitted variable problem</h2>
  <div class="card">
    <p>
      If important variables are missing from the model,
      the estimated relationship can be misleading.
    </p>
  </div>

  <h2>4) Confounding</h2>
  <div class="card">
    <p>
      When variables are related to each other,
      ignoring some of them can distort interpretation.
    </p>
  </div>

  <h2>5) Why multiple regression helps</h2>
  <div class="card">
    <ul>
      <li>Includes multiple predictors</li>
      <li>Separates their effects</li>
      <li>Provides more realistic models</li>
    </ul>
  </div>

  <h2>6) Better explanation and prediction</h2>
  <div class="card">
    <p>
      Using multiple predictors often improves:
    </p>
    <ul>
      <li>Interpretation of relationships</li>
      <li>Prediction accuracy</li>
    </ul>
  </div>

  <h2>7) Important warning</h2>
  <div class="card">
    <ul>
      <li>Adding variables does not guarantee a better model</li>
      <li>Irrelevant variables can add noise</li>
      <li>Model complexity must be justified</li>
    </ul>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Multiple regression is the foundation of most modern statistical modeling
      and many machine learning methods.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand limitations of simple regression</li>
      <li>Recognize need for multiple predictors</li>
      <li>Understand omitted variable bias</li>
      <li>Understand confounding at a basic level</li>
      <li>Prepare for model structure</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we define the structure of a multiple regression model.
    </p>
    <a class="btn" href="/modeling/multiple-regression/model-structure/">
      Next lesson: Model Structure →
    </a>
  </div>

</section>