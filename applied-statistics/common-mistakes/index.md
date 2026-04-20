---
layout: default
title: Block 5 — Common Mistakes & Pitfalls
permalink: /applied-statistics/common-mistakes/
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
        This block focuses on common mistakes in applied statistics.
        Understanding these errors is essential to avoid incorrect conclusions
        and misuse of statistical methods.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_applied_last_block_v0", JSON.stringify({
    url: "/applied-statistics/common-mistakes/",
    label: "Block 5 — Common Mistakes & Pitfalls",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Mistakes</span>
        <span class="badge">Pitfalls</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>Block 5 — Common Mistakes & Pitfalls</h1>

      <p class="lead">
        Applied statistics is often misused through incorrect interpretation,
        inappropriate methods, and misunderstanding of results.
        This block helps identify and avoid the most common errors.
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

          <li><strong>Misuse of tests</strong><span class="meta">Wrong method selection</span></li>
          <li><strong>P-values misuse</strong><span class="meta">Misinterpretation of significance</span></li>
          <li><strong>Multiple comparisons</strong><span class="meta">Inflated false positives</span></li>
          <li><strong>Non-significant results</strong><span class="meta">Incorrect conclusions</span></li>
          <li><strong>Overinterpretation</strong><span class="meta">Going beyond data</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-common-mistakes" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-common-mistakes-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-common-mistakes-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons focus on identifying and correcting common errors in applied statistical work.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/common-mistakes/wrong-test/">1. Choosing the Wrong Statistical Test</a></h3>
      <p>Understand how incorrect method selection leads to invalid results.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/common-mistakes/wrong-test/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/common-mistakes/pvalues/">2. Misinterpreting P-values</a></h3>
      <p>Clarify what p-values do and do not mean.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/common-mistakes/pvalues/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/common-mistakes/multiple-testing/">3. Multiple Comparisons Problem</a></h3>
      <p>Understand why repeated testing increases false positives.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/common-mistakes/multiple-testing/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/common-mistakes/non-significant/">4. Misinterpreting Non-Significant Results</a></h3>
      <p>Learn why "not significant" does not mean "no effect".</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/common-mistakes/non-significant/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/common-mistakes/overinterpretation/">5. Overinterpretation of Results</a></h3>
      <p>Avoid drawing conclusions beyond what the data supports.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/common-mistakes/overinterpretation/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 5</h2>
      <ul class="bullets">
        <li>Recognize common statistical mistakes</li>
        <li>Avoid misuse of statistical tests</li>
        <li>Interpret p-values correctly</li>
        <li>Understand risks of multiple testing</li>
        <li>Draw conclusions responsibly</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/applied-statistics/reporting/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 6 — Reporting Results</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_applied_common-mistakes_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-common-mistakes");
    var label = document.getElementById("continue-reading-common-mistakes-label");
    var btn = document.getElementById("continue-reading-common-mistakes-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>