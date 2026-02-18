---
layout: default
title: "1. Linearity of Expectation"
description: "A core rule that makes expectations easy: E[aX+b]=aE[X]+b and E[X+Y]=E[X]+E[Y] (no independence required)."
permalink: /probability/expectation-variability/linearity-of-expectation/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow.
        Examples, graphs, and software demonstrations will be added later without changing the lesson order.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 4 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_expectation_variability_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/expectation-variability/linearity-of-expectation/",
      label: "Lesson 1 — Linearity of Expectation",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Expectation</span>
        <span class="badge">Linearity</span>
      </div>

      <h1>1. Linearity of Expectation</h1>

      <p class="lead">
        Linearity is the most powerful expectation rule: it simplifies complex random quantities into sums of
        simple expectations — and it works even when variables are not independent.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/expectation-variability/">Back to Block 4</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Version 0: structure first. Examples and software demos will be added later.
      </p>

    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we move from expectation to variability and learn how variance behaves under transformations and sums.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/expectation-variability/variance-rules-and-sums/">
          Next lesson: 2. Variance Rules & Sums →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/random-variables/variance-and-standard-deviation/" style="color:#1a73e8; text-decoration:underline;">
            Block 3 — Lesson 6: Variance & Standard Deviation
          </a>
        </div>
      </div>
    </div>
  </div>
</section>