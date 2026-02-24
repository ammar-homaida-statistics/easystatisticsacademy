<!-- =========================================================
BLOCK 6 — INTERPRETATION & REPORTING
File: /inference/interpretation-reporting/index.md
========================================================= -->
---
layout: default
title: Block 6 — Interpretation & Reporting
description: Interpret and report inference correctly: what p-values and confidence intervals mean, effect sizes, practical significance, multiple testing, and clear scientific communication.
permalink: /inference/interpretation-reporting/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block focuses on the hardest part of inference: <strong>interpretation</strong>.
        You will learn to report results accurately, avoid common wording mistakes,
        and connect statistical outputs (p-values, CIs, effect sizes) to real meaning.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/interpretation-reporting/",
      label: "Block 6 — Interpretation & Reporting",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Interpretation</span>
        <span class="badge">Reporting</span>
        <span class="badge">Communication</span>
      </div>

      <h1>Block 6 — Interpretation &amp; Reporting</h1>
      <p class="lead">
        A correct calculation with a wrong interpretation is still wrong.
        This block teaches how to interpret p-values and confidence intervals,
        emphasize effect sizes and practical significance, and report results clearly and honestly.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">Back to Statistical Inference</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will expand without changing URLs or order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Meaning of p-values</strong><span class="meta">What they are / what they are not</span></li>
          <li style="margin:.35rem 0;"><strong>CI interpretation</strong><span class="meta">Coverage, precision, and language</span></li>
          <li style="margin:.35rem 0;"><strong>Effect sizes</strong><span class="meta">Magnitude, not only significance</span></li>
          <li style="margin:.35rem 0;"><strong>Multiple testing</strong><span class="meta">False positives and adjustment logic</span></li>
          <li style="margin:.35rem 0;"><strong>Reporting</strong><span class="meta">Clear sentences, tables, and figures</span></li>
          <li style="margin:.35rem 0;"><strong>Reproducibility</strong><span class="meta">Checks, transparency, and workflow</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading (lesson-level placeholder key for this block) -->
<section class="section" id="continue-reading-block6" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block6-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block6-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons are published in order to keep interpretation logic coherent.
      The list below is the permanent structure for this block.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- Lesson 1 -->
    <div class="card lesson-card">
      <h3><a href="/inference/interpretation-reporting/p-values-what-they-mean/">1. p-Values: What They Mean (and Do Not Mean)</a></h3>
      <p>Define p-values precisely, connect them to the null model, and avoid classic interpretation errors.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/p-values-what-they-mean/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 2 -->
    <div class="card lesson-card">
      <h3><a href="/inference/interpretation-reporting/statistical-vs-practical-significance/">2. Statistical vs Practical Significance</a></h3>
      <p>Why “significant” does not mean “important” and how sample size changes conclusions.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/statistical-vs-practical-significance/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 3 -->
    <div class="card lesson-card">
      <h3><a href="/inference/interpretation-reporting/interpreting-confidence-intervals/">3. Interpreting Confidence Intervals Correctly</a></h3>
      <p>Coverage meaning, wrong wording, and how CI width communicates precision.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/interpreting-confidence-intervals/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 4 -->
    <div class="card lesson-card">
      <h3><a href="/inference/interpretation-reporting/interpreting-effect-sizes/">4. Interpreting Effect Sizes</a></h3>
      <p>Effect size families (difference, ratio, standardized) and how to explain magnitude.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/interpreting-effect-sizes/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 5 -->
    <div class="card lesson-card">
      <h3><a href="/inference/interpretation-reporting/multiple-testing-and-false-positives/">5. Multiple Testing and False Positives</a></h3>
      <p>Why multiple comparisons inflate false discoveries and what adjustments mean conceptually.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/multiple-testing-and-false-positives/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 6 -->
    <div class="card lesson-card">
      <h3><a href="/inference/interpretation-reporting/reporting-results-clear-language/">6. Reporting Results in Clear Language</a></h3>
      <p>Templates for correct reporting: what to include, what to avoid, and how to write honest conclusions.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/reporting-results-clear-language/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 7 -->
    <div class="card lesson-card">
      <h3><a href="/inference/interpretation-reporting/tables-figures-and-visual-communication/">7. Tables, Figures, and Visual Communication</a></h3>
      <p>How to present inference results visually: CI plots, effect plots, and common visualization traps.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/tables-figures-and-visual-communication/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 8 -->
    <div class="card lesson-card">
      <h3><a href="/inference/interpretation-reporting/reproducibility-and-analysis-checklist/">8. Reproducibility and an Analysis Checklist</a></h3>
      <p>A practical checklist: assumptions, sensitivity, documentation, and reproducible reporting habits.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/reproducibility-and-analysis-checklist/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 6</h2>
      <ul class="bullets">
        <li>Interpret p-values and CIs correctly using precise language</li>
        <li>Separate statistical significance from practical importance</li>
        <li>Report effect sizes and uncertainty clearly</li>
        <li>Avoid common reporting traps and improve reproducibility</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/assumptions-robustness/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 7 — Assumptions & Robustness</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading Script (lesson-level) -->
<script>
  (function () {
    var KEY = "esa_continue_inference_interpretation_reporting_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block6");
      var label = document.getElementById("continue-reading-block6-label");
      var btn = document.getElementById("continue-reading-block6-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>