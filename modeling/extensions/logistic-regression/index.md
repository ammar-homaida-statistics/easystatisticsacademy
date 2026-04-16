---
layout: default
title: 2. Logistic Regression
permalink: /modeling/extensions/logistic-regression/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces logistic regression conceptually.
      Mathematical formulation and estimation will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_extensions_lesson_v0", JSON.stringify({
    url: "/modeling/extensions/logistic-regression/",
    label: "Lesson 2 — Logistic Regression",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 7</span>
      <span class="badge">Lesson 2</span>
      <span class="badge">Logistic Regression</span>
      <span class="badge">Binary Outcomes</span>
    </div>

    <h1>2. Logistic Regression</h1>

    <p class="lead">
      Logistic regression is used when the outcome is binary.
      Instead of modeling the outcome directly, it models the probability of an event.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/extensions/">Back to Block 7</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding of binary outcome modeling.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what logistic regression is
    and why it is used for binary outcomes.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Logistic regression models the probability of an outcome, not the outcome itself.
    </p>
  </div>

  <h2>1) The problem with linear regression</h2>
  <div class="card">
    <p>
      When the outcome is binary (0 or 1),
      linear regression can produce invalid predictions:
    </p>
    <ul>
      <li>Predicted values less than 0</li>
      <li>Predicted values greater than 1</li>
    </ul>
  </div>

  <h2>2) What we want instead</h2>
  <div class="card">
    <p>
      We want a model that:
    </p>
    <ul>
      <li>Predicts probabilities</li>
      <li>Keeps values between 0 and 1</li>
      <li>Reflects nonlinear relationships</li>
    </ul>
  </div>

  <h2>3) What logistic regression does</h2>
  <div class="card">
    <p>
      Logistic regression models the probability that the outcome equals 1.
    </p>
  </div>

  <h2>4) Output of the model</h2>
  <div class="card">
    <p>
      The model produces values between 0 and 1,
      interpreted as probabilities.
    </p>
  </div>

  <h2>5) Shape of the relationship</h2>
  <div class="card">
    <p>
      Instead of a straight line,
      logistic regression produces an S-shaped curve.
    </p>
  </div>

  <h2>6) Interpretation</h2>
  <div class="card">
    <p>
      The model describes how predictors affect the probability of an event.
    </p>
  </div>

  <h2>7) Examples of use</h2>
  <div class="card">
    <ul>
      <li>Disease vs no disease</li>
      <li>Purchase vs no purchase</li>
      <li>Pass vs fail</li>
    </ul>
  </div>

  <h2>8) Key difference from linear regression</h2>
  <div class="card">
    <ul>
      <li>Linear regression → continuous outcome</li>
      <li>Logistic regression → probability of binary outcome</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Logistic regression allows valid modeling of binary outcomes,
      which are common in real-world problems.
    </p>
  </div>

  <h2>10) What comes next</h2>
  <div class="card">
    <p>
      To understand logistic regression fully,
      we need to connect probabilities to a linear model using the logit transformation.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand logistic regression conceptually</li>
      <li>Recognize limitations of linear regression for binary data</li>
      <li>Interpret probabilities as model outputs</li>
      <li>Understand the S-shaped relationship</li>
      <li>Prepare for logit transformation</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now explain how probabilities are transformed into a linear form using the logit.
    </p>
    <a class="btn" href="/modeling/extensions/probability-vs-logit/">
      Next lesson: Probability vs Logit →
    </a>
  </div>

</section>