---
layout: default
title: "4. Existence and Uniqueness of the MLE"
description: "Understand when the maximum likelihood estimator exists, is unique, or may fail."
permalink: /mathematical-statistics/maximum-likelihood-estimation/existence-and-uniqueness/
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
        Version 0 introduces when the MLE exists, when it is unique,
        and situations where it may fail. Later versions will include formal convexity conditions.
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
        url: "/mathematical-statistics/maximum-likelihood-estimation/existence-and-uniqueness/",
        label: "Lesson 4 — Existence and Uniqueness",
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
        <span class="badge">Lesson 4</span>
        <span class="badge">Concavity</span>
        <span class="badge">Pathologies</span>
      </div>

      <h1>4. Existence and Uniqueness of the MLE</h1>

      <p class="lead">
        The maximum likelihood estimator does not always exist —
        and when it exists, it may not be unique.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/maximum-likelihood-estimation/">Back to Block 3</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Optimization requires structure.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand conditions under which the MLE exists,
      when it is unique, and common situations where it fails.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) When does the MLE exist?</h2>
  </div>

  <div class="card">
    The MLE exists if the likelihood function achieves a maximum
    at some parameter value inside the parameter space.
  </div>

  <p style="margin-top:.75rem;">
    Problems arise when:
  </p>

  <div class="card">
    <ul class="bullets">
      <li>The likelihood increases without bound</li>
      <li>The maximum occurs at the boundary</li>
      <li>The parameter space is not closed</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Example: Bernoulli boundary case</h2>
  </div>

  <div class="card">
    If all observations are 1, then
    \[
    L(p) = p^n.
    \]
  </div>

  <div class="card">
    The maximum occurs at
    \[
    p = 1.
    \]
  </div>

  <p class="muted-mini">
    The MLE lies at the boundary of the parameter space.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) When is the MLE unique?</h2>
  </div>

  <div class="card">
    If the log-likelihood is strictly concave,
    then the MLE is unique.
  </div>

  <div class="card">
    Strict concavity implies:
    \[
    \frac{\partial^2}{\partial \theta^2} \ell(\theta) < 0.
    \]
  </div>

  <p class="muted-mini">
    Many exponential family models have strictly concave log-likelihoods.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Non-uniqueness and multiple maxima</h2>
  </div>

  <div class="card">
    In mixture models,
    the likelihood may have several local maxima.
  </div>

  <div class="card">
    Numerical algorithms may converge to different solutions
    depending on starting values.
  </div>

  <p class="muted-mini">
    Global optimization is not guaranteed in non-convex problems.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Non-existence example</h2>
  </div>

  <div class="card">
    In certain heavy-tailed models,
    the likelihood may increase without bound.
  </div>

  <div class="card">
    For example, variance estimation in small samples
    can cause the likelihood to diverge.
  </div>

  <p class="muted-mini">
    Regularity conditions help avoid such cases.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Recognize when the MLE exists</li>
        <li>Understand boundary solutions</li>
        <li>Understand uniqueness via concavity</li>
        <li>Recognize non-regular and multi-peak cases</li>
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
        We now compute MLEs in standard parametric families.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/maximum-likelihood-estimation/mle-examples-bernoulli-poisson-normal/">
          Continue to Lesson 5 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/maximum-likelihood-estimation/invariance-property-of-mle/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Invariance Property of MLE
          </a>
        </div>
      </div>
    </div>

  </div>
</section>