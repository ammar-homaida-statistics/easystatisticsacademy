---
layout: default
title: Discrete vs Continuous Data
description: Learn the difference between discrete and continuous numerical variables and why this distinction matters in statistics.
permalink: /descriptive/data-variables/discrete-vs-continuous/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_data_variables_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/data-variables/discrete-vs-continuous/",
    label: "Discrete vs Continuous Data",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->
<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 1</span>
      <span class="badge">Numerical Variables</span>
      <span class="badge">Measurement</span>
    </div>

    <h1>Discrete vs Continuous Data</h1>

    <p class="lead">
      Numerical variables are not all the same.
    </p>

    <p class="lead">
      Some numerical variables count separate individual values,
      while others measure quantities on a continuous scale.
      This creates the distinction between discrete and continuous data.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/data-variables/nominal-vs-ordinal/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/data-variables/data-structure-and-datasets/">
         Next Lesson →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->
<section class="section">

  <div class="content-narrow">

    <h2>Two Types of Numerical Variables</h2>

    <p>
      In the previous lessons,
      we separated numerical variables from categorical variables.
    </p>

    <p>
      Numerical variables themselves also split into two major types:
    </p>

    <ul class="bullets">
      <li>Discrete variables</li>
      <li>Continuous variables</li>
    </ul>

    <p>
      The key difference is whether values are counted
      or measured.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Discrete variables count separate values.
        Continuous variables measure quantities on a scale.
      </p>

    </div>

    <h2>What Is Discrete Data?</h2>

    <p>
      <strong>Discrete data</strong>
      consists of separate, countable values.
    </p>

    <p>
      Discrete variables usually arise from counting.
    </p>

    <p>
      Examples:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Variable</th>
            <th>Possible Values</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Number of children</td>
            <td>0, 1, 2, 3...</td>
          </tr>

          <tr>
            <td>Number of emails received</td>
            <td>5, 12, 24...</td>
          </tr>

          <tr>
            <td>Defects in a product batch</td>
            <td>0, 2, 7...</td>
          </tr>

          <tr>
            <td>Goals scored</td>
            <td>0, 1, 2, 3...</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      These variables move in jumps between values.
      Fractions usually do not make sense.
    </p>

    <div class="example-box">

      <p>
        A family cannot have 2.4 children.
      </p>

    </div>

    <h2>What Is Continuous Data?</h2>

    <p>
      <strong>Continuous data</strong>
      represents measurements on a continuous scale.
    </p>

    <p>
      Continuous variables usually arise from measuring.
    </p>

    <p>
      Examples:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Variable</th>
            <th>Example Values</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Height</td>
            <td>170.2 cm, 181.7 cm</td>
          </tr>

          <tr>
            <td>Weight</td>
            <td>68.4 kg, 91.1 kg</td>
          </tr>

          <tr>
            <td>Time</td>
            <td>2.53 sec, 7.91 sec</td>
          </tr>

          <tr>
            <td>Temperature</td>
            <td>18.6°C, 31.2°C</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Continuous variables can theoretically take infinitely many values
      within an interval.
    </p>

    <h2>The Main Difference</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Discrete</th>
            <th>Continuous</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Usually counts</td>
            <td>Usually measurements</td>
          </tr>

          <tr>
            <td>Separate values</td>
            <td>Infinite possible values</td>
          </tr>

          <tr>
            <td>Often whole numbers</td>
            <td>Often decimals</td>
          </tr>

          <tr>
            <td>Jumps between values</td>
            <td>Flows continuously</td>
          </tr>

        </tbody>

      </table>

    </div>

<img src="{{ 'descriptive/images/discrete-vs-continuous-visual.png' | relative_url }}" 
     alt="Discrete versus continuous data" 
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Discrete variables move between separate values,
while continuous variables vary along a measurement scale.
</p>

<p>
  Both discrete and continuous variables are numerical variables.
</p>

<p>
  The distinction is not whether numbers are used,
  but how the values are generated and interpreted.
</p>

    <h2>Continuous Variables Are Often Rounded</h2>

<p>
Spreadsheet software such as Excel may display rounded values,
even when the underlying variable is continuous.
</p>

    <p>
      In practice,
      continuous measurements are usually rounded.
    </p>

<p>
  Real measurements are limited by instrument precision,
  so observed continuous values are always approximations.
