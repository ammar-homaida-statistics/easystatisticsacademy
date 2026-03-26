---
layout: default
title: 3. Slope (Interpretation)
permalink: /modeling/simple-linear-regression/slope/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on correct interpretation of the slope.
      Applications and multiple examples will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_slr_lesson_v0", JSON.stringify({
    url: "/modeling/simple-linear-regression/slope/",
    label: "Lesson 3 — Slope",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 2</span>
      <span class="badge">Lesson 3</span>
      <span class="badge">Slope</span>
      <span class="badge">Interpretation</span>
    </div>

    <h1>3. Slope (Interpretation)</h1>

    <p class="lead">
      The slope is the most important parameter in regression.
      It tells us how the response variable changes when the predictor changes.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/simple-linear-regression/">Back to Block 2</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: interpretation-first. Avoid memorization—focus on meaning.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should correctly interpret the slope
    in a regression model and understand its meaning in real-world context.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      The slope (β₁) represents the expected change in the response variable
      for a one-unit increase in the predictor.
    </p>
  </div>

  <h2>1) Where the slope appears</h2>
  <div class="card">
    <p><strong>Y = β₀ + β₁X + ε</strong></p>
    <p>
      The slope is β₁.
    </p>
  </div>

  <h2>2) Basic interpretation</h2>
  <div class="card">
    <p>
      For a one-unit increase in X,
      the expected value of Y changes by β₁ units.
    </p>
  </div>

  <h2>3) Direction of relationship</h2>
  <div class="card">
    <ul>
      <li><strong>β₁ > 0</strong> → positive relationship</li>
      <li><strong>β₁ < 0</strong> → negative relationship</li>
      <li><strong>β₁ = 0</strong> → no linear relationship</li>
    </ul>
  </div>

  <h2>4) Interpretation must include context</h2>
  <div class="card">
    <p>
      A correct interpretation always includes:
    </p>
    <ul>
      <li>the variables</li>
      <li>the units</li>
      <li>the direction</li>
    </ul>
  </div>

  <h2>5) Example</h2>
  <div class="card">
    <p>
      Model:
    </p>
    <p><strong>Score = 50 + 5 × Hours</strong></p>
    <p>
      Interpretation:
    </p>
    <p>
      For each additional hour of study, the expected exam score increases by 5 points.
    </p>
  </div>

  <h2>6) Common mistakes</h2>
  <div class="card">
    <ul>
      <li>Ignoring units</li>
      <li>Interpreting slope as causation automatically</li>
      <li>Confusing slope with correlation</li>
    </ul>
  </div>

  <h2>7) Slope and prediction</h2>
  <div class="card">
    <p>
      The slope determines how predictions change when X changes.
    </p>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Correct interpretation of slope is essential for understanding
      relationships and making valid conclusions from models.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Identify the slope in a regression model</li>
      <li>Interpret slope correctly with units</li>
      <li>Understand direction of relationships</li>
      <li>Avoid common interpretation mistakes</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we interpret the intercept and its meaning.
    </p>
    <a class="btn" href="/modeling/simple-linear-regression/intercept/">
      Next lesson: Intercept →
    </a>
  </div>

</section>