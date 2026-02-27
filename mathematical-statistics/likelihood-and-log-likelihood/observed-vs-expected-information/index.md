---
layout: default
title: "4. Observed vs Expected Information"
description: "Define observed and expected information and understand curvature of the log-likelihood."
permalink: /mathematical-statistics/likelihood-and-log-likelihood/observed-vs-expected-information/
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
        Version 0 introduces curvature and the distinction between observed
        and expected information. Later versions will connect this to asymptotic normality.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {

    localStorage.setItem(
      "esa_continue_ms_likelihood_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/likelihood-and-log-likelihood/observed-vs-expected-information/",
        label: "Lesson 4 — Observed vs Expected Information",
        ts: Date.now()
      })
    );

    localStorage.setItem(
      "esa_continue_ms_last_block_v0",
      JSON.stringify({
        url: "/mathematical-statistics/likelihood-and-log-likelihood/",
        label: "Block 2 — Likelihood & Log-Likelihood",
        ts: Date.now()
      })
    );

  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">Curvature</span>
        <span class="badge">Information</span>
      </div>

      <h1>4. Observed vs Expected Information</h1>

      <p class="lead">
        The curvature of the log-likelihood determines estimator precision.
        Information measures that curvature.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/likelihood-and-log-likelihood/">Back to Block 2</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Curvature quantifies certainty.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define observed and expected information and understand
      how curvature relates to estimator variance.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Second derivative of log-likelihood</h2>
  </div>

  <div class="card">
    The second derivative is
    \[
    \frac{\partial^2}{\partial \theta^2} \ell(\theta).
    \]
  </div>

  <p style="margin-top:.75rem;">
    At a maximum, this quantity is negative.
  </p>

  <div class="card">
    Curvature magnitude is given by
    \[
    -\frac{\partial^2}{\partial \theta^2} \ell(\theta).
    \]
  </div>

  <p class="muted-mini">
    Larger curvature implies sharper peak and higher precision.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Observed information</h2>
  </div>

  <div class="card">
    Observed information is defined as
    \[
    J(\theta)
    =
    -\frac{\partial^2}{\partial \theta^2} \ell(\theta).
    \]
  </div>

  <p style="margin-top:.75rem;">
    It depends on the specific observed sample.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Expected (Fisher) information</h2>
  </div>

  <div class="card">
    Expected information is
    \[
    I(\theta)
    =
    \mathbb{E}\left[
    -\frac{\partial^2}{\partial \theta^2} \ell(\theta)
    \right].
    \]
  </div>

  <div class="card">
    Under regularity conditions,
    \[
    I(\theta)
    =
    \mathbb{E}\left[ U(\theta)^2 \right].
    \]
  </div>

  <p class="muted-mini">
    Fisher information is a property of the model,
    not of a particular dataset.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Interpretation</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Sharp likelihood</h3>
      <p style="margin:0;">
        Large information → narrow peak → precise estimator.
      </p>
    </div>

    <div class="card">
      <h3>Flat likelihood</h3>
      <p style="margin:0;">
        Small information → wide peak → high variance.
      </p>
    </div>

    <div class="card">
      <h3>Observed vs expected</h3>
      <p style="margin:0;">
        Observed varies by sample.
        Expected is theoretical average curvature.
      </p>
    </div>

    <div class="card">
      <h3>Variance link (preview)</h3>
      <p style="margin:0;">
        Later: Var(θ̂) ≈ 1 / I(θ).
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Example: Bernoulli model</h2>
  </div>

  <div class="card">
    From previous lesson,
    \[
    U(p)
    =
    \frac{\sum X_i}{p}
    -
    \frac{n-\sum X_i}{1-p}.
    \]
  </div>

  <div class="card">
    Second derivative:
    \[
    -\frac{\partial^2}{\partial p^2} \ell(p)
    =
    \frac{\sum X_i}{p^2}
    +
    \frac{n-\sum X_i}{(1-p)^2}.
    \]
  </div>

  <div class="card">
    Expected information:
    \[
    I(p)
    =
    \frac{n}{p(1-p)}.
    \]
  </div>

  <p class="muted-mini">
    Information increases with sample size.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define observed information</li>
        <li>Define expected (Fisher) information</li>
        <li>Understand curvature interpretation</li>
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
        Before proving efficiency results,
        we must understand the assumptions behind the theory.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/likelihood-and-log-likelihood/regularity-conditions-preview/">
          Continue to Lesson 5 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/likelihood-and-log-likelihood/score-function/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Score Function
          </a>
        </div>
      </div>
    </div>

  </div>
</section>