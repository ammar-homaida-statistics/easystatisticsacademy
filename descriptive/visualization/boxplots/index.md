---
layout: default
title: "Boxplots & Outliers"
description: "Understanding the five-number summary, interquartile range (IQR), and visual detection of outliers."
permalink: /descriptive/visualization/boxplots/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/visualization/density-curves/">
    ← Previous Lesson: Density Curves
  </a>
</section>

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Visual examples and multi-group comparisons will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

<div class="section-head">
  <h1>Boxplots & Outliers</h1>
  <p>
    A boxplot summarizes a distribution using five key statistics and highlights potential outliers.
  </p>
</div>

<hr>

<h2>1. The Five-Number Summary</h2>

A boxplot is built from:

<ul>
  <li>Minimum</li>
  <li>Q1 (First Quartile)</li>
  <li>Median (Q2)</li>
  <li>Q3 (Third Quartile)</li>
  <li>Maximum</li>
</ul>

<p>
These values divide the data into four equal parts.
</p>

<hr>

<h2>2. Interquartile Range (IQR)</h2>

<p>
The IQR measures spread in the middle 50% of the data.
</p>

<p>
IQR = Q3 − Q1
</p>

<p>
It is resistant to extreme values.
</p>

<hr>

<h2>3. Structure of a Boxplot</h2>

<ul>
  <li>The box spans from Q1 to Q3.</li>
  <li>The line inside the box marks the median.</li>
  <li>Whiskers extend toward minimum and maximum (excluding outliers).</li>
</ul>

<p>
The box shows central spread. Whiskers show range.
</p>

<hr>

<h2>4. Detecting Outliers</h2>

<p>
An observation is often considered an outlier if:
</p>

<p>
Value &lt; Q1 − 1.5 × IQR  
or  
Value &gt; Q3 + 1.5 × IQR
</p>

<p>
Outliers appear as separate points beyond the whiskers.
</p>

<hr>

<h2>5. What Boxplots Reveal</h2>

Boxplots allow us to see:

<ul>
  <li>Median location</li>
  <li>Spread (IQR)</li>
  <li>Skewness (asymmetry in box/whiskers)</li>
  <li>Presence of outliers</li>
</ul>

<hr>

<h2>6. Comparing Groups</h2>

<p>
Multiple boxplots side-by-side allow comparison of:
</p>

<ul>
  <li>Center (median differences)</li>
  <li>Spread (IQR differences)</li>
  <li>Outlier patterns</li>
</ul>

<p>
They are powerful for group comparison.
</p>

<hr>

<h2>7. Strengths and Limitations</h2>

<strong>Strengths:</strong>

<ul>
  <li>Compact summary</li>
  <li>Outlier detection</li>
  <li>Good for group comparison</li>
</ul>

<strong>Limitations:</strong>

<ul>
  <li>Do not show detailed shape</li>
  <li>Hide multimodality</li>
  <li>Less intuitive for beginners</li>
</ul>

<hr>

<h2>Summary</h2>

<ul>
  <li>Boxplots summarize distributions using five numbers.</li>
  <li>IQR measures middle spread.</li>
  <li>Outliers are identified using 1.5 × IQR rule.</li>
  <li>Excellent tool for comparing groups.</li>
</ul>

<p>
Boxplots connect visualization to numerical summaries of spread.
</p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/visualization/scatterplots/">
    Next Lesson → Scatterplots
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_visualization_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/visualization/boxplots/",
      label: "Lesson 7 — Boxplots & Outliers",
      ts: Date.now()
    }));
  })();
</script>