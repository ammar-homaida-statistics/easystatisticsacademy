---
layout: default
title: "5. Regularity Conditions (Preview)"
description: "Understand why likelihood theory requires assumptions and what regularity conditions guarantee."
permalink: /mathematical-statistics/likelihood-and-log-likelihood/regularity-conditions-preview/
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
        Version 0 introduces the intuition behind regularity conditions.
        Later versions will include formal theorem statements and counterexamples.
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
        url: "/mathematical-statistics/likelihood-and-log-likelihood/regularity-conditions-preview/",
        label: "Lesson 5 — Regularity Conditions",
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
        <span class="badge">Lesson 5</span>
        <span class="badge">Assumptions</span>
        <span class="badge">Theory</span>
      </div>

      <h1>5. Regularity Conditions (Preview)</h1>

      <p class="lead">
        The powerful results of likelihood theory hold under specific assumptions.
        These assumptions are called regularity conditions.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/likelihood-and-log-likelihood/">Back to Block 2</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Theorems require structure.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand why likelihood results such as unbiased score,
      Fisher information identity, and asymptotic normality
      require technical assumptions.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Why assumptions are needed</h2>
  </div>

  <div class="card">
    In previous lessons, we used results such as:
    \[
    \mathbb{E}[U(\theta)] = 0
    \]
    and
    \[
    I(\theta) = \mathbb{E}[U(\theta)^2].
    \]
  </div>

  <p style="margin-top:.75rem;">
    These identities do not hold automatically.
    They require conditions allowing differentiation under the integral sign.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Typical regularity conditions</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Smoothness</h3>
      <p style="margin:0;">
        The likelihood must be differentiable with respect to the parameter.
      </p>
    </div>

    <div class="card">
      <h3>Parameter interior</h3>
      <p style="margin:0;">
        The true parameter lies inside the parameter space, not on the boundary.
      </p>
    </div>

    <div class="card">
      <h3>Interchange of derivative and expectation</h3>
      <p style="margin:0;">
        Differentiation and integration can be exchanged.
      </p>
    </div>

    <div class="card">
      <h3>Finite information</h3>
      <p style="margin:0;">
        Fisher information must be finite.
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) When regularity fails</h2>
  </div>

  <div class="card">
    Regularity conditions fail in:
    <ul class="bullets">
      <li>Boundary parameter problems</li>
      <li>Mixture models</li>
      <li>Heavy-tailed distributions</li>
      <li>Discrete parameter spaces</li>
    </ul>
  </div>

  <p class="muted-mini">
    In such cases, classical asymptotic results may not hold.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Why this matters</h2>
  </div>

  <div class="card">
    Under regularity conditions, we obtain:
    \[
    \sqrt{n}(\hat{\theta}-\theta)
    \xrightarrow{d}
    N\left(0, I(\theta)^{-1}\right).
    \]
  </div>

  <p style="margin-top:.75rem;">
    This asymptotic normality result underlies confidence intervals
    and hypothesis testing.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand why likelihood theory needs assumptions</li>
        <li>Recognize common regularity conditions</li>
        <li>Identify situations where theory may fail</li>
        <li>Prepare for asymptotic MLE theory</li>
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
        We now formally construct estimators using likelihood.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/maximum-likelihood-estimation/">
          Continue to Block 3 — Maximum Likelihood Estimation →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/likelihood-and-log-likelihood/observed-vs-expected-information/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Observed vs Expected Information
          </a>
        </div>
      </div>
    </div>

  </div>
</section>