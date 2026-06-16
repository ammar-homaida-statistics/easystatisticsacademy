---
layout: default
title: Block 5 — Diagnostics
description: Learn how to evaluate regression models using residuals, diagnostic plots, leverage, influence measures, and practical model-checking workflows.
permalink: /modeling/diagnostics/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_modeling_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/diagnostics/",
    label: "Block 5 — Diagnostics",
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
        <span class="badge">Block 5</span>
        <span class="badge">Diagnostics</span>
        <span class="badge">Model Checking</span>
      </div>

      <h1>Block 5 — Diagnostics</h1>

      <p class="lead">
        Building a model is only the beginning.
      </p>

      <p class="lead">
        Diagnostics help determine whether a model is trustworthy by revealing
        assumption violations, unusual observations, influential cases,
        and other issues that may affect interpretation and prediction.
      </p>

      <p class="muted-mini">
        9 lessons • Model evaluation • Builds on Model Assumptions • Prepares for Model Fit & Comparison
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
          🔍
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Assumptions cannot be evaluated by theory alone.
            Diagnostics provide the practical tools used by statisticians
            and data scientists to assess model quality,
            identify problems,
            and improve models responsibly.
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
          <div class="mini-body">Applied model evaluation</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Diagnose and evaluate regression models
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Model Fit & Comparison
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-modeling-diagnostics"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-modeling-diagnostics-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-modeling-diagnostics-btn"
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
      These lessons develop the diagnostic tools used to evaluate models,
      detect problems,
      and determine whether model assumptions are reasonable.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/diagnostics/residuals/">
          Residuals: The Core Idea
        </a>
      </h3>

      <p>
        Learn what residuals represent and why they are central to regression diagnostics.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Residuals</span>
        <span class="pill">Errors</span>
        <span class="pill">Diagnostics</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/residuals/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/diagnostics/residual-plots/">
          Residual Plots
        </a>
      </h3>

      <p>
        Use residual plots to identify patterns, assumption violations, and model weaknesses.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Plots</span>
        <span class="pill">Residuals</span>
        <span class="pill">Visualization</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/residual-plots/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/diagnostics/nonlinearity/">
          Detecting Nonlinearity
        </a>
      </h3>

      <p>
        Learn how residual patterns reveal incorrect functional forms and missing structure.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Nonlinearity</span>
        <span class="pill">Patterns</span>
        <span class="pill">Model Form</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/nonlinearity/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/diagnostics/heteroscedasticity/">
          Detecting Heteroscedasticity
        </a>
      </h3>

      <p>
        Identify changing variance patterns and understand their implications for inference.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Variance</span>
        <span class="pill">Residuals</span>
        <span class="pill">Assumptions</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/heteroscedasticity/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/diagnostics/outliers/">
          Outliers
        </a>
      </h3>

      <p>
        Learn how unusual observations are identified and how they affect models.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Outliers</span>
        <span class="pill">Unusual Data</span>
        <span class="pill">Influence</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/outliers/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 6 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/diagnostics/leverage/">
          Leverage
        </a>
      </h3>

      <p>
        Understand why observations with extreme predictor values deserve special attention.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Leverage</span>
        <span class="pill">Predictors</span>
        <span class="pill">Influence</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/leverage/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 7 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/diagnostics/influence/">
          Influence
        </a>
      </h3>

      <p>
        Learn how individual observations can strongly affect model estimates and conclusions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Influence</span>
        <span class="pill">Sensitivity</span>
        <span class="pill">Estimation</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/influence/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 8 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/diagnostics/cooks-distance/">
          Cook's Distance
        </a>
      </h3>

      <p>
        Use Cook's Distance to assess the overall influence of observations on model estimates.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Cook's Distance</span>
        <span class="pill">Influence</span>
        <span class="pill">Diagnostics</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/cooks-distance/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 9 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/diagnostics/diagnostic-workflow/">
          Diagnostic Workflow
        </a>
      </h3>

      <p>
        Develop a practical step-by-step process for evaluating regression models.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Workflow</span>
        <span class="pill">Practice</span>
        <span class="pill">Model Checking</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/diagnostic-workflow/">
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
        Model assumptions establish what should be true.
        Diagnostics provide the tools used to check whether those assumptions
        are supported by the observed data.
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
              <td>Residual Analysis</td>
              <td>Forms the foundation of model checking</td>
            </tr>

            <tr>
              <td>Diagnostic Plots</td>
              <td>Reveal hidden model problems visually</td>
            </tr>

            <tr>
              <td>Outliers</td>
              <td>Identify unusual observations requiring investigation</td>
            </tr>

            <tr>
              <td>Influence Measures</td>
              <td>Assess the stability of model conclusions</td>
            </tr>

            <tr>
              <td>Diagnostic Workflow</td>
              <td>Supports consistent and reproducible model evaluation</td>
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

        <li>Use residuals to evaluate model quality</li>

        <li>Interpret diagnostic plots correctly</li>

        <li>Identify nonlinearity and heteroscedasticity</li>

        <li>Recognize outliers and influential observations</li>

        <li>Understand leverage and Cook's Distance</li>

        <li>Assess the reliability of model conclusions</li>

        <li>Apply a structured diagnostic workflow</li>

        <li>Prepare for formal model comparison and evaluation</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Model Fit & Comparison</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          A model should always be checked before it is trusted.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          The next block examines how competing models are evaluated and compared.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/modeling/assumptions/">
      ← Previous Block: Model Assumptions
    </a>

    <a class="btn" href="/modeling/model-fit-comparison/">
      Next Block: Model Fit & Comparison →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_modeling_diagnostics_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-modeling-diagnostics"
      );

    const label =
      document.getElementById(
        "continue-reading-modeling-diagnostics-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-modeling-diagnostics-btn"
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