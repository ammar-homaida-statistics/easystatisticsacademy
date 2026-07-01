---
layout: default
title: Arithmetic Mean
description: Learn what the arithmetic mean is, how it is calculated, how it is interpreted, and why it is one of the most important statistics in data analysis.
permalink: /descriptive/center/arithmetic-mean/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_center_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/center/arithmetic-mean/",
    label: "Arithmetic Mean",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 4</span>
      <span class="badge">Center</span>
      <span class="badge">Mean</span>
    </div>

    <h1>Arithmetic Mean</h1>

    <p class="lead">
      The arithmetic mean is the most widely used measure of center in statistics.
    </p>

    <p class="lead">
      When people talk about an "average,"
      they are usually referring to the arithmetic mean.
      It summarizes a dataset by representing its balance point with a single value.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/center/what-is-center/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/center/median/">
         Next: Median →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is the Arithmetic Mean?</h2>

    <p>
      The arithmetic mean is obtained by adding all observations
      and dividing by the number of observations.
    </p>

    <p>
      It provides a measure of the typical location of a dataset.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The arithmetic mean is the total of all values divided by the number of values.
      </p>

    </div>

    <h2>The Formula</h2>

    <p>
      For a dataset containing <em>n</em> observations:
    </p>

  <div class="formula-box">

$$
\bar{x}=\frac{\sum_{i=1}^{n} x_i}{n}
$$

</div>

    <p>
      The symbol
      <strong>x̄</strong>
      (pronounced "x-bar")
      is the standard notation for the sample mean.
    </p>

    <h2>Understanding the Formula</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Symbol</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>x₁, x₂, ... , xₙ</td>
            <td>Individual observations</td>
          </tr>

          <tr>
            <td>n</td>
            <td>Number of observations</td>
          </tr>

          <tr>
            <td>x̄</td>
            <td>Sample mean</td>
          </tr>

        </tbody>

      </table>

    </div>

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
      Step 1: Add all observations.
    </p>

    <div class="example-box">

      <p>
        4 + 6 + 8 + 10 + 12 = 40
      </p>

    </div>

    <p>
      Step 2: Count the observations.
    </p>

    <div class="example-box">

      <p>
        n = 5
      </p>

    </div>

    <p>
      Step 3: Divide the total by the number of observations.
    </p>

   <div class="formula-box">

\[
\bar{x}=\frac{40}{5}=8
\]

</div>

    <p>
      Therefore,
      the mean is 8.
    </p>

    <h2>Another Example</h2>

    <p>
      Suppose five students receive the following scores:
    </p>

    <div class="example-box">

      <p>
        70, 75, 80, 85, 90
      </p>

    </div>

    <p>
      Adding the values:
    </p>

    <div class="example-box">

      <p>
        70 + 75 + 80 + 85 + 90 = 400
      </p>

    </div>

    <p>
      Dividing by the number of students:
    </p>

   <div class="formula-box">

\[
\bar{x}=\frac{400}{5}=80
\]

</div>

    <p>
      The average score is 80.
    </p>

    <h2>The Mean as a Balance Point</h2>

    <img src="{{ 'descriptive/images/mean-balance-point.png' | relative_url }}"
     alt="Mean as the balance point of a distribution"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
The arithmetic mean can be viewed as the balance point of a distribution.
</p>

    <p>
      The mean is not just a computational formula.
    </p>

    <p>
      It has an important physical interpretation.
    </p>

    <p>
      Imagine placing each observation on a number line.
    </p>

    <p>
      The mean acts as the balance point of the distribution.
    </p>

    <p>
      Values below the mean balance values above the mean.
    </p>

    <h2>Why the Mean Is Popular</h2>

    <p>
      The arithmetic mean has several useful properties.
    </p>

    <ul class="bullets">

      <li>Easy to calculate</li>

      <li>Uses every observation</li>

      <li>Widely understood</li>

      <li>Works well in many statistical methods</li>

      <li>Provides a useful summary of center</li>

    </ul>

    <p>
      Because of these advantages,
      the mean appears throughout statistics and data science.
    </p>

    <h2>The Mean Uses All Observations</h2>

    <div class="example-box">

  <strong>Important:</strong>

  <p>
    Because every observation contributes to the calculation,
    the mean may not correspond to an actual observed value.
  </p>

</div>

    <p>
      Unlike some other measures of center,
      the mean depends on every value in the dataset.
    </p>

    <p>
      Changing even one observation changes the mean.
    </p>

    <p>
      This can be both an advantage and a disadvantage.
    </p>

    <h2>The Effect of an Outlier</h2>

    <p>
      Consider the dataset:
    </p>

    <div class="example-box">

      <p>
        10, 11, 12, 13, 14
      </p>

    </div>

    <p>
      The mean is:
    </p>

    <div class="formula-box">

