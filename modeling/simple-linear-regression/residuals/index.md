---
layout: default
title: Residuals and Least Squares
description: Learn what residuals are, why they matter in regression, and how the least-squares method finds the regression line that best fits the data.
permalink: /modeling/simple-linear-regression/residuals-and-least-squares/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_simple_linear_regression_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/simple-linear-regression/residuals-and-least-squares/",
    label: "Residuals and Least Squares",
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
      <span class="badge">Residuals</span>
    </div>

    <h1>Residuals and Least Squares</h1>

    <p class="lead">
      Regression models rarely predict every observation perfectly.
    </p>

    <p class="lead">
      Residuals measure prediction errors, and the least-squares method uses those errors to find the regression line that best fits the data.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/simple-linear-regression/intercept/">
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

    <h2>Why Prediction Errors Matter</h2>

    <p>
      Even when a regression model captures an important relationship, actual observations rarely fall exactly on the regression line.
    </p>

    <p>
      Real-world data contain noise, measurement error, and unobserved influences.
    </p>

    <p>
      As a result, some prediction error is unavoidable.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Residuals measure the difference between observed outcomes and the values predicted by a regression model.
      </p>

    </div>

    <h2>What Is a Residual?</h2>

    <p>
      A residual is the prediction error for a single observation.
    </p>

    <p>
      It measures how far an observed value lies above or below the regression line.
    </p>

    <div class="example-box">

      <p>
        Residual = Observed Value − Predicted Value
      </p>
    </div>

    <p>
      Every observation in a dataset has its own residual.
    </p>

    <h2>Residual Notation</h2>

    <p>
      Residuals are commonly denoted by:
    </p>

    <div class="example-box">

      <p>
        e = y − ŷ
      </p>
    </div>

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>y = observed outcome</li>

      <li>ŷ = predicted outcome</li>

      <li>e = residual</li>

    </ul>

    <h2>A Simple Example</h2>

    <p>
      Suppose a regression model predicts an exam score of 80.
    </p>

    <p>
      A student actually scores 86.
    </p>

    <p>
      The residual is:
    </p>

    <div class="example-box">

      <p>
        86 − 80 = 6
      </p>
    </div>

    <p>
      The observation lies 6 points above the regression line.
    </p>

    <h2>Positive Residuals</h2>

    <p>
      A positive residual occurs when:
    </p>

    <div class="example-box">

      <p>
        Observed Value &gt; Predicted Value
      </p>
    </div>

    <p>
      This means the model underestimated the outcome.
    </p>

    <p>
      The observation appears above the regression line.
    </p>

    <h2>Negative Residuals</h2>

    <p>
      A negative residual occurs when:
    </p>

    <div class="example-box">

      <p>
        Observed Value &lt; Predicted Value
      </p>
    </div>

    <p>
      This means the model overestimated the outcome.
    </p>

    <p>
      The observation appears below the regression line.
    </p>

    <h2>Zero Residual</h2>

    <p>
      If the observed value equals the predicted value:
    </p>

    <div class="example-box">

      <p>
        Residual = 0
      </p>
    </div>

    <p>
      The observation falls exactly on the regression line.
    </p>

    <p>
      Perfect predictions produce zero residuals.
    </p>

    <h2>Residuals Measure Unexplained Variation</h2>

    <p>
      Recall the distinction between signal and noise.
    </p>

    <p>
      The regression line represents the systematic signal.
    </p>

    <p>
      Residuals represent variation not explained by the model.
    </p>

    <div class="concept-box">

      <strong>Key interpretation:</strong>

      <p>
        Residuals capture the portion of the outcome that remains unexplained after accounting for the predictor variable.
      </p>

    </div>

    <h2>Why We Need a Best-Fitting Line</h2>

    <p>
      Many different lines can be drawn through a scatterplot.
    </p>

    <p>
      The question becomes:
    </p>

    <div class="example-box">

      <p>
        Which line fits the data best?
      </p>
    </div>

    <p>
      Regression answers this question using the least-squares principle.
    </p>

    <h2>The Problem With Raw Residuals</h2>

    <p>
      One possible idea would be to add all residuals together.
    </p>

    <p>
      However, positive and negative residuals cancel each other out.
    </p>

    <p>
      A model with large errors could still produce a residual sum near zero.
    </p>

    <p>
      We therefore need a different measure of overall error.
    </p>

    <h2>Squaring the Residuals</h2>

    <p>
      To prevent cancellation, regression squares every residual.
    </p>

    <p>
      Squaring produces two useful effects:
    </p>

    <ul class="bullets">

      <li>All values become positive</li>

      <li>Large errors receive greater weight</li>

    </ul>

    <p>
      This creates a meaningful measure of total prediction error.
    </p>

    <h2>The Least-Squares Criterion</h2>

    <p>
      The least-squares method selects the regression line that minimizes:
    </p>

    <div class="example-box">

      <p>
        Sum of Squared Residuals
      </p>
    </div>

    <p>
      This quantity is often abbreviated:
    </p>

    <div class="example-box">

      <p>
        SSR = Σe²
      </p>
    </div>

    <p>
      Smaller values indicate a better-fitting regression line.
    </p>

    <h2>Why Least Squares Is Popular</h2>

    <p>
      Least squares has several important advantages:
    </p>

    <ul class="bullets">

      <li>Simple mathematical properties</li>

      <li>Unique best-fitting solution</li>

      <li>Penalizes large errors strongly</li>

      <li>Works well in many applications</li>

    </ul>

    <p>
      These advantages explain its widespread use in statistics.
    </p>

    <h2>Visual Interpretation</h2>

    <p>
      On a scatterplot, residuals appear as vertical distances between observed points and the regression line.
    </p>

    <p>
      The least-squares line is the line that makes the total squared distances as small as possible.
    </p>

    <p>
      No other straight line achieves a smaller total squared error.
    </p>

    <h2>Residuals and Model Quality</h2>

    <p>
      Large residuals indicate poor predictions for specific observations.
    </p>

    <p>
      Small residuals indicate predictions that closely match observed values.
    </p>

    <p>
      Examining residuals helps analysts evaluate model performance.
    </p>

    <h2>Residuals Reveal Problems</h2>

    <p>
      Residual analysis can uncover issues such as:
    </p>

    <ul class="bullets">

      <li>Nonlinear relationships</li>

      <li>Outliers</li>

      <li>Changing variability</li>

      <li>Model misspecification</li>

    </ul>

    <p>
      Residuals are therefore a critical diagnostic tool.
    </p>

    <h2>Residuals and Prediction</h2>

    <p>
      Even excellent models typically produce nonzero residuals.
    </p>

    <p>
      Prediction errors are a natural consequence of uncertainty and noise.
    </p>

    <p>
      The goal is not perfect prediction but useful prediction.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        A good regression model minimizes error, but it does not eliminate uncertainty.
      </p>

    </div>

    <h2>Connection to Future Lessons</h2>

    <p>
      Residuals play a central role throughout regression analysis.
    </p>

    <p>
      Many measures of model performance are based on residuals, including:
    </p>

    <ul class="bullets">

      <li>R-squared</li>

      <li>Residual standard error</li>

      <li>Diagnostic plots</li>

      <li>Model comparison metrics</li>

    </ul>

    <p>
      Understanding residuals is therefore essential for evaluating regression models.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Regression models attempt to explain variation in an outcome variable.
    </p>

    <p>
      Residuals measure the variation that remains unexplained.
    </p>

    <p>
      The least-squares method finds the regression line that minimizes total squared prediction error, providing the foundation for modern regression analysis.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Residuals are prediction errors equal to observed values minus predicted values. The least-squares method chooses the regression line that minimizes the sum of squared residuals, producing the best-fitting linear model.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Once a regression line has been fitted, analysts want to know how much variation in the outcome it actually explains.
    </p>

    <p>
      One of the most widely used measures for answering this question is R-squared.
    </p>

    <p>
      The next lesson introduces R-squared and explains how it measures model fit.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Residuals are prediction errors for individual observations</li>

        <li>Residual = Observed Value − Predicted Value</li>

        <li>Positive residuals indicate underprediction</li>

        <li>Negative residuals indicate overprediction</li>

        <li>Residuals represent unexplained variation</li>

        <li>Least squares minimizes the sum of squared residuals</li>

        <li>Squaring prevents positive and negative errors from canceling</li>

        <li>Residual analysis is essential for evaluating model quality</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/intercept/">
         ← Previous: Intercept
      </a>

      <a class="btn"
         href="/modeling/simple-linear-regression/r-squared/">
         Next: R-Squared →
      </a>

    </div>

  </div>

</section>