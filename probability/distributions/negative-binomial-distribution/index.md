---
layout: default
title: "4. Negative Binomial Distribution"
description: "The negative binomial distribution models the number of trials required to achieve r successes; PMF, mean, variance, and connection to geometric."
permalink: /probability/distributions/negative-binomial-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow.
        Worked examples, simulations, and visual comparisons will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 5 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/negative-binomial-distribution/",
      label: "Lesson 4 — Negative Binomial Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">Discrete</span>
        <span class="badge">Negative Binomial</span>
      </div>

      <h1>4. Negative Binomial Distribution</h1>
      <p class="lead">
        The negative binomial distribution generalizes the geometric distribution.
        Instead of waiting for the <strong>first</strong> success,
        we wait until the <strong>r-th success</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Think: repeated independent trials until r successes occur.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define the negative binomial distribution,
      write its PMF, compute its mean and variance, and understand how it relates to geometric and binomial.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Negative binomial models waiting time for r successes.</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition</h2>
    <p>
      Consider independent Bernoulli trials with success probability \(p\).
      Let \(X\) be the number of trials required to obtain \(r\) successes.
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      X \sim \operatorname{NegBin}(r,p).
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Support: \(X = r, r+1, r+2, \ldots\)
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Probability mass function (PMF)</h2>
    <p>
      To have the r-th success on trial \(k\):
      exactly \(r-1\) successes must occur in the first \(k-1\) trials,
      and trial \(k\) must be a success.
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      \Pr(X = k)
      =
      \binom{k-1}{r-1}
      p^{\,r}
      (1-p)^{\,k-r},
      \qquad k=r,r+1,\ldots
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Why the binomial coefficient appears</h2>
      <p style="margin:0;">
        Among the first \(k-1\) trials, we choose which \(r-1\) are successes.
        The last trial is fixed as a success.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Mean and variance</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Expectation</h3>
      <p style="margin:0; font-size:1.1rem;">
        \[
        \mathbb{E}[X] = \frac{r}{p}.
        \]
      </p>
    </div>

    <div class="card">
      <h3>Variance</h3>
      <p style="margin:0; font-size:1.1rem;">
        \[
        \operatorname{Var}(X)
        =
        \frac{r(1-p)}{p^2}.
        \]
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Notice: for \(r=1\), this reduces to the geometric distribution.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Connection to geometric</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      If \(r=1\), the PMF becomes:
      \[
      \Pr(X = k) = (1-p)^{k-1}p,
      \]
      which is exactly the geometric distribution.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Geometric = special case of negative binomial.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Alternative parameterization (counting failures)</h2>
    <p>
      Some texts define the negative binomial as the number of failures before the r-th success.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      If \(Y = X - r\), then:
      \[
      \Pr(Y = y)
      =
      \binom{y+r-1}{r-1}
      p^{\,r}
      (1-p)^{\,y},
      \qquad y=0,1,2,\ldots
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Always check which definition a software package uses.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) When to use</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Repeated independent trials</li>
      <li>Constant success probability p</li>
      <li>Interest in waiting time until r successes</li>
      <li>Modeling over-dispersed count data (in applied settings)</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Recognize waiting-time-for-r-success scenarios</li>
        <li>Use the PMF formula correctly</li>
        <li>Use \(\mathbb{E}[X]=r/p\)</li>
        <li>Understand connection to geometric distribution</li>
        <li>Prepare for continuous waiting-time models</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we move to a continuous waiting-time model:
        the <strong>Exponential distribution</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/exponential-distribution/">
          Next lesson: 5. Exponential Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/geometric-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Geometric Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>