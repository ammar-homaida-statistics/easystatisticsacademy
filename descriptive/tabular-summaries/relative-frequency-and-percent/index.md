---
layout: default
title: "Relative Frequency & Percent"
description: "Proportions vs percent, percent points, and common mistakes in percentage interpretation."
permalink: /descriptive/tabular-summaries/relative-frequency-and-percent/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/tabular-summaries/frequency-tables/">
    ← Previous Lesson: Frequency Tables (Counts)
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
        This lesson is being expanded. More applied examples and software demonstrations will be added.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Relative Frequency & Percent</h1>
    <p>
      A count tells you how many.  
      A relative frequency tells you how large that count is compared to the total.
    </p>
  </div>

  <h2>1. What Is Relative Frequency?</h2>

  <p>
    Relative frequency = frequency ÷ total number of observations.
  </p>

  <p>
    It expresses the proportion of observations in a category.
  </p>

  <p>
    Formula:
  </p>

  <p><strong>Relative Frequency = f / n</strong></p>

  <hr>

  <h2>2. What Is Percent?</h2>

  <p>
    Percent is simply relative frequency multiplied by 100.
  </p>

  <p><strong>Percent = (f / n) × 100</strong></p>

  <p>
    Percent is easier for communication, but it hides the denominator.
  </p>

  <hr>

  <h2>3. Example</h2>

  <p>
    Suppose we survey 20 students about preferred study method.
  </p>

  <table class="table">
    <thead>
      <tr>
        <th>Method</th>
        <th>Frequency</th>
        <th>Relative Frequency</th>
        <th>Percent</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Group Study</td>
        <td>8</td>
        <td>0.40</td>
        <td>40%</td>
      </tr>
      <tr>
        <td>Individual Study</td>
        <td>12</td>
        <td>0.60</td>
        <td>60%</td>
      </tr>
      <tr>
        <td><strong>Total</strong></td>
        <td><strong>20</strong></td>
        <td><strong>1.00</strong></td>
        <td><strong>100%</strong></td>
      </tr>
    </tbody>
  </table>

  <p>
    The table confirms:
  </p>

  <ul>
    <li>Counts add to 20</li>
    <li>Relative frequencies add to 1</li>
    <li>Percentages add to 100%</li>
  </ul>

  <hr>

  <h2>4. Why Denominator Awareness Matters</h2>

  <p>
    Suppose 5 students did not respond.
  </p>

  <p>
    Now:
  </p>

  <ul>
    <li>Total sample size = 25</li>
    <li>Valid responses = 20</li>
  </ul>

  <p>
    If you compute percent using 20, you get:
  </p>

  <ul>
    <li>8 / 20 = 40%</li>
  </ul>

  <p>
    But if you compute percent using 25:
  </p>

  <ul>
    <li>8 / 25 = 32%</li>
  </ul>

  <p>
    Same count. Different percent.  
    The denominator changes the interpretation.
  </p>

  <hr>

  <h2>5. Percent vs Percentage Points</h2>

  <p>
    If approval increases from 40% to 50%:
  </p>

  <ul>
    <li>It increased by 10 percentage points.</li>
    <li>It increased by 25% relative change.</li>
  </ul>

  <p>
    These are not the same.
  </p>

  <hr>

  <h2>6. Common Mistakes</h2>

  <ul>
    <li>Reporting percent without reporting sample size</li>
    <li>Comparing percentages from different denominators</li>
    <li>Ignoring missing values when computing percent</li>
    <li>Rounding errors that prevent totals from equaling 100%</li>
  </ul>

  <p>
    Always check:
  </p>

  <ul>
    <li>What is the denominator?</li>
    <li>Do percentages sum correctly?</li>
  </ul>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/tabular-summaries/handling-missing-values/">
    Next Lesson → Handling Missing Values in Tables
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_tabular_summaries_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/tabular-summaries/relative-frequency-and-percent/",
      label: "Lesson 3 — Relative Frequency & Percent",
      ts: Date.now()
    }));
  })();
</script>