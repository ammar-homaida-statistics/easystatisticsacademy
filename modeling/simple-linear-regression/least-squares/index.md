---
layout: default
title: 6. Least Squares
permalink: /modeling/simple-linear-regression/least-squares/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 explains how regression chooses the best-fitting line.
      Formal derivations and matrix methods will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_slr_lesson_v0", JSON.stringify({
    url: "/modeling/simple-linear-regression/least-squares/",
    label: "Lesson 6 — Least Squares",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 2</span>
      <span class="badge">Lesson 6</span>
      <span class="badge">Least Squares</span>
      <span class="badge">Optimization</span>
    </div>

    <h1>6. Least Squares</h1>

    <p class="lead">
      Among all possible lines, regression chooses the one that minimizes
      the total squared residuals. This is the least squares principle.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/simple-linear-regression/">Back to Block 2</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: intuition-first. Focus on understanding the criterion.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand how the regression line
    is chosen and why least squares is used.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      The best regression line is the one that minimizes the sum of squared residuals.
    </p>
  </div>

  <h2>1) Many possible lines</h2>
  <div class="card">
    <p>
      Given a dataset, many different lines could be drawn.
      Each line produces different predictions and residuals.
    </p>
  </div>

  <h2>2) Measuring model error</h2>
  <div class="card">
    <p>
      To choose the best line, we need a way to measure error.
      Residuals provide this measure.
    </p>
  </div>

  <h2>3) Why square the residuals?</h2>
  <div class="card">
    <ul>
      <li>Prevents positive and negative residuals from canceling out</li>
      <li>Penalizes large errors more heavily</li>
      <li>Makes the optimization mathematically convenient</li>
    </ul>
  </div>

  <h2>4) The least squares criterion</h2>
  <div class="card">
    <p>
      The objective is to minimize:
    </p>
    <p><strong>Sum of squared residuals = Σ (Y − Ŷ)²</strong></p>
  </div>

  <h2>5) Best-fitting line</h2>
  <div class="card">
    <p>
      The regression line is chosen so that the total squared distance
      between observed and predicted values is as small as possible.
    </p>
  </div>

  <h2>6) Intuition</h2>
  <div class="card">
    <p>
      The best line balances errors across all data points,
      rather than fitting any single point perfectly.
    </p>
  </div>

  <h2>7) Residuals and least squares</h2>
  <div class="card">
    <p>
      Residuals are the inputs to the least squares criterion.
      Smaller residuals → better model fit.
    </p>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Least squares defines how regression models are fitted.
      It is the foundation for parameter estimation and model comparison.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand why multiple lines are possible</li>
      <li>Define the least squares criterion</li>
      <li>Explain why residuals are squared</li>
      <li>Understand how the best line is selected</li>
      <li>Connect residuals to model fitting</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we quantify how well the model explains variation in the data:
      R².
    </p>
    <a class="btn" href="/modeling/simple-linear-regression/r-squared/">
      Next lesson: R² →
    </a>
  </div>

</section>