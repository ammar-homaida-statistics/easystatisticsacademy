---
layout: default
title: "4. Slutsky Theorem and Continuous Mapping"
description: "Understand how asymptotic results combine and transform using Slutsky’s theorem and the continuous mapping theorem."
permalink: /mathematical-statistics/asymptotic-theory/slutsky-theorem-and-continuous-mapping/
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
        Version 0 introduces Slutsky’s theorem and the continuous mapping theorem.
        Later versions will include formal proofs and additional examples.
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
      url:"/mathematical-statistics/asymptotic-theory/slutsky-theorem-and-continuous-mapping/",
      label:"Lesson 4 — Slutsky Theorem",
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
        <span class="badge">Lesson 4</span>
        <span class="badge">Slutsky</span>
        <span class="badge">Continuous Mapping</span>
      </div>

      <h1>4. Slutsky Theorem and Continuous Mapping</h1>

      <p class="lead">
        Slutsky’s theorem and the continuous mapping theorem allow
        combining and transforming asymptotic results.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/">Back to Block 6</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        These tools are essential for deriving asymptotic distributions.
      </p>

    </div>
  </div>
</section>

<section class="section">
<div class="section-head">
<h2>Learning objective</h2>
<p>
Understand how limits behave when random variables are combined or transformed.
</p>
</div>
</section>

<section class="section">
<div class="section-head">
<h2>1) Slutsky’s theorem</h2>
</div>

<div class="card">

Suppose

\[
X_n \xrightarrow{d} X
\]

and

\[
Y_n \xrightarrow{p} c
\]

where \(c\) is a constant.

</div>

<div class="card">

Then

\[
X_n + Y_n \xrightarrow{d} X + c
\]

</div>

<div class="card">

and

\[
X_n Y_n \xrightarrow{d} cX
\]

</div>

<div class="card">

and if \(c\neq 0\)

\[
\frac{X_n}{Y_n} \xrightarrow{d} \frac{X}{c}
\]

</div>

<p class="muted-mini">
Random quantities converging to constants behave like constants asymptotically.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>2) Why Slutsky’s theorem matters</h2>
</div>

<div class="grid grid-2">

<div class="card">
<h3>Standard errors</h3>
<p style="margin:0;">
Unknown variance estimates can replace true variance.
</p>
</div>

<div class="card">
<h3>Studentized statistics</h3>
<p style="margin:0;">
t-statistics rely on Slutsky’s theorem.
</p>
</div>

<div class="card">
<h3>Plug-in estimates</h3>
<p style="margin:0;">
Unknown parameters can be replaced by consistent estimates.
</p>
</div>

<div class="card">
<h3>Asymptotic inference</h3>
<p style="margin:0;">
Confidence intervals rely on this substitution principle.
</p>
</div>

</div>

</section>

<section class="section">
<div class="section-head">
<h2>3) Continuous mapping theorem</h2>
</div>

<div class="card">

If

\[
X_n \xrightarrow{d} X
\]

and \(g(\cdot)\) is a continuous function, then

\[
g(X_n) \xrightarrow{d} g(X).
\]

</div>

<p>
Continuous transformations preserve convergence in distribution.
</p>

<p class="muted-mini">
This theorem allows transforming asymptotic distributions.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>4) Example</h2>
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
(\hat{\theta}-\theta)^2
\]

converges in distribution to

\[
\sigma^2 Z^2
\]

where \(Z\sim N(0,1)\).

</div>

<p class="muted-mini">
This follows from the continuous mapping theorem.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>5) Combined usage</h2>
</div>

<div class="card">

Many asymptotic derivations combine:

- asymptotic normality  
- Slutsky’s theorem  
- continuous mapping theorem  

</div>

<p>
Together they allow deriving complex limiting distributions.
</p>

<p class="muted-mini">
The delta method in the next lesson relies on these tools.
</p>

</section>

<section class="section section-slim">

<div class="callout">
<div class="callout-copy">

<h2>Outcome of this lesson</h2>

<ul class="bullets">
<li>Understand Slutsky’s theorem</li>
<li>Understand the continuous mapping theorem</li>
<li>Learn how asymptotic results combine</li>
<li>Prepare for the delta method</li>
</ul>

</div>
</div>

</section>

<section class="section section-slim">

<div class="callout">

<div class="callout-copy">

<h2>Next lesson</h2>

<p style="margin:0;">
We now introduce the delta method,
which uses Taylor expansion to approximate distributions of transformations.
</p>

<div class="pill-row" style="margin-top:1rem;">
<a class="btn" href="/mathematical-statistics/asymptotic-theory/delta-method/">
Continue to Lesson 5 →
</a>
</div>

</div>

<div class="callout-side">

<div class="mini" style="border-left:4px solid #1a73e8;padding-left:12px;">

<div class="mini-title" style="color:#1a73e8;">
Previous lesson
</div>

<div class="mini-body">
<a href="/mathematical-statistics/asymptotic-theory/asymptotic-normality-of-mle/" style="color:#1a73e8;text-decoration:underline;">
Lesson 3: Asymptotic Normality of MLE
</a>
</div>

</div>

</div>

</div>

</section>