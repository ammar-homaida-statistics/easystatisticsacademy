---
layout: default
title: 6. Multicollinearity
permalink: /modeling/multiple-regression/multicollinearity/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding multicollinearity conceptually.
      Formal diagnostics and remedies will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_mr_lesson_v0", JSON.stringify({
    url: "/modeling/multiple-regression/multicollinearity/",
    label: "Lesson 6 — Multicollinearity",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 3</span>
      <span class="badge">Lesson 6</span>
      <span class="badge">Multicollinearity</span>
      <span class="badge">Stability</span>
    </div>

    <h1>6. Multicollinearity</h1>

    <p class="lead">
      Multicollinearity occurs when predictors are highly correlated,
      making it difficult to separate their individual effects.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/multiple-regression/">Back to Block 3</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: intuitive understanding of instability in coefficients.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what multicollinearity is,
    why it occurs, and how it affects regression coefficients.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      When predictors are strongly related to each other,
      the model struggles to determine their individual contributions.
    </p>
  </div>

  <h2>1) What is multicollinearity?</h2>
  <div class="card">
    <p>
      Multicollinearity occurs when two or more predictors are highly correlated.
    </p>
  </div>

  <h2>2) Example</h2>
  <div class="card">
    <p>
      Suppose we include:
    </p>
    <ul>
      <li>Height (cm)</li>
      <li>Height (inches)</li>
    </ul>
    <p>
      These variables contain nearly identical information.
    </p>
  </div>

  <h2>3) Why it is a problem</h2>
  <div class="card">
    <ul>
      <li>Coefficients become unstable</li>
      <li>Small data changes → large coefficient changes</li>
      <li>Interpretation becomes unreliable</li>
    </ul>
  </div>

  <h2>4) Intuition</h2>
  <div class="card">
    <p>
      If two predictors move together, the model cannot clearly assign
      their individual effects.
    </p>
  </div>

  <h2>5) Effect on predictions</h2>
  <div class="card">
    <p>
      Predictions may still be accurate,
      even if individual coefficients are unstable.
    </p>
  </div>

  <h2>6) Important distinction</h2>
  <div class="card">
    <ul>
      <li><strong>Prediction</strong> → may remain good</li>
      <li><strong>Interpretation</strong> → becomes difficult</li>
    </ul>
  </div>

  <h2>7) Signs of multicollinearity</h2>
  <div class="card">
    <ul>
      <li>Unexpected coefficient signs</li>
      <li>Large standard errors (later topic)</li>
      <li>Highly correlated predictors</li>
    </ul>
  </div>

  <h2>8) Common situations</h2>
  <div class="card">
    <ul>
      <li>Redundant variables</li>
      <li>Derived variables</li>
      <li>Highly related features in real data</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Multicollinearity limits our ability to interpret coefficients,
      even if the model fits the data well.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define multicollinearity</li>
      <li>Understand its impact on coefficients</li>
      <li>Distinguish prediction vs interpretation issues</li>
      <li>Recognize common warning signs</li>
      <li>Prepare for categorical variables</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we extend regression to include categorical variables using dummy coding.
    </p>
    <a class="btn" href="/modeling/multiple-regression/dummy-variables/">
      Next lesson: Dummy Variables →
    </a>
  </div>

</section>