---
layout: default
title: "5. Exponential Distribution"
description: "The exponential distribution models continuous waiting time until the first event in a Poisson process; PDF, CDF, mean, variance, and memoryless property."
permalink: /probability/distributions/exponential-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 focuses on structure and mathematical clarity.
        Graphs, simulations, and applied case studies will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 5 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/exponential-distribution/",
      label: "Lesson 5 — Exponential Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">Continuous</span>
        <span class="badge">Waiting Time</span>
      </div>

      <h1>5. Exponential Distribution</h1>
      <p class="lead">
        The exponential distribution models the <strong>continuous waiting time</strong>
        until the first event occurs in a process with constant rate.
        It is the continuous analogue of the geometric distribution.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Think: time until next arrival, failure, or event.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define the exponential distribution,
      write its PDF and CDF, compute probabilities, and understand the memoryless property.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Exponential distribution models waiting time with constant hazard rate.</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition</h2>
    <p>
      Let \(X\) represent waiting time until the first event in a process
      with constant rate \(\lambda &gt; 0\).
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      X \sim \operatorname{Exp}(\lambda).
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Support: \(X \ge 0\).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Probability density function (PDF)</h2>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      f(x) =
      \begin{cases}
      \lambda e^{-\lambda x}, & x \ge 0 \\
      0, & x &lt; 0
      \end{cases}
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The density decreases exponentially as x increases.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Cumulative distribution function (CDF)</h2>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      F(x) = \Pr(X \le x)
      =
      1 - e^{-\lambda x},
      \quad x \ge 0.
      \]
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Survival function</h3>
    <p style="margin:0;">
      \[
      \Pr(X &gt; x) = e^{-\lambda x}.
      \]
    </p>
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
        \mathbb{E}[X] = \frac{1}{\lambda}.
        \]
      </p>
    </div>

    <div class="card">
      <h3>Variance</h3>
      <p style="margin:0; font-size:1.1rem;">
        \[
        \operatorname{Var}(X) = \frac{1}{\lambda^2}.
        \]
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Larger λ → shorter expected waiting time.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Memoryless property</h2>
    <p>
      The exponential distribution is the only continuous distribution
      with the memoryless property.
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      \Pr(X &gt; s + t \mid X &gt; s)
      =
      \Pr(X &gt; t).
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Interpretation: the process “forgets” how long it has already waited.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Relationship to Poisson process</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>If events occur according to a Poisson process with rate λ,</li>
      <li>then the waiting time between events follows Exp(λ).</li>
      <li>Counts → Poisson; Waiting times → Exponential.</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Write PDF and CDF correctly</li>
        <li>Use mean and variance formulas</li>
        <li>Understand memoryless property</li>
        <li>Connect exponential to Poisson process</li>
        <li>Prepare for Gamma distribution</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we generalize exponential waiting time to multiple events:
        the <strong>Gamma distribution</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/gamma-distribution/">
          Next lesson: 6. Gamma Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/negative-binomial-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Negative Binomial Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>