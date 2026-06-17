---
layout: default
title: Model Comparison
description: Learn how analysts compare competing models, evaluate trade-offs between fit and complexity, and select models appropriate for their goals.
permalink: /modeling/model-fit-comparison/model-comparison/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_model_fit_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/model-fit-comparison/model-comparison/",
    label: "Model Comparison",
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
      <span class="badge">Model Selection</span>
    </div>

    <h1>Model Comparison</h1>

    <p class="lead">
      Statistical analysis rarely involves only one possible model.
    </p>

    <p class="lead">
      Analysts often build multiple candidate models and then compare them to determine which provides the best balance of fit, simplicity, interpretability, and predictive performance.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/model-fit-comparison/train-vs-test/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/aic-bic/">
         Next: AIC & BIC →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Compare Models?</h2>

    <p>
      Many different models can often be fitted to the same dataset.
    </p>

    <p>
      For example, analysts may consider:
    </p>

    <ul class="bullets">

      <li>Different predictor sets</li>

      <li>Different interaction terms</li>

      <li>Different functional forms</li>

      <li>Different levels of complexity</li>

    </ul>

    <p>
      Model comparison helps determine which alternative best serves the analytical objective.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Model comparison evaluates competing models to identify the one that provides the most useful balance between fit, complexity, and practical value.
      </p>

    </div>

    <h2>There Is Rarely One Perfect Model</h2>

    <p>
      Real-world data often support multiple plausible models.
    </p>

    <p>
      Different models may emphasize different goals:
    </p>

    <ul class="bullets">

      <li>Prediction accuracy</li>

      <li>Interpretability</li>

      <li>Scientific explanation</li>

      <li>Computational simplicity</li>

    </ul>

    <p>
      The best model depends partly on the purpose of the analysis.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose analysts want to predict house prices.
    </p>

    <p>
      They may compare:
    </p>

    <ul class="bullets">

      <li>A model using only house size</li>

      <li>A model using size and location</li>

      <li>A model using size, location, age, and neighborhood characteristics</li>

    </ul>

    <p>
      Each model may perform differently and involve different trade-offs.
    </p>

    <h2>What Makes a Model Better?</h2>

    <p>
      A better model is not necessarily the one with the highest fit statistic.
    </p>

    <p>
      Analysts often consider:
    </p>

    <ul class="bullets">

      <li>Model fit</li>

      <li>Predictive performance</li>

      <li>Complexity</li>

      <li>Interpretability</li>

      <li>Robustness</li>

    </ul>

    <p>
      Multiple criteria usually contribute to model selection.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        The goal is not simply to maximize fit. The goal is to find a model that is useful, reliable, and appropriate for the task.
      </p>

    </div>

    <h2>Comparing R-Squared Values</h2>

    <p>
      One common approach is comparing R-squared values.
    </p>

    <p>
      Models with larger R-squared values explain more variation in the outcome.
    </p>

    <p>
      However, R-squared alone can favor unnecessarily complex models.
    </p>

    <h2>The Complexity Problem</h2>

    <p>
      Adding predictors almost always increases R-squared.
    </p>

    <p>
      As a result, models with many variables often appear superior even when additional predictors provide little practical value.
    </p>

    <p>
      This is one reason why adjusted R-squared and other comparison tools are important.
    </p>

    <h2>Prediction-Focused Comparison</h2>

    <p>
      When prediction is the primary goal, analysts often compare:
    </p>

    <ul class="bullets">

      <li>Test-set performance</li>

      <li>Cross-validation results</li>

      <li>Prediction errors</li>

    </ul>

    <p>
      These measures evaluate how well models generalize to new data.
    </p>

    <h2>Interpretability Matters</h2>

    <p>
      Sometimes a simpler model is preferred even if a more complex model performs slightly better.
    </p>

    <p>
      Simpler models are often:
    </p>

    <ul class="bullets">

      <li>Easier to explain</li>

      <li>Easier to communicate</li>

      <li>Easier to implement</li>

      <li>More transparent</li>

    </ul>

    <p>
      Practical considerations frequently influence model choice.
    </p>

    <h2>The Principle of Parsimony</h2>

    <p>
      Parsimony favors simpler explanations when multiple models perform similarly.
    </p>

    <p>
      This idea is often summarized by:
    </p>

    <div class="example-box">

      <p>
        Prefer the simplest model that adequately explains the data.
      </p>
    </div>

    <p>
      Parsimony helps reduce unnecessary complexity and overfitting.
    </p>

    <h2>Nested Model Comparison</h2>

    <p>
      Sometimes one model is a special case of another.
    </p>

    <p>
      These are called nested models.
    </p>

    <p>
      Analysts may formally test whether additional predictors significantly improve fit.
    </p>

    <h2>Comparing Several Candidate Models</h2>

    <p>
      Consider three competing models:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Model</th>
            <th>Predictors</th>
            <th>Adjusted R²</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>A</td>
            <td>2</td>
            <td>0.62</td>
          </tr>

          <tr>
            <td>B</td>
            <td>5</td>
            <td>0.71</td>
          </tr>

          <tr>
            <td>C</td>
            <td>12</td>
            <td>0.72</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Although Model C performs slightly better, analysts may prefer Model B because it achieves nearly the same fit with substantially less complexity.
    </p>

    <h2>Comparing Performance Metrics</h2>

    <p>
      Depending on the objective, analysts may compare:
    </p>

    <ul class="bullets">

      <li>R-squared</li>

      <li>Adjusted R-squared</li>

      <li>RMSE</li>

      <li>MAE</li>

      <li>Cross-validation error</li>

      <li>Information criteria</li>

    </ul>

    <p>
      Different metrics emphasize different aspects of performance.
    </p>

    <h2>No Single Metric Is Sufficient</h2>

    <p>
      Every comparison metric has strengths and limitations.
    </p>

    <p>
      A model may rank highly on one measure and less favorably on another.
    </p>

    <p>
      Effective model comparison typically uses multiple perspectives.
    </p>

    <div class="concept-box">

      <strong>Important warning:</strong>

      <p>
        Selecting a model based on a single statistic can be misleading. Multiple evaluation criteria should be considered whenever possible.
      </p>

    </div>

    <h2>Model Comparison and Overfitting</h2>

    <p>
      Comparison tools help protect against overfitting.
    </p>

    <p>
      Rather than automatically rewarding increasingly complex models, analysts evaluate whether additional complexity produces meaningful improvement.
    </p>

    <p>
      This encourages better generalization.
    </p>

    <h2>Model Selection Is Goal Dependent</h2>

    <p>
      Different goals may produce different model choices.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Goal</th>
            <th>Common Priority</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Prediction</td>
            <td>Future accuracy</td>
          </tr>

          <tr>
            <td>Explanation</td>
            <td>Interpretability</td>
          </tr>

          <tr>
            <td>Scientific research</td>
            <td>Theoretical relevance</td>
          </tr>

          <tr>
            <td>Operations</td>
            <td>Simplicity and reliability</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The best model depends on the problem being solved.
    </p>

    <h2>Model Comparison Is an Ongoing Process</h2>

    <p>
      Analysts often compare several alternatives before settling on a final model.
    </p>

    <p>
      New predictors, new data, or new objectives may motivate additional comparisons later.
    </p>

    <p>
      Model selection is rarely a one-time decision.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical modeling involves choices.
    </p>

    <p>
      Because multiple reasonable models often exist, analysts must compare alternatives systematically.
    </p>

    <p>
      Model comparison provides a framework for balancing fit, complexity, interpretability, and predictive performance in order to select models that are both useful and reliable.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Model comparison helps analysts choose among competing models by evaluating trade-offs between fit, complexity, interpretability, and predictive performance. The best model is usually the one that best serves the goals of the analysis rather than the one that simply fits the data most closely.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      One important family of model comparison tools explicitly balances fit against complexity.
    </p>

    <p>
      Two of the most widely used measures are the Akaike Information Criterion (AIC) and the Bayesian Information Criterion (BIC).
    </p>

    <p>
      The next lesson introduces AIC and BIC and explains how they help analysts compare competing statistical models while discouraging unnecessary complexity.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Model comparison evaluates competing models rather than focusing on a single model</li>

        <li>Good model selection balances fit, complexity, and practical usefulness</li>

        <li>Higher fit does not automatically imply a better model</li>

        <li>Prediction-focused comparisons often emphasize test performance</li>

        <li>Interpretability and simplicity are important considerations</li>

        <li>Parsimony favors simpler models when performance is similar</li>

        <li>Multiple evaluation metrics should be considered together</li>

        <li>Model choice depends on the goals of the analysis</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/train-vs-test/">
         ← Previous: Train vs Test Performance
      </a>

      <a class="btn"
         href="/modeling/model-fit-comparison/aic-bic/">
         Next: AIC & BIC →
      </a>

    </div>

  </div>

</section>