---
layout: default
title: "2. Variance Rules & Sums of Variables"
description: "Scaling, shifting, and adding random variables: variance rules, covariance, and when variances add."
permalink: /probability/expectation-variance/variance-rules-and-sums/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the correct mathematical structure of variance rules.
        Worked examples, simulations, and graphical illustrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited lesson (Block 4) -->
<script>
  (function () {
    var KEY = "esa_continue_probability_expectation_variability_lesson_v0";
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
        <span class="badge">Dependence</span>
      </div>

      <h1>2. Variance &amp; Sums of Variables</h1>

      <p class="lead">
        Expectation behaves linearly without conditions.
        Variance does not. Understanding how variance changes under scaling,
        shifting, and addition is fundamental to statistical modeling.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/expectation-variance/">Back to Block 4</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        The key idea: variance measures spread, and spread interacts with dependence.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should understand how variance behaves
      under scaling and shifting, and how to compute the variance of sums
      using covariance.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Scaling and shifting</h2>
  </div>

  <div class="card">
    <p><strong>Var(aX + b) = a² Var(X)</strong></p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>Shift (b)</h3>
      <p>
        Adding a constant does not change spread.
      </p>
    </div>

    <div class="card">
      <h3>Scaling (a)</h3>
      <p>
        Multiplying by a changes spread by a².
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Variance of a sum</h2>
  </div>

  <div class="card">
    <p><strong>Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y)</strong></p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Critical insight</h2>
      <p style="margin:0;">
        Variances add cleanly only when covariance is zero.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Independence case</h2>
  </div>

  <div class="card">
    <p>If X and Y are independent:</p>
    <p><strong>Var(X + Y) = Var(X) + Var(Y)</strong></p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Independence implies Cov(X, Y) = 0.
    But zero covariance does not necessarily imply independence.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) More than two variables</h2>
  </div>

  <div class="card">
    <p><strong>Var(ΣXᵢ) = ΣVar(Xᵢ) + 2ΣΣCov(Xᵢ, Xⱼ)</strong></p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Every pair contributes covariance.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Assuming variances always add</li>
        <li>Forgetting the covariance term</li>
        <li>Thinking zero covariance means independence</li>
        <li>Forgetting to square the scaling factor</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Apply Var(aX + b) correctly</li>
        <li>Compute Var(X + Y) with covariance</li>
        <li>Understand when variances add</li>
        <li>Prepare for formal covariance definition next</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we formally define <strong>covariance</strong> and interpret dependence structure.
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