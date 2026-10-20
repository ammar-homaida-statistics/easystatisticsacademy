---
layout: default
title: "2. Cramér–Rao Lower Bound"
description: "Derive and interpret the Cramér–Rao lower bound for unbiased estimators."
permalink: /mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/
sidebar: false
math: true
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#eef5ff; border:2px solid #3f51b5; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#283593; line-height:1.6;">
        Version 0 derives the scalar Cramér–Rao lower bound (CRLB).
        Later versions will include the multivariate matrix form.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    "use strict";
    try {
    localStorage.setItem(
      "esa_continue_ms_information_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/",
        label: "Lesson 2 — Cramér–Rao Lower Bound",
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
    } catch (_) {
      // Blocked storage must never prevent a student from using this lesson or its interactive explorer.
    }
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">CRLB</span>
        <span class="badge">Variance Bound</span>
      </div>

      <h1>2. Cramér–Rao Lower Bound</h1>

      <p class="lead">
        The Cramér–Rao lower bound gives a fundamental lower limit
        on the variance of unbiased estimators.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/fisher-information-and-efficiency/">Back to Block 5</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        No unbiased estimator can beat this bound.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Derive the Cramér–Rao lower bound and understand its interpretation
      as a theoretical precision limit.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Statement of the bound</h2>
  </div>

  <div class="card">
    If \(\hat{\theta}\) is an unbiased estimator of \(\theta\),
    then
    \[
    \text{Var}(\hat{\theta})
    \ge
    \frac{1}{I(\theta)}.
    \]
  </div>

  <p class="muted-mini">
    \(I(\theta)\) is the Fisher information.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Idea of the proof</h2>
  </div>

  <div class="card">
    Start from the score:
    \[
    U(\theta)
    =
    \frac{\partial}{\partial \theta}\ell(\theta).
    \]
  </div>

  <div class="card">
    Under regularity conditions:
    \[
    \mathbb{E}[U(\theta)] = 0.
    \]
  </div>

  <div class="card">
    Use covariance and Cauchy–Schwarz inequality
    to derive the variance bound.
  </div>

  <p class="muted-mini">
    The proof relies on orthogonality between estimator error and score.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Interpretation</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Precision limit</h3>
      <p style="margin:0;">
        Variance cannot be smaller than \(1/I(\theta)\).
      </p>
    </div>

    <div class="card">
      <h3>Model-dependent</h3>
      <p style="margin:0;">
        The bound depends on the statistical model.
      </p>
    </div>

    <div class="card">
      <h3>Sample size effect</h3>
      <p style="margin:0;">
        For IID data, bound shrinks as \(n\) increases.
      </p>
    </div>

    <div class="card">
      <h3>Unbiasedness requirement</h3>
      <p style="margin:0;">
        The bound applies to unbiased estimators.
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Example: Bernoulli model</h2>
  </div>

  <div class="card">
    For \(X_i \sim \text{Bernoulli}(p)\):
    \[
    I(p)
    =
    \frac{n}{p(1-p)}.
    \]
  </div>

  <div class="card">
    Therefore,
    \[
    \text{Var}(\hat{p})
    \ge
    \frac{p(1-p)}{n}.
    \]
  </div>

  <p class="muted-mini">
    The sample proportion achieves this bound.
  </p>
</section>

<section class="section" aria-labelledby="esa-crlb-title">
<div class="content-narrow">
  <div class="concept-box" id="esa-crlb-lab" style="max-width:100%;min-width:0;overflow-x:clip;overflow-wrap:anywhere">
    <h2 id="esa-crlb-title">Interactive Bernoulli Cramér–Rao Explorer</h2>
    <p>Compare two unbiased estimators of the success probability in <strong>n independent Bernoulli(p) observations</strong>: the sample proportion \(\overline{X}\), which uses the full sample, and \(X_1\), which uses only the first observation. Both estimate the same interior parameter \(0&lt;p&lt;1\).</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;align-items:end">
      <label for="esa-crlb-p">Success probability p (strictly between 0 and 1)
        <input id="esa-crlb-p" type="number" min="0.001" max="0.999" step="0.01" value="0.30" inputmode="decimal" style="display:block;width:100%;max-width:12rem">
      </label>
      <label for="esa-crlb-n">Sample size n (1–500)
        <input id="esa-crlb-n" type="number" min="1" max="500" step="1" value="20" inputmode="numeric" style="display:block;width:100%;max-width:12rem">
      </label>
      <button class="btn" id="esa-crlb-run" type="button">Compute bound</button>
      <button class="btn btn-outline" id="esa-crlb-reset" type="button">Reset</button>
    </div>
    <p id="esa-crlb-status" role="status" aria-live="polite"></p>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,190px),1fr));gap:1rem">
      <div class="example-box" style="min-width:0;overflow-wrap:anywhere">
        <h3>Information and bound</h3>
        <p>Fisher information: <output id="esa-crlb-information">—</output></p>
        <p>CRLB: <output id="esa-crlb-crlb">—</output></p>
      </div>
      <div class="example-box" style="min-width:0;overflow-wrap:anywhere">
        <h3>Sample proportion (efficient)</h3>
        <p>Variance: <output id="esa-crlb-variance-mean">—</output></p>
        <p>Efficiency: <output id="esa-crlb-efficiency-mean">—</output></p>
      </div>
      <div class="example-box" style="min-width:0;overflow-wrap:anywhere">
        <h3>First observation X₁ (unbiased)</h3>
        <p>Variance: <output id="esa-crlb-variance-first">—</output></p>
        <p>Efficiency: <output id="esa-crlb-efficiency-first">—</output></p>
        <p>Variance relative to CRLB: <output id="esa-crlb-ratio">—</output></p>
      </div>
    </div>
    <h3>Mathematical reference</h3>
    <div style="max-width:100%;overflow-x:auto" role="region" aria-label="Bernoulli information and variance identities" tabindex="0">
    \[
    I_n(p)=\frac{n}{p(1-p)},\qquad
    \operatorname{CRLB}=\frac{p(1-p)}{n},\qquad 0<p<1.
    \]
    \[
    \operatorname{Var}(\bar X)=\frac{p(1-p)}n,\quad
    \operatorname{Var}(X_1)=p(1-p).
    \]
    </div>
    <p>The <strong>variance-based efficiency</strong> of an unbiased estimator is the lower bound divided by the estimator variance. Consequently, the sample proportion has 100% efficiency, while \(X_1\) has efficiency \(1/n\). At \(n=1\), the estimators coincide. This is an exact finite-sample result under the regular IID Bernoulli model, not a general bound on biased estimators.</p>
    <p><strong>Independent benchmark:</strong> At p = 0.30 and n = 20, \(I_n=95.238095\), CRLB = 0.010500, Var(\(\bar X\)) = 0.010500, Var(\(X_1\)) = 0.210000, and efficiency(\(X_1\)) = 5%. The expression \(I_n(p)\) applies to <em>interior</em> p, not p=0 or p=1.</p>
    <p><strong>Regularity:</strong> The support is fixed, observations are independent with the same p, and differentiation and expectation interchange under the usual regularity conditions. The familiar scalar bound concerns estimators unbiased throughout a neighborhood of the parameter. No separate numerical simulation is necessary because both variance expressions are exact.</p>
  </div>
</div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>State the Cramér–Rao bound</li>
        <li>Understand its proof idea</li>
        <li>Interpret it as a precision limit</li>
        <li>Prepare for efficiency concept</li>
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
        We now define efficiency and examine when
        the Cramér–Rao bound can be achieved.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/fisher-information-and-efficiency/efficiency-and-achieving-the-bound/">
          Continue to Lesson 3 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/fisher-information-and-efficiency/fisher-information-definition/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: Fisher Information
          </a>
        </div>
      </div>
    </div>

  </div>
</section>
<script src="/js/bernoulli-crlb-explorer.js" defer></script>
