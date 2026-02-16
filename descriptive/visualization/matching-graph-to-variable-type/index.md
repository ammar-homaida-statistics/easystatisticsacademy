---
layout: default
title: "Matching Graph Type to Variable Type"
description: "The core rule of visualization: categorical vs numerical variables determine the correct graphical summary."
permalink: /descriptive/visualization/matching-graph-to-variable-type/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/visualization/why-visualization-matters/">
    ← Previous Lesson: Why Visualization Matters
  </a>
</section>

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Visual comparisons, incorrect examples, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

<div class="section-head">
  <h1>Matching Graph Type to Variable Type</h1>
  <p>
    The most important rule in visualization is simple:
    <strong>The type of variable determines the correct graph.</strong>
  </p>
</div>

<hr>

<h2>1. The Fundamental Rule</h2>

<p>
Before choosing a graph, ask:
</p>

<ul>
  <li>Is the variable categorical?</li>
  <li>Is the variable numerical?</li>
</ul>

<p>
If this step is wrong, the visualization will be misleading.
</p>

<hr>

<h2>2. Categorical Variables → Bar Charts</h2>

<p>
Categorical variables represent groups or labels.
</p>

Examples:
<ul>
  <li>Gender</li>
  <li>Department</li>
  <li>Education level</li>
  <li>Product category</li>
</ul>

<p>
Correct graph:
</p>

<ul>
  <li>Bar chart</li>
</ul>

<p>
Bars are separated because categories are distinct.
</p>

<hr>

<h2>3. Numerical Variables → Histograms</h2>

<p>
Numerical variables represent measurements or counts.
</p>

Examples:
<ul>
  <li>Age</li>
  <li>Income</li>
  <li>Height</li>
  <li>Exam score</li>
</ul>

<p>
Correct graph:
</p>

<ul>
  <li>Histogram</li>
</ul>

<p>
Histogram bars touch because the data are continuous.
</p>

<hr>

<h2>4. Two Numerical Variables → Scatterplot</h2>

<p>
When studying the relationship between two numerical variables:
</p>

Examples:
<ul>
  <li>Study hours and exam score</li>
  <li>Income and years of education</li>
</ul>

<p>
Correct graph:
</p>

<ul>
  <li>Scatterplot</li>
</ul>

<p>
This shows association patterns visually.
</p>

<hr>

<h2>5. Time-Based Data → Line Chart</h2>

<p>
When data are ordered in time:
</p>

Examples:
<ul>
  <li>Monthly sales</li>
  <li>Yearly inflation rate</li>
</ul>

<p>
Correct graph:
</p>

<ul>
  <li>Line chart</li>
</ul>

<p>
Lines imply continuity across ordered points.
</p>

<hr>

<h2>6. Common Mistakes</h2>

<ul>
  <li>Using a histogram for categorical data</li>
  <li>Using a bar chart for continuous distribution shape</li>
  <li>Using line charts for unordered categories</li>
</ul>

<p>
Incorrect graph choice creates false visual meaning.
</p>

<hr>

<h2>7. Quick Decision Table</h2>

<table class="table">
  <thead>
    <tr>
      <th>Variable Type</th>
      <th>Recommended Graph</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Categorical</td>
      <td>Bar chart</td>
    </tr>
    <tr>
      <td>Numerical (one variable)</td>
      <td>Histogram</td>
    </tr>
    <tr>
      <td>Numerical (two variables)</td>
      <td>Scatterplot</td>
    </tr>
    <tr>
      <td>Time-ordered data</td>
      <td>Line chart</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Summary</h2>

<ul>
  <li>Always identify the variable type first.</li>
  <li>Categorical → Bar chart.</li>
  <li>Numerical → Histogram.</li>
  <li>Two numerical variables → Scatterplot.</li>
  <li>Time data → Line chart.</li>
</ul>

<p>
Correct visualization begins with correct classification.
</p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/visualization/bar-charts/">
    Next Lesson → Bar Charts
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_visualization_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/visualization/matching-graph-to-variable-type/",
      label: "Lesson 2 — Matching Graph Type to Variable Type",
      ts: Date.now()
    }));
  })();
</script>