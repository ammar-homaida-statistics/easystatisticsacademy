---
layout: default
title: Block 2 — Study Design & Data Context
permalink: /applied-statistics/study-design/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; line-height:1.6;">
        This block explains how study design shapes statistical conclusions.
        It introduces how data is generated, the difference between observational and experimental studies,
        and why correct interpretation depends on design.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_applied_last_block_v0", JSON.stringify({
    url: "/applied-statistics/study-design/",
    label: "Block 2 — Study Design & Data Context",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Design</span>
        <span class="badge">Studies</span>
        <span class="badge">Context</span>
      </div>

      <h1>Block 2 — Study Design & Data Context</h1>

      <p class="lead">
        Applied statistics depends on how data is collected.
        This block shows how different study designs influence what conclusions are valid,
        and why statistical reasoning begins before analysis.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/applied-statistics/">Back to Applied Statistics</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Content will expand without changing URLs.
      </p>

    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0;">

          <li><strong>Study types</strong><span class="meta">Experimental vs observational</span></li>
          <li><strong>Sampling</strong><span class="meta">How data represents populations</span></li>
          <li><strong>Bias</strong><span class="meta">Systematic errors in data collection</span></li>
          <li><strong>Confounding</strong><span class="meta">Hidden variables affecting results</span></li>
          <li><strong>Interpretation limits</strong><span class="meta">What design allows you to conclude</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-study-design" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-study-design-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-study-design-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons are organized to build correct understanding of how data context determines valid conclusions.
      This structure will not change.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/study-design/experimental-vs-observational/">1. Experimental vs Observational Studies</a></h3>
      <p>Understand the difference between intervention-based and observational data.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/study-design/experimental-vs-observational/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/study-design/common-designs/">2. Common Study Designs</a></h3>
      <p>Learn cross-sectional, cohort, case-control, and experimental designs conceptually.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/study-design/common-designs/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/study-design/sampling-representativeness/">3. Sampling and Representativeness</a></h3>
      <p>Understand how sampling affects generalization to populations.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/study-design/sampling-representativeness/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/study-design/bias-confounding/">4. Bias and Confounding</a></h3>
      <p>Identify common sources of bias and understand confounding effects.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/study-design/bias-confounding/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/study-design/design-and-conclusions/">5. What Study Design Allows You to Conclude</a></h3>
      <p>Understand the limits of interpretation based on study structure.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/study-design/design-and-conclusions/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 2</h2>
      <ul class="bullets">
        <li>Distinguish experimental and observational designs</li>
        <li>Understand major study types</li>
        <li>Recognize sampling and representativeness issues</li>
        <li>Identify bias and confounding</li>
        <li>Interpret results in context of study design</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/applied-statistics/assumptions/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 3 — Assumptions & Validity</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_applied_study-design_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-study-design");
    var label = document.getElementById("continue-reading-study-design-label");
    var btn = document.getElementById("continue-reading-study-design-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>