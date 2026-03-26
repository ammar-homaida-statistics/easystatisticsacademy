---
layout: default
title: 3. Adjusted Effects
permalink: /modeling/multiple-regression/adjusted-effects/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding adjusted effects conceptually.
      Formal estimation and statistical inference will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_mr_lesson_v0", JSON.stringify({
    url: "/modeling/multiple-regression/adjusted-effects/",
    label: "Lesson 3 — Adjusted Effects",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 3</span>
      <span class="badge">Lesson 3</span>
      <span class="badge">Adjusted Effects</span>
      <span class="badge">Interpretation</span>
    </div>

    <h1>3. Adjusted Effects</h1>

    <p class="lead">
      In multiple regression, each coefficient represents the effect of a predictor
      while holding all other variables constant.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/multiple-regression/">Back to Block 3</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: core interpretation principle of multiple regression.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand how to interpret regression coefficients
    as adjusted effects and why this is essential for correct modeling.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Each coefficient measures the effect of one predictor while controlling for the others.
    </p>
  </div>

  <h2>1) What does “adjusted” mean?</h2>
  <div class="card">
    <p>
      “Adjusted” means that the effect of a predictor is estimated after accounting for
      the influence of other variables in the model.
    </p>
  </div>

  <h2>2) Example</h2>
  <div class="card">
    <p>
      Model:
    </p>
    <p><strong>Score = β₀ + β₁(Hours) + β₂(Sleep)</strong></p>

    <p>
      Interpretation of β₁:
    </p>
    <p>
      The effect of study hours on score <strong>holding sleep constant</strong>.
    </p>
  </div>

  <h2>3) Why adjustment is necessary</h2>
  <div class="card">
    <p>
      Predictors are often related to each other.
      Without adjustment, their effects can be mixed together.
    </p>
  </div>

  <h2>4) Partial effect</h2>
  <div class="card">
    <p>
      Each coefficient represents a <strong>partial effect</strong>:
      the unique contribution of that predictor to the response.
    </p>
  </div>

  <h2>5) Holding other variables constant</h2>
  <div class="card">
    <p>
      Conceptually, we compare observations that differ in one variable
      while keeping others fixed.
    </p>
  </div>

  <h2>6) Comparison to simple regression</h2>
  <div class="card">
    <ul>
      <li><strong>Simple regression</strong> → effect without adjustment</li>
      <li><strong>Multiple regression</strong> → adjusted effect</li>
    </ul>
  </div>

  <h2>7) Interpretation example</h2>
  <div class="card">
    <p>
      If β₁ = 3:
    </p>
    <p>
      Increasing X₁ by one unit increases Y by 3 units,
      <strong>holding other predictors constant</strong>.
    </p>
  </div>

  <h2>8) Common mistakes</h2>
  <div class="card">
    <ul>
      <li>Ignoring the phrase “holding others constant”</li>
      <li>Interpreting coefficients as simple relationships</li>
      <li>Confusing adjusted effects with causal effects</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Correct interpretation of coefficients is essential for valid conclusions
      in both research and applied work.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand adjusted (partial) effects</li>
      <li>Interpret coefficients correctly</li>
      <li>Understand “holding others constant”</li>
      <li>Avoid misinterpretation of regression output</li>
      <li>Prepare for confounding</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we examine what happens when variables are related
      and how this affects interpretation.
    </p>
    <a class="btn" href="/modeling/multiple-regression/confounding/">
      Next lesson: Confounding →
    </a>
  </div>

</section>