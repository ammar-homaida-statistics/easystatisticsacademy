---
layout: default
title: 7. R² (Coefficient of Determination)
permalink: /modeling/simple-linear-regression/r-squared/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on interpreting R² conceptually.
      Mathematical decomposition and extensions will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_slr_lesson_v0", JSON.stringify({
    url: "/modeling/simple-linear-regression/r-squared/",
    label: "Lesson 7 — R²",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 2</span>
      <span class="badge">Lesson 7</span>
      <span class="badge">R²</span>
      <span class="badge">Model Fit</span>
    </div>

    <h1>7. R² (Coefficient of Determination)</h1>

    <p class="lead">
      R² measures how much of the variation in the response variable
      is explained by the model.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/simple-linear-regression/">Back to Block 2</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: interpretation-first. Avoid formula memorization.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what R² represents,
    how to interpret it, and its limitations.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      R² is the proportion of total variation in Y that is explained by the model.
    </p>
  </div>

  <h2>1) What does R² measure?</h2>
  <div class="card">
    <p>
      R² answers the question:
    </p>
    <p><strong>How much of the variability in Y is explained by X?</strong></p>
  </div>

  <h2>2) Interpretation</h2>
  <div class="card">
    <p>
      R² ranges from 0 to 1:
    </p>
    <ul>
      <li><strong>R² = 0</strong> → model explains none of the variation</li>
      <li><strong>R² = 1</strong> → model explains all variation (perfect fit)</li>
    </ul>
  </div>

  <h2>3) Example</h2>
  <div class="card">
    <p>
      If R² = 0.70:
    </p>
    <p>
      70% of the variation in the response variable is explained by the model,
      and 30% remains unexplained (noise).
    </p>
  </div>

  <h2>4) Connection to signal vs noise</h2>
  <div class="card">
    <ul>
      <li><strong>Explained variation</strong> → signal</li>
      <li><strong>Unexplained variation</strong> → noise</li>
    </ul>
  </div>

  <h2>5) R² and residuals</h2>
  <div class="card">
    <p>
      Smaller residuals generally lead to higher R².
      Better fit → more explained variation.
    </p>
  </div>

  <h2>6) What R² does NOT tell you</h2>
  <div class="card">
    <ul>
      <li>Does not imply causation</li>
      <li>Does not guarantee a good model</li>
      <li>Does not detect model misspecification</li>
    </ul>
  </div>

  <h2>7) High vs low R²</h2>
  <div class="card">
    <ul>
      <li>High R² → strong relationship (but not necessarily correct)</li>
      <li>Low R² → weak relationship (may still be useful)</li>
    </ul>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      R² is widely used but often misunderstood.
      Correct interpretation is essential for evaluating models.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define R² correctly</li>
      <li>Interpret R² values</li>
      <li>Connect R² to variation and noise</li>
      <li>Avoid common misconceptions</li>
      <li>Understand its limitations</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we distinguish two related but different concepts:
      correlation and regression.
    </p>
    <a class="btn" href="/modeling/simple-linear-regression/correlation-vs-regression/">
      Next lesson: Correlation vs Regression →
    </a>
  </div>

</section>