---
layout: default
title: "3. Checking Normality: What and Why"
description: "Clarify what 'normality' refers to in statistical models, when it matters, and how to assess it responsibly."
permalink: /inference/assumptions-robustness/checking-normality-what-and-why/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 clarifies what normality means in inference,
        when it is required, and how to check it without overreacting.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/checking-normality-what-and-why/",
      label: "Lesson 3 — Checking Normality",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/assumptions-robustness/",
      label: "Block 7 — Assumptions & Robustness",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">Normality</span>
        <span class="badge">Diagnostics</span>
      </div>

      <h1>3. Checking Normality: What and Why</h1>

      <p class="lead">
        Normality assumptions are frequently misunderstood.
        It is essential to know what must be normal —
        and what does not need to be.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/assumptions-robustness/">Back to Block 7</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        In many cases, the sampling distribution matters more than the raw data distribution.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Distinguish between normality of data, residuals, and estimators,
      and evaluate when deviations meaningfully affect inference.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core clarification</h2>
      <p style="margin:0;">
        Most classical tests assume normality of errors or residuals —
        not necessarily of the raw observed data.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What must be normal?</h2>
  </div>

  <div class="card">
    For the one-sample t-test:
    <br><br>
    If n is small:
    \[
    X_i \sim \mathcal{N}(\mu, \sigma^2)
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    For linear regression:
    <br><br>
    \[
    \varepsilon_i \sim \mathcal{N}(0, \sigma^2)
    \]
  </div>

  <p>
    It is the error term (or residuals), not Y itself,
    that is assumed normal.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) When normality matters</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Small sample size</h3>
      <p>
        Distributional assumptions are more influential.
      </p>
    </div>

    <div class="card">
      <h3>Large sample size</h3>
      <p>
        Central Limit Theorem reduces sensitivity.
      </p>
    </div>

    <div class="card">
      <h3>Heavy tails</h3>
      <p>
        May inflate variance and affect Type I error.
      </p>
    </div>

    <div class="card">
      <h3>Severe skewness</h3>
      <p>
        Can distort small-sample inference.
      </p>
    </div>
  </div>

  <div class="card" style="margin-top:1rem;">
    Central Limit Theorem:
    \[
    \bar{X} \approx \mathcal{N}(\mu, \sigma^2/n)
    \quad \text{for large } n
    \]
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) How to check normality</h2>
  </div>

  <div class="card">
    Graphical methods:
    <br><br>
    • Histogram  
    • Q–Q plot  
    • Boxplot  
  </div>

  <div class="card" style="margin-top:1rem;">
    Formal tests:
    <br><br>
    • Shapiro–Wilk  
    • Kolmogorov–Smirnov  
  </div>

  <p class="muted-mini">
    With large samples, normality tests almost always reject.
    Visual inspection is often more informative.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Overchecking problem</h2>
  </div>

  <div class="card">
    Testing normality at large n:
    <br><br>
    Detects trivial deviations that have negligible impact on inference.
  </div>

  <p>
    The practical question is:
    <br>
    Does non-normality meaningfully change the result?
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical guideline</h2>
  </div>

  <div class="card">
    Recommended approach:
    <br><br>
    1. Inspect graphically  
    2. Consider sample size  
    3. Evaluate skewness/outliers  
    4. Compare with robust alternative if needed  
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand what normality refers to</li>
        <li>Know when it matters</li>
        <li>Use graphical diagnostics responsibly</li>
        <li>Avoid overreaction to minor deviations</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine independence and dependence —
        one of the most critical assumptions in inference.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/assumptions-robustness/independence-and-dependence/">
          Next lesson: 4. Independence and Dependence →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Model vs Design Assumptions
          </a>
        </div>
      </div>
    </div>
  </div>
</section>