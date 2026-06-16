---
layout: default
title: Correlation vs Regression
description: Learn the differences between correlation and regression, what each measures, and when to use one instead of the other.
permalink: /modeling/simple-linear-regression/correlation-vs-regression/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_simple_linear_regression_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/simple-linear-regression/correlation-vs-regression/",
    label: "Correlation vs Regression",
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
      <span class="badge">Relationships</span>
    </div>

    <h1>Correlation vs Regression</h1>

    <p class="lead">
      Correlation and regression are closely related statistical tools, and they are often introduced together.
    </p>

    <p class="lead">
      Although both study relationships between variables, they answer different questions and serve different purposes.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/simple-linear-regression/r-squared/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/prediction/">
         Next: Prediction →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why People Confuse Them</h2>

    <p>
      Both correlation and regression examine relationships between variables.
    </p>

    <p>
      Both often use the same dataset.
    </p>

    <p>
      Both are strongest when variables move together in a consistent linear pattern.
    </p>

    <p>
      Because of these similarities, the concepts are frequently confused.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Correlation measures the strength of association between variables, while regression models how one variable changes as another changes.
      </p>

    </div>

    <h2>What Correlation Measures</h2>

    <p>
      Correlation measures the strength and direction of a relationship between two variables.
    </p>

    <p>
      The most common measure is the Pearson correlation coefficient, denoted by:
    </p>

    <div class="example-box">

      <p>
        r
      </p>
    </div>

    <p>
      Correlation focuses on association, not prediction.
    </p>

    <h2>What Regression Measures</h2>

    <p>
      Regression models how an outcome variable changes as a predictor variable changes.
    </p>

    <p>
      Regression produces:
    </p>

    <ul class="bullets">

      <li>A fitted equation</li>

      <li>Predicted values</li>

      <li>Slope estimates</li>

      <li>Measures of uncertainty</li>

    </ul>

    <p>
      Regression focuses on modeling and prediction.
    </p>

    <h2>A Simple Comparison</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Question</th>
            <th>Correlation</th>
            <th>Regression</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Are variables related?</td>
            <td>Yes</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>How strong is the relationship?</td>
            <td>Yes</td>
            <td>Partially</td>
          </tr>

          <tr>
            <td>Can we predict outcomes?</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Provides an equation?</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Symmetry vs Direction</h2>

    <p>
      One of the most important differences involves symmetry.
    </p>

    <p>
      Correlation treats variables equally.
    </p>

    <div class="example-box">

      <p>
        Correlation(X,Y) = Correlation(Y,X)
      </p>
    </div>

    <p>
      Switching the variables does not change the correlation coefficient.
    </p>

    <p>
      Regression is different.
    </p>

    <p>
      Regression distinguishes between:
    </p>

    <ul class="bullets">

      <li>Predictor variable</li>

      <li>Outcome variable</li>

    </ul>

    <p>
      Reversing those roles generally changes the regression model.
    </p>

    <h2>Correlation Does Not Produce Predictions</h2>

    <p>
      Suppose study hours and exam scores have:
    </p>

    <div class="example-box">

      <p>
        r = 0.80
      </p>
    </div>

    <p>
      This tells us the relationship is strong and positive.
    </p>

    <p>
      However, it does not tell us:
    </p>

    <ul class="bullets">

      <li>Expected exam scores</li>

      <li>Predicted scores</li>

      <li>Rate of change</li>

    </ul>

    <p>
      Correlation alone cannot generate predictions.
    </p>

    <h2>Regression Produces Predictions</h2>

    <p>
      A regression model might produce:
    </p>

    <div class="example-box">

      <p>
        Exam Score = 50 + 4 × Study Hours
      </p>
    </div>

    <p>
      This equation allows predictions for new observations.
    </p>

    <p>
      Correlation cannot do this.
    </p>

    <h2>Units Matter in Regression</h2>

    <p>
      Regression slopes have units.
    </p>

    <p>
      Example:
    </p>

    <div class="example-box">

      <p>
        4 score points per study hour
      </p>
    </div>

    <p>
      Correlation coefficients have no units.
    </p>

    <p>
      They are standardized measures that always fall between −1 and 1.
    </p>

    <h2>The Range of Correlation</h2>

    <p>
      Correlation values always satisfy:
    </p>

    <div class="example-box">

      <p>
        −1 ≤ r ≤ 1
      </p>
    </div>

    <p>
      Regression slopes have no fixed range.
    </p>

    <p>
      Their values depend on measurement units and the scale of the variables.
    </p>

    <h2>Relationship to R-Squared</h2>

    <p>
      In simple linear regression, correlation and regression are mathematically connected.
    </p>

    <p>
      Specifically:
    </p>

    <div class="example-box">

      <p>
        R² = r²
      </p>
    </div>

    <p>
      This relationship explains why strong correlations often correspond to high R-squared values.
    </p>

    <h2>Correlation Does Not Imply Causation</h2>

    <p>
      A strong correlation does not prove that one variable causes another.
    </p>

    <p>
      The same warning applies to regression.
    </p>

    <div class="concept-box">

      <strong>Important reminder:</strong>

      <p>
        Neither correlation nor regression alone can establish causality.
      </p>

    </div>

    <h2>When Correlation Is Useful</h2>

    <p>
      Correlation is often useful when the goal is simply to assess association.
    </p>

    <p>
      Common uses include:
    </p>

    <ul class="bullets">

      <li>Exploratory analysis</li>

      <li>Variable screening</li>

      <li>Relationship assessment</li>

      <li>Data description</li>

    </ul>

    <h2>When Regression Is Useful</h2>

    <p>
      Regression is often useful when the goal is to:
    </p>

    <ul class="bullets">

      <li>Make predictions</li>

      <li>Estimate effects</li>

      <li>Model relationships</li>

      <li>Explain variation</li>

    </ul>

    <p>
      Regression provides substantially more information than a correlation coefficient alone.
    </p>

    <h2>A Practical Example</h2>

    <p>
      Imagine a company studying advertising and sales.
    </p>

    <p>
      Correlation answers:
    </p>

    <div class="example-box">

      <p>
        Are advertising spending and sales related?
      </p>
    </div>

    <p>
      Regression answers:
    </p>

    <div class="example-box">

      <p>
        How much are sales expected to increase for each additional dollar spent on advertising?
      </p>
    </div>

    <p>
      These are different but complementary questions.
    </p>

    <h2>Why Both Matter</h2>

    <p>
      Correlation and regression are not competitors.
    </p>

    <p>
      Instead, they provide different perspectives on relationships between variables.
    </p>

    <p>
      Correlation summarizes association.
    </p>

    <p>
      Regression builds a predictive and explanatory model.
    </p>

    <h2>Common Misconceptions</h2>

    <ul class="bullets">

      <li>A high correlation does not automatically imply accurate prediction</li>

      <li>A statistically significant regression does not prove causality</li>

      <li>Correlation is not a substitute for regression when prediction is needed</li>

      <li>Regression provides more information than correlation alone</li>

    </ul>

    <h2>The Bigger Picture</h2>

    <p>
      Correlation and regression both help us understand relationships among variables.
    </p>

    <p>
      Correlation summarizes the strength and direction of association.
    </p>

    <p>
      Regression goes further by describing the relationship mathematically and enabling prediction.
    </p>

    <p>
      Understanding the distinction is essential for selecting the right tool for a particular analytical goal.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Correlation measures the strength and direction of association between variables, while regression models how an outcome changes as a predictor changes and provides a framework for prediction and explanation.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      One of the most important uses of regression is prediction.
    </p>

    <p>
      Once a regression equation has been fitted, it can be used to estimate outcomes for new observations.
    </p>

    <p>
      The next lesson focuses on how regression models generate predictions and the limitations of those predictions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Correlation measures association, while regression models relationships</li>

        <li>Correlation is symmetric; regression is directional</li>

        <li>Correlation does not produce predictions</li>

        <li>Regression produces equations and predictions</li>

        <li>Correlation coefficients are unitless and range from −1 to 1</li>

        <li>Regression slopes depend on measurement units</li>

        <li>In simple linear regression, R² equals r²</li>

        <li>Neither correlation nor regression alone proves causation</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/r-squared/">
         ← Previous: R-Squared
      </a>

      <a class="btn"
         href="/modeling/simple-linear-regression/prediction/">
         Next: Prediction →
      </a>

    </div>

  </div>

</section>