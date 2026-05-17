---
layout: default
title: Grouped Frequency Tables
description: Learn how grouped frequency tables summarize large numerical datasets using intervals and class groupings.
permalink: /descriptive/tabular-summaries/grouped-frequency-tables/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_tabular_summaries_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/tabular-summaries/grouped-frequency-tables/",
    label: "Grouped Frequency Tables",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->
<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 2</span>
      <span class="badge">Grouped Data</span>
      <span class="badge">Tabular Summaries</span>
    </div>

    <h1>Grouped Frequency Tables</h1>

    <p class="lead">
      Large numerical datasets are often difficult to summarize using individual values.
    </p>

    <p class="lead">
      Grouped frequency tables organize numerical observations into intervals,
      making distributions easier to interpret and visualize.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/tabular-summaries/relative-frequency-and-percent/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/tabular-summaries/cumulative-frequency/">
         Next: Cumulative Frequency
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->
<section class="section">

  <div class="content-narrow">

    <h2>Why Group Data?</h2>

    <p>
      Small datasets can often be summarized directly.
    </p>

    <p>
      But when numerical datasets become large,
      listing every distinct value becomes impractical.
    </p>

    <p>
      Example:
    </p>

    <div class="example-box">

      <p>
        58, 61, 63, 65, 67, 68, 69, 70, 71,
        72, 73, 74, 74, 75, 76, 77, 78...
      </p>

    </div>

    <p>
      Even moderate-sized datasets quickly become difficult to interpret directly.
    </p>

    <p>
      Grouping values into intervals simplifies interpretation.
    </p>

    <img src="{{ 'descriptive/images/raw-to-grouped-table.png' | relative_url }}" 
     alt="Raw numerical data transformed into grouped intervals" 
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Grouping transforms long lists of numerical observations
into compact interval summaries.
</p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Grouped frequency tables summarize ranges of values instead of individual observations.
      </p>

    </div>

    <h2>What Is a Grouped Frequency Table?</h2>

    <p>
      A <strong>grouped frequency table</strong>
      organizes numerical data into intervals called classes.
    </p>

    <p>
      Instead of counting each value separately,
      we count how many observations fall inside each interval.
    </p>

    <p>
  Grouping creates an approximate summary
  of the underlying numerical distribution.
</p>

    <p>
      Example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Exam Score Interval</th>
            <th>Frequency</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>50–59</td>
            <td>4</td>
          </tr>

          <tr>
            <td>60–69</td>
            <td>9</td>
          </tr>

          <tr>
            <td>70–79</td>
            <td>15</td>
          </tr>

          <tr>
            <td>80–89</td>
            <td>11</td>
          </tr>

          <tr>
            <td>90–99</td>
            <td>3</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This table provides a compact summary
      of the distribution of exam scores.
    </p>

    <h2>Understanding Class Intervals</h2>

    <p>
      Each interval is called a <strong>class</strong>.
    </p>

    <p>
      Example:
    </p>

    <ul class="bullets">
      <li>50–59</li>
      <li>60–69</li>
      <li>70–79</li>
    </ul>

    <p>
      These intervals divide the dataset into ranges.
    </p>

    <p>
      Every observation belongs to exactly one class.
    </p>

    <h2>Class Width</h2>

    <p>
      The size of each interval is called the <strong>class width</strong>.
    </p>

    <p>
      Formula:
    </p>

    <p>
  Formula:
</p>

<div class="formula-box">
  Class Width = Upper Class Boundary − Lower Class Boundary
</div>

    <p>
      Example:
    </p>

    <ul class="bullets">
      <li>70–79 → width ≈ 10</li>
      <li>80–89 → width ≈ 10</li>
    </ul>

    <p>
      Consistent class widths usually improve readability.
    </p>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Grouping transforms large collections of raw numerical values
    into interpretable distribution patterns.
  </p>

