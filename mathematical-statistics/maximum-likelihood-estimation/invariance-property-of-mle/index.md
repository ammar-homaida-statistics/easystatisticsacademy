---
layout: default
title: "3. Invariance Property of MLE"
description: "Understand the invariance property of maximum likelihood estimators under transformations."
permalink: /mathematical-statistics/maximum-likelihood-estimation/invariance-property-of-mle/
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
        Version 0 introduces the invariance property and its intuition.
        Later versions will include multidimensional examples and geometric visualization.
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
        url: "/mathematical-statistics/maximum-likelihood-estimation/invariance-property-of-mle/",
        label: "Lesson 3 — Invariance Property of MLE",
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
        <span class="badge">Lesson 3</span>
        <span class="badge">Transformation</span>
        <span class="badge">Structure</span>
      </div>

      <h1>3. Invariance Property of MLE</h1>

      <p class="lead">
        If \(\hat{\theta}\) is the MLE of \(\theta\),
        then the MLE of a function \(g(\theta)\) is
        simply \(g(\hat{\theta})\).
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/maximum-likelihood-estimation/">Back to Block 3</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        MLE transforms naturally.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand and prove the invariance property of maximum likelihood estimators,
      and interpret why it holds.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Statement of the invariance property</h2>
  </div>

  <div class="card">
    Suppose \(\hat{\theta}\) maximizes \(L(\theta)\).
    For a function \(g(\theta)\), define
    \[
    \psi = g(\theta).
    \]
  </div>

  <div class="card">
    Then the MLE of \(\psi\) is
    \[
    \hat{\psi}
    =
    g(\hat{\theta}).
    \]
  </div>

  <p class="muted-mini">
    We do not need to re-maximize the likelihood in terms of \(\psi\).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Why this works</h2>
  </div>

  <div class="card">
    The likelihood is maximized at \(\hat{\theta}\).
    Any transformation of the parameter does not change
    which value of \(\theta\) maximizes the likelihood.
  </div>

  <div class="card">
    If
    \[
    L(\hat{\theta}) \ge L(\theta)
    \quad \forall \theta,
    \]
    then
    \[
    g(\hat{\theta})
    \text{ corresponds to the maximizing parameter value.}
    \]
  </div>

  <p class="muted-mini">
    The maximizer transforms consistently.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Example: Bernoulli model</h2>
  </div>

  <div class="card">
    If \(X_i \sim \text{Bernoulli}(p)\),
    \[
    \hat{p} = \bar{X}.
    \]
  </div>

  <div class="card">
    Suppose we want the MLE of
    \[
    \psi = p(1-p).
    \]
  </div>

  <div class="card">
    By invariance:
    \[
    \hat{\psi}
    =
    \hat{p}(1-\hat{p})
    =
    \bar{X}(1-\bar{X}).
    \]
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Example: Normal variance</h2>
  </div>

  <div class="card">
    For \(X_i \sim N(\mu,\sigma^2)\),
    the MLE of \(\sigma^2\) is
    \[
    \hat{\sigma}^2
    =
    \frac{1}{n}\sum (X_i-\bar{X})^2.
    \]
  </div>

  <div class="card">
    The MLE of \(\sigma\) is therefore
    \[
    \hat{\sigma}
    =
    \sqrt{\hat{\sigma}^2}.
    \]
  </div>

  <p class="muted-mini">
    No additional maximization is required.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why this property is special</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Method of moments</h3>
      <p style="margin:0;">
        Does not generally satisfy invariance.
      </p>
    </div>

    <div class="card">
      <h3>MLE</h3>
      <p style="margin:0;">
        Automatically invariant under transformations.
      </p>
    </div>

    <div class="card">
      <h3>Practical importance</h3>
      <p style="margin:0;">
        Simplifies estimation of derived parameters.
      </p>
    </div>

    <div class="card">
      <h3>Theoretical importance</h3>
      <p style="margin:0;">
        Reflects optimization-based construction.
      </p>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>State the invariance property</li>
        <li>Understand why it holds</li>
        <li>Apply invariance in simple models</li>
        <li>Recognize its structural importance</li>
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
        We now study when MLE exists and whether it is unique.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/maximum-likelihood-estimation/existence-and-uniqueness/">
          Continue to Lesson 4 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/maximum-likelihood-estimation/finding-mle-by-optimization/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Finding MLE by Optimization
          </a>
        </div>
      </div>
    </div>

  </div>
</section>