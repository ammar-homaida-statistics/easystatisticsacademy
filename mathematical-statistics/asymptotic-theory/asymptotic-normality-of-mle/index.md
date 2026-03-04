---
layout: default
title: "3. Asymptotic Normality of MLE"
description: "Understand the asymptotic normal distribution of the maximum likelihood estimator and its role in inference."
permalink: /mathematical-statistics/asymptotic-theory/asymptotic-normality-of-mle/
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
        Version 0 introduces the asymptotic normality of the maximum likelihood estimator.
        Later versions will include a full proof using Taylor expansion of the score.
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
      url:"/mathematical-statistics/asymptotic-theory/asymptotic-normality-of-mle/",
      label:"Lesson 3 — Asymptotic Normality of MLE",
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
        <span class="badge">Lesson 3</span>
        <span class="badge">MLE</span>
        <span class="badge">Normal Approximation</span>
      </div>

      <h1>3. Asymptotic Normality of the MLE</h1>

      <p class="lead">
        Under regularity conditions, the maximum likelihood estimator
        becomes approximately normally distributed as sample size grows.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/">Back to Block 6</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        This result enables standard errors, confidence intervals, and Wald tests.
      </p>

    </div>
  </div>
</section>

<section class="section">
<div class="section-head">
<h2>Learning objective</h2>
<p>
Understand the asymptotic distribution of the MLE and why it becomes approximately normal for large samples.
</p>
</div>
</section>

<section class="section">
<div class="section-head">
<h2>1) Main asymptotic result</h2>
</div>

<div class="card">

Under regularity conditions,

\[
\sqrt{n}(\hat{\theta}-\theta)
\xrightarrow{d}
\mathcal{N}(0,I_1(\theta)^{-1})
\]

</div>

<p style="margin-top:.75rem;">
Equivalently,

\[
\hat{\theta}
\approx
\mathcal{N}
\left(
\theta,
\frac{1}{n I_1(\theta)}
\right)
\]

for large sample sizes.
</p>

<p class="muted-mini">
The variance depends on Fisher information.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>2) Intuition behind the result</h2>
</div>

<div class="card">

Near the true parameter, the log-likelihood can be approximated by
a quadratic function:

\[
\ell(\theta)
\approx
\ell(\theta_0)
-
\frac{n I_1(\theta_0)}{2}
(\theta-\theta_0)^2
\]

</div>

<p>
The maximum of this quadratic approximation produces
a normally distributed estimator.
</p>

<p class="muted-mini">
Likelihood curvature determines estimator variance.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>3) Role of the score function</h2>
</div>

<div class="card">

The MLE satisfies

\[
U(\hat{\theta}) = 0
\]

where

\[
U(\theta) = \frac{\partial}{\partial\theta}\ell(\theta)
\]

is the score function.
</div>

<div class="card">

A Taylor expansion around the true parameter gives

\[
0
\approx
U(\theta)
+
(\hat{\theta}-\theta)U'(\theta)
\]

</div>

<p class="muted-mini">
Combining this expansion with the central limit theorem leads to asymptotic normality.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>4) Practical interpretation</h2>
</div>

<div class="grid grid-2">

<div class="card">
<h3>Large samples</h3>
<p style="margin:0;">
MLE behaves approximately normally.
</p>
</div>

<div class="card">
<h3>Variance estimate</h3>
<p style="margin:0;">
Variance ≈ \(1/(nI_1(\theta))\)
</p>
</div>

<div class="card">
<h3>Confidence intervals</h3>
<p style="margin:0;">
Normal approximation allows interval construction.
</p>
</div>

<div class="card">
<h3>Hypothesis tests</h3>
<p style="margin:0;">
Wald statistics rely on this result.
</p>
</div>

</div>

</section>

<section class="section">
<div class="section-head">
<h2>5) Example: Normal mean</h2>
</div>

<div class="card">

For \(X_i \sim N(\mu,\sigma^2)\)

\[
\hat{\mu} = \bar{X}
\]

</div>

<div class="card">

\[
\sqrt{n}(\bar{X}-\mu)
\xrightarrow{d}
N(0,\sigma^2)
\]

</div>

<p class="muted-mini">
This result is exact for the normal model.
</p>

</section>

<section class="section section-slim">

<div class="callout">
<div class="callout-copy">

<h2>Outcome of this lesson</h2>

<ul class="bullets">
<li>Understand asymptotic normality of MLE</li>
<li>See the connection between Fisher information and variance</li>
<li>Understand the role of Taylor expansion and CLT</li>
<li>Prepare for transformation tools such as Slutsky and the delta method</li>
</ul>

</div>
</div>

</section>

<section class="section section-slim">

<div class="callout">

<div class="callout-copy">

<h2>Next lesson</h2>

<p style="margin:0;">
We now introduce Slutsky’s theorem and the continuous mapping theorem,
which allow combining and transforming asymptotic results.
</p>

<div class="pill-row" style="margin-top:1rem;">
<a class="btn" href="/mathematical-statistics/asymptotic-theory/slutsky-theorem-and-continuous-mapping/">
Continue to Lesson 4 →
</a>
</div>

</div>

<div class="callout-side">

<div class="mini" style="border-left:4px solid #1a73e8;padding-left:12px;">

<div class="mini-title" style="color:#1a73e8;">
Previous lesson
</div>

<div class="mini-body">
<a href="/mathematical-statistics/asymptotic-theory/consistency-of-mle-idea/" style="color:#1a73e8;text-decoration:underline;">
Lesson 2: Consistency of MLE
</a>
</div>

</div>

</div>

</div>

</section>