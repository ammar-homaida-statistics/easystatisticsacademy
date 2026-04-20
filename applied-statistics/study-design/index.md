---
layout: default
title: Block 2 — Study Design & Data Context
permalink: /applied-statistics/study-design/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="margin-top:0; color:#e65100;">🚧 This Block Is Under Construction</h2>
    <p>Understanding how data is generated is essential for correct statistical conclusions.</p>
  </div>
</section>

<script>
(function () {
  localStorage.setItem("esa_continue_applied_last_block_v0", JSON.stringify({
    url: "/applied-statistics/study-design/",
    label: "Block 2 — Study Design & Data Context",
    ts: Date.now()
  }));
})();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Design</span>
        <span class="badge">Data</span>
      </div>

      <h1>Block 2 — Study Design & Data Context</h1>

      <p class="lead">
        Statistical results depend on how data is collected.
        This block explains study designs and their implications.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/applied-statistics/">Back</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2>What this block covers</h2>
        <ul class="quickstart">
          <li>Experimental vs observational</li>
          <li>Sampling methods</li>
          <li>Bias and confounding</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="continue-reading-study-design" style="display:none;" class="section">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-study-design-label"></p>
    <a id="continue-reading-study-design-btn" class="btn">Continue</a>
  </div>
</section>

<section class="section" id="lessons">
  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/study-design/experimental-vs-observational/">1. Experimental vs Observational</a></h3>
      <p>Understand causal vs non-causal designs.</p>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/study-design/sampling/">2. Sampling Methods</a></h3>
      <p>How samples represent populations.</p>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/study-design/bias/">3. Bias in Studies</a></h3>
      <p>Selection, measurement, and survivorship bias.</p>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/study-design/confounding/">4. Confounding Variables</a></h3>
      <p>Hidden variables affecting results.</p>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/study-design/design-interpretation/">5. Design and Interpretation</a></h3>
      <p>Why design determines validity.</p>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <h2>Outcome</h2>
    <ul class="bullets">
      <li>Understand study types</li>
      <li>Recognize bias and confounding</li>
      <li>Interpret results in context</li>
    </ul>
  </div>
</section>

<script>
(function () {
  var KEY = "esa_continue_applied_study-design_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  var data = JSON.parse(raw);
  document.getElementById("continue-reading-study-design-label").innerHTML =
    'You last visited: <strong>' + data.label + '</strong>';
  document.getElementById("continue-reading-study-design-btn").href = data.url;
  document.getElementById("continue-reading-study-design").style.display = "block";
})();
</script>