---
layout: default
title: "5. Information and MLE Connection (Preview)"
description: "Preview how Fisher information determines the asymptotic variance of the maximum likelihood estimator."
permalink: /mathematical-statistics/fisher-information-and-efficiency/information-and-mle-connection-preview/
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
        Version 0 previews the asymptotic link between Fisher information
        and the variance of the maximum likelihood estimator.
        Full proofs are developed in Block 6.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {

    localStorage.setItem(
      "esa_continue_ms_information_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/fisher-information-and-efficiency/information-and-mle-connection-preview/",
        label: "Lesson 5 — Information and MLE Connection",
        ts: Date.now()
      })
    );

    localStorage.setItem(
      "esa_continue_ms_last_block_v0",
      JSON.stringify({
        url: "/mathematical-statistics/fisher-information-and-efficiency/",
        label: "Block 5 — Fisher Information & Efficiency",
        ts: Date.now()
      })
    );

  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">MLE</span>
        <span class="badge">Asymptotics</span>
      </div>

      <h1>5. Information and MLE Connection (Preview)</h1>

      <p class="lead">
        Under regularity conditions, the maximum likelihood estimator
        is approximately normal with variance determined by Fisher information.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/fisher-information-and-efficiency/">Back to Block 5</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Information determines asymptotic precision.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand how Fisher information governs the large-sample
      distribution and variance of the maximum likelihood estimator.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Key asymptotic result (informal statement)</h2>
  </div>

  <div class="card">
    Under regularity conditions and IID sampling,
    \[
    \sqrt{n}(\hat{\theta}_{MLE}-\theta)
    \xrightarrow{d}
    \mathcal{N}\left(0,\frac{1}{I_1(\theta)}\right).
    \]
  </div>

  <div class="card">
    Equivalently,
    \[
    \hat{\theta}_{MLE}
    \approx
    \mathcal{N}\left(
    \theta,
    \frac{1}{n I_1(\theta)}
    \right)
    \quad \text{for large } n.
    \]
  </div>

  <p class="muted-mini">
    The asymptotic variance equals the inverse of total information.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Why information appears</h2>
  </div>

  <div class="card">
    Near the true parameter,
    the log-likelihood can be approximated by a quadratic expansion:
    \[
    \ell(\theta)
    \approx
    \ell(\theta_0)
    -
    \frac{n I_1(\theta_0)}{2}
    (\theta-\theta_0)^2.
    \]
  </div>

  <p>
    The curvature coefficient \(n I_1(\theta_0)\)
    determines how sharply peaked the likelihood is.
  </p>

  <p class="muted-mini">
    Sharper peak → smaller variance.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Connection to CRLB</h2>
  </div>

  <div class="card">
    Recall the CRLB:
    \[
    \text{Var}(\hat{\theta})
    \ge
    \frac{1}{n I_1(\theta)}.
    \]
  </div>

  <p>
    The asymptotic variance of the MLE equals this lower bound.
  </p>

  <p class="muted-mini">
    The MLE is asymptotically efficient.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Interpretation</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Finite sample</h3>
      <p style="margin:0;">
        MLE may not achieve CRLB exactly.
      </p>
    </div>

    <div class="card">
      <h3>Large sample</h3>
      <p style="margin:0;">
        MLE variance approaches the lower bound.
      </p>
    </div>

    <div class="card">
      <h3>Information controls precision</h3>
      <p style="margin:0;">
        Larger information → tighter normal approximation.
      </p>
    </div>

    <div class="card">
      <h3>Regularity matters</h3>
      <p style="margin:0;">
        Without assumptions, asymptotic normality can fail.
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Example: Normal mean (known variance)</h2>
  </div>

  <div class="card">
    For \(X_i \sim \mathcal{N}(\mu,\sigma^2)\),
    the MLE is
    \[
    \hat{\mu} = \bar{X}.
    \]
  </div>

  <div class="card">
    Fisher information:
    \[
    I_1(\mu) = \frac{1}{\sigma^2}.
    \]
  </div>

  <div class="card">
    Asymptotic variance:
    \[
    \frac{1}{n I_1(\mu)}
    =
    \frac{\sigma^2}{n}.
    \]
  </div>

  <p class="muted-mini">
    In this model, the result is exact—not only asymptotic.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>See the asymptotic normality of MLE (informally)</li>
        <li>Understand variance ≈ 1/(nI₁)</li>
        <li>Connect Fisher information to precision</li>
        <li>Prepare for formal asymptotic theory</li>
      </ul>
    </div>
  </div>
</section>

<!-- ✅ Transition to next block -->
<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next block</h2>
      <p style="margin:0;">
        We now formalize large-sample theory:
        convergence concepts, consistency, and asymptotic normality.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/asymptotic-theory/">
          Continue to Block 6 — Asymptotic Theory →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/fisher-information-and-efficiency/information-additivity-and-iid/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Information Additivity and IID
          </a>
        </div>
      </div>
    </div>

  </div>
</section>