---
layout: default
title: "7. Tables, Figures, and Visual Communication"
description: "Present statistical results effectively using well-structured tables and informative figures without distorting interpretation."
permalink: /inference/interpretation-reporting/tables-figures-and-visual-communication/
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
        Version 0 establishes principles for clear statistical tables and figures.
        Applied design examples and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_interpretation_reporting_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/interpretation-reporting/tables-figures-and-visual-communication/",
      label: "Lesson 7 — Tables, Figures & Visual Communication",
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
        <span class="badge">Lesson 7</span>
        <span class="badge">Tables</span>
        <span class="badge">Figures</span>
      </div>

      <h1>7. Tables, Figures, and Visual Communication</h1>

      <p class="lead">
        Clear statistical communication requires more than correct numbers.
        Tables and figures must present results accurately,
        transparently, and without visual distortion.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/">Back to Block 6</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Visual design affects interpretation.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Design tables and figures that communicate results clearly,
      avoid misleading visuals,
      and align graphical displays with statistical interpretation.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core principle</h2>
      <p style="margin:0;">
        A figure should clarify the statistical result —
        not exaggerate it.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Well-structured tables</h2>
  </div>

  <div class="card">
    A statistical results table should include:
    <br><br>
    • Variable or comparison label  
    • Estimate (mean, difference, coefficient, etc.)  
    • Standard error or standard deviation  
    • Confidence interval  
    • Test statistic and p-value  
    • Effect size (if applicable)  
  </div>

  <p>
    Avoid overcrowded tables with redundant values.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Graphical integrity</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Avoid</h3>
      <p>
        Truncated axes that exaggerate differences.
      </p>
    </div>

    <div class="card">
      <h3>Prefer</h3>
      <p>
        Clearly labeled axes with meaningful scales.
      </p>
    </div>

    <div class="card">
      <h3>Avoid</h3>
      <p>
        3D charts that distort perception.
      </p>
    </div>

    <div class="card">
      <h3>Prefer</h3>
      <p>
        Clean 2D visualizations with uncertainty bars.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Always show uncertainty</h2>
  </div>

  <div class="card">
    For estimated means or proportions, include:
    <br><br>
    • Error bars representing confidence intervals  
    • Clear legend explaining interval type  
  </div>

  <p>
    A point estimate without uncertainty is incomplete.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Match figure to question</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Group comparisons</h3>
      <p>
        Bar chart with CI or dot plot with intervals.
      </p>
    </div>

    <div class="card">
      <h3>Associations</h3>
      <p>
        Scatterplot with regression line.
      </p>
    </div>

    <div class="card">
      <h3>Distribution</h3>
      <p>
        Histogram or density plot.
      </p>
    </div>

    <div class="card">
      <h3>Model coefficients</h3>
      <p>
        Forest plot style visualization.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Caption clarity</h2>
  </div>

  <div class="card">
    A good caption should state:
    <br><br>
    • What is displayed  
    • What the error bars represent  
    • Sample size  
    • Key takeaway  
  </div>

  <p>
    Readers should understand the figure without reading the full text.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Design clean statistical tables</li>
        <li>Avoid misleading visual distortions</li>
        <li>Include uncertainty in figures</li>
        <li>Write informative captions</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We conclude this block with reproducibility
        and a structured analysis checklist.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/interpretation-reporting/reproducibility-and-analysis-checklist/">
          Next lesson: 8. Reproducibility & Analysis Checklist →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/interpretation-reporting/reporting-results-clear-language/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 6: Reporting Results in Clear Language
          </a>
        </div>
      </div>
    </div>
  </div>
</section>