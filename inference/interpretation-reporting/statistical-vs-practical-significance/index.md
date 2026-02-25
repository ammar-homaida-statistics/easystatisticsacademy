---
layout: default
title: "2. Statistical vs Practical Significance"
description: "Distinguish statistical significance from practical importance. Understand how sample size affects p-values and why effect size matters."
permalink: /inference/interpretation-reporting/statistical-vs-practical-significance/
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
        Version 0 clarifies why “statistically significant” does not imply
        “important” and how sample size influences conclusions.
        Applied examples will be expanded later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_interpretation_reporting_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/interpretation-reporting/statistical-vs-practical-significance/",
      label: "Lesson 2 — Statistical vs Practical Significance",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/interpretation-reporting/",
      label: "Block 6 — Interpretation & Reporting",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Effect Size</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>2. Statistical vs Practical Significance</h1>

      <p class="lead">
        A small p-value indicates statistical evidence.
        It does not automatically imply that the effect is meaningful in practice.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/">Back to Block 6</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Statistical detectability and real-world importance are different concepts.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Distinguish between statistical significance and practical relevance,
      and understand how sample size affects p-values.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core distinction</h2>
      <p style="margin:0;">
        Statistical significance answers:
        “Is the effect detectable?”
        <br><br>
        Practical significance answers:
        “Is the effect large enough to matter?”
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Role of sample size</h2>
  </div>

  <div class="card">
    Test statistic (mean case):
    \[
    T =
    \frac{\bar{X} - \mu_0}{SE}
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Standard error:
    \[
    SE = \frac{\sigma}{\sqrt{n}}
    \]
  </div>

  <p>
    As n increases:
    <br>
    • SE decreases  
    • T increases for same difference  
    • p-value becomes smaller  
  </p>

  <p class="muted-mini">
    Large samples can detect very small effects.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Small effect, large sample</h2>
  </div>

  <div class="card">
    Even a tiny difference
    \[
    \Delta \approx 0
    \]
    may yield:
    \[
    p < 0.05
    \]
    when n is very large.
  </div>

  <p>
    This does not guarantee meaningful impact.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Large effect, small sample</h2>
  </div>

  <div class="card">
    With small n:
    <br><br>
    • SE is large  
    • Test statistic may be modest  
    • p-value may exceed 0.05  
  </div>

  <p>
    A practically important effect may fail to reach significance.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Effect size measures</h2>
  </div>

  <div class="card">
    Standardized mean difference:
    \[
    d = \frac{\Delta}{\sigma}
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    For proportions:
    \[
    \Delta = |p_1 - p_2|
    \]
  </div>

  <p>
    Effect sizes quantify magnitude independently of sample size.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Reporting recommendation</h2>
  </div>

  <div class="card">
    Good reporting includes:
    <br><br>
    • Effect size  
    • Confidence interval  
    • p-value  
    • Contextual interpretation  
  </div>

  <p>
    Avoid binary language such as “significant / not significant”
    without discussing magnitude.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Separate detectability from importance</li>
        <li>Understand impact of sample size on p-values</li>
        <li>Use effect size for magnitude assessment</li>
        <li>Report results responsibly</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now clarify how to interpret confidence intervals correctly.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/interpretation-reporting/interpreting-confidence-intervals/">
          Next lesson: 3. Interpreting Confidence Intervals →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/interpretation-reporting/p-values-what-they-mean/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: P-Values — What They Mean
          </a>
        </div>
      </div>
    </div>
  </div>
</section>