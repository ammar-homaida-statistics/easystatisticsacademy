---
layout: default
title: "9. Gamma Distribution"
description: "A flexible continuous distribution that generalizes the exponential and models waiting time until multiple events occur."
permalink: /probability/distributions/gamma-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 defines structure, parameters, and core formulas.
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
      url: "/probability/distributions/gamma-distribution/",
      label: "Lesson 9 — Gamma Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 9</span>
        <span class="badge">Continuous</span>
        <span class="badge">Waiting Time</span>
      </div>

      <h1>9. Gamma Distribution</h1>

      <p class="lead">
        The Gamma distribution models the waiting time until the 
        <strong>k-th event</strong> in a Poisson process with rate λ.
        It generalizes the exponential distribution.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Exponential is the special case when k = 1.
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
      A random variable X follows a Gamma distribution with 
      shape parameter k > 0 and rate λ > 0 if:
    </p>

    <p style="font-size:1.1rem;">
      $$
      f(x) =
      \frac{\lambda^k}{\Gamma(k)} x^{k-1} e^{-\lambda x},
      \quad x \ge 0
      $$
    </p>

    <p class="muted-mini">
      Γ(k) is the Gamma function, a continuous extension of factorial.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Mean and Variance</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      $$
      E[X] = \frac{k}{\lambda}
      $$
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      $$
      Var(X) = \frac{k}{\lambda^2}
      $$
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Special Cases</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Exponential</h3>
      <p style="margin:0;">
        When k = 1:
        $$
        f(x) = \lambda e^{-\lambda x}
        $$
      </p>
    </div>

    <div class="card">
      <h3>Erlang Distribution</h3>
      <p>
        When k is a positive integer,
        the Gamma is sometimes called the Erlang distribution.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Interpretation</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Models time until k arrivals in a Poisson process</li>
      <li>Flexible shape: skewed for small k, more symmetric for large k</li>
      <li>Used in reliability and queuing theory</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand Gamma as multi-event waiting time model</li>
        <li>Compute mean and variance</li>
        <li>Recognize exponential as special case</li>
        <li>Prepare for Normal distribution next</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we study the most important distribution in statistics:
        the Normal distribution.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/normal-distribution/">
          Next lesson: 10. Normal Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/exponential-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 8 — Exponential Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>