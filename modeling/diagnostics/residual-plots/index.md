---
layout: default
title: Residual Plots
description: Learn how residual plots help diagnose regression models by revealing patterns, assumption violations, and opportunities for model improvement.
permalink: /modeling/diagnostics/residual-plots/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_diagnostics_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/diagnostics/residual-plots/",
    label: "Residual Plots",
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
      <span class="badge">Residual Analysis</span>
    </div>

    <h1>Residual Plots</h1>

    <p class="lead">
      Residuals contain valuable information about how well a regression model fits the data.
    </p>

    <p class="lead">
      Residual plots visualize those residuals and are among the most powerful diagnostic tools available to analysts.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/diagnostics/residuals/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/nonlinearity/">
         Next: Nonlinearity →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Residual Plot?</h2>

    <p>
      A residual plot is a graph that displays residuals against fitted values or predictor values.
    </p>

    <p>
      Instead of focusing on the regression line itself, the plot focuses on the model's prediction errors.
    </p>

    <p>
      This often reveals problems that are difficult to detect from coefficients alone.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Residual plots help analysts determine whether regression assumptions appear reasonable and whether the model adequately captures the structure of the data.
      </p>

    </div>

    <h2>Why Residual Plots Matter</h2>

    <p>
      A regression line may appear to fit the data well while still violating important assumptions.
    </p>

    <p>
      Residual plots help identify:
    </p>

    <ul class="bullets">

      <li>Nonlinearity</li>

      <li>Heteroscedasticity</li>

      <li>Outliers</li>

      <li>Influential observations</li>

      <li>Model misspecification</li>

    </ul>

    <p>
      For this reason, residual plots are a standard part of regression diagnostics.
    </p>

    <h2>The Most Common Residual Plot</h2>

    <p>
      The most frequently used diagnostic plot displays:
    </p>

    <ul class="bullets">

      <li>Horizontal axis: fitted values (ŷ)</li>

      <li>Vertical axis: residuals (e)</li>

    </ul>

    <p>
      This plot allows analysts to examine how prediction errors behave across the range of model predictions.
    </p>

    <h2>What a Good Residual Plot Looks Like</h2>

    <p>
      When assumptions are reasonably satisfied, residuals should appear:
    </p>

    <ul class="bullets">

      <li>Randomly scattered</li>

      <li>Centered around zero</li>

      <li>Roughly evenly spread</li>

      <li>Without visible patterns</li>

    </ul>

    <p>
      Random scatter suggests that the model has captured the major relationships in the data.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        The best residual plot often looks boring. Random scatter is usually a sign that the model is working appropriately.
      </p>

    </div>

    <h2>Visualizing an Ideal Residual Pattern</h2>

    <p>
      In an ideal residual plot:
    </p>

    <ul class="bullets">

      <li>Points appear above and below zero</li>

      <li>No systematic shape emerges</li>

      <li>Residual spread remains relatively constant</li>

    </ul>

    <p>
      Such a pattern supports key regression assumptions.
    </p>

    <h2>Example of Random Scatter</h2>

    

    <p>
      This type of pattern generally suggests that the model is capturing the relationship appropriately.
    </p>

    <h2>Looking for Patterns</h2>

    <p>
      Residual plots become useful when patterns appear.
    </p>

    <p>
      Visible structure often indicates that the model is missing something important.
    </p>

    <p>
      The goal is to identify these signals before drawing conclusions.
    </p>

    <h2>Curved Patterns</h2>

    <p>
      A curved pattern in residuals often suggests nonlinearity.
    </p>

    <p>
      This means the relationship between predictors and the outcome may not be adequately represented by a straight line.
    </p>

    <p>
      The model may be systematically underpredicting in some regions and overpredicting in others.
    </p>

    <h2>Funnel Patterns</h2>

    <p>
      A funnel-shaped residual plot often indicates heteroscedasticity.
    </p>

    <p>
      Residual variability changes across the range of fitted values.
    </p>

    <p>
      This violates the constant variance assumption.
    </p>

    <h2>Clusters</h2>

    <p>
      Residual plots sometimes reveal distinct clusters.
    </p>

    <p>
      Clustering may suggest:
    </p>

    <ul class="bullets">

      <li>Missing predictors</li>

      <li>Subgroups in the data</li>

      <li>Important categorical variables</li>

    </ul>

    <p>
      The model may not be accounting for meaningful differences among observations.
    </p>

    <h2>Outliers in Residual Plots</h2>

    <p>
      Points far from the bulk of residuals may be outliers.
    </p>

    <p>
      These observations often deserve additional investigation.
    </p>

    <p>
      Large residuals can indicate unusual observations or model weaknesses.
    </p>

    <h2>Residuals Around Zero</h2>

    <p>
      The horizontal line at zero plays an important role.
    </p>

    <p>
      Residuals should fluctuate around zero rather than remaining consistently positive or negative.
    </p>

    <p>
      Persistent deviation from zero may indicate systematic bias.
    </p>

    <h2>Residual Plots and Assumption Checking</h2>

    <p>
      Residual plots help assess several assumptions simultaneously:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Pattern</th>
            <th>Possible Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Random scatter</td>
            <td>Assumptions appear reasonable</td>
          </tr>

          <tr>
            <td>Curved pattern</td>
            <td>Nonlinearity</td>
          </tr>

          <tr>
            <td>Funnel shape</td>
            <td>Heteroscedasticity</td>
          </tr>

          <tr>
            <td>Large isolated points</td>
            <td>Outliers</td>
          </tr>

          <tr>
            <td>Clusters</td>
            <td>Missing structure in the model</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Residuals Versus Predictors</h2>

    <p>
      Analysts sometimes plot residuals against individual predictors instead of fitted values.
    </p>

    <p>
      This can reveal whether a particular predictor contributes to assumption violations or unexplained patterns.
    </p>

    <p>
      Different plots may reveal different problems.
    </p>

    <h2>Residual Plots and Model Improvement</h2>

    <p>
      Diagnostics are not merely about identifying problems.
    </p>

    <p>
      Residual plots often suggest ways to improve a model.
    </p>

    <p>
      Potential responses include:
    </p>

    <ul class="bullets">

      <li>Adding predictors</li>

      <li>Including interaction terms</li>

      <li>Applying transformations</li>

      <li>Using alternative models</li>

    </ul>

    <p>
      The plots help guide model refinement.
    </p>

    <h2>Residual Analysis Is an Ongoing Process</h2>

    <p>
      Analysts often fit a model, examine residual plots, revise the model, and then examine residuals again.
    </p>

    <p>
      This iterative process continues until the model adequately represents the data.
    </p>

    <p>
      Residual plots therefore play a central role throughout model development.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Residual plots transform prediction errors into diagnostic information that helps analysts evaluate and improve models.
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Residual plots are among the most valuable tools in regression analysis.
    </p>

    <p>
      They reveal patterns that numerical summaries often hide and provide direct evidence about whether assumptions appear reasonable.
    </p>

    <p>
      Learning to interpret residual plots is a fundamental skill for statistical modeling.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Residual plots visualize prediction errors and help analysts evaluate model assumptions, detect problems, and improve model quality. Random scatter generally supports model adequacy, while visible patterns often signal violations or missing structure.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      One of the most common patterns observed in residual plots is curvature.
    </p>

    <p>
      Curved residual patterns often indicate that a linear regression model is attempting to fit a relationship that is not truly linear.
    </p>

    <p>
      The next lesson focuses specifically on diagnosing nonlinearity and understanding its consequences for regression analysis.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Residual plots display prediction errors graphically</li>

        <li>Random scatter generally indicates a satisfactory model</li>

        <li>Curved patterns often suggest nonlinearity</li>

        <li>Funnel patterns often indicate heteroscedasticity</li>

        <li>Large isolated residuals may indicate outliers</li>

        <li>Clusters may reveal missing variables or subgroup structure</li>

        <li>Residual plots support assumption checking and model improvement</li>

        <li>Residual analysis is one of the most important parts of regression diagnostics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/diagnostics/residuals/">
         ← Previous: Residuals
      </a>

      <a class="btn"
         href="/modeling/diagnostics/nonlinearity/">
         Next: Nonlinearity →
      </a>

    </div>

  </div>

</section>