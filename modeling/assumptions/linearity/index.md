---
layout: default
title: 2. Linearity
permalink: /modeling/assumptions/linearity/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding the linearity assumption conceptually.
      Diagnostic tools and remedies will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_assumptions_lesson_v0", JSON.stringify({
    url: "/modeling/assumptions/linearity/",
    label: "Lesson 2 — Linearity",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 4</span>
      <span class="badge">Lesson 2</span>
      <span class="badge">Linearity</span>
      <span class="badge">Model Form</span>
    </div>

    <h1>2. Linearity</h1>

    <p class="lead">
      The linearity assumption requires that the relationship between predictors
      and the response is correctly specified by the model.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/assumptions/">Back to Block 4</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding before diagnostics and transformations.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what the linearity assumption means
    and how violations affect model performance.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      The model must correctly represent the relationship between predictors and the outcome.
    </p>
  </div>

  <h2>1) What does linearity mean?</h2>
  <div class="card">
    <p>
      Linearity means that the expected value of Y is a linear function of the predictors.
    </p>
  </div>

  <h2>2) Important clarification</h2>
  <div class="card">
    <p>
      Linearity refers to the model being linear in the coefficients,
      not necessarily linear in the variables themselves.
    </p>
  </div>

  <h2>3) Example</h2>
  <div class="card">
    <p>
      These are still linear models:
    </p>
    <ul>
      <li>Y = β₀ + β₁X</li>
      <li>Y = β₀ + β₁X + β₂X²</li>
    </ul>
  </div>

  <h2>4) What is a violation?</h2>
  <div class="card">
    <p>
      A violation occurs when the true relationship is not captured
      by the chosen model form.
    </p>
  </div>

  <h2>5) Consequences of violation</h2>
  <div class="card">
    <ul>
      <li>Biased estimates</li>
      <li>Poor predictions</li>
      <li>Systematic errors in residuals</li>
    </ul>
  </div>

  <h2>6) How violations appear</h2>
  <div class="card">
    <p>
      Residuals show patterns instead of random scatter.
    </p>
  </div>

  <h2>7) Fixing non-linearity</h2>
  <div class="card">
    <ul>
      <li>Add transformed variables (e.g., X², log(X))</li>
      <li>Include interaction terms</li>
      <li>Use more flexible models</li>
    </ul>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      If the model form is incorrect, all interpretations based on the model can be misleading.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand the linearity assumption</li>
      <li>Distinguish linear in parameters vs variables</li>
      <li>Recognize violations conceptually</li>
      <li>Understand consequences of misspecification</li>
      <li>Prepare for diagnostics</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now examine the independence assumption,
      which concerns the relationship between observations.
    </p>
    <a class="btn" href="/modeling/assumptions/independence/">
      Next lesson: Independence →
    </a>
  </div>

</section>