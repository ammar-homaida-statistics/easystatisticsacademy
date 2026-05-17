---
layout: default
title: Relative Frequency and Percent
description: Learn how relative frequencies and percentages standardize frequency counts and improve interpretation of statistical distributions.
permalink: /descriptive/tabular-summaries/relative-frequency-and-percent/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_tabular_summaries_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/tabular-summaries/relative-frequency-and-percent/",
    label: "Relative Frequency and Percent",
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
      <span class="badge">Percentages</span>
    </div>

    <h1>Relative Frequency and Percent</h1>

    <p class="lead">
      Raw counts alone are often not enough for interpretation.
    </p>

    <p class="lead">
      Relative frequencies and percentages standardize frequencies,
      allowing us to compare categories and datasets more meaningfully,
      even when sample sizes differ.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/tabular-summaries/frequency-tables/">
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

    <h2>Why Raw Frequencies Can Be Misleading</h2>

    <p>
      Frequency tables show how many times values occur,
      but raw counts depend heavily on sample size.
    </p>

    <p>
      Example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Class</th>
            <th>Students Passing</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Class A</td>
            <td>40</td>
          </tr>

          <tr>
            <td>Class B</td>
            <td>80</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      At first glance,
      Class B appears better.
    </p>

    <p>
      But suppose:
    </p>

    <ul class="bullets">
      <li>Class A has 50 students</li>
      <li>Class B has 200 students</li>
    </ul>

    <p>
      Then:
    </p>

    <ul class="bullets">
      <li>Class A pass rate = 80%</li>
      <li>Class B pass rate = 40%</li>
    </ul>

    <p>
      Considering relative frequency completely changes the interpretation.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Relative frequency standardizes counts by sample size.
      </p>

    </div>

    <img src="{{ 'descriptive/images/raw-vs-relative-frequency.png' | relative_url }}" 
     alt="Raw counts versus relative frequencies" 
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Relative frequencies standardize counts,
allowing fair comparisons across different sample sizes.
</p>

    <h2>What Is Relative Frequency?</h2>

    <p>
      <strong>Relative frequency</strong>
      describes the proportion of observations
      belonging to a category or value.
    </p>

    <p>
  Relative frequency can be viewed
  as an empirical estimate of probability.
</p>

    <p>
      Formula:
    </p>

    <div class="formula-box">
  Relative Frequency =
  <span class="fraction">
    Frequency / Total Number of Observations
  </span>
</div>

    <p>
      Relative frequencies range between:
    </p>

    <ul class="bullets">
      <li>0</li>
      <li>1</li>
    </ul>

    <p>
      because they represent proportions.
    </p>

    <img src="{{ 'descriptive/images/frequency-to-relative-frequency.png' | relative_url }}" 
     alt="Converting frequencies into relative frequencies" 
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Relative frequency converts raw counts into proportions of the total sample.
</p>

    <h2>Example Calculation</h2>

    <p>
      Suppose we survey 20 students
      about preferred operating systems:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Operating System</th>
            <th>Frequency</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Windows</td>
            <td>12</td>
          </tr>

          <tr>
            <td>macOS</td>
            <td>5</td>
          </tr>

          <tr>
            <td>Linux</td>
            <td>3</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Relative frequencies:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Operating System</th>
            <th>Relative Frequency</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Windows</td>
            <td>12 / 20 = 0.60</td>
          </tr>

          <tr>
            <td>macOS</td>
            <td>5 / 20 = 0.25</td>
          </tr>

          <tr>
            <td>Linux</td>
            <td>3 / 20 = 0.15</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      These proportions are easier to compare than raw counts alone.
    </p>

    <h2>What Is Percent?</h2>

    <p>
      Percentages are simply relative frequencies expressed out of 100.
    </p>

    <p>
      Formula:
    </p>

    <div class="formula-box">
  Percent = Relative Frequency × 100
</div>

    <p>
      Using the previous example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Operating System</th>
            <th>Percent</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Windows</td>
            <td>60%</td>
          </tr>

          <tr>
            <td>macOS</td>
            <td>25%</td>
          </tr>

          <tr>
            <td>Linux</td>
            <td>15%</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Percentages are often easier for humans to interpret.
    </p>

    <h2>Relative Frequency Tables</h2>

    <p>
      Frequency tables are often expanded
      to include relative frequencies and percentages together.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Category</th>
            <th>Frequency</th>
            <th>Relative Frequency</th>
            <th>Percent</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>A</td>
            <td>18</td>
            <td>0.36</td>
            <td>36%</td>
          </tr>

          <tr>
            <td>B</td>
            <td>22</td>
            <td>0.44</td>
            <td>44%</td>
          </tr>

          <tr>
            <td>C</td>
            <td>10</td>
            <td>0.20</td>
            <td>20%</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Such tables provide richer interpretation
      than raw frequencies alone.
    </p>

    <h2>Relative Frequencies Always Sum to 1</h2>

    <p>
      If all categories are included,
      relative frequencies sum to:
    </p>

    <div class="formula-box">
  Sum of Relative Frequencies = 1
