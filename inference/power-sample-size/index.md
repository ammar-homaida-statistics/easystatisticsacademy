<!-- =========================================================
BLOCK 5 — POWER AND SAMPLE SIZE
File: /inference/power-sample-size/index.md
========================================================= -->
---
layout: default
title: Block 5 — Power and Sample Size
description: Learn how statistical power works, how sample size determines precision and detectability, and how to plan studies responsibly.
permalink: /inference/power-sample-size/
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
        This block explains how statistical power works, how sample size controls
        detectability and precision, and how to design studies responsibly before collecting data.
      </p>
    </div>
  </div>
</section>

<!-- Update last visited block -->
<script>
(function () {
  var KEY = "esa_continue_inference_last_block_v0";
  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/power-sample-size/",
    label: "Block 5 — Power and Sample Size",
    ts: Date.now()
  }));
})();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Power</span>
        <span class="badge">Sample Size</span>
        <span class="badge">Planning</span>
      </div>

      <h1>Block 5 — Power and Sample Size</h1>

      <p class="lead">
        Power analysis moves inference from reactive to proactive.
        Instead of asking “Is it significant?”, we ask:
        “Is the study capable of detecting what matters?”
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">Back to Statistical Inference</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure locked. Mathematical derivations and software tools added later.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Power definition</strong><span class="meta">1 − β</span></li>
          <li style="margin:.35rem 0;"><strong>Effect size</strong><span class="meta">Practical magnitude</span></li>
          <li style="margin:.35rem 0;"><strong>Sample size formulas</strong><span class="meta">Means & proportions</span></li>
          <li style="margin:.35rem 0;"><strong>Trade-offs</strong><span class="meta">α, β, effect size, n</span></li>
          <li style="margin:.35rem 0;"><strong>Precision planning</strong><span class="meta">Width-based design</span></li>
          <li style="margin:.35rem 0;"><strong>Ethical study design</strong><span class="meta">Underpowered risks</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="continue-reading-block5" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block5-label"></p>
      <a class="btn" id="continue-reading-block5-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons follow a logical progression from definition of power
      to practical study design and ethical considerations.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/inference/power-sample-size/what-is-statistical-power/">1. What Is Statistical Power?</a></h3>
      <p>Define power formally as 1 − β and connect it to Type II error.</p>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/power-sample-size/effect-size-and-practical-importance/">2. Effect Size and Practical Importance</a></h3>
      <p>Distinguish detectability from meaningful magnitude.</p>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/power-sample-size/power-curve-and-tradeoffs/">3. Power Curves and Trade-offs</a></h3>
      <p>How α, n, and effect size shift the rejection region.</p>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/power-sample-size/sample-size-for-mean/">4. Sample Size for a Mean</a></h3>
      <p>Deriving required n for detecting a mean difference.</p>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/power-sample-size/sample-size-for-proportion/">5. Sample Size for a Proportion</a></h3>
      <p>Planning n for detecting differences in rates.</p>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/power-sample-size/precision-vs-detectability/">6. Precision vs Detectability</a></h3>
      <p>Interval-width planning versus hypothesis-testing planning.</p>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/power-sample-size/underpowered-studies/">7. The Risk of Underpowered Studies</a></h3>
      <p>False negatives, unstable estimates, and reproducibility.</p>
    </div>

    <div class="card lesson-card">
      <h3><a href="/inference/power-sample-size/software-and-power-analysis/">8. Software and Practical Power Analysis</a></h3>
      <p>R, Python, SPSS, and online tools for power calculations.</p>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 5</h2>
      <ul class="bullets">
        <li>Define statistical power precisely</li>
        <li>Explain effect size vs significance</li>
        <li>Plan required sample sizes</li>
        <li>Understand ethical implications of underpowered research</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/interpretation-reporting/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 6 — Interpretation and Reporting</strong>
          </a>.
        </div>
      </div>
    </div>
  </div>
</section>

<script>
(function () {
  var KEY = "esa_continue_inference_power_sample_size_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-block5");
    var label = document.getElementById("continue-reading-block5-label");
    var btn = document.getElementById("continue-reading-block5-btn");
    if (!wrap || !label || !btn) return;

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";
  } catch (e) {}
})();
</script>