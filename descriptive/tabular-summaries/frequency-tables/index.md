---
layout: default
title: "Frequency Tables (Counts)"
description: "How to build frequency tables correctly: categories, missing values, ordering, and interpretation."
permalink: /descriptive/tabular-summaries/frequency-tables/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/tabular-summaries/why-tables-come-first/">
    ← Previous Lesson: Why Tables Come First
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
        This lesson is being developed. Examples and applied demonstrations will be expanded.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Frequency Tables (Counts)</h1>
    <p>
      A frequency table is the most basic and most important tabular summary.
      It shows how many observations fall into each category or value.
    </p>
  </div>

  <h2>1. What Is a Frequency?</h2>

  <p>
    A <strong>frequency</strong> is simply a count.
  </p>

  <p>
    If 12 students are in the Mathematics department, then the frequency of Mathematics = 12.
  </p>

  <hr>

  <h2>2. Basic Structure of a Frequency Table</h2>

  <p>
    A clean frequency table contains:
  </p>

  <ul>
    <li>Category (or value)</li>
    <li>Count (frequency)</li>
    <li>Total (optional but recommended)</li>
  </ul>

  <h3>Example</h3>

  <table class="table">
    <thead>
      <tr>
        <th>Department</th>
        <th>Frequency</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Math</td><td>8</td></tr>
      <tr><td>Biology</td><td>7</td></tr>
      <tr><td>Economics</td><td>5</td></tr>
      <tr><td><strong>Total</strong></td><td><strong>20</strong></td></tr>
    </tbody>
  </table>

  <p>
    The total confirms sample size.
  </p>

  <hr>

  <h2>3. Frequency Tables for Numerical Variables</h2>

  <p>
    For discrete numerical variables (e.g., number of children),
    each unique value may appear as its own row.
  </p>

  <h3>Example</h3>

  <table class="table">
    <thead>
      <tr>
        <th>Number of Children</th>
        <th>Frequency</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>0</td><td>4</td></tr>
      <tr><td>1</td><td>6</td></tr>
      <tr><td>2</td><td>5</td></tr>
      <tr><td>3</td><td>3</td></tr>
      <tr><td>4</td><td>2</td></tr>
      <tr><td><strong>Total</strong></td><td><strong>20</strong></td></tr>
    </tbody>
  </table>

  <p>
    For continuous variables, we later use grouped tables (next lessons).
  </p>

  <hr>

  <h2>4. Ordering Categories Correctly</h2>

  <p>
    Categories must be ordered logically:
  </p>

  <ul>
    <li>Alphabetical (nominal)</li>
    <li>Natural order (ordinal)</li>
    <li>Ascending numerical order</li>
  </ul>

  <p>
    Wrong ordering creates confusion.
  </p>

  <hr>

  <h2>5. What About Missing Values?</h2>

  <p>
    A proper frequency table should clarify whether missing values are:
  </p>

  <ul>
    <li>Excluded</li>
    <li>Reported separately</li>
  </ul>

  <p>
    Example:
  </p>

  <table class="table">
    <thead>
      <tr>
        <th>Response</th>
        <th>Frequency</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Yes</td><td>15</td></tr>
      <tr><td>No</td><td>3</td></tr>
      <tr><td>Missing</td><td>2</td></tr>
      <tr><td><strong>Total</strong></td><td><strong>20</strong></td></tr>
    </tbody>
  </table>

  <p>
    If missing values are ignored, percentages may become misleading.
  </p>

  <hr>

  <h2>6. Common Mistakes</h2>

  <ul>
    <li>Forgetting to include the total</li>
    <li>Hiding missing values</li>
    <li>Combining categories without explanation</li>
    <li>Using inconsistent category names</li>
  </ul>

  <p>
    A frequency table should always be clear, complete, and logically ordered.
  </p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/tabular-summaries/relative-frequency-and-percent/">
    Next Lesson → Relative Frequency & Percent
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_tabular_summaries_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/tabular-summaries/frequency-tables/",
      label: "Lesson 2 — Frequency Tables (Counts)",
      ts: Date.now()
    }));
  })();
</script>