---
layout: default
title: "Choosing the Right Percentage (Row vs Column vs Total)"
description: "The most common cross-tab error: wrong denominator. Learn what row %, column %, and total % mean."
permalink: /descriptive/tabular-summaries/choosing-the-right-percentage/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/tabular-summaries/contingency-tables/">
    ← Previous Lesson: Contingency Tables (Cross-tabs)
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
        Additional applied case studies and reporting examples will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Choosing the Right Percentage</h1>
    <p>
      In contingency tables, the most common mistake is using the wrong denominator.
      Raw counts are not enough. Percentages must match the research question.
    </p>
  </div>

  <h2>1. Three Types of Percentages</h2>

  <ul>
    <li><strong>Row percentage</strong> → Within each row</li>
    <li><strong>Column percentage</strong> → Within each column</li>
    <li><strong>Total percentage</strong> → Out of the entire sample</li>
  </ul>

  <p>
    Each answers a different question.
  </p>

  <hr>

  <h2>2. Example Table (Counts)</h2>

  <table class="table">
    <thead>
      <tr>
        <th></th>
        <th>Group Study</th>
        <th>Individual Study</th>
        <th>Total</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Male</td>
        <td>8</td>
        <td>12</td>
        <td>20</td>
      </tr>
      <tr>
        <td>Female</td>
        <td>14</td>
        <td>6</td>
        <td>20</td>
      </tr>
      <tr>
        <td><strong>Total</strong></td>
        <td><strong>22</strong></td>
        <td><strong>18</strong></td>
        <td><strong>40</strong></td>
      </tr>
    </tbody>
  </table>

  <hr>

  <h2>3. Row Percentages (Within Gender)</h2>

  <p>
    Question: Among males, what percent prefer group study?
  </p>

  <ul>
    <li>Male group study = 8 / 20 = 40%</li>
    <li>Female group study = 14 / 20 = 70%</li>
  </ul>

  <p>
    Row percentages compare categories within each row group.
  </p>

  <p>
    Use row % when:
  </p>

  <ul>
    <li>You want to compare outcomes across row categories.</li>
    <li>The row variable defines the grouping of interest.</li>
  </ul>

  <hr>

  <h2>4. Column Percentages (Within Study Method)</h2>

  <p>
    Question: Among students who prefer group study, what percent are female?
  </p>

  <ul>
    <li>Female group study = 14 / 22 ≈ 64%</li>
    <li>Male group study = 8 / 22 ≈ 36%</li>
  </ul>

  <p>
    Column percentages compare categories within each column group.
  </p>

  <p>
    Use column % when:
  </p>

  <ul>
    <li>You want to compare row distribution inside each column category.</li>
  </ul>

  <hr>

  <h2>5. Total Percentages</h2>

  <p>
    Total percent uses the grand total (40 in this case).
  </p>

  <ul>
    <li>Female group study = 14 / 40 = 35%</li>
  </ul>

  <p>
    Total percent answers:
  </p>

  <ul>
    <li>What fraction of the entire sample is in this cell?</li>
  </ul>

  <p>
    It does not directly show association.
  </p>

  <hr>

  <h2>6. The Core Principle</h2>

  <p>
    The denominator must match the question.
  </p>

  <ul>
    <li>If asking “within males?” → use row %.</li>
    <li>If asking “within group study?” → use column %.</li>
    <li>If asking “out of entire sample?” → use total %.</li>
  </ul>

  <hr>

  <h2>7. Common Errors</h2>

  <ul>
    <li>Comparing raw counts when group sizes differ.</li>
    <li>Reporting total % when row % is required.</li>
    <li>Mixing row and column percentages in the same interpretation.</li>
    <li>Not stating which percentage is being used.</li>
  </ul>

  <p>
    Always state clearly:
  </p>

  <ul>
    <li>“Row percentages were calculated.”</li>
    <li>or “Column percentages were used.”</li>
  </ul>

  <p>
    Transparency prevents misleading interpretation.
  </p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/tabular-summaries/standard-table-layout-and-reporting/">
    Next Lesson → Standard Table Layout & Reporting
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_tabular_summaries_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/tabular-summaries/choosing-the-right-percentage/",
      label: "Lesson 8 — Choosing the Right Percentage",
      ts: Date.now()
    }));
  })();
</script>