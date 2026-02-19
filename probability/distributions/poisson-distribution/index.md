---
layout: default
title: "5. Poisson Distribution"
description: "Counts of events in time or space under a constant rate model. Foundation for rare-event modeling and approximation theory."
permalink: /probability/distributions/poisson-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100;">🚧 Lesson Under Construction</h2>
      <p style="margin:0;">
        Version 0 establishes the mathematical structure.
        Graphs, simulations (R/Python), and real-case examples will be added later.
      </p>
    </div>
  </div>
</section>

<!-- CONTINUE READING TRACKING -->
<script>
(function () {
  var KEY = "esa_continue_probability_distributions_lesson_v0";
  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/poisson-distribution/",
    label: "Lesson 5 — Poisson Distribution",
    ts: Date.now()
  }));
})();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">Discrete</span>
        <span class="badge">Rate model</span>
      </div>

      <h1>5. Poisson Distribution</h1>

      <p class="lead">
        The Poisson distribution models the number of events occurring in a fixed
        time or space interval when events happen independently at a constant rate.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Core idea: modeling counts via intensity (rate) instead of fixed trials.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Definition</h2>
  </div>

  <div class="card">
    <p>
      A random variable \( X \sim \text{Poisson}(\lambda) \) has PMF:
    </p>

    <p style="font-size:1.1rem;">
      \[
      P(X = k) = \frac{e^{-\lambda}\lambda^k}{k!},
      \quad k = 0,1,2,\dots
      \]
    </p>

    <p>
      where \( \lambda > 0 \) is the expected number of events in the interval.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Interpretation of λ</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Rate parameter</h3>
      <ul class="bullets">
        <li>λ = average number of events</li>
        <li>Controls both center and spread</li>
      </ul>
    </div>

    <div class="card">
      <h3>Key property</h3>
      <p>
        \[
        \mathbb{E}[X] = \lambda
        \]
        \[
        \mathrm{Var}(X) = \lambda
        \]
      </p>
      <p class="muted-mini">
        Mean equals variance — a distinctive Poisson signature.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>When to Use Poisson</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Rare events</li>
      <li>Counts over time (calls/hour)</li>
      <li>Counts over area (defects/m²)</li>
      <li>When events occur independently</li>
      <li>Constant average rate</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Connection to Binomial</h2>
  </div>

  <div class="card">
    <p>
      If \( X \sim \text{Binomial}(n,p) \) and:
    </p>

    <p>
      \[
      n \to \infty, \quad p \to 0,
      \quad \text{with } np = \lambda
      \]
    </p>

    <p>
      then:
      \[
      \text{Binomial}(n,p) \approx \text{Poisson}(\lambda)
      \]
    </p>

    <p class="muted-mini">
      Poisson is the rare-event limit of Binomial.
    </p>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common Mistakes</h2>
      <ul class="bullets">
        <li>Using Poisson when rate is not constant</li>
        <li>Using Poisson when events are dependent</li>
        <li>Ignoring mean = variance diagnostic</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand Poisson rate model</li>
        <li>Use PMF formula correctly</li>
        <li>Interpret λ clearly</li>
        <li>Recognize Binomial → Poisson approximation</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we study sampling without replacement,
        which introduces dependence between draws.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/hypergeometric-distribution/">
          Next lesson: 6. Hypergeometric Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/negative-binomial-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Negative Binomial Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>