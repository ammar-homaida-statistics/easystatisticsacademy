---
layout: default
title: Discrete vs Continuous Data
description: Understand the difference between discrete and continuous data and why it matters for probability, modeling, and analysis.
permalink: /foundations/discrete-vs-continuous-data/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Foundations</span>
      <span class="badge">Numerical data</span>
      <span class="badge">Very important</span>
    </div>

    <h1>Discrete vs Continuous Data</h1>

    <p class="lead">
      Learn the difference between countable and measurable data —
      a key distinction for probability, distributions, and modeling.
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
      Numerical data comes in two fundamentally different forms:
    </p>

    <ul class="bullets">
      <li><strong>Discrete</strong> → countable values</li>
      <li><strong>Continuous</strong> → measurable values</li>
    </ul>

    <p>
      This distinction determines:
    </p>

    <ul class="bullets">
      <li>which probability models are valid</li>
      <li>how data is visualized</li>
      <li>what statistical methods can be used</li>
    </ul>
  </div>

  <!-- DISCRETE -->
  <div class="section-block">
    <h2>Discrete Data</h2>

    <p>
      Discrete data consists of <strong>separate, countable values</strong>.
    </p>

    <p>
      There are gaps between possible values.
    </p>

    <p><strong>Examples:</strong></p>

    <ul class="bullets">
      <li>Number of students (20, 21, 22)</li>
      <li>Number of errors (0, 1, 2, 3)</li>
      <li>Number of cars in a parking lot</li>
    </ul>

    <p><strong>Key property:</strong></p>

    <ul class="bullets">
      <li>You cannot have fractions between values</li>
    </ul>

    <p>
      Example: 2.5 students ❌
    </p>
  </div>

  <!-- CONTINUOUS -->
  <div class="section-block">
    <h2>Continuous Data</h2>

    <p>
      Continuous data consists of <strong>measurable values</strong>.
    </p>

    <p>
      Values can take any number within a range.
    </p>

    <p><strong>Examples:</strong></p>

    <ul class="bullets">
      <li>Height (170.2 cm, 170.25 cm, 170.251 cm)</li>
      <li>Weight (65.3 kg)</li>
      <li>Time (2.5 seconds)</li>
    </ul>

    <p><strong>Key property:</strong></p>

    <ul class="bullets">
      <li>Infinite possible values between any two points</li>
    </ul>
  </div>

  <!-- VISUAL DIFFERENCE -->
  <div class="section-block">
    <h2>Conceptual Difference</h2>

    <p>
      Think of it this way:
    </p>

    <ul class="bullets">
      <li><strong>Discrete:</strong> points on a number line</li>
      <li><strong>Continuous:</strong> a full line with no gaps</li>
    </ul>

    <p>
      Discrete = counting  
      Continuous = measuring
    </p>
  </div>

  <!-- IMPORTANT INSIGHT -->
  <div class="section-block">
    <h2>Important Insight</h2>

    <p>
      The difference is not about decimals.
    </p>

    <p><strong>Example:</strong></p>

    <ul class="bullets">
      <li>Age = 25 → looks discrete</li>
      <li>But real age = 25.3, 25.31, 25.312 → continuous</li>
    </ul>

    <p>
      Many variables that look discrete are actually continuous,
      but are recorded in rounded form.
    </p>
  </div>

  <!-- TABLE -->
  <div class="section-block">
    <h2>Comparison Table</h2>

    <table style="width:100%; border-collapse:collapse;">
      <thead>
        <tr style="background:#f3f4f6;">
          <th style="padding:10px; border:1px solid #ddd;">Feature</th>
          <th style="padding:10px; border:1px solid #ddd;">Discrete</th>
          <th style="padding:10px; border:1px solid #ddd;">Continuous</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">Nature</td>
          <td style="padding:10px; border:1px solid #ddd;">Countable</td>
          <td style="padding:10px; border:1px solid #ddd;">Measurable</td>
        </tr>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">Values</td>
          <td style="padding:10px; border:1px solid #ddd;">Separate</td>
          <td style="padding:10px; border:1px solid #ddd;">Continuous range</td>
        </tr>
        <tr>
          <td style="padding:10px; border:1px solid #ddd;">Example</td>
          <td style="padding:10px; border:1px solid #ddd;">Number of students</td>
          <td style="padding:10px; border:1px solid #ddd;">Height</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- WHY IT MATTERS -->
  <div class="section-block">
    <h2>Why This Matters</h2>

    <p>
      This distinction affects:
    </p>

    <ul class="bullets">
      <li>Probability models (Binomial vs Normal)</li>
      <li>Graphs (bar chart vs histogram)</li>
      <li>Statistical methods</li>
    </ul>

    <p>
      Using the wrong type leads to incorrect analysis.
    </p>
  </div>

  <!-- NUMERICAL EXAMPLE -->
  <div class="section-block">
    <h2>Example</h2>

    <p><strong>Dataset:</strong></p>

    <ul class="bullets">
      <li>Number of children: 0, 1, 2, 3 → discrete</li>
      <li>Weight: 60.2, 61.8, 59.5 → continuous</li>
    </ul>

    <p>
      These require completely different modeling approaches.
    </p>
  </div>

  <!-- KEY INSIGHT -->
  <div class="section-block">
    <h2>Key Insight</h2>

    <p>
      Always ask:
    </p>

    <ul class="bullets">
      <li>Am I counting or measuring?</li>
    </ul>

    <p>
      That single question determines the correct classification.
    </p>
  </div>

  <!-- NEXT -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Next, we study a very special case of data:
    </p>

    <ul class="bullets">
      <li>Binary data (yes/no, success/failure)</li>
    </ul>

    <p>
      This type is extremely important in statistics and machine learning.
    </p>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/types-of-data/">
          ← Previous: Types of Data
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/binary-data/">
          Next: Binary Data →
        </a>

      </div>

    </div>

  </div>
</section>