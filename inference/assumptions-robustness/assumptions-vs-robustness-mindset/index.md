---
layout: default
title: "1. Assumptions vs Robustness: The Mindset"
description: "Understand why statistical assumptions exist, what robustness means, and how to think when assumptions are only approximately true."
permalink: /inference/assumptions-robustness/assumptions-vs-robustness-mindset/
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
        Version 0 establishes the conceptual mindset for thinking about assumptions
        and robustness. Applied diagnostics and examples will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/assumptions-vs-robustness-mindset/",
      label: "Lesson 1 — Assumptions vs Robustness",
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
        <span class="badge">Lesson 1</span>
        <span class="badge">Assumptions</span>
        <span class="badge">Robustness</span>
      </div>

      <h1>1. Assumptions vs Robustness: The Mindset</h1>

      <p class="lead">
        Statistical procedures rely on assumptions.
        Robustness describes how sensitive conclusions are
        when those assumptions are not perfectly satisfied.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/assumptions-robustness/">Back to Block 7</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        The goal is not perfect assumptions — but valid inference.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand why assumptions are required,
      what robustness means formally,
      and how to evaluate practical impact of assumption violations.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core idea</h2>
      <p style="margin:0;">
        Every inference method depends on a probability model.
        Assumptions define that model.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Why assumptions exist</h2>
  </div>

  <div class="card">
    Example:
    <br><br>
    One-sample t statistic:
    \[
    T =
    \frac{\bar{X} - \mu_0}{S / \sqrt{n}}
    \]
  </div>

  <p>
    Its sampling distribution depends on:
    <br>
    • Independence  
    • Identical distribution  
    • Approximate normality (for small n)  
  </p>

  <p>
    Without assumptions, the distribution of T is unknown.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) What robustness means</h2>
  </div>

  <div class="card">
    A method is robust if:
    <br><br>
    Small violations of assumptions
    → small changes in inference.
  </div>

  <p>
    Robustness is not binary.
    It is a matter of degree.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Approximate validity</h2>
  </div>

  <div class="card">
    Central Limit Theorem:
    \[
    \bar{X} \approx \mathcal{N}(\mu, \sigma^2/n)
    \quad \text{for large } n
    \]
  </div>

  <p>
    Many classical methods remain approximately valid
    when n is large, even if data are not perfectly normal.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Sensitivity mindset</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Ask:</h3>
      <p>
        Does violation change standard errors?
      </p>
    </div>

    <div class="card">
      <h3>Ask:</h3>
      <p>
        Does violation bias the estimate?
      </p>
    </div>

    <div class="card">
      <h3>Ask:</h3>
      <p>
        Is the effect large relative to noise?
      </p>
    </div>

    <div class="card">
      <h3>Ask:</h3>
      <p>
        Would a robust alternative change the conclusion?
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical interpretation</h2>
  </div>

  <div class="card">
    Good practice:
    <br><br>
    • Check assumptions  
    • Quantify violations  
    • Use robust methods when needed  
    • Report limitations transparently  
  </div>

  <p>
    Statistical rigor means evaluating stability,
    not blindly applying formulas.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand role of assumptions</li>
        <li>Define robustness clearly</li>
        <li>Adopt a sensitivity mindset</li>
        <li>Recognize approximate validity</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now distinguish between model assumptions
        and design assumptions.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/">
          Next lesson: 2. Model vs Design Assumptions →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous block</div>
        <div class="mini-body">
          <a href="/inference/interpretation-reporting/" style="color:#1a73e8; text-decoration:underline;">
            Block 6: Interpretation & Reporting
          </a>
        </div>
      </div>
    </div>
  </div>
</section>