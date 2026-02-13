---
layout: default
title: "Why Tables Come First"
description: "Why tables are the most reliable summary: clarity, auditability, and avoiding visual distortion."
permalink: /descriptive/tabular-summaries/why-tables-come-first/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/tabular-summaries/">
    ← Back to Block 2: Tabular Summaries
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
        This lesson is being developed. Content will be refined while preserving the structure and examples.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Why Tables Come First</h1>
    <p>
      Before charts, before means, before models: tables are the most reliable way to summarize data.
      They are precise, auditable, and harder to misread than visuals.
    </p>
  </div>

  <h2>1. What a Table Does (And What It Does Not)</h2>
  <p>
    A table organizes information into categories or intervals and reports exact values such as
    <strong>counts</strong>, <strong>proportions</strong>, and <strong>percentages</strong>.
  </p>
  <p>
    A table does not try to “look impressive.” It tries to be correct and transparent.
  </p>

  <h2>2. Tables Are Auditable</h2>
  <p>
    “Auditable” means: anyone can check the numbers.
    If a table says there are 42 observations in a category, a reader can verify it directly.
  </p>
  <p>
    Charts often hide small but important details (exact counts, denominator changes, missing values).
  </p>

  <h2>3. Tables Force You to Define the Denominator</h2>
  <p>
    The biggest source of descriptive mistakes is a hidden denominator:
  </p>
  <ul>
    <li>Are percentages out of the total sample?</li>
    <li>Or only out of non-missing values?</li>
    <li>Or out of a subgroup (row/column in a cross-tab)?</li>
  </ul>
  <p>
    A good table makes the denominator obvious.
  </p>

  <h2>4. Mini Example (Counts vs Percent)</h2>
  <p>Suppose you have 20 students and their department:</p>

  <table class="table">
    <thead>
      <tr>
        <th>Department</th>
        <th>Count</th>
        <th>Percent</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Math</td><td>8</td><td>40%</td></tr>
      <tr><td>Biology</td><td>7</td><td>35%</td></tr>
      <tr><td>Economics</td><td>5</td><td>25%</td></tr>
      <tr><td><strong>Total</strong></td><td><strong>20</strong></td><td><strong>100%</strong></td></tr>
    </tbody>
  </table>

  <p>
    From this table, the reader immediately knows:
  </p>
  <ul>
    <li>The total sample size (20)</li>
    <li>Exact counts per category</li>
    <li>Percentages that add to 100%</li>
  </ul>

  <h2>5. Why Charts Can Mislead (Even When Not Intentional)</h2>
  <p>Common issues:</p>
  <ul>
    <li>Missing values not shown (percentages look bigger than they should)</li>
    <li>Axis manipulation (bar chart scale exaggerates differences)</li>
    <li>Too many categories (readers cannot compare properly)</li>
    <li>Pie charts hide small differences and make comparisons hard</li>
  </ul>
  <p>
    A table may be less “visual,” but it is usually more honest.
  </p>

  <h2>6. Practical Rule for This Block</h2>
  <ul>
    <li>Start with tables to confirm counts, totals, and missingness.</li>
    <li>Then (later) use charts to communicate patterns.</li>
  </ul>

  <p>
    In the next lesson, we build frequency tables correctly — including what to do with missing values.
  </p>
</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/tabular-summaries/frequency-tables/">
    Next Lesson → Frequency Tables (Counts)
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_tabular_summaries_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/tabular-summaries/why-tables-come-first/",
      label: "Lesson 1 — Why Tables Come First",
      ts: Date.now()
    }));
  })();
</script>