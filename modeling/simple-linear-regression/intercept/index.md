---
layout: default
title: 4. Intercept (Interpretation)
permalink: /modeling/simple-linear-regression/intercept/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on correct interpretation of the intercept.
      Real-world meaning and limitations will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_slr_lesson_v0", JSON.stringify({
    url: "/modeling/simple-linear-regression/intercept/",
    label: "Lesson 4 — Intercept",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 2</span>
      <span class="badge">Lesson 4</span>
      <span class="badge">Intercept</span>
      <span class="badge">Interpretation</span>
    </div>

    <h1>4. Intercept (Interpretation)</h1>

    <p class="lead">
      The intercept represents the expected value of the response when the predictor equals zero.
      Its meaning depends strongly on context.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/simple-linear-regression/">Back to Block 2</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: interpretation-first. Context matters more than formula.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what the intercept represents,
    when it is meaningful, and how to interpret it correctly.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      The intercept (β₀) is the expected value of Y when X = 0.
    </p>
  </div>

  <h2>1) Where the intercept appears</h2>
  <div class="card">
    <p><strong>Y = β₀ + β₁X + ε</strong></p>
    <p>
      The intercept is β₀.
    </p>
  </div>

  <h2>2) Basic interpretation</h2>
  <div class="card">
    <p>
      When the predictor X equals zero,
      the expected value of Y is β₀.
    </p>
  </div>

  <h2>3) Example</h2>
  <div class="card">
    <p><strong>Score = 50 + 5 × Hours</strong></p>
    <p>
      Interpretation:
    </p>
    <p>
      When study hours = 0, the expected score is 50.
    </p>
  </div>

  <h2>4) When the intercept is meaningful</h2>
  <div class="card">
    <ul>
      <li>When X = 0 is realistic and observable</li>
      <li>When zero has a real-world interpretation</li>
    </ul>
  </div>

  <h2>5) When the intercept is NOT meaningful</h2>
  <div class="card">
    <ul>
      <li>When X = 0 is outside the data range</li>
      <li>When zero is not meaningful in context</li>
    </ul>
    <p>
      In such cases, the intercept is a mathematical artifact,
      not a useful interpretation.
    </p>
  </div>

  <h2>6) Intercept and graph</h2>
  <div class="card">
    <p>
      The intercept is the point where the regression line crosses the Y-axis.
    </p>
  </div>

  <h2>7) Common mistakes</h2>
  <div class="card">
    <ul>
      <li>Forcing interpretation when X = 0 is unrealistic</li>
      <li>Ignoring units and context</li>
      <li>Overinterpreting the intercept</li>
    </ul>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Understanding the intercept prevents incorrect conclusions
      and helps focus interpretation on meaningful parts of the model.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Identify the intercept in a regression model</li>
      <li>Interpret it correctly when meaningful</li>
      <li>Recognize when it should not be interpreted</li>
      <li>Understand its graphical meaning</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we examine the difference between observed and predicted values:
      residuals.
    </p>
    <a class="btn" href="/modeling/simple-linear-regression/residuals/">
      Next lesson: Residuals →
    </a>
  </div>

</section>