---
layout: default
title: Diagnostic Workflow
description: Learn a systematic workflow for evaluating regression models using residual analysis, assumption checks, influence diagnostics, and model refinement.
permalink: /modeling/diagnostics/diagnostic-workflow/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_diagnostics_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/diagnostics/diagnostic-workflow/",
    label: "Diagnostic Workflow",
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
      <span class="badge">Workflow</span>
    </div>

    <h1>Diagnostic Workflow</h1>

    <p class="lead">
      Individual diagnostic tools are useful, but effective model evaluation requires a systematic process.
    </p>

    <p class="lead">
      Rather than checking diagnostics randomly, analysts typically follow a structured workflow that helps identify model weaknesses, evaluate assumptions, and improve model quality.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/diagnostics/cooks-distance/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/">
         Continue to Model Fit & Comparison →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Use a Diagnostic Workflow?</h2>

    <p>
      Regression diagnostics generate a large amount of information.
    </p>

    <p>
      Without a systematic approach, it is easy to overlook important issues or focus on less important problems.
    </p>

    <p>
      A structured workflow helps ensure that model evaluation is comprehensive and consistent.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        A diagnostic workflow provides a step-by-step process for evaluating model assumptions, identifying problems, and improving regression models.
      </p>

    </div>

    <h2>Diagnostics Are About Understanding Models</h2>

    <p>
      The purpose of diagnostics is not to prove that a model is perfect.
    </p>

    <p>
      Instead, diagnostics help analysts understand:
    </p>

    <ul class="bullets">

      <li>How well the model fits the data</li>

      <li>Whether assumptions appear reasonable</li>

      <li>Where the model performs poorly</li>

      <li>How conclusions might be affected by model limitations</li>

    </ul>

    <p>
      Diagnostic evaluation is therefore a key part of responsible modeling.
    </p>

    <h2>Step 1: Examine Overall Fit</h2>

    <p>
      Diagnostic analysis often begins with basic model summaries.
    </p>

    <p>
      Analysts review:
    </p>

    <ul class="bullets">

      <li>Regression coefficients</li>

      <li>R-squared values</li>

      <li>Adjusted R-squared values</li>

      <li>Overall significance tests</li>

    </ul>

    <p>
      These measures provide an initial understanding of model performance.
    </p>

    <h2>Step 2: Inspect Residuals</h2>

    <p>
      Residuals are the foundation of regression diagnostics.
    </p>

    <p>
      Analysts examine:
    </p>

    <ul class="bullets">

      <li>Residual values</li>

      <li>Residual distributions</li>

      <li>Residual plots</li>

    </ul>

    <p>
      Residual behavior often reveals issues that are not visible from model summaries alone.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Coefficients describe the model. Residuals reveal how well the model actually works.
      </p>

    </div>

    <h2>Step 3: Check Linearity</h2>

    <p>
      Analysts evaluate whether predictor relationships appear reasonably linear.
    </p>

    <p>
      Important tools include:
    </p>

    <ul class="bullets">

      <li>Residual versus fitted plots</li>

      <li>Scatterplots</li>

      <li>Partial residual plots</li>

    </ul>

    <p>
      Curved residual patterns often indicate nonlinearity.
    </p>

    <h2>Step 4: Check Variance Patterns</h2>

    <p>
      Next, analysts evaluate homoscedasticity.
    </p>

    <p>
      The goal is to determine whether residual spread remains approximately constant across fitted values.
    </p>

    <p>
      Funnel-shaped residual plots often indicate heteroscedasticity.
    </p>

    <h2>Step 5: Evaluate Normality</h2>

    <p>
      Normality diagnostics help assess whether residual distributions are approximately normal.
    </p>

    <p>
      Common tools include:
    </p>

    <ul class="bullets">

      <li>Histograms</li>

      <li>Q-Q plots</li>

      <li>Normality tests</li>

    </ul>

    <p>
      These diagnostics are especially relevant when inference is important.
    </p>

    <h2>Step 6: Search for Outliers</h2>

    <p>
      Analysts investigate observations with unusually large residuals.
    </p>

    <p>
      Questions include:
    </p>

    <ul class="bullets">

      <li>Are the observations valid?</li>

      <li>Were there measurement errors?</li>

      <li>Do they reveal missing structure?</li>

    </ul>

    <p>
      Outlier investigation helps determine whether unusual observations affect conclusions.
    </p>

    <h2>Step 7: Examine Leverage</h2>

    <p>
      High-leverage observations occupy unusual locations in the predictor space.
    </p>

    <p>
      Analysts identify these observations because they possess elevated potential to influence the model.
    </p>

    <p>
      Leverage diagnostics help highlight observations that deserve closer inspection.
    </p>

    <h2>Step 8: Evaluate Influence</h2>

    <p>
      Influence diagnostics determine whether observations actually change the model.
    </p>

    <p>
      Common tools include:
    </p>

    <ul class="bullets">

      <li>Cook's Distance</li>

      <li>DFFITS</li>

      <li>DFBETAs</li>

    </ul>

    <p>
      These measures identify observations that substantially affect results.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        High leverage creates the potential for influence, but influence diagnostics reveal whether the model is truly sensitive to specific observations.
      </p>

    </div>

    <h2>Step 9: Assess Practical Consequences</h2>

    <p>
      Finding a diagnostic issue does not automatically invalidate a model.
    </p>

    <p>
      Analysts evaluate:
    </p>

    <ul class="bullets">

      <li>The severity of the issue</li>

      <li>The sample size</li>

      <li>The purpose of the analysis</li>

      <li>The robustness of conclusions</li>

    </ul>

    <p>
      Practical importance is often more relevant than perfect assumptions.
    </p>

    <h2>Step 10: Revise the Model If Necessary</h2>

    <p>
      Diagnostics often suggest improvements.
    </p>

    <p>
      Potential modifications include:
    </p>

    <ul class="bullets">

      <li>Adding predictors</li>

      <li>Transforming variables</li>

      <li>Including interaction terms</li>

      <li>Adding polynomial terms</li>

      <li>Using robust methods</li>

    </ul>

    <p>
      Diagnostics therefore support model development rather than merely model criticism.
    </p>

    <h2>The Workflow Is Iterative</h2>

    <p>
      Model building rarely ends after one diagnostic review.
    </p>

    <p>
      Analysts often:
    </p>

    <ol>

      <li>Fit a model.</li>

      <li>Evaluate diagnostics.</li>

      <li>Modify the model.</li>

      <li>Recheck diagnostics.</li>

      <li>Repeat as needed.</li>

    </ol>

    <p>
      This iterative process helps improve model quality over time.
    </p>

    <h2>A Practical Checklist</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Diagnostic Area</th>
            <th>Main Question</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Model Fit</td>
            <td>Does the model explain meaningful variation?</td>
          </tr>

          <tr>
            <td>Linearity</td>
            <td>Are relationships approximately linear?</td>
          </tr>

          <tr>
            <td>Variance</td>
            <td>Is residual spread roughly constant?</td>
          </tr>

          <tr>
            <td>Normality</td>
            <td>Are residuals approximately normal?</td>
          </tr>

          <tr>
            <td>Outliers</td>
            <td>Are unusual observations present?</td>
          </tr>

          <tr>
            <td>Leverage</td>
            <td>Are predictor values unusually extreme?</td>
          </tr>

          <tr>
            <td>Influence</td>
            <td>Do individual observations drive results?</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Diagnostics Support Better Decisions</h2>

    <p>
      Diagnostics are not simply technical exercises.
    </p>

    <p>
      They help analysts determine whether conclusions are trustworthy.
    </p>

    <p>
      Understanding model weaknesses often improves decision-making more than focusing exclusively on model strengths.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Regression diagnostics bring together many tools that evaluate model quality from different perspectives.
    </p>

    <p>
      A systematic workflow ensures that important assumptions, influential observations, and model limitations receive appropriate attention.
    </p>

    <p>
      By following a structured diagnostic process, analysts can develop models that are more accurate, interpretable, and reliable.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A diagnostic workflow provides a structured process for evaluating regression models. By examining fit, residuals, assumptions, leverage, and influence, analysts can identify problems, improve models, and increase confidence in their conclusions.
      </p>

    </div>

    <h2>Completing the Diagnostics Block</h2>

    <p>
      You have now completed the Diagnostics block.
    </p>

    <p>
      This block introduced the major tools used to evaluate regression models, including residual analysis, nonlinearity detection, heteroscedasticity assessment, outlier identification, leverage diagnostics, influence measures, and systematic model evaluation.
    </p>

    <p>
      These tools form the practical foundation of responsible regression analysis.
    </p>

    <p>
      The next block focuses on model fit and comparison, where you will learn how analysts evaluate competing models, compare predictive performance, and select models appropriate for specific goals.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Diagnostics are most effective when used within a structured workflow</li>

        <li>Residual analysis is the foundation of model evaluation</li>

        <li>Linearity, variance, normality, leverage, and influence should all be assessed</li>

        <li>Diagnostic issues should be evaluated based on practical consequences</li>

        <li>Model improvement is often guided by diagnostic findings</li>

        <li>Diagnostics support both model understanding and model refinement</li>

        <li>Model evaluation is typically an iterative process</li>

        <li>A systematic workflow improves the reliability of statistical conclusions</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/diagnostics/cooks-distance/">
         ← Previous: Cook's Distance
      </a>

      <a class="btn"
         href="/modeling/model-fit-comparison/">
         Continue to Model Fit & Comparison →
      </a>

    </div>

  </div>

</section>