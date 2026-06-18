---
layout: default
title: Comparing Linear and Logistic Regression
description: Learn the similarities and differences between linear and logistic regression, including outcomes, interpretation, assumptions, predictions, and applications.
permalink: /modeling/extensions/comparing-linear-and-logistic/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_extensions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/extensions/comparing-linear-and-logistic/",
    label: "Comparing Linear and Logistic Regression",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 7</span>
      <span class="badge">Extensions</span>
      <span class="badge">Model Comparison</span>
    </div>

    <h1>Comparing Linear and Logistic Regression</h1>

    <p class="lead">
      Linear regression and logistic regression are two of the most important statistical models.
    </p>

    <p class="lead">
      Although they share many underlying ideas, they are designed for different types of outcomes and produce different kinds of interpretations.
    </p>

    <p class="lead">
      Understanding their similarities and differences helps analysts choose the appropriate model for a given problem.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/extensions/link-functions/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/extensions/bridge-to-machine-learning/">
         Next: Bridge to Machine Learning →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Two Models, One Foundation</h2>

    <p>
      At first glance, linear regression and logistic regression appear quite different.
    </p>

    <p>
      However, both models are built around the same central idea:
    </p>

    <div class="example-box">

      <p>
        Use predictor variables to explain or predict an outcome.
      </p>
    </div>

    <p>
      Both models estimate coefficients, evaluate relationships, and generate predictions.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Linear and logistic regression share a common regression framework but differ in the types of outcomes they model and how predictions are interpreted.
      </p>

    </div>

    <h2>The Most Important Difference</h2>

    <p>
      The primary distinction involves the outcome variable.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Model</th>
            <th>Outcome Type</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Linear Regression</td>
            <td>Continuous</td>
          </tr>

          <tr>
            <td>Logistic Regression</td>
            <td>Binary</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This difference drives many of the distinctions between the two approaches.
    </p>

    <h2>Linear Regression Predictions</h2>

    <p>
      Linear regression predicts numerical values directly.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Income</li>

      <li>Blood pressure</li>

      <li>Exam scores</li>

      <li>House prices</li>

    </ul>

    <p>
      Predictions can take many possible values.
    </p>

    <h2>Logistic Regression Predictions</h2>

    <p>
      Logistic regression predicts probabilities.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Probability of disease</li>

      <li>Probability of purchase</li>

      <li>Probability of default</li>

      <li>Probability of passing an exam</li>

    </ul>

    <p>
      Predicted values always remain between 0 and 1.
    </p>

    <h2>The Regression Equations</h2>

    <p>
      Both models use a linear predictor:
    </p>

    0

    <p>
      However, logistic regression adds a transformation that converts the linear predictor into a probability.
    </p>

    <p>
      This transformation is achieved through the logit link function.
    </p>

    <h2>Output Scale</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Feature</th>
            <th>Linear Regression</th>
            <th>Logistic Regression</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Prediction</td>
            <td>Numerical value</td>
            <td>Probability</td>
          </tr>

          <tr>
            <td>Range</td>
            <td>Unrestricted</td>
            <td>0 to 1</td>
          </tr>

          <tr>
            <td>Outcome Type</td>
            <td>Continuous</td>
            <td>Binary</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Coefficient Interpretation</h2>

    <p>
      The interpretation of coefficients differs substantially.
    </p>

    <h3>Linear Regression</h3>

    <p>
      A coefficient represents the expected change in the outcome associated with a one-unit increase in a predictor.
    </p>

    <div class="example-box">

      <p>
        Income increases by $2,000 for each additional year of education.
      </p>
    </div>

    <h3>Logistic Regression</h3>

    <p>
      A coefficient represents a change in log-odds.
    </p>

    <p>
      Analysts often convert coefficients into odds ratios for interpretation.
    </p>

    <div class="example-box">

      <p>
        Odds of purchase increase by 30% for each additional advertisement viewed.
      </p>
    </div>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Linear regression coefficients affect the outcome directly, while logistic regression coefficients affect odds and probabilities indirectly.
      </p>

    </div>

    <h2>Shapes of the Relationships</h2>

    <p>
      Linear regression assumes a straight-line relationship between predictors and the expected outcome.
    </p>

    <p>
      Logistic regression produces an S-shaped relationship between predictors and predicted probabilities.
    </p>

    <p>
      This shape helps keep predictions within valid probability limits.
    </p>

    <h2>Error Structure</h2>

    <p>
      The models also differ in how variability is represented.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Model</th>
            <th>Typical Distribution</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Linear Regression</td>
            <td>Normal</td>
          </tr>

          <tr>
            <td>Logistic Regression</td>
            <td>Binomial</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This difference is one reason logistic regression belongs to the broader GLM framework.
    </p>

    <h2>Model Assumptions</h2>

    <p>
      Both models rely on assumptions, but the assumptions differ somewhat.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Assumption</th>
            <th>Linear</th>
            <th>Logistic</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Independent observations</td>
            <td>Yes</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Linearity</td>
            <td>Outcome scale</td>
            <td>Logit scale</td>
          </tr>

          <tr>
            <td>Normally distributed errors</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Binary outcome required</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Common Applications</h2>

    <p>
      Linear regression is commonly used when predicting quantities.
    </p>

    <p>
      Logistic regression is commonly used when predicting categories or risks.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Question</th>
            <th>Appropriate Model</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>What will the house price be?</td>
            <td>Linear Regression</td>
          </tr>

          <tr>
            <td>Will the customer purchase?</td>
            <td>Logistic Regression</td>
          </tr>

          <tr>
            <td>What will the exam score be?</td>
            <td>Linear Regression</td>
          </tr>

          <tr>
            <td>Will the patient recover?</td>
            <td>Logistic Regression</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>What They Share</h2>

    <p>
      Despite their differences, both models involve:
    </p>

    <ul class="bullets">

      <li>Predictor variables</li>

      <li>Coefficients</li>

      <li>Hypothesis testing</li>

      <li>Confidence intervals</li>

      <li>Model diagnostics</li>

      <li>Prediction</li>

    </ul>

    <p>
      Learning one model makes it easier to understand the other.
    </p>

    <h2>Choosing Between Them</h2>

    <p>
      In most cases, the outcome variable determines the choice.
    </p>

    <div class="example-box">

      <p>
        Continuous outcome → Linear Regression
      </p>

      <p>
        Binary outcome → Logistic Regression
      </p>
    </div>

    <p>
      Selecting the correct model is essential for valid inference and prediction.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Logistic regression is not a replacement for linear regression. It is an extension designed for a different type of outcome variable.
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Linear and logistic regression are closely related members of the broader Generalized Linear Model family.
    </p>

    <p>
      They share common principles while addressing different types of analytical problems.
    </p>

    <p>
      Understanding both models provides a foundation for many additional statistical and machine learning methods.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Linear regression models continuous outcomes, while logistic regression models binary outcomes. Although they differ in prediction scales, interpretation, and assumptions, both share the same underlying regression framework.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Regression models form part of a much larger predictive modeling landscape.
    </p>

    <p>
      Many machine learning algorithms build upon ideas that are already familiar from statistical modeling, including prediction, model fitting, evaluation, and generalization.
    </p>

    <p>
      The next lesson serves as a bridge to machine learning and shows how regression concepts connect to modern predictive analytics.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Linear regression models continuous outcomes</li>

        <li>Logistic regression models binary outcomes</li>

        <li>Linear regression predicts values directly, while logistic regression predicts probabilities</li>

        <li>Linear coefficients affect outcomes directly</li>

        <li>Logistic coefficients affect log-odds and odds ratios</li>

        <li>The models use different distributions and link functions</li>

        <li>Both belong to the Generalized Linear Model family</li>

        <li>The outcome variable usually determines which model is appropriate</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/extensions/link-functions/">
         ← Previous: Link Functions
      </a>

      <a class="btn"
         href="/modeling/extensions/bridge-to-machine-learning/">
         Next: Bridge to Machine Learning →
      </a>

    </div>

  </div>

</section>