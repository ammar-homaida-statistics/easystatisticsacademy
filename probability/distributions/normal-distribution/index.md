---
layout: default
title: "10. Normal Distribution"
description: "The Normal distribution: bell-shaped symmetry, mean and variance, standardization, and why it dominates statistical theory."
permalink: /probability/distributions/normal-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 establishes the formal definition and key properties.
        Graphical intuition, applications, and software demonstrations will be added next.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/normal-distribution/",
      label: "Lesson 10 — Normal Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 10</span>
        <span class="badge">Continuous</span>
        <span class="badge">Bell Curve</span>
      </div>

      <h1>10. Normal Distribution</h1>

      <p class="lead">
        The Normal distribution is the most important continuous distribution in statistics.
        It models natural variation, measurement error, and arises from the Central Limit Theorem.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Symmetric, bell-shaped, and mathematically central to inference.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition</h2>
  </div>

  <div class="card">
    <p>
      A random variable X follows a Normal distribution with mean μ and variance σ² if:
    </p>

    <p style="font-size:1.1rem;">
      $$
      f(x) =
      \frac{1}{\sigma \sqrt{2\pi}}
      \exp\!\left(
        -\frac{(x-\mu)^2}{2\sigma^2}
      \right),
      \quad x \in (-\infty, \infty)
      $$
    </p>

    <p class="muted-mini">
      Notation: X ~ N(μ, σ²)
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Key Properties</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Mean and Variance</h3>
      <p style="margin:0;">
        $$
        E[X] = \mu
        $$
      </p>
      <p style="margin-top:.5rem;">
        $$
        Var(X) = \sigma^2
        $$
      </p>
    </div>

    <div class="card">
      <h3>Shape</h3>
      <ul class="bullets">
        <li>Symmetric around μ</li>
        <li>Bell-shaped curve</li>
        <li>Mean = Median = Mode</li>
        <li>Tails extend infinitely</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Standard Normal Distribution</h2>
  </div>

  <div class="card">
    <p>
      The standard normal distribution has:
    </p>
    <p style="margin:0;">
      $$
      Z \sim N(0,1)
      $$
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Standardization (Z-score)</h3>
    <p style="margin:0;">
      $$
      Z = \frac{X - \mu}{\sigma}
      $$
    </p>
    <p class="muted-mini" style="margin-top:.5rem;">
      Converts any normal variable to standard normal.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) The 68–95–99.7 Rule</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>≈ 68% within μ ± 1σ</li>
      <li>≈ 95% within μ ± 2σ</li>
      <li>≈ 99.7% within μ ± 3σ</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This empirical rule explains why normal distributions appear stable and predictable.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why Normal Is So Important</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Central Limit Theorem</li>
      <li>Measurement errors</li>
      <li>Sampling distributions</li>
      <li>Foundation of confidence intervals and hypothesis testing</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define the Normal distribution formally</li>
        <li>Understand μ and σ² roles</li>
        <li>Standardize using Z-scores</li>
        <li>Recognize why normal dominates inference</li>
      </ul>
    </div>
  </div>
</section>

<!-- ✅ FIXED: Next lesson goes to Lognormal -->
<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we study the Lognormal distribution, which models positive-valued quantities
        created by exponentiating a Normal variable.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/lognormal-distribution/">
          Next lesson: 11. Lognormal Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/gamma-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 9 — Gamma Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>