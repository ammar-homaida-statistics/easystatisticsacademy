---
layout: default
title: "3. Critical Values: z and t"
description: "Understand critical values in confidence intervals: when to use z vs t, how degrees of freedom matter, and why t intervals are wider."
permalink: /inference/confidence-intervals/critical-values-z-and-t/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the conceptual difference between z and t critical values.
        Tables, numeric examples, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Inference Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/critical-values-z-and-t/",
      label: "Lesson 3 — Critical Values: z and t",
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
        <span class="badge">Lesson 3</span>
        <span class="badge">z</span>
        <span class="badge">t</span>
      </div>

      <h1>3. Critical Values: z and t</h1>
      <p class="lead">
        The critical value determines how far we move from the estimate in standard error units.
        Choosing between <strong>z</strong> and <strong>t</strong> depends on what we know about variability.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: conceptual clarity first. Tables and computation next.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to distinguish z and t critical values,
      explain why t intervals are wider, and identify when each distribution applies.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        The critical value reflects how much uncertainty we must account for.
        When the population variance is unknown, extra uncertainty is introduced —
        and that is why we use the t distribution.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The z critical value</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      The z critical value comes from the <strong>standard normal distribution</strong>.
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>When to use z</h3>
      <ul class="bullets">
        <li>Population standard deviation σ is known</li>
        <li>Large-sample approximations (common for proportions)</li>
      </ul>
    </div>

    <div class="card">
      <h3>Common values</h3>
      <ul class="bullets">
        <li>90% → 1.645</li>
        <li>95% → 1.96</li>
        <li>99% → 2.576</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) The t critical value</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      The t critical value comes from the <strong>Student’s t distribution</strong>,
      which depends on degrees of freedom (df).
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>When to use t</h3>
      <ul class="bullets">
        <li>Population standard deviation is unknown</li>
        <li>Using sample standard deviation S</li>
        <li>Typical case for mean inference</li>
      </ul>
    </div>

    <div class="card">
      <h3>Degrees of freedom</h3>
      <p>
        For a one-sample mean:
        df = n − 1
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The t distribution is wider (heavier tails) than the normal distribution,
    especially for small sample sizes.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why t intervals are wider</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      When σ is unknown, we estimate it using S.
      That introduces additional variability.
      The t distribution adjusts for that uncertainty.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    As sample size increases, the t distribution approaches the standard normal distribution.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Summary comparison</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>z Interval</h3>
      <ul class="bullets">
        <li>Uses σ</li>
        <li>Fixed critical values</li>
        <li>Narrower (if σ known)</li>
      </ul>
    </div>

    <div class="card">
      <h3>t Interval</h3>
      <ul class="bullets">
        <li>Uses S</li>
        <li>Depends on df</li>
        <li>Wider (accounts for extra uncertainty)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical rule</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      In real applications for means,
      σ is almost never known.
      Therefore, the t interval is the standard default.
    </p>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Distinguish between z and t critical values</li>
        <li>Understand the role of degrees of freedom</li>
        <li>Explain why t intervals are wider</li>
        <li>Know when each distribution applies</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we construct a full interval step-by-step
        for a population mean.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/">
          Next lesson: 4. CI for a Mean →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: CI Blueprint
          </a>
        </div>
      </div>
    </div>

  </div>
</section>