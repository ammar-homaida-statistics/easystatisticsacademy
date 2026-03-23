---
layout: default
title: "3. Bayesian Point Estimation (Preview)"
description: "Introduce Bayesian estimation using prior, likelihood, and posterior; define MAP and posterior mean."
permalink: /mathematical-statistics/alternative-estimation-methods/bayesian-point-estimation-preview/
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
        Version 0 introduces Bayesian point estimation and contrasts it with frequentist methods.
        Later versions will include conjugate priors and full posterior analysis.
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
        url: "/mathematical-statistics/alternative-estimation-methods/bayesian-point-estimation-preview/",
        label: "Lesson 3 — Bayesian Point Estimation",
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
        <span class="badge">Lesson 3</span>
        <span class="badge">Bayesian</span>
        <span class="badge">Posterior</span>
      </div>

      <h1>3. Bayesian Point Estimation (Preview)</h1>

      <p class="lead">
        Bayesian estimation treats parameters as random variables
        and combines prior information with data through the posterior distribution.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/">Back to Block 7</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        In Bayesian thinking, uncertainty about parameters is modeled explicitly.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand how Bayesian estimation combines prior beliefs and data,
      and define MAP and posterior mean estimators.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Prior, likelihood, posterior</h2>
  </div>

  <div class="card">
    Bayes’ rule:

\[
\text{Posterior} \propto \text{Likelihood} \times \text{Prior}.
\]
  </div>

  <div class="card">
    More explicitly:

\[
p(\theta \mid X)
=
\frac{p(X \mid \theta)p(\theta)}{p(X)}.
\]
  </div>

  <p class="muted-mini">
    The posterior distribution summarizes updated knowledge about the parameter.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Posterior mean estimator</h2>
  </div>

  <div class="card">
    The posterior mean is

\[
\hat{\theta}_{\text{PM}} = \mathbb{E}[\theta \mid X].
\]
  </div>

  <p>
    It minimizes expected squared error under the posterior distribution.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) MAP estimator</h2>
  </div>

  <div class="card">
    The MAP estimator is

\[
\hat{\theta}_{\text{MAP}} = \arg\max_\theta p(\theta \mid X).
\]
  </div>

  <p>
    It selects the most probable parameter value given the data.
  </p>

  <p class="muted-mini">
    MAP resembles MLE but includes the prior.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Comparison with MLE</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>MLE</h3>
      <p style="margin:0;">
        Uses only likelihood.
      </p>
    </div>

    <div class="card">
      <h3>Bayesian</h3>
      <p style="margin:0;">
        Combines prior and likelihood.
      </p>
    </div>

    <div class="card">
      <h3>Interpretation</h3>
      <p style="margin:0;">
        Bayesian treats parameters as random.
      </p>
    </div>

    <div class="card">
      <h3>Flexibility</h3>
      <p style="margin:0;">
        Prior information can improve estimation.
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why this matters</h2>
  </div>

  <div class="card">
    Bayesian estimation is widely used in:

    <ul class="bullets">
      <li>Machine learning</li>
      <li>Hierarchical models</li>
      <li>Small-sample problems</li>
    </ul>
  </div>

  <p class="muted-mini">
    It provides a flexible alternative to classical estimation.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand prior, likelihood, posterior</li>
        <li>Define posterior mean estimator</li>
        <li>Define MAP estimator</li>
        <li>Compare Bayesian and MLE approaches</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now explore shrinkage, where introducing bias
        can reduce overall estimation error.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/alternative-estimation-methods/shrinkage-intuition-preview/">
          Continue to Lesson 4 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/alternative-estimation-methods/estimating-equations-preview/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Estimating Equations
          </a>
        </div>
      </div>
    </div>

  </div>
</section>