---
layout: default
title: 8. Comparing Linear and Logistic Regression
permalink: /modeling/extensions/comparing-linear-and-logistic/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 compares linear and logistic regression conceptually.
      Deeper mathematical comparisons will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_extensions_lesson_v0", JSON.stringify({
    url: "/modeling/extensions/comparing-linear-and-logistic/",
    label: "Lesson 8 — Comparing Linear and Logistic Regression",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 7</span>
      <span class="badge">Lesson 8</span>
      <span class="badge">Comparison</span>
      <span class="badge">Linear vs Logistic</span>
    </div>

    <h1>8. Comparing Linear and Logistic Regression</h1>

    <p class="lead">
      Linear and logistic regression share the same modeling structure,
      but differ in how the outcome is modeled and interpreted.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/extensions/">Back to Block 7</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: final conceptual consolidation of regression models.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand the similarities and differences
    between linear and logistic regression.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Both models use a linear predictor,
      but differ in how the outcome is connected to it.
    </p>
  </div>

  <h2>1) What they have in common</h2>
  <div class="card">
    <ul>
      <li>Linear predictor (Xβ)</li>
      <li>Use of coefficients</li>
      <li>Modeling relationships between variables</li>
    </ul>
  </div>

  <h2>2) Key difference</h2>
  <div class="card">
    <ul>
      <li>Linear regression → models outcome directly</li>
      <li>Logistic regression → models probability via logit</li>
    </ul>
  </div>

  <h2>3) Outcome type</h2>
  <div class="card">
    <ul>
      <li>Linear → continuous outcome</li>
      <li>Logistic → binary outcome</li>
    </ul>
  </div>

  <h2>4) Link function</h2>
  <div class="card">
    <ul>
      <li>Linear → identity link</li>
      <li>Logistic → logit link</li>
    </ul>
  </div>

  <h2>5) Output</h2>
  <div class="card">
    <ul>
      <li>Linear → predicted values</li>
      <li>Logistic → predicted probabilities</li>
    </ul>
  </div>

  <h2>6) Interpretation</h2>
  <div class="card">
    <ul>
      <li>Linear → additive effects</li>
      <li>Logistic → multiplicative effects (odds ratios)</li>
    </ul>
  </div>

  <h2>7) Shape of relationship</h2>
  <div class="card">
    <ul>
      <li>Linear → straight line</li>
      <li>Logistic → S-shaped curve</li>
    </ul>
  </div>

  <h2>8) When to use each</h2>
  <div class="card">
    <ul>
      <li>Linear → continuous outcomes</li>
      <li>Logistic → binary outcomes</li>
    </ul>
  </div>

  <h2>9) Unified view (GLM)</h2>
  <div class="card">
    <p>
      Both models are part of the Generalized Linear Model framework.
    </p>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      Understanding both models allows you to choose the correct method
      based on the structure of your data.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Compare linear and logistic regression</li>
      <li>Understand structural similarities</li>
      <li>Recognize key differences</li>
      <li>Select appropriate model</li>
      <li>Prepare for machine learning concepts</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now connect statistical modeling to machine learning concepts.
    </p>
    <a class="btn" href="/modeling/extensions/bridge-to-machine-learning/">
      Next lesson: Bridge to Machine Learning →
    </a>
  </div>

</section>