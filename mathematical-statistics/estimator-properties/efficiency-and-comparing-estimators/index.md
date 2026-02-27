---
layout: default
title: "4. Efficiency and Comparing Estimators"
description: "Compare estimators using variance and MSE and introduce the idea of efficiency."
permalink: /mathematical-statistics/estimator-properties/efficiency-and-comparing-estimators/
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
        Version 0 introduces estimator comparison via variance and MSE
        and defines relative efficiency. Later versions will connect this
        to the Cramér–Rao lower bound.
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
        url: "/mathematical-statistics/estimator-properties/efficiency-and-comparing-estimators/",
        label: "Lesson 4 — Efficiency and Comparing Estimators",
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
        <span class="badge">Lesson 4</span>
        <span class="badge">Efficiency</span>
        <span class="badge">Comparison</span>
      </div>

      <h1>4. Efficiency and Comparing Estimators</h1>

      <p class="lead">
        When multiple estimators exist for the same parameter,
        we need principled criteria to decide which one is better.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/estimator-properties/">Back to Block 4</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Smaller variance (or MSE) implies greater precision.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Compare estimators using variance and MSE,
      and define the concept of relative efficiency.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Comparing unbiased estimators</h2>
  </div>

  <div class="card">
    Suppose \(\hat{\theta}_1\) and \(\hat{\theta}_2\) are unbiased.
  </div>

  <div class="card">
    We prefer the estimator with smaller variance:
    \[
    \text{Var}(\hat{\theta}_1) < \text{Var}(\hat{\theta}_2).
    \]
  </div>

  <p class="muted-mini">
    Among unbiased estimators, lower variance means greater precision.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Comparing general estimators</h2>
  </div>

  <div class="card">
    In general, we compare mean squared error:
    \[
    \text{MSE}(\hat{\theta})
    =
    \text{Var}(\hat{\theta})
    +
    \text{Bias}(\hat{\theta})^2.
    \]
  </div>

  <p>
    An estimator with lower MSE is preferable,
    even if it is slightly biased.
  </p>

  <p class="muted-mini">
    This motivates shrinkage estimators.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Relative efficiency</h2>
  </div>

  <div class="card">
    The relative efficiency of \(\hat{\theta}_1\) to \(\hat{\theta}_2\) is
    \[
    \text{Eff}(\hat{\theta}_1, \hat{\theta}_2)
    =
    \frac{\text{Var}(\hat{\theta}_2)}{\text{Var}(\hat{\theta}_1)}.
    \]
  </div>

  <p class="muted-mini">
    If this ratio is greater than 1,
    \(\hat{\theta}_1\) is more efficient.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Example: Mean vs single observation</h2>
  </div>

  <div class="card">
    For IID data with variance \(\sigma^2\):
    \[
    \text{Var}(\bar{X})
    =
    \frac{\sigma^2}{n}.
    \]
  </div>

  <div class="card">
    For a single observation:
    \[
    \text{Var}(X_1) = \sigma^2.
    \]
  </div>

  <p class="muted-mini">
    The sample mean is \(n\)-times more efficient.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Finite-sample vs asymptotic efficiency</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Finite-sample</h3>
      <p style="margin:0;">
        Compare exact variances.
      </p>
    </div>

    <div class="card">
      <h3>Asymptotic</h3>
      <p style="margin:0;">
        Compare limiting variances as \(n \to \infty\).
      </p>
    </div>

  </div>

  <p class="muted-mini">
    Asymptotic efficiency becomes central in later blocks.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Compare unbiased estimators via variance</li>
        <li>Compare general estimators via MSE</li>
        <li>Define relative efficiency</li>
        <li>Prepare for information-based efficiency bounds</li>
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
        We now preview sufficiency and how some statistics
        preserve all information about the parameter.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/estimator-properties/sufficiency-preview/">
          Continue to Lesson 5 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/estimator-properties/consistency-basic-idea/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Consistency
          </a>
        </div>
      </div>
    </div>

  </div>
</section>