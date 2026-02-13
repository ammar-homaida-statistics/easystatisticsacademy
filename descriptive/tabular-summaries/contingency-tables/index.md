---
layout: default
title: "Contingency Tables (Cross-tabs)"
description: "Two-way tables and what they answer: association patterns using correct totals."
permalink: /descriptive/tabular-summaries/contingency-tables/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/tabular-summaries/grouped-frequency-tables/">
    ← Previous Lesson: Grouped Frequency Tables (Binning)
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
        Advanced interpretation examples and software outputs will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Contingency Tables (Cross-tabs)</h1>
    <p>
      A contingency table (or cross-tabulation) summarizes the relationship between two categorical variables.
    </p>
  </div>

  <h2>1. What Is a Contingency Table?</h2>

  <p>
    It is a two-way table that shows how frequencies are distributed across combinations of categories.
  </p>

  <p>
    It answers:
  </p>

  <ul>
    <li>How does one variable vary across categories of another?</li>
    <li>Is there a pattern of association?</li>
  </ul>

  <hr>

  <h2>2. Example</h2>

  <p>
    Suppose we survey 40 students about gender and preferred study method.
  </p>

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

  <h2>3. What Can We See?</h2>

  <p>
    Raw counts show:
  </p>

  <ul>
    <li>More females prefer group study (14 vs 8 males).</li>
    <li>More males prefer individual study (12 vs 6 females).</li>
  </ul>

  <p>
    But raw counts alone are not enough.
  </p>

  <hr>

  <h2>4. Why Percentages Matter</h2>

  <p>
    To interpret association correctly, we need row or column percentages.
  </p>

  <p>
    For example, row percentages (within gender):
  </p>

  <ul>
    <li>Male: 8/20 = 40% group study</li>
    <li>Female: 14/20 = 70% group study</li>
  </ul>

  <p>
    Now the comparison is clearer.
  </p>

  <hr>

  <h2>5. Marginal Totals</h2>

  <p>
    Marginal totals are the row and column totals.
  </p>

  <ul>
    <li>Row totals → total per gender</li>
    <li>Column totals → total per study method</li>
  </ul>

  <p>
    The grand total is the total sample size.
  </p>

  <hr>

  <h2>6. What Contingency Tables Do Not Prove</h2>

  <ul>
    <li>They do not prove causation.</li>
    <li>They do not test statistical significance (that comes later).</li>
    <li>They only describe association patterns.</li>
  </ul>

  <hr>

  <h2>7. Common Mistakes</h2>

  <ul>
    <li>Comparing raw counts without considering group sizes.</li>
    <li>Using the wrong percentage (row vs column).</li>
    <li>Ignoring small sample sizes.</li>
    <li>Drawing causal conclusions from descriptive data.</li>
  </ul>

  <p>
    Proper interpretation requires choosing the correct denominator — which is the next lesson.
  </p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/tabular-summaries/choosing-the-right-percentage/">
    Next Lesson → Choosing the Right Percentage
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_tabular_summaries_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/tabular-summaries/contingency-tables/",
      label: "Lesson 7 — Contingency Tables (Cross-tabs)",
      ts: Date.now()
    }));
  })();
</script>