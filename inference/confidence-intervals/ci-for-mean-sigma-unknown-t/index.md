---
layout: default
title: "5. CI for a Mean (σ Unknown): t Interval"
description: "Construct and interpret a confidence interval for a population mean when the population standard deviation is unknown. Full t-based formulation."
permalink: /inference/confidence-intervals/ci-for-mean-sigma-unknown-t/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the full structure of the t-based confidence interval.
        Worked numerical examples and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Inference Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/",
      label: "Lesson 5 — CI for a Mean (σ Unknown): t Interval",
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
        <span class="badge">Lesson 5</span>
        <span class="badge">Mean</span>
        <span class="badge">t Interval</span>
      </div>

      <h1>5. CI for a Mean (σ Unknown): t Interval</h1>
      <p class="lead">
        In real applications, the population standard deviation is almost never known.
        Therefore, confidence intervals for a mean typically use the
        <strong>t distribution</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        This is the practical default for mean inference.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to derive, compute, and interpret
      the t-based confidence interval for a population mean.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        When σ is unknown and replaced by the sample standard deviation S,
        additional uncertainty appears. The t distribution adjusts for that uncertainty.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Sampling distribution (unknown σ)</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      If the population is normal (or n is large), then:
      \[
      T = \frac{\bar{X} - \mu}{S/\sqrt{n}}
      \sim t_{n-1}
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    The degrees of freedom are:
    \[
    df = n - 1
    \]
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Standard error of the mean</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      SE(\bar{X}) = \frac{S}{\sqrt{n}}
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Notice the difference: S replaces σ.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Deriving the interval</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      P\left(
      -t_{\alpha/2,\,df}
      \le
      \frac{\bar{X}-\mu}{S/\sqrt{n}}
      \le
      t_{\alpha/2,\,df}
      \right)
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
      \bar{X}
      \pm
      t_{\alpha/2,\,n-1}
      \frac{S}{\sqrt{n}}
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
      \bar{X}
      \pm
      t_{\alpha/2,\,n-1}
      \frac{S}{\sqrt{n}}
      \]
      </strong>
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why t intervals are wider</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Because S is random and estimates σ,
      the interval must compensate for additional uncertainty.
      The t critical value is larger than z (for small n).
    </p>
  </div>

  <p style="margin-top:.75rem;">
    As n increases, the t distribution approaches the normal distribution.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Assumptions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Normal population</h3>
      <p>
        Required for small samples.
      </p>
    </div>

    <div class="card">
      <h3>Large sample size</h3>
      <p>
        By the Central Limit Theorem,
        approximate validity even if the population is not perfectly normal.
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
      <h3>Trap A: Using z instead of t</h3>
      <p>
        If σ is unknown, t is required.
      </p>
    </div>

    <div class="card">
      <h3>Trap B: Forgetting degrees of freedom</h3>
      <p>
        df = n − 1.
      </p>
    </div>

    <div class="card">
      <h3>Trap C: Ignoring normality with very small n</h3>
      <p>
        For n < 15, normality matters more.
      </p>
    </div>

    <div class="card">
      <h3>Trap D: Misinterpreting the interval</h3>
      <p>
        The parameter is fixed; the interval varies.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Construct a t-based CI correctly</li>
        <li>Compute standard error using S</li>
        <li>Understand degrees of freedom</li>
        <li>Explain why t is wider than z</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we move to confidence intervals for a population proportion.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/condition-normality-clt-independence/">
          Next lesson: 6. Conditions for Valid Confidence intervals→
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: CI for Mean (σ Known)
          </a>
        </div>
      </div>
    </div>

  </div>
</section>