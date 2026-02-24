---
layout: default
title: "9. CI for Difference of Proportions"
description: "Construct and interpret a confidence interval for the difference between two independent population proportions."
permalink: /inference/confidence-intervals/ci-for-difference-of-proportions/
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
        Version 0 establishes the structure of the two-proportion confidence interval.
        Exact and Wilson-based refinements will be added later.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/ci-for-difference-of-proportions/",
      label: "Lesson 9 — CI for Difference of Proportions",
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
        <span class="badge">Lesson 9</span>
        <span class="badge">Two Proportions</span>
        <span class="badge">z Interval</span>
      </div>

      <h1>9. CI for Difference of Proportions</h1>

      <p class="lead">
        We often compare two independent groups using proportions.
        This lesson constructs a confidence interval for 
        \( p_1 - p_2 \).
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Large-sample normal approximation method.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Construct and interpret a confidence interval for the difference
      between two independent population proportions.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        The difference between two sample proportions is approximately normal
        when sample sizes are sufficiently large.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The estimator</h2>
  </div>

  <div class="card">
    \[
    \hat p_1 - \hat p_2
    \]
  </div>

  <p class="muted-mini">
    Target parameter: \( p_1 - p_2 \)
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Standard error</h2>
  </div>

  <div class="card">
    \[
    SE =
    \sqrt{
      \frac{\hat p_1 (1-\hat p_1)}{n_1}
      +
      \frac{\hat p_2 (1-\hat p_2)}{n_2}
    }
    \]
  </div>

  <p class="muted-mini">
    Assumes independence between the two samples.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Confidence interval formula</h2>
  </div>

  <div class="card">
    <strong>
    \[
    (\hat p_1 - \hat p_2)
    \pm
    z_{\alpha/2}
    \cdot SE
    \]
    </strong>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Conditions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Independence within groups</h3>
      <p>Random sampling or assignment.</p>
    </div>

    <div class="card">
      <h3>Independence between groups</h3>
      <p>Groups must not overlap.</p>
    </div>

    <div class="card">
      <h3>Large counts condition</h3>
      <p>
        \( n_1\hat p_1 ≥ 10 \),  
        \( n_1(1-\hat p_1) ≥ 10 \),  
        \( n_2\hat p_2 ≥ 10 \),  
        \( n_2(1-\hat p_2) ≥ 10 \)
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Interpretation</h2>
  </div>

  <div class="card">
    A 95% CI for \( p_1 - p_2 \) gives plausible values
    for the true difference in population proportions.
  </div>

  <p class="muted-mini">
    If 0 is inside the interval, the data are consistent
    with no difference.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Construct CI for \( p_1 - p_2 \)</li>
        <li>Compute correct standard error</li>
        <li>Check large-count conditions</li>
        <li>Interpret inclusion of 0</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we consider dependent samples
        and construct a confidence interval for paired differences.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/ci-for-paired-mean-difference/">
          Next lesson: 10. CI for Paired Mean Difference →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/ci-for-difference-of-means-independent/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 8: CI for Difference of Means (Independent)
          </a>
        </div>
      </div>
    </div>

  </div>
</section>