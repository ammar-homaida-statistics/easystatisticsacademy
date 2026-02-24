---
layout: default
title: "3. Power Curves and Trade-offs"
description: "Understand how power changes with sample size, effect size, variability, and α. Learn the core design trade-offs."
permalink: /inference/power-sample-size/power-curve-and-tradeoffs/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 fixes the conceptual geometry of power curves. Plots and numeric examples will be added later.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_power_sample_size_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/power-sample-size/power-curve-and-tradeoffs/",
      label: "Lesson 3 — Power Curves and Trade-offs",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/power-sample-size/",
      label: "Block 5 — Power and Sample Size",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">Trade-offs</span>
        <span class="badge">Design</span>
      </div>

      <h1>3. Power Curves and Trade-offs</h1>
      <p class="lead">
        Power is not a fixed property of a test — it depends on the design.
        This lesson shows how α, n, effect size, and variability jointly determine power.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/power-sample-size/">Back to Block 5</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">Version 0: shape and logic first.</p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">Next we compute required sample size for a mean difference.</p>
      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/power-sample-size/sample-size-for-mean/">
          Next lesson: 4. Sample Size for a Mean →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/power-sample-size/effect-size-and-practical-importance/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Effect Size and Practical Importance
          </a>
        </div>
      </div>
    </div>
  </div>
</section>