---
layout: default
title: 8. AIC & BIC
permalink: /modeling/model-fit-comparison/aic-bic/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces AIC and BIC conceptually.
      Mathematical details and derivations will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_model_fit_lesson_v0", JSON.stringify({
    url: "/modeling/model-fit-comparison/aic-bic/",
    label: "Lesson 8 — AIC & BIC",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 6</span>
      <span class="badge">Lesson 8</span>
      <span class="badge">AIC</span>
      <span class="badge">BIC</span>
    </div>

    <h1>8. AIC & BIC</h1>

    <p class="lead">
      AIC and BIC are formal criteria used to compare models by balancing fit and complexity.
      They penalize overly complex models to reduce overfitting.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/model-fit-comparison/">Back to Block 6</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding before formulas.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand how AIC and BIC
    are used to compare models and control complexity.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      AIC and BIC reward good fit but penalize model complexity.
    </p>
  </div>

  <h2>1) Why we need AIC/BIC</h2>
  <div class="card">
    <p>
      R² and adjusted R² are not always sufficient for comparing models,
      especially in more complex settings.
    </p>
  </div>

  <h2>2) Core principle</h2>
  <div class="card">
    <p>
      AIC and BIC balance:
    </p>
    <ul>
      <li>Model fit (how well the model explains data)</li>
      <li>Model complexity (number of parameters)</li>
    </ul>
  </div>

  <h2>3) Interpretation</h2>
  <div class="card">
    <p>
      Lower AIC or BIC values indicate better models.
    </p>
  </div>

  <h2>4) AIC vs BIC</h2>
  <div class="card">
    <ul>
      <li>AIC → lighter penalty for complexity</li>
      <li>BIC → stronger penalty for complexity</li>
    </ul>
  </div>

  <h2>5) Model selection use</h2>
  <div class="card">
    <p>
      Used to compare multiple models and choose the one with the lowest value.
    </p>
  </div>

  <h2>6) Important property</h2>
  <div class="card">
    <p>
      Values are only meaningful relative to other models,
      not in isolation.
    </p>
  </div>

  <h2>7) Connection to overfitting</h2>
  <div class="card">
    <p>
      Penalization helps prevent selecting overly complex models.
    </p>
  </div>

  <h2>8) Common mistake</h2>
  <div class="card">
    <p>
      Interpreting AIC or BIC as absolute measures of model quality.
    </p>
  </div>

  <h2>9) When to use them</h2>
  <div class="card">
    <ul>
      <li>Comparing multiple models</li>
      <li>Variable selection</li>
      <li>Complex modeling scenarios</li>
    </ul>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      AIC and BIC provide a principled way to balance fit and simplicity.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand AIC and BIC conceptually</li>
      <li>Compare models using formal criteria</li>
      <li>Balance fit and complexity</li>
      <li>Avoid overfitting in selection</li>
      <li>Prepare for modeling strategy</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now develop a structured way of thinking about model selection.
    </p>
    <a class="btn" href="/modeling/model-fit-comparison/model-selection-thinking/">
      Next lesson: Model Selection Thinking →
    </a>
  </div>

</section>