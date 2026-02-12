---
layout: default
title: "Discrete vs Continuous Variables"
description: "Understanding count data vs measurement data and why the distinction affects summaries and graphs."
permalink: /descriptive/data-variables/discrete-vs-continuous/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/data-variables/nominal-vs-ordinal/">
    ← Previous Lesson: Nominal vs Ordinal Variables
  </a>
</section>

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This lesson is being expanded. Structure is stable; examples and visuals will be refined.
      </p>
    </div>
  </div>
</section>

<section class="section">

  <div class="section-head">
    <h1>Discrete vs Continuous Variables</h1>
    <p>
      Both are numerical variables — but they behave differently.
      The distinction affects how we summarize, visualize, and model data.
    </p>
  </div>

  <h2>1. Discrete Variables</h2>

  <p>
    A <strong>discrete variable</strong> takes separate, countable values.
    There are gaps between possible values.
  </p>

  <h3>Examples:</h3>
  <ul>
    <li>Number of students in a class</li>
    <li>Number of hospital visits</li>
    <li>Number of defects in a product</li>
    <li>Number of children in a family</li>
  </ul>

  <p>
    You cannot have 2.5 students.
  </p>

  <h3>Key idea:</h3>
  <p>
    Discrete data usually arise from <strong>counting</strong>.
  </p>

  <hr>

  <h2>2. Continuous Variables</h2>

  <p>
    A <strong>continuous variable</strong> can take any value within a range.
  </p>

  <h3>Examples:</h3>
  <ul>
    <li>Height</li>
    <li>Weight</li>
    <li>Time</li>
    <li>Temperature</li>
    <li>Blood pressure</li>
  </ul>

  <p>
    Between 170 cm and 171 cm, infinitely many values exist.
  </p>

  <h3>Key idea:</h3>
  <p>
    Continuous data arise from <strong>measurement</strong>.
  </p>

  <hr>

  <h2>3. Why This Distinction Matters</h2>

  <h3>Graphs</h3>
  <ul>
    <li>Discrete → Bar chart (sometimes histogram)</li>
    <li>Continuous → Histogram, density plot</li>
  </ul>

  <h3>Mathematics</h3>
  <ul>
    <li>Discrete → Probability mass functions</li>
    <li>Continuous → Probability density functions</li>
  </ul>

  <h3>Interpretation</h3>
  <p>
    Treating discrete counts as continuous may distort interpretation,
    especially when sample size is small.
  </p>

  <hr>

  <h2>4. Borderline Cases</h2>

  <p>
    Age can be discrete (in years) or continuous (exact age in days).
  </p>

  <p>
    Income may be recorded as whole numbers,
    but conceptually it is continuous.
  </p>

  <p>
    In practice, context determines classification.
  </p>

  <hr>

  <h2>5. Summary Table</h2>

  <table class="table">
    <thead>
      <tr>
        <th>Feature</th>
        <th>Discrete</th>
        <th>Continuous</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Source</td>
        <td>Counting</td>
        <td>Measurement</td>
      </tr>
      <tr>
        <td>Possible Values</td>
        <td>Separate integers</td>
        <td>Infinite within interval</td>
      </tr>
      <tr>
        <td>Typical Graph</td>
        <td>Bar chart</td>
        <td>Histogram</td>
      </tr>
      <tr>
        <td>Examples</td>
        <td>Number of visits</td>
        <td>Height, weight</td>
      </tr>
    </tbody>
  </table>

  <hr>

  <h2>6. Common Mistakes</h2>

  <ul>
    <li>Using histograms for very small discrete counts</li>
    <li>Forgetting that recorded discrete values may represent underlying continuous variables</li>
    <li>Ignoring measurement precision limits</li>
  </ul>

  <p>
    Clear variable classification is foundational for correct descriptive statistics.
  </p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/data-variables/data-structure-datasets/">
    Next Lesson → Data Structure & Datasets
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_data_variables_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/data-variables/discrete-vs-continuous/",
      label: "Lesson 5 — Discrete vs Continuous Variables",
      ts: Date.now()
    }));
  })();
</script>