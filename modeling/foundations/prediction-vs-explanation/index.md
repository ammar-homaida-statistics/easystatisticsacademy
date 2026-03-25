---
layout: default
title: 5. Prediction vs Explanation
permalink: /modeling/foundations/prediction-vs-explanation/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding the two main goals of modeling:
      prediction and explanation. Practical examples and case studies will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_foundations_lesson_v0", JSON.stringify({
    url: "/modeling/foundations/prediction-vs-explanation/",
    label: "Lesson 5 — Prediction vs Explanation",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 1</span>
      <span class="badge">Lesson 5</span>
      <span class="badge">Prediction</span>
      <span class="badge">Explanation</span>
    </div>

    <h1>5. Prediction vs Explanation</h1>

    <p class="lead">
      Models can be used for different purposes.
      Some aim to predict outcomes accurately,
      while others aim to explain relationships between variables.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/foundations/">Back to Block 1</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual distinction first. Applications will follow.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand the difference between
    prediction and explanation, and how this affects model design and interpretation.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A model that predicts well is not necessarily good for explanation,
      and a model that explains well is not always best for prediction.
    </p>
  </div>

  <h2>1) What is prediction?</h2>
  <div class="card">
    <p>
      Prediction focuses on accurately forecasting outcomes.
      The goal is to minimize prediction error on new data.
    </p>
  </div>

  <h2>2) What is explanation?</h2>
  <div class="card">
    <p>
      Explanation focuses on understanding how variables are related.
      The goal is to interpret the effect of predictors on the response.
    </p>
  </div>

  <h2>3) Key differences</h2>
  <div class="card">
    <ul>
      <li><strong>Prediction</strong> — accuracy is the priority</li>
      <li><strong>Explanation</strong> — interpretation is the priority</li>
    </ul>
  </div>

  <h2>4) Model complexity</h2>
  <div class="card">
    <ul>
      <li>Prediction models can be complex and less interpretable</li>
      <li>Explanatory models are often simpler and interpretable</li>
    </ul>
  </div>

  <h2>5) Example</h2>
  <div class="card">
    <p>
      Suppose we model house prices:
    </p>
    <ul>
      <li><strong>Prediction goal:</strong> accurately predict price</li>
      <li><strong>Explanation goal:</strong> understand effect of size, location, etc.</li>
    </ul>
  </div>

  <h2>6) Trade-offs</h2>
  <div class="card">
    <p>
      Improving prediction may reduce interpretability.
      Improving interpretability may reduce predictive accuracy.
    </p>
  </div>

  <h2>7) Why this matters</h2>
  <div class="card">
    <p>
      Choosing the wrong goal leads to incorrect conclusions,
      misuse of models, and poor decisions.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Distinguish prediction vs explanation clearly</li>
      <li>Understand differences in goals</li>
      <li>Recognize trade-offs in modeling</li>
      <li>Choose appropriate modeling approach</li>
    </ul>
  </div>

  <!-- NEXT = BLOCK 2 -->
  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we begin building actual models using simple linear regression.
    </p>
    <a class="btn" href="/modeling/simple-linear-regression/">
      Go to Block 2 — Simple Linear Regression →
    </a>
  </div>

</section>