---
layout: default
title: Handling Missing Values
description: Learn what missing data is, why it occurs, how it affects analysis, and how statisticians report and summarize missing values.
permalink: /descriptive/tabular-summaries/handling-missing-values/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_tabular_summaries_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/tabular-summaries/handling-missing-values/",
    label: "Handling Missing Values",
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
      <span class="badge">Data Quality</span>
      <span class="badge">Missing Data</span>
    </div>

    <h1>Handling Missing Values</h1>

    <p class="lead">
      Real-world datasets are rarely complete.
    </p>

    <p class="lead">
      Missing values occur in surveys,
      experiments,
      medical studies,
      business databases,
      and almost every form of data collection.
      Understanding how to identify and report missing data is an essential statistical skill.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/tabular-summaries/choosing-the-right-percentage/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/tabular-summaries/standard-table-layout-and-reporting/">
         Next: Standard Table Layout and Reporting
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->
<section class="section">

  <div class="content-narrow">

    <h2>What Is a Missing Value?</h2>

    <p>
      A <strong>missing value</strong>
      occurs when information that should exist for an observation
      is unavailable.
    </p>

    <p>
      Instead of a recorded value,
      the dataset contains a blank,
      a special code,
      or a missing-data indicator.
    </p>

    <p>
      Example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Participant</th>
            <th>Age</th>
            <th>Income</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>P01</td>
            <td>32</td>
            <td>4200</td>
          </tr>

          <tr>
            <td>P02</td>
            <td>29</td>
            <td>Missing</td>
          </tr>

          <tr>
            <td>P03</td>
            <td>41</td>
            <td>5100</td>
          </tr>

        </tbody>

      </table>

    </div>

    <img src="{{ 'descriptive/images/complete-vs-missing-data.png' | relative_url }}"
     alt="Complete versus missing data"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Missing values create gaps in otherwise complete datasets.
</p>

    <p>
      Participant P02 did not provide income information.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Missing data means information is unavailable,
        not that the value equals zero.
      </p>

    </div>

    <p>
  Missing values represent uncertainty about the true value,
  not the absence of a value.
</p>

    <h2>Why Do Missing Values Occur?</h2>

    <p>
      Missing values arise for many reasons.
    </p>

    <ul class="bullets">

      <li>Survey questions skipped by participants</li>

      <li>Data entry errors</li>

      <li>Measurement failures</li>

      <li>Equipment malfunctions</li>

      <li>Lost records</li>

      <li>Participant dropout</li>

      <li>Privacy concerns</li>

    </ul>

    <p>
      Missingness is a natural part of real-world data collection.
    </p>

    <h2>Missing Values Are Not Zeros</h2>

    <p>
      One of the most common mistakes is treating missing values as zero.
    </p>

    <p>
      Example:
    </p>

    <ul class="bullets">
      <li>Missing income ≠ $0 income</li>
      <li>Missing age ≠ 0 years old</li>
      <li>Missing blood pressure ≠ 0 mmHg</li>
    </ul>

    <img src="{{ 'descriptive/images/missing-vs-zero.png' | relative_url }}"
     alt="Missing values versus zero values"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
A value of zero contains information.
A missing value indicates unknown information.
</p>

    <p>
      A missing value means the true value is unknown.
    </p>

    <div class="example-box">

      <strong>Important:</strong>

      <p>
        Unknown and zero are fundamentally different concepts.
      </p>

    </div>

    <h2>How Missing Data Appears in Datasets</h2>

    <p>
      Different software packages use different representations.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Representation</th>
            <th>Example</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Blank cell</td>
            <td>(empty)</td>
          </tr>

          <tr>
            <td>NA</td>
            <td>NA</td>
          </tr>

          <tr>
            <td>NULL</td>
            <td>NULL</td>
          </tr>

          <tr>
            <td>Special code</td>
            <td>-99 or 999</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Analysts must understand how missing values are coded
      before performing calculations.
    </p>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Missing data affects not only the amount of information available,
    but also the reliability of conclusions drawn from the data.
  </p>

</div>

    <h2>Why Missing Data Matters</h2>

    <p>
      Missing values can affect:
    </p>

    <ul class="bullets">

      <li>Means</li>

      <li>Percentages</li>

      <li>Correlations</li>

      <li>Regression models</li>

      <li>Statistical tests</li>

      <li>Machine learning algorithms</li>

    </ul>

    <p>
      Ignoring missing values may produce misleading conclusions.
    </p>

    <h2>Example: Effect on a Mean</h2>

    <p>
      Consider the following incomes:
    </p>

    <div class="example-box">

      <p>
        3000, 3500, 4000, Missing
      </p>

    </div>

    <p>
      The mean should be calculated from the available values:
    </p>

    <div class="formula-box">
