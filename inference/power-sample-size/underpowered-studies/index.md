---
layout: default
title: "7. Underpowered Studies"
description: "Understand the consequences of low statistical power, why small studies can mislead, and how underpowered designs distort inference."
permalink: /inference/power-sample-size/underpowered-studies/
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
        Version 0 explains why low power weakens scientific conclusions.
        Simulation examples and empirical illustrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_power_sample_size_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/power-sample-size/underpowered-studies/",
      label: "Lesson 7 — Underpowered Studies",
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
        <span class="badge">Lesson 7</span>
        <span class="badge">Power</span>
        <span class="badge">Study Design</span>
      </div>

      <h1>7. Underpowered Studies</h1>

      <p class="lead">
        A study with low statistical power has a high probability of
        failing to detect real effects.
        Underpowered designs create unreliable and unstable conclusions.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/power-sample-size/">Back to Block 5</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Low power does not only increase Type II error — it affects interpretation quality.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand the statistical and practical consequences of low power
      and recognize why adequate sample size is essential for credible inference.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core issue</h2>
      <p style="margin:0;">
        When power is low:
        \[
        P(\text{Reject } H_0 \mid H_1 \text{ true})
        \text{ is small.}
        \]
        Real effects are frequently missed.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Increased Type II error</h2>
  </div>

  <div class="card">
    Power:
    \[
    1 - \beta
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Underpowered study:
    \[
    \beta \text{ is large}
    \quad\Rightarrow\quad
    \text{High probability of false negative.}
    \]
  </div>

  <p class="muted-mini">
    Important effects may go undetected.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Instability of significant results</h2>
  </div>

  <div class="card">
    In low-power settings:
    <br><br>
    • Only large observed effects become significant  
    • Estimated effect sizes are exaggerated  
    • Results are less reproducible  
  </div>

  <p>
    This phenomenon is sometimes called
    <strong>effect size inflation</strong>.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Wide confidence intervals</h2>
  </div>

  <div class="card">
    Standard error:
    \[
    SE \propto \frac{1}{\sqrt{n}}
    \]
  </div>

  <p>
    Small n leads to:
    <br>
    • Large standard errors  
    • Wide confidence intervals  
    • Imprecise estimates  
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Misleading interpretation</h2>
  </div>

  <div class="card">
    Non-significant result in an underpowered study
    does <strong>not</strong> imply:
    <br><br>
    “No effect exists.”
  </div>

  <p>
    It may simply reflect insufficient sensitivity.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical consequences</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Scientific impact</h3>
      <ul class="bullets">
        <li>Irreproducible findings</li>
        <li>Inconsistent literature</li>
        <li>False sense of null effect</li>
      </ul>
    </div>

    <div class="card">
      <h3>Ethical impact</h3>
      <ul class="bullets">
        <li>Wasted resources</li>
        <li>Participant burden without strong inference</li>
        <li>Poor decision-making</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Practical rule</h2>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Recommended threshold</h2>
      <p style="margin:0;">
        Many applied fields use
        \[
        \text{Power} \ge 0.80
        \]
        as a minimum planning benchmark.
      </p>
    </div>
  </div>

  <p class="muted-mini">
    This is not universal, but commonly accepted.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Recognize consequences of low power</li>
        <li>Understand effect size inflation</li>
        <li>Distinguish non-significant from “no effect”</li>
        <li>Appreciate ethical dimension of study design</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine how statistical software performs
        power and sample size analysis in practice.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/power-sample-size/software-and-power-analysis/">
          Next lesson: 8. Software & Power Analysis →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/power-sample-size/precision-vs-detectability/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 6: Precision vs Detectability
          </a>
        </div>
      </div>
    </div>
  </div>
</section>