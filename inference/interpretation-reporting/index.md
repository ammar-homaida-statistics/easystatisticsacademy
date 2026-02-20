<!-- =========================================================
BLOCK 6 — INTERPRETATION & REPORTING
File: /inference/interpretation-reporting/index.md
========================================================= -->
---
layout: default
title: Block 6 — Interpretation & Reporting
description: Turn statistical outputs into correct conclusions: effect sizes, uncertainty, evidence, and reporting language.
permalink: /inference/interpretation-reporting/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block focuses on the most important skill in applied inference: correct interpretation.
        It teaches how to report results using effect size + uncertainty + context, and avoid misleading conclusions.
      </p>
    </div>
  </div>
</section>

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
        <span class="badge">Effect</span>
        <span class="badge">Uncertainty</span>
        <span class="badge">Reporting</span>
      </div>

      <h1>Block 6 — Interpretation &amp; Reporting</h1>
      <p class="lead">
        Inference is only useful if conclusions are correct.
        This block teaches how to read statistical output (CI, p-values, effect sizes) and translate it into clear,
        valid statements—without overstating evidence or confusing statistical and practical importance.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">Back to Statistical Inference</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will be refined without changing order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Effect vs significance</strong><span class="meta">Magnitude vs detectability</span></li>
          <li style="margin:.35rem 0;"><strong>CI-first interpretation</strong><span class="meta">Precision and importance</span></li>
          <li style="margin:.35rem 0;"><strong>p-values as evidence</strong><span class="meta">Graded evidence, not proof</span></li>
          <li style="margin:.35rem 0;"><strong>Correct sentences</strong><span class="meta">Templates for reporting</span></li>
          <li style="margin:.35rem 0;"><strong>Common mistakes</strong><span class="meta">Overclaiming, “no effect” claims</span></li>
          <li style="margin:.35rem 0;"><strong>Multiple testing preview</strong><span class="meta">Why many tests inflate false positives</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

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
    <p>Lesson links will appear when published. The list and order will remain stable.</p>
  </div>

  <div class="grid grid-2">
    <div class="card lesson-card">
      <h3>Lesson placeholders</h3>
      <p>Coming soon. This area will contain the permanent lesson list for this block.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <div class="card lesson-card">
      <h3>Software examples later</h3>
      <p>We will later map SPSS/R/Python/Excel output into correct reporting language.</p>
      <div class="pill-row"><span class="badge">Planned</span></div>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 6</h2>
      <ul class="bullets">
        <li>Report results with effect + uncertainty + context</li>
        <li>Avoid classic misinterpretations of CIs and p-values</li>
        <li>Use CI width to discuss precision and practical importance</li>
        <li>Write clean, academically correct conclusion statements</li>
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