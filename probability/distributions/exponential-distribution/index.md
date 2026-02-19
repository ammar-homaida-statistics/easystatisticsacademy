---
layout: default
title: "8. Exponential Distribution"
description: "The fundamental continuous waiting-time model with constant hazard and memoryless property."
permalink: /probability/distributions/exponential-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 establishes structure, formulas, and interpretation.
        Worked examples, intuition visuals, and simulations will be added next.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/exponential-distribution/",
      label: "Lesson 8 — Exponential Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 8</span>
        <span class="badge">Continuous</span>
        <span class="badge">Waiting Time</span>
      </div>

      <h1>8. Exponential Distribution</h1>

      <p class="lead">
        The exponential distribution models waiting time until the first event
        in a process with a constant rate. It is the continuous analogue of
        the geometric distribution.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Key idea: constant hazard rate ⇒ memoryless property.
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
      A random variable X follows an exponential distribution with rate parameter λ > 0 if:
    </p>

    <p style="font-size:1.1rem;">
      $$
      f(x) =
      \begin{cases}
      \lambda e^{-\lambda x}, & x \ge 0 \\
      0, & x < 0
      \end{cases}
      $$
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Cumulative Distribution Function</h2>
  </div>

  <div class="card">
    <p style="font-size:1.1rem;">
      $$
      F(x) = 1 - e^{-\lambda x}, \quad x \ge 0
      $$
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Survival Function</h3>
    <p style="margin:0;">
      $$
      P(X > x) = e^{-\lambda x}
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
      E[X] = \frac{1}{\lambda}
      $$
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      $$
      Var(X) = \frac{1}{\lambda^2}
      $$
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Memoryless Property</h2>
  </div>

  <div class="card">
    <p style="font-size:1.1rem;">
      $$
      P(X > s + t \mid X > s) = P(X > t)
      $$
    </p>
  </div>

  <p class="muted-mini">
    The exponential distribution is the only continuous distribution with this property.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Hazard Rate</h2>
  </div>

  <div class="card">
    <p>
      The hazard rate is:
    </p>

    <p style="font-size:1.1rem;">
      $$
      h(x) = \lambda
      $$
    </p>

    <p class="muted-mini">
      Constant hazard ⇒ no aging effect.
    </p>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand exponential waiting-time interpretation</li>
        <li>Compute probabilities using PDF and CDF</li>
        <li>Apply memoryless property correctly</li>
        <li>Connect exponential to geometric and Poisson processes</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we generalize exponential waiting times using the Gamma distribution.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/gamma-distribution/">
          Next lesson: 9. Gamma Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/uniform-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 7 — Uniform Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>