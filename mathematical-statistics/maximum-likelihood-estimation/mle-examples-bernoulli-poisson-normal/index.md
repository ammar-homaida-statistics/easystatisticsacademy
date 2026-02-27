---
layout: default
title: "5. MLE Examples: Bernoulli, Poisson, Normal"
description: "Compute maximum likelihood estimators in standard parametric families and interpret the results."
permalink: /mathematical-statistics/maximum-likelihood-estimation/mle-examples-bernoulli-poisson-normal/
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
        Version 0 derives MLEs in three core parametric families.
        Later versions will include additional models and computational illustrations.
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
        url: "/mathematical-statistics/maximum-likelihood-estimation/mle-examples-bernoulli-poisson-normal/",
        label: "Lesson 5 — MLE Examples",
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
        <span class="badge">Lesson 5</span>
        <span class="badge">Examples</span>
        <span class="badge">Core Models</span>
      </div>

      <h1>5. MLE Examples: Bernoulli, Poisson, Normal</h1>

      <p class="lead">
        We compute maximum likelihood estimators in three foundational models
        and observe recurring structural patterns.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/maximum-likelihood-estimation/">Back to Block 3</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        The sample mean repeatedly appears.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Derive MLEs in common parametric families and recognize
      structural similarities across models.
    </p>
  </div>
</section>

<!-- Bernoulli -->
<section class="section">
  <div class="section-head">
    <h2>1) Bernoulli model</h2>
  </div>

  <div class="card">
    If \(X_i \sim \text{Bernoulli}(p)\),
    \[
    L(p)
    =
    p^{\sum X_i}(1-p)^{n-\sum X_i}.
    \]
  </div>

  <div class="card">
    Log-likelihood:
    \[
    \ell(p)
    =
    \sum X_i \log p
    +
    (n-\sum X_i)\log(1-p).
    \]
  </div>

  <div class="card">
    MLE:
    \[
    \hat{p}
    =
    \bar{X}.
    \]
  </div>

  <p class="muted-mini">
    The MLE equals the sample proportion.
  </p>
</section>

<!-- Poisson -->
<section class="section">
  <div class="section-head">
    <h2>2) Poisson model</h2>
  </div>

  <div class="card">
    If \(X_i \sim \text{Poisson}(\lambda)\),
    \[
    L(\lambda)
    =
    \prod_{i=1}^n
    \frac{e^{-\lambda}\lambda^{X_i}}{X_i!}.
    \]
  </div>

  <div class="card">
    Log-likelihood:
    \[
    \ell(\lambda)
    =
    -n\lambda
    +
    \left(\sum X_i\right)\log \lambda
    + C.
    \]
  </div>

  <div class="card">
    Differentiating and solving:
    \[
    \hat{\lambda}
    =
    \bar{X}.
    \]
  </div>

  <p class="muted-mini">
    Again, the MLE equals the sample mean.
  </p>
</section>

<!-- Normal -->
<section class="section">
  <div class="section-head">
    <h2>3) Normal model</h2>
  </div>

  <div class="card">
    If \(X_i \sim N(\mu,\sigma^2)\),
    \[
    \ell(\mu,\sigma^2)
    =
    -\frac{n}{2}\log\sigma^2
    -
    \frac{1}{2\sigma^2}\sum (X_i-\mu)^2
    + C.
    \]
  </div>

  <div class="card">
    MLE of the mean:
    \[
    \hat{\mu}
    =
    \bar{X}.
    \]
  </div>

  <div class="card">
    MLE of variance:
    \[
    \hat{\sigma}^2
    =
    \frac{1}{n}
    \sum (X_i-\bar{X})^2.
    \]
  </div>

  <p class="muted-mini">
    Note the divisor is \(n\), not \(n-1\).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Structural pattern</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Exponential family</h3>
      <p style="margin:0;">
        Many common models belong to this family.
      </p>
    </div>

    <div class="card">
      <h3>Sample mean</h3>
      <p style="margin:0;">
        Appears naturally in score equations.
      </p>
    </div>

    <div class="card">
      <h3>Optimization principle</h3>
      <p style="margin:0;">
        Derivatives lead to moment-type solutions.
      </p>
    </div>

    <div class="card">
      <h3>Efficiency preview</h3>
      <p style="margin:0;">
        These estimators are often efficient.
      </p>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Compute MLE in Bernoulli model</li>
        <li>Compute MLE in Poisson model</li>
        <li>Compute MLE in Normal model</li>
        <li>Recognize recurring structural patterns</li>
      </ul>
    </div>
  </div>
</section>

<!-- ✅ Next + Previous navigation -->
<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next block</h2>
      <p style="margin:0;">
        We now evaluate estimators using bias,
        variance, consistency, and efficiency.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/estimator-properties/">
          Continue to Block 4 — Estimator Properties →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/maximum-likelihood-estimation/existence-and-uniqueness/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Existence and Uniqueness
          </a>
        </div>
      </div>
    </div>

  </div>
</section>