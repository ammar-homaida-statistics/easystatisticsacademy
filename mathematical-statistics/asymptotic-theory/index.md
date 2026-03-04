---
layout: default
title: "1. Modes of Convergence (Review)"
description: "Review convergence in probability, distribution, and almost sure convergence and understand how they differ."
permalink: /mathematical-statistics/asymptotic-theory/modes-of-convergence-review/
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
        Version 0 reviews the main convergence concepts used in asymptotic statistics.
        Later versions will include formal proofs and graphical illustrations.
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
      url:"/mathematical-statistics/asymptotic-theory/modes-of-convergence-review/",
      label:"Lesson 1 — Modes of Convergence",
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
        <span class="badge">Lesson 1</span>
        <span class="badge">Convergence</span>
        <span class="badge">Probability Theory</span>
      </div>

      <h1>1. Modes of Convergence</h1>

      <p class="lead">
        Asymptotic theory studies how random quantities behave as sample size grows.
        Convergence concepts formalize what it means for estimators to approach
        the true parameter.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/asymptotic-theory/">Back to Block 6</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Different convergence types capture different asymptotic behaviors.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Review the main convergence concepts used throughout asymptotic statistics
      and understand their relationships.
    </p>
  </div>
</section>

<section class="section">
<div class="section-head">
<h2>1) Convergence in probability</h2>
</div>

<div class="card">

A sequence of random variables \(X_n\) converges in probability to \(X\) if

\[
P(|X_n - X| > \varepsilon) \to 0
\quad \text{for every } \varepsilon>0.
\]

</div>

<p style="margin-top:.75rem;">
The probability of large deviations goes to zero.
</p>

<p class="muted-mini">
Consistency of estimators is defined using convergence in probability.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>2) Convergence in distribution</h2>
</div>

<div class="card">

We say

\[
X_n \xrightarrow{d} X
\]

if the cumulative distribution functions converge:

\[
F_{X_n}(x) \to F_X(x)
\]

at all continuity points of \(F_X\).

</div>

<p class="muted-mini">
Asymptotic normality is expressed using convergence in distribution.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>3) Almost sure convergence</h2>
</div>

<div class="card">

Almost sure convergence means

\[
P\left(
\lim_{n\to\infty} X_n = X
\right) = 1.
\]

</div>

<p style="margin-top:.75rem;">
This is the strongest commonly used convergence concept.
</p>

<p class="muted-mini">
The Strong Law of Large Numbers is stated using almost sure convergence.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>4) Relationship between convergence types</h2>
</div>

<div class="grid grid-2">

<div class="card">
<h3>Strongest</h3>
<p style="margin:0;">
Almost sure convergence
</p>
</div>

<div class="card">
<h3>Intermediate</h3>
<p style="margin:0;">
Convergence in probability
</p>
</div>

<div class="card">
<h3>Weakest</h3>
<p style="margin:0;">
Convergence in distribution
</p>
</div>

<div class="card">
<h3>Implication chain</h3>

\[
X_n \xrightarrow{a.s.} X
\Rightarrow
X_n \xrightarrow{p} X
\Rightarrow
X_n \xrightarrow{d} X
\]

</div>

</div>

<p class="muted-mini">
The reverse implications do not generally hold.
</p>

</section>

<section class="section">
<div class="section-head">
<h2>5) Why convergence matters in statistics</h2>
</div>

<div class="grid grid-2">

<div class="card">
<h3>Consistency</h3>
<p style="margin:0;">
Estimator converges to the true parameter.
</p>
</div>

<div class="card">
<h3>Asymptotic normality</h3>
<p style="margin:0;">
Distribution of estimator approaches a normal distribution.
</p>
</div>

<div class="card">
<h3>Large-sample inference</h3>
<p style="margin:0;">
Confidence intervals and tests rely on asymptotic approximations.
</p>
</div>

<div class="card">
<h3>Approximation tools</h3>
<p style="margin:0;">
Slutsky and delta method rely on convergence concepts.
</p>
</div>

</div>

</section>

<section class="section section-slim">
<div class="callout">
<div class="callout-copy">

<h2>Outcome of this lesson</h2>

<ul class="bullets">
<li>Define convergence in probability</li>
<li>Define convergence in distribution</li>
<li>Define almost sure convergence</li>
<li>Understand their relationships</li>
</ul>

</div>
</div>
</section>

<!-- Next + Previous navigation -->

<section class="section section-slim">

<div class="callout">

<div class="callout-copy">

<h2>Next lesson</h2>

<p style="margin:0;">
We now apply convergence concepts to estimation and explain
why the maximum likelihood estimator is consistent.
</p>

<div class="pill-row" style="margin-top:1rem;">
<a class="btn" href="/mathematical-statistics/asymptotic-theory/consistency-of-mle-idea/">
Continue to Lesson 2 →
</a>
</div>

</div>

<div class="callout-side">

<div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">

<div class="mini-title" style="color:#1a73e8;">
Previous block
</div>

<div class="mini-body">
<a href="/mathematical-statistics/fisher-information-and-efficiency/" style="color:#1a73e8;text-decoration:underline;">
Block 5 — Fisher Information & Efficiency
</a>
</div>

</div>

</div>

</div>

</section>