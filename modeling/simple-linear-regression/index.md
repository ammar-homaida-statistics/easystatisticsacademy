---
layout: default
title: Block 2 — Simple Linear Regression
description: Learn simple linear regression from first principles: regression equations, slope, intercept, residuals, least squares, prediction, and explained variation.
permalink: /modeling/simple-linear-regression/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_modeling_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/simple-linear-regression/",
    label: "Block 2 — Simple Linear Regression",
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
        <span class="badge">Block 2</span>
        <span class="badge">Regression</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>Block 2 — Simple Linear Regression</h1>

      <p class="lead">
        Simple linear regression is the first complete statistical model.
      </p>

      <p class="lead">
        This block introduces how relationships between variables are represented,
        how regression lines are interpreted,
        how predictions are generated,
        and how variation is explained through a statistical model.
      </p>

      <p class="muted-mini">
        9 lessons • First regression model • Builds on Modeling Foundations • Prepares for Multiple Regression
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
          📉
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Linear regression is one of the most widely used tools in statistics,
            data science,
            economics,
            social science,
            and machine learning.
            Understanding regression correctly is essential before moving to more complex models.
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
          <div class="mini-body">Introductory regression modeling</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Interpret and understand simple regression models
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Multiple Regression
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-modeling-slr"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-modeling-slr-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-modeling-slr-btn"
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
      These lessons develop the ideas of regression,
      prediction,
      residual variation,
      and interpretation from first principles.
    </p>

  </div>

  <div class="grid grid-2">

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/simple-linear-regression/what-is-regression/">
          What Is Regression?
        </a>
      </h3>

      <p>
        Learn how regression models relationships and why it is more than simply drawing a line through points.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Regression</span>
        <span class="pill">Relationships</span>
        <span class="pill">Modeling</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/what-is-regression/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/simple-linear-regression/regression-equation/">
          The Regression Equation
        </a>
      </h3>

      <p>
        Understand the mathematical structure of a simple regression model and the role of each component.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Equation</span>
        <span class="pill">Model</span>
        <span class="pill">Structure</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/regression-equation/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/simple-linear-regression/slope/">
          Slope Interpretation
        </a>
      </h3>

      <p>
        Learn how to interpret the effect of a one-unit change in the predictor variable.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Slope</span>
        <span class="pill">Effect</span>
        <span class="pill">Interpretation</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/slope/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/simple-linear-regression/intercept/">
          Intercept Interpretation
        </a>
      </h3>

      <p>
        Understand the meaning of the intercept and when it should or should not be interpreted.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Intercept</span>
        <span class="pill">Baseline</span>
        <span class="pill">Context</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/intercept/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/simple-linear-regression/residuals/">
          Residuals and Errors
        </a>
      </h3>

      <p>
        Learn how observed and predicted values differ and why residuals are central to regression.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Residuals</span>
        <span class="pill">Errors</span>
        <span class="pill">Variation</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/residuals/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/simple-linear-regression/least-squares/">
          Least Squares Method
        </a>
      </h3>

      <p>
        Understand why regression lines are fitted by minimizing squared residuals.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Least Squares</span>
        <span class="pill">Optimization</span>
        <span class="pill">Fit</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/least-squares/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/simple-linear-regression/r-squared/">
          R² (Explained Variation)
        </a>
      </h3>

      <p>
        Learn what R² measures, how it relates to model performance, and what it cannot tell us.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">R²</span>
        <span class="pill">Variation</span>
        <span class="pill">Fit</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/r-squared/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/simple-linear-regression/correlation-vs-regression/">
          Correlation vs Regression
        </a>
      </h3>

      <p>
        Distinguish association from modeling and understand how correlation relates to regression.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Correlation</span>
        <span class="pill">Association</span>
        <span class="pill">Regression</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/correlation-vs-regression/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/simple-linear-regression/prediction/">
          Prediction Using the Model
        </a>
      </h3>

      <p>
        Learn how regression generates predictions and why predictions have uncertainty.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Prediction</span>
        <span class="pill">Forecasting</span>
        <span class="pill">Uncertainty</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/prediction/">
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
        Simple linear regression is the bridge between abstract modeling concepts
        and practical statistical models.
        It introduces coefficients,
        fitted values,
        residuals,
        prediction,
        and model interpretation.
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
              <td>Slope</td>
              <td>Foundation for interpreting regression coefficients</td>
            </tr>

            <tr>
              <td>Residuals</td>
              <td>Supports diagnostics and assumption checking</td>
            </tr>

            <tr>
              <td>Least Squares</td>
              <td>Provides the fitting principle used throughout regression</td>
            </tr>

            <tr>
              <td>R²</td>
              <td>Introduces model evaluation concepts</td>
            </tr>

            <tr>
              <td>Prediction</td>
              <td>Prepares for forecasting and applied modeling</td>
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

        <li>Understand simple regression as a statistical model</li>

        <li>Interpret slope and intercept correctly</li>

        <li>Understand residuals and model error</li>

        <li>Explain least squares conceptually</li>

        <li>Interpret R² appropriately</li>

        <li>Distinguish correlation from regression</li>

        <li>Understand prediction and its limitations</li>

        <li>Prepare for multiple regression models</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Multiple Regression</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Regression models relationships while accounting for variation.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          The next block expands from one predictor to many predictors.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/modeling/foundations/">
      ← Previous Block: Modeling Foundations
    </a>

    <a class="btn" href="/modeling/multiple-regression/">
      Next Block: Multiple Regression →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_modeling_slr_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-modeling-slr"
      );

    const label =
      document.getElementById(
        "continue-reading-modeling-slr-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-modeling-slr-btn"
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