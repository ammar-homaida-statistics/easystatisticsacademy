---
layout: default
title: "6. CI for a Proportion: z Interval"
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
        for a population proportion. Extensions and refinements will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Inference Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/ci-for-proportion/",
      label: "Lesson 6 — CI for a Proportion",
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
        <span class="badge">Lesson 6</span>
        <span class="badge">Proportion</span>
        <span class="badge">z Interval</span>
      </div>

      <h1>6. CI for a Proportion: z Interval</h1>
      <p class="lead">
        When estimating a population proportion, the sampling distribution
        of the sample proportion can be approximated by the normal distribution.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        This is the standard large-sample interval for proportions.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to derive, compute,
      and interpret a confidence interval for a population proportion.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        The sample proportion behaves approximately normally
        when the sample size is large enough.
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
      If X is the number of successes in n trials:
      \[
      \hat{p} = \frac{X}{n}
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    Here:
    - p = population proportion (unknown parameter)  
    - \(\hat{p}\) = sample proportion (estimator)
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Sampling distribution of \(\hat{p}\)</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      For large n:
      \[
      \hat{p} \approx N\left(p, \frac{p(1-p)}{n}\right)
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    The standard error of the sample proportion is:
  </p>

  <div class="card">
    <p style="margin:0;">
      \[
      SE(\hat{p}) = \sqrt{\frac{p(1-p)}{n}}
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Since p is unknown, we substitute \(\hat{p}\).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Estimated standard error</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      SE(\hat{p}) = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
      \]
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Final confidence interval formula</h2>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      <strong>
      Confidence Interval =
      \[
      \hat{p}
      \pm
      z_{\alpha/2}
      \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
      \]
      </strong>
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Conditions for validity</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Independence</h3>
      <p>
        Observations should be independent
        (random sampling or randomized experiment).
      </p>
    </div>

    <div class="card">
      <h3>Large sample condition</h3>
      <p>
        np ≥ 10 and n(1 − p) ≥ 10  
        (often checked using \(\hat{p}\)).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Interpretation</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      A 95% confidence interval for p means that
      95% of similarly constructed intervals
      would contain the true population proportion.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>7) Common traps</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Trap A: Using small samples</h3>
      <p>
        If counts are small, the normal approximation is unreliable.
      </p>
    </div>

    <div class="card">
      <h3>Trap B: Forgetting condition checks</h3>
      <p>
        Always verify np and n(1−p).
      </p>
    </div>

    <div class="card">
      <h3>Trap C: Negative lower bound</h3>
      <p>
        Normal-based intervals can produce values below 0 or above 1.
      </p>
    </div>

    <div class="card">
      <h3>Trap D: Confusing count and proportion</h3>
      <p>
        The interval estimates p, not the number of successes.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Construct a z-based CI for p</li>
        <li>Compute the correct standard error</li>
        <li>Check validity conditions</li>
        <li>Interpret coverage correctly</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next we examine interval width and how to plan sample size.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/interval-width-and-sample-size/">
          Next lesson: 7. Interval Width & Sample Size →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 5: CI for Mean (t)
          </a>
        </div>
      </div>
    </div>

  </div>
</section>