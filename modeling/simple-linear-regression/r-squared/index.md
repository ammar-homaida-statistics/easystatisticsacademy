---
layout: default
title: R-Squared
description: Learn what R-squared measures, how it summarizes regression model fit, and how to interpret the proportion of variation explained by a regression model.
permalink: /modeling/simple-linear-regression/r-squared/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_simple_linear_regression_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/simple-linear-regression/r-squared/",
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
      <span class="badge">Block 2</span>
      <span class="badge">Simple Linear Regression</span>
      <span class="badge">Model Fit</span>
    </div>

    <h1>R-Squared</h1>

    <p class="lead">
      After fitting a regression model, an important question remains:
    </p>

    <p class="lead">
      How much of the variation in the outcome variable does the model actually explain?
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/simple-linear-regression/least-squares/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/correlation-vs-regression/">
         Next: Correlation vs Regression →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why We Need a Measure of Fit</h2>

    <p>
      A regression line always exists once we fit a model.
    </p>

    <p>
      However, some regression lines explain a great deal of variation, while others explain very little.
    </p>

    <p>
      We need a way to quantify how useful the fitted line is.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        R-squared measures the proportion of variation in the outcome variable that is explained by the regression model.
      </p>

    </div>

    <h2>What Is R-Squared?</h2>

    <p>
      R-squared (R²) is one of the most commonly reported statistics in regression analysis.
    </p>

    <p>
      It summarizes how well the regression model explains variation in the outcome variable.
    </p>

    <p>
      R-squared is often called:
    </p>

    <ul class="bullets">

      <li>Coefficient of determination</li>

      <li>Proportion of explained variance</li>

      <li>Measure of model fit</li>

    </ul>

    <h2>The Core Interpretation</h2>

    <p>
      R-squared answers the question:
    </p>

    <div class="example-box">

      <p>
        What percentage of the variability in the outcome is explained by the predictor?
      </p>
    </div>

    <p>
      Larger values indicate that the regression model explains more of the observed variation.
    </p>

    <h2>The Range of R-Squared</h2>

    <p>
      In ordinary simple linear regression:
    </p>

    <div class="example-box">

      <p>
        0 ≤ R² ≤ 1
      </p>
    </div>

    <p>
      R-squared is often expressed as a proportion or percentage.
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
            <td>0</td>
            <td>Explains none of the variation</td>
          </tr>

          <tr>
            <td>0.25</td>
            <td>Explains 25% of the variation</td>
          </tr>

          <tr>
            <td>0.70</td>
            <td>Explains 70% of the variation</td>
          </tr>

          <tr>
            <td>1</td>
            <td>Explains all variation perfectly</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>An Example</h2>

    <p>
      Suppose a regression model predicts exam scores from study hours.
    </p>

    <p>
      The analysis produces:
    </p>

    <div class="example-box">

      <p>
        R² = 0.64
      </p>
    </div>

    <p>
      Interpretation:
    </p>

    <p>
      Approximately 64% of the variation in exam scores is explained by study hours.
    </p>

    <p>
      The remaining 36% is unexplained by the model.
    </p>

    <h2>Explained vs Unexplained Variation</h2>

    <p>
      Recall that data contain both signal and noise.
    </p>

    <p>
      R-squared measures how much signal the regression model has captured.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Component</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Explained Variation</td>
            <td>Captured by the regression model</td>
          </tr>

          <tr>
            <td>Unexplained Variation</td>
            <td>Left in the residuals</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Higher R-squared values indicate that more variation is being explained.
    </p>

    <h2>Perfect Fit</h2>

    <p>
      If:
    </p>

    <div class="example-box">

      <p>
        R² = 1
      </p>
    </div>

    <p>
      every observation lies exactly on the regression line.
    </p>

    <p>
      In this case:
    </p>

    <ul class="bullets">

      <li>Residuals are zero</li>

      <li>Predictions are perfect</li>

      <li>All variation is explained</li>

    </ul>

    <p>
      Perfect fits are rare in real-world data.
    </p>

    <h2>No Explanatory Power</h2>

    <p>
      If:
    </p>

    <div class="example-box">

      <p>
        R² = 0
      </p>
    </div>

    <p>
      the regression model explains none of the variation in the outcome.
    </p>

    <p>
      The predictor contributes no linear explanatory power.
    </p>

    <h2>R-Squared Is About Variation</h2>

    <p>
      A common misconception is that R-squared measures prediction accuracy directly.
    </p>

    <p>
      It does not.
    </p>

    <p>
      Instead, R-squared measures how much variation is explained.
    </p>

    <p>
      A model may have a high R-squared and still produce practically important prediction errors.
    </p>

    <div class="concept-box">

      <strong>Important distinction:</strong>

      <p>
        R-squared measures explained variation, not whether predictions are perfect.
      </p>

    </div>

    <h2>High R-Squared Is Not Always Better</h2>

    <p>
      A higher R-squared often indicates stronger explanatory power.
    </p>

    <p>
      However, extremely high values can sometimes indicate:
    </p>

    <ul class="bullets">

      <li>Overfitting</li>

      <li>Data leakage</li>

      <li>Artificial relationships</li>

    </ul>

    <p>
      R-squared should always be interpreted alongside other diagnostics.
    </p>

    <h2>Low R-Squared Does Not Always Mean Failure</h2>

    <p>
      Some fields naturally contain substantial randomness.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Human behavior</li>

      <li>Financial markets</li>

      <li>Social outcomes</li>

    </ul>

    <p>
      In these areas, even modest R-squared values can be scientifically useful.
    </p>

    <h2>R-Squared and Correlation</h2>

    <p>
      In simple linear regression, there is a special relationship:
    </p>

    <div class="example-box">

      <p>
        R² = r²
      </p>
    </div>

    <p>
      where r is the correlation coefficient between the predictor and outcome.
    </p>

    <p>
      This connection links regression and correlation closely together.
    </p>

    <h2>What R-Squared Does Not Tell Us</h2>

    <p>
      R-squared alone cannot determine:
    </p>

    <ul class="bullets">

      <li>Whether the relationship is causal</li>

      <li>Whether assumptions are satisfied</li>

      <li>Whether predictions generalize well</li>

      <li>Whether the model is appropriate</li>

    </ul>

    <p>
      Additional analyses are always necessary.
    </p>

    <h2>R-Squared and Residuals</h2>

    <p>
      As residuals become smaller:
    </p>

    <ul class="bullets">

      <li>Explained variation increases</li>

      <li>R-squared increases</li>

    </ul>

    <p>
      As residuals become larger:
    </p>

    <ul class="bullets">

      <li>Unexplained variation increases</li>

      <li>R-squared decreases</li>

    </ul>

    <p>
      This is why R-squared is closely connected to model fit.
    </p>

    <h2>A Visual Intuition</h2>

    <p>
      Imagine a scatterplot:
    </p>

    <ul class="bullets">

      <li>Points tightly clustered around a line → High R²</li>

      <li>Points widely scattered around a line → Low R²</li>

    </ul>

    <p>
      R-squared reflects how tightly observations follow the fitted relationship.
    </p>

    <h2>Why Analysts Report R-Squared</h2>

    <p>
      R-squared provides a simple summary of:
    </p>

    <ul class="bullets">

      <li>Model fit</li>

      <li>Explanatory power</li>

      <li>Amount of captured variation</li>

    </ul>

    <p>
      Because it is easy to interpret, it is one of the most commonly reported regression statistics.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Regression attempts to explain variation in outcomes using predictors.
    </p>

    <p>
      R-squared measures how successful that effort has been by quantifying the proportion of variation captured by the model.
    </p>

    <p>
      While it is an important summary statistic, it should always be interpreted alongside residual analysis, assumptions, and substantive context.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        R-squared measures the proportion of variation in an outcome variable explained by a regression model. Larger values indicate stronger explanatory power, but R-squared alone does not determine whether a model is good, causal, or appropriate.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Regression and correlation are closely related concepts, but they answer different questions.
    </p>

    <p>
      Correlation measures the strength of association, while regression models the relationship and enables prediction.
    </p>

    <p>
      The next lesson explores the similarities and differences between correlation and regression.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>R-squared measures the proportion of variation explained by a regression model</li>

        <li>R² ranges from 0 to 1 in ordinary simple linear regression</li>

        <li>Higher R² values indicate more explained variation</li>

        <li>R² = 0 means no explained variation</li>

        <li>R² = 1 means perfect explanation of variation</li>

        <li>R-squared measures explained variation, not perfect prediction</li>

        <li>Low R² values may still be useful in noisy domains</li>

        <li>In simple linear regression, R² equals the square of the correlation coefficient</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/least-squares/">
         ← Previous: Least Squares
      </a>

      <a class="btn"
         href="/modeling/simple-linear-regression/correlation-vs-regression/">
         Next: Correlation vs Regression →
      </a>

    </div>

  </div>

</section>