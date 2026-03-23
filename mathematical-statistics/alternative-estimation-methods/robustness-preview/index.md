---
layout: default
title: "5. Robustness (Preview)"
description: "Understand how estimation behaves under model misspecification and why robustness matters."
permalink: /mathematical-statistics/alternative-estimation-methods/robustness-preview/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#eef5ff; border:2px solid #3f51b5; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#283593; line-height:1.6;">
        Version 0 introduces robustness as a key concept when model assumptions fail.
        Later versions will include robust estimators, influence functions, and breakdown points.
      </p>
    </div>
  </div>
</section>

<!-- Continue-reading tracking -->
<script>
  (function () {

    localStorage.setItem(
      "esa_continue_ms_methods_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/alternative-estimation-methods/robustness-preview/",
        label: "Lesson 5 — Robustness",
        ts: Date.now()
      })
    );

    localStorage.setItem(
      "esa_continue_ms_last_block_v0",
      JSON.stringify({
        url: "/mathematical-statistics/alternative-estimation-methods/",
        label: "Block 7 — Alternative Estimation Methods",
        ts: Date.now()
      })
    );

  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">Robustness</span>
        <span class="badge">Assumptions</span>
      </div>

      <h1>5. Robustness (Preview)</h1>

      <p class="lead">
        Real data rarely satisfy ideal assumptions.
        Robustness studies how estimation behaves when models are wrong.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/alternative-estimation-methods/">Back to Block 7</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Good estimators should not break under small violations.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand what robustness means, why assumptions fail in practice,
      and how estimators can remain reliable under deviations.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Model assumptions vs reality</h2>
  </div>

  <div class="card">
    Statistical models assume:
    <ul class="bullets">
      <li>Correct distribution form</li>
      <li>Independence</li>
      <li>No outliers</li>
    </ul>
  </div>

  <p style="margin-top:.75rem;">
    In practice, these assumptions are often violated.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Sensitivity to violations</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Non-robust estimators</h3>
      <p style="margin:0;">
        Strongly affected by outliers or misspecification.
      </p>
    </div>

    <div class="card">
      <h3>Robust estimators</h3>
      <p style="margin:0;">
        Remain stable under small deviations.
      </p>
    </div>

    <div class="card">
      <h3>Example</h3>
      <p style="margin:0;">
        Mean vs median under extreme values.
      </p>
    </div>

    <div class="card">
      <h3>Goal</h3>
      <p style="margin:0;">
        Balance efficiency and stability.
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Key robustness concepts</h2>
  </div>

  <div class="card">
    Important ideas include:
    <ul class="bullets">
      <li>Influence of individual observations</li>
      <li>Breakdown point</li>
      <li>Resistance to outliers</li>
    </ul>
  </div>

  <p class="muted-mini">
    These measure how sensitive an estimator is.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Tradeoff with efficiency</h2>
  </div>

  <div class="card">
    Highly robust estimators may be less efficient
    when assumptions are perfectly satisfied.
  </div>

  <p>
    Choosing an estimator depends on the data context.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why robustness matters</h2>
  </div>

  <div class="card">
    Robust methods are important in:

    <ul class="bullets">
      <li>Real-world data analysis</li>
      <li>Outlier-prone datasets</li>
      <li>Model uncertainty</li>
    </ul>
  </div>

  <p class="muted-mini">
    Practical statistics requires robustness.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand robustness conceptually</li>
        <li>Recognize assumption violations</li>
        <li>Compare robust vs non-robust estimators</li>
        <li>Prepare for applied statistical practice</li>
      </ul>
    </div>
  </div>
</section>

<!-- ✅ Final navigation -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        You have completed the Mathematical Statistics unit.
        Now return to the main section or proceed to Statistical Inference.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/">
          Back to Mathematical Statistics →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/alternative-estimation-methods/shrinkage-intuition-preview/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Shrinkage Intuition
          </a>
        </div>
      </div>
    </div>

  </div>
</section>