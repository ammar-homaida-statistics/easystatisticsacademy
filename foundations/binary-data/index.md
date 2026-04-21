---
layout: default
title: Binary Data
description: Understand binary data (yes/no, success/failure) and why it is fundamental in statistics, probability, and machine learning.
permalink: /foundations/binary-data/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Foundations</span>
      <span class="badge">Special case</span>
      <span class="badge">Very important</span>
    </div>

    <h1>Binary Data</h1>

    <p class="lead">
      Learn how yes/no data works — one of the most important data types in statistics,
      probability, and machine learning.
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
      Binary data is a special type of data with only two possible outcomes.
    </p>

    <ul class="bullets">
      <li>Yes / No</li>
      <li>Success / Failure</li>
      <li>True / False</li>
      <li>0 / 1</li>
    </ul>

    <p>
      Even though it often uses numbers (0 and 1), it is fundamentally
      <strong>categorical data</strong>.
    </p>
  </div>

  <!-- EXAMPLES -->
  <div class="section-block">
    <h2>Examples of Binary Data</h2>

    <ul class="bullets">
      <li>Passed exam: Yes / No</li>
      <li>Has disease: Yes / No</li>
      <li>Clicked ad: Yes / No</li>
      <li>Customer churn: Stayed / Left</li>
    </ul>

    <p>
      Binary variables appear everywhere in real-world data.
    </p>
  </div>

  <!-- CODING -->
  <div class="section-block">
    <h2>Numerical Coding (0 and 1)</h2>

    <p>
      Binary data is often coded as:
    </p>

    <ul class="bullets">
      <li>1 = Yes / Success</li>
      <li>0 = No / Failure</li>
    </ul>

    <p>
      This allows mathematical operations — but does not change the type.
    </p>

    <p>
      It is still <strong>categorical</strong>, not continuous.
    </p>
  </div>

  <!-- IMPORTANT PROPERTY -->
  <div class="section-block">
    <h2>Important Property</h2>

    <p>
      The mean of binary data has a special interpretation.
    </p>

    <p><strong>Example:</strong></p>

    <p>
      Data: 1, 0, 1, 1, 0
    </p>

    <p>
      Mean = (1 + 0 + 1 + 1 + 0) / 5 = 0.6
    </p>

    <p>
      This means:
    </p>

    <ul class="bullets">
      <li>60% of observations are “success”</li>
    </ul>

    <p>
      So the mean of binary data = <strong>proportion</strong>.
    </p>
  </div>

  <!-- LINK TO PROBABILITY -->
  <div class="section-block">
    <h2>Connection to Probability</h2>

    <p>
      Binary data is the foundation of probability models.
    </p>

    <ul class="bullets">
      <li>Single trial → Bernoulli distribution</li>
      <li>Multiple trials → Binomial distribution</li>
    </ul>

    <p>
      This is why binary data is central to statistics.
    </p>
  </div>

  <!-- LINK TO ML -->
  <div class="section-block">
    <h2>Connection to Machine Learning</h2>

    <p>
      Many machine learning problems are binary:
    </p>

    <ul class="bullets">
      <li>Spam vs Not spam</li>
      <li>Fraud vs Not fraud</li>
      <li>Disease vs Healthy</li>
    </ul>

    <p>
      These are called <strong>binary classification problems</strong>.
    </p>
  </div>

  <!-- COMMON MISTAKE -->
  <div class="section-block">
    <h2>Common Mistake</h2>

    <p>
      Treating binary data as continuous.
    </p>

    <p><strong>Example:</strong></p>

    <ul class="bullets">
      <li>Using methods designed for continuous data ❌</li>
      <li>Ignoring its categorical nature ❌</li>
    </ul>

    <p>
      Always remember:
    </p>

    <ul class="bullets">
      <li>Binary = categorical with two levels</li>
    </ul>
  </div>

  <!-- KEY INSIGHT -->
  <div class="section-block">
    <h2>Key Insight</h2>

    <p>
      Binary data is simple — but extremely powerful.
    </p>

    <ul class="bullets">
      <li>It connects data → probability → inference → machine learning</li>
    </ul>

    <p>
      Many advanced methods are built on this simple idea.
    </p>
  </div>

  <!-- NEXT -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Now we move to a deeper concept:
    </p>

    <ul class="bullets">
      <li>Measurement scales</li>
    </ul>

    <p>
      This will determine what operations and analyses are valid.
    </p>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/discrete-vs-continuous-data/">
          ← Previous: Discrete vs Continuous
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/measurement-scales/">
          Next: Measurement Scales →
        </a>

      </div>

    </div>

  </div>
</section>