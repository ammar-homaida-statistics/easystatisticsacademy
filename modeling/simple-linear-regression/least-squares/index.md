---
layout: default
title: Least Squares
description: Learn how the least-squares method fits a regression line by minimizing prediction errors and why it is the foundation of ordinary linear regression.
permalink: /modeling/simple-linear-regression/least-squares/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_simple_linear_regression_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/simple-linear-regression/least-squares/",
    label: "Least Squares",
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
      <span class="badge">Least Squares</span>
    </div>

    <h1>Least Squares</h1>

    <p class="lead">
      A regression line is not chosen arbitrarily.
    </p>

    <p class="lead">
      The least-squares method selects the line that minimizes overall prediction error, making it the standard approach for fitting linear regression models.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/simple-linear-regression/residuals/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/r-squared/">
         Next: R-Squared →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why We Need a Fitting Method</h2>

    <p>
      Suppose we have a scatterplot showing the relationship between two variables.
    </p>

    <p>
      Many different lines could be drawn through the data.
    </p>

    <p>
      The question becomes:
    </p>

    <div class="example-box">

      <p>
        Which line should we choose?
      </p>
    </div>

    <p>
      The least-squares method provides a mathematical answer.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Least squares chooses the regression line that minimizes the total squared residuals.
      </p>

    </div>

    <h2>Recall: What Is a Residual?</h2>

    <p>
      A residual measures prediction error:
    </p>

    

    <p>
      Residuals indicate how far observations are from the fitted regression line.
    </p>

    <p>
      Smaller residuals imply better predictions.
    </p>

    <h2>Why Not Minimize Raw Residuals?</h2>

    <p>
      If we simply added residuals together, positive and negative values would cancel.
    </p>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        +5 + (−5) = 0
      </p>
    </div>

    <p>
      A total of zero would incorrectly suggest perfect predictions.
    </p>

    <p>
      We need a way to measure error that avoids cancellation.
    </p>

    <h2>Squaring Residuals</h2>

    <p>
      Least squares solves this problem by squaring every residual.
    </p>

    <p>
      Squaring produces two benefits:
    </p>

    <ul class="bullets">

      <li>All values become nonnegative</li>

      <li>Large errors receive greater penalties</li>

    </ul>

    <p>
      For example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Residual</th>
            <th>Squared Residual</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>2</td>
            <td>4</td>
          </tr>

          <tr>
            <td>5</td>
            <td>25</td>
          </tr>

          <tr>
            <td>-5</td>
            <td>25</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Large mistakes contribute much more to the total error.
    </p>

    <h2>The Least-Squares Criterion</h2>

    <p>
      The regression line is chosen to minimize:
    </p>

    

    <p>
      This quantity is called the Sum of Squared Residuals (SSR) or Residual Sum of Squares (RSS).
    </p>

    <p>
      The best-fitting line is the one with the smallest possible value.
    </p>

    <h2>What Does This Mean Geometrically?</h2>

    <p>
      Imagine drawing vertical distances from every data point to the regression line.
    </p>

    <p>
      Each vertical distance is a residual.
    </p>

    <p>
      Least squares finds the line that makes the combined squared distances as small as possible.
    </p>

    <h2>A Visual Interpretation</h2>

    <p>
      Think of every residual as a tiny prediction mistake.
    </p>

    <p>
      Least squares seeks the line that makes the overall collection of mistakes as small as possible.
    </p>

    <p>
      This provides a principled definition of the "best" line.
    </p>

    <h2>Why Large Errors Matter More</h2>

    <p>
      Because errors are squared, large residuals contribute disproportionately.
    </p>

    <p>
      Compare:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Residual</th>
            <th>Squared Value</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>2</td>
            <td>4</td>
          </tr>

          <tr>
            <td>10</td>
            <td>100</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      A residual five times larger produces twenty-five times more squared error.
    </p>

    <p>
      This strongly discourages large prediction mistakes.
    </p>

    <h2>Ordinary Least Squares (OLS)</h2>

    <p>
      The standard regression-fitting method is called Ordinary Least Squares (OLS).
    </p>

    <p>
      OLS estimates the slope and intercept that minimize the residual sum of squares.
    </p>

    <p>
      Most introductory regression analysis is based on OLS.
    </p>

    <h2>How the Regression Line Is Determined</h2>

    <p>
      OLS simultaneously chooses:
    </p>

    <ul class="bullets">

      <li>The intercept</li>

      <li>The slope</li>

    </ul>

    <p>
      so that the total squared residuals become as small as possible.
    </p>

    <p>
      Once these values are found, the regression line is fully determined.
    </p>

    <h2>Why Least Squares Became Popular</h2>

    <p>
      Least squares has several desirable properties:
    </p>

    <ul class="bullets">

      <li>Mathematically tractable</li>

      <li>Computationally efficient</li>

      <li>Produces interpretable estimates</li>

      <li>Works well under many conditions</li>

    </ul>

    <p>
      These advantages have made it the dominant linear regression fitting method.
    </p>

    <h2>Least Squares and Prediction</h2>

    <p>
      Because least squares minimizes prediction errors within the observed sample, it often produces strong predictive performance.
    </p>

    <p>
      However, minimizing training error alone does not guarantee perfect performance on future data.
    </p>

    <p>
      Generalization remains an important consideration.
    </p>

    <h2>Residuals After Fitting</h2>

    <p>
      Once the least-squares line is fitted:
    </p>

    <ul class="bullets">

      <li>Residuals can be calculated</li>

      <li>Model assumptions can be checked</li>

      <li>Prediction quality can be evaluated</li>

      <li>Model fit can be summarized</li>

    </ul>

    <p>
      Much of regression analysis builds upon these residuals.
    </p>

    <h2>Least Squares Does Not Guarantee Perfection</h2>

    <p>
      The least-squares line is the best line according to the least-squares criterion.
    </p>

    <p>
      It does not mean:
    </p>

    <ul class="bullets">

      <li>Predictions are perfect</li>

      <li>The relationship is strong</li>

      <li>The model is causal</li>

      <li>The line explains all variation</li>

    </ul>

    <p>
      It simply means no other straight line produces a smaller total squared residual.
    </p>

    <div class="concept-box">

      <strong>Important distinction:</strong>

      <p>
        Least squares identifies the best-fitting line among linear candidates, not necessarily a perfect model of reality.
      </p>

    </div>

    <h2>Connecting Least Squares to Model Fit</h2>

    <p>
      Smaller residual sums generally indicate better fit.
    </p>

    <p>
      However, analysts often want a standardized measure of fit that is easier to interpret.
    </p>

    <p>
      This leads naturally to one of the most common regression metrics: R-squared.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Least squares provides the mathematical foundation of ordinary linear regression.
    </p>

    <p>
      By minimizing the total squared residuals, it determines the line that best balances prediction errors across all observations.
    </p>

    <p>
      Understanding least squares is essential because it explains how regression models are fitted and why the resulting line looks the way it does.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The least-squares method fits a regression line by minimizing the sum of squared residuals. This produces the ordinary least-squares regression line, the standard approach used in simple linear regression.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      After fitting a regression line, analysts want to know how much variation in the outcome has been explained.
    </p>

    <p>
      One of the most widely used measures for answering this question is R-squared.
    </p>

    <p>
      The next lesson introduces R-squared and explains how it summarizes model fit.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Least squares is the standard method for fitting linear regression models</li>

        <li>Residuals measure prediction errors</li>

        <li>Residuals are squared to prevent cancellation and emphasize large errors</li>

        <li>The least-squares line minimizes the sum of squared residuals</li>

        <li>Ordinary Least Squares (OLS) is the most common regression-fitting method</li>

        <li>OLS determines both the slope and intercept simultaneously</li>

        <li>The least-squares line is the best-fitting line under the squared-error criterion</li>

        <li>Least squares forms the mathematical foundation of linear regression</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/residuals/">
         ← Previous: Residuals
      </a>

      <a class="btn"
         href="/modeling/simple-linear-regression/r-squared/">
         Next: R-Squared →
      </a>

    </div>

  </div>

</section>