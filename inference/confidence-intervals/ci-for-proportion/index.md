---
layout: default
title: "7. Confidence Interval for a Proportion"
description: "Build a confidence interval for a population proportion p using the standard error of p-hat and the success–failure condition."
permalink: /inference/confidence-intervals/ci-for-proportion/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 locks the proportion CI structure. Worked examples and real interpretation come later.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/ci-for-proportion/",
      label: "Lesson 7 — Confidence Interval for a Proportion",
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
        <span class="badge">Lesson 7</span>
        <span class="badge">Proportion</span>
        <span class="badge">SE</span>
      </div>

      <h1>7. Confidence Interval for a Proportion</h1>
      <p class="lead">
        For a population proportion \(p\), we estimate uncertainty using
        \(SE(\hat{p})=\sqrt{\hat{p}(1-\hat{p})/n}\).
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Inference home</a>
      </div>

      <p class="muted-mini">Version 0: structure first.</p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next we compare <strong>two independent means</strong> with a CI for \(\mu_1-\mu_2\).
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">
          Next lesson: 8. CI for Difference of Means →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/conditions-normality-clt-independence/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 6: Conditions for Valid CIs
          </a>
        </div>
      </div>
    </div>
  </div>
</section>