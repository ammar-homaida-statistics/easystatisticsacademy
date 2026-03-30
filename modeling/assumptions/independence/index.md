---
layout: default
title: 3. Independence
permalink: /modeling/assumptions/independence/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding the independence assumption conceptually.
      Time series and advanced dependence structures will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_assumptions_lesson_v0", JSON.stringify({
    url: "/modeling/assumptions/independence/",
    label: "Lesson 3 — Independence",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 4</span>
      <span class="badge">Lesson 3</span>
      <span class="badge">Independence</span>
      <span class="badge">Residuals</span>
    </div>

    <h1>3. Independence</h1>

    <p class="lead">
      The independence assumption requires that residuals are not related to each other.
      Violations can lead to misleading conclusions even if the model appears to fit well.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/assumptions/">Back to Block 4</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding before time-series extensions.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what independence means in regression
    and why it is essential for valid inference.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      The errors (residuals) in a regression model should be independent of each other.
    </p>
  </div>

  <h2>1) What does independence mean?</h2>
  <div class="card">
    <p>
      Independence means that the error for one observation does not depend on
      the error of another observation.
    </p>
  </div>

  <h2>2) Important clarification</h2>
  <div class="card">
    <p>
      Independence refers to <strong>residuals</strong>, not necessarily the predictors.
    </p>
  </div>

  <h2>3) Example of independence</h2>
  <div class="card">
    <p>
      Observations collected randomly from a population are often approximately independent.
    </p>
  </div>

  <h2>4) Example of violation</h2>
  <div class="card">
    <p>
      Time series data:
    </p>
    <ul>
      <li>Today’s value depends on yesterday’s value</li>
      <li>Errors are correlated over time</li>
    </ul>
  </div>

  <h2>5) Consequences of violation</h2>
  <div class="card">
    <ul>
      <li>Standard errors become incorrect</li>
      <li>Confidence intervals become unreliable</li>
      <li>Hypothesis tests may be invalid</li>
    </ul>
  </div>

  <h2>6) What independence does NOT affect</h2>
  <div class="card">
    <p>
      Model predictions may still be reasonable,
      but inference becomes unreliable.
    </p>
  </div>

  <h2>7) How violations appear</h2>
  <div class="card">
    <p>
      Residuals show patterns over time or ordering,
      instead of random behavior.
    </p>
  </div>

  <h2>8) Common situations</h2>
  <div class="card">
    <ul>
      <li>Time series data</li>
      <li>Repeated measurements</li>
      <li>Clustered or grouped data</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Independence is crucial for valid statistical inference,
      even if the model appears to fit the data well.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand independence of residuals</li>
      <li>Distinguish data vs error independence</li>
      <li>Recognize violations conceptually</li>
      <li>Understand consequences for inference</li>
      <li>Prepare for variance-related assumptions</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now examine homoscedasticity,
      which concerns the consistency of variance in residuals.
    </p>
    <a class="btn" href="/modeling/assumptions/homoscedasticity/">
      Next lesson: Homoscedasticity →
    </a>
  </div>

</section>