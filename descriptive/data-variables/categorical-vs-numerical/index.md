---
layout: default
title: Categorical vs Numerical Data
description: Learn the fundamental distinction between categorical and numerical variables and why this classification determines statistical analysis.
permalink: /descriptive/data-variables/categorical-vs-numerical/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_data_variables_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/data-variables/categorical-vs-numerical/",
    label: "Categorical vs Numerical Data",
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
      <span class="badge">Variable Types</span>
      <span class="badge">Foundations</span>
    </div>

    <h1>Categorical vs Numerical Data</h1>

    <p class="lead">
      Not all variables behave the same way.
    </p>

    <p class="lead">
      One of the most important distinctions in statistics
      is whether a variable is categorical or numerical.
      This classification determines which summaries,
      graphs, and statistical methods are appropriate.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/data-variables/units-observations-and-variables/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/data-variables/nominal-vs-ordinal/">
         Next: Nominal vs Ordinal
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->
<section class="section">

  <div class="content-narrow">

    <h2>Why Variable Type Matters</h2>

    <p>
      Before analyzing any dataset,
      we must identify the type of each variable.
    </p>

    <p>
      Different variable types require different:
    </p>

    <ul class="bullets">
      <li>Summaries</li>
      <li>Graphs</li>
      <li>Statistical methods</li>
      <li>Interpretations</li>
    </ul>

    <p>
      Using the wrong method for a variable type
      can produce meaningless or misleading conclusions.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Statistical analysis always depends on the type of data being analyzed.
      </p>

    </div>

    <div class="concept-box">

<strong>In practice:</strong>

<p>
In SPSS Variable View,
variables are classified using measurement types such as:
</p>

<ul class="bullets">
  <li>Nominal</li>
  <li>Ordinal</li>
  <li>Scale</li>
</ul>

</div>

    <h2>What Is Categorical Data?</h2>

    <p>
      <strong>Categorical data</strong>
      places observations into groups or categories.
    </p>

    <p>
      These categories describe qualities or labels,
      not numerical quantities.
    </p>

    <p>
      Examples:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Variable</th>
            <th>Possible Categories</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Blood type</td>
            <td>A, B, AB, O</td>
          </tr>

          <tr>
            <td>Eye color</td>
            <td>Brown, Blue, Green</td>
          </tr>

          <tr>
            <td>Marital status</td>
            <td>Single, Married, Divorced</td>
          </tr>

          <tr>
            <td>Country</td>
            <td>Japan, Brazil, Egypt</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      These categories identify groups,
      not measurable quantities.
    </p>

    <h2>What Is Numerical Data?</h2>

    <p>
      <strong>Numerical data</strong>
      represents measurable quantities or counts.
    </p>

    <p>
      Numerical variables involve real numbers
      where arithmetic operations are meaningful.
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
            <td>Age</td>
            <td>18, 25, 42</td>
          </tr>

          <tr>
            <td>Height</td>
            <td>160 cm, 172 cm</td>
          </tr>

          <tr>
            <td>Income</td>
            <td>3200, 4500</td>
          </tr>

          <tr>
            <td>Number of children</td>
            <td>0, 2, 5</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Numerical values measure magnitude or quantity.
    </p>

    <p>
  Numerical variables may be:
</p>

<ul class="bullets">
  <li><strong>Discrete:</strong> countable values (e.g., number of children)</li>
  <li><strong>Continuous:</strong> measurements on a scale (e.g., height, weight)</li>
</ul>

    <h2>The Key Difference</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Categorical</th>
            <th>Numerical</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Represents groups or labels</td>
            <td>Represents quantities</td>
          </tr>

          <tr>
            <td>Arithmetic is meaningless</td>
            <td>Arithmetic is meaningful</td>
          </tr>

          <tr>
            <td>Usually summarized with counts or percentages</td>
            <td>Usually summarized with means or medians</td>
          </tr>

          <tr>
            <td>Often visualized using bar charts</td>
            <td>Often visualized using histograms</td>
          </tr>

        </tbody>

      </table>

      <p>
  Categorical variables are also called
  <strong>qualitative variables</strong>,
  while numerical variables are also called
  <strong>quantitative variables</strong>.
</p>

    </div>

    <h2>Why Arithmetic Matters</h2>

    <p>
  The key issue is not whether values are written as numbers,
  but whether numerical operations carry meaningful interpretation.
</p>

    <p>
      One useful test is asking:
    </p>

    <div class="example-box">

      <p>
        “Does arithmetic on these values make sense?”
      </p>

    </div>

    <p>
      For example:
    </p>

    <ul class="bullets">
      <li>Average age → meaningful</li>
      <li>Average income → meaningful</li>
      <li>Average eye color → meaningless</li>
      <li>Average country → meaningless</li>
    </ul>

    <p>
      This helps distinguish numerical from categorical variables.
    </p>

    <h2>Numbers Can Still Be Categorical</h2>

    <p>
