---
layout: default
title: "2. Model Assumptions vs Design Assumptions"
description: "Distinguish between statistical model assumptions and study design assumptions, and understand which violations threaten validity most."
permalink: /inference/assumptions-robustness/model-assumptions-vs-design-assumptions/
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
        Version 0 clarifies the distinction between model-based assumptions
        and design-based assumptions, and why design violations are often more serious.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/",
      label: "Lesson 2 — Model vs Design Assumptions",
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
        <span class="badge">Lesson 2</span>
        <span class="badge">Model</span>
        <span class="badge">Design</span>
      </div>

      <h1>2. Model Assumptions vs Design Assumptions</h1>

      <p class="lead">
        Not all assumptions are equally important.
        Violations of study design assumptions often threaten validity
        more seriously than violations of distributional assumptions.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/assumptions-robustness/">Back to Block 7</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Good design can rescue weak models; weak design cannot be fixed by modeling.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Distinguish between model-based and design-based assumptions,
      and evaluate their relative importance for valid inference.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core distinction</h2>
      <p style="margin:0;">
        Model assumptions describe probability structure.  
        Design assumptions describe how data were generated.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Model assumptions</h2>
  </div>

  <div class="card">
    Examples:
    <br><br>
    • Normality of errors  
    • Equal variances  
    • Linearity  
    • Homoscedasticity  
  </div>

  <p>
    These assumptions determine the sampling distribution
    of estimators and test statistics.
  </p>

  <div class="card" style="margin-top:1rem;">
    Example (linear model):
    \[
    Y = X\beta + \varepsilon,
    \quad
    \varepsilon \sim \mathcal{N}(0, \sigma^2)
    \]
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Design assumptions</h2>
  </div>

  <div class="card">
    Examples:
    <br><br>
    • Random sampling  
    • Random assignment  
    • Independence between units  
    • No selection bias  
  </div>

  <p>
    These assumptions justify generalization and causal interpretation.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Which matters more?</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Minor non-normality</h3>
      <p>
        Often harmless with moderate or large n.
      </p>
    </div>

    <div class="card">
      <h3>Biased sampling</h3>
      <p>
        Invalidates generalization completely.
      </p>
    </div>

    <div class="card">
      <h3>Mild heteroscedasticity</h3>
      <p>
        Can be corrected with robust standard errors.
      </p>
    </div>

    <div class="card">
      <h3>Lack of independence</h3>
      <p>
        Severely distorts standard errors and inference.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Example comparison</h2>
  </div>

  <div class="card">
    Scenario A:
    <br>
    Data slightly skewed but randomly sampled.
  </div>

  <div class="card" style="margin-top:1rem;">
    Scenario B:
    <br>
    Perfectly normal data but non-random convenience sample.
  </div>

  <p>
    Scenario B poses a larger threat to validity.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical guideline</h2>
  </div>

  <div class="card">
    Priority order:
    <br><br>
    1. Design validity  
    2. Independence  
    3. Correct model form  
    4. Distributional details  
  </div>

  <p class="muted-mini">
    Distributional assumptions are often the most robust.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Differentiate model vs design assumptions</li>
        <li>Recognize threats to validity</li>
        <li>Prioritize independence and sampling</li>
        <li>Interpret assumption violations correctly</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine what “normality” really means
        and how to check it responsibly.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/assumptions-robustness/checking-normality-what-and-why/">
          Next lesson: 3. Checking Normality — What and Why →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/assumptions-robustness/assumptions-vs-robustness-mindset/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: Assumptions vs Robustness
          </a>
        </div>
      </div>
    </div>
  </div>
</section>