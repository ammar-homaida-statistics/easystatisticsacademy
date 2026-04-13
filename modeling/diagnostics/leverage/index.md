---
layout: default
title: 6. Leverage
permalink: /modeling/diagnostics/leverage/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding leverage conceptually.
      Formal influence measures will follow in the next lesson.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_diagnostics_lesson_v0", JSON.stringify({
    url: "/modeling/diagnostics/leverage/",
    label: "Lesson 6 — Leverage",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 5</span>
      <span class="badge">Lesson 6</span>
      <span class="badge">Leverage</span>
      <span class="badge">Predictors</span>
    </div>

    <h1>6. Leverage</h1>

    <p class="lead">
      Leverage measures how extreme an observation is in terms of predictor values.
      High-leverage points have the potential to strongly influence the regression model.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/diagnostics/">Back to Block 5</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding before influence measures.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what leverage is,
    how it differs from outliers, and why it matters in regression analysis.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Leverage depends on how far an observation's predictor values are from the center of the data.
    </p>
  </div>

  <h2>1) What is leverage?</h2>
  <div class="card">
    <p>
      Leverage measures how unusual an observation is in terms of its predictor (X) values.
    </p>
  </div>

  <h2>2) High vs low leverage</h2>
  <div class="card">
    <ul>
      <li>High leverage → extreme X values</li>
      <li>Low leverage → typical X values</li>
    </ul>
  </div>

  <h2>3) Example</h2>
  <div class="card">
    <p>
      In a dataset of heights:
    </p>
    <ul>
      <li>Average values → low leverage</li>
      <li>Very extreme values → high leverage</li>
    </ul>
  </div>

  <h2>4) Leverage vs outliers</h2>
  <div class="card">
    <ul>
      <li>Leverage → unusual X values</li>
      <li>Outlier → unusual Y values (large residual)</li>
    </ul>
  </div>

  <h2>5) Why leverage matters</h2>
  <div class="card">
    <p>
      High-leverage points can strongly affect the regression line,
      even if they are not outliers.
    </p>
  </div>

  <h2>6) When leverage is dangerous</h2>
  <div class="card">
    <ul>
      <li>High leverage + large residual → very influential</li>
      <li>High leverage + small residual → less problematic</li>
    </ul>
  </div>

  <h2>7) How leverage appears</h2>
  <div class="card">
    <p>
      Points far from the center of the X distribution
      often have high leverage.
    </p>
  </div>

  <h2>8) Common misunderstanding</h2>
  <div class="card">
    <p>
      Not all high-leverage points are problematic.
      They only become problematic when combined with large residuals.
    </p>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Understanding leverage helps identify points that can control the model,
      even if they do not appear unusual at first.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define leverage clearly</li>
      <li>Distinguish leverage vs outliers</li>
      <li>Recognize high-leverage points</li>
      <li>Understand their potential impact</li>
      <li>Prepare for influence measures</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now combine residuals and leverage to study influence,
      which identifies points that actually change the model.
    </p>
    <a class="btn" href="/modeling/diagnostics/influence/">
      Next lesson: Influence →
    </a>
  </div>

</section>