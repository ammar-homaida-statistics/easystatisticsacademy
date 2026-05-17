---
layout: default
title: Frequency Tables
description: Learn how frequency tables summarize data distributions and why they are one of the most important tools in descriptive statistics.
permalink: /descriptive/tabular-summaries/frequency-tables/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_tabular_summaries_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/tabular-summaries/frequency-tables/",
    label: "Frequency Tables",
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
      <span class="badge">Frequency Analysis</span>
      <span class="badge">Tabular Summaries</span>
    </div>

    <h1>Frequency Tables</h1>

    <p class="lead">
      One of the first ways statisticians summarize data
      is by counting how often values occur.
    </p>

    <p class="lead">
      Frequency tables organize observations into categories or values
      and display how frequently each appears in the dataset.
      They are foundational tools in descriptive statistics.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/tabular-summaries/why-tables-come-first/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/tabular-summaries/relative-frequency-and-percent/">
         Next: Relative Frequency and Percent →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->
<section class="section">

  <div class="content-narrow">

    <h2>What Is a Frequency?</h2>

    <p>
      A <strong>frequency</strong>
      is simply the number of times a value or category appears.
    </p>

    <p>
      Example:
    </p>

    <p>
      Suppose we record favorite drinks:
    </p>

    <div class="example-box">

      <p>
        Coffee, Tea, Coffee, Juice, Tea,
        Coffee, Water, Coffee
      </p>

    </div>

    <p>
Spreadsheet software such as Excel can create frequency summaries
using functions like COUNTIF().
</p>

    <p>
      We can count how often each category occurs.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Drink</th>
            <th>Frequency</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Coffee</td>
            <td>4</td>
          </tr>

          <tr>
            <td>Tea</td>
            <td>2</td>
          </tr>

          <tr>
            <td>Juice</td>
            <td>1</td>
          </tr>

          <tr>
            <td>Water</td>
            <td>1</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This is a frequency table.
    </p>

    <p>
  These counts are called <strong>absolute frequencies</strong>
  because they represent raw numbers of occurrences.
</p>

    <h2>What Is a Frequency Table?</h2>

    <p>
      A <strong>frequency table</strong>
      summarizes how often values or categories occur in a dataset.
    </p>

    <p>
  In descriptive statistics,
  frequency tables provide one of the simplest representations
  of an empirical distribution.
</p>

    <p>
      Frequency tables:
    </p>

    <ul class="bullets">
      <li>Reduce raw data complexity</li>
      <li>Reveal patterns quickly</li>
      <li>Show concentration and imbalance</li>
      <li>Prepare data for graphs and analysis</li>
    </ul>

    <img src="{{ 'descriptive/images/raw-to-frequency-table.png' | relative_url }}" 
     alt="Raw observations transformed into a frequency table" 
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Frequency tables organize repeated observations into structured summaries.
</p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Frequency tables transform raw observations
        into organized distributions.
      </p>

    </div>

    <h2>Frequency Tables for Categorical Variables</h2>

    <p>
      Frequency tables are especially useful
      for categorical data.
    </p>

    <p>
      Example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Blood Type</th>
            <th>Frequency</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>A</td>
            <td>32</td>
          </tr>

          <tr>
            <td>B</td>
            <td>18</td>
          </tr>

          <tr>
            <td>AB</td>
            <td>7</td>
          </tr>

          <tr>
            <td>O</td>
            <td>43</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The table immediately reveals
the distribution of blood types in the sample.
    </p>

    <h2>Frequency Tables for Numerical Variables</h2>

    <p>
      Frequency tables can also summarize numerical data.
    </p>

    <p>
      Example:
    </p>

    <div class="example-box">

      <p>
        Number of children per household:
      </p>

      <p>
        0, 1, 2, 2, 3, 1, 0, 2, 1, 4
      </p>

    </div>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Children</th>
            <th>Frequency</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0</td>
            <td>2</td>
          </tr>

          <tr>
            <td>1</td>
            <td>3</td>
          </tr>

          <tr>
            <td>2</td>
            <td>3</td>
          </tr>

          <tr>
            <td>3</td>
            <td>1</td>
          </tr>

          <tr>
            <td>4</td>
            <td>1</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This table summarizes the distribution of counts.
    </p>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Frequency tables transform individual observations
    into structured summaries of how data is distributed.
  </p>

