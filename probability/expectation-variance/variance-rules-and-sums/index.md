---
layout: default
title: "2. Variance Rules & Sums of Variables"
description: "How variance behaves under scaling and shifting, and how to compute Var(X+Y) using covariance. The key contrast: variance is not linear."
permalink: /probability/expectation-variance/variance-rules-and-sums/
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

<!-- ✅ Update "last visited lesson" for Probability Block 4 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_expectation_variance_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/expectation-variance/variance-rules-and-sums/",
      label: "Lesson 2 — Variance Rules & Sums of Variables",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Variance</span>
        <span class="badge">Sums</span>
      </div>

      <h1>2. Variance Rules &amp; Sums of Variables</h1>
      <p class="lead">
        Expectation is linear. Variance is not.
        This lesson gives the core variance transformation rules and shows exactly what happens when you take
        the variance of a sum. The extra term you must respect is <strong>covariance</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/expectation-variance/">Back to Block 4</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Key message: <strong>Var(X+Y)</strong> depends on whether X and Y move together.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to apply the variance transformation rules,
      compute variance for sums using covariance, and recognize when you can (and cannot) add variances.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Variance measures spread around the mean.</strong>
        When you combine random variables, spread depends on both their individual spreads and their
        <strong>dependence</strong>.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Reminder: definition of variance</h2>
    <p>
      Variance is defined as the expected squared deviation from the mean.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>Var(X) = E[(X − E[X])²]</strong>
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Computational form</h3>
    <p style="margin:0;">
      <strong>Var(X) = E[X²] − (E[X])²</strong>
    </p>
    <p class="muted-mini" style="margin-top:.5rem;">
      This form is often easier for algebra.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Transformation rules: shifting and scaling</h2>
    <p>
      These are the two most-used variance rules.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Rule A — Shifts do not change variance</h3>
      <p style="margin:0;">
        For any constant b:
        <strong>Var(X + b) = Var(X)</strong>
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Adding a constant moves the distribution but does not change spread.
      </p>
    </div>

    <div class="card">
      <h3>Rule B — Scaling multiplies variance by a²</h3>
      <p style="margin:0;">
        For any constant a:
        <strong>Var(aX) = a² Var(X)</strong>
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        Scaling stretches or compresses spread; variance uses squared units.
      </p>
    </div>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Combined rule</h3>
    <p style="margin:0;">
      <strong>Var(aX + b) = a² Var(X)</strong>
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Variance of a sum: where covariance appears</h2>
    <p>
      This is the central formula of the lesson.
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      <strong>Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)</strong>
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>What the covariance term means</h3>
      <p style="margin:0;">
        Cov(X,Y) measures how X and Y move together.
        If they tend to increase together, covariance is positive and the sum is more variable.
        If one increases when the other decreases, covariance is negative and the sum is less variable.
      </p>
    </div>

    <div class="card">
      <h3>Why this matters</h3>
      <p style="margin:0;">
        This is exactly why variance is not “linear.”
        You cannot generally say Var(X+Y)=Var(X)+Var(Y) unless you know something about dependence.
      </p>
    </div>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Special case</h2>
      <p style="margin:0;">
        If X and Y are <strong>independent</strong>, then <strong>Cov(X,Y)=0</strong> and:
        <strong>Var(X+Y)=Var(X)+Var(Y)</strong>.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Variance of a difference</h2>
    <p>
      Subtraction changes the sign of the covariance term.
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      <strong>Var(X − Y) = Var(X) + Var(Y) − 2Cov(X, Y)</strong>
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    If X and Y are independent, Var(X−Y)=Var(X)+Var(Y).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) General form (many variables)</h2>
    <p>
      For a sum of many variables, variance includes all pairwise covariance terms.
    </p>
  </div>

  <div class="card">
  <p style="margin:0;">
    $$ 
    \mathrm{Var}\!\left(\sum_{i=1}^{n} X_i\right)
    =
    \sum_{i=1}^{n} \mathrm{Var}(X_i)
    +
    2\sum_{i<j} \mathrm{Cov}(X_i, X_j)
    $$
  </p>
</div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key consequence</h2>
      <p style="margin:0;">
        If all Xᵢ are independent, all covariance terms are zero, and variance becomes the sum of variances.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Problem-solving pattern</h2>
    <p>
      When you see variance in a problem:
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Simplify using shifts and scaling: Var(aX+b)=a²Var(X).</li>
      <li>If you have a sum/difference, write the covariance formula.</li>
      <li>Decide whether covariance is known, zero (independence), or must be computed.</li>
      <li>Only then compute the final value.</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Assuming Var(X+Y)=Var(X)+Var(Y) without independence (or covariance = 0)</li>
        <li>Forgetting the factor 2 in 2Cov(X,Y)</li>
        <li>Thinking Var(X+b) changes variance (it does not)</li>
        <li>Using Var(aX)=aVar(X) instead of a²Var(X)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Use Var(aX+b)=a²Var(X) correctly</li>
        <li>Compute Var(X+Y) with the covariance term</li>
        <li>Know exactly when variances add (independence / zero covariance)</li>
        <li>Be ready to define and interpret covariance next</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we define <strong>covariance</strong> carefully and interpret it as the key measure of joint movement
        that controls variability of sums.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/expectation-variance/covariance/">
          Next lesson: 3. Covariance →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/expectation-variance/linearity-of-expectation/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: Linearity of Expectation
          </a>
        </div>
      </div>
    </div>
  </div>
</section>