---
layout: default
title: Train vs Test Performance
description: Learn why analysts evaluate models on both training and test data, how train-test comparisons reveal overfitting, and why generalization is the ultimate goal of modeling.
permalink: /modeling/model-fit-comparison/train-vs-test/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_model_fit_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/model-fit-comparison/train-vs-test/",
    label: "Train vs Test Performance",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 6</span>
      <span class="badge">Model Fit & Comparison</span>
      <span class="badge">Generalization</span>
    </div>

    <h1>Train vs Test Performance</h1>

    <p class="lead">
      A model's performance on the data used to build it is only part of the story.
    </p>

    <p class="lead">
      The real challenge is determining whether the model performs well on new observations that it has never seen before.
    </p>

    <p class="lead">
      Comparing training and test performance is one of the most important tools for evaluating model quality.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/model-fit-comparison/underfitting/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/model-comparison/">
         Next: Model Comparison →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Training Performance Is Not Enough</h2>

    <p>
      Every model is designed using a particular dataset.
    </p>

    <p>
      Because the model has already seen those observations, strong performance on that dataset is not surprising.
    </p>

    <p>
      The more important question is whether the model can make accurate predictions for future observations.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Good models do not simply fit existing data—they generalize to new data.
      </p>

    </div>

    <h2>Training Data</h2>

    <p>
      Training data are the observations used to estimate model parameters.
    </p>

    <p>
      During training, the model learns relationships between predictors and outcomes.
    </p>

    <p>
      Model coefficients are calculated from these observations.
    </p>

    <h2>Test Data</h2>

    <p>
      Test data consist of observations that are not used during model fitting.
    </p>

    <p>
      After the model has been trained, analysts evaluate performance on this separate dataset.
    </p>

    <p>
      This provides a more realistic estimate of future performance.
    </p>

    <h2>The Core Idea</h2>

    <p>
      The model learns from one dataset and is evaluated on another.
    </p>

    <p>
      If performance remains strong on both datasets, the model is more likely to have learned meaningful patterns.
    </p>

    <p>
      If performance drops substantially, overfitting may be present.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Test performance is usually a better indicator of future usefulness than training performance.
      </p>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Suppose a dataset contains 1,000 observations.
    </p>

    <p>
      An analyst may:
    </p>

    <ul class="bullets">

      <li>Use 800 observations for training</li>

      <li>Reserve 200 observations for testing</li>

    </ul>

    <p>
      The model is fitted using the training set and evaluated using the test set.
    </p>

    <h2>Why Separate Data Matter</h2>

    <p>
      Evaluating performance on training data can create an overly optimistic impression.
    </p>

    <p>
      The model has already adapted to those observations.
    </p>

    <p>
      Test data provide a more independent evaluation.
    </p>

    <h2>Overfitting Revealed</h2>

    <p>
      Train-test comparisons are especially useful for detecting overfitting.
    </p>

    <p>
      Overfitted models often show:
    </p>

    <ul class="bullets">

      <li>Excellent training performance</li>

      <li>Much worse test performance</li>

    </ul>

    <p>
      The gap between the two provides evidence that the model has learned noise rather than signal.
    </p>

    <h2>Underfitting Revealed</h2>

    <p>
      Underfitted models often perform poorly on both training and test data.
    </p>

    <p>
      Because the model is too simple, it cannot capture important relationships even in the training dataset.
    </p>

    <p>
      Test performance is similarly weak.
    </p>

    <h2>Three Common Scenarios</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Training Performance</th>
            <th>Test Performance</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>High</td>
            <td>High</td>
            <td>Good generalization</td>
          </tr>

          <tr>
            <td>High</td>
            <td>Low</td>
            <td>Overfitting</td>
          </tr>

          <tr>
            <td>Low</td>
            <td>Low</td>
            <td>Underfitting</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Visualizing the Idea</h2>

    

    <p>
      The healthiest models typically show strong and relatively similar performance on both datasets.
    </p>

    <h2>Generalization Error</h2>

    <p>
      The difference between training and test performance is often called the generalization gap.
    </p>

    <p>
      Small gaps suggest that learned patterns extend beyond the training data.
    </p>

    <p>
      Large gaps suggest that the model may not generalize well.
    </p>

    <h2>Choosing Performance Metrics</h2>

    <p>
      Train and test performance can be evaluated using many measures.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>R-squared</li>

      <li>Mean squared error (MSE)</li>

      <li>Root mean squared error (RMSE)</li>

      <li>Mean absolute error (MAE)</li>

    </ul>

    <p>
      The choice depends on the modeling goal.
    </p>

    <h2>Train-Test Splits</h2>

    <p>
      Different splitting strategies exist.
    </p>

    <p>
      Common examples include:
    </p>

    <ul class="bullets">

      <li>80/20 split</li>

      <li>70/30 split</li>

      <li>75/25 split</li>

    </ul>

    <p>
      The optimal choice depends on sample size and application.
    </p>

    <h2>Limitations of a Single Split</h2>

    <p>
      Results can depend on which observations happen to fall into the training and test sets.
    </p>

    <p>
      A fortunate or unfortunate split may distort performance estimates.
    </p>

    <p>
      This motivates more advanced approaches such as cross-validation.
    </p>

    <h2>Cross-Validation</h2>

    <p>
      Cross-validation repeatedly creates different training and validation subsets.
    </p>

    <p>
      Performance is averaged across many evaluations.
    </p>

    <p>
      This often provides a more stable estimate of generalization ability than a single train-test split.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        A model should be judged by how well it predicts data it has not seen, not merely by how well it explains data it already knows.
      </p>

    </div>

    <h2>Why This Matters in Practice</h2>

    <p>
      Many real-world applications depend on future performance:
    </p>

    <ul class="bullets">

      <li>Business forecasting</li>

      <li>Medical prediction models</li>

      <li>Risk assessment</li>

      <li>Machine learning systems</li>

    </ul>

    <p>
      Strong training performance alone provides little value if future predictions are inaccurate.
    </p>

    <h2>Train vs Test and Model Selection</h2>

    <p>
      When comparing multiple models, analysts often prioritize models with stronger test performance rather than models with the highest training performance.
    </p>

    <p>
      This encourages models that generalize effectively.
    </p>

    <p>
      Predictive reliability becomes the central criterion.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical modeling is fundamentally about learning relationships that extend beyond the current dataset.
    </p>

    <p>
      Comparing training and test performance helps determine whether a model has learned meaningful structure or simply adapted to a particular sample.
    </p>

    <p>
      This makes train-test evaluation one of the most important tools for assessing model quality.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Training performance shows how well a model fits known data, while test performance shows how well it generalizes to new data. Strong models perform well on both.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Analysts rarely evaluate just one model.
    </p>

    <p>
      In practice, multiple candidate models are often compared to determine which best balances fit, complexity, interpretability, and predictive performance.
    </p>

    <p>
      The next lesson introduces model comparison and explores how analysts choose among competing statistical models.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Training data are used to fit models, while test data are used to evaluate them</li>

        <li>Test performance is usually a better indicator of future usefulness than training performance</li>

        <li>Overfitting often appears as high training performance and lower test performance</li>

        <li>Underfitting often produces poor performance on both datasets</li>

        <li>The generalization gap reflects differences between training and test performance</li>

        <li>Cross-validation provides a more stable estimate of predictive performance</li>

        <li>Model quality depends on generalization, not just fit to existing data</li>

        <li>Train-test comparisons are central to modern model evaluation</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/underfitting/">
         ← Previous: Underfitting
      </a>

      <a class="btn"
         href="/modeling/model-fit-comparison/model-comparison/">
         Next: Model Comparison →
      </a>

    </div>

  </div>

</section>