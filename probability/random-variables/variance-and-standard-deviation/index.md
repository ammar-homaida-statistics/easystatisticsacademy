---
layout: default
title: "6. Variance & Standard Deviation"
description: "Variance and standard deviation measure variability around the mean and quantify dispersion of a random variable."
permalink: /probability/random-variables/variance-and-standard-deviation/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 focuses on conceptual clarity and correct mathematical structure.
        Numerical examples, simulations, and visual demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
  (function () {
    var KEY = "esa_continue_probability_random_variables_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/random-variables/variance-and-standard-deviation/",
      label: "Lesson 6 — Variance & Standard Deviation",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Lesson 6</span>
        <span class="badge">Dispersion</span>
        <span class="badge">Variability</span>
      </div>

      <h1>6. Variance &amp; Standard Deviation</h1>

      <p class="lead">
        Expectation measures the center of a distribution. Variance measures its spread.
        Together, they summarize location and variability of a random variable.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/random-variables/">Back to Block 3</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Variance quantifies uncertainty around the mean.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define variance and standard deviation,
      compute them for discrete and continuous random variables, and interpret variability correctly.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Variance measures the average squared deviation from the mean.</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition of variance</h2>
  </div>

  <div class="card">
    <p>
      The variance of a random variable X is:
    </p>
    <p style="margin:0;"><strong>Var(X) = E[(X − μ)²]</strong></p>
    <p class="muted-mini">
      where μ = E[X].
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Alternative formula (computational form)</h3>
    <p style="margin:0;"><strong>Var(X) = E[X²] − (E[X])²</strong></p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Discrete case</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>Var(X) = Σ (x − μ)² p(x)</strong>
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      Using shortcut:
      <strong>Var(X) = Σ x² p(x) − μ²</strong>
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Continuous case</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>Var(X) = ∫ (x − μ)² f(x) dx</strong>
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      Or:
      <strong>Var(X) = ∫ x² f(x) dx − μ²</strong>
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Standard deviation</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>SD(X) = √Var(X)</strong>
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Standard deviation is in the same units as X, making it easier to interpret.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Important properties</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Scaling rule</h3>
      <p style="margin:0;">
        Var(aX + b) = a² Var(X)
      </p>
    </div>

    <div class="card">
      <h3>Sum of independent variables</h3>
      <p style="margin:0;">
        If X and Y are independent:
        Var(X + Y) = Var(X) + Var(Y)
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Interpretation</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Small variance → values tightly clustered around the mean.</li>
      <li>Large variance → values widely spread.</li>
      <li>Variance is always non-negative.</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Confusing variance with standard deviation</li>
        <li>Forgetting to square deviations</li>
        <li>Ignoring independence when adding variances</li>
        <li>Thinking variance measures center instead of spread</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 3</h2>
      <ul class="bullets">
        <li>Understand random variables formally</li>
        <li>Work with PMF, PDF, and CDF</li>
        <li>Compute expectation and variance</li>
        <li>Be ready for Probability Distributions (Block 4)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next block</h2>
      <p style="margin:0;">
        Continue to probability distributions.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/">
          Block 4 — Probability Distributions →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/random-variables/expectation/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 5: Expectation
          </a>
        </div>
      </div>
    </div>
  </div>
</section>