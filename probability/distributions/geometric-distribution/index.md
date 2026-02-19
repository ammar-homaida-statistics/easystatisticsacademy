---
layout: default
title: "3. Geometric Distribution"
description: "The geometric distribution models the number of trials required until the first success; PMF, memoryless property, mean, and variance."
permalink: /probability/distributions/geometric-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow.
        Numerical examples, graphs, and software demonstrations will be added later without changing the lesson order.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 5 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/geometric-distribution/",
      label: "Lesson 3 — Geometric Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">Discrete</span>
        <span class="badge">Geometric</span>
      </div>

      <h1>3. Geometric Distribution</h1>
      <p class="lead">
        The geometric distribution answers a different question from binomial:
        instead of “How many successes in n trials?” we ask
        <strong>“How many trials until the first success?”</strong>
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Think: repeated independent trials until success occurs.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define the geometric distribution,
      write its PMF, understand the memoryless property, and compute its mean and variance.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Geometric models waiting time.</strong>
        It counts how many independent Bernoulli trials are needed until the first success.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition</h2>
    <p>
      Suppose independent Bernoulli trials are performed with success probability \(p\).
      Let \(X\) be the number of trials required until the first success.
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      X \sim \operatorname{Geometric}(p).
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Here we use the common convention:
    \(X = 1,2,3,\ldots\) (counts trials, not failures).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Probability mass function (PMF)</h2>
    <p>
      To observe the first success on trial \(k\):
      the first \(k-1\) trials must be failures, and the \(k\)-th trial must be success.
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      \Pr(X = k) = (1-p)^{k-1} p, \qquad k = 1,2,3,\ldots
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Why this formula makes sense</h2>
      <p style="margin:0;">
        \((1-p)^{k-1}\): probability that the first \(k-1\) trials are failures.  
        \(p\): probability that the \(k\)-th trial is success.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) CDF and tail probability</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Tail probability</h3>
      <p style="margin:0;">
        \[
        \Pr(X > k) = (1-p)^k.
        \]
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Probability that first success occurs after trial k.
      </p>
    </div>

    <div class="card">
      <h3>CDF</h3>
      <p style="margin:0;">
        \[
        \Pr(X \le k) = 1 - (1-p)^k.
        \]
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Mean and variance</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Expectation</h3>
      <p style="margin:0; font-size:1.1rem;">
        \[
        \mathbb{E}[X] = \frac{1}{p}.
        \]
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        If success is rare (small p), expected waiting time is large.
      </p>
    </div>

    <div class="card">
      <h3>Variance</h3>
      <p style="margin:0; font-size:1.1rem;">
        \[
        \operatorname{Var}(X) = \frac{1-p}{p^2}.
        \]
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Memoryless property (very important)</h2>
    <p>
      The geometric distribution is the only discrete distribution with the memoryless property.
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.05rem;">
      \[
      \Pr(X > s+t \mid X > s) = \Pr(X > t).
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        If you have already waited \(s\) trials without success,
        the additional waiting time distribution is unchanged.
        The process “forgets” the past.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) When NOT to use geometric</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Trials are not independent</li>
      <li>Success probability changes over time</li>
      <li>You are counting number of successes in fixed trials (use Binomial instead)</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Recognize waiting-time scenarios</li>
        <li>Use PMF \(\Pr(X=k)=(1-p)^{k-1}p\)</li>
        <li>Use \(\mathbb{E}[X]=1/p\) and \(\operatorname{Var}(X)=(1-p)/p^2\)</li>
        <li>Understand the memoryless property</li>
        <li>Prepare for Negative Binomial distribution</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        What if we wait until the <strong>r-th success</strong> instead of the first?
        That leads to the <strong>Negative Binomial distribution</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/negative-binomial-distribution/">
          Next lesson: 4. Negative Binomial Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/binomial-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Binomial Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>