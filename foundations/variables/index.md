---
layout: default
title: Variables
description: Understand what variables are, how they differ from constants, and why they are central to statistical analysis.
permalink: /foundations/variables/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Foundations</span>
      <span class="badge">Variables</span>
      <span class="badge">Core concept</span>
    </div>

    <h1>Variables</h1>

    <p class="lead">
      Learn what variables are, how they represent measurements, and why they are the building blocks of statistical analysis.
    </p>

    <div class="hero-actions">
      <a class="btn" href="#content">Start lesson</a>
      <a class="btn btn-outline" href="/foundations/">Back to Foundations</a>
    </div>

  </div>
</section>

<!-- CONTENT -->
<section class="section" id="content">

  <!-- DEFINITION -->
  <div class="section-block">
    <h2>What Is a Variable?</h2>

    <p>
      A variable is a characteristic or property that can take different values across observational units.
    </p>

    <p>
      In simple terms:
      <strong>a variable is what we measure or record for each unit.</strong>
    </p>
  </div>

  <!-- SIMPLE EXAMPLES -->
  <div class="section-block">
    <h2>Examples of Variables</h2>

    <ul class="bullets">
      <li>Height (in cm)</li>
      <li>Age (in years)</li>
      <li>Gender (Male/Female)</li>
      <li>Exam score</li>
      <li>Income</li>
    </ul>

    <p>
      These values can differ from one observational unit to another.
    </p>
  </div>

  <!-- TABLE -->
  <div class="section-block">
    <h2>Variables in a Dataset</h2>

    <table style="width:100%; border-collapse:collapse; margin-top:10px;">
      <thead>
        <tr style="background:#f3f4f6;">
          <th style="padding:10px; border:1px solid #ddd;">Student</th>
          <th style="padding:10px; border:1px solid #ddd;">Height</th>
          <th style="padding:10px; border:1px solid #ddd;">Score</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">A</td>
          <td style="padding:10px; border:1px solid #ddd;">170</td>
          <td style="padding:10px; border:1px solid #ddd;">75</td>
        </tr>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">B</td>
          <td style="padding:10px; border:1px solid #ddd;">165</td>
          <td style="padding:10px; border:1px solid #ddd;">80</td>
        </tr>
      </tbody>
    </table>

    <p>
      Here:
    </p>

    <ul class="bullets">
      <li>Observational unit = Student</li>
      <li>Variables = Height, Score</li>
    </ul>

    <p>
      Each column (except identifiers) is a variable.
    </p>
  </div>

  <!-- VARIABLE VS CONSTANT -->
  <div class="section-block">
    <h2>Variable vs Constant</h2>

    <p>
      A variable changes across units, while a constant does not.
    </p>

    <p><strong>Example:</strong></p>

    <ul class="bullets">
      <li>Height → variable (different for each person)</li>
      <li>Country (if all students are from the same country) → constant</li>
    </ul>

    <p>
      Only variables provide useful information for statistical analysis.
    </p>
  </div>

  <!-- TYPES INTRO -->
  <div class="section-block">
    <h2>Types of Variables (Preview)</h2>

    <p>
      Variables can be classified into two main types:
    </p>

    <ul class="bullets">
      <li><strong>Numerical variables</strong> → numbers (height, age, income)</li>
      <li><strong>Categorical variables</strong> → labels or groups (gender, color)</li>
    </ul>

    <p>
      This distinction is fundamental and will be studied in detail later.
    </p>
  </div>

  <!-- IMPORTANT INSIGHT -->
  <div class="section-block">
    <h2>Key Insight</h2>

    <p>
      Variables are not “natural objects” — they are choices.
    </p>

    <p>
      The researcher decides:
    </p>

    <ul class="bullets">
      <li>what to measure</li>
      <li>how to measure it</li>
      <li>how to record it</li>
    </ul>

    <p>
      Different choices lead to different analyses.
    </p>
  </div>

  <!-- COMMON MISTAKES -->
  <div class="section-block">
    <h2>Common Mistakes</h2>

    <ul class="bullets">
      <li>Confusing variables with observational units ❌</li>
      <li>Assuming all variables must be numerical ❌</li>
      <li>Ignoring how variables are measured ❌</li>
    </ul>

    <p>
      Example mistake:
    </p>

    <ul class="bullets">
      <li>Treating categories as numbers without meaning (e.g., coding gender as 1 and 2 without interpretation)</li>
    </ul>
  </div>

  <!-- NUMERICAL EXAMPLE -->
  <div class="section-block">
    <h2>Numerical Example</h2>

    <p>
      Suppose we collect data on 4 people:
    </p>

    <table style="width:100%; border-collapse:collapse; margin-top:10px;">
      <thead>
        <tr style="background:#f3f4f6;">
          <th style="padding:10px; border:1px solid #ddd;">Person</th>
          <th style="padding:10px; border:1px solid #ddd;">Age</th>
          <th style="padding:10px; border:1px solid #ddd;">Income</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">A</td>
          <td style="padding:10px; border:1px solid #ddd;">25</td>
          <td style="padding:10px; border:1px solid #ddd;">2000</td>
        </tr>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">B</td>
          <td style="padding:10px; border:1px solid #ddd;">30</td>
          <td style="padding:10px; border:1px solid #ddd;">2500</td>
        </tr>
      </tbody>
    </table>

    <p>
      Variables:
    </p>

    <ul class="bullets">
      <li>Age</li>
      <li>Income</li>
    </ul>
  </div>

  <!-- WHY IMPORTANT -->
  <div class="section-block">
    <h2>Why Variables Matter</h2>

    <p>
      Variables are the core of all statistical analysis.
    </p>

    <p>
      They determine:
    </p>

    <ul class="bullets">
      <li>what relationships we study</li>
      <li>what models we build</li>
      <li>what conclusions we draw</li>
    </ul>

    <p>
      Without variables, there is no analysis.
    </p>
  </div>

  <!-- CONNECTION -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Now we combine:
    </p>

    <ul class="bullets">
      <li>Observational units → rows</li>
      <li>Variables → columns</li>
    </ul>

    <p>
      This leads to the concept of:
      <strong>datasets as structured objects.</strong>
    </p>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/observational-units/">
          ← Previous: Observational Units
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/datasets-as-structures/">
          Next: Datasets as Structures →
        </a>

      </div>

    </div>

  </div>
</section>