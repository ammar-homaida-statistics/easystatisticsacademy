---
layout: default
title: "9. Sensitivity Analysis and Specification"
description: "Assess how sensitive your conclusions are to modeling choices, assumptions, and analytic decisions."
permalink: /inference/assumptions-robustness/sensitivity-analysis-and-specification/
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
        Version 0 formalizes sensitivity analysis as a disciplined robustness practice:
        vary reasonable assumptions and check whether conclusions materially change.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/sensitivity-analysis-and-specification/",
      label: "Lesson 9 — Sensitivity Analysis & Specification",
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
        <span class="badge">Lesson 9</span>
        <span class="badge">Sensitivity</span>
        <span class="badge">Specification</span>
      </div>

      <h1>9. Sensitivity Analysis and Specification</h1>

      <p class="lead">
        Robust inference is not only about alternative estimators.
        It is about asking: <em>Would my conclusion change under reasonable alternative choices?</em>
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/assumptions-robustness/">Back to Block 7</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Stability of conclusions is stronger evidence than a single significant result.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand how to evaluate whether results depend critically
      on modeling assumptions, parameter choices, or analytic specifications.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core principle</h2>
      <p style="margin:0;">
        A result is more credible when it remains consistent
        across plausible alternative specifications.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What is sensitivity analysis?</h2>
  </div>

  <div class="card">
    Sensitivity analysis evaluates how results change when:
    <br><br>
    • Assumptions are relaxed  
    • Model form is altered  
    • Outliers are excluded  
    • Alternative estimators are used  
  </div>

  <p>
    It does not search for significance.
    It tests stability.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Specification choices that matter</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Distributional assumptions</h3>
      <p>
        Normal vs nonparametric inference.
      </p>
    </div>

    <div class="card">
      <h3>Variance assumptions</h3>
      <p>
        Equal vs unequal variances.
      </p>
    </div>

    <div class="card">
      <h3>Functional form</h3>
      <p>
        Linear vs nonlinear models.
      </p>
    </div>

    <div class="card">
      <h3>Outlier handling</h3>
      <p>
        With vs without influential points.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Example: two-sample mean test</h2>
  </div>

  <div class="card">
    Compare:
    <br><br>
    • Classical pooled t-test  
    • Welch unequal-variance t-test  
    • Wilcoxon rank-sum test  
  </div>

  <p>
    If all approaches yield similar conclusions,
    inference is robust to specification.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Quantifying sensitivity</h2>
  </div>

  <div class="card">
    Compare:
    <br><br>
    • Significance decision (reject / not reject)  
    • Effect size estimates  
    • Confidence interval overlap  
  </div>

  <p>
    Large shifts in effect size or inference suggest fragile conclusions.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Interpretation guideline</h2>
  </div>

  <div class="card">
    Robust conclusion:
    <br><br>
    Same direction, similar magnitude,
    similar decision across specifications.
  </div>

  <div class="card" style="margin-top:1rem;">
    Fragile conclusion:
    <br><br>
    Significance depends heavily on one modeling choice.
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define sensitivity analysis clearly</li>
        <li>Identify key specification decisions</li>
        <li>Compare classical and alternative methods</li>
        <li>Assess stability of conclusions</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        Finally, we discuss how to report assumptions,
        robustness checks, and limitations transparently.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/assumptions-robustness/reporting-assumptions-and-limitations/">
          Next lesson: 10. Reporting Assumptions & Limitations →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/assumptions-robustness/bootstrap-as-robust-tool/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 8: Bootstrap as a Robust Tool
          </a>
        </div>
      </div>
    </div>
  </div>
</section>