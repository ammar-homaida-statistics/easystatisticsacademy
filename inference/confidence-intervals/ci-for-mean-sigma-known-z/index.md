---
layout: default
title: "4. CI for a Mean (σ Known): z Interval"
description: "Construct and interpret a confidence interval for a population mean when the population standard deviation is known. Full z-based formulation."
permalink: /inference/confidence-intervals/ci-for-mean-sigma-known-z/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the full mathematical structure of the z-based confidence interval.
        Worked datasets, simulations, and software examples will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Inference Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/ci-for-mean-sigma-known-z/",
      label: "Lesson 4 — CI for a Mean (σ Known): z Interval",
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
        <span class="badge">Lesson 4</span>
        <span class="badge">Mean</span>
        <span class="badge">z Interval</span>
      </div>

      <h1>4. CI for a Mean (σ Known): z Interval</h1>
      <p class="lead">
        When the population standard deviation σ is known, the sampling distribution
        of the sample mean is normal, and the confidence interval uses the
        <strong>z critical value</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Conceptually important, but rarely used in practice (σ is usually unknown).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to derive, compute, and interpret
      the z-based confidence interval for a population mean when σ is known.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        If σ is known, the standardized sample mean follows the standard normal distribution.
        That is why the z critical value applies.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Sampling distribution of the mean</h2>
    <p>
      If the population mean is μ and population standard deviation is σ:
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      \bar{X} \sim N\left(\mu,\; \frac{\sigma^2}{n}\right)
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    The standard error of the mean is:
  </p>

  <div class="card">
    <p style="margin:0;">
      \[
      SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}
      \]
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Standardization</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}
      \sim N(0,1)
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    This transformation allows us to use the standard normal distribution
    to determine probability coverage.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Deriving the confidence interval</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      For confidence level (1 − α):
      \[
      P\left(-z_{\alpha/2} \le
      \frac{\bar{X} - \mu}{\sigma/\sqrt{n}}
      \le z_{\alpha/2}\right)
      = 1-\alpha
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    Solving for μ gives:
  </p>

  <div class="card">
    <p style="margin:0;">
      \[
      \bar{X} \pm z_{\alpha/2}
      \frac{\sigma}{\sqrt{n}}
      \]
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Final formula</h2>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      <strong>
      Confidence Interval =
      \[
      \bar{X} \pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}
      \]
      </strong>
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Interpretation</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      A 95% z-interval means that if we repeatedly sampled
      and constructed intervals using this formula,
      approximately 95% of them would contain μ.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) When is this realistic?</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Common in theory</h3>
      <p>
        Used for deriving results and understanding interval logic.
      </p>
    </div>

    <div class="card">
      <h3>Rare in practice</h3>
      <p>
        In real applications, σ is almost never known.
        Therefore, t intervals are more common.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>7) Common traps</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Trap A: Using z when σ unknown</h3>
      <p>
        If σ is replaced by S, you must use t instead.
      </p>
    </div>

    <div class="card">
      <h3>Trap B: Forgetting √n</h3>
      <p>
        Standard error shrinks with sample size.
      </p>
    </div>

    <div class="card">
      <h3>Trap C: Confusing σ and S</h3>
      <p>
        σ is population parameter. S is sample statistic.
      </p>
    </div>

    <div class="card">
      <h3>Trap D: Ignoring assumptions</h3>
      <p>
        Requires either normal population or large sample size.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Derive the z-based CI for μ</li>
        <li>Compute SE correctly</li>
        <li>Interpret coverage properly</li>
        <li>Know when the method applies</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we construct the realistic version:
        <strong>CI for a Mean when σ is unknown (t interval)</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">
          Next lesson: 5. CI for a Mean (σ Unknown) →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/critical-values-z-and-t/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Critical Values
          </a>
        </div>
      </div>
    </div>

  </div>
</section>