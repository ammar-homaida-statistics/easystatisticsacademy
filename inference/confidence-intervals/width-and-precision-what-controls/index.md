---
layout: default
title: "11. Width and Precision: What Controls It"
description: "Understand what determines confidence interval width and statistical precision: sample size, variability, and confidence level."
permalink: /inference/confidence-intervals/width-and-precision-what-controls/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 explains the structural determinants of interval width.
        Numeric examples and visual simulations will be added later.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/width-and-precision-what-controls/",
      label: "Lesson 11 — Width and Precision",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/confidence-intervals/",
      label: "Block 2 — Confidence Intervals",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 11</span>
        <span class="badge">Precision</span>
        <span class="badge">Sample Size</span>
      </div>

      <h1>11. Width and Precision: What Controls It</h1>

      <p class="lead">
        Confidence intervals differ in width.
        Understanding what controls width is essential for study design
        and for interpreting statistical precision.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Precision is not random — it is structurally determined.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Identify and explain the three core factors that determine
      confidence interval width.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        Interval width depends on:
        (1) variability,
        (2) sample size,
        (3) confidence level.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) General structure</h2>
  </div>

  <div class="card">
    \[
    \text{CI Width} \propto
    \text{Critical Value}
    \times
    \text{Standard Error}
    \]
  </div>

  <p class="muted-mini">
    Since SE typically equals (variability) / √n,
    the structure becomes clear.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Sample size (n)</h2>
  </div>

  <div class="card">
    \[
    SE \propto \frac{1}{\sqrt{n}}
    \]
  </div>

  <p>
    Increasing sample size reduces width.
    But the reduction follows a square-root law —
    doubling n does not cut width in half.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Variability</h2>
  </div>

  <div class="card">
    Higher variability → larger standard error → wider interval.
  </div>

  <p class="muted-mini">
    Study design can sometimes reduce variability
    (e.g., paired designs).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Confidence level</h2>
  </div>

  <div class="card">
    Higher confidence level → larger critical value → wider interval.
  </div>

  <p>
    99% intervals are wider than 95% intervals,
    which are wider than 90% intervals.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Precision vs accuracy</h2>
  </div>

  <div class="card">
    Narrow intervals reflect precision,
    not necessarily correctness.
  </div>

  <p class="muted-mini">
    Biased sampling can produce narrow but misleading intervals.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Explain how n affects width</li>
        <li>Explain role of variability</li>
        <li>Explain effect of confidence level</li>
        <li>Distinguish precision from validity</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we address the most common interpretation errors
        in confidence intervals.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/common-mistakes-and-interpretation/">
          Next lesson: 12. Common Mistakes & Interpretation →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/ci-for-paired-mean-difference/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 10: CI for Paired Mean Difference
          </a>
        </div>
      </div>
    </div>

  </div>
</section>