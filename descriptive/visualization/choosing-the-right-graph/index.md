---
layout: default
title: "Choosing the Right Graph (Decision Framework)"
description: "A structured decision framework to choose the correct visualization based on variable type and purpose."
permalink: /descriptive/visualization/choosing-the-right-graph/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/visualization/misleading-graphs/">
    ← Previous Lesson: Misleading Graphs & Visual Manipulation
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
        Visual decision trees, flowcharts, and software examples will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

<div class="section-head">
  <h1>Choosing the Right Graph (Decision Framework)</h1>
  <p>
    Selecting the correct graph is not artistic — it is statistical.
    This framework ensures your visualization matches your variable type and analytical purpose.
  </p>
</div>

<hr>

<h2>Step 1 — How Many Variables?</h2>

<ul>
  <li><strong>One variable</strong> → Distribution summary</li>
  <li><strong>Two variables</strong> → Relationship or comparison</li>
  <li><strong>Time variable involved?</strong> → Trend visualization</li>
</ul>

<hr>

<h2>Step 2 — What Type of Variable?</h2>

<h3>Case A: Categorical Variable</h3>

<ul>
  <li>Bar chart (primary choice)</li>
  <li>Pie chart (limited use)</li>
</ul>

<p>
Avoid histograms for categorical data.
</p>

<hr>

<h3>Case B: Numerical Variable</h3>

<ul>
  <li>Histogram → distribution shape</li>
  <li>Boxplot → summary & outliers</li>
  <li>Density curve → smooth distribution</li>
</ul>

<p>
Avoid bar charts for continuous data.
</p>

<hr>

<h3>Case C: Two Numerical Variables</h3>

<ul>
  <li>Scatterplot → relationship pattern</li>
</ul>

<hr>

<h3>Case D: Numerical by Categorical</h3>

<ul>
  <li>Side-by-side boxplots</li>
  <li>Grouped bar charts (if summarized)</li>
</ul>

<hr>

<h2>Step 3 — What Is Your Goal?</h2>

<ul>
  <li>Show distribution → Histogram / Boxplot</li>
  <li>Compare categories → Bar chart</li>
  <li>Compare numerical across groups → Boxplot</li>
  <li>Show relationship → Scatterplot</li>
  <li>Show trend over time → Line graph</li>
</ul>

<hr>

<h2>Decision Summary Table</h2>

<table class="table">
  <thead>
    <tr>
      <th>Data Structure</th>
      <th>Best Graph</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1 categorical variable</td>
      <td>Bar chart</td>
    </tr>
    <tr>
      <td>1 numerical variable</td>
      <td>Histogram / Boxplot</td>
    </tr>
    <tr>
      <td>2 numerical variables</td>
      <td>Scatterplot</td>
    </tr>
    <tr>
      <td>Numerical by categorical</td>
      <td>Side-by-side boxplots</td>
    </tr>
    <tr>
      <td>Time series</td>
      <td>Line graph</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Common Mistake Checklist</h2>

<ul>
  <li>Using bar charts for continuous data</li>
  <li>Using histograms for categorical data</li>
  <li>Choosing graph before understanding variable type</li>
  <li>Ignoring the research question</li>
</ul>

<hr>

<h2>Professional Rule</h2>

<p>
Tables verify.
Graphs reveal.
Interpretation explains.
</p>

<p>
Never reverse this order.
</p>

<hr>

<h2>Summary</h2>

<ul>
  <li>Graph selection depends on variable type.</li>
  <li>Number of variables determines structure.</li>
  <li>Purpose determines final choice.</li>
  <li>Visualization is statistical logic, not decoration.</li>
</ul>

<p>
If you can justify your graph choice logically, you are thinking statistically.
</p>

</section>

<!-- Return to Descriptive Home -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/">
    Back to Descriptive Statistics →
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_visualization_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/visualization/choosing-the-right-graph/",
      label: "Lesson 11 — Choosing the Right Graph (Decision Framework)",
      ts: Date.now()
    }));
  })();
</script>