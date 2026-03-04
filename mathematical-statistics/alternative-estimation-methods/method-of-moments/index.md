---
layout: default
title: "1. Method of Moments"
description: "Construct estimators by matching theoretical moments to sample moments."
permalink: /mathematical-statistics/alternative-estimation-methods/method-of-moments/
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
        Version 0 introduces the method of moments as an alternative
        estimation approach. Later versions will include multi-parameter
        examples and comparisons with maximum likelihood.
      </p>
    </div>
  </div>
</section>

<!-- Continue-reading tracking -->
<script>
  (function () {

    localStorage.setItem(
      "esa_continue_ms_methods_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/alternative-estimation-methods/method-of-moments/",
        label: "Lesson 1 — Method of Moments",
        ts: Date.now()
      })
    );

    localStorage.setItem(
      "esa_continue_ms_last_block_v0",
      JSON.stringify({
        url: "/mathematical-statistics/alternative-estimation-methods/",
        label: "Block 7 — Alternative Estimation Methods",
        ts: Date.now()
      })
    );

  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Moments</span>
        <span class="badge">Estimation</span>
      </div>

      <h1>1. Method of Moments</h1>

      <p class="lead">
        The method of moments constructs estimators by matching
        theoretical moments of a distribution to sample moments.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/">Back to Block 7</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Estimation by matching model structure to observed data.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand how estimators can be obtained by equating
      sample moments with theoretical moments of a model.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Population moments</h2>
  </div>

  <div class="card">
    A moment of order \(k\) is

\[
\mathbb{E}[X^k].
\]

  </div>

  <p style="margin-top:.75rem;">
    Moments describe key properties of a distribution,
    such as mean and variance.
  </p>

</section>

<section class="section">
  <div class="section-head">
    <h2>2) Sample moments</h2>
  </div>

  <div class="card">

The sample moment of order \(k\) is

\[
\frac{1}{n}\sum_{i=1}^{n} X_i^k .
\]

  </div>

  <p class="muted-mini">
    Sample moments estimate the corresponding population moments.
  </p>

</section>

<section class="section">
  <div class="section-head">
    <h2>3) Method of moments idea</h2>
  </div>

  <div class="card">

The method of moments sets

\[
\text{Sample moment}
=
\text{Population moment}.
\]

  </div>

  <p>
    Solving these equations provides parameter estimates.
  </p>

</section>

<section class="section">
  <div class="section-head">
    <h2>4) Example: estimating the mean</h2>
  </div>

  <div class="card">

Suppose

\[
\mathbb{E}[X] = \mu.
\]

  </div>

  <div class="card">

The sample moment is

\[
\bar{X}.
\]

  </div>

  <div class="card">

Setting them equal gives

\[
\hat{\mu} = \bar{X}.
\]

  </div>

  <p class="muted-mini">
    The sample mean is the method-of-moments estimator for the population mean.
  </p>

</section>

<section class="section">
  <div class="section-head">
    <h2>5) Multiple parameters</h2>
  </div>

  <div class="card">

If a model has \(p\) parameters,
we match the first \(p\) sample moments
to the first \(p\) theoretical moments.

  </div>

  <p>
    This produces a system of equations
    that can be solved for the parameters.
  </p>

</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand what moments are</li>
        <li>Define sample and population moments</li>
        <li>Construct estimators using moment matching</li>
        <li>Prepare for estimating equations</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now generalize the method of moments
        using estimating equations.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/alternative-estimation-methods/estimating-equations-preview/">
          Continue to Lesson 2 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous block</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/asymptotic-theory/" style="color:#1a73e8; text-decoration:underline;">
            Block 6: Asymptotic Theory
          </a>
        </div>
      </div>
    </div>

  </div>
</section>