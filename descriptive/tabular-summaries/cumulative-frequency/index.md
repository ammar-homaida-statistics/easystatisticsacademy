---
layout: default
title: "Cumulative Frequency & Cumulative Percent"
description: "Distribution buildup: how to read cumulative summaries and why they matter for percentiles."
permalink: /descriptive/tabular-summaries/cumulative-frequency/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/tabular-summaries/handling-missing-values/">
    ← Previous Lesson: Handling Missing Values in Tables
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
        Applied examples and graphical interpretation will be expanded later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Cumulative Frequency & Cumulative Percent</h1>
    <p>
      Cumulative summaries show how a distribution builds up from the smallest value to the largest.
      They are essential for understanding percentiles and distribution shape.
    </p>
  </div>

  <h2>1. What Is Cumulative Frequency?</h2>

  <p>
    Cumulative frequency is the running total of frequencies up to a given category or value.
  </p>

  <p>
    It answers:
  </p>

  <ul>
    <li>How many observations are at or below this value?</li>
  </ul>

  <hr>

  <h2>2. Example</h2>

  <p>
    Suppose we have test scores from 20 students:
  </p>

  <table class="table">
    <thead>
      <tr>
        <th>Score</th>
        <th>Frequency</th>
        <th>Cumulative Frequency</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>50–59</td><td>2</td><td>2</td></tr>
      <tr><td>60–69</td><td>4</td><td>6</td></tr>
      <tr><td>70–79</td><td>7</td><td>13</td></tr>
      <tr><td>80–89</td><td>5</td><td>18</td></tr>
      <tr><td>90–100</td><td>2</td><td>20</td></tr>
    </tbody>
  </table>

  <p>
    Interpretation:
  </p>

  <ul>
    <li>6 students scored below 70.</li>
    <li>13 students scored below 80.</li>
    <li>All 20 students are included by the last row.</li>
  </ul>

  <hr>

  <h2>3. What Is Cumulative Percent?</h2>

  <p>
    Cumulative percent = (cumulative frequency ÷ total) × 100
  </p>

  <table class="table">
    <thead>
      <tr>
        <th>Score</th>
        <th>Cumulative Percent</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>50–59</td><td>10%</td></tr>
      <tr><td>60–69</td><td>30%</td></tr>
      <tr><td>70–79</td><td>65%</td></tr>
      <tr><td>80–89</td><td>90%</td></tr>
      <tr><td>90–100</td><td>100%</td></tr>
    </tbody>
  </table>

  <p>
    Now we can say:
  </p>

  <ul>
    <li>65% of students scored below 80.</li>
    <li>90% scored below 90.</li>
  </ul>

  <hr>

  <h2>4. Why Cumulative Tables Matter</h2>

  <ul>
    <li>They allow percentile interpretation.</li>
    <li>They help identify medians.</li>
    <li>They show distribution buildup.</li>
    <li>They help compare performance thresholds.</li>
  </ul>

  <hr>

  <h2>5. Important Rules</h2>

  <ul>
    <li>Cumulative frequency must always increase.</li>
    <li>The final cumulative frequency must equal total n.</li>
    <li>Cumulative percent must end at 100%.</li>
  </ul>

  <hr>

  <h2>6. Common Mistakes</h2>

  <ul>
    <li>Using cumulative percent for nominal categories (not valid).</li>
    <li>Incorrect ordering of categories.</li>
    <li>Arithmetic errors in running totals.</li>
    <li>Interpreting cumulative percent as category percent.</li>
  </ul>

  <p>
    Cumulative summaries are meaningful only when data have a natural order.
  </p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/tabular-summaries/grouped-frequency-tables/">
    Next Lesson → Grouped Frequency Tables (Binning)
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_tabular_summaries_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/tabular-summaries/cumulative-frequency/",
      label: "Lesson 5 — Cumulative Frequency & Cumulative Percent",
      ts: Date.now()
    }));
  })();
</script>