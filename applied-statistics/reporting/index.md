---
layout: default
title: Block 6 — Reporting Results
permalink: /applied-statistics/reporting/
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
        This block focuses on how to communicate statistical results clearly and correctly.
        Proper reporting ensures that findings are understandable, accurate, and reproducible.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_applied_last_block_v0", JSON.stringify({
    url: "/applied-statistics/reporting/",
    label: "Block 6 — Reporting Results",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Reporting</span>
        <span class="badge">Communication</span>
        <span class="badge">Clarity</span>
      </div>

      <h1>Block 6 — Reporting Results</h1>

      <p class="lead">
        Statistical results must be communicated clearly and correctly.
        This block teaches how to present findings using proper language,
        tables, and figures, ensuring results are interpretable and reliable.
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

          <li><strong>Statistical language</strong><span class="meta">Clear and precise wording</span></li>
          <li><strong>Tables</strong><span class="meta">Structured presentation of results</span></li>
          <li><strong>Figures</strong><span class="meta">Visual communication of data</span></li>
          <li><strong>Effect sizes</strong><span class="meta">Reporting magnitude, not just significance</span></li>
          <li><strong>Transparency</strong><span class="meta">Reproducibility and clarity</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-reporting" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-reporting-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-reporting-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons focus on communicating statistical findings in a clear,
      correct, and professional way.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/reporting/statements/">1. Writing Statistical Statements</a></h3>
      <p>Learn how to report results using correct statistical language.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/reporting/statements/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/reporting/tables/">2. Presenting Results in Tables</a></h3>
      <p>Structure tables to communicate results clearly and efficiently.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/reporting/tables/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/reporting/figures/">3. Presenting Results in Figures</a></h3>
      <p>Use graphs and charts to support interpretation of findings.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/reporting/figures/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/reporting/effect-sizes/">4. Reporting Effect Sizes and Confidence Intervals</a></h3>
      <p>Report magnitude and uncertainty, not just significance.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/reporting/effect-sizes/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/reporting/transparency/">5. Transparency and Reproducibility</a></h3>
      <p>Ensure results can be understood, verified, and replicated.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/reporting/transparency/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 6</h2>
      <ul class="bullets">
        <li>Write clear and correct statistical statements</li>
        <li>Present results using tables and figures effectively</li>
        <li>Report effect sizes and uncertainty properly</li>
        <li>Communicate findings in a professional way</li>
        <li>Ensure transparency and reproducibility</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/applied-statistics/practice/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 7 — From Analysis to Practice</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_applied_reporting_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-reporting");
    var label = document.getElementById("continue-reading-reporting-label");
    var btn = document.getElementById("continue-reading-reporting-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>