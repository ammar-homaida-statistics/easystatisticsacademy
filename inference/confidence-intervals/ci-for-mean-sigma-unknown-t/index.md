---
layout: default
title: "5. CI for a Mean (σ Unknown): t-Interval"
description: "Construct a confidence interval for the population mean when σ is unknown using the t distribution, sample standard deviation s, and degrees of freedom n−1."
permalink: /inference/confidence-intervals/ci-for-mean-sigma-unknown-t/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 locks the t-interval structure. Worked examples and software outputs will be added later.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/",
      label: "Lesson 5 — CI for a Mean (σ Unknown): t-Interval",
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
        <span class="badge">Lesson 5</span>
        <span class="badge">Mean</span>
        <span class="badge">t-interval</span>
      </div>

      <h1>5. CI for a Mean (σ Unknown): t-Interval</h1>
      <p class="lead">
        In practice \(\sigma\) is unknown. We replace it with \(s\) and use a t critical value:
        \(\bar{X} \pm t^\*_{n-1}\, s/\sqrt{n}\).
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
        Next we formalize the <strong>conditions</strong> that make CIs valid.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/conditions-normality-clt-independence/">
          Next lesson: 6. Conditions for Valid CIs →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/ci-for-mean-sigma-known-z/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: z-Interval
          </a>
        </div>
      </div>
    </div>
  </div>
</section>