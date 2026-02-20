<!-- =========================================================
BLOCK 7 — ASSUMPTIONS & ROBUSTNESS
File: /inference/assumptions-robustness/index.md
========================================================= -->
---
layout: default
title: Block 7 — Assumptions & Robustness
description: Learn what inference methods assume, how robust they are, how to diagnose violations, and what to do when assumptions fail.
permalink: /inference/assumptions-robustness/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block focuses on assumptions and robustness: when classical inference works, when it breaks,
        how to diagnose problems, and which alternatives are reasonable.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/",
      label: "Block 7 — Assumptions & Robustness",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Assumptions</span>
        <span class="badge">Diagnostics</span>
        <span class="badge">Robustness</span>
      </div>

      <h1>Block 7 — Assumptions &amp; Robustness</h1>
      <p class="lead">
        Inference methods are conditional: they rely on assumptions.
        This block explains the assumptions behind classical procedures, how robust they are,
        how to detect violations, and how to respond (transformations, alternatives, resampling previews).
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
          <li style="margin:.35rem 0;"><strong>Independence</strong><span class="meta">Design and sampling dependence</span></li>
          <li style="margin:.35rem 0;"><strong>Normality</strong><span class="meta">When it matters; robustness intuition</span></li>
          <li style="margin:.35rem 0;"><strong>Equal variance</strong><span class="meta">Homoscedasticity and alternatives</span></li>
          <li style="margin:.35rem 0;"><strong>Outliers</strong><span class="meta">Impact on mean-based inference</span></li>
          <li style="margin:.35rem 0;"><strong>Diagnostics</strong><span class="meta">Checks and practical reasoning</span></li>
          <li style="margin:.35rem 0;"><strong>What to do next</strong><span class="meta">Transformations, nonparametric preview</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="continue-reading-block7" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block7-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block7-btn" href="#">Continue</a>
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
      <p>Diagnostics and robustness workflows will be added in SPSS/R/Python/Excel later.</p>
      <div class="pill-row"><span class="badge">Planned</span></div>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 7</h2>
      <ul class="bullets">
        <li>State the key assumptions behind common inference procedures</li>
        <li>Recognize when results are fragile vs robust</li>
        <li>Use practical diagnostics reasoning</li>
        <li>Choose reasonable alternatives when assumptions fail</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next section</div>
        <div class="mini-body">
          Continue to
          <a href="/modeling/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Statistical Modeling</strong>
          </a>.
        </div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block7");
      var label = document.getElementById("continue-reading-block7-label");
      var btn = document.getElementById("continue-reading-block7-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>