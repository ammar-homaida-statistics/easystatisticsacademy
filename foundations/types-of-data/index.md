---
layout: default
title: Types of Data
description: Understand categorical vs numerical data and why data type determines analysis, visualization, and interpretation.
permalink: /foundations/types-of-data/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Foundations</span>
      <span class="badge">Core concept</span>
      <span class="badge">Critical decision</span>
    </div>

    <h1>Types of Data</h1>

    <p class="lead">
      Learn how to classify data correctly — because data type determines
      which summaries, graphs, and statistical methods are valid.
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
      Not all data is the same.
    </p>

    <p>
      Every variable belongs to a type, and that type determines:
    </p>

    <ul class="bullets">
      <li>what summaries are valid</li>
      <li>what graphs are appropriate</li>
      <li>what statistical methods you can use</li>
    </ul>

    <p>
      Using the wrong type leads to incorrect conclusions.
    </p>
  </div>

  <!-- MAIN TYPES -->
  <div class="section-block">
    <h2>The Two Main Types of Data</h2>

    <h3>1. Categorical Data</h3>

    <p>
      Data that represents categories or labels.
    </p>

    <ul class="bullets">
      <li>No meaningful numerical operations</li>
      <li>Values represent groups, not quantities</li>
    </ul>

    <p><strong>Examples:</strong></p>

    <ul class="bullets">
      <li>Gender (Male / Female)</li>
      <li>Color (Red / Blue / Green)</li>
      <li>Country (USA / UK / Egypt)</li>
    </ul>

    <hr style="margin:20px 0;">

    <h3>2. Numerical Data</h3>

    <p>
      Data that represents measurable quantities.
    </p>

    <ul class="bullets">
      <li>Arithmetic operations are meaningful (e.g., calculating averages or differences produces meaningful interpretations)</li>
      <li>Values represent measurable quantities</li>
    </ul>

    <p><strong>Examples:</strong></p>

    <ul class="bullets">
      <li>Height (170 cm)</li>
      <li>Income ($2000)</li>
      <li>Age (25 years)</li>
    </ul>

  </div>

  <!-- IMPORTANT WARNING -->
  <div class="section-block">
    <h2>Important Warning</h2>

    <p>
      Numbers do not always mean numerical data.
    </p>

    <p><strong>Example:</strong></p>

    <ul class="bullets">
      <li>1 = Male</li>
      <li>2 = Female</li>
    </ul>

    <p>
      These are still <strong>categorical</strong>, not numerical.
    </p>

    <p>
      You cannot average them or treat them as quantities.
    </p>
  </div>

  <!-- SUBTYPES -->
  <div class="section-block">
    <h2>Subtypes of Data</h2>

    <h3>Categorical Data</h3>

    <ul class="bullets">
      <li><strong>Nominal:</strong> no order (e.g., color)</li>
      <li><strong>Ordinal:</strong> ordered categories (e.g., low/medium/high)</li>
    </ul>

    <h3>Numerical Data</h3>

    <ul class="bullets">
      <li><strong>Discrete:</strong> countable values (e.g., number of students)</li>
      <li><strong>Continuous:</strong> measurable values (e.g., weight, time)</li>
    </ul>

    <p>
      We will study discrete vs continuous in the next lesson.
    </p>
  </div>

  <!-- TABLE EXAMPLE -->
  <div class="section-block">
    <h2>Example Dataset</h2>

    <table style="width:100%; border-collapse:collapse; margin-top:10px;">
      <thead>
        <tr style="background:#f3f4f6;">
          <th style="padding:10px; border:1px solid #ddd;">Variable</th>
          <th style="padding:10px; border:1px solid #ddd;">Type</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">Gender</td>
          <td style="padding:10px; border:1px solid #ddd;">Categorical</td>
        </tr>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">Age</td>
          <td style="padding:10px; border:1px solid #ddd;">Numerical</td>
        </tr>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">Satisfaction Level</td>
          <td style="padding:10px; border:1px solid #ddd;">Ordinal</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- WHY THIS MATTERS -->
  <div class="section-block">
    <h2>Why This Matters</h2>

    <p>
      Data type determines everything:
    </p>

    <ul class="bullets">
      <li>Categorical → bar charts, proportions</li>
      <li>Numerical → histograms, mean, standard deviation</li>
    </ul>

    <p>
      If you confuse them:
    </p>

    <ul class="bullets">
      <li>You will use wrong graphs ❌</li>
      <li>You will compute meaningless summaries ❌</li>
    </ul>
  </div>

  <!-- NUMERICAL EXAMPLE -->
  <div class="section-block">
    <h2>Numerical Example</h2>

    <p>
      Dataset:
    </p>

    <ul class="bullets">
      <li>Gender: Male, Female</li>
      <li>Age: 20, 25, 30</li>
    </ul>

    <p>
      Valid:
    </p>

    <ul class="bullets">
      <li>Average age = (20 + 25 + 30) / 3 = 25</li>
    </ul>

    <p>
      Invalid:
    </p>

    <ul class="bullets">
      <li>Average gender ❌</li>
    </ul>
  </div>

  <!-- KEY INSIGHT -->
  <div class="section-block">
    <h2>Key Insight</h2>

    <p>
      Before analyzing any dataset, always ask:
    </p>

    <ul class="bullets">
      <li>What type of data is this?</li>
    </ul>

    <p>
      This single decision controls your entire analysis.
    </p>
  </div>

  <!-- NEXT -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Now we go deeper into numerical data:
    </p>

    <ul class="bullets">
      <li>Discrete vs continuous data</li>
    </ul>

    <p>
      This distinction is essential for probability and modeling.
    </p>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/datasets-as-structures/">
          ← Previous: Datasets as Structures
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/discrete-vs-continuous-data/">
          Next: Discrete vs Continuous →
        </a>

      </div>

    </div>

  </div>
</section>