</div>

    <p>
      Similarly,
      percentages sum to:
    </p>

    <div class="formula-box">
  Sum of Percentages = 100%
</div>

    <p>
      Small differences may occur because of rounding.
    </p>

    <p>
  Slight deviations from exactly 1 or 100%
  are common in practical reporting.
</p>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Relative frequencies remove the direct influence of sample size,
    making comparisons more meaningful across datasets.
  </p>

</div>

    <h2>Relative Frequency Improves Comparisons</h2>

    <p>
      Relative frequencies are especially useful when comparing:
    </p>

    <ul class="bullets">
      <li>Different sample sizes</li>
      <li>Different populations</li>
      <li>Different time periods</li>
      <li>Different experimental groups</li>
    </ul>

    <p>
      Standardization allows fair comparison.
    </p>

    <h2>Relative Frequency Connects to Probability</h2>

    <p>
      Relative frequency also plays an important role in probability.
    </p>

    <p>
      In many situations:
    </p>

    <div class="example-box">

      <p>
        Probability can be interpreted as long-run relative frequency.
      </p>

    </div>

    <p>
      This connection becomes fundamental in later statistics and probability courses.
    </p>

    <h2>Common Mistakes</h2>

    <p>
      Common errors include:
    </p>

    <ul class="bullets">
      <li>Confusing frequency with relative frequency</li>
      <li>Using percentages without sample size context</li>
      <li>Ignoring rounding effects</li>
      <li>Comparing raw counts from unequal groups</li>
    </ul>

    <p>
      Correct interpretation requires understanding both counts and proportions.
    </p>

    <h2>Relative Frequencies Appear Everywhere</h2>

    <p>
      Relative frequencies and percentages are used constantly in:
    </p>

    <ul class="bullets">
      <li>Survey reports</li>
      <li>Public health statistics</li>
      <li>Business analytics</li>
      <li>Election results</li>
      <li>Experimental studies</li>
      <li>Machine learning datasets</li>
    </ul>

    <p>
      They are among the most widely used descriptive summaries.
    </p>

    <div class="concept-box">

  <strong>Key insight:</strong>

  <p>
    Relative frequencies help transform raw counts
    into standardized distributions that are easier to compare,
    interpret,
    and connect to probability.
  </p>

</div>

<img src="{{ 'descriptive/images/percent-visualizations.png' | relative_url }}" 
     alt="Percentages visualized using charts" 
     style="margin-top:15px; max-width:100%; height:auto;">

     <div class="concept-box">

<strong>In practice:</strong>

<p>
In SPSS, frequency tables commonly include:
</p>

<ul class="bullets">
  <li>Frequency</li>
  <li>Percent</li>
  <li>Valid Percent</li>
  <li>Cumulative Percent</li>
</ul>

<p>
Spreadsheet software such as Excel can calculate percentages
by dividing counts by the total sample size.
</p>

</div>

<h3>Python Example</h3>

<p>
This example converts frequencies into percentages.
</p>

<pre><code>counts = [12, 5, 3]

total = sum(counts)

percentages = [x / total * 100 for x in counts]
</code></pre>

<img src="{{ 'descriptive/images/Python_relative-frequency-and-percent.png' | relative_url }}" 
     style="margin-top:15px; max-width:100%; height:auto;">

<h3>R Example</h3>

<p>
This example converts frequencies into proportions.
</p>

<pre><code>counts <- c(12, 5, 3)

counts / sum(counts)
</code></pre>

<img src="{{ 'descriptive/images/R_relative-frequency-and-percent.png' | relative_url }}" 
     style="margin-top:15px; max-width:100%; height:auto;"> 

    <!-- TAKEAWAYS -->
    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Relative frequency measures proportion rather than raw count</li>

        <li>Percentages are relative frequencies multiplied by 100</li>

        <li>Relative frequencies standardize comparisons across sample sizes</li>

        <li>Relative frequencies sum to 1</li>

        <li>Percentages sum to 100%</li>

        <li>Relative frequency is closely connected to probability concepts</li>

        <li>Interpretation requires considering both counts and proportions</li>

      </ul>

    </div>

    <!-- NAVIGATION -->
    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/tabular-summaries/frequency-tables/">
         ← Previous: Frequency Tables
      </a>

      <a class="btn"
         href="/descriptive/tabular-summaries/cumulative-frequency/">
         Next: Cumulative Frequency →
      </a>

    </div>

  </div>

</section>
