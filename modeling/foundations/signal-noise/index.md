---
layout: default
title: 3. Signal vs Noise
permalink: /modeling/foundations/signal-noise/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on separating systematic structure (signal)
      from randomness (noise). Visual demonstrations will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_foundations_lesson_v0", JSON.stringify({
    url: "/modeling/foundations/signal-noise/",
    label: "Lesson 3 — Signal vs Noise",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 1</span>
      <span class="badge">Lesson 3</span>
      <span class="badge">Signal</span>
      <span class="badge">Noise</span>
    </div>

    <h1>3. Signal vs Noise</h1>

    <p class="lead">
      Every dataset contains both structure and randomness.
      Modeling is the process of separating meaningful patterns (signal)
      from unpredictable variation (noise).
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/foundations/">Back to Block 1</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: intuition-first. Formal definitions and visuals will follow.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand the difference between
    signal and noise, and how models aim to extract signal while accounting for noise.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Observed data = signal + noise.
      A good model captures the signal and leaves only noise unexplained.
    </p>
  </div>

  <h2>1) What is signal?</h2>
  <div class="card">
    <p>
      Signal is the systematic, predictable part of the relationship.
      It represents the underlying structure that we want to learn.
    </p>
  </div>

  <h2>2) What is noise?</h2>
  <div class="card">
    <p>
      Noise is random variation that cannot be explained by the model.
      It comes from measurement error, unobserved factors, or inherent randomness.
    </p>
  </div>

  <h2>3) The basic decomposition</h2>
  <div class="card">
    <p>
      A standard modeling framework:
    </p>
    <p><strong>Observed outcome = signal + noise</strong></p>
    <p><strong>Y = f(X) + ε</strong></p>
    <p>
      The function captures signal, and ε (error) represents noise.
    </p>
  </div>

  <h2>4) Why noise always exists</h2>
  <div class="card">
    <ul>
      <li>Incomplete information (missing variables)</li>
      <li>Measurement error</li>
      <li>Natural randomness</li>
      <li>Unpredictable behavior</li>
    </ul>
  </div>

  <h2>5) Strong vs weak signal</h2>
  <div class="card">
    <ul>
      <li><strong>Strong signal</strong> — clear pattern, low noise</li>
      <li><strong>Weak signal</strong> — pattern hidden by noise</li>
    </ul>
    <p>
      Modeling becomes harder when noise dominates signal.
    </p>
  </div>

  <h2>6) Residuals = estimated noise</h2>
  <div class="card">
    <p>
      After fitting a model, the leftover differences are called residuals.
      These are our estimates of the noise.
    </p>
  </div>

  <h2>7) Overfitting vs underfitting</h2>
  <div class="card">
    <ul>
      <li><strong>Underfitting</strong> — model misses signal</li>
      <li><strong>Overfitting</strong> — model captures noise as if it were signal</li>
    </ul>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Good modeling requires correctly separating signal from noise.
      Mistaking noise for signal leads to poor predictions and false conclusions.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define signal and noise clearly</li>
      <li>Understand the decomposition \(Y = f(X) + ε\)</li>
      <li>Explain why noise is unavoidable</li>
      <li>Understand residuals as estimated noise</li>
      <li>Recognize overfitting vs underfitting</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we define the quantities that describe the model itself:
      parameters.
    </p>
    <a class="btn" href="/modeling/foundations/parameters/">
      Next lesson: Parameters →
    </a>
  </div>

</section>