---
layout: default
title: 7. Model Comparison
permalink: /modeling/model-fit-comparison/model-comparison/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces how to compare models using fit and generalization.
      Formal criteria (AIC/BIC) will follow in the next lesson.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_model_fit_lesson_v0", JSON.stringify({
    url: "/modeling/model-fit-comparison/model-comparison/",
    label: "Lesson 7 — Model Comparison",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 6</span>
      <span class="badge">Lesson 7</span>
      <span class="badge">Model Comparison</span>
      <span class="badge">Selection</span>
    </div>

    <h1>7. Model Comparison</h1>

    <p class="lead">
      Model comparison involves evaluating multiple models
      to select the one that best balances fit and generalization.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/model-fit-comparison/">Back to Block 6</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual model selection framework.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand how to compare models
    and choose between them based on multiple criteria.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      The best model is not the one with the highest fit,
      but the one that generalizes best.
    </p>
  </div>

  <h2>1) Why model comparison is needed</h2>
  <div class="card">
    <p>
      Multiple models can be built from the same data.
      We need a systematic way to choose among them.
    </p>
  </div>

  <h2>2) Comparing based on fit</h2>
  <div class="card">
    <ul>
      <li>R²</li>
      <li>Adjusted R²</li>
    </ul>
  </div>

  <h2>3) Comparing based on generalization</h2>
  <div class="card">
    <ul>
      <li>Train vs test performance</li>
      <li>Prediction accuracy</li>
    </ul>
  </div>

  <h2>4) Trade-off</h2>
  <div class="card">
    <p>
      Better fit often means higher complexity,
      which can lead to overfitting.
    </p>
  </div>

  <h2>5) Ideal model</h2>
  <div class="card">
    <ul>
      <li>Explains the data well</li>
      <li>Generalizes to new data</li>
      <li>Remains interpretable</li>
    </ul>
  </div>

  <h2>6) Example comparison</h2>
  <div class="card">
    <ul>
      <li>Model A: simple, lower R², stable</li>
      <li>Model B: complex, higher R², overfits</li>
    </ul>
  </div>

  <h2>7) Common mistake</h2>
  <div class="card">
    <p>
      Choosing the model with the highest R² without considering generalization.
    </p>
  </div>

  <h2>8) Practical strategy</h2>
  <div class="card">
    <ul>
      <li>Start simple</li>
      <li>Increase complexity gradually</li>
      <li>Evaluate using multiple criteria</li>
    </ul>
  </div>

  <h2>9) Limitations</h2>
  <div class="card">
    <p>
      Informal comparison may not always be sufficient.
      Formal criteria are needed.
    </p>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      Model selection determines the validity of conclusions
      and the quality of predictions.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Compare models systematically</li>
      <li>Balance fit and generalization</li>
      <li>Avoid overfitting in selection</li>
      <li>Understand trade-offs</li>
      <li>Prepare for AIC/BIC</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now introduce formal criteria for model comparison:
      AIC and BIC.
    </p>
    <a class="btn" href="/modeling/model-fit-comparison/aic-bic/">
      Next lesson: AIC & BIC →
    </a>
  </div>

</section>