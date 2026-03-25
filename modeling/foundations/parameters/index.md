---
layout: default
title: 4. Parameters
permalink: /modeling/foundations/parameters/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding parameters conceptually.
      Estimation methods and inference will be developed later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_foundations_lesson_v0", JSON.stringify({
    url: "/modeling/foundations/parameters/",
    label: "Lesson 4 — Parameters",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 1</span>
      <span class="badge">Lesson 4</span>
      <span class="badge">Parameters</span>
      <span class="badge">Model Structure</span>
    </div>

    <h1>4. Parameters</h1>

    <p class="lead">
      Parameters define the structure of a model.
      They quantify relationships and determine how inputs affect outcomes.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/foundations/">Back to Block 1</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: concept-first. Estimation comes later.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what parameters are,
    how they differ from data, and how they define the behavior of a model.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Parameters are fixed but unknown quantities that describe the true relationship
      between variables.
    </p>
  </div>

  <h2>1) What is a parameter?</h2>
  <div class="card">
    <p>
      A parameter is a numerical value that defines a model.
      It determines how predictors influence the response.
    </p>
  </div>

  <h2>2) Example: linear regression</h2>
  <div class="card">
    <p><strong>Y = β₀ + β₁X + ε</strong></p>
    <ul>
      <li><strong>β₀</strong> — intercept</li>
      <li><strong>β₁</strong> — slope</li>
    </ul>
    <p>
      These parameters define the relationship between X and Y.
    </p>
  </div>

  <h2>3) Parameters vs data</h2>
  <div class="card">
    <ul>
      <li><strong>Parameters</strong> — fixed, unknown, describe reality</li>
      <li><strong>Data</strong> — observed, variable, come from samples</li>
    </ul>
    <p>
      We use data to learn about parameters.
    </p>
  </div>

  <h2>4) Parameters are not random (in classical statistics)</h2>
  <div class="card">
    <p>
      In standard statistical modeling, parameters are fixed values.
      The randomness comes from the data, not from the parameters.
    </p>
  </div>

  <h2>5) Role of parameters in modeling</h2>
  <div class="card">
    <ul>
      <li>Define the shape of the model</li>
      <li>Quantify relationships</li>
      <li>Enable prediction</li>
      <li>Support interpretation</li>
    </ul>
  </div>

  <h2>6) True vs estimated parameters</h2>
  <div class="card">
    <p>
      The true parameters are unknown.
      We estimate them using data (later: estimators like β̂).
    </p>
  </div>

  <h2>7) Why this matters</h2>
  <div class="card">
    <p>
      Understanding parameters prevents confusion between:
      the true relationship and what we observe in data.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define parameters in a model</li>
      <li>Distinguish parameters from data</li>
      <li>Understand parameters as fixed but unknown</li>
      <li>Explain the role of parameters in modeling</li>
      <li>Recognize the need for estimation</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we distinguish two different goals of modeling:
      prediction vs explanation.
    </p>
    <a class="btn" href="/modeling/foundations/prediction-vs-explanation/">
      Next lesson: Prediction vs Explanation →
    </a>
  </div>

</section>