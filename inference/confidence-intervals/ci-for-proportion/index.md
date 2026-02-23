---
layout: default
title: "7. CI for a Proportion: z Interval"
description: "Construct and interpret a confidence interval for a population proportion using the normal approximation."
permalink: /inference/confidence-intervals/ci-for-proportion/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the mathematical structure of the z-based confidence interval
        for a population proportion. Wilson and exact methods will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/ci-for-proportion/",
      label: "Lesson 7 — CI for a Proportion",
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
        <span class="badge">Lesson 7</span>
        <span class="badge">Proportion</span>
        <span class="badge">z Interval</span>
      </div>

      <h1>7. CI for a Proportion: z Interval</h1>

      <p class="lead">
        The z-based confidence interval for a population proportion relies on the
        normal approximation to the sampling distribution of the sample proportion.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: large-sample method first. Refinements later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to construct,
      compute, and interpret a z-based confidence interval for a population proportion.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        When the sample size is large, the sampling distribution of 
        \(\hat p\) is approximately normal.
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
    \hat p = \frac{X}{n}
    \]
  </div>

  <p class="muted-mini">
    p = population proportion (unknown)  
    \(\hat p\) = sample proportion (random variable)
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Sampling distribution</h2>
  </div>

  <div class="card">
    \[
    \hat p \approx N\left(p, \frac{p(1-p)}{n}\right)
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    \[
    SE(\hat p) = \sqrt{\frac{\hat p (1-\hat p)}{n}}
    \]
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Confidence interval formula</h2>
  </div>

  <div class="card">
    <strong>
    \[
    \hat p \pm z_{\alpha/2}
    \sqrt{\frac{\hat p(1-\hat p)}{n}}
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
      <h3>Independence</h3>
      <ul class="bullets">
        <li>Random sampling or random assignment</li>
        <li>No strong clustering or dependence</li>
      </ul>
    </div>

    <div class="card">
      <h3>Large count condition</h3>
      <ul class="bullets">
        <li>\(n\hat p \ge 10\)</li>
        <li>\(n(1-\hat p) \ge 10\)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Interpretation</h2>
  </div>

  <div class="card">
    A 95% confidence interval means that 95% of intervals
    constructed using this method would contain the true proportion.
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common traps</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Small samples</h3>
      <p>Normal approximation fails when counts are small.</p>
    </div>

    <div class="card">
      <h3>Bounds outside [0,1]</h3>
      <p>z intervals may produce impossible values.</p>
    </div>

    <div class="card">
      <h3>Ignoring design</h3>
      <p>Sampling bias invalidates interpretation.</p>
    </div>

    <div class="card">
      <h3>Confusing count and proportion</h3>
      <p>The interval estimates p, not X.</p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Construct a z-based CI for a proportion</li>
        <li>Compute SE correctly</li>
        <li>Verify validity conditions</li>
        <li>Interpret coverage precisely</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we extend interval construction to compare two independent means.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">
          Next lesson: 8. CI for Difference of Means (Independent) →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/conditions-normality-clt-independence/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 6: Conditions for Valid Confidence Intervals
          </a>
        </div>
      </div>
    </div>

  </div>
</section>