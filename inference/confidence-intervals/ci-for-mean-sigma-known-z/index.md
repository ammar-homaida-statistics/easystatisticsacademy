---
layout: default
title: "4. CI for a Mean (σ Known): z-Interval"
description: "Construct a confidence interval for the population mean when σ is known, using the Normal (z) critical value and the standard error σ/√n."
permalink: /inference/confidence-intervals/ci-for-mean-sigma-known-z/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 locks the z-interval structure. Fully worked numeric examples will be added later.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/ci-for-mean-sigma-known-z/",
      label: "Lesson 4 — CI for a Mean (σ Known): z-Interval",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/confidence-intervals/",
      label: "Block 2 — Confidence Intervals",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">Mean</span>
        <span class="badge">z-interval</span>
      </div>

      <h1>4. CI for a Mean (σ Known): z-Interval</h1>
      <p class="lead">
        This interval clarifies the clean CI logic when the population standard deviation \(\sigma\) is known:
        \(\bar{X} \pm z^\* \, \sigma/\sqrt{n}\).
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Inference home</a>
      </div>

      <p class="muted-mini">Version 0: structure first. Examples later.</p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next we handle the real-world case: \(\sigma\) unknown → <strong>t-interval</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/">
          Next lesson: 5. CI for Mean (σ Unknown) →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/critical-values-z-and-t/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Critical Values
          </a>
        </div>
      </div>
    </div>
  </div>
</section>