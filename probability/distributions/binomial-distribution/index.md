---
layout: default
title: "2. Binomial Distribution"
description: "Binomial(n,p) models the number of successes in n independent Bernoulli trials; PMF, mean/variance, and core interpretations."
permalink: /probability/distributions/binomial-distribution/
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
      url: "/probability/distributions/binomial-distribution/",
      label: "Lesson 2 — Binomial Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Discrete</span>
        <span class="badge">Binomial</span>
      </div>

      <h1>2. Binomial Distribution</h1>
      <p class="lead">
        The binomial distribution models the number of successes in a fixed number of independent trials.
        It is the natural extension of the Bernoulli distribution from <strong>one</strong> trial to <strong>n</strong> trials.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Think: repeated yes/no trials → count the successes.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to recognize binomial settings, define
      <strong>Binomial(n,p)</strong>, write its PMF, and use its mean and variance correctly.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Binomial counts successes.</strong> It applies only when you have a fixed number of trials,
        identical success probability, and independence between trials.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) When do we use a binomial model?</h2>
    <p>
      A random variable <strong>X</strong> is binomial if it counts successes in repeated trials under these conditions:
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li><strong>Fixed number of trials:</strong> n is known and constant</li>
      <li><strong>Two outcomes per trial:</strong> success/failure (coded 1/0)</li>
      <li><strong>Constant success probability:</strong> P(success) = p in each trial</li>
      <li><strong>Independence:</strong> outcomes of trials do not affect each other</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    If any of these fail (especially independence or constant p), the binomial model may be inappropriate.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Definition</h2>
    <p>
      Let <strong>X</strong> be the number of successes in <strong>n</strong> independent Bernoulli trials with success probability <strong>p</strong>.
      Then:
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      X \sim \operatorname{Binomial}(n,p).
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Connection to Bernoulli</h2>
      <p style="margin:0;">
        If \(X_i \sim \operatorname{Bernoulli}(p)\) and trials are independent, then
        \[
        X=\sum_{i=1}^{n} X_i \sim \operatorname{Binomial}(n,p).
        \]
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) PMF (probability mass function)</h2>
    <p>
      The probability of observing exactly <strong>k</strong> successes is:
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      \Pr(X=k)=\binom{n}{k}p^{k}(1-p)^{\,n-k}, \qquad k=0,1,2,\ldots,n.
      \]
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>What each term means</h3>
      <ul class="bullets">
        <li>\(\binom{n}{k}\): number of ways to choose which k trials are successes</li>
        <li>\(p^{k}\): probability of k successes (for a fixed pattern)</li>
        <li>\((1-p)^{n-k}\): probability of n−k failures (for the same pattern)</li>
      </ul>
    </div>

    <div class="card">
      <h3>Binomial coefficient</h3>
      <p style="margin:0;">
        \[
        \binom{n}{k}=\frac{n!}{k!(n-k)!}.
        \]
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Counts combinations (order does not matter).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Mean and variance</h2>
    <p>
      For \(X \sim \operatorname{Binomial}(n,p)\):
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Expectation</h3>
      <p style="margin:0; font-size:1.1rem;">
        \[
        \mathbb{E}[X]=np.
        \]
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Expected number of successes = trials × success probability.
      </p>
    </div>

    <div class="card">
      <h3>Variance</h3>
      <p style="margin:0; font-size:1.1rem;">
        \[
        \operatorname{Var}(X)=np(1-p).
        \]
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Variability grows with n and is largest near \(p=0.5\).
      </p>
    </div>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Why these formulas make sense</h2>
      <p style="margin:0;">
        Since \(X=\sum_{i=1}^{n}X_i\) with \(X_i\sim\operatorname{Bernoulli}(p)\), linearity gives
        \(\mathbb{E}[X]=\sum \mathbb{E}[X_i]=np\), and (with independence) variances add to give \(np(1-p)\).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Interpretation and quick checks</h2>
    <p>
      Before using a binomial model, verify the story matches the assumptions.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Good binomial examples</h3>
      <ul class="bullets">
        <li>Number of heads in n coin tosses (fair coin: \(p=0.5\))</li>
        <li>Number of defective items in n independent inspections</li>
        <li>Number of patients responding to treatment in n trials (if assumptions hold)</li>
      </ul>
    </div>

    <div class="card">
      <h3>Not binomial (common)</h3>
      <ul class="bullets">
        <li>Sampling <strong>without replacement</strong> from a finite population (often hypergeometric)</li>
        <li>Changing probability over time (non-constant p)</li>
        <li>Dependence between trials (clustered outcomes)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Using binomial when trials are not independent</li>
        <li>Forgetting k must be between 0 and n</li>
        <li>Confusing “exactly k” with “at least k” (requires summation)</li>
        <li>Using binomial for sampling without replacement (often hypergeometric)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Recognize when Binomial(n,p) is appropriate</li>
        <li>Use the PMF \(\Pr(X=k)=\binom{n}{k}p^k(1-p)^{n-k}\)</li>
        <li>Use \(\mathbb{E}[X]=np\) and \(\operatorname{Var}(X)=np(1-p)\)</li>
        <li>Prepare for Geometric distribution (waiting time until first success)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we change the question:
        instead of “How many successes in n trials?”, we ask
        “How many trials until the first success?” — the <strong>Geometric distribution</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/geometric-distribution/">
          Next lesson: 3. Geometric Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/bernoulli-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: Bernoulli Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>