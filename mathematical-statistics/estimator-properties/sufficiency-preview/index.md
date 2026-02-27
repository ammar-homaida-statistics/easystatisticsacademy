---
layout: default
title: "5. Sufficiency (Preview)"
description: "Introduce sufficient statistics and understand how data can be compressed without losing information about the parameter."
permalink: /mathematical-statistics/estimator-properties/sufficiency-preview/
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
        Version 0 introduces the idea of sufficiency conceptually.
        Later versions will include the factorization theorem and formal proofs.
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
        url: "/mathematical-statistics/estimator-properties/sufficiency-preview/",
        label: "Lesson 5 — Sufficiency (Preview)",
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
        <span class="badge">Lesson 5</span>
        <span class="badge">Sufficiency</span>
        <span class="badge">Information</span>
      </div>

      <h1>5. Sufficiency (Preview)</h1>

      <p class="lead">
        A statistic is sufficient if it captures all information
        in the sample about the parameter.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/estimator-properties/">Back to Block 4</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Sufficiency is about information compression without loss.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand the intuition behind sufficient statistics
      and why they matter in estimation theory.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Intuitive idea</h2>
  </div>

  <div class="card">
    Suppose we observe data \(X_1, \dots, X_n\).
  </div>

  <div class="card">
    A statistic \(T(X)\) is sufficient if,
    once we know \(T(X)\),
    the remaining data provide no additional information about \(\theta\).
  </div>

  <p class="muted-mini">
    The statistic summarizes everything relevant to the parameter.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Example: Bernoulli model</h2>
  </div>

  <div class="card">
    For IID Bernoulli(\(p\)):
    \[
    T = \sum_{i=1}^n X_i
    \]
    is sufficient for \(p\).
  </div>

  <p>
    The full dataset is not needed — only the total number of successes.
  </p>

  <p class="muted-mini">
    All information about \(p\) is contained in the sum.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Example: Normal model</h2>
  </div>

  <div class="card">
    If \(X_i \sim N(\mu, \sigma^2)\) with known variance,
    the sample mean \(\bar{X}\) is sufficient for \(\mu\).
  </div>

  <p class="muted-mini">
    Again, the data reduce to a lower-dimensional summary.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Why sufficiency matters</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Data reduction</h3>
      <p style="margin:0;">
        Compress data without losing parameter information.
      </p>
    </div>

    <div class="card">
      <h3>Efficiency</h3>
      <p style="margin:0;">
        Efficient estimators often depend only on sufficient statistics.
      </p>
    </div>

    <div class="card">
      <h3>Likelihood structure</h3>
      <p style="margin:0;">
        Likelihood often depends on the data only through a sufficient statistic.
      </p>
    </div>

    <div class="card">
      <h3>Foundation for MVUE</h3>
      <p style="margin:0;">
        Leads to Rao–Blackwell and Lehmann–Scheffé results.
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Formal definition (preview)</h2>
  </div>

  <div class="card">
    A statistic \(T(X)\) is sufficient if the conditional distribution
    of \(X\) given \(T(X)\) does not depend on \(\theta\).
  </div>

  <p class="muted-mini">
    Full formal treatment appears later using the factorization theorem.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand the intuition of sufficiency</li>
        <li>See examples in Bernoulli and Normal models</li>
        <li>Recognize its role in efficiency theory</li>
        <li>Prepare for Fisher information</li>
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
        We now formalize information and derive
        efficiency bounds using Fisher information.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/fisher-information-and-efficiency/">
          Continue to Block 5 — Fisher Information →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/estimator-properties/efficiency-and-comparing-estimators/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Efficiency and Comparing Estimators
          </a>
        </div>
      </div>
    </div>

  </div>
</section>