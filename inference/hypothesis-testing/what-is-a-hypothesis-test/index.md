---
layout: default
title: "1. What Is a Hypothesis Test?"
description: "Understand hypothesis testing as a decision procedure: null model, evidence, and how tests formalize conclusions under uncertainty."
permalink: /inference/hypothesis-testing/what-is-a-hypothesis-test/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the lesson structure. Examples, visuals, and software workflows will be added later.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/what-is-a-hypothesis-test/",
      label: "Lesson 1 — What Is a Hypothesis Test?",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/hypothesis-testing/",
      label: "Block 3 — Hypothesis Testing",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Testing</span>
        <span class="badge">Decision</span>
      </div>

      <h1>1. What Is a Hypothesis Test?</h1>
      <p class="lead">
        A hypothesis test is a formal rule for deciding whether data are compatible with a null model.
        This lesson introduces the testing mindset before any formulas.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Back to Block 3</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">Version 0: structure first. Examples and computations later.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>Define hypothesis testing as a decision procedure and identify its core ingredients (H₀, statistic, p-value, rule).</p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Version 0 focus</h2>
      <p style="margin:0;">Conceptual structure: what a test is, what it tries to answer, and what “evidence against H₀” means.</p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">Next we define the null and alternative hypotheses properly.</p>
      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/hypothesis-testing/null-and-alternative/">
          Next lesson: 2. Null and Alternative Hypotheses →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Block page</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/" style="color:#1a73e8; text-decoration:underline;">
            Back to Block 3 structure
          </a>
        </div>
      </div>
    </div>
  </div>
</section>