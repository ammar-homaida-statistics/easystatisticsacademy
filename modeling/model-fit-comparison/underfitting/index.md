---
layout: default
title: 5. Underfitting
permalink: /modeling/model-fit-comparison/underfitting/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces underfitting conceptually.
      Bias–variance tradeoff will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_model_fit_lesson_v0", JSON.stringify({
    url: "/modeling/model-fit-comparison/underfitting/",
    label: "Lesson 5 — Underfitting",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 6</span>
      <span class="badge">Lesson 5</span>
      <span class="badge">Underfitting</span>
      <span class="badge">Model Simplicity</span>
    </div>

    <h1>5. Underfitting</h1>

    <p class="lead">
      Underfitting occurs when a model is too simple to capture the underlying pattern in the data,
      leading to poor performance even on training data.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/model-fit-comparison/">Back to Block 6</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding of insufficient model complexity.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what underfitting is
    and how it differs from overfitting.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Underfitting means the model is too simple to represent the true relationship.
    </p>
  </div>

  <h2>1) What is underfitting?</h2>
  <div class="card">
    <p>
      Underfitting occurs when a model fails to capture important patterns in the data.
    </p>
  </div>

  <h2>2) Key symptom</h2>
  <div class="card">
    <ul>
      <li>Poor fit on training data</li>
      <li>Poor performance on new data</li>
    </ul>
  </div>

  <h2>3) Why it happens</h2>
  <div class="card">
    <ul>
      <li>Model too simple</li>
      <li>Missing important variables</li>
      <li>Incorrect model form</li>
    </ul>
  </div>

  <h2>4) Visual intuition</h2>
  <div class="card">
    <p>
      A straight line used to model a curved relationship
      is a typical example of underfitting.
    </p>
  </div>

  <h2>5) Comparison with overfitting</h2>
  <div class="card">
    <ul>
      <li>Underfitting → too simple</li>
      <li>Overfitting → too complex</li>
    </ul>
  </div>

  <h2>6) Impact on model performance</h2>
  <div class="card">
    <p>
      The model fails to capture the signal,
      leading to systematic errors.
    </p>
  </div>

  <h2>7) How to detect it</h2>
  <div class="card">
    <ul>
      <li>Large residuals</li>
      <li>Poor overall fit</li>
      <li>Clear patterns in residuals</li>
    </ul>
  </div>

  <h2>8) Fixing underfitting</h2>
  <div class="card">
    <ul>
      <li>Add relevant predictors</li>
      <li>Use more flexible models</li>
      <li>Include nonlinear terms</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      A model that underfits cannot provide useful insights or predictions.
    </p>
  </div>

  <h2>10) Big picture</h2>
  <div class="card">
    <p>
      Good modeling requires balancing underfitting and overfitting.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand underfitting clearly</li>
      <li>Distinguish from overfitting</li>
      <li>Recognize symptoms</li>
      <li>Identify causes</li>
      <li>Prepare for validation concepts</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now compare training and test performance
      to evaluate model generalization.
    </p>
    <a class="btn" href="/modeling/model-fit-comparison/train-vs-test/">
      Next lesson: Train vs Test →
    </a>
  </div>

</section>