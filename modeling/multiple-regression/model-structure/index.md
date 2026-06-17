---
layout: default
title: Model Structure
description: Learn the structure of the multiple regression model and how several predictors are combined to explain and predict an outcome.
permalink: /modeling/multiple-regression/model-structure/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_multiple_regression_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/multiple-regression/model-structure/",
    label: "Model Structure",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 3</span>
      <span class="badge">Multiple Regression</span>
      <span class="badge">Model Structure</span>
    </div>

    <h1>Model Structure</h1>

    <p class="lead">
      Multiple regression extends the simple regression model by allowing several predictors to influence an outcome simultaneously.
    </p>

    <p class="lead">
      Understanding the structure of the model is essential because it provides the foundation for interpretation, prediction, and statistical inference.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/multiple-regression/why-multiple/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/adjusted-effects/">
         Next: Adjusted Effects →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>From One Predictor to Many</h2>

    <p>
      Simple linear regression uses a single predictor variable.
    </p>

    <p>
      Its structure is:
    </p>

    <div class="example-box">

      <p>
        Outcome = Intercept + Slope × Predictor
      </p>
    </div>

    <p>
      Multiple regression extends this idea by including additional predictors.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Multiple regression models an outcome as a combination of several predictor variables, each with its own estimated effect.
      </p>

    </div>

    <h2>The Multiple Regression Equation</h2>

    <p>
      The general form of a multiple regression model is:
    </p>

    <div class="example-box">

      <p>
        y = β₀ + β₁x₁ + β₂x₂ + β₃x₃ + ... + βₖxₖ
      </p>
    </div>

    <p>
      This equation may appear more complex than simple regression, but the underlying logic is the same.
    </p>

    <h2>What the Symbols Mean</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Symbol</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>y</td>
            <td>Outcome variable</td>
          </tr>

          <tr>
            <td>β₀</td>
            <td>Intercept</td>
          </tr>

          <tr>
            <td>x₁, x₂, ..., xₖ</td>
            <td>Predictor variables</td>
          </tr>

          <tr>
            <td>β₁, β₂, ..., βₖ</td>
            <td>Regression coefficients</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Each predictor has its own coefficient that measures its contribution to the model.
    </p>

    <h2>A Housing Example</h2>

    <p>
      Suppose we want to predict house prices.
    </p>

    <p>
      A multiple regression model might include:
    </p>

    <ul class="bullets">

      <li>House size</li>

      <li>Number of bedrooms</li>

      <li>Property age</li>

      <li>Distance from city center</li>

    </ul>

    <p>
      The regression equation combines all of these variables into a single prediction.
    </p>

    <h2>Each Predictor Gets Its Own Effect</h2>

    <p>
      Unlike simple regression, multiple regression allows each predictor to contribute separately.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>Size may increase price</li>

      <li>Property age may decrease price</li>

      <li>Location may increase price</li>

    </ul>

    <p>
      The model estimates all of these effects simultaneously.
    </p>

    <h2>Adding Contributions Together</h2>

    <p>
      The predicted outcome is obtained by adding:
    </p>

    <ul class="bullets">

      <li>The intercept</li>

      <li>The contribution from predictor 1</li>

      <li>The contribution from predictor 2</li>

      <li>The contribution from predictor 3</li>

      <li>And so on</li>

    </ul>

    <p>
      Each predictor contributes according to its coefficient and observed value.
    </p>

    <h2>A Numerical Illustration</h2>

    <p>
      Suppose a model is:
    </p>

    <div class="example-box">

      <p>
        Price = 50,000 + 120(Size) + 15,000(Bedrooms)
      </p>
    </div>

    <p>
      For a home with:
    </p>

    <ul class="bullets">

      <li>Size = 2,000 square feet</li>

      <li>Bedrooms = 3</li>

    </ul>

    <p>
      The prediction combines contributions from both variables.
    </p>

    <p>
      This illustrates how multiple predictors work together within the model.
    </p>

    <h2>The Intercept Still Exists</h2>

    <p>
      Multiple regression still contains an intercept term.
    </p>

    <p>
      The intercept represents the expected outcome when all predictors equal zero.
    </p>

    <p>
      As in simple regression, the practical interpretation may or may not be meaningful.
    </p>

    <h2>More Predictors, More Flexibility</h2>

    <p>
      Each additional predictor allows the model to capture more information about the outcome.
    </p>

    <p>
      This often improves:
    </p>

    <ul class="bullets">

      <li>Prediction accuracy</li>

      <li>Explanatory power</li>

      <li>Understanding of relationships</li>

    </ul>

    <p>
      However, additional predictors also increase complexity.
    </p>

    <h2>Simple Regression as a Special Case</h2>

    <p>
      If a multiple regression model contains only one predictor:
    </p>

    <div class="example-box">

      <p>
        y = β₀ + β₁x₁
      </p>
    </div>

    <p>
      it becomes simple linear regression.
    </p>

    <p>
      Thus, simple regression is simply the simplest form of the more general multiple regression framework.
    </p>

    <h2>Prediction in Multiple Regression</h2>

    <p>
      Predictions are generated the same way as before.
    </p>

    <p>
      We substitute predictor values into the regression equation and calculate the resulting outcome estimate.
    </p>

    <p>
      The only difference is that several predictors now contribute to the prediction.
    </p>

    <h2>Residuals Still Exist</h2>

    <p>
      Even with multiple predictors, predictions are rarely perfect.
    </p>

    <p>
      The difference between observed and predicted values remains:
    </p>

    <div class="example-box">

      <p>
        Residual = Observed − Predicted
      </p>
    </div>

    <p>
      Residuals continue to represent unexplained variation.
    </p>

    <h2>Least Squares Still Fits the Model</h2>

    <p>
      Multiple regression is still typically estimated using ordinary least squares.
    </p>

    <p>
      The procedure chooses coefficients that minimize the total squared residuals.
    </p>

    <p>
      The principle is unchanged from simple regression.
    </p>

    <h2>The Main Challenge</h2>

    <p>
      The structure of the equation is straightforward.
    </p>

    <p>
      The greater challenge lies in interpretation.
    </p>

    <p>
      Once multiple predictors are included, each coefficient must be interpreted while accounting for the others.
    </p>

    <p>
      This idea becomes central to multiple regression analysis.
    </p>

    <div class="concept-box">

      <strong>Important transition:</strong>

      <p>
        In multiple regression, coefficients represent effects after accounting for the other predictors in the model.
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Multiple regression extends simple regression by combining several predictors into a single model.
    </p>

    <p>
      Each predictor contributes its own estimated effect, allowing more realistic explanations and predictions of complex outcomes.
    </p>

    <p>
      The structure is simple, but interpreting the resulting coefficients requires careful thinking.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The multiple regression model combines several predictors into a single equation. Each predictor has its own coefficient, and the outcome is predicted by combining the contributions of all included variables.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Once multiple predictors are included, regression coefficients take on a new interpretation.
    </p>

    <p>
      Rather than describing simple relationships, they describe effects after accounting for other variables in the model.
    </p>

    <p>
      The next lesson introduces adjusted effects and explains how coefficients should be interpreted in multiple regression.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Multiple regression extends simple regression by including several predictors</li>

        <li>Each predictor receives its own regression coefficient</li>

        <li>The outcome is predicted by combining contributions from all predictors</li>

        <li>The intercept remains part of the model</li>

        <li>Simple regression is a special case of multiple regression</li>

        <li>Predictions are generated by substituting values into the regression equation</li>

        <li>Residuals and least squares remain fundamental concepts</li>

        <li>Coefficient interpretation becomes more complex when multiple predictors are included</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/why-multiple/">
         ← Previous: Why Multiple Regression?
      </a>

      <a class="btn"
         href="/modeling/multiple-regression/adjusted-effects/">
         Next: Adjusted Effects →
      </a>

    </div>

  </div>

</section>