---
layout: default
title: "2. Unbiasedness and Bias Correction"
description: "Define unbiased estimators, understand when unbiasedness matters, and learn basic bias correction ideas."
permalink: /mathematical-statistics/estimator-properties/unbiasedness-and-bias-correction/
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
        Version 0 formalizes unbiasedness and introduces bias correction.
        Later versions will include Rao–Blackwell and small-sample corrections.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {

    localStorage.setItem(
      "esa_continue_ms_properties_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/estimator-properties/unbiasedness-and-bias-correction/",
        label: "Lesson 2 — Unbiasedness and Bias Correction",
        ts: Date.now()
      })
    );

    localStorage.setItem(
      "esa_continue_ms_last_block_v0",
      JSON.stringify({
        url: "/mathematical-statistics/estimator-properties/",
        label: "Block 4 — Estimator Properties",
        ts: Date.now()
      })
    );

  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Unbiasedness</span>
        <span class="badge">Correction</span>
      </div>

      <h1>2. Unbiasedness and Bias Correction</h1>

      <p class="lead">
        An estimator is unbiased if its expected value equals the true parameter.
        But unbiasedness alone does not guarantee optimal performance.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/estimator-properties/">Back to Block 4</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Zero bias does not mean zero error.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define unbiased estimators, examine when unbiasedness is meaningful,
      and understand basic bias correction techniques.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition of unbiasedness</h2>
  </div>

  <div class="card">
    An estimator \(\hat{\theta}\) is unbiased if
    \[
    \mathbb{E}[\hat{\theta}] = \theta.
    \]
  </div>

  <p class="muted-mini">
    On average, the estimator equals the true parameter.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Example: Sample mean</h2>
  </div>

  <div class="card">
    For IID data with mean \(\mu\),
    \[
    \bar{X} = \frac{1}{n}\sum_{i=1}^n X_i
    \]
    satisfies
    \[
    \mathbb{E}[\bar{X}] = \mu.
    \]
  </div>

  <p class="muted-mini">
    The sample mean is unbiased for the population mean.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Example: Variance estimator</h2>
  </div>

  <div class="card">
    The MLE variance estimator:
    \[
    \hat{\sigma}^2_{\text{MLE}}
    =
    \frac{1}{n}\sum (X_i-\bar{X})^2
    \]
  </div>

  <div class="card">
    Its expectation:
    \[
    \mathbb{E}[\hat{\sigma}^2_{\text{MLE}}]
    =
    \frac{n-1}{n}\sigma^2.
    \]
  </div>

  <p class="muted-mini">
    It is biased downward.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Bias correction</h2>
  </div>

  <div class="card">
    Multiply by correction factor:
    \[
    \hat{\sigma}^2
    =
    \frac{n}{n-1}
    \hat{\sigma}^2_{\text{MLE}}
    =
    \frac{1}{n-1}\sum (X_i-\bar{X})^2.
    \]
  </div>

  <p class="muted-mini">
    This produces an unbiased estimator of variance.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) When unbiasedness may mislead</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>High variance</h3>
      <p style="margin:0;">
        An unbiased estimator can still fluctuate heavily.
      </p>
    </div>

    <div class="card">
      <h3>Trade-offs</h3>
      <p style="margin:0;">
        A slightly biased estimator may have lower MSE.
      </p>
    </div>

    <div class="card">
      <h3>Shrinkage</h3>
      <p style="margin:0;">
        Biased estimators can outperform unbiased ones.
      </p>
    </div>

    <div class="card">
      <h3>Finite sample vs asymptotic</h3>
      <p style="margin:0;">
        Unbiasedness is a finite-sample property.
      </p>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define unbiased estimator formally</li>
        <li>Understand bias correction</li>
        <li>Recognize limits of unbiasedness</li>
        <li>Prepare for consistency</li>
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
        We now move to large-sample behavior
        and define consistency.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/estimator-properties/consistency-basic-idea/">
          Continue to Lesson 3 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/estimator-properties/bias-variance-and-mse/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: Bias, Variance, and MSE
          </a>
        </div>
      </div>
    </div>

  </div>
</section>