In spreadsheets such as Excel,
identification numbers and postal codes may appear numeric,
but they still function as categorical labels.
</p>

    <p>
      A very common mistake is assuming:
    </p>

    <div class="example-box">

      <p>
        “If the values are numbers,
        the variable must be numerical.”
      </p>

    </div>

    <p>
      This is false.
    </p>

    <p>
      Sometimes numbers are only labels.
    </p>

    <p>
      Examples:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Variable</th>
            <th>Meaning</th>
            <th>Type</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Jersey number</td>
            <td>Player identifier</td>
            <td>Categorical</td>
          </tr>

          <tr>
            <td>Postal code</td>
            <td>Location label</td>
            <td>Categorical</td>
          </tr>

          <tr>
            <td>Student ID</td>
            <td>Identifier</td>
            <td>Categorical</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Even though these variables use numbers,
      arithmetic on them is meaningless.
    </p>

    <h2>Choosing Correct Summaries</h2>

    <p>
  Different variable types produce different kinds of distributions,
  requiring different descriptive and inferential tools.
</p>

    <p>
      Variable type determines how we summarize data.
    </p>

    <div class="grid grid-2">

      <div class="card">

        <h3>Categorical variables</h3>

        <ul class="bullets">
          <li>Counts</li>
          <li>Percentages</li>
          <li>Bar charts</li>
          <li>Pie charts</li>
        </ul>

      </div>

      <div class="card">

        <h3>Numerical variables</h3>

        <ul class="bullets">
          <li>Mean</li>
          <li>Median</li>
          <li>Standard deviation</li>
          <li>Histograms</li>
        </ul>

      </div>

    </div>

    <img src="{{ 'descriptive/images/categorical-vs-numerical-graphs.png' | relative_url }}" 
     alt="Bar chart and histogram comparison" 
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Categorical variables are commonly visualized using bar charts,
while numerical variables are often visualized using histograms.
</p>

    <p>
      Mixing these approaches incorrectly
      creates invalid analysis.
    </p>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    Incorrectly classifying a variable
    can lead to inappropriate statistical methods
    and misleading conclusions.
  </p>

</div>

    <h2>Real-World Example</h2>

    <p>
      Suppose a university records:
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
            <td>Major</td>
            <td>Categorical</td>
          </tr>

          <tr>
            <td>Gender</td>
            <td>Categorical</td>
          </tr>

          <tr>
            <td>GPA</td>
            <td>Numerical</td>
          </tr>

          <tr>
            <td>Age</td>
            <td>Numerical</td>
          </tr>

        </tbody>

      </table>

    </div>

    <img src="{{ 'descriptive/images/variable-types-table.png' | relative_url }}" 
     alt="Dataset showing categorical and numerical variables" 
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      Each variable requires different descriptive methods.
    </p>

    <h2>This Distinction Appears Everywhere in Statistics</h2>

    <p>
      The categorical/numerical distinction affects:
    </p>

    <ul class="bullets">
      <li>Descriptive statistics</li>
      <li>Probability models</li>
      <li>Hypothesis testing</li>
      <li>Regression modeling</li>
      <li>Machine learning algorithms</li>
      <li>Visualization choices</li>
    </ul>

    <p>
      This is one of the foundational classifications in statistics.
    </p>

<div>
      <h3>Python Example</h3>

<p>
This example creates both categorical and numerical variables.
</p>

<pre><code>import pandas as pd

data = pd.DataFrame({
    "Major": ["Biology", "Statistics", "Engineering"],
    "GPA": [3.5, 3.9, 3.2]
})
</code></pre>

<h3>R Example</h3>

<p>
This example creates a small dataset with categorical and numerical variables.
</p>

<pre><code>data <- data.frame(
  Major = c("Biology", "Statistics", "Engineering"),
  GPA = c(3.5, 3.9, 3.2)
)
</code></pre>
</div>

    <!-- TAKEAWAYS -->
    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Categorical variables represent groups or labels</li>

        <li>Numerical variables represent measurable quantities</li>

        <li>Arithmetic operations are meaningful only for numerical variables</li>

        <li>Numbers themselves do not guarantee numerical data</li>

        <li>Variable type determines appropriate statistical methods</li>

        <li>Correct classification is essential for valid analysis</li>

      </ul>

    </div>

    <!-- NAVIGATION -->
    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/data-variables/units-observations-and-variables/">
         ← Previous: Units, Observations, and Variables
      </a>

      <a class="btn"
         href="/descriptive/data-variables/nominal-vs-ordinal/">
         Next: Nominal vs Ordinal →
      </a>

    </div>

  </div>

</section>
