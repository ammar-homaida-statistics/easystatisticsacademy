---
layout: default
title: Datasets as Structures
description: Understand how datasets are structured using rows and columns, and why structure determines analysis.
permalink: /foundations/datasets-as-structures/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Foundations</span>
      <span class="badge">Data structure</span>
      <span class="badge">Core concept</span>
    </div>

    <h1>Datasets as Structures</h1>

    <p class="lead">
      Learn how datasets are organized into rows and columns — and why this structure
      determines what analysis is possible.
    </p>

    <div class="hero-actions">
      <a class="btn" href="#content">Start lesson</a>
      <a class="btn btn-outline" href="/foundations/">Back to Foundations</a>
    </div>

  </div>
</section>

<!-- CONTENT -->
<section class="section" id="content">

  <!-- CORE IDEA -->
  <div class="section-block">
    <h2>The Core Idea</h2>

    <p>
      A dataset is not just a list of values.
    </p>

    <p>
      It is a structured system that organizes information into:
    </p>

    <ul class="bullets">
      <li><strong>Rows</strong> → observational units</li>
      <li><strong>Columns</strong> → variables</li>
    </ul>

    <p>
      This structure is the foundation of all statistical analysis.
    </p>
  </div>

  <!-- TABLE -->
  <div class="section-block">
    <h2>Example Dataset</h2>

    <table style="width:100%; border-collapse:collapse; margin-top:10px;">
      <thead>
        <tr style="background:#f3f4f6;">
          <th style="padding:10px; border:1px solid #ddd;">Student</th>
          <th style="padding:10px; border:1px solid #ddd;">Age</th>
          <th style="padding:10px; border:1px solid #ddd;">Score</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">A</td>
          <td style="padding:10px; border:1px solid #ddd;">20</td>
          <td style="padding:10px; border:1px solid #ddd;">75</td>
        </tr>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">B</td>
          <td style="padding:10px; border:1px solid #ddd;">22</td>
          <td style="padding:10px; border:1px solid #ddd;">80</td>
        </tr>
      </tbody>
    </table>

    <p>
      Interpretation:
    </p>

    <ul class="bullets">
      <li>Each row = one student (observational unit)</li>
      <li>Each column = one variable (Age, Score)</li>
    </ul>
  </div>

  <!-- STRUCTURE MATTERS -->
  <div class="section-block">
    <h2>Why Structure Matters</h2>

    <p>
      The structure of your dataset determines:
    </p>

    <ul class="bullets">
      <li>what questions you can answer</li>
      <li>what methods you can use</li>
      <li>how results are interpreted</li>
    </ul>

    <p>
      Poor structure leads to incorrect analysis.
    </p>
  </div>

  <!-- DIFFERENT STRUCTURES -->
  <div class="section-block">
    <h2>Different Structures for the Same Data</h2>

    <p>
      The same information can be structured in different ways.
    </p>

    <p><strong>Example:</strong></p>

    <p>
      You can organize data:
    </p>

    <ul class="bullets">
      <li>By student → rows = students</li>
      <li>By class → rows = classes</li>
      <li>By school → rows = schools</li>
    </ul>

    <p>
      Each structure answers different questions.
    </p>

    <p>
      Choosing the wrong structure can hide important patterns or create misleading results.
    </p>
  </div>

  <!-- LONG VS WIDE (IMPORTANT) -->
  <div class="section-block">
    <h2>Wide vs Long Format (Preview)</h2>

    <p>
      Datasets can be structured in different formats.
    </p>

    <p><strong>Wide format:</strong></p>

    <ul class="bullets">
      <li>Multiple columns for related measurements</li>
    </ul>

    <p><strong>Long format:</strong></p>

    <ul class="bullets">
      <li>One column for values, one for category/time</li>
    </ul>

    <p>
      This will become important in:
    </p>

    <ul class="bullets">
      <li>data analysis</li>
      <li>visualization</li>
      <li>machine learning</li>
    </ul>

    <p>
      Long format is typically preferred for analysis and visualization, while wide format is often used for data entry or reporting.
      </p>
  </div>

  <!-- KEY INSIGHT -->
  <div class="section-block">
    <h2>Key Insight</h2>

    <p>
      A dataset is not just data — it is a structured design.
    </p>

    <p>
      You decide:
    </p>

    <ul class="bullets">
      <li>what each row represents</li>
      <li>what each column represents</li>
      <li>how the data is organized</li>
    </ul>

    <p>
      These decisions affect everything that follows.
    </p>
  </div>

  <!-- COMMON MISTAKES -->
  <div class="section-block">
    <h2>Common Mistakes</h2>

    <ul class="bullets">
      <li>Mixing multiple observational units in one table ❌</li>
      <li>Repeating the same information in different formats ❌</li>
      <li>Poorly labeled columns ❌</li>
    </ul>

    <p>
      Example mistake:
    </p>

    <ul class="bullets">
      <li>Having both student-level and class-level data in the same row</li>
    </ul>
  </div>

  <!-- NUMERICAL EXAMPLE -->
  <div class="section-block">
    <h2>Numerical Example</h2>

    <p>
      Suppose we track scores across two exams:
    </p>

    <p><strong>Wide format:</strong></p>

    <table style="width:100%; border-collapse:collapse; margin-top:10px;">
      <thead>
        <tr style="background:#f3f4f6;">
          <th style="padding:10px; border:1px solid #ddd;">Student</th>
          <th style="padding:10px; border:1px solid #ddd;">Exam 1</th>
          <th style="padding:10px; border:1px solid #ddd;">Exam 2</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">A</td>
          <td style="padding:10px; border:1px solid #ddd;">70</td>
          <td style="padding:10px; border:1px solid #ddd;">80</td>
        </tr>
      </tbody>
    </table>

    <p><strong>Long format:</strong></p>

    <table style="width:100%; border-collapse:collapse; margin-top:10px;">
      <thead>
        <tr style="background:#f3f4f6;">
          <th style="padding:10px; border:1px solid #ddd;">Student</th>
          <th style="padding:10px; border:1px solid #ddd;">Exam</th>
          <th style="padding:10px; border:1px solid #ddd;">Score</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">A</td>
          <td style="padding:10px; border:1px solid #ddd;">1</td>
          <td style="padding:10px; border:1px solid #ddd;">70</td>
        </tr>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">A</td>
          <td style="padding:10px; border:1px solid #ddd;">2</td>
          <td style="padding:10px; border:1px solid #ddd;">80</td>
        </tr>
      </tbody>
    </table>

    <p>
      Same data — different structure — different analysis possibilities.
    </p>
  </div>

  <!-- CONNECTION -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Now that we understand dataset structure, the next step is:
    </p>

    <ul class="bullets">
      <li>understanding types of data</li>
      <li>how variables differ in nature</li>
    </ul>

    <p>
      This leads to:
      <strong>types of data.</strong>
    </p>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/variables/">
          ← Previous: Variables
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/types-of-data/">
          Next: Types of Data →
        </a>

      </div>

    </div>

  </div>
</section>
