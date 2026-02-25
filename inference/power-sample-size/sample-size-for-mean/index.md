---
layout: default
title: "4. Sample Size for a Mean"
description: "Derive and interpret the required sample size for detecting a mean difference with specified alpha and power."
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
        Version 0 derives the core sample size formula for a mean under
        normal approximation. Extensions to two-sample cases and software
        implementation will be added later.
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
        Before collecting data, we must determine how many observations
        are required to detect a meaningful difference in the population mean
        with specified power and significance level.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/power-sample-size/">Back to Block 5</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Sample size planning connects effect size, alpha, and power.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Derive and interpret the required sample size for detecting
      a specified mean difference with chosen alpha and power.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Planning question</h2>
      <p style="margin:0;">
        What sample size n ensures:
        \[
        P(\text{Reject } H_0 \mid \mu = \mu_0 + \Delta) = 1 - \beta ?
        \]
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Setup</h2>
  </div>

  <div class="card">
    Test:
    \[
    H_0: \mu = \mu_0
    \qquad
    H_1: \mu \neq \mu_0
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Standardized test statistic:
    \[
    Z =
    \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}
    \]
  </div>

  <p class="muted-mini">
    Assume σ known and normal approximation.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Detectable difference</h2>
  </div>

  <div class="card">
    Let
    \[
    \Delta = |\mu - \mu_0|
    \]
    denote the smallest meaningful difference.
  </div>

  <p>
    Under the alternative,
    the standardized mean shift equals:
    \[
    \frac{\Delta}{\sigma/\sqrt{n}}
    =
    \frac{\Delta \sqrt{n}}{\sigma}
    \]
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Sample size formula (two-sided test)</h2>
  </div>

  <div class="card">
    Required sample size:
    \[
    n =
    \left(
    \frac{ z_{\alpha/2} + z_{\beta} }{\Delta / \sigma}
    \right)^2
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Equivalent form:
    \[
    n =
    \frac{ (z_{\alpha/2} + z_{\beta})^2 \sigma^2 }
         { \Delta^2 }
    \]
  </div>

  <p class="muted-mini">
    Where:
    <br>
    • \(z_{\alpha/2}\) controls Type I error  
    • \(z_{\beta}\) controls power  
    • \(\Delta\) is the smallest effect of interest  
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Interpretation</h2>
  </div>

  <div class="card">
    Larger required n when:
    <br><br>
    • Desired power increases  
    • Significance level decreases  
    • Variability increases  
    • Detectable effect size decreases  
  </div>

  <p>
    Small meaningful differences require large samples.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical workflow</h2>
  </div>

  <div class="card">
    Step 1: Choose alpha (e.g., 0.05)  
    <br>
    Step 2: Choose desired power (e.g., 0.80 or 0.90)  
    <br>
    Step 3: Specify smallest meaningful difference Δ  
    <br>
    Step 4: Estimate population standard deviation σ  
    <br>
    Step 5: Compute required n  
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Derive sample size formula for a mean</li>
        <li>Interpret roles of alpha and beta</li>
        <li>Understand impact of variability</li>
        <li>Plan studies based on meaningful differences</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now derive required sample size for detecting
        a difference in proportions.
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