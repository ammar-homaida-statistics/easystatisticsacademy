---
layout: default
title: "Valid vs Invalid Operations on Data"
description: "Understanding which mathematical operations are valid for different measurement scales."
permalink: /descriptive/data-variables/valid-vs-invalid-operations/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/data-variables/measurement-scales/">
    ← Previous Lesson: Measurement Scales
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
        Core framework is complete. Applied examples and software illustrations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

  <div class="section-head">
    <h1>Valid vs Invalid Operations on Data</h1>
    <p>
      Not every mathematical operation is meaningful for every type of data.
      Understanding this prevents serious statistical errors.
    </p>
  </div>

  <h2>1. Why This Lesson Matters</h2>

  <p>
    Many statistical mistakes occur when analysts apply formulas without checking
    whether the underlying scale allows those operations.
  </p>

  <p>
    Mathematics must match measurement.
  </p>

  <hr>

  <h2>2. Nominal Scale: Only Counting Is Valid</h2>

  <p><strong>Valid:</strong></p>
  <ul>
    <li>Counting frequencies</li>
    <li>Calculating proportions</li>
    <li>Finding the mode</li>
  </ul>

  <p><strong>Invalid:</strong></p>
  <ul>
    <li>Mean</li>
    <li>Standard deviation</li>
    <li>Ratios</li>
  </ul>

  <p>
    Example:
  </p>

  <p>
    If Gender is coded as 1 = Male, 2 = Female,
    the mean of Gender has no interpretation.
  </p>

  <hr>

  <h2>3. Ordinal Scale: Order Is Valid, Distance Is Not</h2>

  <p><strong>Valid:</strong></p>
  <ul>
    <li>Ranking</li>
    <li>Median</li>
    <li>Percentiles</li>
  </ul>

  <p><strong>Often Invalid:</strong></p>
  <ul>
    <li>Mean (unless strong justification exists)</li>
    <li>Standard deviation</li>
  </ul>

  <p>
    Example:
  </p>

  <p>
    Satisfaction levels coded 1–5:
    The difference between 1 and 2 may not equal the difference between 4 and 5.
  </p>

  <hr>

  <h2>4. Interval Scale: Differences Are Meaningful</h2>

  <p><strong>Valid:</strong></p>
  <ul>
    <li>Addition</li>
    <li>Subtraction</li>
    <li>Mean</li>
    <li>Variance</li>
  </ul>

  <p><strong>Invalid:</strong></p>
  <ul>
    <li>Ratios</li>
  </ul>

  <p>
    Example:
  </p>

  <p>
    20°C is not twice as hot as 10°C.
  </p>

  <hr>

  <h2>5. Ratio Scale: Full Arithmetic Is Valid</h2>

  <p><strong>Valid:</strong></p>
  <ul>
    <li>Addition</li>
    <li>Subtraction</li>
    <li>Multiplication</li>
    <li>Division</li>
    <li>Ratios</li>
    <li>Geometric mean</li>
  </ul>

  <p>
    Example:
  </p>

  <p>
    A person earning $60,000 earns twice as much as someone earning $30,000.
  </p>

  <hr>

  <h2>6. Practical Summary Table</h2>

  <table class="table">
    <thead>
      <tr>
        <th>Operation</th>
        <th>Nominal</th>
        <th>Ordinal</th>
        <th>Interval</th>
        <th>Ratio</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Count</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
      </tr>
      <tr>
        <td>Rank</td>
        <td>No</td>
        <td>Yes</td>
        <td>Yes</td>
        <td>Yes</td>
      </tr>
      <tr>
        <td>Mean</td>
        <td>No</td>
        <td>Usually No</td>
        <td>Yes</td>
        <td>Yes</td>
      </tr>
      <tr>
        <td>Ratios</td>
        <td>No</td>
        <td>No</td>
        <td>No</td>
        <td>Yes</td>
      </tr>
    </tbody>
  </table>

  <hr>

  <h2>7. The Core Principle</h2>

  <p>
    The scale determines the mathematics.
  </p>

  <p>
    If the mathematics does not match the scale,
    the result may be numerically correct — but conceptually wrong.
  </p>

  <p>
    Always ask:
  </p>

  <ul>
    <li>What is the measurement scale?</li>
    <li>Is this operation valid for that scale?</li>
  </ul>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/">
    → Return to Descriptive Statistics Section
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_data_variables_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/data-variables/valid-vs-invalid-operations/",
      label: "Lesson 8 — Valid vs Invalid Operations",
      ts: Date.now()
    }));
  })();
</script>