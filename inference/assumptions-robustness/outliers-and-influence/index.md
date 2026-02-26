---
layout: default
title: "6. Outliers and Influence"
description: "Understand what outliers are, how influential observations affect estimates, and how to diagnose and handle them responsibly."
permalink: /inference/assumptions-robustness/outliers-and-influence/
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
        Version 0 explains the distinction between outliers and influential points,
        and introduces diagnostic tools for assessing their impact.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/outliers-and-influence/",
      label: "Lesson 6 — Outliers and Influence",
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
        <span class="badge">Lesson 6</span>
        <span class="badge">Outliers</span>
        <span class="badge">Influence</span>
      </div>

      <h1>6. Outliers and Influence</h1>

      <p class="lead">
        A single observation can substantially change an estimate,
        a confidence interval, or even a hypothesis test conclusion.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/assumptions-robustness/">Back to Block 7</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Not all outliers are influential — and not all influential points are outliers.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Distinguish between outliers and influential observations,
      understand their impact on inference,
      and apply diagnostic tools responsibly.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core distinction</h2>
      <p style="margin:0;">
        An outlier is extreme in value.  
        An influential point changes the model result when removed.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Outliers</h2>
  </div>

  <div class="card">
    An observation is an outlier if:
    <br><br>
    • It lies far from the center of the data  
    • It deviates strongly from the pattern  
  </div>

  <p>
    Example (z-score rule):
    \[
    |Z| > 3
    \]
  </p>

  <p class="muted-mini">
    Extreme values do not automatically invalidate analysis.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Influence</h2>
  </div>

  <div class="card">
    Influence measures how much an observation changes:
    <br><br>
    • Estimated coefficients  
    • Standard errors  
    • Test statistics  
  </div>

  <div class="card" style="margin-top:1rem;">
    Cook’s distance:
    \[
    D_i
    \]
  </div>

  <p>
    Large values of \(D_i\) indicate influential observations.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why they matter</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Mean sensitivity</h3>
      <p>
        The sample mean is highly sensitive to extreme values.
      </p>
    </div>

    <div class="card">
      <h3>Regression slopes</h3>
      <p>
        A single high-leverage point can alter slope direction.
      </p>
    </div>

    <div class="card">
      <h3>Type I error</h3>
      <p>
        Outliers can inflate variance and distort inference.
      </p>
    </div>

    <div class="card">
      <h3>Misleading conclusions</h3>
      <p>
        Results may be driven by a small subset of observations.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Diagnostic tools</h2>
  </div>

  <div class="card">
    Common diagnostics:
    <br><br>
    • Boxplots  
    • Residual plots  
    • Leverage statistics  
    • Cook’s distance  
  </div>

  <div class="card" style="margin-top:1rem;">
    Standardized residual:
    \[
    r_i = \frac{e_i}{\hat{\sigma}(e_i)}
    \]
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) What to do</h2>
  </div>

  <div class="card">
    Responsible strategy:
    <br><br>
    1. Investigate data entry errors  
    2. Assess influence formally  
    3. Compare results with and without the point  
    4. Consider robust alternatives  
  </div>

  <p class="muted-mini">
    Removing points without justification is not acceptable practice.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define outliers precisely</li>
        <li>Understand influence vs extremeness</li>
        <li>Apply diagnostic tools</li>
        <li>Handle extreme values responsibly</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine robust and nonparametric alternatives
        when assumptions fail substantially.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/assumptions-robustness/robust-alternatives-nonparametric/">
          Next lesson: 7. Robust and Nonparametric Alternatives →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/assumptions-robustness/heteroscedasticity-variance-issues/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 5: Heteroscedasticity
          </a>
        </div>
      </div>
    </div>
  </div>
</section>