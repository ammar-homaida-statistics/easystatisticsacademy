---
layout: default
title: "Data Structure & Datasets"
description: "Understanding rows, columns, observational units, and dataset organization."
permalink: /descriptive/data-variables/data-structure-datasets/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/data-variables/discrete-vs-continuous/">
    ← Previous Lesson: Discrete vs Continuous Variables
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
        This lesson structure is fixed. Examples and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

  <div class="section-head">
    <h1>Data Structure & Datasets</h1>
    <p>
      Before calculating anything, you must understand how data are organized.
      Most statistical errors begin with structural confusion.
    </p>
  </div>

  <h2>1. What Is a Dataset?</h2>

  <p>
    A dataset is a structured collection of observations and variables.
  </p>

  <p>
    In most statistical software and spreadsheets:
  </p>

  <ul>
    <li>Each <strong>row</strong> represents one observational unit.</li>
    <li>Each <strong>column</strong> represents one variable.</li>
  </ul>

  <hr>

  <h2>2. Observational Units</h2>

  <p>
    The observational unit is the entity being measured.
  </p>

  <h3>Examples:</h3>
  <ul>
    <li>One student</li>
    <li>One patient</li>
    <li>One company</li>
    <li>One country</li>
    <li>One time point</li>
  </ul>

  <p>
    All variables in a dataset must refer to the same observational unit.
  </p>

  <p>
    Mixing units creates invalid data.
  </p>

  <hr>

  <h2>3. Variables vs Values</h2>

  <p>
    A <strong>variable</strong> is a column.
  </p>

  <p>
    A <strong>value</strong> is the specific entry for one observation.
  </p>

  <h3>Example Table:</h3>

  <table class="table">
    <thead>
      <tr>
        <th>ID</th>
        <th>Age</th>
        <th>Gender</th>
        <th>Exam Score</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>20</td>
        <td>Female</td>
        <td>78</td>
      </tr>
      <tr>
        <td>2</td>
        <td>22</td>
        <td>Male</td>
        <td>85</td>
      </tr>
    </tbody>
  </table>

  <p>
    Age is a variable.  
    20 is a value.
  </p>

  <hr>

  <h2>4. Cross-Sectional vs Time-Series Data</h2>

  <h3>Cross-Sectional</h3>
  <p>
    Different units measured at the same time.
  </p>

  <p>Example: 100 patients measured today.</p>

  <h3>Time-Series</h3>
  <p>
    One unit measured repeatedly over time.
  </p>

  <p>Example: Daily stock price for one company.</p>

  <hr>

  <h2>5. Structured vs Messy Data</h2>

  <h3>Structured Data</h3>
  <ul>
    <li>One row = one unit</li>
    <li>One column = one variable</li>
    <li>No merged cells</li>
    <li>No multiple variables in one column</li>
  </ul>

  <h3>Messy Data Problems</h3>
  <ul>
    <li>Names and age in the same column</li>
    <li>Multiple time points in one row</li>
    <li>Missing identifiers</li>
    <li>Inconsistent coding</li>
  </ul>

  <p>
    Good descriptive statistics require clean structure first.
  </p>

  <hr>

  <h2>6. Why Structure Matters</h2>

  <ul>
    <li>Determines valid summaries</li>
    <li>Determines valid graphs</li>
    <li>Determines valid modeling</li>
    <li>Prevents logical contradictions</li>
  </ul>

  <p>
    Before describing data, always check:
  </p>

  <ul>
    <li>What is the unit?</li>
    <li>What are the variables?</li>
    <li>Is the structure consistent?</li>
  </ul>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/data-variables/measurement-scales/">
    Next Lesson → Measurement Scales
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_data_variables_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/data-variables/data-structure-datasets/",
      label: "Lesson 6 — Data Structure & Datasets",
      ts: Date.now()
    }));
  })();
</script>