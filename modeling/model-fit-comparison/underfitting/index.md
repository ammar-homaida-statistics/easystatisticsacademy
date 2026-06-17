---
layout: default
title: Underfitting
description: Learn what underfitting is, why overly simple models can fail to capture important patterns, and how underfitting differs from overfitting.
permalink: /modeling/model-fit-comparison/underfitting/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_model_fit_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/model-fit-comparison/underfitting/",
    label: "Underfitting",
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
      <span class="badge">Underfitting</span>
    </div>

    <h1>Underfitting</h1>

    <p class="lead">
      While overfitting occurs when a model is too complex, the opposite problem occurs when a model is too simple.
    </p>

    <p class="lead">
      Underfitting happens when a model fails to capture important patterns in the data, leading to poor performance even on the data used to fit the model.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/model-fit-comparison/overfitting/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/train-vs-test/">
         Next: Train vs Test Performance →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is Underfitting?</h2>

    <p>
      Underfitting occurs when a model is too simple to adequately represent the relationships present in the data.
    </p>

    <p>
      Important patterns remain unexplained because the model lacks sufficient flexibility.
    </p>

    <p>
      As a result, predictions are often poor and substantial variation remains unexplained.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Underfitting happens when a model is not complex enough to capture meaningful structure in the data.
      </p>

    </div>

    <h2>Why Underfitting Matters</h2>

    <p>
      Statistical models are intended to represent important relationships.
    </p>

    <p>
      If a model is too simplistic, it may ignore valuable information and produce inaccurate conclusions.
    </p>

    <p>
      Underfitting can therefore limit both explanation and prediction.
    </p>

    <h2>An Everyday Analogy</h2>

    <p>
      Imagine trying to describe an entire city using only one sentence.
    </p>

    <p>
      The description may be simple, but it would fail to capture most important details.
    </p>

    <p>
      Underfitted models behave similarly by oversimplifying reality.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Underfitting occurs when simplicity becomes so extreme that important patterns are lost.
      </p>

    </div>

    <h2>How Underfitting Happens</h2>

    <p>
      Several situations can produce underfitting:
    </p>

    <ul class="bullets">

      <li>Too few predictors</li>

      <li>Ignoring important variables</li>

      <li>Using an overly restrictive model form</li>

      <li>Failing to account for nonlinear relationships</li>

      <li>Oversimplifying a complex process</li>

    </ul>

    <p>
      In each case, the model lacks the flexibility needed to represent the data adequately.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose the true relationship between study hours and exam scores exhibits a curved pattern.
    </p>

    <p>
      A model that forces a straight-line relationship may miss important features of the data.
    </p>

    <p>
      The resulting predictions may be systematically inaccurate.
    </p>

    <h2>Underfitting and Residuals</h2>

    <p>
      Underfitted models often leave large residuals because substantial information remains unexplained.
    </p>

    <p>
      Residual plots may reveal clear patterns that indicate the model is missing important structure.
    </p>

    <p>
      These patterns are often visible even on the training data.
    </p>

    <h2>Training Performance Is Poor</h2>

    <p>
      One of the defining features of underfitting is weak performance on the training data itself.
    </p>

    <p>
      Unlike overfitting, which often excels on training data, underfitting struggles even before new data are considered.
    </p>

    <p>
      This makes underfitting easier to detect.
    </p>

    <div class="concept-box">

      <strong>Important warning:</strong>

      <p>
        If a model performs poorly on the data used to fit it, it is unlikely to perform well on new data.
      </p>

    </div>

    <h2>Underfitting and R-Squared</h2>

    <p>
      Underfitted models often produce relatively low R-squared values because much of the outcome variation remains unexplained.
    </p>

    <p>
      The model simply fails to capture important predictive information.
    </p>

    <p>
      However, R-squared alone is not sufficient to diagnose underfitting.
    </p>

    <h2>Signs of Underfitting</h2>

    <p>
      Common indicators include:
    </p>

    <ul class="bullets">

      <li>Poor training performance</li>

      <li>Large residuals</li>

      <li>Low explanatory power</li>

      <li>Visible patterns in residual plots</li>

      <li>Consistently inaccurate predictions</li>

    </ul>

    <p>
      These symptoms suggest that the model is too simple.
    </p>

    <h2>Underfitting vs Overfitting</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Feature</th>
            <th>Underfitting</th>
            <th>Overfitting</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Model complexity</td>
            <td>Too low</td>
            <td>Too high</td>
          </tr>

          <tr>
            <td>Training performance</td>
            <td>Poor</td>
            <td>Excellent</td>
          </tr>

          <tr>
            <td>Generalization</td>
            <td>Poor</td>
            <td>Poor</td>
          </tr>

          <tr>
            <td>Main problem</td>
            <td>Misses signal</td>
            <td>Learns noise</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bias–Variance Perspective</h2>

    <p>
      Underfitting is often associated with high bias.
    </p>

    <p>
      The model makes overly strong simplifying assumptions that prevent it from capturing important relationships.
    </p>

    <p>
      Overfitting, by contrast, is often associated with high variance.
    </p>

    <h2>How Analysts Respond</h2>

    <p>
      When underfitting is detected, analysts often increase model flexibility.
    </p>

    <p>
      Possible strategies include:
    </p>

    <ul class="bullets">

      <li>Adding relevant predictors</li>

      <li>Including interaction terms</li>

      <li>Adding polynomial terms</li>

      <li>Using more flexible models</li>

      <li>Improving feature selection</li>

    </ul>

    <p>
      The goal is to better capture meaningful patterns in the data.
    </p>

    <h2>Balancing Simplicity and Complexity</h2>

    <p>
      Good modeling involves finding a balance.
    </p>

    <p>
      Models should be:
    </p>

    <ul class="bullets">

      <li>Complex enough to capture important patterns</li>

      <li>Simple enough to generalize well</li>

    </ul>

    <p>
      Both extremes create problems.
    </p>

    <h2>The Model Complexity Curve</h2>

    <p>
      As model complexity increases:
    </p>

    <ul class="bullets">

      <li>Underfitting decreases</li>

      <li>Fit improves initially</li>

      <li>Overfitting eventually becomes a risk</li>

    </ul>

    <p>
      The best models typically occupy a middle ground between these extremes.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        The goal of model building is not maximum simplicity or maximum complexity. It is finding the level of complexity that captures signal without memorizing noise.
      </p>

    </div>

    <h2>Why Underfitting Is Sometimes Overlooked</h2>

    <p>
      Discussions of model quality often focus heavily on overfitting.
    </p>

    <p>
      However, underfitting can be equally harmful because it prevents models from learning meaningful relationships in the first place.
    </p>

    <p>
      Effective model evaluation must consider both risks.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Underfitting represents one side of the model complexity trade-off.
    </p>

    <p>
      When a model is too simple, it fails to capture important patterns and performs poorly even on training data.
    </p>

    <p>
      Understanding underfitting helps analysts build models that are flexible enough to learn meaningful relationships while still maintaining strong generalization.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Underfitting occurs when a model is too simple to capture important structure in the data. Such models often perform poorly on both training and future data because they miss meaningful patterns.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Overfitting and underfitting are often revealed by comparing performance on different datasets.
    </p>

    <p>
      Analysts commonly compare training performance with performance on unseen test data to evaluate generalization.
    </p>

    <p>
      The next lesson introduces train-versus-test performance and explains how this comparison helps identify whether a model is learning meaningful patterns or merely adapting to a specific dataset.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Underfitting occurs when a model is too simple to capture important patterns</li>

        <li>Underfitted models often perform poorly even on training data</li>

        <li>Large residuals and visible residual patterns are common warning signs</li>

        <li>Missing predictors and restrictive model forms can cause underfitting</li>

        <li>Underfitting is often associated with high bias</li>

        <li>Both underfitting and overfitting reduce model usefulness</li>

        <li>Model complexity should balance flexibility and generalization</li>

        <li>Effective models avoid both extremes of the complexity spectrum</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/overfitting/">
         ← Previous: Overfitting
      </a>

      <a class="btn"
         href="/modeling/model-fit-comparison/train-vs-test/">
         Next: Train vs Test Performance →
      </a>

    </div>

  </div>

</section>