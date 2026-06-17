---
layout: default
title: Residuals
description: Learn what residuals are, why they are central to regression diagnostics, and how they help analysts evaluate model quality.
permalink: /modeling/diagnostics/residuals/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_diagnostics_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/diagnostics/residuals/",
    label: "Residuals",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 5</span>
      <span class="badge">Diagnostics</span>
      <span class="badge">Foundations</span>
    </div>

    <h1>Residuals</h1>

    <p class="lead">
      Every regression model makes mistakes.
    </p>

    <p class="lead">
      Residuals measure those mistakes and provide one of the most important tools for evaluating whether a model is performing appropriately.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/diagnostics/">
         ← Block Home
      </a>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/residual-plots/">
         Next: Residual Plots →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Residual?</h2>

    <p>
      A residual is the difference between an observed outcome and the value predicted by a regression model.
    </p>

    <p>
      It measures how far the model's prediction misses the actual observation.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Residuals are prediction errors. They show how closely a regression model matches the observed data.
      </p>

    </div>

    <h2>The Residual Formula</h2>

    <p>
      Residuals are calculated as:
    </p>

    

    <p>
      where:
    </p>

    <ul class="bullets">

      <li><strong>y</strong> = observed value</li>

      <li><strong>ŷ</strong> = predicted value</li>

      <li><strong>e</strong> = residual</li>

    </ul>

    <p>
      Each observation has its own residual.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose a regression model predicts an exam score of 82.
    </p>

    <p>
      The student's actual score is 88.
    </p>

    <p>
      The residual is:
    </p>

    <div class="example-box">

      <p>
        Residual = 88 − 82 = 6
      </p>
    </div>

    <p>
      The model underestimated the student's score by 6 points.
    </p>

    <h2>Positive and Negative Residuals</h2>

    <p>
      Residuals can be either positive or negative.
    </p>

    <ul class="bullets">

      <li>Positive residual → actual value exceeds prediction</li>

      <li>Negative residual → actual value is below prediction</li>

    </ul>

    <p>
      The sign indicates the direction of the prediction error.
    </p>

    <h2>Residuals Represent Unexplained Variation</h2>

    <p>
      Regression models rarely explain everything.
    </p>

    <p>
      Residuals represent the portion of the outcome that remains unexplained after accounting for the predictors in the model.
    </p>

    <p>
      They capture randomness, omitted factors, measurement error, and other influences.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Residuals contain information about what the model failed to explain.
      </p>

    </div>

    <h2>Why Residuals Matter</h2>

    <p>
      Residuals are central to regression diagnostics.
    </p>

    <p>
      By studying residuals, analysts can evaluate:
    </p>

    <ul class="bullets">

      <li>Model fit</li>

      <li>Assumption validity</li>

      <li>Prediction quality</li>

      <li>Potential problems in the model</li>

    </ul>

    <p>
      Residual analysis is often more informative than simply examining coefficients.
    </p>

    <h2>Good Models and Residuals</h2>

    <p>
      A good regression model typically produces residuals that:
    </p>

    <ul class="bullets">

      <li>Are relatively small</li>

      <li>Have no obvious pattern</li>

      <li>Are centered around zero</li>

      <li>Appear randomly distributed</li>

    </ul>

    <p>
      These characteristics suggest that the model has captured the main structure of the data.
    </p>

    <h2>Large Residuals</h2>

    <p>
      Large residuals indicate observations that the model predicts poorly.
    </p>

    <p>
      Such observations may arise because of:
    </p>

    <ul class="bullets">

      <li>Outliers</li>

      <li>Missing predictors</li>

      <li>Measurement error</li>

      <li>Model misspecification</li>

    </ul>

    <p>
      Large residuals often warrant further investigation.
    </p>

    <h2>Residuals and Model Assumptions</h2>

    <p>
      Most regression assumptions are evaluated through residual behavior.
    </p>

    <p>
      Analysts examine residuals to assess:
    </p>

    <ul class="bullets">

      <li>Linearity</li>

      <li>Independence</li>

      <li>Constant variance</li>

      <li>Normality</li>

    </ul>

    <p>
      Residuals therefore serve as the primary diagnostic window into model performance.
    </p>

    <h2>Residuals Are Not Random Noise Alone</h2>

    <p>
      Ideally, residuals should resemble random noise.
    </p>

    <p>
      However, systematic patterns sometimes appear.
    </p>

    <p>
      These patterns often reveal problems with the model.
    </p>

    <p>
      Detecting such patterns is one of the primary goals of regression diagnostics.
    </p>

    <h2>Residuals and Prediction Accuracy</h2>

    <p>
      Prediction accuracy is closely related to residual size.
    </p>

    <p>
      Smaller residuals generally indicate more accurate predictions.
    </p>

    <p>
      Larger residuals suggest greater prediction error.
    </p>

    <h2>Residuals and Least Squares</h2>

    <p>
      Ordinary least squares regression chooses coefficient estimates by minimizing the sum of squared residuals.
    </p>

    <p>
      This means residuals are directly involved in determining the fitted regression line.
    </p>

    <p>
      The model is literally built around them.
    </p>

    <h2>Residuals vs Errors</h2>

    <p>
      The terms residual and error are often used interchangeably, but they are not identical.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Term</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Error</td>
            <td>True but unobservable deviation from the population model</td>
          </tr>

          <tr>
            <td>Residual</td>
            <td>Observed estimate of that deviation in a sample</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      In practice, residuals provide the information analysts can actually examine.
    </p>

    <h2>Standardized Residuals</h2>

    <p>
      Raw residuals depend on the scale of the outcome variable.
    </p>

    <p>
      Analysts often standardize residuals so they can be compared more easily across observations.
    </p>

    <p>
      Standardized residuals are especially useful for identifying unusual observations.
    </p>

    <h2>Residuals and Outliers</h2>

    <p>
      Observations with exceptionally large residuals may be outliers.
    </p>

    <p>
      Such observations deserve attention because they may influence conclusions and indicate model weaknesses.
    </p>

    <h2>The Foundation of Diagnostics</h2>

    <p>
      Nearly every regression diagnostic begins with residuals.
    </p>

    <p>
      Residual plots, influence measures, normality checks, and variance assessments all rely on residual information.
    </p>

    <p>
      Understanding residuals is therefore essential before learning more advanced diagnostic techniques.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Coefficients describe the model. Residuals reveal how well the model actually works.
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Regression models attempt to explain and predict outcomes, but no model is perfect.
    </p>

    <p>
      Residuals quantify the gap between model predictions and reality.
    </p>

    <p>
      By studying residuals, analysts gain insight into model accuracy, assumption validity, and opportunities for improvement.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Residuals are the differences between observed and predicted values. They represent unexplained variation and provide the primary tool for evaluating model fit, assumptions, and prediction quality.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Individual residual values are informative, but visualizing residuals often reveals patterns that are difficult to detect numerically.
    </p>

    <p>
      One of the most powerful diagnostic tools in regression is the residual plot.
    </p>

    <p>
      The next lesson explores residual plots and shows how they help analysts identify assumption violations and model weaknesses.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Residuals are differences between observed and predicted values</li>

        <li>Residuals represent unexplained variation in the outcome</li>

        <li>Positive residuals indicate underprediction</li>

        <li>Negative residuals indicate overprediction</li>

        <li>Residuals are central to regression diagnostics</li>

        <li>Good models typically produce small, pattern-free residuals</li>

        <li>Large residuals may indicate outliers or model problems</li>

        <li>Residual analysis provides critical insight into model performance</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/diagnostics/">
         ← Back to Block Home
      </a>

      <a class="btn"
         href="/modeling/diagnostics/residual-plots/">
         Next: Residual Plots →
      </a>

    </div>

  </div>

</section>