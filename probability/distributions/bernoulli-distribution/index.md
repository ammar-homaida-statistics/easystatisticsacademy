---
layout: default
title: "1. Bernoulli Distribution"
description: "Bernoulli(p) models a single trial with success/failure outcomes and is the building block for many discrete distributions."
permalink: /probability/distributions/bernoulli-distribution/
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
      url: "/probability/distributions/bernoulli-distribution/",
      label: "Lesson 1 — Bernoulli Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Discrete</span>
        <span class="badge">Bernoulli</span>
      </div>

      <h1>1. Bernoulli Distribution</h1>
      <p class="lead">
        The Bernoulli distribution models the simplest random experiment:
        a single trial with only two outcomes — <strong>success</strong> or <strong>failure</strong>.
        It is the basic building block behind the Binomial, Geometric, and many other models.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        If you understand Bernoulli well, most discrete distributions become easier.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define a Bernoulli random variable,
      write its PMF, interpret the parameter <strong>p</strong>, and compute its expectation and variance.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        A Bernoulli variable takes only two values:
        <strong>1</strong> (success) with probability <strong>p</strong>, and
        <strong>0</strong> (failure) with probability <strong>1 − p</strong>.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition</h2>
    <p>
      A random variable <strong>X</strong> follows a Bernoulli distribution with parameter <strong>p</strong>
      if it takes values:
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.05rem;">
      <strong>X ∈ {0, 1}</strong>, with
      <strong>P(X = 1) = p</strong> and <strong>P(X = 0) = 1 − p</strong>.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The parameter <strong>p</strong> must satisfy <strong>0 ≤ p ≤ 1</strong>.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) PMF (probability mass function)</h2>
    <p>
      The PMF of a Bernoulli random variable is:
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      <strong>
        P(X = x) = p^x (1-p)^{1-x}, &nbsp; x ∈ {0,1}
      </strong>
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        This single formula covers both cases:
        if x=1 you get p, and if x=0 you get (1-p).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Real-life examples</h2>
    <p>
      Bernoulli models a single yes/no outcome:
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Typical examples</h3>
      <ul class="bullets">
        <li>Patient has a condition (1) or not (0)</li>
        <li>Email is spam (1) or not (0)</li>
        <li>Coin toss is heads (1) or tails (0)</li>
        <li>Product passes QC (1) or fails (0)</li>
      </ul>
    </div>

    <div class="card">
      <h3>Modeling note</h3>
      <p style="margin:0;">
        “Success” does not mean “good”. It simply means the event you label as 1.
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Example: in medicine, “success” may be “disease present”.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Expectation and variance</h2>
    <p>
      For X ~ Bernoulli(p):
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Mean</h3>
      <p style="margin:0;">
        <strong>E[X] = p</strong>
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        The mean equals the success probability.
      </p>
    </div>

    <div class="card">
      <h3>Variance</h3>
      <p style="margin:0;">
        <strong>Var(X) = p(1 − p)</strong>
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Maximum at p=0.5, small near 0 or 1.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Using values {−1,1} but still calling it Bernoulli(you must define coding clearly)</li>
        <li>Mixing up p with 1−p (define what “success=1” means)</li>
        <li>Forgetting that Bernoulli is a single trial (Binomial is n trials)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define Bernoulli(p) and interpret p</li>
        <li>Write the PMF in both table form and compact form</li>
        <li>Use E[X]=p and Var(X)=p(1−p)</li>
        <li>Prepare for Binomial as “sum of Bernoulli trials”</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we move from a single Bernoulli trial to <strong>n</strong> independent trials:
        the <strong>Binomial distribution</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/binomial-distribution/">
          Next lesson: 2. Binomial Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous</div>
        <div class="mini-body">
          <a href="/probability/expectation-variance/" style="color:#1a73e8; text-decoration:underline;">
            Block 4 — Expectation &amp; Variability
          </a>
        </div>
      </div>
    </div>
  </div>
</section>