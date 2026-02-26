---
layout: default
title: "10. Reporting Assumptions and Limitations"
description: "Learn how to transparently report model assumptions, robustness checks, and study limitations to strengthen credibility."
permalink: /inference/assumptions-robustness/reporting-assumptions-and-limitations/
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
        Version 0 formalizes how to report assumptions, diagnostic checks,
        robustness analyses, and limitations with clarity and integrity.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/reporting-assumptions-and-limitations/",
      label: "Lesson 10 — Reporting Assumptions & Limitations",
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
        <span class="badge">Lesson 10</span>
        <span class="badge">Transparency</span>
        <span class="badge">Limitations</span>
      </div>

      <h1>10. Reporting Assumptions and Limitations</h1>

      <p class="lead">
        Credible inference requires more than correct calculations.
        It requires transparent reporting of assumptions, diagnostics,
        robustness checks, and study limitations.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/assumptions-robustness/">Back to Block 7</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Transparency increases reproducibility and scientific trust.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Develop a structured and professional approach to reporting
      statistical assumptions, diagnostics, robustness checks,
      and practical limitations.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core principle</h2>
      <p style="margin:0;">
        Statistical reporting should make it possible for another analyst
        to understand, evaluate, and replicate the inferential logic.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Report model assumptions explicitly</h2>
  </div>

  <div class="card">
    Clearly state:
    <br><br>
    • Independence assumptions  
    • Distributional assumptions (e.g., normality)  
    • Variance assumptions (equal vs unequal)  
    • Design assumptions (random sampling, random assignment)  
  </div>

  <p>
    Do not assume readers will infer which assumptions were used.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Report diagnostic checks</h2>
  </div>

  <div class="card">
    Include:
    <br><br>
    • Normality diagnostics (QQ-plot summary)  
    • Variance checks  
    • Outlier analysis  
    • Sensitivity analysis summary  
  </div>

  <p>
    Diagnostics need not be exhaustive,
    but key checks should be documented.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Report robustness comparisons</h2>
  </div>

  <div class="card">
    Example phrasing:
    <br><br>
    “Results were consistent under Welch’s correction.”  
    “Conclusions remained unchanged using a nonparametric alternative.”  
  </div>

  <p>
    Stability strengthens credibility.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Distinguish limitations clearly</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Statistical limitations</h3>
      <p>
        Small sample size, measurement error, assumption concerns.
      </p>
    </div>

    <div class="card">
      <h3>Design limitations</h3>
      <p>
        Non-random sampling, observational data, confounding.
      </p>
    </div>
  </div>

  <p>
    Limitations do not invalidate results —
    but they bound interpretation.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Recommended reporting structure</h2>
  </div>

  <div class="card">
    Suggested order:
    <br><br>
    1. Research question  
    2. Statistical method  
    3. Assumptions  
    4. Test results (estimate, CI, p-value)  
    5. Robustness checks  
    6. Limitations  
    7. Practical interpretation  
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Report assumptions clearly</li>
        <li>Document diagnostics and robustness</li>
        <li>Distinguish statistical and design limits</li>
        <li>Strengthen transparency and reproducibility</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Return to the full Statistical Inference structure
        to integrate all components.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/">
          Back to Statistical Inference →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/assumptions-robustness/sensitivity-analysis-and-specification/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 9: Sensitivity Analysis & Specification
          </a>
        </div>
      </div>
    </div>
  </div>
</section>