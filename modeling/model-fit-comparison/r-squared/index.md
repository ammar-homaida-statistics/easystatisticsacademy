---
layout: default
title: R-Squared
description: Learn what R-squared measures, how it is interpreted, and why it is one of the most commonly reported statistics in regression analysis.
permalink: /modeling/model-fit-comparison/r-squared/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_model_fit_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/model-fit-comparison/r-squared/",
    label: "R-Squared",
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
      <span class="badge">R-Squared</span>
    </div>

    <h1>R-Squared</h1>

    <p class="lead">
      One of the most common questions in regression analysis is:
    </p>

    <p class="lead">
      How much of the variation in the outcome does the model explain?
    </p>

    <p class="lead">
      R-squared provides a numerical answer to that question and is one of the most widely reported measures of model fit.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/model-fit-comparison/what-is-model-fit/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/adjusted-r-squared/">
         Next: Adjusted R-Squared →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is R-Squared?</h2>

    <p>
      R-squared measures the proportion of variation in the outcome variable that is explained by the regression model.
    </p>

    <p>
      It provides a summary of how well the model accounts for differences in observed outcomes.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        R-squared represents the percentage of outcome variation explained by the predictors in a regression model.
      </p>

    </div>

    <h2>The Basic Idea</h2>

    <p>
      Outcomes vary from one observation to another.
    </p>

    <p>
      Some of that variation can be explained by predictors included in the model.
    </p>

    <p>
      The remaining variation remains unexplained and appears in the residuals.
    </p>

    <p>
      R-squared quantifies how much variation is explained relative to the total variation present in the data.
    </p>

    <h2>The Formula</h2>

    <p>
      Conceptually, R-squared can be expressed as:
    </p>

    

    <p>
      Higher values indicate that the model explains a larger proportion of the outcome variability.
    </p>

    <h2>Interpreting R-Squared</h2>

    <p>
      R-squared ranges from 0 to 1.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>R² Value</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0.00</td>
            <td>Model explains none of the variation</td>
          </tr>

          <tr>
            <td>0.25</td>
            <td>Model explains 25% of the variation</td>
          </tr>

          <tr>
            <td>0.50</td>
            <td>Model explains 50% of the variation</td>
          </tr>

          <tr>
            <td>0.75</td>
            <td>Model explains 75% of the variation</td>
          </tr>

          <tr>
            <td>1.00</td>
            <td>Model explains all observed variation</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>A Practical Example</h2>

    <p>
      Suppose a regression model predicts exam scores from study hours and achieves:
    </p>

    <div class="example-box">

      <p>
        R² = 0.64
      </p>
    </div>

    <p>
      This means the model explains 64% of the observed variation in exam scores.
    </p>

    <p>
      The remaining 36% remains unexplained by the predictors in the model.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        R-squared describes explained variation, not prediction accuracy for individual observations.
      </p>

    </div>

    <h2>Why R-Squared Is Popular</h2>

    <p>
      R-squared provides a simple summary of model fit.
    </p>

    <p>
      Analysts, researchers, and decision-makers often find it intuitive because it can be interpreted as a percentage of explained variation.
    </p>

    <p>
      This makes it useful for communicating results.
    </p>

    <h2>Higher Is Usually Better</h2>

    <p>
      In general, larger R-squared values indicate better fit.
    </p>

    <p>
      More variation in the outcome is being explained by the model.
    </p>

    <p>
      However, higher is not always better in every situation.
    </p>

    <h2>R-Squared Does Not Measure Causation</h2>

    <p>
      A high R-squared value does not imply that predictors cause the outcome.
    </p>

    <p>
      It merely indicates that the model captures variation in the observed data.
    </p>

    <p>
      Causal conclusions require additional assumptions and study design considerations.
    </p>

    <h2>R-Squared Does Not Prove Correctness</h2>

    <p>
      A model may have a high R-squared value and still be flawed.
    </p>

    <p>
      Potential problems include:
    </p>

    <ul class="bullets">

      <li>Confounding variables</li>

      <li>Incorrect assumptions</li>

      <li>Nonlinearity</li>

      <li>Overfitting</li>

    </ul>

    <p>
      R-squared should therefore be interpreted alongside other diagnostics.
    </p>

    <div class="concept-box">

      <strong>Important warning:</strong>

      <p>
        A high R-squared value does not guarantee a good model.
      </p>

    </div>

    <h2>Low R-Squared Is Not Always Bad</h2>

    <p>
      In some fields, outcomes are naturally difficult to predict.
    </p>

    <p>
      Human behavior, social systems, and biological processes often contain substantial randomness.
    </p>

    <p>
      In these situations, relatively modest R-squared values may still be scientifically meaningful.
    </p>

    <h2>Acceptable Values Depend on Context</h2>

    <p>
      Different disciplines often have different expectations.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Context</th>
            <th>Typical Expectations</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Physical sciences</td>
            <td>Often higher R² values</td>
          </tr>

          <tr>
            <td>Engineering</td>
            <td>Often high predictive accuracy</td>
          </tr>

          <tr>
            <td>Social sciences</td>
            <td>Moderate values may be meaningful</td>
          </tr>

          <tr>
            <td>Behavioral research</td>
            <td>Lower values are often common</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>R-Squared and Residuals</h2>

    <p>
      R-squared is closely connected to residual variation.
    </p>

    <p>
      Smaller residuals generally produce larger R-squared values because more variation is explained.
    </p>

    <p>
      Larger residuals reduce explained variation and lower R-squared.
    </p>

    <h2>R-Squared and Additional Predictors</h2>

    <p>
      Adding predictors can only maintain or increase R-squared.
    </p>

    <p>
      It never decreases when new variables are added.
    </p>

    <p>
      This property creates an important limitation when comparing models of different complexity.
    </p>

    <h2>The Problem with R-Squared</h2>

    <p>
      Because R-squared always increases or remains unchanged when predictors are added, it may reward unnecessary complexity.
    </p>

    <p>
      Even irrelevant variables can slightly increase R-squared.
    </p>

    <p>
      This can encourage overfitting.
    </p>

    <h2>Adjusted R-Squared</h2>

    <p>
      To address this limitation, analysts often use adjusted R-squared.
    </p>

    <p>
      Adjusted R-squared introduces a penalty for unnecessary predictors and provides a more balanced measure of model fit.
    </p>

    <p>
      It is especially useful when comparing models with different numbers of predictors.
    </p>

    <h2>R-Squared and Prediction</h2>

    <p>
      Although R-squared reflects explained variation, it does not directly measure predictive performance on new data.
    </p>

    <p>
      Cross-validation and out-of-sample testing are often better tools for evaluating predictive ability.
    </p>

    <p>
      Fit and prediction are related but distinct concepts.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      R-squared is one of the most widely used measures of model fit because it provides an intuitive summary of explained variation.
    </p>

    <p>
      However, no single statistic can fully evaluate a regression model.
    </p>

    <p>
      Effective model assessment combines R-squared with diagnostics, theoretical understanding, and predictive evaluation.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        R-squared measures the proportion of variation in the outcome explained by a regression model. Higher values indicate greater explained variation, but R-squared should be interpreted alongside other measures of model quality.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      One limitation of R-squared is that it always increases when predictors are added, even if those predictors provide little value.
    </p>

    <p>
      Analysts therefore often use adjusted R-squared when comparing models of different complexity.
    </p>

    <p>
      The next lesson explains adjusted R-squared and shows how it improves upon ordinary R-squared for model comparison.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>R-squared measures the proportion of outcome variation explained by a model</li>

        <li>R-squared ranges from 0 to 1</li>

        <li>Higher values generally indicate better fit</li>

        <li>R-squared describes explained variation, not causation</li>

        <li>High R-squared values do not guarantee a good model</li>

        <li>Low R-squared values may still be meaningful in some fields</li>

        <li>Adding predictors always increases or maintains R-squared</li>

        <li>Adjusted R-squared helps address limitations of ordinary R-squared</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/what-is-model-fit/">
         ← Previous: What Is Model Fit?
      </a>

      <a class="btn"
         href="/modeling/model-fit-comparison/adjusted-r-squared/">
         Next: Adjusted R-Squared →
      </a>

    </div>

  </div>

</section>