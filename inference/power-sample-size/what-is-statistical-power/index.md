---
layout: default
title: "1. What Is Statistical Power?"
description: "Define statistical power formally as 1 − beta and understand its connection to Type II error and detectability."
permalink: /inference/power-sample-size/what-is-statistical-power/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the formal definition of statistical power
        and its role in study planning.
        Numerical examples and software illustrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_power_sample_size_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/power-sample-size/what-is-statistical-power/",
      label: "Lesson 1 — What Is Statistical Power?",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/power-sample-size/",
      label: "Block 5 — Power & Sample Size",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Power</span>
        <span class="badge">1 − β</span>
      </div>

      <h1>1. What Is Statistical Power?</h1>

      <p class="lead">
        Statistical power is the probability that a test
        correctly rejects a false null hypothesis.
        It quantifies a study’s ability to detect real effects.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/power-sample-size/">Back to Block 5</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Power complements Type I and Type II error control.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define statistical power formally,
      relate it to Type II error,
      and understand why it is essential for study design.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Formal definition</h2>
      <p style="margin:0;">
        \[
        \text{Power} = P(\text{Reject } H_0 \mid H_1 \text{ is true})
        \]
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Connection to Type II error</h2>
  </div>

  <div class="card">
    Type II error probability:
    \[
    \beta = P(\text{Fail to reject } H_0 \mid H_1 \text{ is true})
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Therefore:
    \[
    \text{Power} = 1 - \beta
    \]
  </div>

  <p class="muted-mini">
    High power implies low probability of missing a real effect.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Why power matters</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Scientific reliability</h3>
      <p>
        Low power increases false negatives
        and reduces reproducibility.
      </p>
    </div>

    <div class="card">
      <h3>Ethical responsibility</h3>
      <p>
        Underpowered studies waste resources
        and may expose participants without benefit.
      </p>
    </div>

    <div class="card">
      <h3>Study planning</h3>
      <p>
        Power determines required sample size.
      </p>
    </div>

    <div class="card">
      <h3>Interpretation</h3>
      <p>
        A non-significant result in a low-power study
        provides weak evidence.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) What affects power?</h2>
  </div>

  <div class="card">
    Power depends on:
    <br><br>
    • Significance level alpha  
    • Sample size n  
    • Effect size  
    • Population variability  
  </div>

  <p class="muted-mini">
    Increasing n or effect size increases power.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define statistical power formally</li>
        <li>Understand the relation power = 1 − beta</li>
        <li>Explain why low power is problematic</li>
        <li>Identify main determinants of power</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now distinguish detectability from practical importance
        using effect size.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/power-sample-size/effect-size-and-practical-importance/">
          Next lesson: 2. Effect Size & Practical Importance →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Block overview</div>
        <div class="mini-body">
          <a href="/inference/power-sample-size/" style="color:#1a73e8; text-decoration:underline;">
            Block 5 — Power & Sample Size
          </a>
        </div>
      </div>
    </div>
  </div>
</section>