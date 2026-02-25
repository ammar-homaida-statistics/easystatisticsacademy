---
layout: default
title: "5. Sample Size for a Proportion"
description: "Derive and interpret the required sample size for detecting a difference in a population proportion with specified alpha and power."
permalink: /inference/power-sample-size/sample-size-for-proportion/
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
        Version 0 derives the core sample size formula for a one-sample proportion
        under normal approximation. Two-sample extensions and software tools
        will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_power_sample_size_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/power-sample-size/sample-size-for-proportion/",
      label: "Lesson 5 — Sample Size for a Proportion",
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
        <span class="badge">Lesson 5</span>
        <span class="badge">Sample Size</span>
        <span class="badge">Proportion</span>
      </div>

      <h1>5. Sample Size for a Proportion</h1>

      <p class="lead">
        To detect a meaningful change in a population proportion,
        we must determine the required sample size
        based on the desired power and significance level.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/power-sample-size/">Back to Block 5</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Planning requires specifying the smallest important difference.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Derive and interpret the required sample size for detecting
      a specified difference in a population proportion.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Planning question</h2>
      <p style="margin:0;">
        What sample size n ensures:
        \[
        P(\text{Reject } H_0 \mid p = p_0 + \Delta) = 1 - \beta ?
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
    Hypotheses:
    \[
    H_0: p = p_0
    \qquad
    H_1: p \neq p_0
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Test statistic (normal approximation):
    \[
    Z =
    \frac{\hat{p} - p_0}
         {\sqrt{ \frac{p_0(1 - p_0)}{n} }}
    \]
  </div>

  <p class="muted-mini">
    Assumes normal approximation to the binomial.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Detectable difference</h2>
  </div>

  <div class="card">
    Let
    \[
    \Delta = |p - p_0|
    \]
    be the smallest meaningful difference.
  </div>

  <p>
    Under the alternative,
    the standardized shift equals:
    \[
    \frac{\Delta}
         {\sqrt{ \frac{p_0(1 - p_0)}{n} }}
    =
    \frac{\Delta \sqrt{n}}
         {\sqrt{p_0(1 - p_0)}}
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
    \frac{
      (z_{\alpha/2} + z_{\beta})^2
      \, p_0 (1 - p_0)
    }
    {\Delta^2}
    \]
  </div>

  <p class="muted-mini">
    Where:
    <br>
    • \(z_{\alpha/2}\) controls Type I error  
    • \(z_{\beta}\) controls power  
    • \(\Delta\) is the smallest meaningful difference  
    • \(p_0\) is the baseline proportion  
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
    • Alpha decreases  
    • Baseline proportion near 0.5 (maximum variance)  
    • Detectable difference becomes smaller  
  </div>

  <p>
    Variance is largest when \(p_0 = 0.5\),
    which yields the most conservative sample size.
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
    Step 4: Specify baseline proportion p₀  
    <br>
    Step 5: Compute required n  
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Derive sample size formula for a proportion</li>
        <li>Understand role of baseline proportion</li>
        <li>Interpret influence of alpha and beta</li>
        <li>Plan proportion studies responsibly</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now distinguish planning for precision
        from planning for detectability.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/power-sample-size/precision-vs-detectability/">
          Next lesson: 6. Precision vs Detectability →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/power-sample-size/sample-size-for-mean/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Sample Size for a Mean
          </a>
        </div>
      </div>
    </div>
  </div>
</section>