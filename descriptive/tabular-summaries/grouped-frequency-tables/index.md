---
layout: default
title: "Grouped Frequency Tables (Binning)"
description: "Turning continuous data into intervals: class width, boundaries, and the effect of bin choice."
permalink: /descriptive/tabular-summaries/grouped-frequency-tables/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/tabular-summaries/cumulative-frequency/">
    ← Previous Lesson: Cumulative Frequency & Cumulative Percent
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
        Applied examples and histogram comparisons will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Grouped Frequency Tables (Binning)</h1>
    <p>
      When data are continuous or have many unique values,
      listing each value separately is not informative.
      Instead, we group values into intervals (bins).
    </p>
  </div>

  <h2>1. Why Group Data?</h2>

  <p>
    Suppose we have 100 exam scores ranging from 0 to 100.
  </p>

  <p>
    A table listing every unique score would be long and unclear.
  </p>

  <p>
    Grouping into intervals reveals patterns more clearly.
  </p>

  <hr>

  <h2>2. Basic Structure of a Grouped Table</h2>

  <p>
    A grouped frequency table includes:
  </p>

  <ul>
    <li>Class intervals (e.g., 50–59)</li>
    <li>Frequency within each interval</li>
    <li>Total</li>
  </ul>

  <h3>Example</h3>

  <table class="table">
    <thead>
      <tr>
        <th>Score Interval</th>
        <th>Frequency</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>50–59</td><td>5</td></tr>
      <tr><td>60–69</td><td>12</td></tr>
      <tr><td>70–79</td><td>28</td></tr>
      <tr><td>80–89</td><td>35</td></tr>
      <tr><td>90–100</td><td>20</td></tr>
      <tr><td><strong>Total</strong></td><td><strong>100</strong></td></tr>
    </tbody>
  </table>

  <hr>

  <h2>3. Choosing Class Width</h2>

  <p>
    Class width = upper limit − lower limit.
  </p>

  <p>
    In the example above, width = 10.
  </p>

  <p>
    Too many bins → table becomes noisy.  
    Too few bins → important detail is lost.
  </p>

  <hr>

  <h2>4. Class Boundaries</h2>

  <p>
    Intervals must not overlap.
  </p>

  <p>
    Incorrect:
  </p>

  <ul>
    <li>50–60</li>
    <li>60–70</li>
  </ul>

  <p>
    Where does 60 belong?
  </p>

  <p>
    Correct approach:
  </p>

  <ul>
    <li>50–59</li>
    <li>60–69</li>
  </ul>

  <p>
    Or specify clearly:
  </p>

  <ul>
    <li>[50, 60)</li>
    <li>[60, 70)</li>
  </ul>

  <hr>

  <h2>5. Effect of Bin Choice</h2>

  <p>
    Changing bin width can change how the distribution looks.
  </p>

  <ul>
    <li>Wide bins smooth patterns.</li>
    <li>Narrow bins show more detail.</li>
  </ul>

  <p>
    The choice affects interpretation.
  </p>

  <hr>

  <h2>6. When to Use Grouped Tables</h2>

  <ul>
    <li>Continuous variables</li>
    <li>Large numerical datasets</li>
    <li>Preparation for histograms</li>
  </ul>

  <p>
    Grouped tables are the tabular foundation of histograms.
  </p>

  <hr>

  <h2>7. Common Mistakes</h2>

  <ul>
    <li>Overlapping intervals</li>
    <li>Unequal bin widths without explanation</li>
    <li>Forgetting to report total</li>
    <li>Too many or too few bins</li>
  </ul>

  <p>
    Always ensure intervals are clearly defined and consistent.
  </p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/tabular-summaries/contingency-tables/">
    Next Lesson → Contingency Tables (Cross-tabs)
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_tabular_summaries_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/tabular-summaries/grouped-frequency-tables/",
      label: "Lesson 6 — Grouped Frequency Tables (Binning)",
      ts: Date.now()
    }));
  })();
</script>