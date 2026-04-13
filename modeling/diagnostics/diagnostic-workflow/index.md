---
layout: default
title: 9. Diagnostic Workflow
permalink: /modeling/diagnostics/diagnostic-workflow/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 integrates all diagnostic tools into a coherent workflow.
      Advanced decision strategies will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_diagnostics_lesson_v0", JSON.stringify({
    url: "/modeling/diagnostics/diagnostic-workflow/",
    label: "Lesson 9 — Diagnostic Workflow",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 5</span>
      <span class="badge">Lesson 9</span>
      <span class="badge">Workflow</span>
      <span class="badge">Integration</span>
    </div>

    <h1>9. Diagnostic Workflow</h1>

    <p class="lead">
      Diagnostic tools are only useful when applied systematically.
      This lesson provides a structured workflow for evaluating regression models.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/diagnostics/">Back to Block 5</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: practical workflow for real-world modeling.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should be able to apply a complete diagnostic workflow
    to evaluate and improve regression models.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Diagnostics is not a single check — it is a structured process.
    </p>
  </div>

  <h2>1) Why a workflow is needed</h2>
  <div class="card">
    <p>
      Individual diagnostics are useful, but without structure,
      important problems may be missed.
    </p>
  </div>

  <h2>2) Step 1 — Check residual plots</h2>
  <div class="card">
    <ul>
      <li>Look for patterns</li>
      <li>Detect nonlinearity</li>
      <li>Check variance consistency</li>
    </ul>
  </div>

  <h2>3) Step 2 — Check assumptions</h2>
  <div class="card">
    <ul>
      <li>Linearity</li>
      <li>Independence</li>
      <li>Homoscedasticity</li>
      <li>Normality</li>
    </ul>
  </div>

  <h2>4) Step 3 — Identify outliers</h2>
  <div class="card">
    <ul>
      <li>Large residuals</li>
      <li>Standardized residuals</li>
    </ul>
  </div>

  <h2>5) Step 4 — Check leverage</h2>
  <div class="card">
    <p>
      Identify observations with extreme predictor values.
    </p>
  </div>

  <h2>6) Step 5 — Evaluate influence</h2>
  <div class="card">
    <ul>
      <li>Combine residual + leverage</li>
      <li>Use Cook’s Distance</li>
    </ul>
  </div>

  <h2>7) Step 6 — Investigate problematic points</h2>
  <div class="card">
    <ul>
      <li>Check for data errors</li>
      <li>Understand context</li>
      <li>Compare models</li>
    </ul>
  </div>

  <h2>8) Step 7 — Improve the model</h2>
  <div class="card">
    <ul>
      <li>Transform variables</li>
      <li>Add missing predictors</li>
      <li>Change model form</li>
    </ul>
  </div>

  <h2>9) Step 8 — Re-evaluate</h2>
  <div class="card">
    <p>
      Diagnostics is iterative — repeat checks after modifications.
    </p>
  </div>

  <h2>10) Common mistake</h2>
  <div class="card">
    <p>
      Treating diagnostics as a one-time step instead of an iterative process.
    </p>
  </div>

  <h2>11) Why this matters</h2>
  <div class="card">
    <p>
      A structured workflow ensures that models are valid, reliable,
      and interpretable.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Apply a full diagnostic workflow</li>
      <li>Integrate all diagnostic tools</li>
      <li>Identify and fix model problems</li>
      <li>Think like a statistical practitioner</li>
      <li>Prepare for model comparison</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now move to evaluating and comparing models.
    </p>
    <a class="btn" href="/modeling/model-fit-comparison/">
      Next block: Model Fit & Comparison →
    </a>
  </div>

</section>