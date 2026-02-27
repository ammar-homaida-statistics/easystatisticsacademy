---
layout: default
title: "2. Finding the MLE by Optimization"
description: "Compute maximum likelihood estimators using likelihood equations and optimization techniques."
permalink: /mathematical-statistics/maximum-likelihood-estimation/finding-mle-by-optimization/
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
        Version 0 derives MLEs using derivatives and likelihood equations.
        Later versions will include numerical optimization and multidimensional cases.
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
        url: "/mathematical-statistics/maximum-likelihood-estimation/finding-mle-by-optimization/",
        label: "Lesson 2 — Finding MLE by Optimization",
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
        <span class="badge">Lesson 2</span>
        <span class="badge">Optimization</span>
        <span class="badge">Likelihood Equations</span>
      </div>

      <h1>2. Finding the MLE by Optimization</h1>

      <p class="lead">
        To compute the MLE, we differentiate the log-likelihood,
        set the derivative equal to zero, and solve.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/maximum-likelihood-estimation/">Back to Block 3</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        MLE is typically found by solving likelihood equations.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Compute maximum likelihood estimators by differentiating the log-likelihood
      and solving the resulting likelihood equations.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The likelihood equation</h2>
  </div>

  <div class="card">
    Let
    \[
    \ell(\theta) = \log L(\theta).
    \]
  </div>

  <div class="card">
    The MLE satisfies
    \[
    \frac{\partial}{\partial \theta} \ell(\theta) = 0.
    \]
  </div>

  <p class="muted-mini">
    This derivative is called the score function.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Example: Bernoulli model</h2>
  </div>

  <div class="card">
    For \(X_i \sim \text{Bernoulli}(p)\),
    \[
    \ell(p)
    =
    \sum X_i \log p
    +
    (n-\sum X_i)\log(1-p).
    \]
  </div>

  <div class="card">
    Differentiate:
    \[
    \frac{d}{dp} \ell(p)
    =
    \frac{\sum X_i}{p}
    -
    \frac{n-\sum X_i}{1-p}.
    \]
  </div>

  <div class="card">
    Set equal to zero:
    \[
    \frac{\sum X_i}{p}
    =
    \frac{n-\sum X_i}{1-p}.
    \]
  </div>

  <div class="card">
    Solving gives:
    \[
    \hat{p}
    =
    \frac{1}{n}\sum X_i.
    \]
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Example: Normal mean (σ² known)</h2>
  </div>

  <div class="card">
    If \(X_i \sim N(\mu,\sigma^2)\) with known variance,
    \[
    \ell(\mu)
    =
    -\frac{1}{2\sigma^2}\sum (X_i-\mu)^2 + C.
    \]
  </div>

  <div class="card">
    Differentiating:
    \[
    \frac{d}{d\mu}\ell(\mu)
    =
    \frac{1}{\sigma^2}\sum (X_i-\mu).
    \]
  </div>

  <div class="card">
    Setting to zero:
    \[
    \hat{\mu}
    =
    \bar{X}.
    \]
  </div>

  <p class="muted-mini">
    The MLE equals the sample mean.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Multidimensional parameters</h2>
  </div>

  <div class="card">
    If \(\theta = (\theta_1,\dots,\theta_k)\),
    we solve the system
    \[
    \nabla \ell(\theta) = 0.
    \]
  </div>

  <p style="margin-top:.75rem;">
    This produces a system of likelihood equations.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) When closed forms do not exist</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Numerical methods</h3>
      <p style="margin:0;">
        Newton–Raphson and gradient methods.
      </p>
    </div>

    <div class="card">
      <h3>Concavity matters</h3>
      <p style="margin:0;">
        Log-likelihood concavity guarantees uniqueness.
      </p>
    </div>

    <div class="card">
      <h3>Boundary solutions</h3>
      <p style="margin:0;">
        Sometimes maximum occurs at parameter boundary.
      </p>
    </div>

    <div class="card">
      <h3>Multiple maxima</h3>
      <p style="margin:0;">
        Mixture models may produce local maxima.
      </p>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Derive likelihood equations</li>
        <li>Solve for MLE in simple models</li>
        <li>Understand multidimensional optimization</li>
        <li>Recognize need for numerical methods</li>
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
        We now study an important structural property of MLE:
        invariance under transformations.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/maximum-likelihood-estimation/invariance-property-of-mle/">
          Continue to Lesson 3 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/maximum-likelihood-estimation/definition-of-mle/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: Definition of MLE
          </a>
        </div>
      </div>
    </div>

  </div>
</section>