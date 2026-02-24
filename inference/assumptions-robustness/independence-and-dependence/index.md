---
layout: default
title: "4. Independence and Dependence"
description: "Why independence matters for standard errors, how dependence arises (clusters, time), and why naive inference can fail."
permalink: /inference/assumptions-robustness/independence-and-dependence/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; color:#5d4037; line-height:1.6;">
        Version 0 locks dependence concepts (clusters/time/order) and why SEs break under dependence.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/independence-and-dependence/",
      label: "Lesson 4 — Independence and Dependence",
      ts: Date.now()
    }));
    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/assumptions-robustness/",
      label: "Block 7 — Assumptions & Robustness",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="badge-row">
      <span class="badge">Block 7</span>
      <span class="badge">Lesson 4</span>
      <span class="badge">Independence</span>
      <span class="badge">Dependence</span>
    </div>

    <h1>4. Independence and Dependence</h1>
    <p class="lead">
      Most inference formulas assume independence.
      This lesson explains how dependence changes variability and invalidates standard errors.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/inference/assumptions-robustness/">Back to Block 7</a>
      <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">Next we study unequal variance patterns (heteroscedasticity).</p>
      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/assumptions-robustness/heteroscedasticity-variance-issues/">
          Next lesson: 5. Heteroscedasticity →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/assumptions-robustness/checking-normality-what-and-why/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Checking Normality
          </a>
        </div>
      </div>
    </div>

  </div>
</section>