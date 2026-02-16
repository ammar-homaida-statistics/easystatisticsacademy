---
layout: default
title: "Scatterplots"
description: "Visualizing relationships between two numerical variables responsibly."
permalink: /descriptive/visualization/scatterplots/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/visualization/boxplots/">
    ← Previous Lesson: Boxplots & Outliers
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
        Real datasets, regression overlays, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

<div class="section-head">
  <h1>Scatterplots</h1>
  <p>
    A scatterplot visualizes the relationship between two numerical variables.
  </p>
</div>

<hr>

<h2>1. When Do We Use a Scatterplot?</h2>

<p>
Use a scatterplot when:
</p>

<ul>
  <li>Both variables are numerical.</li>
  <li>You want to explore association or relationship.</li>
</ul>

<p>
Example:
</p>

<ul>
  <li>Study hours vs exam score</li>
  <li>Age vs income</li>
  <li>Advertising spending vs sales</li>
</ul>

<hr>

<h2>2. Structure of a Scatterplot</h2>

<ul>
  <li>X-axis: explanatory (predictor) variable</li>
  <li>Y-axis: response variable</li>
  <li>Each point represents one observational unit</li>
</ul>

<p>
Each point = (x, y)
</p>

<hr>

<h2>3. What Do We Look For?</h2>

Scatterplots help identify:

<ul>
  <li><strong>Direction</strong> (positive or negative)</li>
  <li><strong>Form</strong> (linear or nonlinear)</li>
  <li><strong>Strength</strong> (tight or scattered pattern)</li>
  <li><strong>Outliers</strong></li>
</ul>

<hr>

<h2>4. Direction of Association</h2>

<strong>Positive association:</strong>  
As X increases, Y increases.

<strong>Negative association:</strong>  
As X increases, Y decreases.

<strong>No association:</strong>  
No clear pattern.

<hr>

<h2>5. Form of Relationship</h2>

<ul>
  <li>Linear pattern (straight line trend)</li>
  <li>Curved pattern</li>
  <li>Clustered pattern</li>
</ul>

<p>
Do not assume linearity without checking visually.
</p>

<hr>

<h2>6. Strength of Relationship</h2>

<p>
Strong relationship: points closely follow a pattern.  
Weak relationship: points widely scattered.
</p>

<p>
Visual strength precedes numerical correlation.
</p>

<hr>

<h2>7. Outliers in Scatterplots</h2>

<p>
Outliers may:
</p>

<ul>
  <li>Influence correlation</li>
  <li>Distort regression results</li>
  <li>Represent data errors</li>
</ul>

<p>
Always investigate before removing.
</p>

<hr>

<h2>8. Important Warning</h2>

<p>
Association does NOT imply causation.
</p>

<p>
A scatterplot shows relationship, not cause.
</p>

<hr>

<h2>Summary</h2>

<ul>
  <li>Scatterplots visualize relationships between two numerical variables.</li>
  <li>Look for direction, form, strength, and outliers.</li>
  <li>Use visuals before calculating correlation.</li>
  <li>Never interpret association as causation without proper design.</li>
</ul>

<p>
Scatterplots are the bridge from descriptive visualization to inferential analysis.
</p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/visualization/misleading-graphs/">
    Next Lesson → Misleading Graphs & Visual Manipulation
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_visualization_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/visualization/scatterplots/",
      label: "Lesson 8 — Scatterplots",
      ts: Date.now()
    }));
  })();
</script>