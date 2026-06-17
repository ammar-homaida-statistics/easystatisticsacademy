---
layout: default
title: AIC and BIC
description: Learn how AIC and BIC help compare statistical models by balancing model fit and complexity, and understand when analysts use these information criteria.
permalink: /modeling/model-fit-comparison/aic-bic/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_model_fit_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/model-fit-comparison/aic-bic/",
    label: "AIC and BIC",
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
      <span class="badge">Information Criteria</span>
    </div>

    <h1>AIC and BIC</h1>

    <p class="lead">
      Better fit is desirable, but more complex models almost always fit data more closely.
    </p>

    <p class="lead">
      To prevent unnecessary complexity from being rewarded automatically, statisticians use information criteria such as AIC and BIC.
    </p>

    <p class="lead">
      These measures help compare competing models while balancing fit and simplicity.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/model-fit-comparison/model-comparison/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/model-selection-thinking/">
         Next: Model Selection Thinking →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Do We Need AIC and BIC?</h2>

    <p>
      Measures such as R-squared reward improved fit but do not adequately discourage unnecessary complexity.
    </p>

    <p>
      Adding more predictors often improves fit even when those predictors contribute little useful information.
    </p>

    <p>
      Information criteria address this problem by introducing explicit penalties for model complexity.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        AIC and BIC compare models by balancing two competing goals: good fit and model simplicity.
      </p>

    </div>

    <h2>The Trade-Off They Address</h2>

    <p>
      Effective model selection involves balancing:
    </p>

    <ul class="bullets">

      <li>Fit to observed data</li>

      <li>Model complexity</li>

    </ul>

    <p>
      Extremely simple models may underfit.
    </p>

    <p>
      Extremely complex models may overfit.
    </p>

    <p>
      AIC and BIC help identify models that strike a reasonable balance.
    </p>

    <h2>What Is AIC?</h2>

    <p>
      AIC stands for <strong>Akaike Information Criterion</strong>.
    </p>

    <p>
      It was developed by the Japanese statistician
      0.
    </p>

    <p>
      AIC estimates how much information is lost when a model is used to represent reality.
    </p>

    <p>
      Models with less information loss are generally preferred.
    </p>

    <h2>What Is BIC?</h2>

    <p>
      BIC stands for <strong>Bayesian Information Criterion</strong>.
    </p>

    <p>
      Like AIC, it balances fit and complexity.
    </p>

    <p>
      However, BIC applies a stronger penalty for additional parameters, especially in large samples.
    </p>

    <h2>The General Idea</h2>

    <p>
      Both criteria can be summarized conceptually as:
    </p>

    <div class="example-box">

      <p>
        Score = Model Fit + Complexity Penalty
      </p>
    </div>

    <p>
      Better fit lowers the score.
    </p>

    <p>
      Greater complexity increases the score.
    </p>

    <p>
      The preferred model is usually the one with the smallest value.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Unlike R-squared, lower values of AIC and BIC generally indicate better models.
      </p>

    </div>

    <h2>AIC Formula</h2>

    <p>
      The basic AIC formula is:
    </p>

    

    <p>
      where:
    </p>

    <ul class="bullets">

      <li><strong>k</strong> = number of model parameters</li>

      <li><strong>L</strong> = likelihood of the model</li>

    </ul>

    <p>
      The first term penalizes complexity, while the second rewards fit.
    </p>

    <h2>BIC Formula</h2>

    <p>
      The basic BIC formula is:
    </p>

    

    <p>
      where:
    </p>

    <ul class="bullets">

      <li><strong>k</strong> = number of parameters</li>

      <li><strong>n</strong> = sample size</li>

      <li><strong>L</strong> = likelihood</li>

    </ul>

    <p>
      Because the penalty includes sample size, BIC tends to penalize complexity more heavily than AIC.
    </p>

    <h2>How To Interpret Them</h2>

    <p>
      Absolute values of AIC and BIC are rarely meaningful by themselves.
    </p>

    <p>
      Instead, analysts compare values across competing models.
    </p>

    <p>
      The model with the smaller value is usually preferred.
    </p>

    <h2>An Example Comparison</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Model</th>
            <th>AIC</th>
            <th>BIC</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Model A</td>
            <td>420</td>
            <td>435</td>
          </tr>

          <tr>
            <td>Model B</td>
            <td>405</td>
            <td>428</td>
          </tr>

          <tr>
            <td>Model C</td>
            <td>399</td>
            <td>445</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Using AIC, Model C would be preferred because it has the smallest value.
    </p>

    <p>
      Using BIC, Model B would be preferred because its stronger complexity penalty changes the comparison.
    </p>

    <h2>Why AIC and BIC May Disagree</h2>

    <p>
      AIC and BIC pursue slightly different goals.
    </p>

    <ul class="bullets">

      <li>AIC tends to favor predictive performance</li>

      <li>BIC tends to favor simpler models</li>

    </ul>

    <p>
      As a result, they sometimes recommend different models.
    </p>

    <h2>AIC vs BIC</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Feature</th>
            <th>AIC</th>
            <th>BIC</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Penalizes complexity</td>
            <td>Yes</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Penalty strength</td>
            <td>Moderate</td>
            <td>Stronger</td>
          </tr>

          <tr>
            <td>Often favors</td>
            <td>Prediction</td>
            <td>Simplicity</td>
          </tr>

          <tr>
            <td>Depends on sample size</td>
            <td>Indirectly</td>
            <td>Directly</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>When Analysts Use AIC</h2>

    <p>
      AIC is commonly used when prediction is a primary objective.
    </p>

    <p>
      Because it imposes a less severe complexity penalty, it often favors models that capture additional predictive information.
    </p>

    <p>
      This can improve future prediction performance.
    </p>

    <h2>When Analysts Use BIC</h2>

    <p>
      BIC is frequently used when identifying a parsimonious explanatory model is important.
    </p>

    <p>
      Its stronger penalty tends to discourage unnecessary predictors.
    </p>

    <p>
      This often leads to simpler final models.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Neither AIC nor BIC is universally superior. Their usefulness depends on the goals of the analysis.
      </p>

    </div>

    <h2>Information Criteria and Overfitting</h2>

    <p>
      Both measures help reduce overfitting risk.
    </p>

    <p>
      Rather than rewarding complexity automatically, they require additional parameters to provide meaningful improvements in fit.
    </p>

    <p>
      This encourages more balanced models.
    </p>

    <h2>Limitations of AIC and BIC</h2>

    <p>
      Information criteria are useful tools, but they are not complete measures of model quality.
    </p>

    <p>
      They do not directly evaluate:
    </p>

    <ul class="bullets">

      <li>Prediction on future data</li>

      <li>Assumption validity</li>

      <li>Causal interpretation</li>

      <li>Scientific plausibility</li>

    </ul>

    <p>
      Other diagnostics remain important.
    </p>

    <h2>Model Selection Requires Judgment</h2>

    <p>
      Analysts rarely choose models based solely on AIC or BIC.
    </p>

    <p>
      Instead, these criteria are typically combined with:
    </p>

    <ul class="bullets">

      <li>Theory</li>

      <li>Interpretability</li>

      <li>Diagnostics</li>

      <li>Predictive evaluation</li>

    </ul>

    <p>
      Statistical judgment remains essential.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      AIC and BIC are among the most widely used tools for comparing competing statistical models.
    </p>

    <p>
      By balancing model fit against complexity, they help analysts avoid overfitting and identify models that provide useful explanations without unnecessary complication.
    </p>

    <p>
      They represent an important step toward principled model selection.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        AIC and BIC compare models by balancing fit and complexity. Lower values generally indicate better models, and both criteria help discourage unnecessary complexity while supporting effective model selection.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Choosing among competing models is not simply a matter of comparing statistics.
    </p>

    <p>
      Effective model selection requires broader thinking about goals, trade-offs, prediction, explanation, and practical usefulness.
    </p>

    <p>
      The next lesson explores model selection thinking and introduces a more holistic approach to choosing statistical models.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>AIC and BIC balance model fit against complexity</li>

        <li>Both measures penalize unnecessary parameters</li>

        <li>Lower values generally indicate better models</li>

        <li>AIC often favors predictive performance</li>

        <li>BIC generally favors simpler models</li>

        <li>Information criteria help reduce overfitting risk</li>

        <li>Absolute values are less important than comparisons between models</li>

        <li>AIC and BIC should be used alongside other model evaluation tools</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/model-fit-comparison/model-comparison/">
         ← Previous: Model Comparison
      </a>

      <a class="btn"
         href="/modeling/model-fit-comparison/model-selection-thinking/">
         Next: Model Selection Thinking →
      </a>

    </div>

  </div>

</section>