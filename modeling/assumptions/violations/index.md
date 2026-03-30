---
layout: default
title: 7. Violations of Assumptions
permalink: /modeling/assumptions/violations/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 integrates all regression assumptions and explains what happens
      when they are violated. Formal diagnostics are introduced in the next block.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_assumptions_lesson_v0", JSON.stringify({
    url: "/modeling/assumptions/violations/",
    label: "Lesson 7 — Violations of Assumptions",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 4</span>
      <span class="badge">Lesson 7</span>
      <span class="badge">Violations</span>
      <span class="badge">Interpretation</span>
    </div>

    <h1>7. Violations of Assumptions</h1>

    <p class="lead">
      Regression assumptions define when model-based conclusions are valid.
      When assumptions are violated, results can become unreliable or misleading.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/assumptions/">Back to Block 4</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual integration before diagnostics and corrections.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand how violations affect models,
    and how to interpret results when assumptions are not fully satisfied.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Violations do not always destroy a model, but they change how results should be interpreted.
    </p>
  </div>

  <h2>1) What is a violation?</h2>
  <div class="card">
    <p>
      A violation occurs when one or more assumptions of the regression model are not satisfied.
    </p>
  </div>

  <h2>2) Types of violations</h2>
  <div class="card">
    <ul>
      <li><strong>Linearity violation:</strong> relationship is not linear</li>
      <li><strong>Independence violation:</strong> errors are correlated</li>
      <li><strong>Heteroscedasticity:</strong> non-constant variance</li>
      <li><strong>Non-normality:</strong> residuals are not normally distributed</li>
      <li><strong>Outliers:</strong> extreme or influential observations</li>
    </ul>
  </div>

  <h2>3) Do violations always matter?</h2>
  <div class="card">
    <p>
      Not all violations are equally serious. The impact depends on:
    </p>
    <ul>
      <li>Sample size</li>
      <li>Purpose of the model (prediction vs inference)</li>
      <li>Severity of the violation</li>
    </ul>
  </div>

  <h2>4) Effect on estimation</h2>
  <div class="card">
    <p>
      Some violations do not affect coefficient estimates directly,
      especially in large samples.
    </p>
  </div>

  <h2>5) Effect on inference</h2>
  <div class="card">
    <ul>
      <li>Standard errors may be incorrect</li>
      <li>Confidence intervals may be misleading</li>
      <li>Hypothesis tests may give wrong conclusions</li>
    </ul>
  </div>

  <h2>6) Prediction vs inference</h2>
  <div class="card">
    <p>
      Models can still predict reasonably well even when assumptions are violated,
      but inference becomes unreliable.
    </p>
  </div>

  <h2>7) Mild vs severe violations</h2>
  <div class="card">
    <ul>
      <li><strong>Mild:</strong> results still usable with caution</li>
      <li><strong>Severe:</strong> model may be invalid</li>
    </ul>
  </div>

  <h2>8) What to do when violations occur</h2>
  <div class="card">
    <ul>
      <li>Check model specification</li>
      <li>Transform variables</li>
      <li>Use robust methods</li>
      <li>Investigate outliers</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Understanding violations allows you to interpret models responsibly
      rather than blindly trusting output.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand types of assumption violations</li>
      <li>Evaluate their impact on models</li>
      <li>Distinguish prediction vs inference effects</li>
      <li>Recognize when results are unreliable</li>
      <li>Prepare for robustness concepts</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now study robustness: when models still work despite violations.
    </p>
    <a class="btn" href="/modeling/assumptions/robustness/">
      Next lesson: Robustness →
    </a>
  </div>

</section>