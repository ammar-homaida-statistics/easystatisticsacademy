---
layout: default
title: "12. Lognormal Distribution"
description: "The Lognormal distribution: modeling positive skewed data, exponential growth, and multiplicative processes derived from the Normal distribution."
permalink: /probability/distributions/lognormal-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 establishes the formal definition and key properties.
        Visual intuition, real-world examples, and software demonstrations will be added next.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/lognormal-distribution/",
      label: "Lesson 12 — Lognormal Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 12</span>
        <span class="badge">Continuous</span>
        <span class="badge">Positive Support</span>
      </div>

      <h1>12. Lognormal Distribution</h1>

      <p class="lead">
        A random variable is lognormally distributed if its logarithm is normally distributed.
        The lognormal distribution models strictly positive and right-skewed data,
        especially in multiplicative growth processes.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        If ln(X) is Normal, then X is Lognormal.
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
      A random variable X follows a Lognormal distribution if:
    </p>

    <p style="font-size:1.1rem;">
      $$
      Y = \ln(X) \sim N(\mu, \sigma^2)
      $$
    </p>

    <p class="muted-mini">
      Notation: X ~ Lognormal(μ, σ²)
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Probability Density Function</h2>
  </div>

  <div class="card">
    <p style="font-size:1.1rem;">
      $$
      f(x) =
      \frac{1}{x \sigma \sqrt{2\pi}}
      \exp\!\left(
        -\frac{(\ln x - \mu)^2}{2\sigma^2}
      \right),
      \quad x > 0
      $$
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Notice: the density is defined only for positive x.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Key Properties</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Support</h3>
      <p style="margin:0;">
        $$
        X > 0
        $$
      </p>
      <p class="muted-mini">
        The distribution is strictly positive.
      </p>
    </div>

    <div class="card">
      <h3>Mean</h3>
      <p style="margin:0;">
        $$
        E[X] = e^{\mu + \sigma^2/2}
        $$
      </p>
    </div>

    <div class="card">
      <h3>Variance</h3>
      <p style="margin:0;">
        $$
        Var(X) =
        \left(e^{\sigma^2} - 1\right)
        e^{2\mu + \sigma^2}
        $$
      </p>
    </div>

    <div class="card">
      <h3>Median</h3>
      <p style="margin:0;">
        $$
        \text{Median} = e^{\mu}
        $$
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Shape & Interpretation</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Right-skewed (long right tail)</li>
      <li>Strictly positive</li>
      <li>Skewness increases as σ increases</li>
      <li>Mean &gt; Median (due to right skew)</li>
    </ul>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Modeling meaning</h2>
      <p style="margin:0;">
        Lognormal distributions arise when growth is multiplicative,
        not additive (e.g., compound returns).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Relationship to Normal Distribution</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>If X is Lognormal → ln(X) is Normal</li>
      <li>If Y is Normal → exp(Y) is Lognormal</li>
      <li>Transformation creates skewness</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This link explains why log-transforming data often stabilizes variance.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define the Lognormal distribution formally</li>
        <li>Understand its relationship to Normal</li>
        <li>Compute mean and variance</li>
        <li>Recognize multiplicative growth modeling</li>
      </ul>
    </div>
  </div>
</section>

<!-- ✅ Next block navigation -->
<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next block</h2>
      <p style="margin:0;">
        Continue to Block 6 — Law of Large Numbers & CLT.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/lln-clt/">
          Block 6 — Law of Large Numbers & CLT →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/normal-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 11 — Normal Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>