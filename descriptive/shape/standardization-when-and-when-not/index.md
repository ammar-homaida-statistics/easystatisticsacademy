---
layout: default
title: Standardization: When and When Not
description: Learn when standardization and z-scores are useful, when they can be misleading, and how to decide whether standardization is appropriate.
permalink: /descriptive/shape/standardization-when-and-when-not/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_shape_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/shape/standardization-when-and-when-not/",
    label: "Standardization: When and When Not",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 6</span>
      <span class="badge">Shape</span>
      <span class="badge">Standardization</span>
    </div>

    <h1>Standardization: When and When Not</h1>

    <p class="lead">
      Z-scores allow observations to be compared on a common scale.
    </p>

    <p class="lead">
      However,
      standardization is not always appropriate.
      Understanding when to use it—and when to avoid it—is an important part of statistical reasoning.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/shape/z-scores/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/shape/shape-in-reporting/">
         Next: Shape in Reporting →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is Standardization?</h2>

    <p>
      Standardization is the process of converting observations into z-scores.
    </p>

    <p>
      Instead of using the original measurement units,
      observations are expressed as distances from the mean measured in standard deviations.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Standardization transforms observations onto a common scale while preserving their relative positions within the distribution.
      </p>

    </div>

    <h2>Why Standardization Is Useful</h2>

    <p>
      Raw values often cannot be compared directly.
    </p>

    <p>
      Different variables may use different units,
      scales,
      or ranges.
    </p>

    <p>
      Standardization removes these differences and creates a common framework for comparison.
    </p>

    <h2>When Standardization Is Helpful</h2>

    <p>
      Standardization is particularly useful when:
    </p>

    <ul class="bullets">

      <li>Comparing observations from different distributions</li>

      <li>Comparing variables measured in different units</li>

      <li>Identifying unusual observations</li>

      <li>Preparing data for statistical models</li>

      <li>Analyzing relative standing within a group</li>

    </ul>

    <p>
      In these situations,
      z-scores often provide information that raw values cannot.
    </p>

    <h2>Example: Comparing Exam Scores</h2>

    <p>
      Student A scores:
    </p>

    <div class="example-box">

      <p>
        85 on Statistics
      </p>
    </div>

    <p>
      Student B scores:
    </p>

    <div class="example-box">

      <p>
        760 on a standardized test
      </p>
    </div>

    <p>
      The raw scores use different scales.
    </p>

    <p>
      Direct comparison is not meaningful.
    </p>

    <p>
      Standardization converts both scores to z-scores,
      allowing us to compare relative performance.
    </p>

    <h2>Example: Identifying Unusual Values</h2>

    <p>
      Suppose an observation has:
    </p>

    <div class="example-box">

      <p>
        z = 3.2
      </p>
    </div>

    <p>
      This observation lies more than three standard deviations above the mean.
    </p>

    <p>
      It would generally be considered highly unusual.
    </p>

    <p>
      Standardization makes such judgments straightforward.
    </p>

    <h2>Standardization Preserves Shape</h2>

    <p>
      A common misconception is that standardization changes the shape of a distribution.
    </p>

    <p>
      It does not.
    </p>

    <p>
      Standardization changes only the scale.
    </p>

    <p>
      The distribution's:
    </p>

    <ul class="bullets">

      <li>Skewness</li>

      <li>Symmetry</li>

      <li>Modality</li>

      <li>Outliers</li>

    </ul>

    <p>
      remain unchanged.
    </p>

    <h2>When Standardization Can Be Misleading</h2>

    <p>
      Although powerful,
      standardization does not automatically make every analysis meaningful.
    </p>

    <p>
      In some situations,
      z-scores can create a false sense of comparability.
    </p>

    <h2>Highly Skewed Distributions</h2>

    <p>
      Z-scores are often easiest to interpret in approximately symmetric,
      bell-shaped distributions.
    </p>

    <p>
      In strongly skewed distributions,
      standard deviations may not describe typical distances particularly well.
    </p>

    <p>
      Consequently,
      z-scores may be less informative.
    </p>

    <div class="example-box">

      <strong>Example:</strong>

      <p>
        Income distributions are often heavily right-skewed.
      </p>

      <p>
        A z-score may not communicate typical standing as clearly as it would in a bell-shaped distribution.
      </p>

    </div>

    <h2>Presence of Extreme Outliers</h2>

    <p>
      Standard deviation is sensitive to outliers.
    </p>

    <p>
      Because z-scores depend on standard deviation,
      extreme observations can influence the scale used for standardization.
    </p>

    <p>
      This may complicate interpretation.
    </p>

    <h2>Categorical Variables Cannot Be Standardized</h2>

    <p>
      Standardization requires numerical data.
    </p>

    <p>
      Categories such as:
    </p>

    <ul class="bullets">

      <li>Gender</li>

      <li>Country</li>

      <li>Blood type</li>

      <li>Favorite color</li>

    </ul>

    <p>
      have no meaningful mean or standard deviation.
    </p>

    <p>
      Therefore,
      z-scores are not appropriate.
    </p>

    <h2>Ordinal Variables Require Caution</h2>

    <p>
      Ordinal scales contain rankings,
      but differences between ranks are not necessarily equal.
    </p>

    <p>
      As a result,
      standardization may not be meaningful.
    </p>

    <p>
      Analysts should evaluate whether arithmetic operations are justified before calculating z-scores.
    </p>

    <h2>When Original Units Matter</h2>

    <p>
      Sometimes the original units provide important practical meaning.
    </p>

    <div class="example-box">

      <p>
        Blood Pressure = 180 mmHg
      </p>
    </div>

    <p>
      This value has immediate medical significance.
    </p>

    <p>
      Converting it into a z-score may remove information that practitioners need.
    </p>

    <p>
      In such situations,
      reporting the original measurement is often preferable.
    </p>

    <h2>Interpretability vs Comparability</h2>

    <p>
      Standardization improves comparability.
    </p>

    <p>
      Original units improve interpretability.
    </p>

    <p>
      Analysts often need to balance these competing goals.
    </p>

    <p>
      In many reports,
      both raw values and standardized values are presented together.
    </p>

    <h2>Standardization in Statistical Modeling</h2>

    <p>
      Many modern analytical methods benefit from standardized variables.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Regression analysis</li>

      <li>Principal component analysis</li>

      <li>Cluster analysis</li>

      <li>Machine learning algorithms</li>

    </ul>

    <p>
      Standardization often improves numerical stability and interpretability in these methods.
    </p>

    <h2>Questions to Ask Before Standardizing</h2>

    <p>
      Before converting observations into z-scores,
      consider:
    </p>

    <ul class="bullets">

      <li>Is the variable numerical?</li>

      <li>Is comparison across scales needed?</li>

      <li>Is the distribution extremely skewed?</li>

      <li>Are there influential outliers?</li>

      <li>Do original units carry important meaning?</li>

    </ul>

    <p>
      These questions help determine whether standardization is appropriate.
    </p>

    <h2>A Practical Rule of Thumb</h2>

    <div class="example-box">

      <strong>Use standardization when:</strong>

      <ul>
        <li>You need comparisons across different scales.</li>
        <li>You want to assess relative standing.</li>
        <li>You need standardized inputs for models.</li>
      </ul>

    </div>

    <div class="example-box">

      <strong>Avoid relying solely on standardization when:</strong>

      <ul>
        <li>The variable is categorical.</li>
        <li>The distribution is extremely irregular.</li>
        <li>Original units are critical for interpretation.</li>
      </ul>

    </div>

    <h2>Why Statistical Judgment Matters</h2>

    <p>
      No statistical tool is universally appropriate.
    </p>

    <p>
      Standardization is valuable,
      but it should be applied thoughtfully.
    </p>

    <p>
      Good analysts consider both the strengths and limitations of z-scores before using them.
    </p>

    <h2>Connecting Shape and Standardization</h2>

    <p>
      Throughout this block,
      we have explored symmetry,
      skewness,
      tails,
      outliers,
      and standardization.
    </p>

    <p>
      These concepts are closely connected.
    </p>

    <p>
      Understanding shape helps determine how standardized measures should be interpreted.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The final lesson of this block focuses on communicating distribution shape effectively.
    </p>

    <p>
      We will learn how to describe shape professionally,
      summarize important features,
      and incorporate shape into statistical reporting.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Standardization converts observations into z-scores</li>

        <li>It allows comparisons across different scales and units</li>

        <li>Standardization preserves the shape of a distribution</li>

        <li>Z-scores may be less informative for highly skewed distributions</li>

        <li>Categorical variables cannot be meaningfully standardized</li>

        <li>Original units sometimes remain important for interpretation</li>

        <li>Good statistical practice requires thoughtful use of standardization</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/shape/z-scores/">
         ← Previous: Z-Scores
      </a>

      <a class="btn"
         href="/descriptive/shape/shape-in-reporting/">
         Next: Shape in Reporting →
      </a>

    </div>

  </div>

</section>