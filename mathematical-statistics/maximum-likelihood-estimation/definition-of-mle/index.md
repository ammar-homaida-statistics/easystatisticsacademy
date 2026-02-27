---
layout: default
title: "1. Definition of Maximum Likelihood Estimation"
description: "Define the maximum likelihood estimator formally and interpret it as an optimization problem."
permalink: /mathematical-statistics/maximum-likelihood-estimation/definition-of-mle/
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
        Version 0 defines the maximum likelihood estimator formally and explains its interpretation.
        Later versions will include geometric intuition and numerical demonstrations.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {

    localStorage.setItem(
      "esa_continue_ms_mle_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/maximum-likelihood-estimation/definition-of-mle/",
        label: "Lesson 1 — Definition of MLE",
        ts: Date.now()
      })
    );

    localStorage.setItem(
      "esa_continue_ms_last_block_v0",
      JSON.stringify({
        url: "/mathematical-statistics/maximum-likelihood-estimation/",
        label: "Block 3 — Maximum Likelihood Estimation",
        ts: Date.now()
      })
    );

  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">MLE</span>
        <span class="badge">Optimization</span>
      </div>

      <h1>1. Definition of Maximum Likelihood Estimation</h1>

      <p class="lead">
        The maximum likelihood estimator is the parameter value
        that makes the observed data most likely under the model.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/maximum-likelihood-estimation/">Back to Block 3</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        MLE is an optimization principle.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Formally define the maximum likelihood estimator and understand
      it as an optimization problem over the parameter space.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The likelihood function</h2>
  </div>

  <div class="card">
    Given a sample \(X_1,\dots,X_n\) with density (or pmf)
    \(f(x;\theta)\), the likelihood function is
    \[
    L(\theta)
    =
    \prod_{i=1}^{n} f(X_i;\theta).
    \]
  </div>

  <p style="margin-top:.75rem;">
    Here, the data are fixed and the parameter varies.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Definition of the MLE</h2>
  </div>

  <div class="card">
    The maximum likelihood estimator is defined as
    \[
    \hat{\theta}_{\text{MLE}}
    =
    \arg\max_{\theta \in \Theta} L(\theta).
    \]
  </div>

  <div class="card">
    Equivalently, since the logarithm is monotone,
    \[
    \hat{\theta}_{\text{MLE}}
    =
    \arg\max_{\theta \in \Theta} \ell(\theta),
    \]
    where
    \[
    \ell(\theta) = \log L(\theta).
    \]
  </div>

  <p class="muted-mini">
    We usually maximize the log-likelihood for mathematical convenience.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Interpretation</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Data fixed</h3>
      <p style="margin:0;">
        The observed sample does not change.
      </p>
    </div>

    <div class="card">
      <h3>Parameter varies</h3>
      <p style="margin:0;">
        We search across possible parameter values.
      </p>
    </div>

    <div class="card">
      <h3>Optimization problem</h3>
      <p style="margin:0;">
        MLE solves a maximization problem.
      </p>
    </div>

    <div class="card">
      <h3>Model dependent</h3>
      <p style="margin:0;">
        Different models produce different estimators.
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Example: Bernoulli model</h2>
  </div>

  <div class="card">
    If \(X_i \sim \text{Bernoulli}(p)\), then
    \[
    L(p)
    =
    p^{\sum X_i}(1-p)^{n-\sum X_i}.
    \]
  </div>

  <p style="margin-top:.75rem;">
    Maximizing this likelihood will produce
    \[
    \hat{p} = \frac{1}{n}\sum X_i.
    \]
  </p>

  <p class="muted-mini">
    We will derive this formally in the next lesson.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define the likelihood function</li>
        <li>Define the MLE as an argmax</li>
        <li>Understand log-likelihood equivalence</li>
        <li>Interpret MLE as an optimization principle</li>
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
        We now compute MLEs explicitly by solving likelihood equations.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/maximum-likelihood-estimation/finding-mle-by-optimization/">
          Continue to Lesson 2 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous block</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/likelihood-and-log-likelihood/" style="color:#1a73e8; text-decoration:underline;">
            Block 2 — Likelihood & Log-Likelihood
          </a>
        </div>
      </div>
    </div>

  </div>
</section>