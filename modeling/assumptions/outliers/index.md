---
layout: default
title: 6. Outliers
permalink: /modeling/assumptions/outliers/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding outliers conceptually.
      Formal influence measures will be covered in the diagnostics block.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_assumptions_lesson_v0", JSON.stringify({
    url: "/modeling/assumptions/outliers/",
    label: "Lesson 6 — Outliers",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 4</span>
      <span class="badge">Lesson 6</span>
      <span class="badge">Outliers</span>
      <span class="badge">Influence</span>
    </div>

    <h1>6. Outliers</h1>

    <p class="lead">
      Outliers are observations that deviate strongly from the general pattern.
      They can distort model estimates, violate assumptions, and lead to misleading conclusions.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/assumptions/">Back to Block 4</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding before formal diagnostics.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what outliers are,
    how they affect models, and why they must be handled carefully.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Outliers are observations that differ substantially from the pattern
      explained by the model.
    </p>
  </div>

  <h2>1) What is an outlier?</h2>
  <div class="card">
    <p>
      An outlier is a data point that lies far from the fitted regression line
      or from the general trend of the data.
    </p>
  </div>

  <h2>2) Types of outliers</h2>
  <div class="card">
    <ul>
      <li><strong>Response outliers:</strong> unusual y-values</li>
      <li><strong>Predictor outliers:</strong> unusual x-values</li>
      <li><strong>Influential points:</strong> strongly affect the model</li>
    </ul>
  </div>

  <h2>3) Why outliers matter</h2>
  <div class="card">
    <ul>
      <li>They can distort regression coefficients</li>
      <li>They can inflate or reduce R²</li>
      <li>They can affect inference results</li>
    </ul>
  </div>

  <h2>4) Example</h2>
  <div class="card">
    <p>
      A single extreme observation can pull the regression line
      toward itself, changing slope and interpretation.
    </p>
  </div>

  <h2>5) Outliers and assumptions</h2>
  <div class="card">
    <ul>
      <li>Can break normality</li>
      <li>Can create heteroscedasticity</li>
      <li>Can distort independence patterns</li>
    </ul>
  </div>

  <h2>6) Outlier ≠ error</h2>
  <div class="card">
    <p>
      Not all outliers are mistakes. Some represent real and important phenomena.
    </p>
  </div>

  <h2>7) When to be careful</h2>
  <div class="card">
    <ul>
      <li>Small datasets</li>
      <li>High-leverage points</li>
      <li>Strong influence on coefficients</li>
    </ul>
  </div>

  <h2>8) Common causes</h2>
  <div class="card">
    <ul>
      <li>Measurement errors</li>
      <li>Data entry errors</li>
      <li>True extreme values</li>
      <li>Model misspecification</li>
    </ul>
  </div>

  <h2>9) What NOT to do</h2>
  <div class="card">
    <ul>
      <li>Do not remove outliers blindly</li>
      <li>Do not ignore them without investigation</li>
    </ul>
  </div>

  <h2>10) What to do instead</h2>
  <div class="card">
    <ul>
      <li>Investigate their origin</li>
      <li>Check model specification</li>
      <li>Use robust methods if needed</li>
    </ul>
  </div>

  <h2>11) Why this matters</h2>
  <div class="card">
    <p>
      Outliers can completely change conclusions if not handled properly.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand what outliers are</li>
      <li>Distinguish types of outliers</li>
      <li>Understand their impact on models</li>
      <li>Recognize when they are problematic</li>
      <li>Prepare for formal diagnostics</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now bring all assumptions together and study violations and their consequences.
    </p>
    <a class="btn" href="/modeling/assumptions/violations/">
      Next lesson: Violations →
    </a>
  </div>

</section>