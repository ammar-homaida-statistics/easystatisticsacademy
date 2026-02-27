---
layout: default
title: "3. Score Function"
description: "Define the score function as the derivative of the log-likelihood and understand its role in estimation."
permalink: /mathematical-statistics/likelihood-and-log-likelihood/score-function/
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
        Version 0 introduces the score function formally.
        Later versions will include multi-parameter geometry and asymptotic properties.
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
        url: "/mathematical-statistics/likelihood-and-log-likelihood/score-function/",
        label: "Lesson 3 — Score Function",
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
        <span class="badge">Lesson 3</span>
        <span class="badge">Derivative</span>
        <span class="badge">Estimation</span>
      </div>

      <h1>3. Score Function</h1>

      <p class="lead">
        The score function is the derivative of the log-likelihood.
        Its zero defines the maximum likelihood estimator.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/likelihood-and-log-likelihood/">Back to Block 2</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Estimation begins with differentiation.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define the score function formally and understand its role
      in maximum likelihood estimation.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition</h2>
  </div>

  <div class="card">
    The score function is defined as
    \[
    U(\theta)
    =
    \frac{\partial}{\partial \theta}
    \ell(\theta).
    \]
  </div>

  <p style="margin-top:.75rem;">
    It is the derivative of the log-likelihood with respect to the parameter.
  </p>

  <p class="muted-mini">
    In multi-parameter models, the score is a gradient vector.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) First-order condition for MLE</h2>
  </div>

  <div class="card">
    The maximum likelihood estimator \( \hat{\theta} \)
    satisfies
    \[
    U(\hat{\theta}) = 0.
    \]
  </div>

  <p style="margin-top:.75rem;">
    This is the first-order condition for maximization.
  </p>

  <p class="muted-mini">
    Additional conditions (second derivative negative)
    ensure a maximum rather than a minimum.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Example: Bernoulli model</h2>
  </div>

  <div class="card">
    Recall the log-likelihood:
    \[
    \ell(p)
    =
    \left(\sum X_i\right)\log p
    +
    \left(n-\sum X_i\right)\log(1-p).
    \]
  </div>

  <div class="card">
    Differentiating:
    \[
    U(p)
    =
    \frac{\sum X_i}{p}
    -
    \frac{n-\sum X_i}{1-p}.
    \]
  </div>

  <p style="margin-top:.75rem;">
    Setting \( U(p)=0 \) yields
    \[
    \hat{p}
    =
    \frac{1}{n} \sum X_i.
    \]
  </p>

  <p class="muted-mini">
    The MLE equals the sample mean.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Interpretation</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Zero slope</h3>
      <p style="margin:0;">
        At the maximum, the log-likelihood has horizontal tangent.
      </p>
    </div>

    <div class="card">
      <h3>Sensitivity</h3>
      <p style="margin:0;">
        The score measures how sensitive likelihood is to parameter changes.
      </p>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define the score function</li>
        <li>Connect score to MLE</li>
        <li>Compute score in simple models</li>
        <li>Prepare for information and curvature</li>
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
        We now study curvature of the log-likelihood
        through observed and expected information.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/likelihood-and-log-likelihood/observed-vs-expected-information/">
          Continue to Lesson 4 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/likelihood-and-log-likelihood/likelihood-and-log-likelihood/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Likelihood and Log-Likelihood
          </a>
        </div>
      </div>
    </div>

  </div>
</section>