\[
\bar{x}=\frac{10+11+12+13+14}{5}=12
\]

</div>

<img src="{{ 'descriptive/images/outlier-effect-on-mean.png' | relative_url }}"
     alt="Effect of an outlier on the arithmetic mean"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
A single extreme observation can substantially change the mean.
</p>

    <p>
      Now replace 14 with 100.
    </p>

    <div class="example-box">

      <p>
        10, 11, 12, 13, 100
      </p>

    </div>

    <p>
      The new mean becomes:
    </p>

  <div class="formula-box">

\[
\bar{x}=\frac{10+11+12+13+100}{5}=29.2
\]

</div>

    <p>
      A single extreme value dramatically changes the mean.
    </p>

    <h2>Sensitivity to Outliers</h2>

    <p>
      Because the mean uses every observation,
      it is sensitive to unusually large or unusually small values.
    </p>

    <p>
      Such values are called
      <strong>outliers</strong>.
    </p>

    <p>
      Outliers can pull the mean away from where most observations are located.
    </p>

    <div class="example-box">

      <strong>Important:</strong>

      <p>
        The mean is not resistant to outliers.
      </p>

    </div>

    <h2>When the Mean Works Well</h2>

    <img src="{{ 'descriptive/images/mean-symmetric-distribution.png' | relative_url }}"
     alt="Mean in a symmetric distribution"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      The arithmetic mean performs particularly well when:
    </p>

    <ul class="bullets">

      <li>The distribution is roughly symmetric</li>

      <li>Extreme outliers are absent</li>

      <li>All observations are meaningful</li>

      <li>A complete numerical summary is desired</li>

    </ul>

    <h2>Situations Where the Mean Can Be Misleading</h2>

    <p>
      The mean can be misleading when:
    </p>

    <ul class="bullets">

      <li>Strong outliers are present</li>

      <li>The distribution is highly skewed</li>

      <li>Most observations are concentrated far from the mean</li>

    </ul>

    <p>
      In such cases,
      the median may provide a better summary.
    </p>

    <h2>Population Mean vs Sample Mean</h2>

    <p>
      The notation depends on whether we are studying a sample or an entire population.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Measure</th>
            <th>Notation</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Sample Mean</td>
            <td>x̄</td>
          </tr>

          <tr>
            <td>Population Mean</td>
            <td>μ</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The population mean is usually unknown,
      while the sample mean can be calculated from observed data.
    </p>

    <h2>SPSS Application</h2>

<p>
SPSS can calculate the arithmetic mean automatically.
</p>

<p>
To compute means in SPSS:
</p>

<div class="example-box">

<p>

<strong>Analyze → Descriptive Statistics → Descriptives</strong>

</p>

</div>

<p>
Select one or more numerical variables and move them into the analysis box.
SPSS will report the mean along with other descriptive statistics.
</p>

    <h2>Applications of the Mean</h2>

    <p>
      Means appear in countless real-world situations:
    </p>

    <ul class="bullets">

      <li>Average income</li>

      <li>Average test score</li>

      <li>Average temperature</li>

      <li>Average sales</li>

      <li>Average blood pressure</li>

      <li>Average production output</li>

    </ul>

    <p>
      It is one of the most frequently reported statistics.
    </p>

    <h2>The Mean and Future Statistics</h2>

    <p>
      The arithmetic mean plays a central role in later topics,
      including:
    </p>

    <ul class="bullets">

      <li>Variance</li>

      <li>Standard deviation</li>

      <li>Correlation</li>

      <li>Regression</li>

      <li>Statistical inference</li>

    </ul>

    <p>
      Understanding the mean thoroughly is essential for advanced statistics.
    </p>

    <h3>Python Example</h3>

<p>
This example calculates the arithmetic mean of exam scores.
</p>

<pre><code>import statistics

scores = [70, 75, 80, 85, 90]

print("Mean =", statistics.mean(scores))
</code></pre>

<h3>R Example</h3>

<p>
This example calculates the arithmetic mean of exam scores.
</p>

<pre><code>scores <- c(70, 75, 80, 85, 90)

mean(scores)
</code></pre>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The arithmetic mean is the most common measure of center</li>

        <li>The mean equals the sum of observations divided by the number of observations</li>

        <li>The sample mean is denoted by x̄</li>

        <li>The mean uses every observation in the dataset</li>

        <li>The mean represents the balance point of a distribution</li>

        <li>Outliers can strongly affect the mean</li>

        <li>The mean works best for roughly symmetric numerical data</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/center/what-is-center/">
         ← Previous: What Is Center?
      </a>

      <a class="btn"
         href="/descriptive/center/median/">
         Next: Median →
      </a>

    </div>

  </div>

</section>
