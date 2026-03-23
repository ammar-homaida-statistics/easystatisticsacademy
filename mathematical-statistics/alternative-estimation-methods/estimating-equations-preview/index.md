---
layout: default
title: "2. Estimating Equations (Preview)"
description: "Generalize estimation using equations; connect method of moments to modern estimation frameworks."
permalink: /mathematical-statistics/alternative-estimation-methods/estimating-equations-preview/
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
        Version 0 introduces estimating equations as a unifying framework
        for estimation. Later versions will connect this to GMM, M-estimators,
        and robust methods.
      </p>
    </div>
  </div>
</section>

<!-- Continue-reading tracking -->
<script>
  (function () {

    localStorage.setItem(
      "esa_continue_ms_methods_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/alternative-estimation-methods/estimating-equations-preview/",
        label: "Lesson 2 — Estimating Equations",
        ts: Date.now()
      })
    );

    localStorage.setItem(
      "esa_continue_ms_last_block_v0",
      JSON.stringify({
        url: "/mathematical-statistics/alternative-estimation-methods/",
        label: "Block 7 — Alternative Estimation Methods",
        ts: Date.now()
      })
    );

  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Equations</span>
        <span class="badge">Generalization</span>
      </div>

      <h1>2. Estimating Equations (Preview)</h1>

      <p class="lead">
        Many estimators are defined as solutions to equations.
        This perspective unifies method of moments, likelihood,
        and modern estimation techniques.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/">Back to Block 7</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Estimation as solving equations, not just maximizing functions.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand how estimators can be defined as solutions to equations,
      and how this generalizes the method of moments and likelihood methods.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) General idea</h2>
  </div>

  <div class="card">

An estimator \(\hat{\theta}\) can be defined as the solution to

\[
\sum_{i=1}^{n} \psi(X_i, \theta) = 0.
\]

  </div>

  <p style="margin-top:.75rem;">
    The function \(\psi\) defines the estimating equation.
  </p>

</section>

<section class="section">
  <div class="section-head">
    <h2>2) Method of moments as a special case</h2>
  </div>

  <div class="card">

Moment conditions can be written as

\[
\mathbb{E}[g(X, \theta)] = 0.
\]

  </div>

  <div class="card">

Replacing expectation with sample average gives

\[
\frac{1}{n}\sum g(X_i, \theta) = 0.
\]

  </div>

  <p class="muted-mini">
    This is exactly an estimating equation.
  </p>

</section>

<section class="section">
  <div class="section-head">
    <h2>3) Likelihood as estimating equation</h2>
  </div>

  <div class="card">

MLE solves the score equation

\[
\sum_{i=1}^{n} \frac{\partial}{\partial \theta} \log f(X_i|\theta) = 0.
\]

  </div>

  <p>
    This is also an estimating equation.
  </p>

  <p class="muted-mini">
    Likelihood is one specific choice of \(\psi\).
  </p>

</section>

<section class="section">
  <div class="section-head">
    <h2>4) Why this framework matters</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Flexibility</h3>
      <p style="margin:0;">
        We can design equations for specific goals.
      </p>
    </div>

    <div class="card">
      <h3>Robustness</h3>
      <p style="margin:0;">
        Some choices reduce sensitivity to outliers.
      </p>
    </div>

    <div class="card">
      <h3>Generalization</h3>
      <p style="margin:0;">
        Includes GMM, M-estimators, and more.
      </p>
    </div>

    <div class="card">
      <h3>Unification</h3>
      <p style="margin:0;">
        Moments and likelihood are special cases.
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Preview of modern methods</h2>
  </div>

  <div class="card">
    Estimating equations lead to:

    <ul class="bullets">
      <li>Generalized Method of Moments (GMM)</li>
      <li>M-estimators</li>
      <li>Robust statistics</li>
    </ul>
  </div>

  <p class="muted-mini">
    These methods are widely used in econometrics and machine learning.
  </p>

</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define estimating equations</li>
        <li>Connect method of moments and likelihood</li>
        <li>Understand general estimation framework</li>
        <li>Prepare for modern estimation methods</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now explore a different paradigm:
        Bayesian estimation based on posterior distributions.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/alternative-estimation-methods/bayesian-point-estimation-preview/">
          Continue to Lesson 3 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/alternative-estimation-methods/method-of-moments/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: Method of Moments
          </a>
        </div>
      </div>
    </div>

  </div>
</section>