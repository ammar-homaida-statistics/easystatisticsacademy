---
layout: default
title: 8. Cook’s Distance
permalink: /modeling/diagnostics/cooks-distance/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces Cook’s Distance as a measure of influence.
      Advanced interpretation and thresholds will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_diagnostics_lesson_v0", JSON.stringify({
    url: "/modeling/diagnostics/cooks-distance/",
    label: "Lesson 8 — Cook’s Distance",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 5</span>
      <span class="badge">Lesson 8</span>
      <span class="badge">Cook’s Distance</span>
      <span class="badge">Influence Measure</span>
    </div>

    <h1>8. Cook’s Distance</h1>

    <p class="lead">
      Cook’s Distance is a numerical measure that identifies influential observations.
      It combines residual size and leverage into a single diagnostic value.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/diagnostics/">Back to Block 5</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding before formal computation details.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what Cook’s Distance measures
    and how to use it to detect influential observations.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Cook’s Distance measures how much the regression model changes
      when a single observation is removed.
    </p>
  </div>

  <h2>1) What is Cook’s Distance?</h2>
  <div class="card">
    <p>
      It is a summary measure of influence for each observation.
    </p>
  </div>

  <h2>2) What it combines</h2>
  <div class="card">
    <ul>
      <li>Residual size (error)</li>
      <li>Leverage (position in X)</li>
    </ul>
  </div>

  <h2>3) Interpretation</h2>
  <div class="card">
    <p>
      Large Cook’s Distance → observation strongly affects the model.
    </p>
  </div>

  <h2>4) Rule of thumb</h2>
  <div class="card">
    <ul>
      <li>D > 1 → potentially influential</li>
      <li>Compare values relative to others</li>
    </ul>
  </div>

  <h2>5) What it tells you</h2>
  <div class="card">
    <ul>
      <li>Which observations affect the model most</li>
      <li>Where to investigate further</li>
    </ul>
  </div>

  <h2>6) What it does NOT tell you</h2>
  <div class="card">
    <p>
      It does not tell you whether the observation is correct or should be removed.
    </p>
  </div>

  <h2>7) Visual interpretation</h2>
  <div class="card">
    <p>
      Cook’s Distance is often visualized as a plot,
      where large spikes indicate influential points.
    </p>
  </div>

  <h2>8) Common mistake</h2>
  <div class="card">
    <p>
      Automatically removing points based only on Cook’s Distance.
    </p>
  </div>

  <h2>9) What to do instead</h2>
  <div class="card">
    <ul>
      <li>Investigate the observation</li>
      <li>Compare models with and without it</li>
      <li>Check data quality</li>
    </ul>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      Cook’s Distance provides a practical way to identify observations
      that control the regression model.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand Cook’s Distance conceptually</li>
      <li>Interpret influence values</li>
      <li>Identify influential observations</li>
      <li>Avoid common misuse</li>
      <li>Prepare for full diagnostic workflow</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now integrate all diagnostic tools into a complete workflow.
    </p>
    <a class="btn" href="/modeling/diagnostics/diagnostic-workflow/">
      Next lesson: Diagnostic Workflow →
    </a>
  </div>

</section>