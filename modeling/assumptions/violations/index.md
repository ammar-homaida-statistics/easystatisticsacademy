---
layout: default
title: Outliers
description: Learn what outliers are, why they matter in regression analysis, how they influence models, and how analysts investigate unusual observations.
permalink: /modeling/assumptions/outliers/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_assumptions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/assumptions/outliers/",
    label: "Outliers",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 4</span>
      <span class="badge">Assumptions</span>
      <span class="badge">Outliers</span>
    </div>

    <h1>Outliers</h1>

    <p class="lead">
      Most observations follow the general pattern present in a dataset.
    </p>

    <p class="lead">
      Occasionally, however, individual observations differ substantially from the rest. These unusual cases are known as outliers and can have a major impact on regression results.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/assumptions/normality/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/assumptions/violations/">
         Next: Assumption Violations →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is an Outlier?</h2>

    <p>
      An outlier is an observation that differs substantially from the overall pattern of the data.
    </p>

    <p>
      Outliers may occur because of:
    </p>

    <ul class="bullets">

      <li>Measurement errors</li>

      <li>Data entry mistakes</li>

      <li>Rare but legitimate events</li>

      <li>Important underlying processes</li>

    </ul>

    <p>
      Not all outliers are mistakes.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Outliers are observations that are unusually distant from the general pattern of the data and may exert disproportionate influence on regression results.
      </p>

    </div>

    <h2>Why Outliers Matter</h2>

    <p>
      Regression models attempt to fit a relationship that best represents the entire dataset.
    </p>

    <p>
      Extreme observations can pull the fitted line toward themselves.
    </p>

    <p>
      As a result, a small number of unusual points may strongly affect model estimates.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Imagine a scatterplot where most observations cluster around a straight-line trend.
    </p>

    <p>
      One observation appears far above the rest of the data.
    </p>

    <p>
      That single point may substantially change the estimated regression line.
    </p>

    <p>
      The effect can be surprisingly large.
    </p>

    <h2>Outliers in the Outcome Variable</h2>

    <p>
      Some outliers have unusual outcome values.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>An unusually high salary</li>

      <li>An exceptionally large sales figure</li>

      <li>An extreme medical measurement</li>

    </ul>

    <p>
      These observations can produce large residuals.
    </p>

    <h2>Outliers in Predictor Variables</h2>

    <p>
      Outliers may also occur in predictor variables.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>An unusually old participant</li>

      <li>An extremely large company</li>

      <li>An exceptionally expensive house</li>

    </ul>

    <p>
      Such observations may have important effects on model estimation.
    </p>

    <h2>Outliers vs Influential Observations</h2>

    <p>
      Not every outlier has a large impact on the regression model.
    </p>

    <p>
      Likewise, not every influential observation is necessarily an obvious outlier.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Concept</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Outlier</td>
            <td>Observation unusually distant from others</td>
          </tr>

          <tr>
            <td>Influential Observation</td>
            <td>Observation that strongly affects model estimates</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The distinction is important in regression diagnostics.
    </p>

    <h2>Leverage</h2>

    <p>
      One important concept is leverage.
    </p>

    <p>
      High-leverage observations have unusual predictor values compared with the rest of the dataset.
    </p>

    <p>
      These observations can strongly influence the fitted regression line.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Observations with unusual predictor values often have greater potential to influence regression results.
      </p>

    </div>

    <h2>Influence</h2>

    <p>
      Influence refers to how much a particular observation affects model estimates.
    </p>

    <p>
      A highly influential observation may:
    </p>

    <ul class="bullets">

      <li>Change coefficients substantially</li>

      <li>Alter significance tests</li>

      <li>Shift predictions</li>

      <li>Modify conclusions</li>

    </ul>

    <p>
      Influence is often a combination of leverage and residual size.
    </p>

    <h2>Why Outliers Occur</h2>

    <p>
      Outliers may arise from several sources:
    </p>

    <ul class="bullets">

      <li>Recording errors</li>

      <li>Instrument problems</li>

      <li>Sampling mistakes</li>

      <li>Rare but valid observations</li>

      <li>Previously unknown phenomena</li>

    </ul>

    <p>
      Understanding their origin is crucial.
    </p>

    <h2>Should Outliers Be Removed?</h2>

    <p>
      A common mistake is automatically deleting outliers.
    </p>

    <p>
      Outliers should not be removed solely because they are unusual.
    </p>

    <p>
      Legitimate extreme observations may contain important information.
    </p>

    <div class="concept-box">

      <strong>Important warning:</strong>

      <p>
        Outlier removal should be based on clear justification, not simply on a desire to improve statistical results.
      </p>

    </div>

    <h2>Detecting Outliers</h2>

    <p>
      Analysts often begin with graphical methods.
    </p>

    <p>
      Common tools include:
    </p>

    <ul class="bullets">

      <li>Scatterplots</li>

      <li>Boxplots</li>

      <li>Residual plots</li>

      <li>Histograms</li>

    </ul>

    <p>
      Visual inspection frequently reveals unusual observations quickly.
    </p>

    <h2>Standardized Residuals</h2>

    <p>
      Large residuals may indicate potential outliers.
    </p>

    <p>
      Analysts often examine standardized residuals to identify observations that differ substantially from model expectations.
    </p>

    <p>
      Extremely large absolute values warrant investigation.
    </p>

    <h2>Cook's Distance</h2>

    <p>
      One of the most widely used influence measures is Cook's Distance.
    </p>

    <p>
      It quantifies how much the regression model changes when a particular observation is removed.
    </p>

    <p>
      Larger values suggest greater influence.
    </p>

    <h2>DFBETAs and Influence Measures</h2>

    <p>
      Additional diagnostics examine how individual observations affect specific coefficients.
    </p>

    <p>
      These tools help analysts identify observations that disproportionately influence parameter estimates.
    </p>

    <h2>Outliers and Assumptions</h2>

    <p>
      Outliers can contribute to:
    </p>

    <ul class="bullets">

      <li>Non-normal residuals</li>

      <li>Heteroscedasticity</li>

      <li>Poor model fit</li>

      <li>Misleading coefficient estimates</li>

    </ul>

    <p>
      Consequently, outlier assessment is often part of broader assumption checking.
    </p>

    <h2>Robust Methods</h2>

    <p>
      When outliers are common or unavoidable, analysts may use robust statistical methods.
    </p>

    <p>
      These methods reduce the influence of extreme observations while retaining valuable information.
    </p>

    <p>
      Robust approaches are especially useful when unusual observations are legitimate rather than erroneous.
    </p>

    <h2>Outliers and Scientific Discovery</h2>

    <p>
      Sometimes the most interesting observations are outliers.
    </p>

    <p>
      An unexpected observation may reveal:
    </p>

    <ul class="bullets">

      <li>A new phenomenon</li>

      <li>A subgroup of interest</li>

      <li>A flaw in assumptions</li>

      <li>A measurement issue</li>

    </ul>

    <p>
      Outliers deserve investigation rather than automatic elimination.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Outliers are an unavoidable feature of many real-world datasets.
    </p>

    <p>
      Some are errors, some are rare events, and some contain valuable information.
    </p>

    <p>
      Careful analysis helps determine whether unusual observations should be corrected, retained, or modeled differently.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Outliers are unusual observations that may exert substantial influence on regression models. Identifying and understanding them is essential because they can affect coefficients, residual behavior, and statistical conclusions.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Individual assumption violations rarely occur in isolation.
    </p>

    <p>
      Real datasets often exhibit multiple issues simultaneously, including nonlinearity, heteroscedasticity, dependence, and influential observations.
    </p>

    <p>
      The next lesson explores assumption violations more broadly and discusses how analysts respond when assumptions are not fully satisfied.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Outliers are observations that differ substantially from the general data pattern</li>

        <li>Outliers are not necessarily errors</li>

        <li>Some outliers can strongly influence regression results</li>

        <li>Leverage refers to unusual predictor values</li>

        <li>Influence measures how strongly an observation affects model estimates</li>

        <li>Cook's Distance is a common influence diagnostic</li>

        <li>Outlier removal requires justification</li>

        <li>Investigating unusual observations often improves understanding of the data and model</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/assumptions/normality/">
         ← Previous: Normality
      </a>

      <a class="btn"
         href="/modeling/assumptions/violations/">
         Next: Assumption Violations →
      </a>

    </div>

  </div>

</section>