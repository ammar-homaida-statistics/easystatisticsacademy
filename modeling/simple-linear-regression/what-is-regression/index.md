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
      Regression is one of the most widely used statistical modeling techniques for understanding relationships between variables.
    </p>

    <p class="lead">
      It helps analysts explain outcomes, estimate effects, and make predictions using observed data.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/simple-linear-regression/">
         ← Block Home
      </a>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/regression-equations/">
         Next: Regression Equations →
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
      Examples include:
    </p>

    <ul class="bullets">

      <li>How does advertising affect sales?</li>

      <li>How does study time affect exam scores?</li>

      <li>How does experience affect salary?</li>

      <li>How does house size affect house price?</li>

    </ul>

    <p>
      Regression provides a framework for analyzing such relationships systematically.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Regression models describe how changes in one variable are associated with changes in another variable.
      </p>

    </div>

    <h2>What Is Regression?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Regression is a statistical method used to model and quantify relationships between an outcome variable and one or more predictor variables.
      </p>

    </div>

    <p>
      The goal is often to understand, explain, or predict the outcome variable.
    </p>

    <h2>The Basic Idea</h2>

    <p>
      Suppose we observe that larger houses tend to sell for higher prices.
    </p>

    <p>
      Instead of describing this relationship qualitatively, regression attempts to represent it mathematically.
    </p>

    <p>
      The resulting model can estimate how much price tends to change as house size changes.
    </p>

    <h2>Predictors and Outcomes</h2>

    <p>
      Every regression model contains variables that play different roles.
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
            <td>Predictor</td>
            <td>Used to explain or predict another variable</td>
          </tr>

          <tr>
            <td>Outcome</td>
            <td>Variable being explained or predicted</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Regression attempts to connect predictors to outcomes through a mathematical relationship.
    </p>

    <h2>A House Price Example</h2>

    <p>
      Consider:
    </p>

    <ul class="bullets">

      <li>Predictor: House size</li>

      <li>Outcome: House price</li>

    </ul>

    <p>
      Regression attempts to estimate how house price changes as house size changes.
    </p>

    <p>
      Once the relationship is estimated, predictions become possible.
    </p>

    <h2>Regression Is About Relationships</h2>

    <p>
      The focus of regression is not simply describing variables individually.
    </p>

    <p>
      Instead, regression studies relationships between variables.
    </p>

    <p>
      Questions often include:
    </p>

    <ul class="bullets">

      <li>How strong is the relationship?</li>

      <li>Is the relationship positive or negative?</li>

      <li>Can the relationship be used for prediction?</li>

      <li>How much uncertainty exists?</li>

    </ul>

    <h2>Positive Relationships</h2>

    <p>
      In a positive relationship:
    </p>

    <div class="example-box">

      <p>
        Larger values of one variable tend to be associated with larger values of another variable.
      </p>

    </div>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Study time and exam scores</li>

      <li>Advertising spending and sales</li>

      <li>House size and house price</li>

    </ul>

    <h2>Negative Relationships</h2>

    <p>
      In a negative relationship:
    </p>

    <div class="example-box">

      <p>
        Larger values of one variable tend to be associated with smaller values of another variable.
      </p>

    </div>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Product price and demand</li>

      <li>Travel speed and travel time</li>

      <li>Exercise frequency and resting heart rate</li>

    </ul>

    <h2>Regression and Prediction</h2>

    <p>
      One important use of regression is prediction.
    </p>

    <p>
      Once a relationship has been estimated, the model can generate expected outcomes for new observations.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>Predict future sales</li>

      <li>Estimate house values</li>

      <li>Forecast energy demand</li>

      <li>Predict exam scores</li>

    </ul>

    <h2>Regression and Explanation</h2>

    <p>
      Regression is also useful for explanation.
    </p>

    <p>
      Analysts often want to understand:
    </p>

    <ul class="bullets">

      <li>Which variables matter most</li>

      <li>How outcomes change with predictors</li>

      <li>The direction of relationships</li>

      <li>The magnitude of effects</li>

    </ul>

    <p>
      These insights help support scientific and business decisions.
    </p>

    <h2>Regression Does Not Guarantee Causation</h2>

    <p>
      One of the most important cautions in modeling is:
    </p>

    <div class="concept-box">

      <strong>Important warning:</strong>

      <p>
        Regression can identify associations, but association alone does not prove causation.
      </p>

    </div>

    <p>
      Two variables may move together for many reasons.
    </p>

    <p>
      Additional evidence is usually needed before causal conclusions can be justified.
    </p>

    <h2>Regression and Noise</h2>

    <p>
      Real-world data contain noise.
    </p>

    <p>
      Even when a relationship exists, observations rarely fall perfectly on a simple pattern.
    </p>

    <p>
      Regression attempts to identify the underlying signal despite random variation.
    </p>

    <h2>Simple vs Multiple Regression</h2>

    <p>
      Regression models can involve different numbers of predictors.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Type</th>
            <th>Predictors</th>
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
      This block begins with simple linear regression because it provides the foundation for many more advanced models.
    </p>

    <h2>Why Regression Is So Popular</h2>

    <p>
      Regression is used extensively because it:
    </p>

    <ul class="bullets">

      <li>Is relatively easy to interpret</li>

      <li>Supports explanation and prediction</li>

      <li>Provides measures of uncertainty</li>

      <li>Can be extended to more complex situations</li>

    </ul>

    <p>
      Many advanced statistical and machine-learning methods build upon regression concepts.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Regression is one of the most important tools in statistics because it transforms relationships among variables into mathematical models.
    </p>

    <p>
      These models help analysts understand patterns, estimate effects, and make predictions while accounting for uncertainty.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Regression is a statistical modeling technique used to describe, explain, and predict relationships between outcome variables and predictor variables. It forms the foundation of much of modern statistical analysis.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      To use regression effectively, we need a mathematical language for expressing relationships between variables.
    </p>

    <p>
      The next lesson introduces regression equations and explains how predictors and outcomes are connected mathematically.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Regression models relationships between variables</li>

        <li>Regression can be used for both explanation and prediction</li>

        <li>Predictors are used to explain or predict outcomes</li>

        <li>Relationships may be positive or negative</li>

        <li>Regression helps identify signal within noisy data</li>

        <li>Association does not automatically imply causation</li>

        <li>Simple regression uses one predictor variable</li>

        <li>Regression is one of the most widely used statistical tools</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/">
         ← Back to Block Home
      </a>

      <a class="btn"
         href="/modeling/simple-linear-regression/regression-equations/">
         Next: Regression Equations →
      </a>

    </div>

  </div>

</section>