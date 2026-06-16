---
layout: default
title: Block 6 — Model Fit & Comparison
description: Learn how to evaluate model quality, interpret fit measures, compare competing models, avoid overfitting, and choose models that generalize well.
permalink: /modeling/model-fit-comparison/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_modeling_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/model-fit-comparison/",
    label: "Block 6 — Model Fit & Comparison",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card hero-split">

    <!-- LEFT -->

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Modeling</span>
        <span class="badge">Block 6</span>
        <span class="badge">Model Fit</span>
        <span class="badge">Comparison</span>
      </div>

      <h1>Block 6 — Model Fit & Comparison</h1>

      <p class="lead">
        Building a model is not enough—models must be evaluated.
      </p>

      <p class="lead">
        This block introduces the concepts and tools used to assess model quality,
        compare competing models,
        balance complexity against performance,
        and choose models that generalize well beyond the data used to build them.
      </p>

      <p class="muted-mini">
        9 lessons • Model evaluation • Builds on Diagnostics • Prepares for Extensions
      </p>

      <div class="hero-actions">

        <a class="btn" href="#lessons">
          Open Lessons
        </a>

        <a class="btn btn-outline" href="/modeling/">
          Back to Statistical Modeling
        </a>

      </div>

      <div class="hero-highlight">

        <div class="hero-highlight-icon">
          ⚖️
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            A model that fits existing data perfectly is not necessarily useful.
            Good modeling requires balancing fit,
            complexity,
            interpretability,
            and performance on future data.
          </p>

        </div>

      </div>

    </div>

    <!-- RIGHT -->

    <div class="hero-panel">

      <div class="panel-card">

        <h2 class="panel-title">Block overview</h2>

        <div class="mini">
          <div class="mini-title">Lessons</div>
          <div class="mini-body">9 structured lessons</div>
        </div>

        <div class="mini">
          <div class="mini-title">Level</div>
          <div class="mini-body">Model evaluation and selection</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Evaluate and compare statistical models
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Extensions
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-modeling-fit"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-modeling-fit-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-modeling-fit-btn"
        href="#"
      >
        Continue
      </a>

    </div>

  </div>

</section>

<!-- LESSONS -->

<section class="section" id="lessons">

  <div class="section-head">

    <h2>Lessons</h2>

    <p>
      These lessons move from basic ideas of model fit
      to practical methods for comparing,
      selecting,
      and evaluating statistical models.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/model-fit-comparison/what-is-model-fit/">
          What Is Model Fit?
        </a>
      </h3>

      <p>
        Learn what it means for a model to fit data and why fit alone is not enough.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Model Fit</span>
        <span class="pill">Evaluation</span>
        <span class="pill">Performance</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/what-is-model-fit/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/model-fit-comparison/r-squared/">
          R² (Coefficient of Determination)
        </a>
      </h3>

      <p>
        Understand explained variation and how R² summarizes model performance.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">R²</span>
        <span class="pill">Variation</span>
        <span class="pill">Fit</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/r-squared/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/model-fit-comparison/adjusted-r-squared/">
          Adjusted R²
        </a>
      </h3>

      <p>
        Learn how adjusted R² accounts for model complexity and additional predictors.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Adjusted R²</span>
        <span class="pill">Complexity</span>
        <span class="pill">Comparison</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/adjusted-r-squared/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/model-fit-comparison/overfitting/">
          Overfitting
        </a>
      </h3>

      <p>
        Understand why highly complex models may perform well on existing data but poorly on new data.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Overfitting</span>
        <span class="pill">Complexity</span>
        <span class="pill">Generalization</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/overfitting/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/model-fit-comparison/underfitting/">
          Underfitting
        </a>
      </h3>

      <p>
        Learn how overly simple models fail to capture meaningful structure in data.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Underfitting</span>
        <span class="pill">Bias</span>
        <span class="pill">Structure</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/underfitting/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 6 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/model-fit-comparison/train-vs-test/">
          Training vs Test Performance
        </a>
      </h3>

      <p>
        Understand why models must be evaluated using data that were not used to fit them.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Training</span>
        <span class="pill">Testing</span>
        <span class="pill">Validation</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/train-vs-test/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 7 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/model-fit-comparison/model-comparison/">
          Comparing Models
        </a>
      </h3>

      <p>
        Learn systematic approaches for comparing competing models.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Comparison</span>
        <span class="pill">Evaluation</span>
        <span class="pill">Selection</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/model-comparison/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 8 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/model-fit-comparison/aic-bic/">
          AIC and BIC
        </a>
      </h3>

      <p>
        Learn how information criteria balance model fit against model complexity.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">AIC</span>
        <span class="pill">BIC</span>
        <span class="pill">Selection</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/aic-bic/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 9 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/model-fit-comparison/model-selection-thinking/">
          Model Selection Thinking
        </a>
      </h3>

      <p>
        Develop practical judgment for selecting useful models beyond simple metrics.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Selection</span>
        <span class="pill">Judgment</span>
        <span class="pill">Practice</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/model-selection-thinking/">
         Open lesson
      </a>

    </div>

  </div>

</section>

<!-- BLOCK MAP -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>How this block fits into modeling</h2>

      <p>
        Diagnostics identify problems within models.
        Model fit and comparison determine which model should ultimately be used.
        Together, these concepts form the foundation of responsible model selection.
      </p>

      <div class="table-wrap">

        <table>

          <thead>
            <tr>
              <th>Concept</th>
              <th>Why it matters later</th>
            </tr>
          </thead>

          <tbody>

            <tr>
              <td>R²</td>
              <td>Provides a basic measure of explained variation</td>
            </tr>

            <tr>
              <td>Adjusted R²</td>
              <td>Allows fairer comparison across models</td>
            </tr>

            <tr>
              <td>Overfitting</td>
              <td>Protects against poor future performance</td>
            </tr>

            <tr>
              <td>AIC & BIC</td>
              <td>Balance fit and complexity systematically</td>
            </tr>

            <tr>
              <td>Model Selection</td>
              <td>Supports evidence-based modeling decisions</td>
            </tr>

          </tbody>

        </table>

      </div>

    </div>

  </div>

</section>

<!-- GOALS -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>Goal of this block</h2>

      <ul class="bullets">

        <li>Understand what model fit means</li>

        <li>Interpret R² and adjusted R² correctly</li>

        <li>Recognize overfitting and underfitting</li>

        <li>Understand training versus test performance</li>

        <li>Compare competing models systematically</li>

        <li>Use AIC and BIC appropriately</li>

        <li>Balance fit, complexity, and interpretability</li>

        <li>Develop sound model-selection judgment</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Extensions</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          The best-fitting model is not always the best model.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          The next block extends modeling beyond standard linear regression.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/modeling/diagnostics/">
      ← Previous Block: Diagnostics
    </a>

    <a class="btn" href="/modeling/extensions/">
      Next Block: Extensions →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_modeling_fit_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-modeling-fit"
      );

    const label =
      document.getElementById(
        "continue-reading-modeling-fit-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-modeling-fit-btn"
      );

    label.innerHTML =
      "You last visited: <strong>" +
      data.label +
      "</strong>";

    btn.href = data.url;

    wrap.style.display = "block";

  } catch (e) {}

})();
</script>