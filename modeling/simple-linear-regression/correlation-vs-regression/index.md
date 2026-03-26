---
layout: default
title: 8. Correlation vs Regression
permalink: /modeling/simple-linear-regression/correlation-vs-regression/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on distinguishing correlation and regression.
      Visual comparisons and applications will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_slr_lesson_v0", JSON.stringify({
    url: "/modeling/simple-linear-regression/correlation-vs-regression/",
    label: "Lesson 8 — Correlation vs Regression",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 2</span>
      <span class="badge">Lesson 8</span>
      <span class="badge">Correlation</span>
      <span class="badge">Regression</span>
    </div>

    <h1>8. Correlation vs Regression</h1>

    <p class="lead">
      Correlation measures association between variables,
      while regression models the relationship to explain or predict outcomes.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/simple-linear-regression/">Back to Block 2</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual clarity first. Avoid confusion between the two.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should clearly distinguish correlation and regression,
    and understand when each is used.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Correlation describes association.
      Regression models how one variable depends on another.
    </p>
  </div>

  <h2>1) What is correlation?</h2>
  <div class="card">
    <p>
      Correlation measures the strength and direction of a linear relationship
      between two variables.
    </p>
    <p><strong>r ∈ [-1, 1]</strong></p>
  </div>

  <h2>2) What is regression?</h2>
  <div class="card">
    <p>
      Regression models how a response variable changes as a function of a predictor.
    </p>
  </div>

  <h2>3) Key difference: purpose</h2>
  <div class="card">
    <ul>
      <li><strong>Correlation</strong> → measure association</li>
      <li><strong>Regression</strong> → model relationship and make predictions</li>
    </ul>
  </div>

  <h2>4) Directionality</h2>
  <div class="card">
    <ul>
      <li><strong>Correlation</strong> is symmetric (X with Y = Y with X)</li>
      <li><strong>Regression</strong> is directional (Y depends on X)</li>
    </ul>
  </div>

  <h2>5) Output</h2>
  <div class="card">
    <ul>
      <li><strong>Correlation</strong> → single number (r)</li>
      <li><strong>Regression</strong> → equation (model)</li>
    </ul>
  </div>

  <h2>6) Interpretation</h2>
  <div class="card">
    <ul>
      <li><strong>Correlation</strong> → strength of relationship</li>
      <li><strong>Regression</strong> → change in Y per unit change in X</li>
    </ul>
  </div>

  <h2>7) Example</h2>
  <div class="card">
    <p>
      Hours studied and exam score:
    </p>
    <ul>
      <li>Correlation → how strongly they are related</li>
      <li>Regression → how much score increases per hour</li>
    </ul>
  </div>

  <h2>8) Common mistakes</h2>
  <div class="card">
    <ul>
      <li>Using correlation to make predictions</li>
      <li>Confusing correlation with causation</li>
      <li>Thinking regression implies causation automatically</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Confusing correlation and regression leads to incorrect modeling
      and misinterpretation of results.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define correlation and regression</li>
      <li>Understand their differences</li>
      <li>Recognize directionality in regression</li>
      <li>Avoid common misconceptions</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we apply regression for prediction.
    </p>
    <a class="btn" href="/modeling/simple-linear-regression/prediction/">
      Next lesson: Prediction →
    </a>
  </div>

</section>