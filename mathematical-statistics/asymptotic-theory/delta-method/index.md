---
layout: default
title: "5. Delta Method"
description: "Approximate the distribution of transformations of estimators using Taylor expansion."
permalink: /mathematical-statistics/asymptotic-theory/delta-method/
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
        Version 0 introduces the delta method as a tool for approximating
        the distribution of transformed estimators using Taylor expansion.
        Later versions will include multivariate forms and detailed proofs.
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
      url:"/mathematical-statistics/asymptotic-theory/delta-method/",
      label:"Lesson 5 — Delta Method",
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
        <span class="badge">Lesson 5</span>
        <span class="badge">Delta Method</span>
        <span class="badge">Transformations</span>
      </div>

      <h1>5. Delta Method</h1>

      <p class="lead">
        The delta method approximates the distribution of functions of estimators
        using Taylor expansion and asymptotic normality.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/">Back to Block 6</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        This method is widely used to obtain approximate variances of transformed estimators.
      </p>

    </div>
  </div>
</section>

<section class="section">
<div class="section-head">
<h2>Learning objective</h2>
<p>
Understand how Taylor expansion can be used to approximate the distribution
of functions of asymptotically normal estimators.
</p>
</div>
</section>

<section class="section">
<div class="section-head">
<h2>1) Basic idea</h2>
</div>

<div class="card">

Suppose an estimator satisfies

\[
\sqrt{n}(\hat{\theta}-\theta)
\xrightarrow{d}
N(0,\sigma^2).
\]

</div>

<p>
We often want the distribution of a transformed estimator \(g(\hat{\theta})\).
</p>

<div class="card">

The delta method approximates this distribution using
a first-order Taylor expansion.
</div>

</section>

<section class="section">
<div class="section-head">
<h2>2) First-order Taylor approximation</h2>
</div>

<div class="card">

For a differentiable function \(g(\theta)\),

\[
g(\hat{\theta})
\approx
g(\theta)
+
g'(\theta)(\hat{\theta}-\theta).
\]

</div>

<p>
This linear approximation allows the asymptotic distribution
to be derived easily.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>3) Delta method result</h2>
</div>

<div class="card">

If

\[
\sqrt{n}(\hat{\theta}-\theta)
\xrightarrow{d}
N(0,\sigma^2)
\]

then

\[
\sqrt{n}(g(\hat{\theta})-g(\theta))
\xrightarrow{d}
N(0,[g'(\theta)]^2\sigma^2).
\]

</div>

<p class="muted-mini">
The variance is scaled by the square of the derivative.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>4) Interpretation</h2>
</div>

<div class="grid grid-2">

<div class="card">
<h3>Transformation effect</h3>
<p style="margin:0;">
Nonlinear transformations change estimator variance.
</p>
</div>

<div class="card">
<h3>Derivative role</h3>
<p style="margin:0;">
The derivative \(g'(\theta)\) measures sensitivity to changes in the parameter.
</p>
</div>

<div class="card">
<h3>Approximate inference</h3>
<p style="margin:0;">
Confidence intervals for transformed parameters use this result.
</p>
</div>

<div class="card">
<h3>General applicability</h3>
<p style="margin:0;">
The method applies whenever the estimator is asymptotically normal.
</p>
</div>

</div>

</section>

<section class="section">
<div class="section-head">
<h2>5) Example</h2>
</div>

<div class="card">

Suppose

\[
\hat{p}
\sim
N\left(p,\frac{p(1-p)}{n}\right)
\]

for large \(n\).

</div>

<p>
Consider the transformation

\[
g(p)=\log(p).
\]

</p>

<div class="card">

The derivative is

\[
g'(p)=\frac{1}{p}.
\]

</div>

<div class="card">

Therefore

\[
Var(\log(\hat{p}))
\approx
\frac{1}{p^2}
\cdot
\frac{p(1-p)}{n}.
\]

</div>

<p class="muted-mini">
The delta method approximates the variance of transformed estimators.
</p>

</section>

<section class="section section-slim">

<div class="callout">
<div class="callout-copy">

<h2>Outcome of this lesson</h2>

<ul class="bullets">
<li>Understand the purpose of the delta method</li>
<li>Use Taylor expansion for approximation</li>
<li>Compute approximate variances of transformed estimators</li>
<li>Prepare for inference with nonlinear parameters</li>
</ul>

</div>
</div>

</section>

<section class="section section-slim">

<div class="callout">

<div class="callout-copy">

<h2>Next block</h2>

<p style="margin:0;">
We now move beyond maximum likelihood and study
alternative estimation strategies used in statistical modeling.
</p>

<div class="pill-row" style="margin-top:1rem;">
<a class="btn" href="/mathematical-statistics/alternative-estimation-methods/">
Continue to Block 7 →
</a>
</div>

</div>

<div class="callout-side">

<div class="mini" style="border-left:4px solid #1a73e8;padding-left:12px;">

<div class="mini-title" style="color:#1a73e8;">
Previous lesson
</div>

<div class="mini-body">
<a href="/mathematical-statistics/asymptotic-theory/slutsky-theorem-and-continuous-mapping/" style="color:#1a73e8;text-decoration:underline;">
Lesson 4: Slutsky Theorem
</a>
</div>

</div>

</div>

</div>

</section>