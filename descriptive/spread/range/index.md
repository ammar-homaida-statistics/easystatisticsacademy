---
layout: default
title: Range
description: Learn what the range is, how it measures variability, and why it provides the simplest summary of spread in a dataset.
permalink: /descriptive/spread/range/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_spread_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/spread/range/",
    label: "Range",
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
      <span class="badge">Range</span>
    </div>

    <h1>Range</h1>

    <p class="lead">
      The simplest measure of variability is the range.
    </p>

    <p class="lead">
      While measures such as variance and standard deviation provide detailed information,
      the range offers a quick summary of how far apart the smallest and largest observations are.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/spread/what-is-variability/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/spread/interquartile-range/">
         Next: Interquartile Range →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is the Range?</h2>

    <p>
      The <strong>range</strong>
      measures the total spread of a dataset.
    </p>

    <p>
      It is calculated as the difference between the largest observation and the smallest observation.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The range measures how far the data extend from the minimum value to the maximum value.
      </p>

    </div>

    <h2>The Formula</h2>

    <p>
      The range is calculated as:
    </p>

    0

    <p>
      Only two observations are needed:
    </p>

    <ul class="bullets">

      <li>The smallest value</li>

      <li>The largest value</li>

    </ul>

    <h2>A Simple Example</h2>

    <p>
      Consider the dataset:
    </p>

    <div class="example-box">

      <p>
        4, 6, 8, 10, 12
      </p>

    </div>

    <p>
      The smallest value is:
    </p>

    <div class="example-box">

      <p>
        4
      </p>

    </div>

    <p>
      The largest value is:
    </p>

    <div class="example-box">

      <p>
        12
      </p>

    </div>

    <p>
      Therefore:
    </p>

    1

    <p>
      The range equals 8.
    </p>

    <h2>Another Example</h2>

    <p>
      Suppose test scores are:
    </p>

    <div class="example-box">

      <p>
        65, 70, 75, 80, 95
      </p>

    </div>

    <p>
      The minimum score is 65.
    </p>

    <p>
      The maximum score is 95.
    </p>

    <p>
      Therefore:
    </p>

    2

    <p>
      The range is 30 points.
    </p>

    <h2>Interpreting the Range</h2>

    <p>
      A small range indicates that observations are relatively close together.
    </p>

    <p>
      A large range indicates that observations are spread farther apart.
    </p>

    <p>
      The range provides a rough measure of overall variability.
    </p>

    <h2>Range and Consistency</h2>

    <p>
      Consider two manufacturing processes.
    </p>

    <div class="grid grid-2">

      <div class="card">

        <h3>Process A</h3>

        <p>
          Range = 2 mm
        </p>

      </div>

      <div class="card">

        <h3>Process B</h3>

        <p>
          Range = 20 mm
        </p>

      </div>

    </div>

    <p>
      Process A produces much more consistent results.
    </p>

    <p>
      Process B exhibits greater variability.
    </p>

    <h2>The Range Uses Only Two Observations</h2>

    <p>
      One important characteristic of the range is that it ignores almost all observations.
    </p>

    <p>
      Only the smallest and largest values affect the calculation.
    </p>

    <p>
      Every other observation is ignored.
    </p>

    <h2>An Important Illustration</h2>

    <p>
      Consider these datasets:
    </p>

    <div class="grid grid-2">

      <div class="card">

        <h3>Dataset A</h3>

        <p>
          1, 2, 3, 4, 5
        </p>

      </div>

      <div class="card">

        <h3>Dataset B</h3>

        <p>
          1, 1, 1, 1, 5
        </p>

      </div>

    </div>

    <p>
      Both datasets have:
    </p>

    <ul class="bullets">

      <li>Minimum = 1</li>

      <li>Maximum = 5</li>

      <li>Range = 4</li>

    </ul>

    <p>
      Yet their distributions are clearly different.
    </p>

    <p>
      This shows that the range provides only limited information about variability.
    </p>

    <h2>Sensitivity to Outliers</h2>

    <p>
      The range is extremely sensitive to outliers.
    </p>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        10, 11, 12, 13, 14
      </p>

    </div>

    <p>
      The range is:
    </p>

    3

    <p>
      Now replace 14 with 100.
    </p>

    <div class="example-box">

      <p>
        10, 11, 12, 13, 100
      </p>

    </div>

    <p>
      The range becomes:
    </p>

    4

    <p>
      A single extreme observation changes the range dramatically.
    </p>

    <div class="example-box">

      <strong>Important:</strong>

      <p>
        The range is not resistant to outliers.
      </p>

    </div>

    <h2>Advantages of the Range</h2>

    <ul class="bullets">

      <li>Very easy to calculate</li>

      <li>Easy to interpret</li>

      <li>Provides a quick measure of spread</li>

      <li>Useful for preliminary exploration</li>

      <li>Requires only the minimum and maximum values</li>

    </ul>

    <h2>Limitations of the Range</h2>

    <ul class="bullets">

      <li>Uses only two observations</li>

      <li>Ignores most of the dataset</li>

      <li>Highly sensitive to outliers</li>

      <li>May provide a misleading picture of variability</li>

    </ul>

    <h2>Range and Different Data Types</h2>

    <p>
      The range requires numerical data because subtraction must be meaningful.
    </p>

    <p>
      Therefore,
      it is generally appropriate for:
    </p>

    <ul class="bullets">

      <li>Interval data</li>

      <li>Ratio data</li>

    </ul>

    <p>
      It is not meaningful for nominal categories.
    </p>

    <h2>Range in Everyday Life</h2>

    <p>
      The range appears frequently in everyday reporting.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Temperature ranges</li>

      <li>Price ranges</li>

      <li>Salary ranges</li>

      <li>Age ranges</li>

      <li>Score ranges</li>

    </ul>

    <p>
      People often use ranges as a quick summary of variability.
    </p>

    <h2>Why More Measures Are Needed</h2>

    <p>
      Although the range is useful,
      statisticians usually need more robust measures of spread.
    </p>

    <p>
      The range is too dependent on extreme observations.
    </p>

    <p>
      More sophisticated measures consider a larger portion of the dataset.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The next lesson introduces the
      <strong>Interquartile Range (IQR)</strong>,
      one of the most important resistant measures of variability.
    </p>

    <p>
      Unlike the range,
      the IQR focuses on the middle portion of the data and is much less affected by outliers.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The range equals the maximum value minus the minimum value</li>

        <li>The range measures the total spread of a dataset</li>

        <li>A larger range indicates greater variability</li>

        <li>The range uses only the smallest and largest observations</li>

        <li>The range is highly sensitive to outliers</li>

        <li>The range is easy to calculate and interpret</li>

        <li>More robust measures of spread are often needed for detailed analysis</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/spread/what-is-variability/">
         ← Previous: What Is Variability?
      </a>

      <a class="btn"
         href="/descriptive/spread/interquartile-range/">
         Next: Interquartile Range →
      </a>

    </div>

  </div>

</section>