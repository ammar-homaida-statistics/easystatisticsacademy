---
layout: default
title: 9. Prediction Using Regression
permalink: /modeling/simple-linear-regression/prediction/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on prediction logic using regression.
      Uncertainty and prediction intervals will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_slr_lesson_v0", JSON.stringify({
    url: "/modeling/simple-linear-regression/prediction/",
    label: "Lesson 9 — Prediction",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 2</span>
      <span class="badge">Lesson 9</span>
      <span class="badge">Prediction</span>
      <span class="badge">Application</span>
    </div>

    <h1>9. Prediction Using Regression</h1>

    <p class="lead">
      Regression models can be used to predict outcomes,
      but predictions always include uncertainty and limitations.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/simple-linear-regression/">Back to Block 2</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding of prediction before formal intervals.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand how regression is used for prediction,
    and why predictions are inherently uncertain.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A regression model provides an expected value of Y for a given X,
      not an exact outcome.
    </p>
  </div>

  <h2>1) How prediction works</h2>
  <div class="card">
    <p>
      Given a model:
    </p>
    <p><strong>Y = β₀ + β₁X</strong></p>
    <p>
      We can plug in a value of X to obtain a predicted value of Y.
    </p>
  </div>

  <h2>2) Example</h2>
  <div class="card">
    <p>
      If the model is:
    </p>
    <p><strong>Score = 50 + 5 × Hours</strong></p>
    <p>
      For 4 hours of study:
    </p>
    <p><strong>Predicted score = 70</strong></p>
  </div>

  <h2>3) Prediction is not exact</h2>
  <div class="card">
    <p>
      Real data contain noise. The predicted value is the average expected outcome,
      not a guaranteed value.
    </p>
  </div>

  <h2>4) Residuals and prediction error</h2>
  <div class="card">
    <p>
      The difference between actual and predicted values is the prediction error (residual).
    </p>
  </div>

  <h2>5) Interpolation vs extrapolation</h2>
  <div class="card">
    <ul>
      <li><strong>Interpolation</strong> → predicting within observed data range (safer)</li>
      <li><strong>Extrapolation</strong> → predicting outside data range (risky)</li>
    </ul>
  </div>

  <h2>6) Why predictions can fail</h2>
  <div class="card">
    <ul>
      <li>Model is misspecified</li>
      <li>Important variables are missing</li>
      <li>Assumptions are violated</li>
      <li>Extrapolation beyond data</li>
    </ul>
  </div>

  <h2>7) Prediction vs explanation</h2>
  <div class="card">
    <p>
      A model can predict well without explaining causality,
      and explain relationships without predicting accurately.
    </p>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Prediction is widely used in real applications,
      but misuse leads to overconfidence and incorrect decisions.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Use regression for prediction</li>
      <li>Understand prediction as expected value</li>
      <li>Distinguish interpolation vs extrapolation</li>
      <li>Recognize sources of prediction error</li>
      <li>Avoid overconfidence in predictions</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we extend regression to multiple predictors,
      allowing more realistic modeling.
    </p>
    <a class="btn" href="/modeling/multiple-regression/">
      Go to Block 3 — Multiple Regression →
    </a>
  </div>

</section>