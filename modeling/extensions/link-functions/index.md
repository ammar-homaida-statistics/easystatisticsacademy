---
layout: default
title: 7. Link Functions
permalink: /modeling/extensions/link-functions/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces link functions conceptually.
      Formal definitions and alternative links will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_extensions_lesson_v0", JSON.stringify({
    url: "/modeling/extensions/link-functions/",
    label: "Lesson 7 — Link Functions",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 7</span>
      <span class="badge">Lesson 7</span>
      <span class="badge">Link Functions</span>
      <span class="badge">Transformation</span>
    </div>

    <h1>7. Link Functions</h1>

    <p class="lead">
      Link functions connect the linear predictor to the expected value of the outcome.
      They determine how predictors influence different types of data.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/extensions/">Back to Block 7</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding of transformation in modeling.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what link functions are
    and why they are essential in generalized linear models.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A link function transforms the expected outcome into a scale
      where a linear relationship with predictors can be used.
    </p>
  </div>

  <h2>1) The problem</h2>
  <div class="card">
    <p>
      The expected value of the outcome may not have a linear relationship with predictors.
    </p>
  </div>

  <h2>2) The solution</h2>
  <div class="card">
    <p>
      Apply a transformation (link function) to make the relationship linear.
    </p>
  </div>

  <h2>3) General idea</h2>
  <div class="card">
    <p>
      GLM models:
    </p>
    <p><strong>link(E[Y]) = Xβ</strong></p>
  </div>

  <h2>4) Identity link</h2>
  <div class="card">
    <p>
      Used in linear regression:
    </p>
    <p><strong>E[Y] = Xβ</strong></p>
  </div>

  <h2>5) Logit link</h2>
  <div class="card">
    <p>
      Used in logistic regression:
    </p>
    <p><strong>log(p / (1 − p)) = Xβ</strong></p>
  </div>

  <h2>6) Why link functions matter</h2>
  <div class="card">
    <ul>
      <li>Ensure valid predictions</li>
      <li>Handle different data types</li>
      <li>Allow linear modeling structure</li>
    </ul>
  </div>

  <h2>7) Intuition</h2>
  <div class="card">
    <p>
      We don’t change the predictors —
      we change how the outcome is connected to them.
    </p>
  </div>

  <h2>8) Different links for different problems</h2>
  <div class="card">
    <ul>
      <li>Identity → continuous outcomes</li>
      <li>Logit → binary outcomes</li>
      <li>Log → count data (preview)</li>
    </ul>
  </div>

  <h2>9) What stays linear</h2>
  <div class="card">
    <p>
      The linear predictor Xβ remains unchanged across models.
    </p>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      Link functions are what allow a single framework (GLM)
      to handle many types of data.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand what a link function is</li>
      <li>Recognize its role in GLM</li>
      <li>Distinguish identity vs logit link</li>
      <li>Understand transformation logic</li>
      <li>Prepare for model comparison</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now compare linear and logistic regression
      to consolidate all concepts.
    </p>
    <a class="btn" href="/modeling/extensions/comparing-linear-and-logistic/">
      Next lesson: Comparing Linear and Logistic →
    </a>
  </div>

</section>