---
layout: default
title: "1. Fisher Information (Definition)"
description: "Define Fisher information via expected curvature and score variance, and interpret it as a measure of precision."
permalink: /mathematical-statistics/fisher-information-and-efficiency/fisher-information-definition/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#eef5ff; border:2px solid #3f51b5; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#283593; line-height:1.6;">
        Version 0 defines Fisher information using both curvature
        and score variance. Later versions will include multi-parameter extensions.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {

    localStorage.setItem(
      "esa_continue_ms_information_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/fisher-information-and-efficiency/fisher-information-definition/",
        label: "Lesson 1 — Fisher Information",
        ts: Date.now()
      })
    );

    localStorage.setItem(
      "esa_continue_ms_last_block_v0",
      JSON.stringify({
        url: "/mathematical-statistics/fisher-information-and-efficiency/",
        label: "Block 5 — Fisher Information & Efficiency",
        ts: Date.now()
      })
    );

  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Information</span>
        <span class="badge">Curvature</span>
      </div>

      <h1>1. Fisher Information (Definition)</h1>

      <p class="lead">
        Fisher information measures how sharply the likelihood peaks
        around the true parameter value.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/fisher-information-and-efficiency/">Back to Block 5</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        More curvature means more information.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define Fisher information formally and interpret it
      as a measure of estimator precision.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition via expected curvature</h2>
  </div>

  <div class="card">
    Let the log-likelihood be
    \[
    \ell(\theta).
    \]
  </div>

  <div class="card">
    Fisher information is defined as
    \[
    I(\theta)
    =
    \mathbb{E}\!\left[
      -\frac{\partial^2}{\partial \theta^2} \ell(\theta)
    \right].
    \]
  </div>

  <p class="muted-mini">
    It is the expected curvature of the log-likelihood.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Definition via the score function</h2>
  </div>

  <div class="card">
    The score is
    \[
    U(\theta)
    =
    \frac{\partial}{\partial \theta} \ell(\theta).
    \]
  </div>

  <div class="card">
    Under regularity conditions,
    \[
    I(\theta)
    =
    \mathbb{E}[U(\theta)^2].
    \]
  </div>

  <p class="muted-mini">
    Information equals the variance of the score.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Interpretation</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Sharp likelihood</h3>
      <p style="margin:0;">
        Large \(I(\theta)\) → narrow peak → precise estimator.
      </p>
    </div>

    <div class="card">
      <h3>Flat likelihood</h3>
      <p style="margin:0;">
        Small \(I(\theta)\) → wide peak → high variance.
      </p>
    </div>

    <div class="card">
      <h3>Sample size</h3>
      <p style="margin:0;">
        For IID data, information typically increases with \(n\).
      </p>
    </div>

    <div class="card">
      <h3>Model property</h3>
      <p style="margin:0;">
        Fisher information depends on the model and parameter.
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Example: Bernoulli model</h2>
  </div>

  <div class="card">
    For \(X_i \sim \text{Bernoulli}(p)\),
    \[
    I(p)
    =
    \frac{n}{p(1-p)}.
    \]
  </div>

  <p class="muted-mini">
    Information increases linearly with sample size.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define Fisher information via curvature</li>
        <li>Define it via score variance</li>
        <li>Interpret it geometrically</li>
        <li>Prepare for Cramér–Rao lower bound</li>
      </ul>
    </div>
  </div>
</section>

<!-- ✅ Next + Previous navigation -->
<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now derive the fundamental lower bound
        on the variance of unbiased estimators.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/">
          Continue to Lesson 2 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous block</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/estimator-properties/" style="color:#1a73e8; text-decoration:underline;">
            Block 4: Estimator Properties
          </a>
        </div>
      </div>
    </div>

  </div>
</section>