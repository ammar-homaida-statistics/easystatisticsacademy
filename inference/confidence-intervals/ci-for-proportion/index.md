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
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; line-height:1.6;">
        Version 0 establishes the mathematical structure of the z-based confidence interval
        for a population proportion. Extensions and refinements (Wilson, exact, bootstrap)
        will be added later.
      </p>
    </div>
  </div>
</section>

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
        When estimating a population proportion, the sampling distribution of the sample
        proportion can be approximated by a normal distribution under large-sample conditions.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Inference home</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Derive, compute, and correctly interpret a confidence interval for a population proportion,
      and verify its validity conditions.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        The sample proportion \(\hat p\) is approximately normal when the sample size is large enough.
        This allows us to construct a z-based confidence interval.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Sample proportion</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      If X = number of successes in n independent trials:
      \[
      \hat p = \frac{X}{n}
      \]
    </p>
  </div>

  <p class="muted-mini">
    p = population proportion (parameter)  
    \(\hat p\) = sample proportion (estimator)
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

  <p>
    Standard error:
  </p>

  <div class="card">
    \[
    SE(\hat p) = \sqrt{\frac{p(1-p)}{n}}
    \]
  </div>

  <p class="muted-mini">
    Since p is unknown, we substitute \(\hat p\).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Estimated standard error</h2>
  </div>

  <div class="card">
    \[
    SE(\hat p) = \sqrt{\frac{\hat p (1-\hat p)}{n}}
    \]
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Confidence interval formula</h2>
  </div>

  <div class="card">
    <strong>
    \[
    \hat p \pm z_{\alpha/2}
    \sqrt{\frac{\hat p (1-\hat p)}{n}}
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
      <h3>Independence</h3>
      <p>Random sampling or random assignment.</p>
    </div>

    <div class="card">
      <h3>Large count condition</h3>
      <p>\(n\hat p ≥ 10\) and \(n(1-\hat p) ≥ 10\)</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Interpretation</h2>
  </div>

  <div class="card">
    A 95% CI means 95% of similarly constructed intervals
    would contain the true population proportion.
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome</h2>
      <ul class="bullets">
        <li>Construct a z-based CI for p</li>
        <li>Compute SE correctly</li>
        <li>Check assumptions</li>
        <li>Interpret coverage properly</li>
      </ul>
    </div>
  </div>
</section>