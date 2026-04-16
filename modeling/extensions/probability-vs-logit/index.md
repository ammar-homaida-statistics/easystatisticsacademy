---
layout: default
title: 3. Probability vs Logit
permalink: /modeling/extensions/probability-vs-logit/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 explains why probabilities cannot be modeled linearly
      and introduces the logit transformation.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_extensions_lesson_v0", JSON.stringify({
    url: "/modeling/extensions/probability-vs-logit/",
    label: "Lesson 3 — Probability vs Logit",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 7</span>
      <span class="badge">Lesson 3</span>
      <span class="badge">Probability</span>
      <span class="badge">Logit</span>
    </div>

    <h1>3. Probability vs Logit</h1>

    <p class="lead">
      Probabilities are bounded between 0 and 1,
      which makes them unsuitable for linear modeling.
      The logit transformation converts probabilities into a form that can be modeled linearly.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/extensions/">Back to Block 7</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual bridge to logistic regression structure.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand why probabilities are not modeled directly
    and how the logit transformation solves this problem.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Probabilities are bounded, but logits are unbounded — allowing linear modeling.
    </p>
  </div>

  <h2>1) The problem with probability</h2>
  <div class="card">
    <p>
      Probabilities must always lie between 0 and 1.
    </p>
  </div>

  <h2>2) Why linear models fail</h2>
  <div class="card">
    <p>
      A linear model can produce values outside this range,
      which are not valid probabilities.
    </p>
  </div>

  <h2>3) Nonlinear relationship</h2>
  <div class="card">
    <p>
      The relationship between predictors and probability is typically nonlinear.
    </p>
  </div>

  <h2>4) The solution: transformation</h2>
  <div class="card">
    <p>
      Instead of modeling probability directly,
      we transform it into another scale.
    </p>
  </div>

  <h2>5) From probability to odds</h2>
  <div class="card">
    <p>
      The first step is converting probability into odds.
    </p>
  </div>

  <h2>6) From odds to logit</h2>
  <div class="card">
    <p>
      Taking the logarithm of odds produces the logit.
    </p>
  </div>

  <h2>7) Why logit works</h2>
  <div class="card">
    <ul>
      <li>Logit values range from −∞ to +∞</li>
      <li>This allows linear modeling</li>
    </ul>
  </div>

  <h2>8) Resulting model</h2>
  <div class="card">
    <p>
      Logistic regression models:
      predictors → logit → probability
    </p>
  </div>

  <h2>9) Intuition</h2>
  <div class="card">
    <p>
      We model a transformed version of probability
      that behaves like a linear variable.
    </p>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      This transformation is what makes logistic regression mathematically valid.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand why probability cannot be modeled linearly</li>
      <li>Understand the need for transformation</li>
      <li>Recognize the role of the logit</li>
      <li>Understand bounded vs unbounded variables</li>
      <li>Prepare for odds interpretation</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now define and interpret odds,
      the key concept underlying the logit transformation.
    </p>
    <a class="btn" href="/modeling/extensions/odds/">
      Next lesson: Odds →
    </a>
  </div>

</section>