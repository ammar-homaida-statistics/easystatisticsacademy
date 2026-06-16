---
layout: default
title: Residuals
description: Learn what residuals are, how they measure prediction errors, and why they are essential for evaluating regression models.
permalink: /modeling/simple-linear-regression/residuals/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_simple_linear_regression_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/simple-linear-regression/residuals/",
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
      <span class="badge">Block 2</span>
      <span class="badge">Simple Linear Regression</span>
      <span class="badge">Residuals</span>
    </div>

    <h1>Residuals</h1>

    <p class="lead">
      No regression model predicts every observation perfectly.
    </p>

    <p class="lead">
      Residuals measure the difference between observed outcomes and the values predicted by the regression model, providing a direct way to assess model performance.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/simple-linear-regression/intercept/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/least-squares/">
         Next: Least Squares →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Residuals Matter</h2>

    <p>
      Regression models describe average relationships rather than perfectly fitting every observation.
    </p>

    <p>
      As a result, actual outcomes usually differ from predicted outcomes.
    </p>

    <p>
      Residuals quantify those differences.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        A residual is the difference between an observed value and the value predicted by a regression model.
      </p>

    </div>

    <h2>The Basic Definition</h2>

    <p>
      For every observation, we can compare:
    </p>

    <ul class="bullets">

      <li>The actual observed value</li>

      <li>The predicted value from the model</li>

    </ul>

    <p>
      The residual measures the gap between the two.
    </p>

    <div class="example-box">

      <p>
        Residual = Observed Value − Predicted Value
      </p>
    </div>

    <h2>Residual Notation</h2>

    <p>
      In regression, residuals are often represented by:
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

    <p>
      Each observation has its own residual.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose a regression model predicts an exam score of:
    </p>

    <div class="example-box">

      <p>
        ŷ = 82
      </p>
    </div>

    <p>
      The student's actual score is:
    </p>

    <div class="example-box">

      <p>
        y = 87
      </p>
    </div>

    <p>
      The residual is:
    </p>

    <div class="example-box">

      <p>
        e = 87 − 82 = 5
      </p>
    </div>

    <p>
      The model underpredicted the score by 5 points.
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
      This means the actual outcome was larger than expected.
    </p>

    <p>
      The model underestimated the observation.
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
      This means the actual outcome was smaller than expected.
    </p>

    <p>
      The model overestimated the observation.
    </p>

    <h2>Zero Residuals</h2>

    <p>
      A residual equal to zero means:
    </p>

    <div class="example-box">

      <p>
        Observed Value = Predicted Value
      </p>
    </div>

    <p>
      The model predicted that observation perfectly.
    </p>

    <p>
      Perfect residuals are uncommon in real-world datasets.
    </p>

    <h2>Residuals Represent Unexplained Variation</h2>

    <p>
      Recall the distinction between signal and noise.
    </p>

    <p>
      The regression line attempts to capture the signal.
    </p>

    <p>
      Residuals represent the remaining variation that the model does not explain.
    </p>

    <div class="concept-box">

      <strong>Key connection:</strong>

      <p>
        Residuals measure the noise left over after the model captures the signal.
      </p>

    </div>

    <h2>Visualizing Residuals</h2>

    <p>
      On a scatterplot with a regression line:
    </p>

    <ul class="bullets">

      <li>Each point has an observed value</li>

      <li>The line provides a predicted value</li>

      <li>The vertical distance between the point and the line is the residual</li>

    </ul>

    <p>
      Residuals can be viewed as prediction errors measured vertically from the line.
    </p>

    <h2>Large vs Small Residuals</h2>

    <p>
      Residual magnitude indicates prediction accuracy.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Residual Size</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Small</td>
            <td>Prediction is close to observation</td>
          </tr>

          <tr>
            <td>Large</td>
            <td>Prediction is far from observation</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Better-fitting models generally have smaller residuals.
    </p>

    <h2>Residuals and Model Quality</h2>

    <p>
      Residuals help answer questions such as:
    </p>

    <ul class="bullets">

      <li>How accurate are predictions?</li>

      <li>Are important patterns being missed?</li>

      <li>Is a linear model appropriate?</li>

      <li>Do unusual observations exist?</li>

    </ul>

    <p>
      Much of regression diagnostics relies on residual analysis.
    </p>

    <h2>Residual Patterns Matter</h2>

    <p>
      Ideally, residuals should appear random.
    </p>

    <p>
      Systematic patterns may indicate:
    </p>

    <ul class="bullets">

      <li>Missing variables</li>

      <li>Nonlinear relationships</li>

      <li>Model misspecification</li>

      <li>Violations of assumptions</li>

    </ul>

    <p>
      Residual plots are therefore powerful diagnostic tools.
    </p>

    <h2>Residuals and Prediction Error</h2>

    <p>
      Every residual is a prediction error for a particular observation.
    </p>

    <p>
      Collectively, residuals summarize how well the model performs across the entire dataset.
    </p>

    <p>
      Smaller residuals generally indicate better predictive performance.
    </p>

    <h2>Why Residuals Sum to Zero</h2>

    <p>
      In ordinary least squares regression with an intercept, positive and negative residuals balance each other.
    </p>

    <p>
      As a result:
    </p>

    <div class="example-box">

      <p>
        Sum of Residuals = 0
      </p>
    </div>

    <p>
      This property follows from the way the regression line is fitted.
    </p>

    <p>
      The next lesson explains exactly how that fitting process works.
    </p>

    <h2>Residuals vs Errors</h2>

    <p>
      Although the terms are sometimes used interchangeably, they are not identical.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Quantity</th>
            <th>Observed?</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Error</td>
            <td>Usually unobservable</td>
          </tr>

          <tr>
            <td>Residual</td>
            <td>Calculated from sample data</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Residuals are estimates of the underlying model errors.
    </p>

    <h2>Residuals and Learning</h2>

    <p>
      Many statistical and machine-learning methods improve models by analyzing residuals.
    </p>

    <p>
      If residuals contain patterns, the model may still have information left to learn.
    </p>

    <p>
      If residuals appear random, the model may already be capturing most of the available signal.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Residuals reveal what the regression model fails to explain.
    </p>

    <p>
      They quantify prediction errors, measure unexplained variation, and provide critical information for assessing model quality.
    </p>

    <p>
      Understanding residuals is essential because nearly every regression diagnostic is built around them.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Residuals are the differences between observed and predicted values. They measure prediction error, represent unexplained variation, and play a central role in evaluating regression models.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      If residuals measure prediction error, an obvious question arises:
    </p>

    <div class="example-box">

      <p>
        How is the regression line chosen in the first place?
      </p>
    </div>

    <p>
      The answer lies in the least-squares principle, the most common method for fitting regression models.
    </p>

    <p>
      The next lesson explains how least squares uses residuals to determine the best-fitting regression line.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A residual equals the observed value minus the predicted value</li>

        <li>Residuals measure prediction error for individual observations</li>

        <li>Positive residuals indicate underprediction</li>

        <li>Negative residuals indicate overprediction</li>

        <li>Zero residuals indicate perfect predictions</li>

        <li>Residuals represent unexplained variation in the data</li>

        <li>Residual patterns help diagnose model problems</li>

        <li>Residuals are central to evaluating regression performance</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/intercept/">
         ← Previous: Intercept
      </a>

      <a class="btn"
         href="/modeling/simple-linear-regression/least-squares/">
         Next: Least Squares →
      </a>

    </div>

  </div>

</section>