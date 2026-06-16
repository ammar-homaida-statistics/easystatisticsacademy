---
layout: default
title: Sensitivity Analysis and Specification
description: Learn how sensitivity analysis evaluates the stability of statistical conclusions under alternative assumptions, models, and analytical decisions.
permalink: /inference/assumptions-robustness/sensitivity-analysis-and-specification/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_assumptions_robustness_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/assumptions-robustness/sensitivity-analysis-and-specification/",
    label: "Sensitivity Analysis and Specification",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 7</span>
      <span class="badge">Assumptions & Robustness</span>
      <span class="badge">Sensitivity Analysis</span>
    </div>

    <h1>Sensitivity Analysis and Specification</h1>

    <p class="lead">
      Statistical conclusions often depend on analytical choices.
    </p>

    <p class="lead">
      Sensitivity analysis evaluates whether conclusions remain stable when assumptions, models, variables, or methods are changed.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/assumptions-robustness/bootstrap-as-robust-tool/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/assumptions-robustness/reporting-assumptions-and-limitations/">
         Next: Reporting Assumptions and Limitations →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Sensitivity Analysis Matters</h2>

    <p>
      Statistical analyses involve many decisions.
    </p>

    <p>
      Analysts choose:
    </p>

    <ul class="bullets">

      <li>Variables to include</li>

      <li>Models to fit</li>

      <li>Assumptions to adopt</li>

      <li>Observations to analyze</li>

      <li>Methods for handling missing data</li>

    </ul>

    <p>
      Different decisions can sometimes lead to different conclusions.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Sensitivity analysis asks whether conclusions remain similar when reasonable analytical choices are varied.
      </p>

    </div>

    <h2>What Is Sensitivity Analysis?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Sensitivity analysis is the process of evaluating how statistical results change when assumptions, inputs, methods, or model specifications are modified.
      </p>

    </div>

    <p>
      It helps determine whether findings are robust or fragile.
    </p>

    <h2>What Is a Specification?</h2>

    <p>
      In statistical modeling, a specification is a particular way of defining an analysis.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Choice of predictors</li>

      <li>Choice of outcome variable</li>

      <li>Choice of statistical model</li>

      <li>Choice of transformations</li>

      <li>Choice of assumptions</li>

    </ul>

    <p>
      Different specifications may produce different numerical results.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose a regression model estimates the effect of education on income.
    </p>

    <p>
      An analyst might compare:
    </p>

    <ul class="bullets">

      <li>A model with age included</li>

      <li>A model without age included</li>

      <li>A model with experience included</li>

      <li>A model with both variables included</li>

    </ul>

    <p>
      If conclusions remain similar, confidence increases.
    </p>

    <h2>Why Stability Is Important</h2>

    <p>
      Findings that appear only under a single specification may be less trustworthy.
    </p>

    <p>
      Findings that persist across multiple reasonable specifications are generally more convincing.
    </p>

    <div class="concept-box">

      <strong>Robustness principle:</strong>

      <p>
        Strong conclusions should not depend heavily on one arbitrary analytical decision.
      </p>

    </div>

    <h2>Common Sources of Sensitivity</h2>

    <p>
      Results may change because of:
    </p>

    <ul class="bullets">

      <li>Outliers</li>

      <li>Missing-data treatments</li>

      <li>Variable selection</li>

      <li>Model assumptions</li>

      <li>Distributional choices</li>

      <li>Sample restrictions</li>

    </ul>

    <p>
      Sensitivity analysis investigates these possibilities systematically.
    </p>

    <h2>Outlier Sensitivity</h2>

    <p>
      One common approach is to compare results:
    </p>

    <ul class="bullets">

      <li>Using all observations</li>

      <li>After removing influential observations</li>

    </ul>

    <p>
      Large changes may indicate that conclusions depend heavily on a small number of data points.
    </p>

    <h2>Model Sensitivity</h2>

    <p>
      Analysts may compare:
    </p>

    <ul class="bullets">

      <li>Linear models</li>

      <li>Nonlinear models</li>

      <li>Parametric methods</li>

      <li>Nonparametric methods</li>

    </ul>

    <p>
      Similar conclusions across models strengthen confidence in results.
    </p>

    <h2>Assumption Sensitivity</h2>

    <p>
      Some conclusions rely heavily on assumptions.
    </p>

    <p>
      Analysts may explore:
    </p>

    <ul class="bullets">

      <li>Alternative variance assumptions</li>

      <li>Alternative distributional assumptions</li>

      <li>Alternative dependence structures</li>

    </ul>

    <p>
      This helps identify assumptions that materially influence results.
    </p>

    <h2>Missing Data Sensitivity</h2>

    <p>
      Missing values can affect analyses in important ways.
    </p>

    <p>
      Sensitivity studies may compare:
    </p>

    <ul class="bullets">

      <li>Complete-case analysis</li>

      <li>Imputation methods</li>

      <li>Alternative missing-data assumptions</li>

    </ul>

    <p>
      Different approaches can sometimes produce different conclusions.
    </p>

    <h2>Subgroup Sensitivity</h2>

    <p>
      Analysts may also examine whether results remain similar across:
    </p>

    <ul class="bullets">

      <li>Age groups</li>

      <li>Regions</li>

      <li>Treatment categories</li>

      <li>Time periods</li>

    </ul>

    <p>
      Large differences may reveal important heterogeneity.
    </p>

    <h2>The Idea of Specification Curves</h2>

    <p>
      Modern researchers sometimes evaluate many reasonable specifications simultaneously.
    </p>

    <p>
      A specification curve displays how estimated effects change across a large collection of analytical choices.
    </p>

    <p>
      This provides a transparent view of analytical sensitivity.
    </p>

    <h2>Fragile Conclusions</h2>

    <p>
      A result may be considered fragile if:
    </p>

    <ul class="bullets">

      <li>Small changes produce large differences</li>

      <li>Significance appears only under one specification</li>

      <li>Estimates vary dramatically across methods</li>

    </ul>

    <p>
      Fragility does not necessarily invalidate a result, but it should be reported and interpreted carefully.
    </p>

    <h2>Robust Conclusions</h2>

    <p>
      A result may be considered robust if:
    </p>

    <ul class="bullets">

      <li>Estimates remain similar across specifications</li>

      <li>Confidence intervals overlap substantially</li>

      <li>Conclusions are consistent across methods</li>

      <li>No single assumption dominates the result</li>

    </ul>

    <p>
      Robust findings inspire greater confidence.
    </p>

    <h2>Sensitivity Analysis Is Not Fishing</h2>

    <p>
      A common misconception is that trying multiple analyses is always problematic.
    </p>

    <p>
      The purpose of sensitivity analysis is not to search for significance.
    </p>

    <p>
      Instead, the goal is to evaluate stability and transparency.
    </p>

    <div class="concept-box">

      <strong>Important distinction:</strong>

      <p>
        Sensitivity analysis examines whether conclusions persist. P-hacking searches for conclusions that happen to appear.
      </p>

    </div>

    <h2>Transparency Is Essential</h2>

    <p>
      Good statistical practice includes reporting:
    </p>

    <ul class="bullets">

      <li>Alternative specifications examined</li>

      <li>Sensitivity analyses performed</li>

      <li>Changes in conclusions</li>

      <li>Important uncertainties</li>

    </ul>

    <p>
      Readers should understand how stable the findings are.
    </p>

    <h2>The Scientific Perspective</h2>

    <p>
      Scientific conclusions are strongest when they survive scrutiny from multiple angles.
    </p>

    <p>
      Sensitivity analysis helps determine whether findings reflect genuine evidence or artifacts of modeling choices.
    </p>

    <h2>A Practical Checklist</h2>

    <ol>

      <li>Identify key assumptions</li>

      <li>Identify important analytical decisions</li>

      <li>Evaluate reasonable alternatives</li>

      <li>Compare conclusions across specifications</li>

      <li>Report any meaningful changes</li>

    </ol>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical analyses inevitably involve judgment and choice.
    </p>

    <p>
      Sensitivity analysis helps quantify how much those choices influence conclusions.
    </p>

    <p>
      Stable findings are generally more trustworthy than findings that depend on a single specification.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Sensitivity analysis evaluates whether conclusions remain stable under alternative assumptions, models, and analytical choices. Robust findings persist across reasonable specifications, while fragile findings require greater caution.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Every statistical analysis relies on assumptions and faces limitations.
    </p>

    <p>
      Responsible reporting requires communicating these assumptions clearly so readers can evaluate the strength and credibility of conclusions.
    </p>

    <p>
      The next lesson focuses on reporting assumptions and limitations as an essential part of transparent statistical practice.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Sensitivity analysis evaluates the stability of conclusions</li>

        <li>Specifications are alternative analytical choices or model definitions</li>

        <li>Robust conclusions remain similar across reasonable specifications</li>

        <li>Outliers, assumptions, and model choices can influence results</li>

        <li>Missing-data handling can affect inference</li>

        <li>Specification curves provide a transparent view of analytical choices</li>

        <li>Sensitivity analysis promotes transparency rather than significance hunting</li>

        <li>Stable conclusions generally inspire greater confidence</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/assumptions-robustness/bootstrap-as-robust-tool/">
         ← Previous: Bootstrap as a Robust Tool
      </a>

      <a class="btn"
         href="/inference/assumptions-robustness/reporting-assumptions-and-limitations/">
         Next: Reporting Assumptions and Limitations →
      </a>

    </div>

  </div>

</section>