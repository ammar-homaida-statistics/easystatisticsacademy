---
layout: default
title: Adjusted R-Squared
description: Learn what adjusted R-squared measures, why it improves upon ordinary R-squared, and how it helps compare regression models with different numbers of predictors.
permalink: /modeling/model-fit-comparison/adjusted-r-squared/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_model_fit_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/model-fit-comparison/adjusted-r-squared/",
    label: "Adjusted R-Squared",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 6</span>
      <span class="badge">Model Fit & Comparison</span>
      <span class="badge">Adjusted R²</span>
    </div>

    <h1>Adjusted R-Squared</h1>

    <p class="lead">
      Ordinary R-squared measures explained variation, but it has an important weakness.
    </p>

    <p class="lead">
      R-squared never decreases when predictors are added, even when those predictors contribute little useful information.
    </p>

    <p class="lead">
      Adjusted R-squared addresses this limitation by accounting for model complexity.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/model-fit-comparison/r-squared/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/overfitting/">
         Next: Overfitting →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Ordinary R-Squared Has a Problem</h2>

    <p>
      R-squared increases whenever additional predictors are added to a regression model.
    </p>

    <p>
      This occurs even if the new predictors have little or no real relationship with the outcome.
    </p>

    <p>
      As a result, R-squared can make unnecessarily complex models appear better than they truly are.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Adjusted R-squared improves on ordinary R-squared by rewarding explanatory power while penalizing unnecessary model complexity.
      </p>

    </div>

    <h2>The Goal of Adjusted R-Squared</h2>

    <p>
      Adjusted R-squared asks a more meaningful question:
    </p>

    <div class="example-box">

      <p>
        Does the improvement in fit justify the addition of more predictors?
      </p>
    </div>

    <p>
      Instead of automatically rewarding complexity, it evaluates whether new variables contribute enough information to be worthwhile.
    </p>

    <h2>How Adjusted R-Squared Works</h2>

    <p>
      Adjusted R-squared modifies ordinary R-squared by incorporating:
    </p>

    <ul class="bullets">

      <li>Sample size</li>

      <li>Number of predictors</li>

      <li>Explained variation</li>

    </ul>

    <p>
      The adjustment becomes larger as more predictors are added.
    </p>

    <h2>The Formula</h2>

    <p>
      The mathematical definition is:
    </p>

    

    <p>
      where:
    </p>

    <ul class="bullets">

      <li><strong>R²</strong> = ordinary R-squared</li>

      <li><strong>n</strong> = sample size</li>

      <li><strong>p</strong> = number of predictors</li>

    </ul>

    <p>
      The formula introduces a penalty for model complexity.
    </p>

    <h2>What Makes It Different?</h2>

    <p>
      Unlike ordinary R-squared:
    </p>

    <ul class="bullets">

      <li>Adjusted R-squared can increase</li>

      <li>Adjusted R-squared can decrease</li>

      <li>Adding weak predictors may lower the statistic</li>

    </ul>

    <p>
      This makes it more useful for comparing models with different numbers of predictors.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        A predictor must improve the model enough to overcome the complexity penalty before adjusted R-squared increases.
      </p>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Suppose a regression model predicting exam scores has:
    </p>

    <div class="example-box">

      <p>R² = 0.70</p>
      <p>Adjusted R² = 0.68</p>
    </div>

    <p>
      The slightly lower adjusted value reflects the cost of including predictors in the model.
    </p>

    <p>
      Most models have adjusted R-squared values that are somewhat lower than ordinary R-squared.
    </p>

    <h2>Adding a Useful Predictor</h2>

    <p>
      Imagine adding a new predictor that substantially improves prediction accuracy.
    </p>

    <p>
      Because the improvement outweighs the complexity penalty:
    </p>

    <ul class="bullets">

      <li>R-squared increases</li>

      <li>Adjusted R-squared also increases</li>

    </ul>

    <p>
      This suggests the new predictor provides meaningful information.
    </p>

    <h2>Adding an Unhelpful Predictor</h2>

    <p>
      Now imagine adding a predictor that contributes almost nothing.
    </p>

    <p>
      In this case:
    </p>

    <ul class="bullets">

      <li>R-squared may increase slightly</li>

      <li>Adjusted R-squared may decrease</li>

    </ul>

    <p>
      The penalty outweighs the small improvement in fit.
    </p>

    <h2>Comparing Two Models</h2>

    <p>
      Consider the following models:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Model</th>
            <th>Predictors</th>
            <th>R²</th>
            <th>Adjusted R²</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>A</td>
            <td>3</td>
            <td>0.72</td>
            <td>0.70</td>
          </tr>

          <tr>
            <td>B</td>
            <td>8</td>
            <td>0.74</td>
            <td>0.68</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Although Model B has a slightly larger R-squared value, Model A has the higher adjusted R-squared.
    </p>

    <p>
      This suggests Model A may provide a better balance between fit and complexity.
    </p>

    <h2>Why Analysts Use Adjusted R-Squared</h2>

    <p>
      Adjusted R-squared is particularly useful when:
    </p>

    <ul class="bullets">

      <li>Comparing multiple regression models</li>

      <li>Evaluating additional predictors</li>

      <li>Assessing model complexity</li>

      <li>Preventing unnecessary variable inclusion</li>

    </ul>

    <p>
      It encourages more parsimonious modeling.
    </p>

    <h2>What Is Parsimony?</h2>

    <p>
      Parsimony refers to explaining data with the simplest model that adequately captures important relationships.
    </p>

    <p>
      Simpler models are often:
    </p>

    <ul class="bullets">

      <li>Easier to interpret</li>

      <li>Easier to communicate</li>

      <li>Less prone to overfitting</li>

    </ul>

    <p>
      Adjusted R-squared supports this principle.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        A slightly simpler model is often preferable if additional predictors contribute little practical value.
      </p>

    </div>

    <h2>Adjusted R-Squared Is Not Perfect</h2>

    <p>
      Although adjusted R-squared improves on ordinary R-squared, it is not a complete measure of model quality.
    </p>

    <p>
      It does not directly evaluate:
    </p>

    <ul class="bullets">

      <li>Prediction on new data</li>

      <li>Assumption validity</li>

      <li>Causal interpretation</li>

      <li>Model correctness</li>

    </ul>

    <p>
      Other diagnostics remain important.
    </p>

    <h2>Adjusted R-Squared and Prediction</h2>

    <p>
      Higher adjusted R-squared values often indicate better-fitting models.
    </p>

    <p>
      However, they do not guarantee superior predictive performance on future data.
    </p>

    <p>
      Validation techniques are needed to evaluate true predictive ability.
    </p>

    <h2>Adjusted R-Squared vs R-Squared</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Feature</th>
            <th>R²</th>
            <th>Adjusted R²</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Measures explained variation</td>
            <td>Yes</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Penalizes complexity</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Can decrease when predictors are added</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Useful for model comparison</td>
            <td>Limited</td>
            <td>Better</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      R-squared provides a useful summary of explained variation, but it can encourage unnecessary model complexity.
    </p>

    <p>
      Adjusted R-squared addresses this issue by balancing model fit against the number of predictors.
    </p>

    <p>
      This makes it a valuable tool for comparing competing regression models and evaluating whether additional variables truly improve performance.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Adjusted R-squared measures explained variation while accounting for model complexity. It helps analysts determine whether additional predictors provide meaningful improvement rather than merely increasing model size.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Even adjusted R-squared can sometimes favor models that fit existing data too closely.
    </p>

    <p>
      This leads to one of the most important challenges in statistical modeling: overfitting.
    </p>

    <p>
      The next lesson explores overfitting and explains why models that appear excellent on training data may perform poorly on new observations.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Adjusted R-squared accounts for both fit and model complexity</li>

        <li>It penalizes the inclusion of unnecessary predictors</li>

        <li>Unlike ordinary R-squared, it can decrease when variables are added</li>

        <li>It is useful for comparing models with different numbers of predictors</li>

        <li>Higher adjusted R-squared values generally indicate better balance between fit and complexity</li>

        <li>Adjusted R-squared supports parsimonious modeling</li>

        <li>It improves upon ordinary R-squared but does not replace other diagnostics</li>

        <li>Model evaluation should combine adjusted R-squared with broader assessment tools</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/r-squared/">
         ← Previous: R-Squared
      </a>

      <a class="btn"
         href="/modeling/model-fit-comparison/overfitting/">
         Next: Overfitting →
      </a>

    </div>

  </div>

</section>