---
layout: default
title: "5. Expectation (Mean of a Random Variable)"
description: "Expectation as the long-run average and weighted average of a distribution for discrete and continuous random variables."
permalink: /probability/random-variables/expectation/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the conceptual structure.
        Numerical examples, simulations, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 3 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_random_variables_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/random-variables/expectation/",
      label: "Lesson 5 — Expectation",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">Mean</span>
        <span class="badge">Long-run average</span>
      </div>

      <h1>5. Expectation (Mean of a Random Variable)</h1>

      <p class="lead">
        Expectation is the central numerical summary of a random variable.
        It represents the long-run average outcome and the weighted average of possible values.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/random-variables/">Back to Block 3</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Expectation is not just “average.” It is probability-weighted structure.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define expectation for discrete and continuous random variables,
      interpret it correctly, and understand its linearity property.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Expectation is a probability-weighted average of all possible values.</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Expectation — discrete case</h2>
  </div>

  <div class="card">
    <p>
      If X is a discrete random variable with PMF p(x):
    </p>
    <p style="margin:0;"><strong>E[X] = Σ x · p(x)</strong></p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Interpretation</h3>
    <ul class="bullets">
      <li>Multiply each possible value by its probability.</li>
      <li>Sum across all possible values.</li>
      <li>The result is the long-run average outcome.</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Expectation — continuous case</h2>
  </div>

  <div class="card">
    <p>
      If X has PDF f(x):
    </p>
    <p style="margin:0;"><strong>E[X] = ∫ x f(x) dx</strong></p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Interpretation</h3>
    <p>
      The expectation is the “center of mass” of the probability density.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Important properties</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Linearity</h3>
      <p style="margin:0;">
        E[aX + b] = aE[X] + b
      </p>
    </div>

    <div class="card">
      <h3>Sum rule</h3>
      <p style="margin:0;">
        E[X + Y] = E[X] + E[Y]
      </p>
      <p class="muted-mini">
        This holds even if X and Y are not independent.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) What expectation is NOT</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>It does not have to be a possible observed value.</li>
      <li>It does not describe variability.</li>
      <li>It does not guarantee future outcomes.</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Compute expectation for discrete and continuous variables</li>
        <li>Interpret expectation as weighted average</li>
        <li>Use linearity correctly</li>
        <li>Prepare for variance next</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we measure variability using variance and standard deviation.
      </p>

      <!-- ✅ MATCHES YOUR FOLDER -->
      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/random-variables/variance-and-standard-deviation/">
          Next lesson: 6. Variance & Standard Deviation →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/random-variables/cumulative-distribution-function/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Cumulative Distribution Function
          </a>
        </div>
      </div>
    </div>
  </div>
</section>