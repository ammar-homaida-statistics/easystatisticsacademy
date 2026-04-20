---
layout: default
title: Block 3 — Assumptions & Validity
permalink: /applied-statistics/assumptions/
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
        This block explains why statistical methods rely on assumptions,
        how to evaluate them, and what happens when they are violated.
        Understanding assumptions is essential for valid conclusions.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_applied_last_block_v0", JSON.stringify({
    url: "/applied-statistics/assumptions/",
    label: "Block 3 — Assumptions & Validity",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Assumptions</span>
        <span class="badge">Validity</span>
        <span class="badge">Checks</span>
      </div>

      <h1>Block 3 — Assumptions & Validity</h1>

      <p class="lead">
        Statistical methods are not universally valid—they depend on assumptions.
        This block explains what assumptions are, why they matter, and how they affect
        interpretation and reliability of results.
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

          <li><strong>What assumptions are</strong><span class="meta">Conditions behind methods</span></li>
          <li><strong>Why they matter</strong><span class="meta">Impact on validity</span></li>
          <li><strong>Common assumptions</strong><span class="meta">Normality, independence, variance</span></li>
          <li><strong>Violations</strong><span class="meta">What goes wrong</span></li>
          <li><strong>Practical checking</strong><span class="meta">Conceptual diagnostics</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-assumptions" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-assumptions-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-assumptions-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons are designed to build a correct understanding of assumptions
      and their role in statistical reasoning.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/assumptions/what-are-assumptions/">1. What Are Statistical Assumptions?</a></h3>
      <p>Understand assumptions as conditions required for methods to work correctly.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/assumptions/what-are-assumptions/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/assumptions/why-assumptions-matter/">2. Why Assumptions Matter</a></h3>
      <p>Learn how violations affect results and conclusions.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/assumptions/why-assumptions-matter/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/assumptions/common-assumptions/">3. Common Assumptions in Practice</a></h3>
      <p>Normality, independence, and equal variance explained conceptually.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/assumptions/common-assumptions/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/assumptions/violations/">4. What Happens When Assumptions Fail?</a></h3>
      <p>Understand the consequences of violating assumptions.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/assumptions/violations/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/assumptions/checking/">5. How to Check Assumptions Conceptually</a></h3>
      <p>Learn practical and conceptual ways to assess assumptions.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/assumptions/checking/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 3</h2>
      <ul class="bullets">
        <li>Understand what statistical assumptions are</li>
        <li>Explain why assumptions matter for validity</li>
        <li>Recognize common assumptions in applied work</li>
        <li>Identify consequences of violations</li>
        <li>Conceptually assess whether assumptions hold</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/applied-statistics/effect-sizes/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 4 — Effect Sizes & Interpretation</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_applied_assumptions_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-assumptions");
    var label = document.getElementById("continue-reading-assumptions-label");
    var btn = document.getElementById("continue-reading-assumptions-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>