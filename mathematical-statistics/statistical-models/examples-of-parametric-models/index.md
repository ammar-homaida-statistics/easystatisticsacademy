---
layout: default
title: "4. Examples of Parametric Models"
description: "Study standard parametric models including Bernoulli, Poisson, Normal, and Exponential families."
permalink: /mathematical-statistics/statistical-models/examples-of-parametric-models/
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
        Version 0 introduces the most common parametric models used in estimation theory.
        Later versions will include geometric interpretation and exponential family structure.
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
        url: "/mathematical-statistics/statistical-models/examples-of-parametric-models/",
        label: "Lesson 4 — Examples of Parametric Models",
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
        <span class="badge">Lesson 4</span>
        <span class="badge">Bernoulli</span>
        <span class="badge">Normal</span>
      </div>

      <h1>4. Examples of Parametric Models</h1>

      <p class="lead">
        A parametric model specifies a family of probability distributions
        indexed by a finite-dimensional parameter.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/statistical-models/">Back to Block 1</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        These models form the foundation of classical estimation theory.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand concrete examples of parametric models
      and how their parameters determine distributional structure.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Bernoulli model</h2>
  </div>

  <div class="card">
    If
    \[
    X_i \sim \text{Bernoulli}(p),
    \quad 0 < p < 1,
    \]
    then the model is
    \[
    \{ \text{Bernoulli}(p) : p \in (0,1) \}.
    \]
  </div>

  <p style="margin-top:.75rem;">
    The parameter \(p\) represents the probability of success.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Poisson model</h2>
  </div>

  <div class="card">
    If
    \[
    X_i \sim \text{Poisson}(\lambda),
    \quad \lambda > 0,
    \]
    then the model is
    \[
    \{ \text{Poisson}(\lambda) : \lambda > 0 \}.
    \]
  </div>

  <p style="margin-top:.75rem;">
    The parameter \( \lambda \) controls both mean and variance.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Normal model</h2>
  </div>

  <div class="card">
    If
    \[
    X_i \sim \mathcal{N}(\mu, \sigma^2),
    \quad \mu \in \mathbb{R}, \ \sigma^2 > 0,
    \]
    then the model is
    \[
    \{ \mathcal{N}(\mu, \sigma^2) : \mu \in \mathbb{R}, \sigma^2 > 0 \}.
    \]
  </div>

  <p style="margin-top:.75rem;">
    The parameter \( \mu \) controls location,
    and \( \sigma^2 \) controls spread.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Exponential model</h2>
  </div>

  <div class="card">
    If
    \[
    X_i \sim \text{Exponential}(\lambda),
    \quad \lambda > 0,
    \]
    then the model is
    \[
    \{ \text{Exponential}(\lambda) : \lambda > 0 \}.
    \]
  </div>

  <p style="margin-top:.75rem;">
    The parameter \( \lambda \) controls the rate of decay.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) What makes these parametric?</h2>
  </div>

  <div class="card">
    These models are parametric because:
    <ul class="bullets">
      <li>The parameter space is finite-dimensional.</li>
      <li>The entire distribution is determined by the parameter.</li>
      <li>Likelihood functions are explicitly computable.</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Recognize standard parametric models</li>
        <li>Understand parameter interpretation</li>
        <li>See how parameters define distribution families</li>
        <li>Prepare for likelihood construction</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine why models determine likelihood
        and why this connection is central to estimation.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/statistical-models/likelihood-preview-why-models-matter/">
          Continue to Lesson 5 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/statistical-models/iid-and-modeling-assumptions/">
            Lesson 3: IID and Modeling Assumptions
          </a>
        </div>
      </div>
    </div>
  </div>
</section> 