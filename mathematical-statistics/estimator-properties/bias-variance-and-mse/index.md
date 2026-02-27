---
layout: default
title: "1. Bias, Variance, and Mean Squared Error"
description: "Define bias, variance, and mean squared error and understand how they decompose estimation error."
permalink: /mathematical-statistics/estimator-properties/bias-variance-and-mse/
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
        Version 0 defines bias, variance, and MSE and derives the bias–variance decomposition.
        Later versions will include geometric interpretation and simulation illustrations.
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
        url: "/mathematical-statistics/estimator-properties/bias-variance-and-mse/",
        label: "Lesson 1 — Bias, Variance, and MSE",
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
        <span class="badge">Lesson 1</span>
        <span class="badge">Bias</span>
        <span class="badge">Variance</span>
      </div>

      <h1>1. Bias, Variance, and Mean Squared Error</h1>

      <p class="lead">
        Estimator quality is measured by how far it deviates from the true parameter —
        systematically and randomly.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/estimator-properties/">Back to Block 4</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Error has two components: bias and variability.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define bias, variance, and mean squared error (MSE),
      and derive the bias–variance decomposition.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Bias</h2>
  </div>

  <div class="card">
    Let \(\hat{\theta}\) be an estimator of \(\theta\).
  </div>

  <div class="card">
    The bias is defined as
    \[
    \text{Bias}(\hat{\theta})
    =
    \mathbb{E}[\hat{\theta}] - \theta.
    \]
  </div>

  <p class="muted-mini">
    Bias measures systematic deviation from the true parameter.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Variance</h2>
  </div>

  <div class="card">
    The variance of the estimator is
    \[
    \text{Var}(\hat{\theta})
    =
    \mathbb{E}\left[(\hat{\theta} - \mathbb{E}[\hat{\theta}])^2\right].
    \]
  </div>

  <p class="muted-mini">
    Variance measures random fluctuation due to sampling variability.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Mean Squared Error (MSE)</h2>
  </div>

  <div class="card">
    The mean squared error is defined as
    \[
    \text{MSE}(\hat{\theta})
    =
    \mathbb{E}\left[(\hat{\theta} - \theta)^2\right].
    \]
  </div>

  <p style="margin-top:.75rem;">
    MSE measures total estimation error.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Bias–Variance Decomposition</h2>
  </div>

  <div class="card">
    Expand:
    \[
    \hat{\theta} - \theta
    =
    (\hat{\theta} - \mathbb{E}[\hat{\theta}])
    +
    (\mathbb{E}[\hat{\theta}] - \theta).
    \]
  </div>

  <div class="card">
    Squaring and taking expectation yields:
    \[
    \text{MSE}(\hat{\theta})
    =
    \text{Var}(\hat{\theta})
    +
    \text{Bias}(\hat{\theta})^2.
    \]
  </div>

  <p class="muted-mini">
    Total error equals variance plus squared bias.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Example: Normal variance estimator</h2>
  </div>

  <div class="card">
    The MLE of variance:
    \[
    \hat{\sigma}^2_{\text{MLE}}
    =
    \frac{1}{n}\sum (X_i-\bar{X})^2.
    \]
  </div>

  <div class="card">
    It is biased:
    \[
    \mathbb{E}[\hat{\sigma}^2_{\text{MLE}}]
    =
    \frac{n-1}{n}\sigma^2.
    \]
  </div>

  <p class="muted-mini">
    Bias correction replaces \(n\) with \(n-1\).
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define bias formally</li>
        <li>Define variance formally</li>
        <li>Define mean squared error</li>
        <li>Derive the bias–variance decomposition</li>
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
        We now examine unbiasedness more closely
        and study bias correction techniques.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/estimator-properties/unbiasedness-and-bias-correction/">
          Continue to Lesson 2 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous block</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/maximum-likelihood-estimation/" style="color:#1a73e8; text-decoration:underline;">
            Block 3: Maximum Likelihood Estimation
          </a>
        </div>
      </div>
    </div>

  </div>
</section>