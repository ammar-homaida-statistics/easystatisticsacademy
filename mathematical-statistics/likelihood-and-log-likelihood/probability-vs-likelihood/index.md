---
layout: default
title: "1. Probability vs Likelihood"
description: "Understand the fundamental distinction between probability and likelihood in statistical modeling."
permalink: /mathematical-statistics/likelihood-and-log-likelihood/probability-vs-likelihood/
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
        Version 0 clarifies the conceptual difference between probability and likelihood.
        Later versions will include geometric visualizations and numerical demonstrations.
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
        url: "/mathematical-statistics/likelihood-and-log-likelihood/probability-vs-likelihood/",
        label: "Lesson 1 — Probability vs Likelihood",
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
        <span class="badge">Lesson 1</span>
        <span class="badge">Conceptual Core</span>
        <span class="badge">Estimation</span>
      </div>

      <h1>1. Probability vs Likelihood</h1>

      <p class="lead">
        Probability treats the parameter as fixed and the data as random.
        Likelihood treats the data as fixed and the parameter as variable.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/likelihood-and-log-likelihood/">Back to Block 2</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        This distinction is the foundation of estimation theory.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Clearly distinguish probability from likelihood and understand
      how reversing the roles of parameter and data creates the likelihood function.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Probability</h2>
  </div>

  <div class="card">
    Suppose
    \[
    X \sim f(x \mid \theta).
    \]
  </div>

  <p style="margin-top:.75rem;">
    In probability:
  </p>

  <ul class="bullets">
    <li>\( \theta \) is fixed (but unknown).</li>
    <li>\( X \) is random.</li>
    <li>We compute probabilities of data given \( \theta \).</li>
  </ul>

  <div class="card">
    \[
    P(X = x \mid \theta).
    \]
  </div>

  <p class="muted-mini">
    Probability answers: “If the parameter were θ, how likely is this data?”
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Likelihood</h2>
  </div>

  <div class="card">
    After observing data \( x \),
    we treat \( x \) as fixed and define
    \[
    L(\theta)
    =
    f(x \mid \theta).
    \]
  </div>

  <ul class="bullets">
    <li>Data are fixed.</li>
    <li>Parameter varies.</li>
    <li>The function is evaluated over \( \theta \).</li>
  </ul>

  <p class="muted-mini">
    Likelihood answers: “Given this data, which θ makes it most plausible?”
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Same formula — different interpretation</h2>
  </div>

  <div class="card">
    The mathematical expression
    \[
    f(x \mid \theta)
    \]
    is the same in both cases.
  </div>

  <p style="margin-top:.75rem;">
    The difference is conceptual:
  </p>

  <ul class="bullets">
    <li>Probability: function of data.</li>
    <li>Likelihood: function of parameter.</li>
  </ul>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Example: Bernoulli model</h2>
  </div>

  <div class="card">
    If \( X_i \sim \text{Bernoulli}(p) \),
    and we observe \( x_1,\dots,x_n \),
    then
    \[
    L(p)
    =
    p^{\sum x_i}
    (1-p)^{n-\sum x_i}.
    \]
  </div>

  <p style="margin-top:.75rem;">
    As a function of \( p \),
    this curve may rise and fall.
  </p>

  <p class="muted-mini">
    The maximum of this curve defines the maximum likelihood estimator.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Distinguish probability from likelihood</li>
        <li>Understand what is fixed and what varies</li>
        <li>Recognize likelihood as a parameter function</li>
        <li>Prepare for log-likelihood and score functions</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now formalize likelihood and introduce log-likelihood
        as the practical working object in estimation.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/likelihood-and-log-likelihood/likelihood-and-log-likelihood/">
          Continue to Lesson 2 →
        </a>
      </div>
    </div>
  </div>
</section>