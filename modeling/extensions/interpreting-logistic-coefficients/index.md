---
layout: default
title: 5. Interpreting Logistic Coefficients
permalink: /modeling/extensions/interpreting-logistic-coefficients/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on interpreting coefficients in logistic regression.
      Mathematical derivations will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_extensions_lesson_v0", JSON.stringify({
    url: "/modeling/extensions/interpreting-logistic-coefficients/",
    label: "Lesson 5 — Interpreting Logistic Coefficients",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 7</span>
      <span class="badge">Lesson 5</span>
      <span class="badge">Interpretation</span>
      <span class="badge">Odds Ratios</span>
    </div>

    <h1>5. Interpreting Logistic Coefficients</h1>

    <p class="lead">
      Logistic regression coefficients describe how predictors affect the log-odds of an outcome.
      These effects are interpreted through odds ratios, not direct probability changes.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/extensions/">Back to Block 7</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: correct interpretation of coefficients using odds and odds ratios.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand how to interpret logistic regression coefficients
    using odds and odds ratios.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Logistic coefficients represent changes in log-odds,
      which translate into multiplicative changes in odds.
    </p>
  </div>

  <h2>1) What the model estimates</h2>
  <div class="card">
    <p>
      Logistic regression models the log-odds of the outcome.
    </p>
  </div>

  <h2>2) Coefficients are not probabilities</h2>
  <div class="card">
    <p>
      A coefficient does NOT represent a change in probability.
    </p>
  </div>

  <h2>3) From coefficient to odds ratio</h2>
  <div class="card">
    <p>
      Exponentiating a coefficient gives the odds ratio:
    </p>
    <p><strong>odds ratio = e^(coefficient)</strong></p>
  </div>

  <h2>4) Interpretation of odds ratio</h2>
  <div class="card">
    <ul>
      <li>OR = 1 → no effect</li>
      <li>OR > 1 → increase in odds</li>
      <li>OR < 1 → decrease in odds</li>
    </ul>
  </div>

  <h2>5) Example</h2>
  <div class="card">
    <p>
      If a coefficient = 0.7:
    </p>
    <ul>
      <li>OR = e^0.7 ≈ 2.01</li>
      <li>Odds are approximately doubled</li>
    </ul>
  </div>

  <h2>6) Interpretation in words</h2>
  <div class="card">
    <p>
      “For a one-unit increase in X,
      the odds of the outcome are multiplied by OR.”
    </p>
  </div>

  <h2>7) Important distinction</h2>
  <div class="card">
    <p>
      Odds ratios are multiplicative, not additive.
    </p>
  </div>

  <h2>8) Common misunderstanding</h2>
  <div class="card">
    <p>
      Odds ratios are often incorrectly interpreted as probability changes.
    </p>
  </div>

  <h2>9) Why interpretation is harder</h2>
  <div class="card">
    <p>
      The relationship between predictors and probability is nonlinear.
    </p>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      Correct interpretation is essential for making valid conclusions
      from logistic regression models.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand log-odds interpretation</li>
      <li>Convert coefficients to odds ratios</li>
      <li>Interpret multiplicative effects</li>
      <li>Avoid common interpretation mistakes</li>
      <li>Prepare for generalized models</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now generalize this framework to a broader class of models.
    </p>
    <a class="btn" href="/modeling/extensions/glm/">
      Next lesson: Generalized Linear Models →
    </a>
  </div>

</section>