---
layout: default
title: 1. What Is Regression?
permalink: /modeling/simple-linear-regression/what-is-regression/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding regression as a modeling framework.
      Mathematical details and estimation will be developed in later lessons.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_slr_lesson_v0", JSON.stringify({
    url: "/modeling/simple-linear-regression/what-is-regression/",
    label: "Lesson 1 — What Is Regression?",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 2</span>
      <span class="badge">Lesson 1</span>
      <span class="badge">Regression</span>
      <span class="badge">Relationships</span>
    </div>

    <h1>1. What Is Regression?</h1>

    <p class="lead">
      Regression is a method for modeling the relationship between variables.
      It allows us to describe, predict, and understand how a response variable
      changes with a predictor.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/simple-linear-regression/">Back to Block 2</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual foundation. Equations come next.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what regression is,
    what problem it solves, and how it connects variables into a model.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Regression models how a response variable changes as a function of one or more predictors.
    </p>
  </div>

  <h2>1) The basic problem</h2>
  <div class="card">
    <p>
      We often want to understand how one variable depends on another.
      For example:
    </p>
    <ul>
      <li>How does income depend on education?</li>
      <li>How does exam score depend on study time?</li>
      <li>How does sales depend on advertising?</li>
    </ul>
  </div>

  <h2>2) Regression as a model</h2>
  <div class="card">
    <p>
      Regression expresses a relationship between variables:
    </p>
    <p><strong>Response = function(predictor) + error</strong></p>
    <p>
      It formalizes the idea that outcomes are partly predictable and partly random.
    </p>
  </div>

  <h2>3) Response and predictor</h2>
  <div class="card">
    <ul>
      <li><strong>Response (Y)</strong> — the variable we want to explain</li>
      <li><strong>Predictor (X)</strong> — the variable used to explain Y</li>
    </ul>
  </div>

  <h2>4) Regression is about relationships</h2>
  <div class="card">
    <p>
      Regression does not just describe data — it models how variables are connected.
      It captures the systematic relationship (signal) between X and Y.
    </p>
  </div>

  <h2>5) Regression and prediction</h2>
  <div class="card">
    <p>
      Once a relationship is modeled, we can predict new values of Y given X.
    </p>
  </div>

  <h2>6) Regression and explanation</h2>
  <div class="card">
    <p>
      Regression also helps us understand how changes in X affect Y.
    </p>
  </div>

  <h2>7) Example</h2>
  <div class="card">
    <p>
      Suppose we model exam score using study hours:
    </p>
    <p><strong>Score = function(Hours) + error</strong></p>
    <p>
      Regression helps us understand and quantify this relationship.
    </p>
  </div>

  <h2>8) Why regression matters</h2>
  <div class="card">
    <p>
      Regression is one of the most widely used tools in statistics,
      economics, business, and data science.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define regression clearly</li>
      <li>Identify response and predictor variables</li>
      <li>Understand regression as a relationship model</li>
      <li>Recognize its role in prediction and explanation</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we formalize regression using a mathematical equation.
    </p>
    <a class="btn" href="/modeling/simple-linear-regression/regression-equation/">
      Next lesson: Regression Equation →
    </a>
  </div>

</section>