---
layout: default
title: 2. R² (Coefficient of Determination)
permalink: /modeling/model-fit-comparison/r-squared/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding R² conceptually and correctly.
      Misinterpretations are explicitly addressed.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_model_fit_lesson_v0", JSON.stringify({
    url: "/modeling/model-fit-comparison/r-squared/",
    label: "Lesson 2 — R²",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 6</span>
      <span class="badge">Lesson 2</span>
      <span class="badge">R²</span>
      <span class="badge">Explained Variance</span>
    </div>

    <h1>2. R² (Coefficient of Determination)</h1>

    <p class="lead">
      R² measures how much of the variation in the outcome variable
      is explained by the model.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/model-fit-comparison/">Back to Block 6</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: correct interpretation before extensions.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what R² measures,
    how to interpret it, and what it does NOT mean.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      R² is the proportion of variation in the outcome explained by the model.
    </p>
  </div>

  <h2>1) What is R²?</h2>
  <div class="card">
    <p>
      R² (coefficient of determination) quantifies how well the model explains variability in the data.
    </p>
  </div>

  <h2>2) Interpretation</h2>
  <div class="card">
    <p>
      Example:
    </p>
    <ul>
      <li>R² = 0.80 → 80% of variation is explained</li>
      <li>R² = 0.20 → 20% of variation is explained</li>
    </ul>
  </div>

  <h2>3) Range of values</h2>
  <div class="card">
    <ul>
      <li>0 ≤ R² ≤ 1 (in standard regression)</li>
      <li>Closer to 1 → better fit</li>
      <li>Closer to 0 → weaker fit</li>
    </ul>
  </div>

  <h2>4) Connection to residuals</h2>
  <div class="card">
    <p>
      Higher R² → smaller residuals on average.
    </p>
  </div>

  <h2>5) What R² measures</h2>
  <div class="card">
    <ul>
      <li>Explained variation</li>
      <li>Model fit (partially)</li>
    </ul>
  </div>

  <h2>6) What R² does NOT measure</h2>
  <div class="card">
    <ul>
      <li>Correctness of the model</li>
      <li>Causality</li>
      <li>Whether assumptions hold</li>
      <li>Prediction quality on new data</li>
    </ul>
  </div>

  <h2>7) Important limitation</h2>
  <div class="card">
    <p>
      R² always increases when more variables are added,
      even if they are not meaningful.
    </p>
  </div>

  <h2>8) Common misunderstanding</h2>
  <div class="card">
    <p>
      High R² does not mean the model is correct or useful.
    </p>
  </div>

  <h2>9) Low R² can still be useful</h2>
  <div class="card">
    <p>
      In many real-world settings (e.g., social sciences),
      useful models may have low R².
    </p>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      R² is widely used, but often misinterpreted.
      Correct understanding is essential.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand R² conceptually</li>
      <li>Interpret values correctly</li>
      <li>Avoid common misconceptions</li>
      <li>Recognize limitations</li>
      <li>Prepare for adjusted R²</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now introduce adjusted R²,
      which corrects for the number of predictors in the model.
    </p>
    <a class="btn" href="/modeling/model-fit-comparison/adjusted-r-squared/">
      Next lesson: Adjusted R² →
    </a>
  </div>

</section>