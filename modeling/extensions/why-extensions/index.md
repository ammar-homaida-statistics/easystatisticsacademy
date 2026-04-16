---
layout: default
title: 1. Why Do We Need Extensions?
permalink: /modeling/extensions/why-extensions/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 explains why ordinary linear regression is not sufficient for every modeling problem.
      Specific extensions will be introduced in the next lessons.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_extensions_lesson_v0", JSON.stringify({
    url: "/modeling/extensions/why-extensions/",
    label: "Lesson 1 — Why Do We Need Extensions?",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 7</span>
      <span class="badge">Lesson 1</span>
      <span class="badge">Extensions</span>
      <span class="badge">Limits of Linear Models</span>
    </div>

    <h1>1. Why Do We Need Extensions?</h1>

    <p class="lead">
      Linear regression is powerful, but it is not suitable for every kind of outcome or relationship.
      Extensions are needed when the structure of the data goes beyond what ordinary linear regression can handle.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/extensions/">Back to Block 7</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual bridge from linear regression to broader modeling frameworks.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand why ordinary linear regression has limits
    and why statistical modeling needs extensions.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Different kinds of data require different kinds of models.
      A single modeling framework cannot solve every problem.
    </p>
  </div>

  <h2>1) What linear regression does well</h2>
  <div class="card">
    <p>
      Ordinary linear regression works well when:
    </p>
    <ul>
      <li>The outcome is continuous</li>
      <li>The relationship is modeled appropriately</li>
      <li>The assumptions are reasonably satisfied</li>
    </ul>
  </div>

  <h2>2) Where linear regression begins to fail</h2>
  <div class="card">
    <p>
      Problems arise when the outcome variable or the data structure
      no longer fits the assumptions of ordinary linear regression.
    </p>
  </div>

  <h2>3) Example: binary outcomes</h2>
  <div class="card">
    <p>
      Suppose the outcome is:
    </p>
    <ul>
      <li>Pass / Fail</li>
      <li>Yes / No</li>
      <li>Disease / No disease</li>
    </ul>
    <p>
      Linear regression is not appropriate here because predictions can fall below 0 or above 1.
    </p>
  </div>

  <h2>4) Why this is a problem</h2>
  <div class="card">
    <ul>
      <li>Predicted values may be impossible</li>
      <li>Error structure changes</li>
      <li>Interpretation becomes misleading</li>
    </ul>
  </div>

  <h2>5) More kinds of outcomes</h2>
  <div class="card">
    <p>
      Extensions are also needed for outcomes such as:
    </p>
    <ul>
      <li>Counts</li>
      <li>Probabilities</li>
      <li>Proportions</li>
      <li>Ordered categories</li>
    </ul>
  </div>

  <h2>6) Different data structures</h2>
  <div class="card">
    <p>
      Some problems also require extensions because of how the data are organized:
    </p>
    <ul>
      <li>Repeated measurements</li>
      <li>Grouped data</li>
      <li>Nonlinear relationships</li>
    </ul>
  </div>

  <h2>7) Core modeling idea remains the same</h2>
  <div class="card">
    <p>
      Even when we move beyond linear regression,
      the main goal is still the same:
      describe relationships, explain variation, and make useful predictions.
    </p>
  </div>

  <h2>8) Extensions are not “completely different”</h2>
  <div class="card">
    <p>
      Extensions build on the same statistical thinking you already learned:
    </p>
    <ul>
      <li>parameters</li>
      <li>predictors and outcomes</li>
      <li>fit</li>
      <li>interpretation</li>
    </ul>
  </div>

  <h2>9) The first major extension</h2>
  <div class="card">
    <p>
      The first important extension is logistic regression,
      which is designed for binary outcomes.
    </p>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      Understanding the limits of linear regression is essential for choosing models responsibly.
      Good modeling begins by matching the model to the problem.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand the limits of ordinary linear regression</li>
      <li>Recognize when extensions are needed</li>
      <li>Identify outcome types that require different models</li>
      <li>See extensions as a continuation of modeling, not a separate topic</li>
      <li>Prepare for logistic regression</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now begin with the most important extension:
      logistic regression for binary outcomes.
    </p>
    <a class="btn" href="/modeling/extensions/logistic-regression/">
      Next lesson: Logistic Regression →
    </a>
  </div>

</section>