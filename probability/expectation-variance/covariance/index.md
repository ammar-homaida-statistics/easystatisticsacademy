---
layout: default
title: "3. Covariance"
description: "Covariance measures how two random variables move together and explains why variance of sums depends on dependence structure."
permalink: /probability/expectation-variance/covariance/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the mathematical structure and interpretation of covariance.
        Numerical examples, simulations, and visual intuition will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 4 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_expectation_variance_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/expectation-variance/covariance/",
      label: "Lesson 3 — Covariance",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">Dependence</span>
        <span class="badge">Covariance</span>
      </div>

      <h1>3. Covariance</h1>
      <p class="lead">
        Variance measures spread of one variable. Covariance measures how two variables move together.
        It is the structural reason why Var(X + Y) depends on dependence.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/expectation-variance/">Back to Block 4</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Key message: covariance captures directional co-movement.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define covariance,
      interpret its sign and magnitude, and understand its role in variance of sums.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key definition</h2>
      <p style="margin:0;">
        <strong>Cov(X,Y) = E[(X − μ_X)(Y − μ_Y)]</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What covariance measures</h2>
    <p>
      Covariance measures whether deviations from the mean move in the same direction.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Positive covariance</h3>
      <ul class="bullets">
        <li>When X is above its mean, Y tends to be above its mean.</li>
        <li>When X is below its mean, Y tends to be below its mean.</li>
        <li>They move together.</li>
      </ul>
    </div>

    <div class="card">
      <h3>Negative covariance</h3>
      <ul class="bullets">
        <li>When X is above its mean, Y tends to be below its mean.</li>
        <li>They move in opposite directions.</li>
      </ul>
    </div>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Zero covariance</h3>
    <p>
      No linear co-movement.
      But zero covariance does <strong>not</strong> necessarily mean independence.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Equivalent formula</h2>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      <strong>Cov(X,Y) = E[XY] − E[X]E[Y]</strong>
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This computational form is often easier to apply.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Independence and covariance</h2>
  </div>

  <div class="card">
    <p>
      If X and Y are independent:
    </p>
    <p style="margin:0;"><strong>Cov(X,Y) = 0</strong></p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Important</h2>
      <p style="margin:0;">
        Independence implies zero covariance.
        The reverse is not always true.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Role in variance of sums</h2>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      <strong>Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)</strong>
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Interpretation</h3>
    <ul class="bullets">
      <li>If Cov > 0 → total variance increases.</li>
      <li>If Cov < 0 → total variance decreases.</li>
      <li>If independent → covariance = 0 → variances add.</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Thinking zero covariance means independence</li>
        <li>Forgetting the factor 2 in variance of sums</li>
        <li>Confusing covariance with correlation</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define covariance formally</li>
        <li>Interpret positive/negative/zero covariance</li>
        <li>Understand Var(X+Y) formula structurally</li>
        <li>Prepare for correlation (standardized covariance)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we standardize covariance to remove scale effects:
        this leads to correlation.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/expectation-variance/correlation/">
          Next lesson: 4. Correlation →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/expectation-variance/variance-rules-and-sums/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Variance Rules & Sums of Variables
          </a>
        </div>
      </div>
    </div>
  </div>
</section>