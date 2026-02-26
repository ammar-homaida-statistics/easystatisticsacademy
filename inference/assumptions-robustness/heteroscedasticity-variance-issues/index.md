---
layout: default
title: "5. Heteroscedasticity and Variance Issues"
description: "Understand heteroscedasticity, why unequal variances matter for inference, and how to diagnose and correct variance-related problems."
permalink: /inference/assumptions-robustness/heteroscedasticity-variance-issues/
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
        Version 0 explains heteroscedasticity, how it affects standard errors,
        and how robust methods can correct inference without changing estimates.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/heteroscedasticity-variance-issues/",
      label: "Lesson 5 — Heteroscedasticity and Variance Issues",
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
        <span class="badge">Lesson 5</span>
        <span class="badge">Variance</span>
        <span class="badge">Robust SE</span>
      </div>

      <h1>5. Heteroscedasticity and Variance Issues</h1>

      <p class="lead">
        Many classical methods assume constant variance.
        When variance changes across observations,
        standard errors — not coefficients — are usually the first casualty.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/assumptions-robustness/">Back to Block 7</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Unequal variance primarily distorts uncertainty, not point estimates.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand what heteroscedasticity is, why it matters,
      and how to detect and correct it in practice.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core idea</h2>
      <p style="margin:0;">
        Heteroscedasticity means that the variance of the error term
        is not constant across observations.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Constant vs non-constant variance</h2>
  </div>

  <div class="card">
    Homoscedasticity:
    \[
    Var(\varepsilon_i) = \sigma^2
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Heteroscedasticity:
    \[
    Var(\varepsilon_i) = \sigma_i^2
    \]
  </div>

  <p>
    The variance differs across levels of X or across groups.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Why it matters</h2>
  </div>

  <div class="card">
    In linear regression:
    \[
    Var(\hat{\beta}) = \sigma^2 (X'X)^{-1}
    \]
  </div>

  <p>
    This formula assumes constant variance.
    If variance is unequal, standard errors become biased.
  </p>

  <div class="card" style="margin-top:1rem;">
    Consequences:
    <br><br>
    • Incorrect confidence intervals  
    • Distorted p-values  
    • Inflated or deflated Type I error  
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Detecting heteroscedasticity</h2>
  </div>

  <div class="card">
    Graphical diagnostics:
    <br><br>
    • Residuals vs fitted values plot  
    • Spread increasing with predictor  
  </div>

  <div class="card" style="margin-top:1rem;">
    Formal tests:
    <br><br>
    • Breusch–Pagan test  
    • White test  
  </div>

  <p class="muted-mini">
    Visual inspection is often more informative than formal testing.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) What does not change</h2>
  </div>

  <div class="card">
    Under standard assumptions:
    <br><br>
    OLS estimates remain unbiased even under heteroscedasticity.
  </div>

  <p>
    The issue is efficiency and correct inference,
    not bias of coefficients.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Remedies</h2>
  </div>

  <div class="card">
    Common solutions:
    <br><br>
    • Heteroscedasticity-robust standard errors  
    • Transformations (log scale)  
    • Weighted least squares  
  </div>

  <div class="card" style="margin-top:1rem;">
    Robust variance estimator:
    \[
    \widehat{Var}(\hat{\beta})_{\text{robust}}
    \]
  </div>

  <p class="muted-mini">
    Robust SE adjusts uncertainty without changing coefficients.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define heteroscedasticity precisely</li>
        <li>Understand its effect on standard errors</li>
        <li>Diagnose variance patterns graphically</li>
        <li>Apply robust inference when necessary</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine outliers and influential observations —
        when a few points control the entire conclusion.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/assumptions-robustness/outliers-and-influence/">
          Next lesson: 6. Outliers and Influence →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/assumptions-robustness/independence-and-dependence/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Independence and Dependence
          </a>
        </div>
      </div>
    </div>
  </div>
</section>