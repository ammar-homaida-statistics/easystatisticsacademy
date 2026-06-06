---
layout: default
title: Cumulative Frequency
description: Learn how cumulative frequencies summarize running totals and help analyze distributions, rankings, and percentiles.
permalink: /descriptive/tabular-summaries/cumulative-frequency/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_tabular_summaries_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/tabular-summaries/cumulative-frequency/",
    label: "Cumulative Frequency",
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
      <span class="badge">Running Totals</span>
    </div>

    <h1>Cumulative Frequency</h1>

    <p class="lead">
      Sometimes we are interested not only in individual frequencies,
      but also in how frequencies accumulate across values.
    </p>

    <p class="lead">
      Cumulative frequency helps summarize distributions progressively,
      making it easier to understand rankings,
      percentiles,
      thresholds,
      and overall distribution structure.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/tabular-summaries/relative-frequency-and-percent/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/tabular-summaries/grouped-frequency-tables/">
         Next: Grouped Frequency Tables
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->
<section class="section">

  <div class="content-narrow">

    <h2>What Is Cumulative Frequency?</h2>

    <p>
      <strong>Cumulative frequency</strong>
      is the running total of frequencies as we move through ordered values or categories.
    </p>

    <p>
      Instead of showing only how often a value occurs,
      cumulative frequency shows how many observations are at or below a value.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Cumulative frequency accumulates counts progressively across ordered values.
      </p>

    </div>

    <h2>Why Ordering Matters</h2>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Cumulative frequency depends on meaningful ordering.
    Without order, accumulation has no statistical interpretation.
  </p>

</div>

    <p>
      Cumulative frequency only makes sense when values are ordered.
    </p>

    <p>
      Therefore,
      cumulative frequencies are commonly used for:
    </p>

    <ul class="bullets">
      <li>Numerical variables</li>
      <li>Ordinal variables</li>
      <li>Grouped intervals</li>
    </ul>

    <p>
      They are generally not meaningful for purely nominal categories.
    </p>

    <h2>Basic Example</h2>

    <p>
      Suppose exam scores are summarized as:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Score</th>
            <th>Frequency</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>60</td>
            <td>2</td>
          </tr>

          <tr>
            <td>70</td>
            <td>5</td>
          </tr>

          <tr>
            <td>80</td>
            <td>4</td>
          </tr>

          <tr>
            <td>90</td>
            <td>3</td>
          </tr>

        </tbody>

      </table>

    </div>

    <img src="{{ 'descriptive/images/frequency-vs-cumulative-frequency.png' | relative_url }}"
     alt="Frequency versus cumulative frequency"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Frequencies show counts at each value,
while cumulative frequencies show how counts accumulate across values.
</p>

    <p>
      We now compute running totals:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Score</th>
            <th>Frequency</th>
            <th>Cumulative Frequency</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>60</td>
            <td>2</td>
            <td>2</td>
          </tr>

          <tr>
            <td>70</td>
            <td>5</td>
            <td>7</td>
          </tr>

          <tr>
            <td>80</td>
            <td>4</td>
            <td>11</td>
          </tr>

          <tr>
            <td>90</td>
            <td>3</td>
            <td>14</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Interpretation:
    </p>

    <ul class="bullets">
      <li>7 students scored 70 or below</li>
      <li>11 students scored 80 or below</li>
      <li>14 students scored 90 or below</li>
    </ul>

    <h2>How Cumulative Frequency Is Calculated</h2>

    <p>
      Each cumulative frequency equals:
    </p>

    <div class="formula-box">
  CFᵢ = CFᵢ₋₁ + fᵢ
</div>

<img src="{{ '/descriptive/images/cumulative-running-total.png' | relative_url }}"
     alt="Running total calculation"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Each cumulative frequency adds the next frequency to the running total.
</p>

    <p>
      The final cumulative frequency always equals the total sample size.
    </p>

    <h2>Cumulative Relative Frequency</h2>

    <p>
      We can also accumulate relative frequencies or percentages.
    </p>

    <p>
      Example:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Score</th>
            <th>Percent</th>
            <th>Cumulative Percent</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>60</td>
            <td>14%</td>
            <td>14%</td>
          </tr>

          <tr>
            <td>70</td>
            <td>36%</td>
            <td>50%</td>
          </tr>

          <tr>
            <td>80</td>
            <td>29%</td>
            <td>79%</td>
          </tr>

          <tr>
            <td>90</td>
            <td>21%</td>
            <td>100%</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Cumulative percentages are widely used in reporting and interpretation.
    </p>

    <h2>Why Cumulative Frequency Is Useful</h2>

    <p>
      Cumulative frequency helps answer questions such as:
    </p>

    <ul class="bullets">
      <li>How many observations are below a threshold?</li>
      <li>What proportion scored below 80?</li>
      <li>Where are the middle observations located?</li>
      <li>How concentrated is the distribution?</li>
    </ul>

    <p>
  Cumulative frequencies reveal how observations accumulate
  throughout a distribution rather than how they are distributed
  within individual categories.
