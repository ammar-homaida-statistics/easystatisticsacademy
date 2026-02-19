---
layout: default
title: "6. Hypergeometric Distribution"
description: "Sampling without replacement: modeling dependent draws from a finite population."
permalink: /probability/distributions/hypergeometric-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 establishes structure and mathematical foundations.
        Worked examples, simulations, and applied modeling cases will be added next.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/hypergeometric-distribution/",
      label: "Lesson 6 — Hypergeometric Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 6</span>
        <span class="badge">Discrete</span>
        <span class="badge">Without Replacement</span>
      </div>

      <h1>6. Hypergeometric Distribution</h1>

      <p class="lead">
        The hypergeometric distribution models the number of successes in a fixed-size sample
        drawn <strong>without replacement</strong> from a finite population.
        Unlike the binomial model, the trials are dependent.
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
    <h2>1) When do we use the Hypergeometric model?</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Finite population of size N</li>
      <li>K successes in the population</li>
      <li>Sample size n</li>
      <li>Sampling without replacement</li>
    </ul>
  </div>

  <p class="muted-mini">
    Dependence appears because removing one item changes the probability of the next.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Probability Mass Function (PMF)</h2>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      $$
      P(X = k)
      =
      \frac{\binom{K}{k}\binom{N-K}{\,n-k\,}}
      {\binom{N}{n}}
      $$
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <ul class="bullets">
      <li>N = population size</li>
      <li>K = number of successes in population</li>
      <li>n = sample size</li>
      <li>k = number of observed successes</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Mean and Variance</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      $$
      E[X] = n \frac{K}{N}
      $$
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      $$
      Var(X)
      =
      n \frac{K}{N}\left(1-\frac{K}{N}\right)
      \frac{N-n}{N-1}
      $$
    </p>
  </div>

  <p class="muted-mini">
    The extra factor \( \frac{N-n}{N-1} \) is called the <strong>finite population correction (FPC)</strong>.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Hypergeometric vs Binomial</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Binomial: independent trials</li>
      <li>Hypergeometric: dependent draws</li>
      <li>Binomial approximates hypergeometric when N is large relative to n</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Recognize sampling without replacement</li>
        <li>Apply the hypergeometric PMF correctly</li>
        <li>Understand the finite population correction</li>
        <li>Distinguish binomial vs hypergeometric modeling</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we transition to continuous models beginning with the Uniform distribution.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/uniform-distribution/">
          Next lesson: 7. Uniform Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/poisson-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 5 — Poisson Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>