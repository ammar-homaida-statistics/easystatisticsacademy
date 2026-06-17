---
layout: default
title: Residuals
description: Learn what residuals are, why they are central to regression diagnostics, and how they help evaluate model performance.
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
      <span class="badge">Residuals</span>
    </div>

    <h1>Residuals</h1>

    <p class="lead">
      Every regression model makes prediction errors.
    </p>

    <p class="lead">
      These errors, known as residuals, provide some of the most important information for evaluating whether a model is working well and whether its assumptions are reasonable.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/diagnostics/">
         ← Block Home
      </a>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/residual-plot/">
         Next: Residual Plot →
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
      It measures how far the model's prediction is from reality for a particular observation.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Residuals represent prediction errors and provide a direct way to assess how well a regression model fits the data.
      </p>

    </div>

    <h2>The Residual Formula</h2>

    <p>
      Residuals are calculated as:
    </p>

    0

    <p>
      where:
    </p>

    <ul class="bullets">

      <li><strong>y</strong> is the observed value</li>

      <li><strong>ŷ</strong> is the predicted value</li>

      <li><strong>e</strong> is the residual</li>

    </ul>

    <p>
      Positive residuals indicate underprediction, while negative residuals indicate overprediction.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose a regression model predicts an exam score of 82.
    </p>

    <p>
      A student actually scores 88.
    </p>

    <p>
      The residual equals:
    </p>

    <p>
      Residual = 88 − 82 = 6
    </p>

    <p>
      The model underpredicted the score by 6 points.
    </p>

    <h2>Positive and Negative Residuals</h2>

    <p>
      Residuals can be:
    </p>

    <ul class="bullets">

      <li>Positive</li>

      <li>Negative</li>

      <li>Zero</li>

    </ul>

    <p>
      A positive residual means the observed value exceeds the prediction.
    </p>

    <p>
      A negative residual means the prediction exceeds the observed value.
    </p>

    <p>
      A residual of zero indicates a perfect prediction.
    </p>

    <h2>Why Residuals Matter</h2>

    <p>
      The regression line itself only shows predicted values.
    </p>

    <p>
      Residuals reveal what the model fails to explain.
    </p>

    <p>
      By studying residuals, analysts can identify weaknesses that are invisible when examining coefficients alone.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Much of regression diagnostics focuses on residual behavior because residuals contain evidence about assumption violations and model quality.
      </p>

    </div>

    <h2>Residuals Measure Unexplained Variation</h2>

    <p>
      No regression model perfectly explains every observation.
    </p>

    <p>
      Residuals represent the portion of variability that remains unexplained after fitting the model.
    </p>

    <p>
      Smaller residuals generally indicate better model fit.
    </p>

    <h2>The Goal Is Not Zero Residuals</h2>

    <p>
      Many beginners assume a good model should produce residuals equal to zero.
    </p>

    <p>
      This is unrealistic.
    </p>

    <p>
      Real-world data contain noise, measurement error, and natural variability.
    </p>

    <p>
      A useful model typically leaves some residual variation unexplained.
    </p>

    <h2>Residuals and Model Fit</h2>

    <p>
      Large residuals suggest observations that are poorly predicted.
    </p>

    <p>
      Small residuals suggest observations that closely follow the model.
    </p>

    <p>
      Examining residual size helps evaluate overall model performance.
    </p>

    <h2>Residuals and Assumptions</h2>

    <p>
      Many regression assumptions concern residuals rather than the raw data.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>Linearity is evaluated using residual patterns</li>

      <li>Normality concerns residual distributions</li>

      <li>Homoscedasticity concerns residual variance</li>

      <li>Independence often involves residual dependence</li>

    </ul>

    <p>
      Residual analysis therefore connects directly to assumption checking.
    </p>

    <h2>Residuals Should Appear Random</h2>

    <p>
      When a model is working well, residuals should look random.
    </p>

    <p>
      They should not display obvious trends or systematic patterns.
    </p>

    <p>
      Patterns often indicate that important information has been missed.
    </p>

    <h2>Large Residuals and Outliers</h2>

    <p>
      Observations with unusually large residuals may be:
    </p>

    <ul class="bullets">

      <li>Outliers</li>

      <li>Data errors</li>

      <li>Special cases</li>

      <li>Evidence of model misspecification</li>

    </ul>

    <p>
      These observations often deserve further investigation.
    </p>

    <h2>Residuals and Prediction Accuracy</h2>

    <p>
      Prediction quality depends directly on residual size.
    </p>

    <p>
      Models with smaller residuals generally provide more accurate predictions.
    </p>

    <p>
      Many prediction metrics are based on residuals.
    </p>

    <h2>Residuals vs Errors</h2>

    <p>
      The terms "error" and "residual" are related but not identical.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Concept</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Error</td>
            <td>True unknown deviation from reality</td>
          </tr>

          <tr>
            <td>Residual</td>
            <td>Observed estimate of that deviation</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Residuals are observable, whereas true errors are generally unknown.
    </p>

    <h2>Residuals in Multiple Regression</h2>

    <p>
      The concept remains the same regardless of model complexity.
    </p>

    <p>
      Whether a model contains one predictor or twenty predictors, residuals still measure the difference between observed and predicted values.
    </p>

    <p>
      Residual analysis remains fundamental.
    </p>

    <h2>Residuals as Diagnostic Tools</h2>

    <p>
      Residuals are often called the "window into the model."
    </p>

    <p>
      Instead of focusing only on what the model explains, analysts examine what the model fails to explain.
    </p>

    <p>
      This perspective frequently reveals hidden problems.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Good regression diagnostics begin with residuals because residual behavior often reveals issues that coefficient estimates cannot.
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Residuals represent the unexplained component of a regression model.
    </p>

    <p>
      They quantify prediction errors, help assess model fit, and provide the foundation for most regression diagnostics.
    </p>

    <p>
      Understanding residuals is essential because nearly every assumption-checking technique relies on analyzing their behavior.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Residuals are the differences between observed and predicted values. They measure prediction errors, reveal unexplained variation, and serve as the primary tool for evaluating regression assumptions and model quality.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Residuals become especially useful when visualized.
    </p>

    <p>
      One of the most important diagnostic tools in regression is the residual plot.
    </p>

    <p>
      The next lesson explores residual plots and explains how they help identify assumption violations, model weaknesses, and opportunities for improvement.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Residuals are differences between observed and predicted values</li>

        <li>Residuals measure prediction errors</li>

        <li>Positive residuals indicate underprediction</li>

        <li>Negative residuals indicate overprediction</li>

        <li>Residuals represent unexplained variation</li>

        <li>Many regression assumptions are evaluated using residuals</li>

        <li>Large residuals may indicate outliers or model problems</li>

        <li>Residual analysis forms the foundation of regression diagnostics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/diagnostics/">
         ← Back to Block Home
      </a>

      <a class="btn"
         href="/modeling/diagnostics/residual-plot/">
         Next: Residual Plot →
      </a>

    </div>

  </div>

</section>