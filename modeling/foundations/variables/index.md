---
layout: default
title: 2. Variables and Relationships
permalink: /modeling/foundations/variables/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on how variables define relationships in models.
      Visual intuition and software examples will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_foundations_lesson_v0", JSON.stringify({
    url: "/modeling/foundations/variables/",
    label: "Lesson 2 — Variables and Relationships",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 1</span>
      <span class="badge">Lesson 2</span>
      <span class="badge">Variables</span>
      <span class="badge">Relationships</span>
    </div>

    <h1>2. Variables and Relationships</h1>

    <p class="lead">
      Models are built from variables and the relationships between them.
      Understanding how variables interact is the foundation of statistical modeling.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/foundations/">Back to Block 1</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: concept-first. Structure before computation.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what variables are,
    how they are classified in modeling, and how relationships between them
    form the basis of statistical models.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A model describes how one variable changes in relation to others.
      Without variables, there is nothing to model.
    </p>
  </div>

  <h2>1) What is a variable?</h2>
  <div class="card">
    <p>
      A variable is any measurable quantity that can take different values.
      In modeling, variables represent the features of a system we want to study.
    </p>
  </div>

  <h2>2) Types of variables in modeling</h2>
  <div class="card">
    <ul>
      <li><strong>Response (dependent variable)</strong> — the outcome we want to explain</li>
      <li><strong>Predictor (independent variable)</strong> — variables used to explain the outcome</li>
    </ul>
    <p>
      A model always has at least one response and one or more predictors.
    </p>
  </div>

  <h2>3) Relationships between variables</h2>
  <div class="card">
    <p>
      A model expresses how the response variable depends on predictors:
    </p>
    <p><strong>Response = function(predictors) + error</strong></p>
    <p>
      This relationship can be linear, nonlinear, strong, weak, or nonexistent.
    </p>
  </div>

  <h2>4) Direction of relationships</h2>
  <div class="card">
    <ul>
      <li><strong>Positive relationship</strong> — as X increases, Y increases</li>
      <li><strong>Negative relationship</strong> — as X increases, Y decreases</li>
      <li><strong>No relationship</strong> — no clear pattern</li>
    </ul>
  </div>

  <h2>5) Strength of relationships</h2>
  <div class="card">
    <p>
      Some relationships are clear and strong, others are weak and noisy.
      Modeling helps quantify and understand this strength.
    </p>
  </div>

  <h2>6) Correlation vs causation</h2>
  <div class="card">
    <p>
      A relationship between variables does not imply that one causes the other.
      Models capture association, not necessarily causality.
    </p>
  </div>

  <h2>7) Example</h2>
  <div class="card">
    <p>
      Suppose we model exam score using study hours:
    </p>
    <p><strong>Score = β₀ + β₁ × Hours + error</strong></p>
    <p>
      Hours is the predictor, score is the response.
      The model describes how score changes with study time.
    </p>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Misunderstanding variables leads to incorrect models,
      wrong interpretations, and misleading conclusions.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define variables in modeling</li>
      <li>Distinguish response vs predictors</li>
      <li>Understand relationships between variables</li>
      <li>Recognize direction and strength of relationships</li>
      <li>Avoid confusing correlation with causation</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we separate what models can explain from what they cannot:
      signal vs noise.
    </p>
    <a class="btn" href="/modeling/foundations/signal-noise/">
      Next lesson: Signal vs Noise →
    </a>
  </div>

</section>