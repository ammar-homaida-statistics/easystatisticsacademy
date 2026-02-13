---
layout: default
title: "Handling Missing Values in Tables"
description: "When to exclude, include, or report missing; how missingness changes denominators and conclusions."
permalink: /descriptive/tabular-summaries/handling-missing-values/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/tabular-summaries/relative-frequency-and-percent/">
    ← Previous Lesson: Relative Frequency & Percent
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
        This lesson will later include applied reporting examples and software demonstrations.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Handling Missing Values in Tables</h1>
    <p>
      Missing values are not a minor detail.  
      They directly affect percentages, interpretation, and conclusions.
    </p>
  </div>

  <h2>1. What Is a Missing Value?</h2>

  <p>
    A missing value occurs when data for a variable is not recorded or not available.
  </p>

  <p>
    Common reasons:
  </p>

  <ul>
    <li>Participant skipped the question</li>
    <li>Data entry error</li>
    <li>Question not applicable</li>
    <li>System recording failure</li>
  </ul>

  <hr>

  <h2>2. Why Missing Values Matter</h2>

  <p>
    Missing values change the denominator.
  </p>

  <p>
    And when the denominator changes, percentages change.
  </p>

  <hr>

  <h2>3. Example: Including vs Excluding Missing</h2>

  <p>
    Suppose 25 people were surveyed.
  </p>

  <ul>
    <li>15 answered “Yes”</li>
    <li>5 answered “No”</li>
    <li>5 did not respond</li>
  </ul>

  <h3>Table 1: Including Missing</h3>

  <table class="table">
    <thead>
      <tr>
        <th>Response</th>
        <th>Frequency</th>
        <th>Percent (Total = 25)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Yes</td><td>15</td><td>60%</td></tr>
      <tr><td>No</td><td>5</td><td>20%</td></tr>
      <tr><td>Missing</td><td>5</td><td>20%</td></tr>
      <tr><td><strong>Total</strong></td><td><strong>25</strong></td><td><strong>100%</strong></td></tr>
    </tbody>
  </table>

  <h3>Table 2: Excluding Missing</h3>

  <table class="table">
    <thead>
      <tr>
        <th>Response</th>
        <th>Frequency</th>
        <th>Valid Percent (Total = 20)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Yes</td><td>15</td><td>75%</td></tr>
      <tr><td>No</td><td>5</td><td>25%</td></tr>
      <tr><td><strong>Total (Valid)</strong></td><td><strong>20</strong></td><td><strong>100%</strong></td></tr>
    </tbody>
  </table>

  <p>
    Same data. Very different percentages.
  </p>

  <hr>

  <h2>4. When Should Missing Be Reported?</h2>

  <ul>
    <li>When missingness is large</li>
    <li>When missingness may bias results</li>
    <li>In academic research</li>
    <li>In surveys and official reports</li>
  </ul>

  <p>
    Hiding missing values can mislead readers.
  </p>

  <hr>

  <h2>5. Valid Percent vs Percent</h2>

  <p>
    Many statistical software packages report:
  </p>

  <ul>
    <li><strong>Percent</strong> → based on total sample size</li>
    <li><strong>Valid Percent</strong> → based on non-missing observations</li>
  </ul>

  <p>
    Always check which one you are using.
  </p>

  <hr>

  <h2>6. Reporting Guidelines</h2>

  <ul>
    <li>Always state the total sample size (n).</li>
    <li>Report number of missing values.</li>
    <li>Clarify whether percentages are based on total or valid cases.</li>
    <li>Never let the denominator be hidden.</li>
  </ul>

  <p>
    Transparency builds trust in descriptive statistics.
  </p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/tabular-summaries/cumulative-frequency/">
    Next Lesson → Cumulative Frequency & Cumulative Percent
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_tabular_summaries_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/tabular-summaries/handling-missing-values/",
      label: "Lesson 4 — Handling Missing Values in Tables",
      ts: Date.now()
    }));
  })();
</script>