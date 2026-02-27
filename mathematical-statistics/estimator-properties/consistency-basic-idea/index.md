---
layout: default
title: "3. Consistency (Basic Idea)"
description: "Define consistency and understand why convergence to the true parameter is essential in large samples."
permalink: /mathematical-statistics/estimator-properties/consistency-basic-idea/
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
        Version 0 introduces consistency informally and formally.
        Later versions will include different modes of convergence and asymptotic tools.
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
        url: "/mathematical-statistics/estimator-properties/consistency-basic-idea/",
        label: "Lesson 3 — Consistency (Basic Idea)",
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
        <span class="badge">Lesson 3</span>
        <span class="badge">Consistency</span>
        <span class="badge">Large Sample</span>
      </div>

      <h1>3. Consistency (Basic Idea)</h1>

      <p class="lead">
        An estimator is consistent if it converges to the true parameter
        as sample size increases.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/estimator-properties/">Back to Block 4</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Consistency is about long-run correctness.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define consistency formally and understand its intuitive meaning
      in terms of large-sample behavior.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Informal definition</h2>
  </div>

  <div class="card">
    As sample size \(n\) increases,
    the estimator \(\hat{\theta}_n\) should get closer
    to the true parameter \(\theta\).
  </div>

  <p class="muted-mini">
    With enough data, we expect the estimator to stabilize near truth.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Formal definition (convergence in probability)</h2>
  </div>

  <div class="card">
    An estimator \(\hat{\theta}_n\) is consistent if
    \[
    \hat{\theta}_n \xrightarrow{P} \theta.
    \]
  </div>

  <div class="card">
    That is,
    \[
    \forall \varepsilon > 0,
    \quad
    \Pr\left(|\hat{\theta}_n - \theta| > \varepsilon\right)
    \to 0
    \quad \text{as } n \to \infty.
    \]
  </div>

  <p class="muted-mini">
    The probability of large error vanishes as the sample grows.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Example: Sample mean</h2>
  </div>

  <div class="card">
    By the Law of Large Numbers,
    \[
    \bar{X} \xrightarrow{P} \mu.
    \]
  </div>

  <p class="muted-mini">
    The sample mean is consistent under mild assumptions.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Bias and consistency</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Unbiased but inconsistent</h3>
      <p style="margin:0;">
        Possible if variance does not shrink with \(n\).
      </p>
    </div>

    <div class="card">
      <h3>Biased but consistent</h3>
      <p style="margin:0;">
        Bias may vanish as \(n \to \infty\).
      </p>
    </div>

  </div>

  <p class="muted-mini">
    Consistency is a large-sample property.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Variance and consistency</h2>
  </div>

  <div class="card">
    If
    \[
    \text{Var}(\hat{\theta}_n) \to 0
    \quad \text{and} \quad
    \text{Bias}(\hat{\theta}_n) \to 0,
    \]
    then the estimator is consistent.
  </div>

  <p class="muted-mini">
    Shrinking variability is essential.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define consistency formally</li>
        <li>Understand convergence in probability</li>
        <li>Recognize difference between unbiasedness and consistency</li>
        <li>Prepare for efficiency comparison</li>
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
        We now compare estimators using variance and MSE,
        and introduce the concept of efficiency.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/estimator-properties/efficiency-and-comparing-estimators/">
          Continue to Lesson 4 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/estimator-properties/unbiasedness-and-bias-correction/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Unbiasedness and Bias Correction
          </a>
        </div>
      </div>
    </div>

  </div>
</section>