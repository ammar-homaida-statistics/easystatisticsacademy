---
layout: default
title: "Mean vs Median (Skewness, Outliers, and Choice Rules)"
description: "How to choose between mean and median using distribution shape, skewness, and outlier behavior."
permalink: /descriptive/center/mean-vs-median/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/center/mode/">
    ← Previous Lesson: Mode
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
        Visual examples, skewed distributions, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Mean vs Median</h1>
    <p>
      Choosing between mean and median depends on distribution shape, skewness,
      and the presence of outliers.
    </p>
  </div>

  <hr>

  <h2>1. When Mean and Median Are Similar</h2>

  <p>
    In symmetric distributions without extreme values:
  </p>

  <ul>
    <li>Mean ≈ Median</li>
    <li>Either measure represents the “center” well</li>
  </ul>

  <p>
    Example: exam scores clustered evenly around 70.
  </p>

  <hr>

  <h2>2. When Data Are Right-Skewed</h2>

  <p>
    In right-skewed distributions:
  </p>

  <ul>
    <li>Mean &gt; Median</li>
    <li>Extreme high values pull the mean upward</li>
  </ul>

  <p>
    Example: income data.
  </p>

  <hr>

  <h2>3. When Data Are Left-Skewed</h2>

  <p>
    In left-skewed distributions:
  </p>

  <ul>
    <li>Mean &lt; Median</li>
    <li>Extreme low values pull the mean downward</li>
  </ul>

  <hr>

  <h2>4. The Role of Outliers</h2>

  <ul>
    <li>Mean is sensitive to extreme values</li>
    <li>Median is robust to outliers</li>
  </ul>

  <p>
    A single extreme observation can shift the mean substantially,
    while the median may remain unchanged.
  </p>

  <hr>

  <h2>5. Practical Decision Rules</h2>

  <ul>
    <li>Use <strong>mean</strong> for symmetric numerical data without outliers.</li>
    <li>Use <strong>median</strong> for skewed data.</li>
    <li>Use <strong>median</strong> when outliers distort the mean.</li>
    <li>For ordinal data, median is usually appropriate.</li>
  </ul>

  <hr>

  <h2>6. Reporting Both</h2>

  <p>
    In professional reporting, both mean and median are often presented
    to describe distribution shape.
  </p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/center/weighted-mean/">
    Next Lesson → Weighted Mean
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_center_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/center/mean-vs-median/",
      label: "Lesson 5 — Mean vs Median (Skewness, Outliers, and Choice Rules)",
      ts: Date.now()
    }));
  })();
</script>