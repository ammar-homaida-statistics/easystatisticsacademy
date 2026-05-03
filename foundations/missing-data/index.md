---
layout: default
title: Missing Data
description: Understand why data is missing, different types of missingness, and why naive fixes can lead to incorrect conclusions.
permalink: /foundations/missing-data/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Data quality</span>
      <span class="badge">Real-world issue</span>
      <span class="badge">Analysis risk</span>
    </div>

    <h1>Missing Data</h1>

    <p class="lead">
      Missing data is unavoidable in real datasets — but how you handle it can strongly affect your conclusions.
    </p>

    <div class="hero-actions">
      <a class="btn" href="#content">Start lesson</a>
      <a class="btn btn-outline" href="/foundations/">Back to Foundations</a>
    </div>

  </div>
</section>

<!-- CONTENT -->
<section class="section" id="content">

  <!-- WHAT IS -->
  <div class="section-block">
    <h2>What Is Missing Data?</h2>

    <p>
      Missing data occurs when some values in a dataset are not observed or recorded.
    </p>

    <ul class="bullets">
      <li>Skipped survey questions</li>
      <li>Measurement failures</li>
      <li>Data entry errors</li>
    </ul>

    <p>
      It is a normal part of real-world data.
    </p>
  </div>

  <!-- EXAMPLE -->
  <div class="section-block">
    <h2>Simple Example</h2>

    <p>
      A dataset of incomes:
    </p>

    <ul class="bullets">
      <li>50,000</li>
      <li>62,000</li>
      <li>Missing</li>
      <li>71,000</li>
    </ul>

    <p>
      The missing value affects summary statistics like the mean.
    </p>
  </div>

  <!-- WHY IT MATTERS -->
  <div class="section-block">
    <h2>Why Missing Data Matters</h2>

    <ul class="bullets">
      <li>Reduces available information</li>
      <li>Can distort results</li>
      <li>May introduce bias</li>
    </ul>

    <p>
      Ignoring missing data can lead to incorrect conclusions.
    </p>
  </div>

  <!-- TYPES -->
  <div class="section-block">
    <h2>Types of Missing Data</h2>

    <p><strong>1. Missing Completely at Random (MCAR)</strong></p>
    <ul class="bullets">
      <li>Missingness is unrelated to any variable</li>
      <li>Example: random technical failure</li>
    </ul>

    <p><strong>2. Missing at Random (MAR)</strong></p>
    <ul class="bullets">
      <li>Missingness depends on observed data</li>
      <li>Example: younger people skip income questions more often</li>
    </ul>

    <p><strong>3. Missing Not at Random (MNAR)</strong></p>
    <ul class="bullets">
      <li>Missingness depends on the missing value itself</li>
      <li>Example: high-income individuals choose not to report income</li>
    </ul>
  </div>

  <!-- KEY INSIGHT -->
  <div class="section-block">
    <h2>Key Insight</h2>

    <p>
      Not all missing data is equal.
    </p>

    <p>
      The reason data is missing determines how serious the problem is.
    </p>
  </div>

  <!-- COMMON MISTAKE -->
  <div class="section-block">
    <h2>Common Mistake</h2>

    <p>
      Simply removing all rows with missing values.
    </p>

    <p>
      Problem:
    </p>

    <ul class="bullets">
      <li>Reduces sample size</li>
      <li>May introduce bias</li>
      <li>Changes the structure of the data</li>
    </ul>
  </div>

  <!-- NAIVE FIXES -->
  <div class="section-block">
    <h2>Naive Fixes (Dangerous)</h2>

    <ul class="bullets">
      <li>Replacing missing values with the mean</li>
      <li>Filling with zeros</li>
      <li>Ignoring missingness entirely</li>
    </ul>

    <p>
      These methods often distort relationships in the data.
    </p>
  </div>

  <!-- REAL WORLD -->
  <div class="section-block">
    <h2>Real-World Example</h2>

    <p>
      Income surveys:
    </p>

    <ul class="bullets">
      <li>High-income individuals may not respond</li>
      <li>Average income becomes underestimated</li>
    </ul>

    <p>
      This creates systematic bias.
    </p>
  </div>

  <!-- BIG IDEA -->
  <div class="section-block">
    <h2>The Big Idea</h2>

    <p>
      Missing data is not just a technical issue —
      it is a conceptual problem.
    </p>

    <p>
      Understanding why data is missing is more important than just “fixing” it.
    </p>
  </div>

  <!-- NEXT -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Another common data issue is extreme values.
    </p>

    <ul class="bullets">
      <li>Outliers</li>
      <li>Unusual observations</li>
      <li>Data errors vs real phenomena</li>
    </ul>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/bias/">
          ← Previous: Bias
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/outliers-conceptual-introduction/">
          Next: Outliers →
        </a>

      </div>

    </div>

  </div>
</section>
