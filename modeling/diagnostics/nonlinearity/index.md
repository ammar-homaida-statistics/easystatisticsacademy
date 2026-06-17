---
layout: default
title: Diagnosing Nonlinearity
description: Learn how to identify nonlinear relationships in regression models, why nonlinearity matters, and how analysts respond when linear assumptions fail.
permalink: /modeling/diagnostics/nonlinearity/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_diagnostics_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/diagnostics/nonlinearity/",
    label: "Diagnosing Nonlinearity",
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
      <span class="badge">Nonlinearity</span>
    </div>

    <h1>Diagnosing Nonlinearity</h1>

    <p class="lead">
      Linear regression assumes that predictors have approximately linear relationships with the outcome.
    </p>

    <p class="lead">
      When this assumption fails, residual patterns often emerge, revealing that the model is missing important structure in the data.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/diagnostics/residual-plots/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/diagnostics/heteroscedasticity/">
         Next: Heteroscedasticity →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is Nonlinearity?</h2>

    <p>
      Nonlinearity occurs when the relationship between a predictor and the outcome cannot be adequately represented by a straight line.
    </p>

    <p>
      The effect of the predictor changes across its range rather than remaining approximately constant.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Nonlinearity means the true relationship contains curvature or changing effects that a simple linear model cannot fully capture.
      </p>

    </div>

    <h2>Why Nonlinearity Matters</h2>

    <p>
      Regression coefficients are interpreted as constant effects.
    </p>

    <p>
      When the true relationship is nonlinear, this interpretation may become misleading.
    </p>

    <p>
      Predictions can also become systematically biased.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose study hours improve exam performance.
    </p>

    <p>
      The first few hours of study may produce large gains, while additional hours produce progressively smaller improvements.
    </p>

    <p>
      This pattern reflects diminishing returns rather than a straight-line relationship.
    </p>

    <h2>How Nonlinearity Appears in Residuals</h2>

    <p>
      If a linear model is fitted to a nonlinear relationship, residuals often display systematic patterns.
    </p>

    <p>
      Instead of appearing randomly scattered, they form visible structures.
    </p>

    <p>
      These structures indicate that the model has not captured the true relationship.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Residual patterns often reveal the shape of the relationship that the model failed to capture.
      </p>

    </div>

    <h2>The Classic U-Shaped Pattern</h2>

    <p>
      One common sign of nonlinearity is a U-shaped residual pattern.
    </p>

    <p>
      Residuals tend to:
    </p>

    <ul class="bullets">

      <li>Be positive at low fitted values</li>

      <li>Become negative in the middle</li>

      <li>Become positive again at high fitted values</li>

    </ul>

    <p>
      This suggests that the true relationship is curved.
    </p>

    <h2>Example of a Curved Residual Pattern</h2>

    

    <p>
      The systematic curve indicates that the linear model is consistently overpredicting in some regions and underpredicting in others.
    </p>

    <h2>Other Residual Patterns</h2>

    <p>
      Nonlinearity can produce several recognizable shapes.
    </p>

    <ul class="bullets">

      <li>U-shaped patterns</li>

      <li>Inverted U-shapes</li>

      <li>S-shaped patterns</li>

      <li>Wave-like structures</li>

    </ul>

    <p>
      Any clear systematic pattern is a warning sign.
    </p>

    <h2>Scatterplots as a Diagnostic Tool</h2>

    <p>
      Residual plots are not the only diagnostic method.
    </p>

    <p>
      Scatterplots of the outcome against individual predictors often reveal curvature directly.
    </p>

    <p>
      Analysts frequently inspect these plots before fitting models.
    </p>

    <h2>Nonlinearity and Prediction Errors</h2>

    <p>
      When nonlinearity exists:
    </p>

    <ul class="bullets">

      <li>Predictions may be systematically wrong</li>

      <li>Certain regions may be consistently underpredicted</li>

      <li>Other regions may be consistently overpredicted</li>

    </ul>

    <p>
      The model fails because a straight line cannot adapt to changing relationships.
    </p>

    <h2>Nonlinearity and R-Squared</h2>

    <p>
      A model can have a respectable R-squared value while still exhibiting substantial nonlinearity.
    </p>

    <p>
      This is why diagnostics remain important even when overall fit statistics appear favorable.
    </p>

    <p>
      Numerical summaries alone may not reveal the problem.
    </p>

    <h2>Sources of Nonlinearity</h2>

    <p>
      Curved relationships arise in many real-world situations.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Diminishing returns</li>

      <li>Biological growth processes</li>

      <li>Learning curves</li>

      <li>Saturation effects</li>

      <li>Threshold effects</li>

    </ul>

    <p>
      Such relationships are often naturally nonlinear.
    </p>

    <h2>What Happens If Nonlinearity Is Ignored?</h2>

    <p>
      Ignoring substantial nonlinearity can lead to:
    </p>

    <ul class="bullets">

      <li>Biased coefficient interpretations</li>

      <li>Poor predictions</li>

      <li>Misleading conclusions</li>

      <li>Persistent residual patterns</li>

    </ul>

    <p>
      The model may appear simpler than reality.
    </p>

    <div class="concept-box">

      <strong>Important warning:</strong>

      <p>
        Strong nonlinearity is often one of the most serious assumption violations because it directly affects the estimated relationships themselves.
      </p>

    </div>

    <h2>How Analysts Respond</h2>

    <p>
      When nonlinearity is detected, analysts may:
    </p>

    <ul class="bullets">

      <li>Transform variables</li>

      <li>Add polynomial terms</li>

      <li>Include interaction terms</li>

      <li>Use nonlinear models</li>

      <li>Fit more flexible modeling approaches</li>

    </ul>

    <p>
      The goal is to better represent the underlying relationship.
    </p>

    <h2>Polynomial Terms</h2>

    <p>
      One common solution is to add higher-order terms.
    </p>

    <p>
      For example:
    </p>

    

    <p>
      The additional term allows the model to represent curvature while remaining within a regression framework.
    </p>

    <h2>Transformations</h2>

    <p>
      Transforming variables can sometimes convert a nonlinear relationship into a more linear one.
    </p>

    <p>
      Common transformations include:
    </p>

    <ul class="bullets">

      <li>Logarithms</li>

      <li>Square roots</li>

      <li>Reciprocals</li>

    </ul>

    <p>
      Transformations are widely used in applied modeling.
    </p>

    <h2>When Mild Nonlinearity Is Acceptable</h2>

    <p>
      Small departures from linearity are often not a major concern.
    </p>

    <p>
      Regression methods can tolerate modest imperfections.
    </p>

    <p>
      Severe curvature, however, deserves careful attention.
    </p>

    <h2>Residual Analysis Is Essential</h2>

    <p>
      Nonlinearity is one of the clearest examples of why residual diagnostics matter.
    </p>

    <p>
      Without residual analysis, analysts may incorrectly assume the model is performing adequately.
    </p>

    <p>
      Residual plots frequently reveal issues that summary statistics cannot.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Linear regression is a powerful tool, but it assumes that relationships can be represented reasonably well by straight lines.
    </p>

    <p>
      Nonlinear relationships violate this assumption and often leave distinctive patterns in residual plots.
    </p>

    <p>
      Recognizing these patterns helps analysts build models that better reflect reality.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Nonlinearity occurs when a straight-line model cannot adequately describe the relationship between predictors and the outcome. Residual plots often reveal this problem through systematic curved patterns, making them essential diagnostic tools.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Residual plots can reveal more than curvature.
    </p>

    <p>
      Another common diagnostic pattern involves changing residual variability across the range of fitted values.
    </p>

    <p>
      The next lesson focuses on heteroscedasticity and explains how changing variance affects regression inference and model evaluation.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Nonlinearity occurs when relationships cannot be adequately represented by a straight line</li>

        <li>Residual plots are one of the primary tools for detecting nonlinearity</li>

        <li>Curved residual patterns often indicate missing structure in the model</li>

        <li>Nonlinearity can produce biased interpretations and poor predictions</li>

        <li>Scatterplots often reveal nonlinear relationships directly</li>

        <li>Polynomial terms and transformations are common solutions</li>

        <li>Strong nonlinearity is one of the most important assumption violations</li>

        <li>Residual diagnostics help analysts identify when more flexible models are needed</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/diagnostics/residual-plots/">
         ← Previous: Residual Plots
      </a>

      <a class="btn"
         href="/modeling/diagnostics/heteroscedasticity/">
         Next: Heteroscedasticity →
      </a>

    </div>

  </div>

</section>