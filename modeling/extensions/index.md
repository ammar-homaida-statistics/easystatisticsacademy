---
layout: default
title: Block 7 — Extensions
description: Learn why statistical modeling extends beyond linear regression, including logistic regression, odds, generalized linear models, and the transition toward more advanced modeling frameworks.
permalink: /modeling/extensions/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_modeling_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/extensions/",
    label: "Block 7 — Extensions",
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
        <span class="badge">Block 7</span>
        <span class="badge">Extensions</span>
        <span class="badge">Logistic Regression</span>
      </div>

      <h1>Block 7 — Extensions</h1>

      <p class="lead">
        Linear regression is one of the most important statistical models,
        but it is not suitable for every type of outcome.
      </p>

      <p class="lead">
        This block introduces the logic behind model extensions,
        focusing on binary outcomes,
        logistic regression,
        generalized linear models,
        and the broader framework that connects classical statistics
        to modern predictive modeling.
      </p>

      <p class="muted-mini">
        9 lessons • Beyond linear regression • Builds on Model Fit & Comparison • Prepares for Applied Statistics
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
          🚀
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Many important statistical problems involve outcomes that are not continuous.
            Logistic regression and generalized linear models provide the tools
            needed to model probabilities,
            risks,
            counts,
            and other outcome types that ordinary linear regression cannot handle appropriately.
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
          <div class="mini-body">Introductory advanced modeling</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Understand when and why models must be extended
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next section</div>
          <div class="mini-body">
            Applied Statistics
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-modeling-extensions"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-modeling-extensions-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-modeling-extensions-btn"
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
      These lessons introduce situations where linear regression becomes inadequate
      and explain the broader modeling framework used to address new types of outcomes.
    </p>

  </div>

  <div class="grid grid-2">

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/extensions/why-extensions/">
          Why Do We Need Extensions?
        </a>
      </h3>

      <p>
        Learn why ordinary linear regression cannot appropriately model every type of outcome.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Limitations</span>
        <span class="pill">Outcomes</span>
        <span class="pill">Motivation</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/extensions/why-extensions/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/extensions/logistic-regression/">
          Logistic Regression
        </a>
      </h3>

      <p>
        Introduce regression models designed for binary outcomes and probabilities.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Logistic</span>
        <span class="pill">Binary Outcomes</span>
        <span class="pill">Probability</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/extensions/logistic-regression/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/extensions/probability-vs-logit/">
          Probability, Logit, and the Need for Transformation
        </a>
      </h3>

      <p>
        Understand why probabilities require a different modeling scale than continuous outcomes.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Probability</span>
        <span class="pill">Logit</span>
        <span class="pill">Transformation</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/extensions/probability-vs-logit/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/extensions/odds/">
          Odds Interpretation
        </a>
      </h3>

      <p>
        Learn how odds and odds ratios are interpreted in practical applications.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Odds</span>
        <span class="pill">Odds Ratio</span>
        <span class="pill">Interpretation</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/extensions/odds/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/extensions/interpreting-logistic-coefficients/">
          Interpreting Logistic Regression Coefficients
        </a>
      </h3>

      <p>
        Understand the meaning of logistic coefficients and their relationship to risk and odds.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Coefficients</span>
        <span class="pill">Log-Odds</span>
        <span class="pill">Interpretation</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/extensions/interpreting-logistic-coefficients/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/extensions/glm/">
          Generalized Linear Models
        </a>
      </h3>

      <p>
        Learn the broader framework that unifies linear regression and logistic regression.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">GLM</span>
        <span class="pill">Framework</span>
        <span class="pill">Model Family</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/extensions/glm/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/extensions/link-functions/">
          Link Functions
        </a>
      </h3>

      <p>
        Understand how generalized models connect predictors to different types of outcomes.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Link Functions</span>
        <span class="pill">GLM</span>
        <span class="pill">Modeling</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/extensions/link-functions/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/extensions/comparing-linear-and-logistic/">
          Linear vs Logistic Regression
        </a>
      </h3>

      <p>
        Compare the assumptions, interpretation, and appropriate use cases of both models.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Comparison</span>
        <span class="pill">Linear</span>
        <span class="pill">Logistic</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/extensions/comparing-linear-and-logistic/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/modeling/extensions/bridge-to-machine-learning/">
          Bridge to Machine Learning
        </a>
      </h3>

      <p>
        See how statistical modeling concepts extend naturally toward modern predictive methods.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Machine Learning</span>
        <span class="pill">Prediction</span>
        <span class="pill">Transition</span>
      </div>

      <a class="btn btn-outline"
         href="/modeling/extensions/bridge-to-machine-learning/">
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
        Previous blocks focused on linear regression and its evaluation.
        This block broadens the modeling framework,
        showing how statistical models adapt to different outcome types
        while preserving many familiar ideas about interpretation and inference.
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
              <td>Logistic Regression</td>
              <td>Models binary outcomes and probabilities</td>
            </tr>

            <tr>
              <td>Odds & Odds Ratios</td>
              <td>Provides practical interpretation of logistic models</td>
            </tr>

            <tr>
              <td>GLMs</td>
              <td>Unifies multiple modeling approaches</td>
            </tr>

            <tr>
              <td>Link Functions</td>
              <td>Connect predictors to diverse outcome types</td>
            </tr>

            <tr>
              <td>Machine Learning Bridge</td>
              <td>Provides conceptual transition to predictive modeling</td>
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

        <li>Understand why linear regression has important limitations</li>

        <li>Explain the logic behind logistic regression</li>

        <li>Interpret odds, log-odds, and odds ratios correctly</li>

        <li>Interpret logistic regression coefficients responsibly</li>

        <li>Understand the idea of generalized linear models</li>

        <li>Recognize the role of link functions</li>

        <li>Compare linear and logistic regression appropriately</li>

        <li>Build a conceptual bridge toward advanced modeling and machine learning</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next section</div>

        <div class="mini-body">
          Continue to <strong>Applied Statistics</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Different outcome types require different statistical models.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          The next section focuses on applying statistical methods to real-world problems and datasets.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/modeling/model-fit-comparison/">
      ← Previous Block: Model Fit & Comparison
    </a>

    <a class="btn" href="/learning-paths/">
      Next: Learning Paths →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_modeling_extensions_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-modeling-extensions"
      );

    const label =
      document.getElementById(
        "continue-reading-modeling-extensions-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-modeling-extensions-btn"
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