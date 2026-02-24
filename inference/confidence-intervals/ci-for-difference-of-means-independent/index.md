---
layout: default
title: "8. CI for Difference of Means (Independent Samples)"
description: "Construct and interpret a confidence interval for the difference between two independent population means."
permalink: /inference/confidence-intervals/ci-for-difference-of-means-independent/
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
        Version 0 establishes the structure of the two-sample confidence interval.
        Pooled vs unpooled cases and software examples will be expanded later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/ci-for-difference-of-means-independent/",
      label: "Lesson 8 — CI for Difference of Means (Independent)",
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
        <span class="badge">Lesson 8</span>
        <span class="badge">Two Samples</span>
        <span class="badge">Independent</span>
      </div>

      <h1>8. CI for Difference of Means (Independent Samples)</h1>

      <p class="lead">
        We often compare two independent groups.
        This lesson builds the confidence interval for the difference
        between two population means.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: conceptual clarity first.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Construct and interpret a confidence interval for
      μ₁ − μ₂ when samples are independent.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        The difference of two independent sample means
        is itself a random variable with its own standard error.
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
    \hat{\mu}_1 - \hat{\mu}_2
    =
    \bar{X}_1 - \bar{X}_2
    \]
  </div>

  <p class="muted-mini">
    Target parameter: μ₁ − μ₂
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
      \frac{S_1^2}{n_1}
      +
      \frac{S_2^2}{n_2}
    }
    \]
  </div>

  <p class="muted-mini">
    This assumes independence between samples.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Confidence interval formula</h2>
  </div>

  <div class="card">
    <strong>
    \[
    (\bar{X}_1 - \bar{X}_2)
    \pm
    t_{\alpha/2, df}
    \cdot SE
    \]
    </strong>
  </div>

  <p class="muted-mini">
    Degrees of freedom typically use the Welch approximation.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Conditions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Independence between groups</h3>
      <p>Groups must be unrelated.</p>
    </div>

    <div class="card">
      <h3>Independence within groups</h3>
      <p>Random sampling or assignment.</p>
    </div>

    <div class="card">
      <h3>Normality or large samples</h3>
      <p>Each group approximately normal or n sufficiently large.</p>
    </div>

    <div class="card">
      <h3>No extreme outliers</h3>
      <p>Especially important for small samples.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Interpretation</h2>
  </div>

  <div class="card">
    A 95% CI for μ₁ − μ₂ gives a range of plausible values
    for the true difference between population means.
  </div>

  <p class="muted-mini">
    If the interval includes 0, the data are consistent with no difference.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Construct CI for μ₁ − μ₂</li>
        <li>Compute correct standard error</li>
        <li>Interpret inclusion of 0</li>
        <li>Understand independence assumption</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we extend the same logic to proportions.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/ci-for-difference-of-proportions/">
          Next lesson: 9. CI for Difference of Proportions →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/ci-for-proportion/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 7: CI for a Proportion
          </a>
        </div>
      </div>
    </div>

  </div>
</section>