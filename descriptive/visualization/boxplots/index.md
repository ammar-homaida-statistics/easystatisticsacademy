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

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Boxplots summarize distributions using only a few numbers,
    making them much more compact than histograms.
  </p>

</div>

<img src="{{ 'descriptive/images/boxplot-anatomy.png' | relative_url }}"
     alt="Anatomy of a boxplot"
     style="margin-top:15px; max-width:100%; height:auto;">

    <h2>The Five-Number Summary</h2>

    <p>
      Boxplots are built from the
      <strong>five-number summary</strong>.
    </p>

    <p>
      These values describe the location and spread of the data.
    </p>

    <p>
  Because quartiles divide the data into four equal parts,
  the interval from Q1 to Q3 always contains the middle 50%
  of observations.
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

    <img src="{{ 'descriptive/images/five-number-summary-boxplot.png' | relative_url }}"
     alt="Five-number summary visualized with a boxplot"
     style="margin-top:15px; max-width:100%; height:auto;">

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

    <p>
  Because quartiles divide the data into four equal parts,
  the interval from Q1 to Q3 always contains the middle 50%
  of observations.
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

    <p>
  In many boxplots, whiskers extend only to the most extreme
  non-outlier observations rather than to the absolute minimum
  and maximum values.
</p>

    <h2>The Interquartile Range (IQR)</h2>

    <p>
      One of the most important measures in a boxplot is the
      <strong>interquartile range</strong>.
    </p>

    <p>
  The IQR measures the distance between the first and third quartiles,
  capturing the spread of the middle 50% of observations.
</p>

    <p>
      The IQR measures the spread of the middle 50% of observations.
    </p>

    <p>
      It is resistant to extreme values and widely used in statistics.
    </p>

    <h2>Detecting Outliers</h2>

    <img src="{{ 'descriptive/images/boxplot-outlier-example.png' | relative_url }}"
     alt="Boxplot showing an outlier"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      Boxplots are famous for identifying outliers.
    </p>

    <p>
      A common rule classifies observations as potential outliers if they lie beyond:
    </p>

    <p>
  Observations outside these boundaries are commonly flagged
  as potential outliers.
</p>

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

    <img src="{{ 'descriptive/images/symmetric-vs-skewed-boxplots.png' | relative_url }}"
     alt="Symmetric and skewed boxplots"
     style="margin-top:15px; max-width:100%; height:auto;">

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

    <img src="{{ 'descriptive/images/group-comparison-boxplots.png' | relative_url }}"
     alt="Comparing groups using boxplots"
     style="margin-top:15px; max-width:100%; height:auto;">

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

    <p>
  Comparing several boxplots side by side is often easier
  than comparing several histograms.
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

    <h2>Histograms and Boxplots Together</h2>

    <img src="{{ 'descriptive/images/histogram-vs-boxplot.png' | relative_url }}"
     alt="Histogram and boxplot comparison"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
  Analysts often examine both a histogram and a boxplot
  for the same dataset.
</p>

<p>
  The histogram reveals detailed shape,
  while the boxplot provides a compact summary.
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

    <div class="concept-box">

  <strong>Key insight:</strong>

  <p>
    Boxplots summarize center, spread, and potential outliers
    in a compact visual form, making them especially useful
    for comparing groups.
  </p>

</div>

<h2>Creating Boxplots in SPSS</h2>

<ul class="bullets">

  <li>Graphs → Chart Builder</li>

  <li>Select Boxplot</li>

  <li>Assign the numerical variable</li>

  <li>SPSS automatically identifies potential outliers</li>

</ul>

<div style="flex:1; min-width:300px;">
    <img src="{{ '/descriptive/images/spss_boxplot_output.png' | relative_url }}"
         alt="SPSS boxplot output"
         style="width:100%; height:auto;">
    <p style="text-align:center;">
      Boxplot showing spread and potential outlier
    </p>
  </div>

<p>
  Boxplots are commonly used as an initial screening tool
  during exploratory data analysis.
</p>

<h3>Python Example</h3>

<p>
This example creates a boxplot for numerical data.
</p>

<pre><code>import matplotlib.pyplot as plt

scores = [55,58,60,62,65,67,68,70,
          72,74,75,77,80,82,85,
          88,90,92,95,120]

plt.boxplot(scores)

plt.show()
</code></pre>

<h3>R Example</h3>

<p>
This example creates a boxplot for numerical data.
</p>

<pre><code>scores <- c(55,58,60,62,65,67,68,70,
            72,74,75,77,80,82,85,
            88,90,92,95,120)

boxplot(scores)
</code></pre>

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
