---
layout: default
title: Linearity
description: Learn the linearity assumption in regression, why it matters, how to assess it, and what happens when relationships are not linear.
permalink: /modeling/assumptions/linearity/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_assumptions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/assumptions/linearity/",
    label: "Linearity",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 4</span>
      <span class="badge">Assumptions</span>
      <span class="badge">Linearity</span>
    </div>

    <h1>Linearity</h1>

    <p class="lead">
      The first major regression assumption concerns the shape of the relationship between predictors and the outcome.
    </p>

    <p class="lead">
      Regression assumes that predictors are related to the outcome through a linear pattern, meaning changes in predictors produce approximately proportional changes in the expected outcome.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/assumptions/why-assumptions/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/assumptions/independence/">
         Next: Independence →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is the Linearity Assumption?</h2>

    <p>
      Regression models assume that the expected value of the outcome changes linearly with the predictors.
    </p>

    <p>
      In practical terms, this means the model assumes that a straight-line relationship provides a reasonable description of the data.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        The linearity assumption states that the average relationship between predictors and the outcome can be represented by a linear function.
      </p>

    </div>

    <h2>What "Linear" Really Means</h2>

    <p>
      Many students assume linearity means all variables must form a perfect straight line.
    </p>

    <p>
      This is not true.
    </p>

    <p>
      Real data always contain variability and noise.
    </p>

    <p>
      Linearity concerns the average pattern rather than every individual observation.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose study hours predict exam scores.
    </p>

    <p>
      A linear relationship suggests that each additional hour of study produces roughly the same expected increase in score.
    </p>

    <p>
      The relationship may not be perfect, but it follows an approximately straight-line pattern.
    </p>

    <h2>Why Linearity Matters</h2>

    <p>
      Regression coefficients are interpreted as constant effects.
    </p>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        One additional study hour increases expected score by 4 points.
      </p>
    </div>

    <p>
      This interpretation only makes sense if the relationship is approximately linear.
    </p>

    <p>
      If the effect changes dramatically across values of the predictor, the interpretation becomes misleading.
    </p>

    <h2>Linearity and the Regression Equation</h2>

    <p>
      A simple regression model takes the form:
    </p>

    

    <p>
      This equation assumes a constant slope across all values of the predictor.
    </p>

    <p>
      The same basic principle applies in multiple regression.
    </p>

    <h2>Examples of Nonlinear Relationships</h2>

    <p>
      Many real-world relationships are not perfectly linear.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Growth curves</li>

      <li>Diminishing returns</li>

      <li>Learning curves</li>

      <li>Saturation effects</li>

      <li>Threshold effects</li>

    </ul>

    <p>
      In these situations, a straight line may not adequately describe the relationship.
    </p>

    <h2>Diminishing Returns Example</h2>

    <p>
      Consider study time and exam performance.
    </p>

    <p>
      The first few hours of study may greatly improve performance.
    </p>

    <p>
      Additional hours may still help but by progressively smaller amounts.
    </p>

    <p>
      This pattern creates curvature rather than a straight line.
    </p>

    <h2>What Happens When Linearity Fails?</h2>

    <p>
      When the relationship is strongly nonlinear:
    </p>

    <ul class="bullets">

      <li>Coefficient interpretations become inaccurate</li>

      <li>Predictions may become biased</li>

      <li>Residual patterns may appear systematic</li>

      <li>Model fit may deteriorate</li>

    </ul>

    <p>
      The model is attempting to fit a straight line to a curved relationship.
    </p>

    <div class="concept-box">

      <strong>Important warning:</strong>

      <p>
        A linear model can provide misleading results when the true relationship contains substantial curvature.
      </p>

    </div>

    <h2>Residual Plots and Linearity</h2>

    <p>
      One of the most important diagnostic tools is the residual plot.
    </p>

    <p>
      If linearity is reasonable:
    </p>

    <ul class="bullets">

      <li>Residuals appear randomly scattered around zero</li>

      <li>No obvious pattern is visible</li>

    </ul>

    <p>
      This suggests the model has captured the main relationship adequately.
    </p>

    <h2>Signs of Nonlinearity</h2>

    <p>
      Residual plots may reveal:
    </p>

    <ul class="bullets">

      <li>Curved patterns</li>

      <li>U-shaped patterns</li>

      <li>Inverted U-shapes</li>

      <li>Systematic trends</li>

    </ul>

    <p>
      Such patterns often indicate that the linearity assumption is questionable.
    </p>

    <h2>Scatterplots as a Diagnostic Tool</h2>

    <p>
      Scatterplots are often the first step in assessing linearity.
    </p>

    <p>
      Analysts look for:
    </p>

    <ul class="bullets">

      <li>Approximately straight trends</li>

      <li>Curvature</li>

      <li>Clusters</li>

      <li>Unusual patterns</li>

    </ul>

    <p>
      Visual inspection frequently provides valuable information before formal modeling begins.
    </p>

    <h2>Linearity Does Not Mean Simplicity</h2>

    <p>
      The term "linear" refers to the model's coefficients rather than necessarily the raw variables themselves.
    </p>

    <p>
      Analysts can often model nonlinear relationships by introducing transformed predictors while maintaining a linear regression framework.
    </p>

    <p>
      This distinction becomes important in more advanced modeling.
    </p>

    <h2>Possible Solutions</h2>

    <p>
      When nonlinearity is detected, several approaches may help:
    </p>

    <ul class="bullets">

      <li>Transform variables</li>

      <li>Add polynomial terms</li>

      <li>Use interaction terms</li>

      <li>Fit alternative models</li>

    </ul>

    <p>
      The appropriate solution depends on the nature of the relationship.
    </p>

    <h2>How Serious Is Nonlinearity?</h2>

    <p>
      Small deviations from linearity are often acceptable.
    </p>

    <p>
      Regression methods are frequently robust to minor imperfections.
    </p>

    <p>
      Severe curvature is more concerning because it can undermine interpretation and prediction.
    </p>

    <h2>Linearity and Prediction</h2>

    <p>
      Even if prediction is the primary goal, strong nonlinearity can reduce predictive accuracy.
    </p>

    <p>
      Capturing the correct shape of the relationship often improves forecasts substantially.
    </p>

    <p>
      This is one reason model diagnostics remain important in predictive settings.
    </p>

    <h2>Linearity in Multiple Regression</h2>

    <p>
      In multiple regression, the linearity assumption applies to each predictor's contribution after accounting for the other predictors.
    </p>

    <p>
      Analysts therefore evaluate linearity within the broader multivariable context rather than examining predictors in isolation.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Linearity is one of the foundational assumptions of regression analysis.
    </p>

    <p>
      It allows coefficients to be interpreted as constant effects and supports the mathematical framework underlying regression models.
    </p>

    <p>
      Evaluating linearity helps ensure that the model captures the essential structure of the data rather than forcing a straight line onto a fundamentally curved relationship.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The linearity assumption states that predictors have approximately linear relationships with the expected outcome. When strong nonlinearity is present, coefficient interpretations and predictions may become unreliable, making diagnostic evaluation essential.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Another important regression assumption concerns independence.
    </p>

    <p>
      Regression generally assumes that observations provide separate pieces of information rather than being strongly dependent on one another.
    </p>

    <p>
      The next lesson explores the independence assumption and explains why dependent observations can create problems for statistical inference.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The linearity assumption concerns the average relationship between predictors and the outcome</li>

        <li>Regression coefficients assume approximately constant effects</li>

        <li>Strong nonlinear relationships can distort interpretation and prediction</li>

        <li>Residual plots are key tools for assessing linearity</li>

        <li>Curved residual patterns often indicate nonlinearity</li>

        <li>Scatterplots provide useful visual evidence about relationship shape</li>

        <li>Minor deviations from linearity are often acceptable</li>

        <li>Evaluating linearity helps ensure the regression model appropriately represents the data</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/assumptions/why-assumptions/">
         ← Previous: Why Assumptions Matter
      </a>

      <a class="btn"
         href="/modeling/assumptions/independence/">
         Next: Independence →
      </a>

    </div>

  </div>

</section>