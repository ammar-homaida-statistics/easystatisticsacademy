---
layout: default
title: 7. Dummy Variables
permalink: /modeling/multiple-regression/dummy-variables/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces dummy variables for categorical predictors.
      Advanced coding schemes and interpretation will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_mr_lesson_v0", JSON.stringify({
    url: "/modeling/multiple-regression/dummy-variables/",
    label: "Lesson 7 — Dummy Variables",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 3</span>
      <span class="badge">Lesson 7</span>
      <span class="badge">Categorical Data</span>
      <span class="badge">Dummy Coding</span>
    </div>

    <h1>7. Dummy Variables</h1>

    <p class="lead">
      Regression models require numeric inputs.
      Dummy variables allow us to include categorical variables in the model.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/multiple-regression/">Back to Block 3</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: basic dummy coding and interpretation.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand how categorical variables
    are represented in regression models using dummy variables.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Categorical variables are converted into binary (0/1) variables
      so they can be included in regression models.
    </p>
  </div>

  <h2>1) Why we need dummy variables</h2>
  <div class="card">
    <p>
      Regression requires numeric predictors,
      but many real-world variables are categorical.
    </p>
  </div>

  <h2>2) Example: gender</h2>
  <div class="card">
    <p>
      Suppose we have:
    </p>
    <ul>
      <li>Male</li>
      <li>Female</li>
    </ul>

    <p>
      We create a dummy variable:
    </p>
    <p><strong>Female = 1, Male = 0</strong></p>
  </div>

  <h2>3) Model with dummy variable</h2>
  <div class="card">
    <p><strong>Y = β₀ + β₁(Female)</strong></p>

    <ul>
      <li>β₀ → baseline (Male)</li>
      <li>β₁ → difference between Female and Male</li>
    </ul>
  </div>

  <h2>4) More than two categories</h2>
  <div class="card">
    <p>
      For k categories, we use k−1 dummy variables.
    </p>
  </div>

  <h2>5) Reference category</h2>
  <div class="card">
    <p>
      One category is chosen as the reference (baseline),
      and all comparisons are made relative to it.
    </p>
  </div>

  <h2>6) Interpretation</h2>
  <div class="card">
    <p>
      Dummy variable coefficients represent differences from the reference group.
    </p>
  </div>

  <h2>7) Common mistakes</h2>
  <div class="card">
    <ul>
      <li>Including all categories (dummy variable trap)</li>
      <li>Misinterpreting the reference group</li>
      <li>Treating categories as numeric values</li>
    </ul>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Most real-world datasets include categorical variables.
      Dummy coding allows them to be included correctly.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand dummy variables</li>
      <li>Convert categorical variables into numeric form</li>
      <li>Interpret coefficients for categorical predictors</li>
      <li>Understand reference categories</li>
      <li>Avoid common coding mistakes</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we explore interaction effects,
      where the effect of one variable depends on another.
    </p>
    <a class="btn" href="/modeling/multiple-regression/interactions/">
      Next lesson: Interactions →
    </a>
  </div>

</section>