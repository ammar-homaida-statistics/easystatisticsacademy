---
layout: default
title: Fisher Information & Efficiency
description: Fisher information, Cramér–Rao lower bound, and efficiency concepts.
permalink: /mathematical-statistics/fisher-information-and-efficiency/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#f3f6ff; border:2px solid #3f51b5; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.6rem;">🚧 This Block Is Under Construction</h2>
      <p style="margin:0; color:#283593; line-height:1.6;">
        This block studies Fisher information and the fundamental limits of estimator precision,
        including the Cramér–Rao lower bound and efficiency.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-lesson">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Information</span>
        <span class="badge">CRLB</span>
        <span class="badge">Efficiency</span>
        <span class="badge">Bounds</span>
      </div>

      <h1>Block 5 — Fisher Information & Efficiency</h1>
      <p class="lead">
        Quantify precision using information and learn the theoretical lower bounds on estimator variance.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/">Back: Mathematical Statistics</a>
        <a class="btn" href="/mathematical-statistics/asymptotic-theory/">Next block: Asymptotic Theory</a>
      </div>

      <p class="muted-mini">
        This block provides the key bridge from likelihood curvature to estimator precision.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">Recommended lesson order</h2>
        <ol class="quickstart">
          <li><a href="#lessons">Fisher information (definition)</a><span class="meta">Core quantity</span></li>
          <li><a href="#lessons">Cramér–Rao lower bound</a><span class="meta">Variance bound</span></li>
          <li><a href="#lessons">Efficiency and achieving the bound</a><span class="meta">Best possible</span></li>
          <li><a href="#lessons">Additivity and IID</a><span class="meta">Information grows with n</span></li>
          <li><a href="#lessons">Information & MLE connection (preview)</a><span class="meta">Asymptotic link</span></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons</h2>
    <p>“Continue reading” resumes your last visited lesson in this block.</p>
  </div>

  <!-- Continue reading -->
  <div id="continue-reading-ms-b5" style="display:none; margin-top:0.75rem;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p class="muted-mini" id="continue-reading-ms-b5-label" style="margin:0 0 .75rem 0;"></p>
        <a class="btn" id="continue-reading-ms-b5-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/fisher-information-and-efficiency/fisher-information-definition/">Fisher information (definition)</a></h3>
      <p>Define information via expected curvature or score variance and interpret it.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/fisher-information-and-efficiency/fisher-information-definition/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/">Cramér–Rao lower bound</a></h3>
      <p>Derive and interpret the fundamental variance bound for unbiased estimators.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/fisher-information-and-efficiency/efficiency-and-achieving-the-bound/">Efficiency and achieving the bound</a></h3>
      <p>What it means to be efficient and when the bound can be attained.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/fisher-information-and-efficiency/efficiency-and-achieving-the-bound/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/fisher-information-and-efficiency/information-additivity-and-iid/">Information additivity and IID</a></h3>
      <p>Why information typically scales with sample size under independence.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/fisher-information-and-efficiency/information-additivity-and-iid/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/mathematical-statistics/fisher-information-and-efficiency/information-and-mle-connection-preview/">Information and MLE connection (preview)</a></h3>
      <p>Preview why MLE variance is linked to information asymptotically.</p>
      <div class="pill-row">
        <a class="btn btn-outline"
           href="/mathematical-statistics/fisher-information-and-efficiency/information-and-mle-connection-preview/"
           style="border-color:#111; color:#111;">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<script>
  (function () {

    try {
      localStorage.setItem("esa_continue_ms_last_block_v0", JSON.stringify({
        label: "Block 5 — Fisher Information & Efficiency",
        url: "/mathematical-statistics/fisher-information-and-efficiency/"
      }));
    } catch (e) {}

    var KEY = "esa_continue_ms_information_last_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-ms-b5");
      var label = document.getElementById("continue-reading-ms-b5-label");
      var btn = document.getElementById("continue-reading-ms-b5-btn");

      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}

  })();
</script>