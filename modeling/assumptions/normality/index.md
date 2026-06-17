---
layout: default
title: Normality
description: Learn the normality assumption in regression, what it applies to, when it matters, and how analysts assess residual normality.
permalink: /modeling/assumptions/normality/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_assumptions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/assumptions/normality/",
    label: "Normality",
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
      <span class="badge">Normality</span>
    </div>

    <h1>Normality</h1>

    <p class="lead">
      One of the most frequently misunderstood regression assumptions concerns normality.
    </p>

    <p class="lead">
      Contrary to a common misconception, regression does not require predictors or outcomes themselves to be normally distributed. The assumption focuses on residuals.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/assumptions/homoscedasticity/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/assumptions/outliers/">
         Next: Outliers →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is the Normality Assumption?</h2>

    <p>
      The normality assumption states that regression residuals are approximately normally distributed.
    </p>

    <p>
      Residuals represent the differences between observed outcomes and model predictions.
    </p>

    <p>
      The assumption concerns the distribution of those prediction errors.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        The normality assumption applies to residuals, not to the predictor variables and not necessarily to the outcome variable itself.
      </p>

    </div>

    <h2>A Common Misconception</h2>

    <p>
      Many students believe regression requires all variables to follow normal distributions.
    </p>

    <p>
      This is incorrect.
    </p>

    <p>
      Predictors may be skewed, multimodal, or otherwise non-normal while regression remains perfectly valid.
    </p>

    <p>
      What matters is the behavior of the residuals.
    </p>

    <h2>Why Normality Matters</h2>

    <p>
      The mathematical theory underlying many regression confidence intervals and hypothesis tests assumes normally distributed residuals.
    </p>

    <p>
      When residuals are approximately normal:
    </p>

    <ul class="bullets">

      <li>Confidence intervals tend to perform as expected</li>

      <li>P-values tend to be reliable</li>

      <li>Hypothesis tests have their intended properties</li>

    </ul>

    <p>
      Normality primarily supports statistical inference.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Normality is mainly an inference assumption rather than an estimation assumption.
      </p>

    </div>

    <h2>What Does a Normal Distribution Look Like?</h2>

    <p>
      A normal distribution is:
    </p>

    <ul class="bullets">

      <li>Bell-shaped</li>

      <li>Symmetric</li>

      <li>Centered around its mean</li>

      <li>Characterized by predictable tail behavior</li>

    </ul>

    <p>
      Residuals do not need to follow this shape perfectly.
    </p>

    <p>
      Approximate normality is often sufficient.
    </p>

    <h2>Why Residuals Might Be Normal</h2>

    <p>
      Residuals frequently reflect the combined influence of many small factors that are not explicitly included in the model.
    </p>

    <p>
      When many small influences accumulate, the resulting errors often resemble a normal distribution.
    </p>

    <p>
      This is one reason normality frequently arises in practice.
    </p>

    <h2>What Happens When Normality Fails?</h2>

    <p>
      Violations of normality can affect:
    </p>

    <ul class="bullets">

      <li>Confidence intervals</li>

      <li>Hypothesis tests</li>

      <li>P-values</li>

    </ul>

    <p>
      The severity of the impact depends on the degree of departure from normality and the sample size.
    </p>

    <h2>Skewed Residuals</h2>

    <p>
      One common violation occurs when residuals are skewed.
    </p>

    <p>
      In a skewed distribution:
    </p>

    <ul class="bullets">

      <li>One tail is longer than the other</li>

      <li>The distribution lacks symmetry</li>

      <li>Extreme values occur more often on one side</li>

    </ul>

    <p>
      Severe skewness may affect inference accuracy.
    </p>

    <h2>Heavy-Tailed Residuals</h2>

    <p>
      Another common violation involves heavy tails.
    </p>

    <p>
      Heavy-tailed distributions generate more extreme residuals than a normal distribution would predict.
    </p>

    <p>
      Such residuals often arise because of outliers or unusual observations.
    </p>

    <h2>Sample Size Matters</h2>

    <p>
      The importance of normality depends heavily on sample size.
    </p>

    <p>
      In large samples:
    </p>

    <ul class="bullets">

      <li>Regression inference is often robust to moderate non-normality</li>

      <li>The Central Limit Theorem provides protection</li>

    </ul>

    <p>
      In small samples:
    </p>

    <ul class="bullets">

      <li>Normality becomes more important</li>

      <li>Inference may be more sensitive to violations</li>

    </ul>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Moderate departures from normality are often much less concerning in large datasets than in small datasets.
      </p>

    </div>

    <h2>Histogram of Residuals</h2>

    <p>
      One common way to assess normality is by examining a histogram of residuals.
    </p>

    <p>
      Analysts look for:
    </p>

    <ul class="bullets">

      <li>Approximate symmetry</li>

      <li>Bell-shaped appearance</li>

      <li>Absence of extreme distortions</li>

    </ul>

    <p>
      Visual assessment often provides useful information.
    </p>

    <h2>Q-Q Plots</h2>

    <p>
      A more powerful diagnostic tool is the quantile-quantile plot (Q-Q plot).
    </p>

    <p>
      A Q-Q plot compares observed residual quantiles with the quantiles expected under a normal distribution.
    </p>

    <p>
      If residuals are approximately normal, points tend to follow a straight line.
    </p>

    <h2>Signs of Non-Normality in a Q-Q Plot</h2>

    <p>
      Potential warning signs include:
    </p>

    <ul class="bullets">

      <li>Curvature</li>

      <li>S-shaped patterns</li>

      <li>Extreme deviations in the tails</li>

      <li>Systematic departures from the reference line</li>

    </ul>

    <p>
      These patterns may indicate skewness or heavy tails.
    </p>

    <h2>Formal Normality Tests</h2>

    <p>
      Analysts sometimes use formal statistical tests such as:
    </p>

    <ul class="bullets">

      <li>Shapiro-Wilk test</li>

      <li>Anderson-Darling test</li>

      <li>Kolmogorov-Smirnov test</li>

    </ul>

    <p>
      However, these tests should be interpreted cautiously.
    </p>

    <p>
      Large samples may flag tiny, unimportant deviations, while small samples may fail to detect meaningful problems.
    </p>

    <h2>Normality and Prediction</h2>

    <p>
      Prediction is often less sensitive to normality violations than inference.
    </p>

    <p>
      A model may generate useful predictions even when residuals are not perfectly normal.
    </p>

    <p>
      Nevertheless, prediction intervals can be affected by severe departures from normality.
    </p>

    <h2>Possible Solutions</h2>

    <p>
      When residuals exhibit substantial non-normality, analysts may:
    </p>

    <ul class="bullets">

      <li>Transform variables</li>

      <li>Investigate outliers</li>

      <li>Use robust methods</li>

      <li>Apply alternative modeling approaches</li>

    </ul>

    <p>
      The appropriate response depends on the source of the violation.
    </p>

    <h2>Normality vs Other Assumptions</h2>

    <p>
      Compared with linearity and independence, normality is often less critical.
    </p>

    <p>
      Severe violations of linearity or independence frequently create larger problems than moderate departures from normality.
    </p>

    <p>
      This is especially true when sample sizes are large.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Normality is an assumption about residual distributions rather than the variables themselves.
    </p>

    <p>
      Its primary role is supporting confidence intervals and hypothesis tests.
    </p>

    <p>
      Understanding what the assumption actually applies to helps analysts avoid one of the most common misunderstandings in regression analysis.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The normality assumption concerns regression residuals, not predictors or outcomes. It mainly supports statistical inference, and moderate departures from normality are often acceptable, especially in large samples.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Even when assumptions appear reasonable overall, individual observations can sometimes exert unusual influence on a regression model.
    </p>

    <p>
      Such observations are known as outliers.
    </p>

    <p>
      The next lesson explores outliers, their impact on regression results, and methods for identifying influential observations.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The normality assumption applies to residuals rather than predictors or outcomes</li>

        <li>Normality primarily supports confidence intervals and hypothesis tests</li>

        <li>Skewness and heavy tails are common forms of non-normality</li>

        <li>Large samples are often robust to moderate normality violations</li>

        <li>Histograms and Q-Q plots are common diagnostic tools</li>

        <li>Formal normality tests should be interpreted cautiously</li>

        <li>Prediction is often less sensitive to normality violations than inference</li>

        <li>Understanding residual normality helps ensure reliable statistical inference</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/assumptions/homoscedasticity/">
         ← Previous: Homoscedasticity
      </a>

      <a class="btn"
         href="/modeling/assumptions/outliers/">
         Next: Outliers →
      </a>

    </div>

  </div>

</section>