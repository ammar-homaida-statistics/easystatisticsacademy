---
layout: default
title: "5. Likelihood Preview: Why Models Matter"
description: "Understand how a statistical model determines the likelihood function and why model choice defines estimation."
permalink: /mathematical-statistics/statistical-models/likelihood-preview-why-models-matter/
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
        Version 0 builds intuition for likelihood as a function of the parameter.
        Formal definitions and properties follow in the next block.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {

    localStorage.setItem(
      "esa_continue_ms_statistical_models_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/statistical-models/likelihood-preview-why-models-matter/",
        label: "Lesson 5 — Likelihood Preview: Why Models Matter",
        ts: Date.now()
      })
    );

    localStorage.setItem(
      "esa_continue_ms_last_block_v0",
      JSON.stringify({
        url: "/mathematical-statistics/statistical-models/",
        label: "Block 1 — Statistical Models",
        ts: Date.now()
      })
    );

  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">Likelihood</span>
        <span class="badge">Bridge</span>
      </div>

      <h1>5. Likelihood Preview: Why Models Matter</h1>

      <p class="lead">
        The statistical model determines the likelihood function.
        Without a model, estimation is undefined.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/statistical-models/">Back to Block 1</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Estimation begins once we view probability as a function of the parameter.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand how a statistical model transforms observed data
      into a likelihood function for the unknown parameter.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) From probability to likelihood</h2>
  </div>

  <div class="card">
    Suppose
    \[
    X_1, \dots, X_n \sim f(x \mid \theta).
    \]
  </div>

  <p style="margin-top:.75rem;">
    For fixed \( \theta \), this gives probabilities of data.
  </p>

  <p>
    But once the data are observed, we treat them as fixed
    and view the expression as a function of \( \theta \).
  </p>

  <div class="card">
    \[
    L(\theta)
    =
    \prod_{i=1}^n f(X_i \mid \theta).
    \]
  </div>

  <p class="muted-mini">
    Likelihood is probability viewed as a function of the parameter.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Why the model determines likelihood</h2>
  </div>

  <div class="card">
    Different models imply different likelihood functions,
    even for the same dataset.
  </div>

  <p style="margin-top:.75rem;">
    Example:
  </p>

  <ul class="bullets">
    <li>Assume Bernoulli model → likelihood depends on number of successes.</li>
    <li>Assume Normal model → likelihood depends on mean and variance.</li>
  </ul>

  <p class="muted-mini">
    The likelihood function is entirely defined by the chosen model.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Example: Bernoulli likelihood</h2>
  </div>

  <div class="card">
    If \( X_i \sim \text{Bernoulli}(p) \),
    then
    \[
    L(p)
    =
    p^{\sum X_i}
    (1-p)^{n-\sum X_i}.
    \]
  </div>

  <p style="margin-top:.75rem;">
    The data enter the likelihood through the sufficient statistic
    \( \sum X_i \).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Why this matters for estimation</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>No model</h3>
      <p style="margin:0;">
        No likelihood.
      </p>
    </div>

    <div class="card">
      <h3>No likelihood</h3>
      <p style="margin:0;">
        No principled estimator.
      </p>
    </div>
  </div>

  <p class="muted-mini">
    Estimation theory is built on likelihood.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand likelihood as a function of the parameter</li>
        <li>See how the model defines the likelihood</li>
        <li>Recognize the bridge from modeling to estimation</li>
        <li>Prepare for formal likelihood theory</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next block</h2>
      <p style="margin:0;">
        We now formally develop likelihood and log-likelihood,
        including the score function and information.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/likelihood-and-log-likelihood/">
          Continue to Block 2 — Likelihood →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/statistical-models/examples-of-parametric-models/">
            Lesson 4: Examples of Parametric Models
          </a>
        </div>
      </div>
    </div>
  </div>
</section>