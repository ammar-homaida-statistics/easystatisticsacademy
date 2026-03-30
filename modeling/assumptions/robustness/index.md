---
layout: default
title: 8. Robustness
permalink: /modeling/assumptions/robustness/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 explains when regression models remain reliable despite assumption violations.
      Practical robustness techniques will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_assumptions_lesson_v0", JSON.stringify({
    url: "/modeling/assumptions/robustness/",
    label: "Lesson 8 — Robustness",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 4</span>
      <span class="badge">Lesson 8</span>
      <span class="badge">Robustness</span>
      <span class="badge">Reliability</span>
    </div>

    <h1>8. Robustness</h1>

    <p class="lead">
      Robustness describes how well a model continues to perform when assumptions are not perfectly satisfied.
      Not all violations are fatal—some models remain reliable under mild deviations.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/assumptions/">Back to Block 4</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual robustness before formal robust methods.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand when regression results remain trustworthy
    despite violations, and when they do not.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A model is robust if small violations of assumptions do not significantly affect its conclusions.
    </p>
  </div>

  <h2>1) What is robustness?</h2>
  <div class="card">
    <p>
      Robustness refers to the stability of model results under imperfect conditions.
    </p>
  </div>

  <h2>2) Why robustness matters</h2>
  <div class="card">
    <p>
      Real-world data rarely satisfy all assumptions perfectly.
      Robustness allows models to still be useful in practice.
    </p>
  </div>

  <h2>3) When models are robust</h2>
  <div class="card">
    <ul>
      <li>Large sample sizes (Central Limit Theorem)</li>
      <li>Mild deviations from assumptions</li>
      <li>Balanced and well-behaved data</li>
    </ul>
  </div>

  <h2>4) When models are NOT robust</h2>
  <div class="card">
    <ul>
      <li>Strong outliers</li>
      <li>Severe heteroscedasticity</li>
      <li>Strong dependence (e.g., time series)</li>
      <li>Highly misspecified models</li>
    </ul>
  </div>

  <h2>5) Robustness and sample size</h2>
  <div class="card">
    <p>
      Larger samples often reduce the impact of violations,
      especially for inference.
    </p>
  </div>

  <h2>6) Robustness vs correctness</h2>
  <div class="card">
    <p>
      A robust model may still give useful results,
      but it is not necessarily fully correct.
    </p>
  </div>

  <h2>7) Practical interpretation</h2>
  <div class="card">
    <ul>
      <li>Do not assume perfection</li>
      <li>Evaluate severity of violations</li>
      <li>Interpret results with appropriate caution</li>
    </ul>
  </div>

  <h2>8) Improving robustness</h2>
  <div class="card">
    <ul>
      <li>Transform variables</li>
      <li>Use robust standard errors</li>
      <li>Use alternative models</li>
      <li>Investigate influential points</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Robustness allows statistical modeling to remain useful in real-world applications,
      where ideal conditions rarely exist.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand the concept of robustness</li>
      <li>Recognize when models remain reliable</li>
      <li>Identify situations where robustness fails</li>
      <li>Interpret results under imperfect assumptions</li>
      <li>Prepare for diagnostic tools</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now move to diagnostics, where we learn how to detect and evaluate assumption violations in practice.
    </p>
    <a class="btn" href="/modeling/diagnostics/">
      Next: Block 5 — Diagnostics →
    </a>
  </div>

</section>