</p>

    <p>
      For example:
    </p>

    <ul class="bullets">
      <li>Height recorded as 170 cm</li>
      <li>Weight recorded as 68.5 kg</li>
      <li>Temperature recorded as 25°C</li>
    </ul>

    <p>
      Even though the recorded values appear discrete,
      the underlying variable remains continuous.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Measurement precision does not change the true type of the variable.
      </p>

    </div>

    <h2>Why This Distinction Matters</h2>

    <p>
      Discrete and continuous variables behave differently.
    </p>

    <p>
      This affects:
    </p>

    <ul class="bullets">
      <li>Probability models</li>
<li>Different probability distributions apply to different variable types</li>
      <li>Graphs and visualization</li>
      <li>Statistical formulas</li>
      <li>Machine learning methods</li>
      <li>Interpretation of results</li>
    </ul>

    <p>
      For example:
    </p>

    <div class="grid grid-2">

      <div class="card">

        <h3>Discrete variables</h3>

        <ul class="bullets">
          <li>Bar charts</li>
          <li>Count models</li>
          <li>Frequency tables</li>
        </ul>

      </div>

      <div class="card">

        <h3>Continuous variables</h3>

        <ul class="bullets">
          <li>Histograms</li>
          <li>Density curves</li>
          <li>Measurement distributions</li>
        </ul>

      </div>

    </div>

<img src="{{ 'descriptive/images/discrete-vs-continuous-graphs.png' | relative_url }}" 
     alt="Graphs for discrete and continuous variables" 
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Discrete variables are often summarized using counts,
while continuous variables are commonly summarized using distributions.
</p>

    <h2>Real-World Example</h2>

    <p>
      Suppose a hospital studies patients.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Variable</th>
            <th>Type</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Number of medications</td>
            <td>Discrete</td>
          </tr>

          <tr>
            <td>Body temperature</td>
            <td>Continuous</td>
          </tr>

          <tr>
            <td>Days hospitalized</td>
            <td>Discrete</td>
          </tr>

          <tr>
            <td>Blood pressure</td>
            <td>Continuous</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both are numerical,
      but they represent fundamentally different types of quantities.
    </p>

    <h2>The Difference Can Sometimes Depend on Context</h2>

<p>
  The classification may depend on the level of measurement precision.
</p>

    <p>
      Some variables may appear discrete or continuous
      depending on how they are measured.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">
      <li>Age in years → often treated as discrete</li>
      <li>Exact age in seconds → continuous</li>
    </ul>

    <p>
      Statistical modeling sometimes simplifies continuous variables
      into discrete categories for practical reasons.
    </p>

    <h2>Understanding Variable Type Improves Analysis</h2>

    <p>
      Correctly identifying discrete and continuous variables helps:
    </p>

    <ul class="bullets">
      <li>Choose proper visualizations</li>
      <li>Select correct probability models</li>
      <li>Avoid incorrect assumptions</li>
      <li>Interpret results properly</li>
    </ul>

    <p>
      This distinction becomes extremely important later
      in probability, inference, and machine learning.
    </p>

<div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Correctly identifying whether data is discrete or continuous
    helps determine valid probability models,
    visualizations, and statistical assumptions.
  </p>

<div class="concept-box">

<strong>In practice:</strong>

<p>
In SPSS, continuous variables are often analyzed using histograms,
while discrete variables are commonly summarized using frequencies and bar charts.
</p>

</div>

</div>

<h3>Python Example</h3>

<p>
This example creates discrete and continuous variables.
</p>

<pre><code>children = [0, 1, 2, 3]
heights = [170.2, 168.5, 181.1]
</code></pre>

<h3>R Example</h3>

<p>
This example creates discrete and continuous variables.
</p>

<pre><code>children <- c(0, 1, 2, 3)
heights <- c(170.2, 168.5, 181.1)
</code></pre>

    <!-- TAKEAWAYS -->
    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Discrete variables usually arise from counting</li>

        <li>Continuous variables usually arise from measuring</li>

        <li>Discrete values are separate and countable</li>

        <li>Continuous variables can theoretically take any value within a range or interval</li>

        <li>Rounding does not change a continuous variable into a discrete one</li>

        <li>This distinction affects statistical methods and interpretation</li>

      </ul>

    </div>

    <!-- NAVIGATION -->
    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/data-variables/nominal-vs-ordinal/">
         ← Previous: Nominal vs Ordinal
      </a>

      <a class="btn"
         href="/descriptive/data-variables/data-structure-and-datasets/">
         Next Lesson →
      </a>

    </div>

  </div>

</section>
