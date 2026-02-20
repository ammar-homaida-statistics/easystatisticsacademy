<!-- =========================================================
BLOCK 2 — CONFIDENCE INTERVALS
File: /inference/confidence-intervals/index.md
========================================================= -->
---
layout: default
title: Block 2 — Confidence Intervals
description: Learn confidence intervals correctly: meaning, construction logic, precision, and common misconceptions.
permalink: /inference/confidence-intervals/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block teaches <strong>confidence intervals</strong> as an uncertainty statement about estimation methods.
        It focuses on correct interpretation, construction logic, and the errors people make when reading intervals.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/",
      label: "Block 2 — Confidence Intervals",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Intervals</span>
        <span class="badge">Precision</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>Block 2 — Confidence Intervals</h1>
      <p class="lead">
        A confidence interval is not “the probability the parameter is inside.”
        This block explains what confidence means in repeated sampling, how intervals are constructed,
        and how to interpret width, confidence level, and practical importance.
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
          <li style="margin:.35rem 0;"><strong>Meaning of confidence</strong><span class="meta">Method reliability over repeats</span></li>
          <li style="margin:.35rem 0;"><strong>Margin of error</strong><span class="meta">Estimator ± uncertainty</span></li>
          <li style="margin:.35rem 0;"><strong>Width and precision</strong><span class="meta">SE, confidence level, n</span></li>
          <li style="margin:.35rem 0;"><strong>CI vs hypothesis tests</strong><span class="meta">Two views of same logic</span></li>
          <li style="margin:.35rem 0;"><strong>Misconceptions</strong><span class="meta">What a CI does NOT say</span></li>
          <li style="margin:.35rem 0;"><strong>Practical interpretation</strong><span class="meta">Statistical vs practical importance</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="continue-reading-block2" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block2-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block2-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lesson links will appear when published. The list and order will remain stable.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card lesson-card">
      <h3>Lesson placeholders</h3>
      <p>Coming soon. This area will contain the permanent lesson list for this block.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <div class="card lesson-card">
      <h3>Software examples later</h3>
      <p>Interval output interpretation in SPSS / R / Python / Excel will be added later.</p>
      <div class="pill-row"><span class="badge">Planned</span></div>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 2</h2>
      <ul class="bullets">
        <li>Interpret confidence intervals correctly (and avoid classic mistakes)</li>
        <li>Explain the margin-of-error construction logic</li>
        <li>Use CI width to discuss precision and uncertainty</li>
        <li>Connect CI thinking to hypothesis testing</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/hypothesis-testing/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 3 — Hypothesis Testing</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block2");
      var label = document.getElementById("continue-reading-block2-label");
      var btn = document.getElementById("continue-reading-block2-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>