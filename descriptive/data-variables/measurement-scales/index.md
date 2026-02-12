---
layout: default
title: "Measurement Scales (Nominal, Ordinal, Interval, Ratio)"
description: "Understanding measurement scales and what mathematical operations are valid for each."
permalink: /descriptive/data-variables/measurement-scales/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/data-variables/data-structure-datasets/">
    ← Previous Lesson: Data Structure & Datasets
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
        Conceptual structure is fixed. More examples and applied cases will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

  <div class="section-head">
    <h1>Measurement Scales</h1>
    <p>
      Measurement scales determine what mathematical operations are valid.
      Using the wrong summary for a scale leads to incorrect conclusions.
    </p>
  </div>

  <h2>1. Nominal Scale</h2>

  <p>
    Categories without order.
  </p>

  <h3>Examples:</h3>
  <ul>
    <li>Gender</li>
    <li>Blood type</li>
    <li>Country</li>
  </ul>

  <h3>What is valid?</h3>
  <ul>
    <li>Counting</li>
    <li>Percentages</li>
    <li>Mode</li>
  </ul>

  <p>
    Arithmetic operations (mean, subtraction, ratios) are meaningless.
  </p>

  <hr>

  <h2>2. Ordinal Scale</h2>

  <p>
    Categories with order, but unequal spacing.
  </p>

  <h3>Examples:</h3>
  <ul>
    <li>Education level</li>
    <li>Satisfaction rating</li>
    <li>Pain severity</li>
  </ul>

  <h3>What is valid?</h3>
  <ul>
    <li>Ranking</li>
    <li>Median</li>
    <li>Percentiles</li>
  </ul>

  <p>
    Differences between levels are not precisely defined.
  </p>

  <hr>

  <h2>3. Interval Scale</h2>

  <p>
    Ordered values with equal intervals but no true zero.
  </p>

  <h3>Examples:</h3>
  <ul>
    <li>Temperature in Celsius</li>
    <li>IQ scores</li>
  </ul>

  <p>
    0°C does not mean “no temperature”.
  </p>

  <h3>What is valid?</h3>
  <ul>
    <li>Addition</li>
    <li>Subtraction</li>
    <li>Mean</li>
    <li>Standard deviation</li>
  </ul>

  <p>
    Ratios are not meaningful (20°C is not twice as hot as 10°C).
  </p>

  <hr>

  <h2>4. Ratio Scale</h2>

  <p>
    Ordered values with equal intervals and a true zero.
  </p>

  <h3>Examples:</h3>
  <ul>
    <li>Height</li>
    <li>Weight</li>
    <li>Income</li>
    <li>Time duration</li>
  </ul>

  <p>
    0 means absence of the quantity.
  </p>

  <h3>What is valid?</h3>
  <ul>
    <li>All arithmetic operations</li>
    <li>Ratios</li>
    <li>Geometric mean</li>
  </ul>

  <hr>

  <h2>5. Summary Table</h2>

  <table class="table">
    <thead>
      <tr>
        <th>Scale</th>
        <th>Order?</th>
        <th>Equal Intervals?</th>
        <th>True Zero?</th>
        <th>Mean Valid?</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Nominal</td>
        <td>No</td>
        <td>No</td>
        <td>No</td>
        <td>No</td>
      </tr>
      <tr>
        <td>Ordinal</td>
        <td>Yes</td>
        <td>No</td>
        <td>No</td>
        <td>Usually No</td>
      </tr>
      <tr>
        <td>Interval</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>No</td>
        <td>Yes</td>
      </tr>
      <tr>
        <td>Ratio</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
      </tr>
    </tbody>
  </table>

  <hr>

  <h2>6. Why This Matters for Descriptive Statistics</h2>

  <ul>
    <li>Mean requires interval or ratio scale.</li>
    <li>Median works for ordinal and above.</li>
    <li>Mode works for all scales.</li>
    <li>Variance requires numerical data.</li>
  </ul>

  <p>
    Scale determines which descriptive measures are mathematically valid.
  </p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/data-variables/valid-vs-invalid-operations/">
    Next Lesson → Valid vs Invalid Operations
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_data_variables_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/data-variables/measurement-scales/",
      label: "Lesson 7 — Measurement Scales",
      ts: Date.now()
    }));
  })();
</script>