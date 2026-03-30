---
layout: default
title: 5. Normality
permalink: /modeling/assumptions/normality/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding the role of normality in regression.
      Formal tests and diagnostics will be introduced later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_assumptions_lesson_v0", JSON.stringify({
    url: "/modeling/assumptions/normality/",
    label: "Lesson 5 — Normality",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 4</span>
      <span class="badge">Lesson 5</span>
      <span class="badge">Normality</span>
      <span class="badge">Residuals</span>
    </div>

    <h1>5. Normality</h1>

    <p class="lead">
      The normality assumption requires that residuals follow an approximately normal distribution.
      This assumption is mainly important for inference, not for estimating the model.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/assumptions/">Back to Block 4</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding before formal tests and diagnostics.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what normality means,
    when it matters, and when it does not.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Residuals should be approximately normally distributed, especially for valid statistical inference.
    </p>
  </div>

  <h2>1) What does normality mean?</h2>
  <div class="card">
    <p>
      The residuals follow a bell-shaped, symmetric distribution centered around zero.
    </p>
  </div>

  <h2>2) Important clarification</h2>
  <div class="card">
    <p>
      Normality applies to <strong>residuals</strong>, not the predictors or the outcome variable itself.
    </p>
  </div>

  <h2>3) Why normality is assumed</h2>
  <div class="card">
    <ul>
      <li>To justify confidence intervals</li>
      <li>To justify hypothesis tests</li>
      <li>To obtain valid p-values</li>
    </ul>
  </div>

  <h2>4) What normality does NOT affect</h2>
  <div class="card">
    <p>
      Regression coefficients can still be estimated correctly even if residuals are not normal.
    </p>
  </div>

  <h2>5) When normality matters most</h2>
  <div class="card">
    <ul>
      <li>Small sample sizes</li>
      <li>Formal inference (tests and intervals)</li>
    </ul>
  </div>

  <h2>6) When it matters less</h2>
  <div class="card">
    <ul>
      <li>Large samples (Central Limit Theorem)</li>
      <li>Pure prediction tasks</li>
    </ul>
  </div>

  <h2>7) Signs of non-normality</h2>
  <div class="card">
    <ul>
      <li>Skewed distribution</li>
      <li>Heavy tails</li>
      <li>Extreme outliers</li>
    </ul>
  </div>

  <h2>8) Common causes</h2>
  <div class="card">
    <ul>
      <li>Outliers</li>
      <li>Incorrect model specification</li>
      <li>Nonlinear relationships</li>
    </ul>
  </div>

  <h2>9) What to do if violated</h2>
  <div class="card">
    <ul>
      <li>Transform variables</li>
      <li>Use robust methods</li>
      <li>Improve model specification</li>
    </ul>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      Normality ensures that uncertainty is modeled correctly,
      especially in small samples.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand normality of residuals</li>
      <li>Distinguish estimation vs inference roles</li>
      <li>Recognize when violations matter</li>
      <li>Identify common causes of non-normality</li>
      <li>Prepare for diagnostic tools</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now examine outliers and their impact on regression models.
    </p>
    <a class="btn" href="/modeling/assumptions/outliers/">
      Next lesson: Outliers →
    </a>
  </div>

</section>