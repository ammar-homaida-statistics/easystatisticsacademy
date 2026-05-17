---
layout: default
title: Discrete vs Continuous Data
description: Learn the difference between discrete and continuous numerical variables and why this distinction matters in statistics and data analysis.
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
      Some numerical variables represent counts,
      while others represent measurements on a continuous scale.
      This creates the distinction between
      discrete and continuous data.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/data-variables/nominal-vs-ordinal/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/data-variables/data-structure-and-datasets/">
         Next: Data Structure and Datasets
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
      we separated variables into:
    </p>

    <ul class="bullets">
      <li>Categorical variables</li>
      <li>Numerical variables</li>
    </ul>

    <p>
      Numerical variables themselves split into two important types:
    </p>

    <ul class="bullets">
      <li>Discrete variables</li>
      <li>Continuous variables</li>
    </ul>

    <p>
      The distinction depends on how values are produced:
      by counting or by measuring.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Discrete variables usually count.
        Continuous variables usually measure.
      </p>

    </div>

    <h2>What Is Discrete Data?</h2>

    <p>
      <strong>Discrete data</strong>
      consists of separate, distinct values.
    </p>

    <p>
      These values often arise from counting.
    </p>

    <p>
  Discrete variables are often whole numbers,
  but the essential feature is that values are separate and countable.
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
            <td>0, 1, 2, 3, ...</td>
          </tr>

          <tr>
            <td>Number of students</td>
            <td>25, 26, 27</td>
          </tr>

          <tr>
            <td>Cars owned</td>
            <td>0, 1, 2</td>
          </tr>

          <tr>
            <td>Hospital visits</td>
            <td>1, 2, 5</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      These variables move in jumps.
      Intermediate values often make no sense.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">
      <li>2.5 children → meaningless</li>
      <li>7.3 hospital visits → meaningless</li>
    </ul>

    <h2>What Is Continuous Data?</h2>

    <p>
      <strong>Continuous data</strong>
      can take any value within a range.
    </p>

    <p>
      These variables usually arise from measurement.
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
            <td>Height</td>
            <td>170.2 cm, 170.25 cm, 170.251 cm...</td>
          </tr>

          <tr>
            <td>Weight</td>
            <td>65.1 kg, 65.12 kg...</td>
          </tr>

          <tr>
            <td>Temperature</td>
            <td>21.4°C, 21.45°C...</td>
          </tr>

          <tr>
            <td>Time</td>
            <td>2.1 sec, 2.15 sec...</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Between any two continuous values,
      more possible values can exist.
    </p>

    <h2>The Core Difference</h2>

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
            <td>Distinct separate values</td>
            <td>Can take any value within intervals</td>
          </tr>

          <tr>
            <td>Often whole numbers</td>
            <td>Decimals are common</td>
          </tr>

          <tr>
            <td>Values “jump”</td>
            <td>Values vary continuously across a scale</td>
          </tr>

        </tbody>

      </table>

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
  The difference is not whether numbers are used,
  but how values are generated and interpreted.
</p>

    </div>

    <h2>Continuous Variables Are Often Rounded</h2>

    <p>
      A very important point:
    </p>

    <div class="example-box">

      <p>
        Continuous variables may appear discrete
        because measurements are rounded.
      </p>

    </div>

    <p>
      For example:
    </p>

    <ul class="bullets">
      <li>Height recorded as 172 cm</li>
      <li>Temperature recorded as 21°C</li>
    </ul>

    <p>
      Even if values look like whole numbers,
      the underlying variable may still be continuous.
    </p>

    <p>
      The distinction depends on the real phenomenon,
      not only on the recorded format.
    </p>

    <h2>Why This Distinction Matters</h2>

    <p>
      Discrete and continuous variables often require different:
    </p>

    <ul class="bullets">
      <li>Probability models</li>
      <li>Graphs</li>
      <li>Statistical methods</li>
      <li>Interpretations</li>
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

     <div class="concept-box">

<strong>In practice:</strong>

<p>
In SPSS, discrete variables are often summarized using frequencies,
while continuous variables are commonly explored using histograms and descriptive statistics.
</p>

</div>

<p>
Discrete variables are commonly summarized using counts,
while continuous variables are often visualized using distributions.
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
            <td>Number of visits</td>
            <td>Discrete</td>
          </tr>

          <tr>
            <td>Weight</td>
            <td>Continuous</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Correctly identifying variable type
      improves statistical interpretation.
    </p>

    <h2>Discrete and Continuous Data in Modern Statistics</h2>

    <p>
      This distinction appears everywhere:
    </p>

    <ul class="bullets">
      <li>Probability theory</li>
      <li>Regression modeling</li>
      <li>Machine learning</li>
      <li>Simulation</li>
      <li>Scientific measurement</li>
      <li>Experimental design</li>
    </ul>

    <p>
      Understanding how data is generated
      is central to statistical thinking.
    </p>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Correctly identifying whether data is discrete or continuous
    helps determine valid probability models,
    visualizations, and statistical assumptions.
  </p>

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

        <li>Continuous variables usually arise from measurement</li>

        <li>Discrete variables contain separate distinct values</li>

        <li>Continuous variables can take infinitely many values within intervals</li>

        <li>Rounded measurements may still represent continuous variables</li>

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
         Next: Data Structure and Datasets →
      </a>

    </div>

  </div>

</section>