</div>

    <h2>Frequency Tables Reveal Distribution Shape</h2>

    <p>
      Frequency tables help identify:
    </p>

    <ul class="bullets">
      <li>Common values</li>
      <li>Rare values</li>
      <li>Concentration of observations</li>
      <li>Potential outliers</li>
      <li>Distribution shape</li>
    </ul>

    <p>
      Even before creating graphs,
      frequency tables provide important insight.
    </p>

    <h2>Grouped Frequency Tables</h2>

    <p>
      When datasets become large,
      listing every distinct value becomes impractical.
    </p>

    <p>
      Values are then grouped into intervals.
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

    <img src="{{ 'descriptive/images/grouped-frequency-histogram.png' | relative_url }}" 
     alt="Grouped frequency table and histogram" 
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Grouped frequency tables are closely connected to histograms.
</p>

    <p>
      Grouping reduces complexity
and makes large numerical datasets easier to interpret.
    </p>

    <h2>Frequency Tables Help Detect Problems</h2>

    <p>
      Frequency tables are also useful
      for checking data quality.
    </p>

    <p>
      They may reveal:
    </p>

    <ul class="bullets">
      <li>Impossible values</li>
      <li>Typing errors</li>
      <li>Unexpected categories</li>
      <li>Missing observations</li>
      <li>Extreme imbalance</li>
    </ul>

    <p>
      Exploratory analysis often begins with frequency inspection.
    </p>

    <h2>Frequency Tables Prepare Data for Visualization</h2>

    <p>
      Many statistical graphs are based directly on frequency tables.
    </p>

    <p>
      Examples:
    </p>

    <ul class="bullets">
      <li>Bar charts</li>
      <li>Histograms</li>
      <li>Pie charts</li>
      <li>Frequency polygons</li>
    </ul>

    <img src="{{ 'descriptive/images/frequency-table-to-bar-chart.png' | relative_url }}" 
     alt="Frequency table converted into a bar chart" 
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Bar charts are often constructed directly from frequency tables.
</p>

    <p>
      Frequency tables often serve
      as the foundation for visual analysis.
    </p>

    <h2>Frequency Does Not Always Mean Importance</h2>

    <p>
      A category appearing frequently
      is not automatically more important.
    </p>

    <p>
      Frequency only describes occurrence,
      not value or significance.
    </p>

    <p>
      Interpretation always depends on context.
    </p>

    <h2>Frequency Tables Are Everywhere in Statistics</h2>

    <p>
      Frequency summaries appear throughout:
    </p>

    <ul class="bullets">
      <li>Survey analysis</li>
      <li>Clinical studies</li>
      <li>Business analytics</li>
      <li>Machine learning preprocessing</li>
      <li>Exploratory data analysis</li>
      <li>Quality control</li>
    </ul>

    <p>
      They are among the most fundamental descriptive tools.
    </p>

    <div class="concept-box">

  <strong>Key insight:</strong>

  <p>
    Frequency analysis is one of the first steps
    in understanding how data is distributed,
    concentrated,
    and structured.
  </p>

</div>

<div class="concept-box">

<strong>In practice:</strong>

<p>
In SPSS, frequency tables are commonly generated using:
</p>

<ul class="bullets">
  <li>Analyze → Descriptive Statistics → Frequencies</li>
</ul>

</div>

<h3>R Example</h3>

<p>
This example creates a frequency table.
</p>

<pre><code>drinks <- c("Coffee", "Tea", "Coffee")

table(drinks)
</code></pre>

<img src="{{ 'descriptive/images/R_Output_frequency tables_Coffee_Tea.png' | relative_url }}" 
     style="margin-top:15px; max-width:100%; height:auto;">

    <!-- TAKEAWAYS -->
    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Frequency means the number of occurrences of a value or category</li>

        <li>Frequency tables organize distributions into understandable summaries</li>

        <li>They are useful for both categorical and numerical data</li>

        <li>Frequency tables reveal patterns and concentration</li>

        <li>Grouped frequency tables simplify large datasets</li>

        <li>Frequency analysis helps detect data quality issues</li>

        <li>Many statistical graphs are built from frequency tables</li>

      </ul>

    </div>

    <!-- NAVIGATION -->
    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/tabular-summaries/why-tables-come-first/">
         ← Previous: Why Tables Come First
      </a>

      <a class="btn"
         href="/descriptive/tabular-summaries/relative-frequency-and-percent/">
         Next: Relative Frequency and Percent →
      </a>

    </div>

  </div>

</section>
