---
layout: default
title: Variance
description: Learn what variance is, how it measures variability, and why it forms the foundation for many advanced statistical methods.
permalink: /descriptive/spread/variance/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_spread_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/spread/variance/",
    label: "Variance",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 5</span>
      <span class="badge">Spread</span>
      <span class="badge">Variance</span>
    </div>

    <h1>Variance</h1>

    <p class="lead">
      The range and the interquartile range provide useful summaries of variability,
      but they do not use all observations in a dataset.
    </p>

    <p class="lead">
      Variance takes a different approach.
      It measures how far observations tend to be from the center,
      making it one of the most important concepts in all of statistics.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/spread/interquartile-range/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/spread/standard-deviation/">
         Next: Standard Deviation →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>Why Do We Need Variance?</h2>

    <p>
      Measures such as the range and IQR tell us about overall spread,
      but they do not account for the position of every observation.
    </p>

    <p>
      Variance uses all observations and measures how much they deviate from the center of the distribution.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Variance measures the average squared distance between observations and their mean.
      </p>

    </div>

    <h2>The Basic Idea</h2>

    <p>
      Suppose every observation is exactly equal to the mean.
    </p>

    <div class="example-box">

      <p>
        10, 10, 10, 10, 10
      </p>

    </div>

    <p>
      There is no variability.
    </p>

    <p>
      Every observation lies directly at the center.
    </p>

    <p>
      In this case,
      variance equals zero.
    </p>

    <p>
      As observations move farther from the mean,
      variance increases.
    </p>

    <h2>Deviation from the Mean</h2>

    <p>
      Variance begins by measuring how far each observation is from the mean.
    </p>

    <p>
      This difference is called a
      <strong>deviation</strong>.
    </p>

    <div class="example-box">

      <p>
        Deviation = Observation − Mean
      </p>

    </div>

    <p>
      Positive deviations occur above the mean.
    </p>

    <p>
      Negative deviations occur below the mean.
    </p>

    <h2>A Problem with Simple Deviations</h2>

    <p>
      Consider the dataset:
    </p>

    <div class="example-box">

      <p>
        4, 6, 8
      </p>

    </div>

    <p>
      The mean is:
    </p>

    0

    <p>
      The deviations are:
    </p>

    <div class="example-box">

      <p>
        -2, 0, +2
      </p>

    </div>

    <p>
      Adding them gives:
    </p>

    <div class="example-box">

      <p>
        -2 + 0 + 2 = 0
      </p>

    </div>

    <p>
      Positive and negative deviations always cancel.
    </p>

    <p>
      Therefore,
      simple deviations cannot measure variability directly.
    </p>

    <h2>Squaring the Deviations</h2>

    <p>
      To prevent cancellation,
      statisticians square each deviation.
    </p>

    <p>
      Squaring makes every value nonnegative.
    </p>

    <div class="example-box">

      <p>
        (-2)² = 4<br>
        0² = 0<br>
        (+2)² = 4
      </p>

    </div>

    <p>
      The squared deviations can now be combined meaningfully.
    </p>

    <h2>The Variance Formula</h2>

    <p>
      For a sample,
      variance is calculated as:
    </p>

    1

    <p>
      For a population,
      variance is:
    </p>

    2

    <h2>Sample Variance vs Population Variance</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Measure</th>
            <th>Symbol</th>
            <th>Denominator</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Sample Variance</td>
            <td>s²</td>
            <td>n − 1</td>
          </tr>

          <tr>
            <td>Population Variance</td>
            <td>σ²</td>
            <td>N</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Most introductory analyses use sample variance because data are usually collected from samples rather than entire populations.
    </p>

    <h2>A Step-by-Step Example</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        4, 6, 8
      </p>

    </div>

    <p>
      Mean:
    </p>

    <div class="example-box">

      <p>
        x̄ = 6
      </p>

    </div>

    <p>
      Deviations:
    </p>

    <div class="example-box">

      <p>
        -2, 0, 2
      </p>

    </div>

    <p>
      Squared deviations:
    </p>

    <div class="example-box">

      <p>
        4, 0, 4
      </p>

    </div>

    <p>
      Sum of squared deviations:
    </p>

    <div class="example-box">

      <p>
        8
      </p>

    </div>

    <p>
      Sample variance:
    </p>

    3

    <p>
      The variance equals 4.
    </p>

    <h2>Interpreting Variance</h2>

    <p>
      Larger variance indicates greater variability.
    </p>

    <p>
      Smaller variance indicates less variability.
    </p>

    <p>
      A variance of zero means all observations are identical.
    </p>

    <h2>The Unit Problem</h2>

    <p>
      One drawback of variance is that it uses squared units.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>Heights measured in meters produce variance in square meters</li>

      <li>Weights measured in kilograms produce variance in square kilograms</li>

      <li>Income measured in dollars produces variance in square dollars</li>

    </ul>

    <p>
      Squared units are often difficult to interpret directly.
    </p>

    <h2>Why Variance Is Still Important</h2>

    <p>
      Even though variance can be difficult to interpret,
      it is mathematically powerful.
    </p>

    <p>
      Many statistical procedures are built directly upon variance.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Standard deviation</li>

      <li>Confidence intervals</li>

      <li>Hypothesis testing</li>

      <li>ANOVA</li>

      <li>Regression analysis</li>

      <li>Machine learning algorithms</li>

    </ul>

    <h2>Variance Uses Every Observation</h2>

    <p>
      Unlike the range,
      variance uses information from every observation in the dataset.
    </p>

    <p>
      This makes it a more comprehensive measure of variability.
    </p>

    <p>
      However,
      it also means variance is sensitive to outliers.
    </p>

    <h2>The Effect of Outliers</h2>

    <p>
      Because deviations are squared,
      extreme observations receive extra weight.
    </p>

    <p>
      A large deviation becomes an even larger squared deviation.
    </p>

    <p>
      Consequently,
      outliers can substantially increase variance.
    </p>

    <div class="example-box">

      <strong>Important:</strong>

      <p>
        Variance is not resistant to outliers.
      </p>

    </div>

    <h2>Variance and Distribution Shape</h2>

    <p>
      Variance describes spread,
      not shape.
    </p>

    <p>
      Different distributions can have similar variances while exhibiting very different patterns.
    </p>

    <p>
      Variance should therefore be interpreted alongside graphs and other descriptive statistics.
    </p>

    <h2>Why Variance Matters</h2>

    <p>
      Variance is one of the foundational concepts in statistics.
    </p>

    <p>
      It provides the mathematical framework for understanding uncertainty,
      variability,
      and random behavior.
    </p>

    <p>
      Much of modern statistical theory is built upon variance.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Although variance is mathematically important,
      its squared units make interpretation difficult.
    </p>

    <p>
      The next lesson introduces
      <strong>standard deviation</strong>,
      which solves this problem by returning variability to the original units of measurement.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Variance measures the average squared distance from the mean</li>

        <li>Variance uses every observation in the dataset</li>

        <li>Sample variance is denoted by s²</li>

        <li>Population variance is denoted by σ²</li>

        <li>Variance equals zero only when all observations are identical</li>

        <li>Variance is sensitive to outliers</li>

        <li>Variance is one of the most important foundations of statistical theory</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/spread/interquartile-range/">
         ← Previous: Interquartile Range
      </a>

      <a class="btn"
         href="/descriptive/spread/standard-deviation/">
         Next: Standard Deviation →
      </a>

    </div>

  </div>

</section>