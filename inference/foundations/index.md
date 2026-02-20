---
layout: default
title: "Inference Foundations"
description: Parameters vs statistics, estimators, standard error, and the core logic of inference.
permalink: /inference/foundations/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:1.25rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin:0 0 .35rem 0; color:#e65100;">🚧 Under Construction</h2>
      <p style="margin:0; color:#5d4037; line-height:1.6;">
        This block is being built lesson-by-lesson. The structure is permanent; content will expand without changing URLs.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Estimation</span>
        <span class="badge">Uncertainty</span>
        <span class="badge">Standard error</span>
      </div>

      <h1>Block 1 — Inference Foundations</h1>
      <p class="lead">
        Build the core concepts behind inference: parameters vs statistics, estimators, sampling variability,
        standard error, and why inference is reasoning—not a calculator output.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">← Back to Inference</a>
        <a class="btn" href="/inference/confidence-intervals/">Next block: Confidence Intervals →</a>
      </div>

      <p class="muted-mini">
        Continue Reading will remember the last block you visited in Statistical Inference.
      </p>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons</h2>
    <p>Placeholders for now. Lessons will become clickable when published.</p>
  </div>

  <div class="grid grid-2">
    <div class="card lesson-card">
      <h3>What is inference?</h3>
      <p>Population vs sample, uncertainty, and why we need inference.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <div class="card lesson-card">
      <h3>Parameters, statistics, estimators</h3>
      <p>What we want to know vs what we can compute.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <div class="card lesson-card">
      <h3>Standard error intuition</h3>
      <p>Sampling variability and why “n” changes reliability.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <div class="card lesson-card">
      <h3>Bias vs variance (intuition)</h3>
      <p>Accuracy vs stability and why tradeoffs matter.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Block goal</h2>
      <ul class="bullets">
        <li>Understand inference as uncertainty-aware reasoning</li>
        <li>Separate parameters from statistics</li>
        <li>Build intuition for standard error</li>
      </ul>
    </div>
    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Next block</div>
        <div class="mini-body">Confidence Intervals</div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    // ✅ Set "Continue reading" to this Inference BLOCK
    var KEY = "esa_continue_inference_last_block_v0";
    var data = {
      url: "/inference/foundations/",
      label: "Block 1 — Inference Foundations",
      ts: Date.now()
    };
    try { localStorage.setItem(KEY, JSON.stringify(data)); } catch (e) {}
  })();
</script>