</p>

    <p>
      These questions are extremely common in statistics.
    </p>

    <h2>Cumulative Frequency and Percentiles</h2>

    <p>
      Percentiles are closely connected
      to cumulative frequency distributions.
    </p>

    <p>
      Example:
    </p>

    <div class="example-box">

      <p>
        The 75th percentile is the value below which 75% of observations fall.
      </p>

    </div>

    <p>
      Cumulative frequencies help identify such cutoff points.
    </p>

    <p>
  Quartiles, deciles, and percentiles are all derived
  from cumulative distributions.
</p>

    <h2>Cumulative Frequency Curves</h2>

    <p>
      Cumulative frequencies can also be visualized graphically.
    </p>

    <p>
      A graph of cumulative frequencies is called an:
    </p>

    <ul class="bullets">
      <li>Ogive</li>
    </ul>

    <p>
      These graphs help visualize accumulation patterns across distributions.
    </p>

    <h2>Example: Customer Waiting Times</h2>

    <p>
      Suppose waiting times are summarized:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Waiting Time (minutes)</th>
            <th>Cumulative Percent</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>5 or less</td>
            <td>20%</td>
          </tr>

          <tr>
            <td>10 or less</td>
            <td>55%</td>
          </tr>

          <tr>
            <td>15 or less</td>
            <td>82%</td>
          </tr>

          <tr>
            <td>20 or less</td>
            <td>100%</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Interpretation:
    </p>

    <ul class="bullets">
      <li>55% waited 10 minutes or less</li>
      <li>82% waited 15 minutes or less</li>
    </ul>

    <p>
      Cumulative summaries provide richer interpretation than raw frequencies alone.
    </p>

    <img src="{{ '/descriptive/images/ogive-example.png' | relative_url }}"
     alt="Ogive cumulative frequency curve"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
An ogive shows how observations accumulate across a distribution.
</p>

    <h2>Common Mistakes</h2>

    <p>
      Common errors include:
    </p>

    <ul class="bullets">
      <li>Using cumulative frequency on unordered categories</li>
      <li>Confusing frequency with cumulative frequency</li>
      <li>Incorrectly summing categories</li>
      <li>Ignoring the importance of ordering</li>
    </ul>

    <p>
      Correct ordering is essential for meaningful cumulative interpretation.
    </p>

    <h2>Cumulative Frequency Is Widely Used</h2>

    <p>
      Cumulative summaries appear throughout:
    </p>

    <ul class="bullets">
      <li>Educational testing</li>
      <li>Quality control</li>
      <li>Survey analysis</li>
      <li>Business analytics</li>
      <li>Medical reporting</li>
      <li>Probability distributions</li>
    </ul>

    <p>
      They are foundational tools for understanding distributions progressively.
    </p>

    <div class="concept-box">

  <strong>Key insight:</strong>

  <p>
    Frequency tables show where observations occur,
    while cumulative frequency tables show how observations
    accumulate across a distribution.
  </p>

</div>

<h2>Optional: Cumulative Frequencies in SPSS</h2>

<ul class="bullets">
  <li>Analyze → Descriptive Statistics → Frequencies</li>
  <li>SPSS can display cumulative frequencies and cumulative percentages</li>
  <li>Cumulative percentages are commonly used to identify percentiles</li>
</ul>



<div style="display:flex; gap:20px; align-items:flex-start; flex-wrap:wrap;">

  <div style="flex:1; min-width:300px;">
    <img src="{{ 'descriptive/images/spss_frequencies_data.png' | relative_url }}"
         alt="SPSS data view"
         style="width:100%; height:auto;">

    <p style="text-align:center;">
      Data entered in SPSS
    </p>
  </div>

  <div style="flex:1; min-width:300px;">
    <img src="{{ 'descriptive/images/spss_frequencies.png' | relative_url }}"
         alt="SPSS frequencies output"
         style="width:100%; height:auto;">

    <p style="text-align:center;">
      Frequency table output
    </p>
  </div>

</div>



<p>
Spreadsheet software such as Excel can compute cumulative totals
using running-sum formulas.
</p>

<h3>Python Example</h3>

<p>
This example computes cumulative frequencies.
</p>

<pre><code>import pandas as pd

freq = [2, 5, 4, 3]

pd.Series(freq).cumsum()
</code></pre>

<h3>R Example</h3>

<p>
This example computes cumulative frequencies.
</p>

<pre><code>freq <- c(2, 5, 4, 3)

cumsum(freq)
</code></pre>

    <!-- TAKEAWAYS -->
    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Cumulative frequency represents running totals across ordered values</li>

        <li>It shows how many observations fall at or below a value</li>

        <li>Cumulative frequency requires meaningful ordering</li>

        <li>The final cumulative frequency equals the total sample size</li>

        <li>Cumulative percentages help interpret distributions and percentiles</li>

        <li>Cumulative summaries are useful for thresholds and rankings</li>

        <li>They are widely used throughout applied statistics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->
    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/tabular-summaries/relative-frequency-and-percent/">
         ← Previous: Relative Frequency and Percent
      </a>

      <a class="btn"
         href="/descriptive/tabular-summaries/grouped-frequency-tables/">
         Next: Grouped Frequency Tables →
      </a>

    </div>

  </div>

</section>
