---
layout: default
title: "Density Curves (Conceptual)"
description: "Understanding smooth distribution representation and the idea of area as proportion."
permalink: /descriptive/visualization/density-curves/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/visualization/histograms/">
    ← Previous Lesson: Histograms
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
        Visual comparisons with histograms and probability examples will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

<div class="section-head">
  <h1>Density Curves (Conceptual)</h1>
  <p>
    A density curve is a smooth representation of a distribution.
    It shows the overall shape without focusing on individual bars.
  </p>
</div>

<hr>

<h2>1. From Histogram to Smooth Curve</h2>

<p>
A histogram shows frequencies using bins.
</p>

<p>
If we smooth the histogram, we obtain a <strong>density curve</strong>.
</p>

<p>
The curve represents the overall distribution pattern.
</p>

<hr>

<h2>2. Area Represents Proportion</h2>

<p>
In a density curve:
</p>

<ul>
  <li>The total area under the curve equals 1 (or 100%).</li>
  <li>Area between two values represents proportion of observations.</li>
</ul>

<p>
This is the key idea that connects descriptive statistics to probability.
</p>

<hr>

<h2>3. Height Is Not Frequency</h2>

<p>
Important distinction:
</p>

<ul>
  <li>Histogram height → frequency (or density)</li>
  <li>Density curve height → relative density</li>
</ul>

<p>
The probability comes from <strong>area</strong>, not height.
</p>

<hr>

<h2>4. Shape Interpretation</h2>

Density curves help identify:

<ul>
  <li>Symmetry</li>
  <li>Right skew</li>
  <li>Left skew</li>
  <li>Peaks (modes)</li>
</ul>

<p>
The curve removes random noise from bin selection.
</p>

<hr>

<h2>5. Why Density Curves Matter</h2>

They prepare you for:

<ul>
  <li>Normal distribution</li>
  <li>Probability calculations</li>
  <li>Z-scores</li>
  <li>Confidence intervals</li>
</ul>

<p>
Understanding density curves is essential before moving to probability.
</p>

<hr>

<h2>6. Density Curve vs Histogram</h2>

<ul>
  <li>Histogram → Empirical counts</li>
  <li>Density curve → Smooth theoretical shape</li>
</ul>

<p>
They complement each other.
</p>

<hr>

<h2>Summary</h2>

<ul>
  <li>Density curves smooth histograms.</li>
  <li>Total area equals 1.</li>
  <li>Area represents proportion.</li>
  <li>Height alone does not represent probability.</li>
  <li>They bridge descriptive statistics and probability.</li>
</ul>

<p>
Density curves transform visualization into mathematical interpretation.
</p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/visualization/boxplots/">
    Next Lesson → Boxplots & Outliers
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_visualization_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/visualization/density-curves/",
      label: "Lesson 6 — Density Curves",
      ts: Date.now()
    }));
  })();
</script>