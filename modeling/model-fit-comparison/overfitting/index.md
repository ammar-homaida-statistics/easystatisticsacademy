---
layout: default
title: 4. Overfitting
permalink: /modeling/model-fit-comparison/overfitting/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces overfitting conceptually.
      Formal validation techniques will be developed later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_model_fit_lesson_v0", JSON.stringify({
    url: "/modeling/model-fit-comparison/overfitting/",
    label: "Lesson 4 — Overfitting",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 6</span>
      <span class="badge">Lesson 4</span>
      <span class="badge">Overfitting</span>
      <span class="badge">Generalization</span>
    </div>

    <h1>4. Overfitting</h1>

    <p class="lead">
      Overfitting occurs when a model captures noise instead of the true underlying relationship,
      leading to poor performance on new data.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/model-fit-comparison/">Back to Block 6</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding of generalization failure.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what overfitting is
    and why it leads to unreliable models.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A model that fits the training data perfectly can fail on new data.
    </p>
  </div>

  <h2>1) What is overfitting?</h2>
  <div class="card">
    <p>
      Overfitting happens when a model learns both the signal and the noise in the data.
    </p>
  </div>

  <h2>2) Intuition</h2>
  <div class="card">
    <p>
      The model becomes too flexible and adapts to random fluctuations
      rather than the true pattern.
    </p>
  </div>

  <h2>3) Key symptom</h2>
  <div class="card">
    <ul>
      <li>Excellent fit on training data</li>
      <li>Poor performance on new data</li>
    </ul>
  </div>

  <h2>4) Why it happens</h2>
  <div class="card">
    <ul>
      <li>Too many predictors</li>
      <li>Overly complex model</li>
      <li>Small dataset</li>
    </ul>
  </div>

  <h2>5) Visual intuition</h2>
  <div class="card">
    <p>
      An overfit model follows every data point,
      resulting in a highly irregular curve.
    </p>
  </div>

  <h2>6) Connection to R²</h2>
  <div class="card">
    <p>
      Overfitted models often have very high R²,
      but poor predictive performance.
    </p>
  </div>

  <h2>7) Why it is dangerous</h2>
  <div class="card">
    <ul>
      <li>Misleading conclusions</li>
      <li>Poor predictions</li>
      <li>False confidence in the model</li>
    </ul>
  </div>

  <h2>8) Overfitting vs good fit</h2>
  <div class="card">
    <p>
      Good models capture general patterns,
      not individual data points.
    </p>
  </div>

  <h2>9) Preventing overfitting</h2>
  <div class="card">
    <ul>
      <li>Simplify the model</li>
      <li>Use adjusted measures (adjusted R²)</li>
      <li>Validate on new data</li>
    </ul>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      The goal of modeling is not to fit existing data perfectly,
      but to generalize to new data.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand overfitting clearly</li>
      <li>Recognize its symptoms</li>
      <li>Distinguish fit vs generalization</li>
      <li>Identify causes</li>
      <li>Prepare for underfitting</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now examine underfitting,
      where the model is too simple to capture the true pattern.
    </p>
    <a class="btn" href="/modeling/model-fit-comparison/underfitting/">
      Next lesson: Underfitting →
    </a>
  </div>

</section>