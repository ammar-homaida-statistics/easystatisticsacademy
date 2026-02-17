---
layout: default
title: "Mini Case Study (End-to-End Descriptive Report)"
description: An end-to-end example: dataset → tables → graphs → structured interpretation → responsible reporting.
permalink: /descriptive/reporting/mini-case-study-end-to-end/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/reporting/outliers-and-exclusions/">
    ← Previous Lesson: Outliers, Exclusions, and Transparency
  </a>
</section>

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5;border:2px solid #ff9800;padding:2rem;border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0;color:#e65100;font-size:1.8rem;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0;font-size:1.05rem;color:#5d4037;line-height:1.6;">
        A full worked dataset, visualizations, and downloadable practice file will be added.
        This lesson will integrate all previous blocks.
      </p>
    </div>
  </div>
</section>

<section class="section">

  <div class="section-head">
    <h1>Mini Case Study: From Raw Data to Clear Message</h1>
    <p class="lead">
      This lesson demonstrates how to move from raw data to a complete,
      structured, responsible descriptive report.
    </p>
  </div>

  <hr>

  <h2>Scenario</h2>

  <p>
    A university collected exam scores (0–100 scale) from 120 students.
    We want to describe overall performance clearly and responsibly.
  </p>

  <hr>

  <h2>Step 1 — Describe the Dataset</h2>

  <ul>
    <li>Variable: Exam score</li>
    <li>Scale: Numeric (interval)</li>
    <li>Sample size: n = 120</li>
    <li>Missing values: 2</li>
  </ul>

  <p>
    Always start by defining what you are describing.
  </p>

  <hr>

  <h2>Step 2 — Measures of Center</h2>

  <ul>
    <li>Mean = 71.8</li>
    <li>Median = 74</li>
    <li>Mode = 78</li>
  </ul>

  <p>
    The median is slightly higher than the mean,
    suggesting possible left skew (low extreme scores).
  </p>

  <hr>

  <h2>Step 3 — Measures of Spread</h2>

  <ul>
    <li>Standard deviation = 12.4</li>
    <li>IQR = 16</li>
    <li>Range = 48</li>
  </ul>

  <p>
    The spread suggests moderate variability in student performance.
  </p>

  <hr>

  <h2>Step 4 — Shape</h2>

  <ul>
    <li>Distribution slightly left-skewed</li>
    <li>Two low extreme scores</li>
  </ul>

  <p>
    Because of skewness, the median may better represent the “typical” student.
  </p>

  <hr>

  <h2>Step 5 — Interpretation (Structured Paragraph)</h2>

  <blockquote>
    Exam scores (n = 120) had a median of 74 and a mean of 71.8 (SD = 12.4).
    The distribution was slightly left-skewed due to a small number of low scores.
    Most students performed between 66 and 82 (IQR = 16).
    Overall performance was moderate with moderate variability.
  </blockquote>

  <hr>

  <h2>What This Example Demonstrates</h2>

  <ul>
    <li>Define the variable and sample first</li>
    <li>Report center and spread together</li>
    <li>Describe shape if relevant</li>
    <li>Avoid causal claims</li>
    <li>Write a structured, neutral interpretation</li>
  </ul>

  <hr>

  <h2>Final Principle</h2>

  <p>
    Descriptive statistics are not just calculations.
    They are structured communication.
  </p>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/">
    Back to Descriptive Statistics →
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_reporting_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/reporting/mini-case-study-end-to-end/",
    label:"Lesson 9 — Mini Case Study (End-to-End Descriptive Report)",
    ts:Date.now()
  }));
})();
</script>