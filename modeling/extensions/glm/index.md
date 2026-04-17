---
layout: default
title: 6. Generalized Linear Models (GLM)
permalink: /modeling/extensions/glm/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces the Generalized Linear Model (GLM) framework.
      Formal theory and estimation details will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_extensions_lesson_v0", JSON.stringify({
    url: "/modeling/extensions/glm/",
    label: "Lesson 6 — Generalized Linear Models",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 7</span>
      <span class="badge">Lesson 6</span>
      <span class="badge">GLM</span>
      <span class="badge">Unified Framework</span>
    </div>

    <h1>6. Generalized Linear Models (GLM)</h1>

    <p class="lead">
      Generalized Linear Models extend linear regression to handle different types of outcomes
      by combining a linear predictor with a link function and an appropriate distribution.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/extensions/">Back to Block 7</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual overview of the GLM framework.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand the structure of generalized linear models
    and how they unify different modeling approaches.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      GLMs generalize linear regression by allowing different outcome types
      through link functions and distributions.
    </p>
  </div>

  <h2>1) Why GLMs are needed</h2>
  <div class="card">
    <p>
      Different types of data require different modeling approaches:
    </p>
    <ul>
      <li>Continuous outcomes</li>
      <li>Binary outcomes</li>
      <li>Count data</li>
    </ul>
  </div>

  <h2>2) Core structure of GLM</h2>
  <div class="card">
    <p>
      A GLM consists of three components:
    </p>
    <ul>
      <li>Linear predictor (Xβ)</li>
      <li>Link function</li>
      <li>Probability distribution</li>
    </ul>
  </div>

  <h2>3) Linear predictor</h2>
  <div class="card">
    <p>
      Same as linear regression:
      a weighted combination of predictors.
    </p>
  </div>

  <h2>4) Link function</h2>
  <div class="card">
    <p>
      Connects the linear predictor to the expected value of the outcome.
    </p>
  </div>

  <h2>5) Distribution</h2>
  <div class="card">
    <p>
      Specifies the type of outcome:
    </p>
    <ul>
      <li>Normal → linear regression</li>
      <li>Binomial → logistic regression</li>
      <li>Poisson → count models</li>
    </ul>
  </div>

  <h2>6) Examples</h2>
  <div class="card">
    <ul>
      <li>Linear regression → identity link</li>
      <li>Logistic regression → logit link</li>
    </ul>
  </div>

  <h2>7) What GLM changes</h2>
  <div class="card">
    <p>
      It changes how the outcome is modeled,
      while keeping the linear structure in predictors.
    </p>
  </div>

  <h2>8) What stays the same</h2>
  <div class="card">
    <ul>
      <li>Interpretation of predictors (conceptually)</li>
      <li>Model-building logic</li>
      <li>Statistical reasoning</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      GLMs provide a unified framework for modeling different types of data.
    </p>
  </div>

  <h2>10) What comes next</h2>
  <div class="card">
    <p>
      We now examine link functions in more detail.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand GLM structure</li>
      <li>Recognize components of a model</li>
      <li>See connection between linear and logistic regression</li>
      <li>Understand role of distributions</li>
      <li>Prepare for link functions</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now explore link functions,
      which connect predictors to outcomes.
    </p>
    <a class="btn" href="/modeling/extensions/link-functions/">
      Next lesson: Link Functions →
    </a>
  </div>

</section>