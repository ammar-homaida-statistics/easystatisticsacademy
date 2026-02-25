---
layout: default
title: "6. Precision vs Detectability"
description: "Distinguish planning for estimation precision (confidence intervals) from planning for detectability (power in hypothesis testing)."
permalink: /inference/power-sample-size/precision-vs-detectability/
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
        Version 0 clarifies the conceptual difference between planning for
        narrow confidence intervals and planning for high statistical power.
        Applied examples and simulations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_power_sample_size_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/power-sample-size/precision-vs-detectability/",
      label: "Lesson 6 — Precision vs Detectability",
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
        <span class="badge">Lesson 6</span>
        <span class="badge">Planning</span>
        <span class="badge">Design Logic</span>
      </div>

      <h1>6. Precision vs Detectability</h1>

      <p class="lead">
        Sample size planning can target two different goals:
        <strong>precise estimation</strong> or <strong>detecting an effect</strong>.
        These are related but not identical objectives.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/power-sample-size/">Back to Block 5</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Planning for confidence intervals is not the same as planning for hypothesis tests.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Distinguish between sample size calculations based on
      margin of error (precision) and those based on power (detectability).
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core distinction</h2>
      <p style="margin:0;">
        Precision planning controls <strong>interval width</strong>.  
        Power planning controls <strong>probability of rejection</strong>.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Precision planning (estimation goal)</h2>
  </div>

  <div class="card">
    Confidence interval for a mean:
    \[
    \bar{X}
    \pm
    z_{\alpha/2}
    \frac{\sigma}{\sqrt{n}}
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Margin of error:
    \[
    ME =
    z_{\alpha/2}
    \frac{\sigma}{\sqrt{n}}
    \]
  </div>

  <p>
    Solving for n:
    \[
    n =
    \left(
      \frac{z_{\alpha/2} \sigma}{ME}
    \right)^2
    \]
  </p>

  <p class="muted-mini">
    Here, n is chosen to achieve a desired maximum margin of error.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Detectability planning (testing goal)</h2>
  </div>

  <div class="card">
    Sample size for detecting difference Δ:
    \[
    n =
    \frac{
      (z_{\alpha/2} + z_{\beta})^2 \sigma^2
    }
    {\Delta^2}
    \]
  </div>

  <p>
    Here, n is chosen to ensure:
    \[
    P(\text{Reject } H_0 \mid \text{true difference } = \Delta)
    =
    1 - \beta
    \]
  </p>

  <p class="muted-mini">
    The goal is not narrow intervals — it is high probability of detection.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Key differences</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Precision focus</h3>
      <ul class="bullets">
        <li>Goal: narrow interval</li>
        <li>Depends on desired margin of error</li>
        <li>No beta term appears</li>
      </ul>
    </div>

    <div class="card">
      <h3>Detectability focus</h3>
      <ul class="bullets">
        <li>Goal: reject false null</li>
        <li>Depends on effect size Δ</li>
        <li>Includes both z_{α/2} and z_{β}</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) When to use each?</h2>
  </div>

  <div class="card">
    Use precision planning when:
    <br><br>
    • Primary goal is estimation  
    • Reporting confidence intervals  
    • No formal testing decision required  
  </div>

  <div class="card" style="margin-top:1rem;">
    Use detectability planning when:
    <br><br>
    • Formal hypothesis test drives decision  
    • Regulatory or confirmatory setting  
    • Type II error control is important  
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Important insight</h2>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Not interchangeable</h2>
      <p style="margin:0;">
        A study designed for narrow intervals may still have low power
        for detecting a small effect.  
        A study designed for high power may produce wide intervals
        if variability is large.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Distinguish precision vs detectability goals</li>
        <li>Recognize different sample size formulas</li>
        <li>Understand role of β in power planning</li>
        <li>Choose planning strategy based on study objective</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine the consequences of studies that are underpowered.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/power-sample-size/underpowered-studies/">
          Next lesson: 7. Underpowered Studies →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/power-sample-size/sample-size-for-proportion/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 5: Sample Size for a Proportion
          </a>
        </div>
      </div>
    </div>
  </div>
</section>