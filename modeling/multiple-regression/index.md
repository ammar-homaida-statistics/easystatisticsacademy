---
layout: default
title: Block 3 — Multiple Regression
description: Learn multiple regression, adjusted effects, confounding, multicollinearity, categorical predictors, interactions, and responsible model building.
permalink: /modeling/multiple-regression/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_modeling_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/multiple-regression/",
    label: "Block 3 — Multiple Regression",
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
        <span class="badge">Block 3</span>
        <span class="badge">Multiple Regression</span>
        <span class="badge">Adjustment</span>
      </div>

      <h1>Block 3 — Multiple Regression</h1>

      <p class="lead">
        Real-world relationships rarely involve only one predictor.
      </p>

      <p class="lead">
        Multiple regression extends simple regression by allowing several predictors
        to be considered simultaneously, making it possible to estimate adjusted effects,
        address confounding, and build more realistic statistical models.
      </p>

      <p class="muted-mini">
        9 lessons • Multivariable modeling • Builds on Simple Linear Regression • Prepares for Model Assumptions
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
          📊
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Most practical statistical analyses involve multiple variables.
            Understanding adjusted effects, confounding, categorical predictors,
            and interactions is essential for interpreting real-world models correctly.
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
          <div class="mini-body">Intermediate regression modeling</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Interpret regression coefficients conditionally
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Model Assumptions
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-modeling-mr"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-modeling-mr-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-modeling-mr-btn"
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
      These lessons develop the concepts needed to build,
      interpret,
      and evaluate multivariable regression models.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/multiple-regression/why-multiple/">
          Why Multiple Regression?
        </a>
      </h3>

      <p>
        Learn why single-predictor models are often incomplete and why multiple variables are needed.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Motivation</span>
        <span class="pill">Predictors</span>
        <span class="pill">Modeling</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/why-multiple/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/multiple-regression/model-structure/">
          The Multiple Regression Model
        </a>
      </h3>

      <p>
        Extend the regression equation to multiple predictors and understand its structure.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Equation</span>
        <span class="pill">Predictors</span>
        <span class="pill">Structure</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/model-structure/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/multiple-regression/adjusted-effects/">
          Adjusted Effects
        </a>
      </h3>

      <p>
        Learn how coefficients represent effects after accounting for other variables.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Adjustment</span>
        <span class="pill">Effects</span>
        <span class="pill">Interpretation</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/adjusted-effects/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/multiple-regression/confounding/">
          Confounding
        </a>
      </h3>

      <p>
        Understand how omitted variables can distort relationships and create misleading conclusions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Confounding</span>
        <span class="pill">Bias</span>
        <span class="pill">Causality</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/confounding/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/multiple-regression/coefficients/">
          Interpreting Coefficients
        </a>
      </h3>

      <p>
        Learn the conditional meaning of regression coefficients and their units.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Coefficients</span>
        <span class="pill">Units</span>
        <span class="pill">Interpretation</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/coefficients/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 6 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/multiple-regression/multicollinearity/">
          Multicollinearity
        </a>
      </h3>

      <p>
        Understand why correlated predictors can destabilize coefficient estimates.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Collinearity</span>
        <span class="pill">Instability</span>
        <span class="pill">Predictors</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/multicollinearity/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 7 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/multiple-regression/dummy-variables/">
          Dummy Variables (Categorical Data)
        </a>
      </h3>

      <p>
        Learn how categorical variables are encoded and interpreted within regression models.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Categorical</span>
        <span class="pill">Dummy Coding</span>
        <span class="pill">Reference Group</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/dummy-variables/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 8 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/multiple-regression/interactions/">
          Interaction Effects
        </a>
      </h3>

      <p>
        Understand how the effect of one predictor can depend on another predictor.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Interactions</span>
        <span class="pill">Effect Modification</span>
        <span class="pill">Interpretation</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/interactions/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 9 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/multiple-regression/model-building/">
          Model Building Thinking
        </a>
      </h3>

      <p>
        Learn principled approaches to choosing predictors and constructing useful models.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Model Building</span>
        <span class="pill">Specification</span>
        <span class="pill">Strategy</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/model-building/">
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
        Multiple regression transforms regression from a simple descriptive tool
        into a framework capable of handling realistic data situations involving
        several variables simultaneously.
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
              <td>Adjusted Effects</td>
              <td>Provides meaningful coefficient interpretation</td>
            </tr>

            <tr>
              <td>Confounding</td>
              <td>Prevents misleading conclusions</td>
            </tr>

            <tr>
              <td>Multicollinearity</td>
              <td>Supports model diagnostics and stability assessment</td>
            </tr>

            <tr>
              <td>Dummy Variables</td>
              <td>Allows categorical predictors in models</td>
            </tr>

            <tr>
              <td>Interactions</td>
              <td>Captures more realistic relationships</td>
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

        <li>Understand why multiple regression is needed</li>

        <li>Interpret adjusted effects correctly</li>

        <li>Recognize and explain confounding</li>

        <li>Understand multicollinearity and its consequences</li>

        <li>Work with categorical predictors using dummy variables</li>

        <li>Interpret interaction effects appropriately</li>

        <li>Develop thoughtful model-building strategies</li>

        <li>Prepare for formal regression assumptions and diagnostics</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Model Assumptions</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Regression coefficients become conditional when multiple predictors are included.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          The next block studies the assumptions required for regression results to be trustworthy.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/modeling/simple-linear-regression/">
      ← Previous Block: Simple Linear Regression
    </a>

    <a class="btn" href="/modeling/assumptions/">
      Next Block: Model Assumptions →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_modeling_mr_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-modeling-mr"
      );

    const label =
      document.getElementById(
        "continue-reading-modeling-mr-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-modeling-mr-btn"
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