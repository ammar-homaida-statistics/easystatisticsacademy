---
layout: default
title: 3. Nonlinearity
permalink: /modeling/diagnostics/nonlinearity/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on detecting nonlinearity using residual plots.
      Model correction techniques will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_diagnostics_lesson_v0", JSON.stringify({
    url: "/modeling/diagnostics/nonlinearity/",
    label: "Lesson 3 — Nonlinearity",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 5</span>
      <span class="badge">Lesson 3</span>
      <span class="badge">Nonlinearity</span>
      <span class="badge">Model Form</span>
    </div>

    <h1>3. Nonlinearity</h1>

    <p class="lead">
      Nonlinearity occurs when the model fails to capture the true relationship between variables.
      Residual plots reveal this problem through systematic patterns.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/diagnostics/">Back to Block 5</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: identifying nonlinearity visually using residual patterns.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should be able to detect nonlinearity
    and understand its impact on regression models.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      If residuals show a pattern, the model form is incorrect.
    </p>
  </div>

  <h2>1) What is nonlinearity?</h2>
  <div class="card">
    <p>
      Nonlinearity occurs when the relationship between predictors and the outcome
      is not correctly captured by a linear model.
    </p>
  </div>

  <h2>2) How to detect nonlinearity</h2>
  <div class="card">
    <p>
      Use a residual plot:
    </p>
    <ul>
      <li>Look for curves or systematic shapes</li>
      <li>Residuals should NOT form patterns</li>
    </ul>
  </div>

  <h2>3) Typical patterns</h2>
  <div class="card">
    <ul>
      <li>U-shape → missing quadratic term</li>
      <li>Inverted U → wrong functional form</li>
      <li>Wave pattern → complex relationship</li>
    </ul>
  </div>

  <h2>4) Why it is a problem</h2>
  <div class="card">
    <ul>
      <li>Biased estimates</li>
      <li>Incorrect interpretation</li>
      <li>Poor predictions</li>
    </ul>
  </div>

  <h2>5) Real meaning</h2>
  <div class="card">
    <p>
      The model is missing structure that exists in the data.
    </p>
  </div>

  <h2>6) Fixing nonlinearity</h2>
  <div class="card">
    <ul>
      <li>Add polynomial terms (X², X³)</li>
      <li>Transform variables (log, sqrt)</li>
      <li>Use more flexible models</li>
    </ul>
  </div>

  <h2>7) Common mistake</h2>
  <div class="card">
    <p>
      Assuming linear models are always appropriate.
      Many real-world relationships are nonlinear.
    </p>
  </div>

  <h2>8) Connection to assumptions</h2>
  <div class="card">
    <p>
      Nonlinearity is a violation of the linearity assumption.
    </p>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      If the model form is wrong, all conclusions drawn from the model can be misleading.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Detect nonlinearity using residual plots</li>
      <li>Recognize common patterns</li>
      <li>Understand consequences of misspecification</li>
      <li>Know basic fixes</li>
      <li>Prepare for variance-related diagnostics</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now examine heteroscedasticity,
      where residual variance changes across values.
    </p>
    <a class="btn" href="/modeling/diagnostics/heteroscedasticity/">
      Next lesson: Heteroscedasticity →
    </a>
  </div>

</section>