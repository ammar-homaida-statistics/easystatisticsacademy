---
layout: default
title: "8. CI for Difference of Means (Independent Samples)"
description: "Construct a confidence interval for μ1−μ2 using two independent samples. Understand the standard error and the Welch (unequal variance) default."
permalink: /inference/confidence-intervals/ci-for-difference-of-means-independent/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 locks the two-sample mean CI structure. Welch vs pooled details will expand later.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/ci-for-difference-of-means-independent/",
      label: "Lesson 8 — CI for Difference of Means (Independent Samples)",
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
        <span class="badge">Lesson 8</span>
        <span class="badge">Two means</span>
        <span class="badge">Welch</span>
      </div>

      <h1>8. CI for Difference of Means (Independent Samples)</h1>
      <p class="lead">
        Compare two group means by estimating \(\mu_1-\mu_2\) and quantifying uncertainty
        through the standard error of \(\bar{X}_1-\bar{X}_2\).
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
        Next we compare <strong>two proportions</strong> with a CI for \(p_1-p_2\).
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/ci-for-difference-of-proportions/">
          Next lesson: 9. CI for Difference of Proportions →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/ci-for-proportion/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 7: CI for a Proportion
          </a>
        </div>
      </div>
    </div>
  </div>
</section>