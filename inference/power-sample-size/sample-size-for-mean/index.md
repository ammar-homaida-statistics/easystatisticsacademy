---
layout: default
title: "4. Sample Size for a Mean"
description: "Derive and interpret the required sample size for detecting a mean difference with specified power and significance level."
permalink: /inference/power-sample-size/sample-size-for-mean/
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
        Version 0 derives the classical sample size formula for detecting a mean difference.
        Extensions to two-sample designs and software tools will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_power_sample_size_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/power-sample-size/sample-size-for-mean/",
      label: "Lesson 4 — Sample Size for a Mean",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/power-sample-size/",
      label: "Block 5 — Power & Sample Size",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">Sample Size</span>
        <span class="badge">Mean</span>
      </div>

      <h1>4. Sample Size for a Mean</h1>

      <p class="lead">
        Before collecting data, we must determine how large a sample is needed
        to detect a meaningful difference in a population mean
        with specified power and significance level.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/power-sample-size/">Back to Block 5</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Planning prevents underpowered studies.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Derive and interpret the required sample size
      for detecting a specified mean difference
      under given alpha and power.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Planning question</h2>
      <p style="margin:0;">
        What sample size ensures at least
        a chosen power (1 − beta)
        for detecting a meaningful difference delta?
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Setup</h2>
  </div>

  <div class="card">
    Hypotheses:
    \[
    H_0: \mu = \mu_0
    \]
    \[
    H_1: \mu = \mu_0 + \delta
    \]
  </div>

  <p>
    Assume known population standard deviation sigma
    (normal approximation).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Test statistic under H1</h2>
  </div>

  <div class="card">
    Standard error:
    \[
    SE = \frac{\sigma}{\sqrt{n}}
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Standardized effect:
    \[
    \frac{\delta}{SE}
    =
    \frac{\delta \sqrt{n}}{\sigma}
    \]
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Required sample size formula</h2>
  </div>

  <div class="card">
    For a two-sided test:
    \[
    n =
    \left(
    \frac{
    z_{\alpha/2} + z_{\beta}
    }{
    \delta / \sigma
    }
    \right)^2
    \]
  </div>

  <p class="muted-mini">
    Where:
    <br>
    • z_{alpha/2} controls Type I error  
    • z_beta ensures desired power  
    • delta is the smallest meaningful difference  
    • sigma is population standard deviation  
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Interpretation</h2>
  </div>

  <div class="card">
    Larger required power → larger n  
    Smaller alpha → larger n  
    Smaller detectable delta → much larger n  
    Larger variability sigma → larger n  
  </div>

  <p>
    Detecting very small effects requires
    disproportionately large samples.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical considerations</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Choose meaningful delta</h3>
      <p>
        Define smallest practically important difference,
        not smallest statistically detectable difference.
      </p>
    </div>

    <div class="card">
      <h3>Estimate sigma carefully</h3>
      <p>
        Use pilot studies or prior research.
      </p>
    </div>

    <div class="card">
      <h3>Account for dropouts</h3>
      <p>
        Increase calculated n if attrition is expected.
      </p>
    </div>

    <div class="card">
      <h3>Two-sample extension</h3>
      <p>
        Similar formula with group allocation adjustment.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Derive classical sample size formula</li>
        <li>Interpret role of alpha and beta</li>
        <li>Understand impact of variability and effect size</li>
        <li>Plan studies responsibly</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now derive required sample size
        for estimating and testing proportions.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/power-sample-size/sample-size-for-proportion/">
          Next lesson: 5. Sample Size for a Proportion →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/power-sample-size/power-curve-and-tradeoffs/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Power Curves & Trade-offs
          </a>
        </div>
      </div>
    </div>
  </div>
</section>