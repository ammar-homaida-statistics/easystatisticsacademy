---
layout: default
title: Leverage
description: Learn what leverage means in regression diagnostics, how high-leverage observations arise, and why they can have a large impact on regression models.
permalink: /modeling/diagnostics/leverage/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_diagnostics_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/diagnostics/leverage/",
    label: "Leverage",
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
      <span class="badge">Leverage</span>
    </div>

    <h1>Leverage</h1>

    <p class="lead">
      Not all observations contribute equally to a regression model.
    </p>

    <p class="lead">
      Some observations have unusual predictor values that give them greater potential to affect the fitted regression equation. This property is known as leverage.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/diagnostics/outliers/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/influence/">
         Next: Influence →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is Leverage?</h2>

    <p>
      Leverage measures how unusual an observation's predictor values are compared with the rest of the dataset.
    </p>

    <p>
      Observations located far from the center of the predictor space have higher leverage.
    </p>

    <p>
      These observations possess greater potential to influence the fitted regression model.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Leverage reflects how far an observation's predictor values are from the average predictor values in the dataset.
      </p>

    </div>

    <h2>Why Leverage Matters</h2>

    <p>
      Regression lines are influenced by the locations of observations.
    </p>

    <p>
      Observations near the center of the predictor distribution usually have limited ability to pull the regression line.
    </p>

    <p>
      Observations far from the center often have much greater influence potential.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose most observations have predictor values between 20 and 40.
    </p>

    <p>
      One observation has a predictor value of 95.
    </p>

    <p>
      That observation lies far from the rest of the data and therefore has high leverage.
    </p>

    <h2>Leverage Depends on Predictors</h2>

    <p>
      Leverage is determined by predictor values rather than outcome values.
    </p>

    <p>
      Two observations may have identical outcomes but very different leverage if their predictor values differ substantially.
    </p>

    <p>
      This distinction is important when interpreting diagnostics.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Outliers in predictor variables create leverage. Outliers in outcome variables create large residuals.
      </p>

    </div>

    <h2>Leverage Is Not Necessarily Bad</h2>

    <p>
      High leverage is not automatically a problem.
    </p>

    <p>
      Many high-leverage observations are valid and informative.
    </p>

    <p>
      In fact, observations at the edges of the predictor range often provide valuable information about relationships.
    </p>

    <h2>Leverage and the Regression Line</h2>

    <p>
      Because high-leverage observations sit far from the center of the predictor space, they can exert a stronger pull on the fitted line.
    </p>

    <p>
      The model may shift noticeably if such observations are altered or removed.
    </p>

    <p>
      This is why analysts pay close attention to leverage diagnostics.
    </p>

    <h2>Visualizing Leverage</h2>

    <p>
      Imagine a scatterplot where nearly all observations cluster together.
    </p>

    <p>
      A single point appears far to the right along the horizontal axis.
    </p>

    <p>
      Even if its residual is small, that point has high leverage because of its unusual predictor value.
    </p>

    <h2>High Leverage with Small Residuals</h2>

    <p>
      A high-leverage observation may lie very close to the regression line.
    </p>

    <p>
      In such cases:
    </p>

    <ul class="bullets">

      <li>Residuals are small</li>

      <li>The observation fits the model well</li>

      <li>The observation may not be problematic</li>

    </ul>

    <p>
      High leverage alone does not imply model distortion.
    </p>

    <h2>High Leverage with Large Residuals</h2>

    <p>
      Greater concern arises when an observation combines:
    </p>

    <ul class="bullets">

      <li>High leverage</li>

      <li>Large residuals</li>

    </ul>

    <p>
      Such observations often have substantial influence on the fitted model.
    </p>

    <p>
      These cases deserve careful investigation.
    </p>

    <div class="concept-box">

      <strong>Important warning:</strong>

      <p>
        High leverage does not guarantee influence, but it creates the potential for influence.
      </p>

    </div>

    <h2>Leverage vs Residual Size</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Diagnostic Feature</th>
            <th>What It Measures</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Residual</td>
            <td>How poorly the observation is predicted</td>
          </tr>

          <tr>
            <td>Leverage</td>
            <td>How unusual the predictor values are</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      These diagnostics provide different information and should be interpreted together.
    </p>

    <h2>Leverage in Multiple Regression</h2>

    <p>
      In multiple regression, leverage depends on all predictors simultaneously.
    </p>

    <p>
      An observation may appear ordinary on each individual predictor but still occupy an unusual location when predictors are considered jointly.
    </p>

    <p>
      Multidimensional predictor space is therefore important.
    </p>

    <h2>The Hat Matrix</h2>

    <p>
      In regression theory, leverage values are derived from the hat matrix.
    </p>

    <p>
      The diagonal elements of this matrix quantify the leverage of individual observations.
    </p>

    <p>
      These values are often called hat values.
    </p>

    <h2>Leverage Values</h2>

    <p>
      Leverage values range between 0 and 1.
    </p>

    <p>
      Larger values indicate greater distance from the center of the predictor space.
    </p>

    <p>
      Analysts often compare leverage values relative to the average leverage in the dataset.
    </p>

    <h2>Identifying High-Leverage Observations</h2>

    <p>
      Statistical software commonly reports leverage values directly.
    </p>

    <p>
      Analysts often use:
    </p>

    <ul class="bullets">

      <li>Leverage plots</li>

      <li>Hat values</li>

      <li>Influence diagnostics</li>

    </ul>

    <p>
      These tools help identify observations that deserve closer inspection.
    </p>

    <h2>What To Do with High-Leverage Observations</h2>

    <p>
      High-leverage observations should not automatically be removed.
    </p>

    <p>
      Instead, analysts should investigate:
    </p>

    <ul class="bullets">

      <li>Data quality</li>

      <li>Measurement validity</li>

      <li>Population relevance</li>

      <li>Model sensitivity</li>

    </ul>

    <p>
      Careful evaluation is essential.
    </p>

    <h2>Leverage and Scientific Discovery</h2>

    <p>
      Some high-leverage observations represent rare but meaningful cases.
    </p>

    <p>
      They may reveal:
    </p>

    <ul class="bullets">

      <li>Previously unseen conditions</li>

      <li>Important subgroups</li>

      <li>Boundary behavior of a process</li>

      <li>New scientific insights</li>

    </ul>

    <p>
      These observations can be especially informative.
    </p>

    <h2>Leverage Is Only Part of the Story</h2>

    <p>
      High leverage alone does not determine whether an observation affects model results.
    </p>

    <p>
      To understand actual impact, analysts must examine influence diagnostics.
    </p>

    <p>
      Influence combines leverage with residual behavior.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Leverage helps identify observations with unusual predictor values and elevated potential to affect regression estimates.
    </p>

    <p>
      While high leverage is not inherently problematic, it highlights observations that deserve closer attention during model evaluation.
    </p>

    <p>
      Understanding leverage is an important step toward understanding influence.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Leverage measures how unusual an observation's predictor values are relative to the rest of the dataset. High-leverage observations have greater potential to affect regression results and should be examined carefully.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Leverage identifies observations that have the potential to affect a regression model.
    </p>

    <p>
      The next question is whether they actually do affect the model.
    </p>

    <p>
      The next lesson introduces influence and explains how analysts determine which observations genuinely alter regression conclusions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Leverage measures how unusual predictor values are</li>

        <li>Observations far from the predictor center have higher leverage</li>

        <li>Leverage depends on predictors, not outcomes</li>

        <li>High leverage creates the potential for influence</li>

        <li>High leverage alone is not necessarily problematic</li>

        <li>Leverage and residual size measure different aspects of an observation</li>

        <li>Hat values are common leverage diagnostics</li>

        <li>High-leverage observations deserve careful investigation but not automatic removal</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/diagnostics/outliers/">
         ← Previous: Outliers and Influential Observations
      </a>

      <a class="btn"
         href="/modeling/diagnostics/influence/">
         Next: Influence →
      </a>

    </div>

  </div>

</section>