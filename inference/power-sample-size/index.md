<!-- =========================================================
BLOCK 5 — POWER & SAMPLE SIZE
File: /inference/power-sample-size/index.md
========================================================= -->
---
layout: default
title: Block 5 — Power & Sample Size
description: Study planning for reliability: power, effect size, Type II error, sample size logic, and practical design decisions.
permalink: /inference/power-sample-size/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block explains <strong>power</strong> and <strong>sample size</strong> as design tools.
        It shifts thinking from “Is it significant?” to “Is the study capable of detecting meaningful effects reliably?”
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/power-sample-size/",
      label: "Block 5 — Power & Sample Size",
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
        <span class="badge">Effect size</span>
        <span class="badge">Planning</span>
      </div>

      <h1>Block 5 — Power &amp; Sample Size</h1>
      <p class="lead">
        Power analysis is the reliability side of inference. This block explains the roles of \(\alpha\), \(\beta\),
        effect size, variability, and sample size—so studies are planned to detect meaningful signals, not just compute p-values.
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
          <li style="margin:.35rem 0;"><strong>Power meaning</strong><span class="meta">Detection probability under H1</span></li>
          <li style="margin:.35rem 0;"><strong>Type II error</strong><span class="meta">False negative risk</span></li>
          <li style="margin:.35rem 0;"><strong>Effect size</strong><span class="meta">Magnitude worth detecting</span></li>
          <li style="margin:.35rem 0;"><strong>Sample size</strong><span class="meta">Precision and detectability</span></li>
          <li style="margin:.35rem 0;"><strong>Tradeoffs</strong><span class="meta">\(\alpha\) vs \(\beta\) vs cost</span></li>
          <li style="margin:.35rem 0;"><strong>Common mistakes</strong><span class="meta">Post-hoc power, rules of thumb</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="continue-reading-block5" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block5-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block5-btn" href="#">Continue</a>
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
      <p>Power/sample size workflows (SPSS/R/Python/Excel) will be added later.</p>
      <div class="pill-row"><span class="badge">Planned</span></div>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 5</h2>
      <ul class="bullets">
        <li>Explain power as detection probability under the alternative</li>
        <li>Connect effect size, variability, and sample size</li>
        <li>Plan studies for reliability rather than “significance hunting”</li>
        <li>Avoid common misuse (especially post-hoc power)</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/interpretation-reporting/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 6 — Interpretation & Reporting</strong>
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