Mean = (3000 + 3500 + 4000) / 3 = 3500
</div>

    <p>
      Treating the missing value as zero would create an incorrect result.
    </p>

    <h2>Reporting Missing Values</h2>

    <p>
      Good statistical practice requires reporting missing data explicitly.
    </p>

    <p>
      Example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Variable</th>
            <th>Valid Responses</th>
            <th>Missing Responses</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Age</td>
            <td>195</td>
            <td>5</td>
          </tr>

          <tr>
            <td>Income</td>
            <td>180</td>
            <td>20</td>
          </tr>

          <tr>
            <td>Education</td>
            <td>198</td>
            <td>2</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Reporting missingness improves transparency.
    </p>

    <p>
  For example, 20 missing income responses out of 200 participants
  corresponds to 10% missing data.
</p>

    <h2>Frequency Tables and Missing Values</h2>

    <p>
      Many statistical software packages provide two options:
    </p>

    <ul class="bullets">

      <li>Exclude missing values from calculations</li>

      <li>Display missing values as a separate category</li>

    </ul>

    <p>
      Example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Response</th>
            <th>Frequency</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Yes</td>
            <td>120</td>
          </tr>

          <tr>
            <td>No</td>
            <td>65</td>
          </tr>

          <tr>
            <td>Missing</td>
            <td>15</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Including a missing category often helps assess data quality.
    </p>

    <p>
  However, missing values should generally not be treated
  as a meaningful response category unless there is a clear reason to do so.
</p>

    <h2>Missing Data Can Signal Problems</h2>

    <p>
      High levels of missing data may indicate:
    </p>

    <ul class="bullets">

      <li>Poor survey design</li>

      <li>Confusing questions</li>

      <li>Data collection issues</li>

      <li>Technical failures</li>

      <li>Participant reluctance</li>

    </ul>

    <p>
      Missingness itself can sometimes provide useful information.
    </p>

    <h2>Descriptive Statistics Comes First</h2>

    <p>
      Before applying advanced methods,
      analysts should always examine:
    </p>

    <ul class="bullets">

      <li>How much data is missing</li>

      <li>Which variables contain missing values</li>

      <li>Whether missingness appears systematic</li>

    </ul>

    <p>
      This is an important part of exploratory data analysis.
    </p>

    <h2>Modern Software Handles Missing Values Automatically</h2>

    <p>
      Programs such as:
    </p>

    <ul class="bullets">

      <li>SPSS</li>

      <li>R</li>

      <li>Python</li>

      <li>Excel</li>

      <li>SAS</li>

      <li>Stata</li>

    </ul>

    <p>
      include tools for identifying and handling missing data.
    </p>

    <p>
      However,
      understanding the concept remains more important than knowing the software commands.
    </p>

    <h2>Good Statistical Practice</h2>

    <p>
      Missing values should never be ignored blindly.
    </p>

    <p>
      Analysts should:
    </p>

    <ul class="bullets">

      <li>Identify missing values</li>

      <li>Report them clearly</li>

      <li>Understand why they occur</li>

      <li>Assess their potential impact</li>

    </ul>

    <p>
      Transparency about missing data is a hallmark of good statistical reporting.
    </p>

    <div class="concept-box">

  <strong>Key insight:</strong>

  <p>
    Before analyzing a dataset,
    always understand how much information is missing
    and where that missingness occurs.
  </p>

</div>

<h3>Python Example</h3>

<p>
This example counts missing values in a dataset.
</p>

<pre><code>import pandas as pd

data = pd.Series([25, 30, None, 28, None, 35])

data.isna().sum()
</code></pre>

<h3>R Example</h3>

<p>
This example counts missing values in a dataset.
</p>

<pre><code>x <- c(25, 30, NA, 28, NA, 35)

sum(is.na(x))
</code></pre>

    <!-- TAKEAWAYS -->
    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Missing values occur when information is unavailable</li>

        <li>Missing data is not the same as zero</li>

        <li>Missingness can arise from many sources</li>

        <li>Missing values can affect statistical summaries and conclusions</li>

        <li>Good practice requires reporting missing values explicitly</li>

        <li>Frequency tables can include missing values as a separate category</li>

        <li>Examining missingness is an important part of descriptive analysis</li>

      </ul>

    </div>

    <!-- NAVIGATION -->
    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/tabular-summaries/choosing-the-right-percentage/">
         ← Previous: Choosing the Right Percentage
      </a>

      <a class="btn"
         href="/descriptive/tabular-summaries/standard-table-layout-and-reporting/">
         Next: Standard Table Layout and Reporting →
      </a>

    </div>

  </div>

</section>
