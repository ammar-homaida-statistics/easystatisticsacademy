---
layout: default
title: "2. Consistency of MLE (Idea)"
description: "Understand why the maximum likelihood estimator converges to the true parameter under regularity conditions."
permalink: /mathematical-statistics/asymptotic-theory/consistency-of-mle-idea/
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
        Version 0 explains the intuition behind MLE consistency.
        Later versions will include formal proofs using the law of large numbers.
      </p>
    </div>
  </div>
</section>

<!-- Continue-reading tracking -->
<script>
(function(){

  localStorage.setItem(
    "esa_continue_ms_asymptotics_last_lesson_v0",
    JSON.stringify({
      url:"/mathematical-statistics/asymptotic-theory/consistency-of-mle-idea/",
      label:"Lesson 2 — Consistency of MLE",
      ts:Date.now()
    })
  );

  localStorage.setItem(
    "esa_continue_ms_last_block_v0",
    JSON.stringify({
      url:"/mathematical-statistics/asymptotic-theory/",
      label:"Block 6 — Asymptotic Theory",
      ts:Date.now()
    })
  );

})();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Consistency</span>
        <span class="badge">MLE</span>
      </div>

      <h1>2. Consistency of the Maximum Likelihood Estimator</h1>

      <p class="lead">
        A consistent estimator approaches the true parameter value
        as the sample size grows.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/">Back to Block 6</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Under mild conditions, the MLE is consistent.
      </p>

    </div>
  </div>
</section>

<section class="section">
<div class="section-head">
<h2>Learning objective</h2>
<p>
Understand why maximizing likelihood tends to recover the true parameter
when sample size becomes large.
</p>
</div>
</section>

<section class="section">
<div class="section-head">
<h2>1) Definition of consistency</h2>
</div>

<div class="card">

An estimator \(\hat{\theta}_n\) is consistent for \(\theta\) if

\[
\hat{\theta}_n \xrightarrow{p} \theta.
\]

</div>

<p style="margin-top:.75rem;">
This means the estimator converges in probability to the true parameter.
</p>

<p class="muted-mini">
Large samples lead to increasingly accurate estimates.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>2) Why likelihood identifies the true parameter</h2>
</div>

<div class="card">

The expected log-likelihood

\[
E[\log f(X;\theta)]
\]

is maximized at the true parameter value \(\theta_0\).

</div>

<p>
This occurs because the model that generated the data
best explains the observations.
</p>

<p class="muted-mini">
The true parameter maximizes expected log-likelihood.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>3) Role of the Law of Large Numbers</h2>
</div>

<div class="card">

The sample log-likelihood is

\[
\ell_n(\theta)
=
\sum_{i=1}^{n} \log f(X_i;\theta).
\]

</div>

<div class="card">

By the Law of Large Numbers,

\[
\frac{1}{n}\ell_n(\theta)
\rightarrow
E[\log f(X;\theta)].
\]

</div>

<p class="muted-mini">
The empirical log-likelihood approaches its expectation.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>4) Why the MLE converges</h2>
</div>

<div class="grid grid-2">

<div class="card">
<h3>Large samples</h3>
<p style="margin:0;">
The empirical likelihood resembles its expectation.
</p>
</div>

<div class="card">
<h3>Expectation maximized at truth</h3>
<p style="margin:0;">
The true parameter maximizes expected log-likelihood.
</p>
</div>

<div class="card">
<h3>Maximum stays near truth</h3>
<p style="margin:0;">
The likelihood peak moves toward the true parameter.
</p>
</div>

<div class="card">
<h3>Result</h3>
<p style="margin:0;">
MLE converges to the true parameter.
</p>
</div>

</div>

</section>

<section class="section">
<div class="section-head">
<h2>5) Example: Normal mean</h2>
</div>

<div class="card">

For \(X_i \sim N(\mu,\sigma^2)\),

\[
\hat{\mu} = \bar{X}.
\]

</div>

<p>
By the Law of Large Numbers,

\[
\bar{X} \xrightarrow{p} \mu.
\]

</p>

<p class="muted-mini">
Thus the MLE of the mean is consistent.
</p>

</section>

<section class="section section-slim">

<div class="callout">
<div class="callout-copy">

<h2>Outcome of this lesson</h2>

<ul class="bullets">
<li>Define estimator consistency</li>
<li>Understand why MLE is consistent</li>
<li>See the role of the Law of Large Numbers</li>
<li>Connect likelihood maximization to truth recovery</li>
</ul>

</div>
</div>

</section>

<!-- Navigation -->

<section class="section section-slim">

<div class="callout">

<div class="callout-copy">

<h2>Next lesson</h2>

<p style="margin:0;">
We now derive the central asymptotic result:
the maximum likelihood estimator is asymptotically normal.
</p>

<div class="pill-row" style="margin-top:1rem;">
<a class="btn" href="/mathematical-statistics/asymptotic-theory/asymptotic-normality-of-mle/">
Continue to Lesson 3 →
</a>
</div>

</div>

<div class="callout-side">

<div class="mini" style="border-left:4px solid #1a73e8;padding-left:12px;">

<div class="mini-title" style="color:#1a73e8;">
Previous lesson
</div>

<div class="mini-body">
<a href="/mathematical-statistics/asymptotic-theory/modes-of-convergence-review/" style="color:#1a73e8;text-decoration:underline;">
Lesson 1: Modes of Convergence
</a>
</div>

</div>

</div>

</div>

</section>