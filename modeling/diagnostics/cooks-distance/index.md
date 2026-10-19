---
layout: default
title: Cook's Distance
description: Learn what Cook's Distance measures, how it combines leverage and residual information, and how analysts identify influential observations in regression models.
permalink: /modeling/diagnostics/cooks-distance/
sidebar: false
math: true
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_diagnostics_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/diagnostics/cooks-distance/",
    label: "Cook's Distance",
    ts: Date.now()
  }));
  } catch (_) {
    // Lesson navigation works when browser storage is unavailable.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 5</span>
      <span class="badge">Diagnostics</span>
      <span class="badge">Influence Analysis</span>
    </div>

    <h1>Cook's Distance</h1>

    <p class="lead">
      Some observations affect a regression model far more than others.
    </p>

    <p class="lead">
      Cook's Distance is one of the most widely used diagnostics for identifying observations that have unusually large influence on regression results.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/diagnostics/influence/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/diagnostic-workflow/">
         Next: Diagnostic Workflow →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is Cook's Distance?</h2>

    <p>
      Cook's Distance is a diagnostic measure that evaluates how much a regression model changes when a particular observation is removed.
    </p>

    <p>
      It summarizes the overall influence of an observation on the fitted model.
    </p>

    <p>
      Larger values indicate observations that have greater impact on model results.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Cook's Distance measures the influence of an observation by assessing how much the fitted regression model changes when that observation is excluded.
      </p>

    </div>

    <h2>Why Cook's Distance Matters</h2>

    <p>
      Analysts often want to know whether important conclusions depend heavily on a small number of observations.
    </p>

    <p>
      Cook's Distance helps answer that question.
    </p>

    <p>
      It identifies observations that deserve additional investigation because they may be driving the results.
    </p>

    <h2>The Basic Idea</h2>

    <p>
      Imagine fitting a regression model using all observations.
    </p>

    <p>
      Next, remove a single observation and refit the model.
    </p>

    <p>
      If the new model differs substantially from the original model, that observation has high influence.
    </p>

    <p>
      Cook's Distance quantifies this change.
    </p>

    <div class="example-box">

      <p>
        Large model change → Large Cook's Distance
      </p>

      <p>
        Small model change → Small Cook's Distance
      </p>

    </div>

    <h2>What Does Cook's Distance Combine?</h2>

    <p>
      Cook's Distance incorporates two important diagnostic concepts:
    </p>

    <ul class="bullets">

      <li>Residual size</li>

      <li>Leverage</li>

    </ul>

    <p>
      Observations that have both unusual predictor values and large residuals often produce the largest Cook's Distance values.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Influence is often strongest when an observation combines high leverage with a large prediction error.
      </p>

    </div>

    <h2>Why Leverage Alone Is Not Enough</h2>

    <p>
      An observation may have high leverage because its predictor values are unusual.
    </p>

    <p>
      However, if it lies close to the regression line, it may have little effect on the fitted model.
    </p>

    <p>
      Cook's Distance accounts for both leverage and model fit simultaneously.
    </p>

    <h2>Why Residuals Alone Are Not Enough</h2>

    <p>
      An observation may have a large residual but still possess little influence if it lies near the center of the predictor space.
    </p>

    <p>
      Large residuals do not automatically imply that model estimates change substantially.
    </p>

    <p>
      Cook's Distance helps identify observations that truly affect the model.
    </p>

    <h2>Interpreting Cook's Distance</h2>

    <p>
      Cook's Distance values are nonnegative.
    </p>

    <p>
      Larger values indicate greater influence.
    </p>

    <p>
      Most observations in a dataset typically have relatively small Cook's Distance values.
    </p>

    <h2>Relative Rather Than Absolute Interpretation</h2>

    <p>
      Analysts often focus on observations that stand out relative to the rest of the dataset.
    </p>

    <p>
      A value that is unusually large compared with other observations may deserve investigation.
    </p>

    <p>
      Context matters more than rigid thresholds.
    </p>

    <h2>Common Rules of Thumb</h2>

    <p>
      Several heuristic guidelines are frequently used.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>Cook's Distance greater than 1 may indicate substantial influence</li>

      <li>Values notably larger than the majority of observations may deserve attention</li>

      <li>Software often highlights unusually influential observations automatically</li>

    </ul>

    <p>
      These guidelines are diagnostic tools rather than strict rules.
    </p>

    <div class="concept-box">

      <strong>Important warning:</strong>

      <p>
        Large Cook's Distance values identify observations for investigation. They do not automatically justify removing observations.
      </p>

    </div>

    <h2>Cook's Distance Plot</h2>

    <p>
      Analysts often visualize Cook's Distance values using a diagnostic plot.
    </p>

    <p>
      Each observation is assigned a Cook's Distance value and displayed on a graph.
    </p>

    <p>
      Observations with unusually large values become easy to identify.
    </p>

    <h2>Example Interpretation</h2>

    <p>
      Suppose a dataset contains 200 observations.
    </p>

    <p>
      Most Cook's Distance values are near zero.
    </p>

    <p>
      Two observations stand substantially above all others.
    </p>

    <p>
      These observations deserve additional examination because they may strongly affect model results.
    </p>

    <h2>Investigating Influential Observations</h2>

    <p>
      When a large Cook's Distance value is detected, analysts often ask:
    </p>

    <ul class="bullets">

      <li>Is the observation valid?</li>

      <li>Was there a measurement error?</li>

      <li>Does the observation belong to the target population?</li>

      <li>Does it reveal a weakness in the model?</li>

    </ul>

    <p>
      These questions help guide appropriate responses.
    </p>

    <h2>Cook's Distance and Robustness</h2>

    <p>
      Cook's Distance supports robustness analysis.
    </p>

    <p>
      Analysts often compare results with and without influential observations.
    </p>

    <p>
      Stable conclusions increase confidence in the model.
    </p>

    <p>
      Dramatic changes may suggest sensitivity.
    </p>

    <h2>Influence Does Not Mean Error</h2>

    <p>
      Influential observations are not necessarily incorrect.
    </p>

    <p>
      Some may represent:
    </p>

    <ul class="bullets">

      <li>Rare but legitimate cases</li>

      <li>Boundary conditions</li>

      <li>Important subgroups</li>

      <li>New scientific insights</li>

    </ul>

    <p>
      Such observations may contain valuable information.
    </p>

    <h2>Cook's Distance and Model Improvement</h2>

    <p>
      Influential observations sometimes reveal model deficiencies.
    </p>

    <p>
      They may indicate:
    </p>

    <ul class="bullets">

      <li>Missing predictors</li>

      <li>Nonlinear relationships</li>

      <li>Population heterogeneity</li>

      <li>Alternative model structures</li>

    </ul>

    <p>
      Diagnostic investigation often leads to stronger models.
    </p>

    <h2>Cook's Distance vs Other Influence Measures</h2>

    <p>
      Cook's Distance is one of several influence diagnostics.
    </p>

    <p>
      Other measures include:
    </p>

    <ul class="bullets">

      <li>DFFITS</li>

      <li>DFBETAs</li>

      <li>COVRATIO</li>

    </ul>

    <p>
      Cook's Distance remains popular because it summarizes overall influence in a single statistic.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Regression conclusions should ideally reflect the overall dataset rather than a handful of observations.
    </p>

    <p>
      Cook's Distance helps analysts identify cases that may disproportionately affect results.
    </p>

    <p>
      By examining influential observations carefully, analysts can better understand the reliability and stability of their models.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Cook's Distance measures how much a regression model changes when an observation is removed. Large values identify observations with substantial influence and help analysts assess the robustness of model conclusions.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Individual diagnostic tools are useful, but effective model evaluation usually involves combining multiple diagnostics into a systematic process.
    </p>

    <p>
      Analysts rarely examine residuals, leverage, influence, or variance patterns in isolation.
    </p>

    <p>
      The next lesson introduces a practical diagnostic workflow that brings these tools together into a structured approach for evaluating regression models.
    </p>


<!-- COOK'S DISTANCE LEARNING EXPLORER -->
<section class="section section-slim" aria-labelledby="esa-cook-heading">
  <div class="container">
    <div class="card" id="esa-cook-lab" style="min-width:0;overflow-wrap:anywhere">
      <h2 id="esa-cook-heading">Interactive Cook's Distance and Influence Explorer</h2>
      <p>Fit a straight line to <strong>eight illustrative observations</strong>.
      Seven values remain fixed; adjust the red eighth point's position.
      The solid green line uses all observations; the dashed orange line refits the model
      <em>without</em> that point. See how influence changes.</p>
      <div style="display:flex;flex-wrap:wrap;gap:1.2rem">
        <label style="flex:1 1 210px">Selected observation's x: <output id="esa-cook-x-value" for="esa-cook-x">9.0</output>
          <input id="esa-cook-x" type="range" min="7.5" max="15" step="0.5" value="9" style="display:block;width:100%">
        </label>
        <label style="flex:1 1 210px">Selected observation's y: <output id="esa-cook-y-value" for="esa-cook-y">25.0</output>
          <input id="esa-cook-y" type="range" min="0" max="35" step="0.5" value="25" style="display:block;width:100%">
        </label>
        <button type="button" class="btn btn-outline" id="esa-cook-reset">Reset</button>
      </div>
      <p id="esa-cook-status" role="status" aria-live="polite"></p>
      <svg id="esa-cook-chart" viewBox="0 0 680 300" role="img" aria-label="Regression points, full fit, and dashed leave-one-out fit" style="width:100%;max-width:680px;display:block"></svg>
      <p><strong>Line key:</strong> blue circles = fixed observations; red circle = adjustable
      observation; solid green = OLS using all 8 points; dashed orange = OLS after removing
      the red point.</p>
      <dl style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,190px),1fr));gap:.5rem">
        <div><dt>Full-model residual MSE (SSE / 6)</dt><dd id="esa-cook-mse">—</dd></div>
        <div><dt>Selected residual</dt><dd id="esa-cook-residual">—</dd></div>
        <div><dt>Selected leverage</dt><dd id="esa-cook-leverage">—</dd></div>
        <div><dt>Selected Cook's distance</dt><dd id="esa-cook-d">—</dd></div>
        <div><dt>All-data intercept</dt><dd id="esa-cook-full-intercept">—</dd></div>
        <div><dt>All-data slope</dt><dd id="esa-cook-full-slope">—</dd></div>
        <div><dt>Leave-one-out intercept</dt><dd id="esa-cook-leave-intercept">—</dd></div>
        <div><dt>Leave-one-out slope</dt><dd id="esa-cook-leave-slope">—</dd></div>
        <div><dt>Slope change (all − deleted)</dt><dd id="esa-cook-delta-slope">—</dd></div>
      </dl>
      <h3>Diagnostics for every observation</h3>
      <div class="table-wrap"><table>
        <caption>Residuals, leverage and Cook's distance from the full OLS model</caption>
        <thead><tr><th>Observation</th><th>Residual</th><th>Leverage</th><th>Cook's D</th></tr></thead>
        <tbody id="esa-cook-table"></tbody>
      </table></div>
      <div class="concept-box">
        <p><strong>Definition:</strong> For a simple OLS regression with an intercept,
        \(p=2\) coefficients, \(n=8\) observations, residuals \(e_i\), leverage \(h_{ii}\),
        and full-model residual mean square \(\operatorname{MSE}=\operatorname{SSE}/(n-p)\),</p>
        <p>\[D_i = \frac{e_i^2}{p\,\operatorname{MSE}}\frac{h_{ii}}{(1-h_{ii})^2}
        = \frac{\sum_{j=1}^n(\hat y_j-\hat y_{j(-i)})^2}{p\,\operatorname{MSE}}.\]</p>
        <p>The tool calculates both expressions using independent leave-one-out refits
        and checks their numerical agreement. A rule such as \(4/n\) is a rough
        screening heuristic, <strong>not</strong> a universal cutoff.
        Investigate highly influential observations before deciding whether any are invalid.
        This is an educational example and should not be used to justify automatic exclusions.</p>
      </div>
    </div>
  </div>
</section>
<script src="/js/cooks-distance-lab.js" defer></script>


    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Cook's Distance measures the influence of observations on a regression model</li>

        <li>It evaluates how much the model changes when an observation is removed</li>

        <li>Cook's Distance combines leverage and residual information</li>

        <li>Large values indicate observations that deserve investigation</li>

        <li>Influential observations are not necessarily errors</li>

        <li>Cook's Distance supports robustness assessment</li>

        <li>Diagnostic interpretation requires context rather than rigid thresholds</li>

        <li>Cook's Distance is one of the most widely used influence diagnostics in regression analysis</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/diagnostics/influence/">
         ← Previous: Influence
      </a>

      <a class="btn"
         href="/modeling/diagnostics/diagnostic-workflow/">
         Next: Diagnostic Workflow →
      </a>

    </div>

  </div>

</section>