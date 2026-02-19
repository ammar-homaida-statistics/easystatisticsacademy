---
layout: default
title: "2. Binomial Distribution"
description: "Binomial(n,p) models the number of successes in n independent Bernoulli trials and connects directly to counting and proportions."
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
        The Binomial distribution counts how many successes occur in
        <strong>n independent Bernoulli trials</strong>, each with success probability <strong>p</strong>.
        It is the standard model for repeated yes/no experiments.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Key message: Binomial = sum of n Bernoulli(p) trials.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define Binomial(n,p),
      state its assumptions, write the PMF, and use its mean and variance.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>X ~ Binomial(n,p)</strong> counts the number of successes in n trials.
        Each trial is Bernoulli(p), and trials are independent.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition and assumptions</h2>
    <p>
      A random variable X follows a Binomial distribution if:
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>There are a fixed number of trials: <strong>n</strong>.</li>
      <li>Each trial has two outcomes (success/failure).</li>
      <li>Success probability is constant: <strong>P(success)=p</strong>.</li>
      <li>Trials are <strong>independent</strong>.</li>
      <li>X counts successes: <strong>X ∈ {0,1,2,...,n}</strong>.</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    If independence or constant p fails, Binomial may not be appropriate (see Hypergeometric later).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) PMF (probability mass function)</h2>
    <p>
      For X ~ Binomial(n,p), the probability of exactly k successes is:
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      <strong>P(X = k) = C(n,k) p^k (1-p)^{n-k}, &nbsp; k=0,1,...,n</strong>
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>What each piece means</h3>
    <ul class="bullets">
      <li><strong>C(n,k)</strong> counts how many ways to place k successes among n trials.</li>
      <li><strong>p^k</strong> is the probability of those k successes.</li>
      <li><strong>(1-p)^{n-k}</strong> is the probability of the remaining failures.</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Connection to Bernoulli</h2>
    <p>
      If X₁,...,Xₙ are independent Bernoulli(p), then:
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      <strong>X = X₁ + X₂ + ... + Xₙ  ~  Binomial(n,p)</strong>
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Modeling translation</h2>
      <p style="margin:0;">
        “Number of successes” is literally a sum of 0/1 indicators.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Mean and variance</h2>
    <p>
      For X ~ Binomial(n,p):
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Mean</h3>
      <p style="margin:0;"><strong>E[X] = np</strong></p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Expected successes = trials × success probability.
      </p>
    </div>

    <div class="card">
      <h3>Variance</h3>
      <p style="margin:0;"><strong>Var(X) = np(1-p)</strong></p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Variability grows with n and is largest near p=0.5.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) When to use Binomial (and when not)</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Use Binomial when</h3>
      <ul class="bullets">
        <li>Fixed n</li>
        <li>Independent trials</li>
        <li>Same p each trial</li>
        <li>Counting successes</li>
      </ul>
    </div>

    <div class="card">
      <h3>Do NOT use Binomial when</h3>
      <ul class="bullets">
        <li>Sampling without replacement from a finite population (Hypergeometric)</li>
        <li>p changes across trials (needs a different model)</li>
        <li>Trials are dependent (variance changes)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Forgetting independence (especially in sampling without replacement)</li>
        <li>Using Binomial when n is not fixed</li>
        <li>Mixing up “exactly k” with “at least k” (needs summation)</li>
        <li>Confusing Binomial with Geometric (which counts trials until first success)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>State Binomial(n,p) assumptions clearly</li>
        <li>Use P(X=k)=C(n,k)p^k(1-p)^{n-k}</li>
        <li>Use E[X]=np and Var(X)=np(1-p)</li>
        <li>Be ready for Geometric as “waiting time” to success</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we move from “counting successes in n trials” to “waiting for the first success”:
        the <strong>Geometric distribution</strong>.
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