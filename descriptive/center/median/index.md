---
layout: default
title: "Median"
description: "Definition, computation, robustness, and interpretation of the median as a measure of center."
permalink: /descriptive/center/median/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/center/arithmetic-mean/">
    ← Previous Lesson: Arithmetic Mean
  </a>
</section>

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5;border:2px solid #ff9800;padding:2rem;border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0;color:#e65100;font-size:1.8rem;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0;font-size:1.05rem;color:#5d4037;line-height:1.6;">
        Graphical comparisons (mean vs median), skewness illustrations, and software demonstrations (SPSS, R, Python, Excel) will be added in future updates.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Median</h1>
    <p class="lead">
      The median is the middle value of an ordered dataset.
      It divides the data into two equal halves.
    </p>
  </div>

  <hr>

  <h2>1. Definition</h2>

  <p>
    The median is the value that separates the lower 50% of observations
    from the upper 50%.
  </p>

  <p>
    It depends on <strong>order</strong>, not on magnitude.
  </p>

  <hr>

  <h2>2. How to Compute the Median</h2>

  <h3>Case 1: Odd Number of Observations</h3>

  <p>
    The median is the middle observation after sorting.
  </p>

  <p><strong>Example:</strong> 2, 5, 7, 9, 12</p>

  <p>
    Median = 7
  </p>

  <hr>

  <h3>Case 2: Even Number of Observations</h3>

  <p>
    The median is the average of the two middle values.
  </p>

  <p><strong>Example:</strong> 2, 5, 7, 9</p>

  <p>
    Median = (5 + 7) / 2 = 6
  </p>

  <hr>

  <h2>3. Robustness to Outliers</h2>

  <p><strong>Data:</strong> 5, 6, 7, 8, 100</p>

  <p>
    Ordered data: 5, 6, 7, 8, 100
  </p>

  <p>
    Median = 7
  </p>

  <p>
    Compare with mean (25.2).
  </p>

  <p>
    The median is <strong>robust</strong> to extreme values.
  </p>

  <hr>

  <h2>4. Interpretation in Skewed Distributions</h2>

  <ul>
    <li>Right-skewed: Mean &gt; Median</li>
    <li>Left-skewed: Mean &lt; Median</li>
    <li>Symmetric: Mean ≈ Median</li>
  </ul>

  <p>
    This relationship helps diagnose distribution shape.
  </p>

  <hr>

  <h2>5. When Is the Median Appropriate?</h2>

  <ul>
    <li>Skewed numerical distributions</li>
    <li>Presence of outliers</li>
    <li>Ordinal data (where ordering exists but averaging is questionable)</li>
  </ul>

  <p>
    The median is especially useful in:
  </p>

  <ul>
    <li>Income data</li>
    <li>House prices</li>
    <li>Waiting times</li>
  </ul>

  <hr>

  <h2>6. Conceptual Perspective</h2>

  <p>
    The median minimizes the sum of absolute deviations:
  </p>

  <p style="font-size:1.05rem;">
    Σ |xᵢ − median|
  </p>

  <p>
    This makes it a central measure from a different mathematical principle than the mean.
  </p>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>The median is the middle ordered value.</li>
    <li>It divides data into two equal halves.</li>
    <li>It is robust to outliers.</li>
    <li>It is preferred for skewed distributions.</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/center/mode/">
    Next Lesson → Mode
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_center_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/center/median/",
    label:"Lesson 3 — Median",
    ts:Date.now()
  }));
})();
</script>