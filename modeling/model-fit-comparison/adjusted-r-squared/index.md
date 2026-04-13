---
layout: default
title: 3. Adjusted R²
permalink: /modeling/model-fit-comparison/adjusted-r-squared/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 explains adjusted R² conceptually and its role in model comparison.
      Formal derivation will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_model_fit_lesson_v0", JSON.stringify({
    url: "/modeling/model-fit-comparison/adjusted-r-squared/",
    label: "Lesson 3 — Adjusted R²",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 6</span>
      <span class="badge">Lesson 3</span>
      <span class="badge">Adjusted R²</span>
      <span class="badge">Complexity</span>
    </div>

    <h1>3. Adjusted R²</h1>

    <p class="lead">
      Adjusted R² improves upon R² by accounting for the number of predictors.
      It penalizes models that add variables without improving explanatory power.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/model-fit-comparison/">Back to Block 6</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual correction to R².
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand why adjusted R² is needed
    and how it improves model evaluation.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Adjusted R² penalizes unnecessary predictors and rewards meaningful ones.
    </p>
  </div>

  <h2>1) Why R² is not enough</h2>
  <div class="card">
    <p>
      R² always increases when new variables are added,
      even if they are irrelevant.
    </p>
  </div>

  <h2>2) What adjusted R² does</h2>
  <div class="card">
    <p>
      Adjusted R² corrects this by taking into account the number of predictors in the model.
    </p>
  </div>

  <h2>3) Interpretation</h2>
  <div class="card">
    <p>
      Adjusted R² increases only when a new variable improves the model beyond chance.
    </p>
  </div>

  <h2>4) Key behavior</h2>
  <div class="card">
    <ul>
      <li>Useful variable → adjusted R² increases</li>
      <li>Useless variable → adjusted R² decreases or stays the same</li>
    </ul>
  </div>

  <h2>5) Comparison use</h2>
  <div class="card">
    <p>
      Adjusted R² is mainly used to compare models with different numbers of predictors.
    </p>
  </div>

  <h2>6) Relationship to R²</h2>
  <div class="card">
    <p>
      Adjusted R² is always less than or equal to R².
    </p>
  </div>

  <h2>7) When to use it</h2>
  <div class="card">
    <ul>
      <li>Multiple regression</li>
      <li>Model comparison</li>
      <li>Variable selection</li>
    </ul>
  </div>

  <h2>8) Common misunderstanding</h2>
  <div class="card">
    <p>
      Adjusted R² does not guarantee the best model —
      it is one of several evaluation tools.
    </p>
  </div>

  <h2>9) Limitation</h2>
  <div class="card">
    <p>
      It does not account for prediction performance on new data.
    </p>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      Adjusted R² helps prevent overfitting by discouraging unnecessary complexity.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand adjusted R²</li>
      <li>Compare models correctly</li>
      <li>Recognize limitations of R²</li>
      <li>Evaluate model complexity</li>
      <li>Prepare for overfitting concept</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now examine overfitting,
      where models fit training data well but fail on new data.
    </p>
    <a class="btn" href="/modeling/model-fit-comparison/overfitting/">
      Next lesson: Overfitting →
    </a>
  </div>

</section>