---
layout: default
title: "10. CI for Paired Mean Difference"
description: "Construct and interpret a confidence interval for the mean difference in paired or matched samples."
permalink: /inference/confidence-intervals/ci-for-paired-mean-difference/
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
        Version 0 establishes the paired-sample framework.
        Extensions and software examples will be added later.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/ci-for-paired-mean-difference/",
      label: "Lesson 10 — CI for Paired Mean Difference",
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
        <span class="badge">Lesson 10</span>
        <span class="badge">Paired</span>
        <span class="badge">Dependent Samples</span>
      </div>

      <h1>10. CI for Paired Mean Difference</h1>

      <p class="lead">
        When observations are naturally paired (before–after, matched units),
        we analyze the differences within pairs — not the groups separately.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        The paired problem is a one-sample problem in disguise.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Construct and interpret a confidence interval for the mean of paired differences.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        Convert paired data into a single variable:
        the difference \( D = X_1 - X_2 \).
        Then perform a one-sample t interval on D.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Define the differences</h2>
  </div>

  <div class="card">
    \[
    D_i = X_{1i} - X_{2i}
    \]
  </div>

  <p class="muted-mini">
    Target parameter: \( \mu_D \)
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Estimator</h2>
  </div>

  <div class="card">
    \[
    \bar{D} = \frac{1}{n}\sum D_i
    \]
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Standard error</h2>
  </div>

  <div class="card">
    \[
    SE =
    \frac{S_D}{\sqrt{n}}
    \]
  </div>

  <p class="muted-mini">
    Where \( S_D \) is the sample standard deviation of the differences.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Confidence interval formula</h2>
  </div>

  <div class="card">
    <strong>
    \[
    \bar{D}
    \pm
    t_{\alpha/2,\,n-1}
    \cdot
    \frac{S_D}{\sqrt{n}}
    \]
    </strong>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Conditions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Paired design</h3>
      <p>Observations are meaningfully linked.</p>
    </div>

    <div class="card">
      <h3>Independence of pairs</h3>
      <p>Pairs independent of each other.</p>
    </div>

    <div class="card">
      <h3>Normality of differences</h3>
      <p>Differences approximately normal or n large.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Interpretation</h2>
  </div>

  <div class="card">
    A 95% CI for \( \mu_D \) gives plausible values
    for the true average paired difference.
  </div>

  <p class="muted-mini">
    If 0 lies in the interval, the data are consistent with no average change.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Transform paired data into differences</li>
        <li>Use one-sample t interval on differences</li>
        <li>Check assumptions properly</li>
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
        Now we analyze what determines interval width and statistical precision.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/width-and-precision-what-controls/">
          Next lesson: 11. Width & Precision: What Controls It →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/ci-for-difference-of-proportions/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 9: CI for Difference of Proportions
          </a>
        </div>
      </div>
    </div>

  </div>
</section>