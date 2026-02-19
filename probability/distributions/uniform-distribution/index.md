---
layout: default
title: "7. Uniform Distribution"
description: "The simplest continuous distribution: constant density on an interval."
permalink: /probability/distributions/uniform-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 establishes structure and core formulas.
        Visual intuition, worked examples, and simulations will be added next.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/uniform-distribution/",
      label: "Lesson 7 — Uniform Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 7</span>
        <span class="badge">Continuous</span>
        <span class="badge">Baseline Model</span>
      </div>

      <h1>7. Uniform Distribution</h1>

      <p class="lead">
        The uniform distribution is the simplest continuous model:
        every value in an interval is equally likely.
        It is the continuous analogue of a discrete fair model.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition</h2>
  </div>

  <div class="card">
    <p>
      A random variable X follows a uniform distribution on the interval [a, b] if:
    </p>

    <p style="font-size:1.1rem;">
      $$
      f(x) =
      \begin{cases}
      \frac{1}{b-a}, & a \le x \le b \\
      0, & \text{otherwise}
      \end{cases}
      $$
    </p>
  </div>

  <p class="muted-mini">
    The density is constant across the interval.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Cumulative Distribution Function (CDF)</h2>
  </div>

  <div class="card">
    <p style="font-size:1.1rem;">
      $$
      F(x) =
      \begin{cases}
      0, & x < a \\
      \frac{x-a}{b-a}, & a \le x \le b \\
      1, & x > b
      \end{cases}
      $$
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Mean and Variance</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      $$
      E[X] = \frac{a+b}{2}
      $$
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      $$
      Var(X) = \frac{(b-a)^2}{12}
      $$
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Probability Computation</h2>
  </div>

  <div class="card">
    <p>
      For any subinterval [c, d] within [a, b]:
    </p>

    <p style="font-size:1.1rem;">
      $$
      P(c \le X \le d) = \frac{d-c}{b-a}
      $$
    </p>
  </div>

  <p class="muted-mini">
    Probability equals relative interval length.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand constant density interpretation</li>
        <li>Compute probabilities using interval length</li>
        <li>Apply mean and variance formulas correctly</li>
        <li>Recognize uniform as baseline continuous model</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we study the exponential distribution,
        the fundamental continuous waiting-time model.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/exponential-distribution/">
          Next lesson: 8. Exponential Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/hypergeometric-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 6 — Hypergeometric Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>