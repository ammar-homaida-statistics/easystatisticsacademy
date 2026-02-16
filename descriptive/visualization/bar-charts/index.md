---
layout: default
title: "Bar Charts"
description: "Correct construction, scaling, labeling, and interpretation of categorical graphical summaries."
permalink: /descriptive/visualization/bar-charts/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/visualization/matching-graph-to-variable-type/">
    ← Previous Lesson: Matching Graph Type to Variable Type
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
        Visual examples, incorrect vs correct comparisons, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

<div class="section-head">
  <h1>Bar Charts</h1>
  <p>
    Bar charts are used to visualize <strong>categorical variables</strong>.
    They display counts or percentages for each category.
  </p>
</div>

<hr>

<h2>1. When to Use a Bar Chart</h2>

<p>
Use a bar chart when your variable is categorical.
</p>

Examples:
<ul>
  <li>Gender distribution</li>
  <li>Department choice</li>
  <li>Product category preference</li>
  <li>Education level</li>
</ul>

<p>
Each category is distinct and unordered (unless ordinal).
</p>

<hr>

<h2>2. Structure of a Proper Bar Chart</h2>

A correct bar chart must have:

<ul>
  <li>Clearly labeled categories (x-axis)</li>
  <li>Counts or percentages (y-axis)</li>
  <li>A meaningful title</li>
  <li>Equal bar widths</li>
  <li>Separated bars (no touching)</li>
</ul>

<p>
Separated bars indicate distinct categories.
</p>

<hr>

<h2>3. Counts vs Percentages</h2>

<p>
Bar charts may display:
</p>

<ul>
  <li>Frequency (counts)</li>
  <li>Relative frequency (percent)</li>
</ul>

<p>
Use percentages when:
</p>

<ul>
  <li>Comparing groups of different sizes</li>
  <li>Communicating proportions clearly</li>
</ul>

<p>
Always label the axis clearly:
</p>

<p><strong>Incorrect:</strong> "Students"</p>
<p><strong>Correct:</strong> "Percentage of Students (%)"</p>

<hr>

<h2>4. Ordering Categories</h2>

Bar charts may be ordered:

<ul>
  <li>Alphabetically</li>
  <li>By frequency (descending order)</li>
  <li>Logically (for ordinal variables)</li>
</ul>

<p>
Ordering by frequency often improves clarity.
</p>

<hr>

<h2>5. Common Bar Chart Mistakes</h2>

<ul>
  <li>Starting y-axis above zero</li>
  <li>Unequal bar widths</li>
  <li>3D distortion</li>
  <li>Too many categories</li>
  <li>Missing labels</li>
</ul>

<p>
The y-axis should generally start at zero to avoid exaggerating differences.
</p>

<hr>

<h2>6. Bar Chart vs Histogram</h2>

<p>
Do not confuse:
</p>

<ul>
  <li><strong>Bar chart</strong> → categorical data</li>
  <li><strong>Histogram</strong> → numerical continuous data</li>
</ul>

<p>
Bar chart bars are separated.  
Histogram bars touch.
</p>

<hr>

<h2>7. Interpreting a Bar Chart</h2>

When interpreting:

<ul>
  <li>Identify the highest category</li>
  <li>Identify the lowest category</li>
  <li>Compare differences carefully</li>
  <li>Avoid causal language</li>
</ul>

<p>
Bar charts describe distribution; they do not explain causes.
</p>

<hr>

<h2>Summary</h2>

<ul>
  <li>Bar charts are for categorical variables.</li>
  <li>Bars must be separated and equal width.</li>
  <li>Axis must be clearly labeled.</li>
  <li>Start y-axis at zero (in most cases).</li>
  <li>Interpret patterns responsibly.</li>
</ul>

<p>
A clean bar chart increases clarity.  
A distorted one increases confusion.
</p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/visualization/pie-charts/">
    Next Lesson → Pie Charts
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_visualization_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/visualization/bar-charts/",
      label: "Lesson 3 — Bar Charts",
      ts: Date.now()
    }));
  })();
</script>