---
layout: default
title: Outliers and Influence
description: Learn what outliers are, how influential observations affect statistical analyses, and how to evaluate their impact responsibly.
permalink: /inference/assumptions-robustness/outliers-and-influence/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_assumptions_robustness_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/assumptions-robustness/outliers-and-influence/",
    label: "Outliers and Influence",
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
      <span class="badge">Outliers</span>
    </div>

    <h1>Outliers and Influence</h1>

    <p class="lead">
      A small number of unusual observations can sometimes have a surprisingly large impact on statistical conclusions.
    </p>

    <p class="lead">
      Understanding outliers and influential observations helps analysts distinguish between meaningful signals, data-quality problems, and artifacts of the analysis process.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/assumptions-robustness/heteroscedasticity-variance-issues/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/assumptions-robustness/robust-alternatives-nonparametric/">
         Next: Robust Alternatives & Nonparametric Methods →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Outliers Matter</h2>

    <p>
      Most statistical methods summarize large collections of observations.
    </p>

    <p>
      Occasionally, one or a few observations fall far from the majority of the data.
    </p>

    <p>
      These unusual observations may substantially affect estimates, standard errors, and statistical conclusions.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Not all unusual observations are problematic, but all important outliers deserve investigation.
      </p>

    </div>

    <h2>What Is an Outlier?</h2>

    <p>
      An outlier is an observation that appears unusually distant from the rest of the dataset.
    </p>

    <p>
      Outliers may occur because of:
    </p>

    <ul class="bullets">

      <li>Natural variation</li>

      <li>Rare events</li>

      <li>Measurement errors</li>

      <li>Data-entry mistakes</li>

      <li>Population heterogeneity</li>

    </ul>

    <h2>Outlier Does Not Mean Error</h2>

    <p>
      A common mistake is assuming that every outlier is wrong.
    </p>

    <p>
      In reality, some outliers represent genuine and important observations.
    </p>

    <div class="example-box">

      <p>
        An unusually large insurance claim may be rare, but it may still be a valid observation.
      </p>
    </div>

    <p>
      Outliers should be examined, not automatically removed.
    </p>

    <h2>Why Outliers Can Be Problematic</h2>

    <p>
      Many statistical methods are sensitive to extreme values.
    </p>

    <p>
      Outliers can affect:
    </p>

    <ul class="bullets">

      <li>Means</li>

      <li>Variances</li>

      <li>Standard deviations</li>

      <li>Regression estimates</li>

      <li>Hypothesis tests</li>

    </ul>

    <p>
      A single observation may sometimes have a disproportionate effect.
    </p>

    <h2>The Mean vs the Median</h2>

    <p>
      Consider the values:
    </p>

    <div class="example-box">

      <p>
        5, 6, 7, 8, 100
      </p>
    </div>

    <p>
      The value 100 strongly influences the mean.
    </p>

    <p>
      The median changes much less.
    </p>

    <p>
      This illustrates why some statistics are more robust than others.
    </p>

    <h2>Outliers and Variability</h2>

    <p>
      Outliers often increase estimates of variability.
    </p>

    <p>
      As a result:
    </p>

    <ul class="bullets">

      <li>Standard deviations may increase</li>

      <li>Standard errors may increase</li>

      <li>Confidence intervals may widen</li>

    </ul>

    <p>
      Inferential conclusions may change substantially.
    </p>

    <h2>Detecting Outliers Graphically</h2>

    <p>
      Visual inspection is often the first step.
    </p>

    <p>
      Useful graphical tools include:
    </p>

    <ul class="bullets">

      <li>Histograms</li>

      <li>Boxplots</li>

      <li>Scatterplots</li>

      <li>Residual plots</li>

    </ul>

    <p>
      Graphs frequently reveal unusual observations more effectively than numerical summaries.
    </p>

    <h2>Boxplots and Outliers</h2>

    <p>
      Boxplots are commonly used to identify potential outliers.
    </p>

    <p>
      Observations located far beyond the whiskers are often flagged for further investigation.
    </p>

    <p>
      Being flagged does not automatically mean the observation should be removed.
    </p>

    <h2>Standardized Observations</h2>

    <p>
      Analysts sometimes examine observations relative to the overall variability of the data.
    </p>

    <p>
      Standardized values help identify observations that are unusually far from the center.
    </p>

    0

    <h2>Outliers in Regression</h2>

    <p>
      Outliers become particularly important in regression analysis.
    </p>

    <p>
      An unusual observation may affect:
    </p>

    <ul class="bullets">

      <li>Regression slopes</li>

      <li>Predicted values</li>

      <li>Standard errors</li>

      <li>Model fit statistics</li>

    </ul>

    <p>
      Some observations can exert much more influence than others.
    </p>

    <h2>What Is Influence?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        An influential observation is one whose inclusion or removal substantially changes the results of an analysis.
      </p>

    </div>

    <p>
      Influence is about impact, not simply unusualness.
    </p>

    <h2>Outlier vs Influential Observation</h2>

    <p>
      These concepts are related but different.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Concept</th>
            <th>Main Idea</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Outlier</td>
            <td>Unusual observation</td>
          </tr>

          <tr>
            <td>Influential Observation</td>
            <td>Observation that changes conclusions</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      An observation can be:
    </p>

    <ul class="bullets">

      <li>An outlier but not influential</li>

      <li>Influential but not extreme in value</li>

      <li>Both outlying and influential</li>

    </ul>

    <h2>High-Leverage Points</h2>

    <p>
      In regression, observations with unusual predictor values are often called:
    </p>

    <div class="example-box">

      <p>
        High-leverage points
      </p>
    </div>

    <p>
      High leverage increases the potential for influence.
    </p>

    <p>
      However, not all high-leverage observations are influential.
    </p>

    <h2>Why Investigation Matters</h2>

    <p>
      When unusual observations appear, analysts should ask:
    </p>

    <ul class="bullets">

      <li>Is the observation valid?</li>

      <li>Was there a recording error?</li>

      <li>Does the observation represent a different population?</li>

      <li>How sensitive are conclusions to its presence?</li>

    </ul>

    <p>
      Investigation is more important than automatic deletion.
    </p>

    <h2>Avoid Automatic Removal</h2>

    <p>
      Removing observations solely because they are unusual can introduce bias.
    </p>

    <p>
      Outlier removal should have a clear justification.
    </p>

    <div class="concept-box">

      <strong>Good practice:</strong>

      <p>
        Remove observations only when there is evidence that they are erroneous or inappropriate for the intended analysis.
      </p>

    </div>

    <h2>Sensitivity Analysis</h2>

    <p>
      One useful strategy is to compare results:
    </p>

    <ul class="bullets">

      <li>With the observation included</li>

      <li>With the observation excluded</li>

    </ul>

    <p>
      Large differences suggest substantial influence.
    </p>

    <p>
      This approach helps evaluate robustness.
    </p>

    <h2>Robust Statistics</h2>

    <p>
      Some statistical methods are intentionally designed to reduce sensitivity to outliers.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Medians instead of means</li>

      <li>Trimmed means</li>

      <li>Robust regression methods</li>

      <li>Nonparametric procedures</li>

    </ul>

    <p>
      These approaches can provide more stable conclusions in the presence of extreme observations.
    </p>

    <h2>Outliers and Scientific Discovery</h2>

    <p>
      Sometimes the most interesting observations are the unusual ones.
    </p>

    <p>
      Scientific breakthroughs have occasionally emerged from investigating observations that initially appeared anomalous.
    </p>

    <p>
      Outliers can reveal important processes that standard analyses overlook.
    </p>

    <h2>The Robustness Perspective</h2>

    <p>
      The key question is not:
    </p>

    <div class="example-box">

      <p>
        Does an outlier exist?
      </p>
    </div>

    <p>
      Instead ask:
    </p>

    <div class="example-box">

      <p>
        Does the outlier meaningfully affect the conclusions?
      </p>
    </div>

    <p>
      This distinction focuses attention on practical impact rather than simple detection.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Outliers are common in real datasets.
    </p>

    <p>
      Some are errors, some are rare events, and some represent important scientific information.
    </p>

    <p>
      Responsible statistical practice involves understanding their source and evaluating their influence rather than applying automatic rules.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Outliers are unusual observations, while influential observations are those that substantially affect analytical conclusions. Good statistical practice focuses on investigation, sensitivity analysis, and robustness rather than automatic removal.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Classical statistical procedures often rely on assumptions about distributions and sensitivity to extreme values.
    </p>

    <p>
      When these assumptions become questionable, analysts may use robust or nonparametric alternatives.
    </p>

    <p>
      The next lesson introduces these approaches and explains when they provide useful alternatives to traditional methods.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Outliers are observations that appear unusually distant from the rest of the data</li>

        <li>Outliers are not automatically errors</li>

        <li>Extreme observations can affect estimates and inference</li>

        <li>Influential observations are those that materially change conclusions</li>

        <li>Outliers and influence are related but distinct concepts</li>

        <li>Graphs are useful for identifying unusual observations</li>

        <li>Sensitivity analysis helps evaluate influence</li>

        <li>Robust methods can reduce sensitivity to extreme observations</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/assumptions-robustness/heteroscedasticity-variance-issues/">
         ← Previous: Heteroscedasticity and Variance Issues
      </a>

      <a class="btn"
         href="/inference/assumptions-robustness/robust-alternatives-nonparametric/">
         Next: Robust Alternatives & Nonparametric Methods →
      </a>

    </div>

  </div>

</section>