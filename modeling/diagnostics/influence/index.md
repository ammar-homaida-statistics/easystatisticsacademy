---
layout: default
title: 7. Influence
permalink: /modeling/diagnostics/influence/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding influence conceptually.
      Formal influence measures will be introduced next.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_diagnostics_lesson_v0", JSON.stringify({
    url: "/modeling/diagnostics/influence/",
    label: "Lesson 7 — Influence",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 5</span>
      <span class="badge">Lesson 7</span>
      <span class="badge">Influence</span>
      <span class="badge">Model Impact</span>
    </div>

    <h1>7. Influence</h1>

    <p class="lead">
      Influence measures how much a single observation affects the regression model.
      It combines residual size and leverage to determine impact.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/diagnostics/">Back to Block 5</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding before numerical measures.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what influence is,
    how it is formed, and why it is critical in regression diagnostics.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Influence depends on both residual size and leverage.
    </p>
  </div>

  <h2>1) What is influence?</h2>
  <div class="card">
    <p>
      Influence measures how much a single observation changes the fitted model.
    </p>
  </div>

  <h2>2) Conceptual definition</h2>
  <div class="card">
    <p>
      An observation is influential if removing it significantly changes:
    </p>
    <ul>
      <li>Regression coefficients</li>
      <li>Predictions</li>
      <li>Model fit</li>
    </ul>
  </div>

  <h2>3) Influence = residual + leverage</h2>
  <div class="card">
    <p>
      Influence occurs when:
    </p>
    <ul>
      <li>Residual is large (outlier)</li>
      <li>Leverage is high (extreme X)</li>
    </ul>
  </div>

  <h2>4) Key combinations</h2>
  <div class="card">
    <ul>
      <li>Low leverage + large residual → limited influence</li>
      <li>High leverage + small residual → limited influence</li>
      <li>High leverage + large residual → strong influence</li>
    </ul>
  </div>

  <h2>5) Why influence matters</h2>
  <div class="card">
    <p>
      Influential points can completely change model conclusions,
      including slope, interpretation, and predictions.
    </p>
  </div>

  <h2>6) Visual intuition</h2>
  <div class="card">
    <p>
      Removing an influential point can cause the regression line to shift noticeably.
    </p>
  </div>

  <h2>7) Common misunderstanding</h2>
  <div class="card">
    <p>
      Not all outliers are influential.
      Not all high-leverage points are influential.
    </p>
  </div>

  <h2>8) What to do with influential points</h2>
  <div class="card">
    <ul>
      <li>Investigate the observation</li>
      <li>Check for errors</li>
      <li>Compare models with and without the point</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Influence determines whether individual observations dominate the model,
      which is critical for reliable interpretation.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define influence clearly</li>
      <li>Understand residual + leverage interaction</li>
      <li>Identify influential scenarios</li>
      <li>Interpret model sensitivity</li>
      <li>Prepare for formal influence measures</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now introduce Cook’s Distance,
      a formal measure of influence in regression.
    </p>
    <a class="btn" href="/modeling/diagnostics/cooks-distance/">
      Next lesson: Cook’s Distance →
    </a>
  </div>

</section>