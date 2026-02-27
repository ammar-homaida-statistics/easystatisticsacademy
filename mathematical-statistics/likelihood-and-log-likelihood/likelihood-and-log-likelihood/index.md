---
layout: default
title: "2. Likelihood and Log-Likelihood"
description: "Formal definition of likelihood and log-likelihood, and why the log transformation is central in estimation."
permalink: /mathematical-statistics/likelihood-and-log-likelihood/likelihood-and-log-likelihood/
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
        Version 0 introduces likelihood and log-likelihood formally.
        Later versions will include geometric visualizations and numerical optimization examples.
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
        url: "/mathematical-statistics/likelihood-and-log-likelihood/likelihood-and-log-likelihood/",
        label: "Lesson 2 — Likelihood and Log-Likelihood",
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
        <span class="badge">Lesson 2</span>
        <span class="badge">Likelihood</span>
        <span class="badge">Log Transform</span>
      </div>

      <h1>2. Likelihood and Log-Likelihood</h1>

      <p class="lead">
        The likelihood function is the core object of estimation.
        The log-likelihood is its practical and mathematical working form.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/likelihood-and-log-likelihood/">Back to Block 2</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Maximizing likelihood is equivalent to maximizing log-likelihood.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define the likelihood function formally and understand
      why log-likelihood simplifies estimation and theory.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Likelihood function</h2>
  </div>

  <div class="card">
    Suppose
    \[
    X_1, \dots, X_n \sim f(x \mid \theta)
    \]
    independently.
  </div>

  <div class="card">
    The likelihood function is
    \[
    L(\theta)
    =
    \prod_{i=1}^n f(X_i \mid \theta).
    \]
  </div>

  <p class="muted-mini">
    This is a function of the parameter θ with observed data fixed.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Log-likelihood</h2>
  </div>

  <div class="card">
    The log-likelihood is defined as
    \[
    \ell(\theta)
    =
    \log L(\theta).
    \]
  </div>

  <div class="card">
    Under IID assumptions,
    \[
    \ell(\theta)
    =
    \sum_{i=1}^n \log f(X_i \mid \theta).
    \]
  </div>

  <p class="muted-mini">
    Products become sums — which are easier to differentiate and analyze.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why use log-likelihood?</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Mathematical convenience</h3>
      <p style="margin:0;">
        Sums are easier than products when taking derivatives.
      </p>
    </div>

    <div class="card">
      <h3>Numerical stability</h3>
      <p style="margin:0;">
        Avoids underflow when multiplying many small probabilities.
      </p>
    </div>

    <div class="card">
      <h3>Same maximizer</h3>
      <p style="margin:0;">
        Since log is monotone increasing,
        maximizing \(L(\theta)\) is equivalent to maximizing \(\ell(\theta)\).
      </p>
    </div>

    <div class="card">
      <h3>Curvature interpretation</h3>
      <p style="margin:0;">
        The second derivative relates to estimator precision.
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Example: Bernoulli model</h2>
  </div>

  <div class="card">
    If \( X_i \sim \text{Bernoulli}(p) \),
    then
    \[
    L(p)
    =
    p^{\sum X_i}(1-p)^{n-\sum X_i}.
    \]
  </div>

  <div class="card">
    The log-likelihood is
    \[
    \ell(p)
    =
    \left(\sum X_i\right)\log p
    +
    \left(n-\sum X_i\right)\log(1-p).
    \]
  </div>

  <p class="muted-mini">
    The additive structure makes differentiation straightforward.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define likelihood formally</li>
        <li>Understand log-likelihood structure</li>
        <li>See why log transformation is essential</li>
        <li>Prepare for derivative-based estimation</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now introduce the score function —
        the derivative of the log-likelihood.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/likelihood-and-log-likelihood/score-function/">
          Continue to Lesson 3 →
        </a>
      </div>
    </div>
  </div>
</section>