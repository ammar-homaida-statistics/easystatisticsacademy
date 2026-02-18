---
layout: default
title: "3. Continuous Random Variables & PDF"
description: "Continuous random variables, probability density functions (PDF), and computing probabilities using area (integration)."
permalink: /probability/random-variables/continuous-random-variables/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow. Numerical examples,
        graphs, and software demonstrations will be added later without changing the lesson order.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 3 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_random_variables_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/random-variables/continuous-random-variables/",
      label: "Lesson 3 — Continuous Random Variables & PDF",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">Continuous</span>
        <span class="badge">PDF</span>
      </div>

      <h1>3. Continuous Random Variables &amp; PDF</h1>
      <p class="lead">
        A continuous random variable takes values in an interval of real numbers.
        Its distribution is described by a <strong>probability density function (PDF)</strong>,
        and probabilities are computed as areas under curves.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/random-variables/">Back to Block 3</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        In the continuous world, probabilities come from area — not from summing masses.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define a continuous random variable,
      interpret a probability density function (PDF), and compute probabilities using integration.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>For continuous random variables, probabilities are areas under a density curve.</strong>
        Individual points have probability zero.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What “continuous” means</h2>
    <p>
      A random variable X is continuous if it can take values in an interval
      (for example, all real numbers between 0 and 10).
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Typical continuous examples</h3>
      <ul class="bullets">
        <li>Height of a person</li>
        <li>Waiting time</li>
        <li>Measurement error</li>
        <li>Temperature</li>
      </ul>
      <p class="muted-mini">
        These are measured quantities rather than counts.
      </p>
    </div>

    <div class="card">
      <h3>Key contrast with discrete case</h3>
      <p>
        Discrete: probabilities assigned to specific values.  
        Continuous: probabilities assigned to intervals.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Probability Density Function (PDF)</h2>
    <p>
      The distribution of a continuous random variable is described by a function f(x),
      called the probability density function.
    </p>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      <strong>f(x) ≥ 0</strong>
    </p>
    <p style="margin-top:.5rem;">
      <strong>∫ f(x) dx over entire support = 1</strong>
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Important clarification</h2>
      <p style="margin:0;">
        f(x) is not a probability. It is a density.  
        Probability comes from integrating (area under the curve).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Computing probabilities</h2>
    <p>
      For continuous X:
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx</strong>
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Probability at a point</h3>
    <p style="margin:0;">
      <strong>P(X = a) = 0</strong>
    </p>
    <p class="muted-mini" style="margin-top:.5rem;">
      A single point has zero width → zero area → zero probability.
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Implication</h3>
    <ul class="bullets">
      <li>P(X ≤ a) = P(X &lt; a)</li>
      <li>P(X ≥ a) = P(X &gt; a)</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Support and shape</h2>
    <p>
      The support of a continuous variable is the interval where f(x) &gt; 0.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Finite support</h3>
      <p>
        Example: X between 0 and 1 only.
      </p>
    </div>

    <div class="card">
      <h3>Infinite support</h3>
      <p>
        Example: X over all real numbers (e.g., normal distribution).
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Shape determines where most probability mass lies (peaks, spread, skewness).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Common traps</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Trap A: Thinking f(x) is probability</h3>
      <p>
        The height of the curve is not the probability.
        Only area corresponds to probability.
      </p>
    </div>

    <div class="card">
      <h3>Trap B: Assigning positive probability to a single value</h3>
      <p>
        In continuous models, this is incorrect.
      </p>
    </div>

    <div class="card">
      <h3>Trap C: Forgetting total area must equal 1</h3>
      <p>
        Always verify ∫ f(x) dx = 1.
      </p>
    </div>

    <div class="card">
      <h3>Trap D: Mixing discrete and continuous logic</h3>
      <p>
        Summation applies to discrete; integration applies to continuous.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define a continuous random variable</li>
        <li>Interpret a probability density function correctly</li>
        <li>Compute probabilities via integration</li>
        <li>Understand why point probabilities are zero</li>
        <li>Be ready to unify both cases using the CDF</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we define the <strong>Cumulative Distribution Function (CDF)</strong>,
        which works for both discrete and continuous variables.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/random-variables/cumulative-distribution-function/">
          Next lesson: 4. Cumulative Distribution Function →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/random-variables/discrete-random-variables/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Discrete Random Variables & PMF
          </a>
        </div>
      </div>
    </div>
  </div>
</section>