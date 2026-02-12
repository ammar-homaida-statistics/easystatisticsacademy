---
layout: default
title: "Categorical vs Numerical Variables"
description: "The core data-type distinction that determines valid tables, plots, and summary measures."
permalink: /descriptive/data-variables/categorical-vs-numerical/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/data-variables/units-observations-and-variables/">
    ← Previous Lesson: Units, Observations & Variables
  </a>
</section>

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This lesson is being refined. The structure is stable and examples will be expanded.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Categorical vs Numerical Variables</h1>
    <p>
      This is one of the most important distinctions in descriptive statistics.
      Almost every statistical mistake begins with misidentifying the type of variable.
    </p>
  </div>

  <h2>1. Categorical Variables</h2>

  <p>
    A <strong>categorical variable</strong> places each observation into a group or category.
  </p>

  <p>Examples:</p>
  <ul>
    <li>Gender (Male, Female)</li>
    <li>Blood Type (A, B, AB, O)</li>
    <li>Department (Math, Biology, Economics)</li>
    <li>Satisfaction Level (Low, Medium, High)</li>
  </ul>

  <p>
    The values represent <strong>labels</strong>, not numerical magnitudes.
  </p>

  <h3>Key Rule:</h3>
  <p>
    You summarize categorical variables using:
  </p>
  <ul>
    <li>Frequency tables</li>
    <li>Percentages</li>
    <li>Bar charts</li>
  </ul>

  <p>
    You do <strong>not</strong> compute means or standard deviations for purely categorical data.
  </p>

  <h2>2. Numerical Variables</h2>

  <p>
    A <strong>numerical variable</strong> represents quantities where arithmetic operations are meaningful.
  </p>

  <p>Examples:</p>
  <ul>
    <li>Age</li>
    <li>Height (cm)</li>
    <li>Income</li>
    <li>Exam score</li>
  </ul>

  <p>
    For numerical variables, you can compute:
  </p>
  <ul>
    <li>Mean</li>
    <li>Median</li>
    <li>Variance</li>
    <li>Standard deviation</li>
  </ul>

  <h2>3. Why This Distinction Is Critical</h2>

  <p>
    Suppose you record:
  </p>

  <ul>
    <li>1 = Male</li>
    <li>2 = Female</li>
  </ul>

  <p>
    The numbers 1 and 2 are <strong>codes</strong>, not quantities.
  </p>

  <p>
    Calculating the mean of Gender would produce a number — but that number has no real interpretation.
  </p>

  <p>
    This is a classic beginner mistake.
  </p>

  <h2>4. A Mini Example</h2>

  <p>Dataset:</p>

  <table class="table">
    <thead>
      <tr>
        <th>Student</th>
        <th>Department</th>
        <th>Score</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>S1</td><td>Math</td><td>70</td></tr>
      <tr><td>S2</td><td>Biology</td><td>85</td></tr>
      <tr><td>S3</td><td>Math</td><td>90</td></tr>
      <tr><td>S4</td><td>Economics</td><td>65</td></tr>
    </tbody>
  </table>

  <p>
    Here:
  </p>

  <ul>
    <li><strong>Department</strong> → Categorical</li>
    <li><strong>Score</strong> → Numerical</li>
  </ul>

  <p>
    Valid summaries:
  </p>

  <ul>
    <li>Department → Count how many students in each department</li>
    <li>Score → Compute mean score (e.g., 77.5)</li>
  </ul>

  <h2>5. Warning: Some Variables Look Numerical But Are Not</h2>

  <p>Examples:</p>
  <ul>
    <li>Zip code</li>
    <li>Student ID</li>
    <li>Product code</li>
  </ul>

  <p>
    These contain numbers, but they are identifiers — not quantities.
  </p>

  <p>
    Arithmetic operations on them are meaningless.
  </p>

  <h2>6. Summary</h2>

  <ul>
    <li>Categorical → Labels or groups</li>
    <li>Numerical → Quantities with meaningful arithmetic</li>
    <li>Correct identification determines correct descriptive tools</li>
  </ul>

  <p>
    Everything in the next blocks (tables, graphs, mean, variance) depends on this classification.
  </p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/data-variables/nominal-vs-ordinal/">
    Next Lesson → Nominal vs Ordinal Variables
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_data_variables_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/data-variables/categorical-vs-numerical/",
      label: "Lesson 3 — Categorical vs Numerical Variables",
      ts: Date.now()
    }));
  })();
</script>