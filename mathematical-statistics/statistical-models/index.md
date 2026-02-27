---
layout: default
title: Statistical Models
description: Parametric models, parameter spaces, identifiability, and modeling assumptions.
permalink: /mathematical-statistics/statistical-models/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#f3f6ff; border:2px solid #3f51b5; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.6rem;">🚧 This Block Is Under Construction</h2>
      <p style="margin:0; color:#283593; line-height:1.6;">
        This block defines statistical models rigorously and establishes the formal framework required for estimation theory.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-lesson">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Models</span>
        <span class="badge">Parameters</span>
        <span class="badge">Identifiability</span>
        <span class="badge">Assumptions</span>
      </div>

      <h1>Block 1 — Statistical Models</h1>
      <p class="lead">
        Learn what a statistical model is, how parameters are defined, and why identifiability and assumptions matter.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/">Back: Mathematical Statistics</a>
        <a class="btn" href="/mathematical-statistics/likelihood-and-log-likelihood/">Next block: Likelihood</a>
      </div>

      <p class="muted-mini">
        Lessons are clickable. Open any lesson page at any time—even if it is still being written.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">Recommended lesson order</h2>
        <ol class="quickstart">
          <li><a href="#lessons">What is a statistical model?</a><span class="meta">Formal setup</span></li>
          <li><a href="#lessons">Parameter space & identifiability</a><span class="meta">When estimation is possible</span></li>
          <li><a href="#lessons">IID & assumptions</a><span class="meta">What you assume (and why)</span></li>
          <li><a href="#lessons">Examples of models</a><span class="meta">Concrete families</span></li>
          <li><a href="#lessons">Likelihood preview</a><span class="meta">Bridge to next block</span></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons</h2>
    <p>
      Lessons are clickable. The “Continue reading” box resumes your last visited lesson in this block.
    </p>
  </div>

  <!-- ✅ Continue reading (Block → last visited LESSON) -->
  <div id="continue-reading-ms-b1" style="display:none; margin-top:0.75rem;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p class="muted-mini" id="continue-reading-ms-b1-label" style="margin:0 0 .75rem 0;"></p>
        <a class="btn" id="continue-reading-ms-b1-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <!-- Lesson 1 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/statistical-models/what-is-a-statistical-model/">What is a statistical model?</a></h3>
      <p>Define a model as a family of distributions indexed by a parameter.</p>
      <div class="pill-row"><span class="badge">Active — open lesson</span></div>
    </div>

    <!-- Lesson 2 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/statistical-models/parameter-space-and-identifiability/">Parameter space & identifiability</a></h3>
      <p>When do different parameters produce different distributions?</p>
      <div class="pill-row"><span class="badge">Active — open lesson</span></div>
    </div>

    <!-- Lesson 3 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/statistical-models/iid-and-modeling-assumptions/">IID and modeling assumptions</a></h3>
      <p>What IID means, what it doesn’t, and why assumptions drive inference quality.</p>
      <div class="pill-row"><span class="badge">Active — open lesson</span></div>
    </div>

    <!-- Lesson 4 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/statistical-models/examples-of-parametric-models/">Examples of parametric models</a></h3>
      <p>Bernoulli, Poisson, Normal families—model form and parameter meaning.</p>
      <div class="pill-row"><span class="badge">Active — open lesson</span></div>
    </div>

    <!-- Lesson 5 -->
    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/statistical-models/likelihood-preview-why-models-matter/">Likelihood preview: why models matter</a></h3>
      <p>How model choice defines likelihood and makes estimation meaningful.</p>
      <div class="pill-row"><span class="badge">Active — open lesson</span></div>
    </div>

  </div>
</section>

<script>
  (function () {
    // ✅ Save last visited BLOCK for Mathematical Statistics HOME
    try {
      localStorage.setItem("esa_continue_ms_last_block_v0", JSON.stringify({
        label: "Block 1 — Statistical Models",
        url: "/mathematical-statistics/statistical-models/"
      }));
    } catch (e) {}

    // ✅ Block continues last visited LESSON (inside this block)
    var KEY = "esa_continue_ms_statistical_models_last_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-ms-b1");
      var label = document.getElementById("continue-reading-ms-b1-label");
      var btn = document.getElementById("continue-reading-ms-b1-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>