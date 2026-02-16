---
layout: default
title: "Histograms"
description: "Understanding distribution shape, bin width, and correct interpretation of continuous data."
permalink: /descriptive/visualization/histograms/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/visualization/pie-charts/">
    ← Previous Lesson: Pie Charts
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
        Visual examples (skewed, symmetric, multimodal distributions) and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

<div class="section-head">
  <h1>Histograms</h1>
  <p>
    Histograms are used to visualize <strong>numerical continuous data</strong>.
    They reveal the shape of a distribution.
  </p>
</div>

<hr>

<h2>1. When to Use a Histogram</h2>

Use a histogram when:

<ul>
  <li>The variable is numerical</li>
  <li>The variable is continuous (or approximately continuous)</li>
  <li>You want to understand distribution shape</li>
</ul>

Examples:
<ul>
  <li>Exam scores</li>
  <li>Income</li>
  <li>Age</li>
  <li>Height</li>
</ul>

<hr>

<h2>2. How a Histogram Is Constructed</h2>

A histogram:

<ul>
  <li>Groups values into intervals (bins)</li>
  <li>Counts how many observations fall in each interval</li>
  <li>Displays bars that touch</li>
</ul>

<p>
Bars touch because the data are continuous.
</p>

<hr>

<h2>3. Bin Width Matters</h2>

Bin width determines how the data appear.

If bins are:
<ul>
  <li><strong>Too wide</strong> → Important detail disappears</li>
  <li><strong>Too narrow</strong> → Graph looks noisy</li>
</ul>

<p>
Different bin choices can create different visual impressions.
</p>

<hr>

<h2>4. What a Histogram Reveals</h2>

Histograms allow us to see:

<ul>
  <li>Symmetry</li>
  <li>Skewness (left or right)</li>
  <li>Outliers</li>
  <li>Clusters</li>
  <li>Multimodality (multiple peaks)</li>
</ul>

<p>
This is impossible to see clearly from a raw table.
</p>

<hr>

<h2>5. Symmetric Distribution</h2>

In a symmetric distribution:

<ul>
  <li>Left and right sides mirror each other</li>
  <li>Mean ≈ Median</li>
</ul>

<p>
This pattern often appears in natural measurement processes.
</p>

<hr>

<h2>6. Skewed Distribution</h2>

Right-skewed:
<ul>
  <li>Long tail on the right</li>
  <li>Mean > Median</li>
</ul>

Left-skewed:
<ul>
  <li>Long tail on the left</li>
  <li>Mean < Median</li>
</ul>

<p>
Understanding skewness prepares you for inference later.
</p>

<hr>

<h2>7. Histogram vs Bar Chart</h2>

Do not confuse:

<ul>
  <li><strong>Histogram</strong> → Continuous numerical data</li>
  <li><strong>Bar chart</strong> → Categorical data</li>
</ul>

Differences:

<ul>
  <li>Histogram bars touch</li>
  <li>Bar chart bars are separated</li>
</ul>

<hr>

<h2>8. Common Mistakes</h2>

<ul>
  <li>Using histogram for categorical data</li>
  <li>Not labeling axis clearly</li>
  <li>Using extreme bin widths</li>
  <li>Interpreting small fluctuations as meaningful patterns</li>
</ul>

<hr>

<h2>Summary</h2>

<ul>
  <li>Histograms visualize continuous numerical data.</li>
  <li>Bin width affects interpretation.</li>
  <li>They reveal distribution shape.</li>
  <li>They prepare you for understanding mean, median, and spread.</li>
</ul>

<p>
A histogram is not decoration — it is the foundation of distribution analysis.
</p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/visualization/density-curves/">
    Next Lesson → Density Curves
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_visualization_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/visualization/histograms/",
      label: "Lesson 5 — Histograms",
      ts: Date.now()
    }));
  })();
</script>