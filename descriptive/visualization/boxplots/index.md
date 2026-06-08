---
layout: default
title: Boxplots
description: Learn how boxplots summarize distributions using the five-number summary and help identify spread, skewness, and outliers.
permalink: /descriptive/visualization/boxplots/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_visualization_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/visualization/boxplots/",
    label: "Boxplots",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 3</span>
      <span class="badge">Visualization</span>
      <span class="badge">Numerical Data</span>
    </div>

    <h1>Boxplots</h1>

    <p class="lead">
      Histograms show the overall shape of a distribution.
    </p>

    <p class="lead">
      Boxplots provide a compact summary of a distribution using only a few key numbers.
      They are especially useful for comparing groups,
      detecting outliers,
      and understanding the spread of data.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/visualization/density-curves/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/visualization/scatterplots/">
         Next: Scatterplots →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is a Boxplot?</h2>

    <p>
      A <strong>boxplot</strong>
      (also called a box-and-whisker plot)
      is a graphical summary of a numerical distribution.
    </p>

    <p>
      Rather than displaying every observation,
      it summarizes the data using key descriptive statistics.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        A boxplot compresses an entire distribution into a small visual summary.
      </p>

    </div>

    <h2>The Five-Number Summary</h2>

    <p>
      Boxplots are built from the
      <strong>five-number summary</strong>.
    </p>

    <p>
      These values describe the location and spread of the data.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Statistic</th>
            <th>Description</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Minimum</td>
            <td>Smallest observation</td>
          </tr>

          <tr>
            <td>Q1</td>
            <td>First quartile (25th percentile)</td>
          </tr>

          <tr>
            <td>Median</td>
            <td>50th percentile</td>
          </tr>

          <tr>
            <td>Q3</td>
            <td>Third quartile (75th percentile)</td>
          </tr>

          <tr>
            <td>Maximum</td>
            <td>Largest observation</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Understanding Quartiles</h2>

    <p>
      Quartiles divide ordered data into four equal parts.
    </p>

    <ul class="bullets">

      <li>25% of observations fall below Q1</li>

      <li>50% fall below the median</li>

      <li>75% fall below Q3</li>

    </ul>

    <p>
      These values help describe where observations are concentrated.
    </p>

    <h2>A Numerical Example</h2>

    <p>
      Consider the ordered dataset:
    </p>

    <div class="example-box">

      <p>
        5, 7, 8, 10, 12, 13, 15, 17, 20
      </p>

    </div>

    <p>
      The five-number summary is:
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Minimum</th>
            <th>Q1</th>
            <th>Median</th>
            <th>Q3</th>
            <th>Maximum</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>5</td>
            <td>7.5</td>
            <td>12</td>
            <td>16</td>
            <td>20</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      A boxplot visualizes these five values.
    </p>

    <h2>The Box</h2>

    <p>
      The box itself extends from:
    </p>

    <ul class="bullets">

      <li>Q1 (left side)</li>

      <li>Q3 (right side)</li>

    </ul>

    <p>
      This region contains the middle 50% of observations.
    </p>

    <p>
      The width of the box reflects the spread of the central portion of the data.
    </p>

    <h2>The Median Line</h2>

    <p>
      A line inside the box marks the median.
    </p>

    <p>
      This line divides the data into two equal halves.
    </p>

    <p>
      Its position can reveal asymmetry in the distribution.
    </p>

    <h2>The Whiskers</h2>

    <p>
      Lines extending from the box are called whiskers.
    </p>

    <p>
      They connect the box to observations outside the middle 50%.
    </p>

    <p>
      Whiskers help show the overall range of the data.
    </p>

    <h2>The Interquartile Range (IQR)</h2>

    <p>
      One of the most important measures in a boxplot is the
      <strong>interquartile range</strong>.
    </p>

    0

    <p>
      The IQR measures the spread of the middle 50% of observations.
    </p>

    <p>
      It is resistant to extreme values and widely used in statistics.
    </p>

    <h2>Detecting Outliers</h2>

    <p>
      Boxplots are famous for identifying outliers.
    </p>

    <p>
      A common rule classifies observations as potential outliers if they lie beyond:
    </p>

    1

    <p>
      Such observations are often displayed as individual points.
    </p>

    <h2>What Boxplots Reveal</h2>

    <p>
      Boxplots provide information about:
    </p>

    <ul class="bullets">

      <li>Center</li>

      <li>Spread</li>

      <li>Skewness</li>

      <li>Outliers</li>

      <li>Variability</li>

    </ul>

    <p>
      All of this information is displayed in a compact form.
    </p>

    <h2>Recognizing Skewness</h2>

    <p>
      A boxplot may suggest skewness when:
    </p>

    <ul class="bullets">

      <li>The median is not centered within the box</li>

      <li>One whisker is noticeably longer than the other</li>

      <li>Outliers appear mainly on one side</li>

    </ul>

    <p>
      These features help identify asymmetric distributions.
    </p>

    <h2>Comparing Groups</h2>

    <p>
      One of the greatest strengths of boxplots
      is comparing multiple distributions simultaneously.
    </p>

    <p>
      Example applications:
    </p>

    <ul class="bullets">

      <li>Exam scores across classrooms</li>

      <li>Income across regions</li>

      <li>Recovery times across treatments</li>

      <li>Sales across stores</li>

    </ul>

    <p>
      Multiple boxplots can reveal differences quickly.
    </p>

    <h2>Boxplots vs Histograms</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Boxplot</th>
            <th>Histogram</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Compact summary</td>
            <td>Detailed shape</td>
          </tr>

          <tr>
            <td>Five-number summary</td>
            <td>Distribution frequencies</td>
          </tr>

          <tr>
            <td>Good for comparisons</td>
            <td>Good for shape analysis</td>
          </tr>

          <tr>
            <td>Highlights outliers</td>
            <td>Shows clusters and peaks</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The two graphs complement one another.
    </p>

    <h2>Limitations of Boxplots</h2>

    <p>
      Boxplots do not show every feature of a distribution.
    </p>

    <p>
      For example,
      they may hide:
    </p>

    <ul class="bullets">

      <li>Multiple peaks</li>

      <li>Detailed distribution shape</li>

      <li>Small clusters</li>

    </ul>

    <p>
      Histograms often provide more detail,
      while boxplots provide greater simplicity.
    </p>

    <h2>Why Boxplots Are Important</h2>

    <p>
      Boxplots are widely used because they:
    </p>

    <ul class="bullets">

      <li>Summarize data efficiently</li>

      <li>Handle large datasets well</li>

      <li>Support group comparisons</li>

      <li>Highlight outliers</li>

      <li>Connect directly to descriptive statistics</li>

    </ul>

    <p>
      They are a standard tool throughout statistics and data science.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Boxplots summarize distributions using the five-number summary</li>

        <li>The box contains the middle 50% of observations</li>

        <li>The median is displayed inside the box</li>

        <li>The interquartile range measures central spread</li>

        <li>Boxplots are useful for identifying outliers</li>

        <li>They are excellent for comparing multiple groups</li>

        <li>Boxplots complement histograms rather than replace them</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/visualization/density-curves/">
         ← Previous: Density Curves
      </a>

      <a class="btn"
         href="/descriptive/visualization/scatterplots/">
         Next: Scatterplots →
      </a>

    </div>

  </div>

</section>