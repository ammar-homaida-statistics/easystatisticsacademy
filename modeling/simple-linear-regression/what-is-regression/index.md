---
layout: default
title: What Is Regression?
description: Learn what regression is, why it is one of the most important statistical modeling techniques, and how it helps explain and predict outcomes.
permalink: /modeling/simple-linear-regression/what-is-regression/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_simple_linear_regression_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/simple-linear-regression/what-is-regression/",
    label: "What Is Regression?",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 2</span>
      <span class="badge">Simple Linear Regression</span>
      <span class="badge">Introduction</span>
    </div>

    <h1>What Is Regression?</h1>

    <p class="lead">
      Regression is one of the most widely used statistical modeling techniques for describing relationships between variables.
    </p>

    <p class="lead">
      It helps analysts understand how changes in one variable are associated with changes in another and provides a framework for prediction.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/simple-linear-regression/">
         ← Block Home
      </a>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/regression-equation/">
         Next: The Regression Equation →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Regression Matters</h2>

    <p>
      Many real-world questions involve relationships between variables.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>How does advertising affect sales?</li>

      <li>How does education relate to income?</li>

      <li>How does house size influence price?</li>

      <li>How does study time relate to exam performance?</li>

    </ul>

    <p>
      Regression provides a systematic way to study these relationships.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Regression models describe how an outcome variable changes as one or more predictor variables change.
      </p>

    </div>

    <h2>What Is Regression?</h2>

    <p>
      Regression is a statistical method used to model the relationship between variables.
    </p>

    <p>
      Typically, a regression model includes:
    </p>

    <ul class="bullets">

      <li>An outcome variable</li>

      <li>One or more predictor variables</li>

      <li>A mathematical relationship connecting them</li>

    </ul>

    <p>
      The goal is to understand, explain, or predict the outcome.
    </p>

    <h2>The Basic Idea</h2>

    <p>
      Suppose we collect information on:
    </p>

    <ul class="bullets">

      <li>Study hours</li>

      <li>Exam scores</li>

    </ul>

    <p>
      We might observe that students who study more tend to earn higher scores.
    </p>

    <p>
      Regression helps quantify that relationship rather than describing it qualitatively.
    </p>

    <h2>Outcome and Predictor Variables</h2>

    <p>
      Regression models distinguish between two key types of variables.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Role</th>
            <th>Description</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Predictor Variable</td>
            <td>Used to explain or predict another variable</td>
          </tr>

          <tr>
            <td>Outcome Variable</td>
            <td>Variable being explained or predicted</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Regression focuses on how predictors relate to outcomes.
    </p>

    <h2>A Real-World Example</h2>

    <p>
      Consider housing prices.
    </p>

    <p>
      A predictor variable might be:
    </p>

    <div class="example-box">

      <p>
        House size
      </p>
    </div>

    <p>
      The outcome variable might be:
    </p>

    <div class="example-box">

      <p>
        House price
      </p>
    </div>

    <p>
      Regression can estimate how expected price changes as size changes.
    </p>

    <h2>Regression Is About Relationships</h2>

    <p>
      Regression does not merely summarize data.
    </p>

    <p>
      It attempts to model a systematic relationship between variables.
    </p>

    <p>
      The relationship may be:
    </p>

    <ul class="bullets">

      <li>Positive</li>

      <li>Negative</li>

      <li>Strong</li>

      <li>Weak</li>

      <li>Linear</li>

      <li>Nonlinear</li>

    </ul>

    <p>
      Understanding these relationships is a central goal of modeling.
    </p>

    <h2>Regression and Prediction</h2>

    <p>
      Once a relationship is estimated, regression models can generate predictions.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>Predict future sales</li>

      <li>Predict exam scores</li>

      <li>Predict medical outcomes</li>

      <li>Predict housing prices</li>

    </ul>

    <p>
      Prediction is one of the most common applications of regression.
    </p>

    <h2>Regression and Explanation</h2>

    <p>
      Regression is also useful for explanation.
    </p>

    <p>
      Analysts often want to understand:
    </p>

    <ul class="bullets">

      <li>Which variables matter most</li>

      <li>Whether relationships exist</li>

      <li>How large effects appear to be</li>

      <li>How variables move together</li>

    </ul>

    <p>
      These questions emphasize interpretation rather than prediction.
    </p>

    <h2>Regression Is Not Proof of Causation</h2>

    <p>
      One of the most important cautions in statistics is:
    </p>

    <div class="example-box">

      <p>
        Regression can reveal associations, but association alone does not prove causation.
      </p>

    </div>

    <p>
      Two variables may move together for many reasons.
    </p>

    <p>
      Additional evidence is needed before claiming a causal relationship.
    </p>

    <h2>Simple vs Multiple Regression</h2>

    <p>
      Regression models vary in complexity.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Model Type</th>
            <th>Number of Predictors</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Simple Regression</td>
            <td>One predictor</td>
          </tr>

          <tr>
            <td>Multiple Regression</td>
            <td>Two or more predictors</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This block focuses on simple linear regression, the foundation for many more advanced methods.
    </p>

    <h2>Why Start with Simple Linear Regression?</h2>

    <p>
      Simple linear regression introduces many core ideas used throughout statistical modeling:
    </p>

    <ul class="bullets">

      <li>Model equations</li>

      <li>Parameters</li>

      <li>Prediction</li>

      <li>Residuals</li>

      <li>Model fit</li>

      <li>Interpretation</li>

    </ul>

    <p>
      Mastering these ideas makes more advanced modeling techniques easier to understand.
    </p>

    <h2>Regression as Signal Extraction</h2>

    <p>
      Recall the distinction between signal and noise.
    </p>

    <p>
      Regression attempts to identify the systematic component of a relationship while separating it from random variation.
    </p>

    <p>
      In this sense, regression acts as a signal-extraction tool.
    </p>

    <h2>What Regression Produces</h2>

    <p>
      A regression analysis typically produces:
    </p>

    <ul class="bullets">

      <li>An estimated relationship</li>

      <li>Model parameters</li>

      <li>Predicted values</li>

      <li>Measures of uncertainty</li>

      <li>Measures of model fit</li>

    </ul>

    <p>
      These outputs help analysts understand and evaluate relationships.
    </p>

    <h2>Applications of Regression</h2>

    <p>
      Regression is used across many disciplines.
    </p>

    <ul class="bullets">

      <li>Economics</li>

      <li>Finance</li>

      <li>Marketing</li>

      <li>Medicine</li>

      <li>Engineering</li>

      <li>Social sciences</li>

      <li>Data science</li>

    </ul>

    <p>
      It remains one of the most important tools in modern statistics.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Regression provides a mathematical framework for describing how variables move together.
    </p>

    <p>
      It helps explain patterns, estimate relationships, and generate predictions while accounting for uncertainty.
    </p>

    <p>
      Because of its flexibility and interpretability, regression forms the foundation of many statistical and machine-learning methods.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Regression is a statistical modeling technique that describes relationships between variables. It helps explain outcomes, make predictions, estimate effects, and separate meaningful patterns from random variation.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Every regression model is built around an equation that formally describes the relationship between predictors and outcomes.
    </p>

    <p>
      Understanding this equation is the next step toward understanding how regression works.
    </p>

    <p>
      The next lesson introduces the regression equation and explains its components.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Regression models relationships between variables</li>

        <li>Regression uses predictors to explain or predict outcomes</li>

        <li>Regression supports both explanation and prediction</li>

        <li>Simple regression uses one predictor variable</li>

        <li>Regression helps separate signal from noise</li>

        <li>Regression produces predictions and interpretable parameter estimates</li>

        <li>Regression identifies associations but does not automatically prove causation</li>

        <li>Regression is one of the most widely used tools in statistics and data science</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/">
         ← Back to Block Home
      </a>

      <a class="btn"
         href="/modeling/simple-linear-regression/regression-equation/">
         Next: The Regression Equation →
      </a>

    </div>

  </div>

</section>