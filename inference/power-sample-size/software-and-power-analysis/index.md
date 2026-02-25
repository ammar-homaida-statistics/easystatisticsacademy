---
layout: default
title: "8. Software and Power Analysis"
description: "Use statistical software to compute power and required sample size. Understand inputs, outputs, and common misinterpretations."
permalink: /inference/power-sample-size/software-and-power-analysis/
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
        Version 0 introduces practical computation of power and sample size
        using statistical software. Full worked examples and screenshots
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
      url: "/inference/power-sample-size/software-and-power-analysis/",
      label: "Lesson 8 — Software & Power Analysis",
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
        <span class="badge">Lesson 8</span>
        <span class="badge">Software</span>
        <span class="badge">Planning</span>
      </div>

      <h1>8. Software and Power Analysis</h1>

      <p class="lead">
        Modern statistical software can compute required sample size,
        achieved power, and detectable effect sizes.
        Understanding inputs and outputs is essential for correct planning.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/power-sample-size/">Back to Block 5</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Software implements formulas — but interpretation remains your responsibility.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Identify required inputs for power analysis,
      interpret software outputs correctly,
      and avoid common computational mistakes.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core principle</h2>
      <p style="margin:0;">
        Every power calculation requires:
        <br>
        • Significance level \( \alpha \)  
        • Desired power \( 1 - \beta \)  
        • Effect size  
        • Variability measure  
        • Test type (one- vs two-sided)  
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Mean tests in software</h2>
  </div>

  <div class="card">
    Required inputs:
    \[
    \alpha, \quad 1 - \beta, \quad \sigma, \quad \Delta
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Software computes:
    \[
    n =
    \frac{(z_{\alpha/2} + z_{\beta})^2 \sigma^2}{\Delta^2}
    \]
  </div>

  <p>
    Some tools also compute achieved power given fixed n.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Proportion tests in software</h2>
  </div>

  <div class="card">
    Required inputs:
    \[
    \alpha, \quad 1 - \beta, \quad p_0, \quad \Delta
    \]
  </div>

  <p>
    Software typically uses normal approximation methods
    unless exact methods are specified.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Effect size specification</h2>
  </div>

  <div class="card">
    For means:
    \[
    d = \frac{\Delta}{\sigma}
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    For proportions:
    \[
    \Delta = |p - p_0|
    \]
  </div>

  <p class="muted-mini">
    Many software tools require standardized effect sizes.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Common mistakes</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Wrong test type</h3>
      <p>Using two-sided instead of one-sided (or vice versa).</p>
    </div>

    <div class="card">
      <h3>Incorrect variability</h3>
      <p>Using unrealistic σ or p estimates.</p>
    </div>

    <div class="card">
      <h3>Post-hoc power misuse</h3>
      <p>Computing power after observing p-value adds little information.</p>
    </div>

    <div class="card">
      <h3>Ignoring design features</h3>
      <p>Clustered or paired designs require adjusted formulas.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Interpretation of output</h2>
  </div>

  <div class="card">
    Software output typically includes:
    <br><br>
    • Required sample size n  
    • Achieved power  
    • Detectable effect size  
    • Assumed parameters  
  </div>

  <p>
    Always verify that:
    <br>
    • Alpha matches design plan  
    • Test direction matches hypothesis  
    • Effect size reflects practical importance  
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Planning workflow</h2>
  </div>

  <div class="card">
    Step 1: Define smallest meaningful effect  
    <br>
    Step 2: Choose alpha  
    <br>
    Step 3: Choose desired power  
    <br>
    Step 4: Estimate variability  
    <br>
    Step 5: Use software to compute n  
    <br>
    Step 6: Document assumptions clearly  
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand required inputs for power analysis</li>
        <li>Interpret software output correctly</li>
        <li>Avoid common computational mistakes</li>
        <li>Document assumptions transparently</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next block</h2>
      <p style="margin:0;">
        We now move to
        <strong>Block 6 — Interpretation & Reporting</strong>,
        where we focus on communicating results responsibly.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/interpretation-reporting/">
          Go to Block 6 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/power-sample-size/underpowered-studies/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 7: Underpowered Studies
          </a>
        </div>
      </div>
    </div>
  </div>
</section>