</div>

    <h2>Why Grouping Helps</h2>

    <p>
      Grouped frequency tables:
    </p>

    <ul class="bullets">
      <li>Reduce complexity</li>
      <li>Reveal distribution shape</li>
      <li>Show concentration of observations</li>
      <li>Prepare data for histograms</li>
      <li>Improve readability for large datasets</li>
    </ul>

    <p>
      They help analysts understand large numerical distributions quickly.
    </p>

    <h2>Grouped vs Ungrouped Tables</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Ungrouped Table</th>
            <th>Grouped Table</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Lists individual values</td>
            <td>Lists intervals</td>
          </tr>

          <tr>
            <td>Useful for small datasets</td>
            <td>Useful for large datasets</td>
          </tr>

          <tr>
            <td>More detailed</td>
            <td>More compact</td>
          </tr>

          <tr>
            <td>Can become cluttered</td>
            <td>Easier to summarize visually</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Choosing Appropriate Intervals</h2>

    <p>
      Interval choice affects interpretation.
    </p>

    <p>
      Too many intervals:
    </p>

    <ul class="bullets">
      <li>Creates unnecessary detail</li>
      <li>Makes patterns harder to see</li>
    </ul>

    <p>
      Too few intervals:
    </p>

    <ul class="bullets">
      <li>Oversimplifies the data</li>
      <li>Hides important variation</li>
    </ul>

    <p>
      Good grouping balances clarity and detail.
    </p>

    <img src="{{ 'descriptive/images/too-many-vs-too-few-bins.png' | relative_url }}" 
     alt="Too many versus too few grouping intervals" 
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Interval choice strongly influences how distributions appear.
</p>

    <h2>Example: Heights of Students</h2>

    <p>
      Suppose student heights are grouped as:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Height (cm)</th>
            <th>Frequency</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>150–159</td>
            <td>5</td>
          </tr>

          <tr>
            <td>160–169</td>
            <td>14</td>
          </tr>

          <tr>
            <td>170–179</td>
            <td>18</td>
          </tr>

          <tr>
            <td>180–189</td>
            <td>7</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The grouped distribution suggests
that observations are concentrated
between 160 cm and 179 cm.
    </p>

    <h2>Grouped Tables Lose Some Detail</h2>

    <p>
      Grouping simplifies interpretation,
      but it also reduces precision.
    </p>

    <p>
      We no longer know exact individual values.
    </p>

    <p>
      Example:
    </p>

    <ul class="bullets">
      <li>We know a student is in 170–179 cm</li>
      <li>We do not know the exact height</li>
    </ul>

    <p>
      Grouping trades detail for simplicity.
    </p>

    <p>
  Grouping can also smooth out small variations
  and make distributions appear more regular.
</p>

    <h2>Grouped Tables Connect Directly to Histograms</h2>

    <p>
      Histograms are graphical representations
      of grouped frequency tables.
    </p>

    <p>
      Each interval becomes a bar,
      and bar height represents frequency.
    </p>

    <p>
  Histograms therefore visualize
  the grouped structure of numerical distributions.
</p>

    <p>
      Understanding grouped tables therefore helps interpret histograms later.
    </p>

    <img src="{{ 'descriptive/images/grouped-table-to-histogram.png' | relative_url }}" 
     alt="Grouped frequency table connected to histogram" 
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Histograms visualize grouped frequency distributions using adjacent bars.
</p>

    <h2>Grouped Frequency Tables Are Common in Statistics</h2>

    <p>
      Grouped summaries appear frequently in:
    </p>

    <ul class="bullets">
      <li>Survey analysis</li>
      <li>Educational testing</li>
      <li>Public health reporting</li>
      <li>Economic statistics</li>
      <li>Quality control</li>
      <li>Scientific measurement</li>
    </ul>

    <p>
      They are fundamental tools in exploratory data analysis.
    </p>

    <div class="concept-box">

  <strong>Key insight:</strong>

  <p>
    Grouped frequency tables simplify large numerical datasets
    by approximating distributions through interval structure.
  </p>

</div>

<div class="concept-box">

<strong>In practice:</strong>

<p>
SPSS histograms and grouped frequency summaries
automatically organize numerical values into intervals.
</p>

</div>

<p>
Spreadsheet software such as Excel can group numerical values into bins for histogram creation.
</p>

<h3>Python Example</h3>

<p>
This example creates grouped intervals using a histogram.
</p>

<pre><code>import matplotlib.pyplot as plt

plt.hist(scores, bins=5)
</code></pre>

<h3>R Example</h3>

<p>
This example creates grouped intervals using a histogram.
</p>

<pre><code>hist(scores, breaks = 5)
</code></pre>

    <!-- TAKEAWAYS -->
    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Grouped frequency tables summarize numerical data using intervals</li>

        <li>Intervals are called classes</li>

        <li>Grouping simplifies interpretation of large datasets</li>

        <li>Class width influences readability and interpretation</li>

        <li>Grouped tables reveal distribution patterns and concentration</li>

        <li>Grouping reduces detail but improves clarity</li>

        <li>Histograms are based directly on grouped frequency tables</li>

      </ul>

    </div>

    <!-- NAVIGATION -->
    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/tabular-summaries/relative-frequency-and-percent/">
         ← Previous: Relative Frequency and Percent
      </a>

      <a class="btn"
         href="/descriptive/tabular-summaries/cumulative-frequency/">
         Next: Cumulative Frequency →
      </a>

    </div>

  </div>

</section>
