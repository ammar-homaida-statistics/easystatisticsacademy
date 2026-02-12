---
layout: default
title: "Units, Observations & Variables"
description: "Observational units, variables vs values, and how datasets represent real-world entities."
permalink: /descriptive/data-variables/units-observations-and-variables/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/data-variables/what-does-it-mean-to-describe-data/">
    ← Previous Lesson: What Does It Mean to “Describe” Data?
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
        This lesson is being developed. Content will be expanded while preserving the structure and examples.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Units, Observations &amp; Variables</h1>
    <p>
      Before you compute any table, plot, mean, or standard deviation, you must know exactly what your dataset
      represents. This lesson defines the core building blocks of a dataset: the <strong>unit</strong>, the
      <strong>observation</strong>, and the <strong>variable</strong>.
    </p>
  </div>

  <h2>1. Observational Unit</h2>
  <p>
    The <strong>observational unit</strong> (often called the <em>unit of analysis</em>) is the “thing” you are measuring.
    It is the entity that each row in your dataset typically represents.
  </p>

  <p>Examples of observational units:</p>
  <ul>
    <li><strong>Person</strong> (patient, student, customer)</li>
    <li><strong>Household</strong></li>
    <li><strong>Company</strong></li>
    <li><strong>Country</strong></li>
    <li><strong>Day</strong> (for time series)</li>
    <li><strong>Transaction</strong> (purchase event)</li>
  </ul>

  <p>
    Choosing the wrong unit leads to incorrect summaries and invalid conclusions.
  </p>

  <h2>2. Observation (Row)</h2>
  <p>
    An <strong>observation</strong> is one recorded unit (one case). In most datasets, each row corresponds to one observation.
  </p>

  <p>
    Example: if your unit is a student, then each row is one student. If your unit is a transaction, then each row is one transaction.
  </p>

  <h2>3. Variable (Column)</h2>
  <p>
    A <strong>variable</strong> is a characteristic measured on each observational unit.
    In most datasets, each column is one variable.
  </p>

  <p>Examples of variables for a student dataset:</p>
  <ul>
    <li>Age</li>
    <li>Gender</li>
    <li>Department</li>
    <li>Study hours per week</li>
    <li>Exam score</li>
  </ul>

  <h2>4. Values (Cells)</h2>
  <p>
    A <strong>value</strong> is the recorded measurement for one variable in one observation (one cell of the dataset).
  </p>

  <p>
    Example: “Exam score = 72” is a value for one student (one row) under the “Exam score” variable (one column).
  </p>

  <h2>5. A Concrete Dataset Example</h2>
  <p>
    Consider a dataset with 4 students:
  </p>

  <table class="table">
    <thead>
      <tr>
        <th>Student_ID</th>
        <th>Age</th>
        <th>Study_Hours</th>
        <th>Score</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>S01</td><td>20</td><td>5</td><td>65</td></tr>
      <tr><td>S02</td><td>21</td><td>7</td><td>70</td></tr>
      <tr><td>S03</td><td>20</td><td>8</td><td>72</td></tr>
      <tr><td>S04</td><td>22</td><td>12</td><td>90</td></tr>
    </tbody>
  </table>

  <ul>
    <li><strong>Unit:</strong> student</li>
    <li><strong>Observations:</strong> 4 students (4 rows)</li>
    <li><strong>Variables:</strong> Student_ID, Age, Study_Hours, Score (4 columns)</li>
    <li><strong>Value example:</strong> Score for S03 is 72</li>
  </ul>

  <h2>6. Variables vs Values: Common Confusions</h2>
  <p>Typical mistakes:</p>
  <ul>
    <li>Confusing a category value with a variable (e.g., “Male” is not a variable; “Gender” is the variable).</li>
    <li>Confusing an ID column with a meaningful variable (IDs identify units; they are usually not analyzed as numeric values).</li>
    <li>Treating repeated measures as different people (unit confusion).</li>
  </ul>

  <h2>7. When Units Change: Repeated Measures (Important)</h2>
  <p>
    Sometimes you measure the same person multiple times (e.g., blood pressure at multiple visits).
    Then the dataset can be organized in different ways:
  </p>

  <ul>
    <li><strong>Unit = person</strong> (one row per person, multiple columns for time points)</li>
    <li><strong>Unit = measurement occasion</strong> (one row per measurement, includes person ID and time)</li>
  </ul>

  <p>
    Both can be valid, but they lead to different summaries and analyses. Always state your unit clearly.
  </p>

  <h2>8. Why This Lesson Matters for Descriptive Statistics</h2>
  <p>
    Descriptive statistics depends on correct dataset understanding:
  </p>
  <ul>
    <li>You cannot summarize correctly if the unit is unclear.</li>
    <li>You cannot choose correct plots if variable roles are confused.</li>
    <li>You cannot interpret results if rows and columns are misunderstood.</li>
  </ul>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/data-variables/categorical-vs-numerical/">
    Next Lesson → Categorical vs Numerical Variables
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_data_variables_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/data-variables/units-observations-and-variables/",
      label: "Lesson 2 — Units, Observations & Variables",
      ts: Date.now()
    }));
  })();
</script>