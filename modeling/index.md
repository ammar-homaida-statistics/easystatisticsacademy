---
layout: default
title: Statistical Modeling
description: Learn statistical modeling correctly: regression, assumptions, diagnostics, interpretation, model comparison, and responsible modeling practice.
permalink: /modeling/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:1.5rem; border-radius:10px;">
    <h2 style="margin-top:0; color:#e65100;">🚧 This Section Is Under Construction</h2>
    <p>The Statistical Modeling unit is being developed block-by-block.</p>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Models</span>
        <span class="badge">Regression</span>
        <span class="badge">Diagnostics</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>Statistical Modeling</h1>

      <p class="lead">
        Learn how to build, evaluate, and interpret statistical models correctly.
      </p>

      <div class="hero-actions">
        <a class="btn" href="/inference/">Prerequisite: Statistical inference</a>
        <a class="btn btn-outline" href="/applied-statistics/">Next: Applied Statistics</a>
      </div>

    </div>
  </div>
</section>

<section class="section" id="blocks">

  <h2>Blocks</h2>

  <!-- ✅ CONTINUE READING -->
  <div id="continue-reading-modeling" style="display:none; margin-top:1rem;">
    <div class="callout">
      <h2>Continue reading</h2>
      <p id="continue-reading-modeling-label"></p>
      <a class="btn" id="continue-reading-modeling-btn">Continue</a>
    </div>
  </div>

  <div class="grid grid-2">

    <!-- Block 1 -->
    <div class="card lesson-card">
      <h3>
        <a class="block-link" href="/modeling/foundations/">Block 1 — Modeling Foundations</a>
      </h3>
      <a class="btn btn-outline block-link" href="/modeling/foundations/">Open block</a>
    </div>

    <!-- Block 2 -->
    <div class="card lesson-card">
      <h3>
        <a class="block-link" href="/modeling/simple-linear-regression/">Block 2 — Simple Linear Regression</a>
      </h3>
      <a class="btn btn-outline block-link" href="/modeling/simple-linear-regression/">Open block</a>
    </div>

    <!-- Block 3 -->
    <div class="card lesson-card">
      <h3>
        <a class="block-link" href="/modeling/multiple-regression/">Block 3 — Multiple Regression</a>
      </h3>
      <a class="btn btn-outline block-link" href="/modeling/multiple-regression/">Open block</a>
    </div>

    <!-- Block 4 -->
    <div class="card lesson-card">
      <h3>
        <a class="block-link" href="/modeling/assumptions/">Block 4 — Model Assumptions</a>
      </h3>
      <a class="btn btn-outline block-link" href="/modeling/assumptions/">Open block</a>
    </div>

    <!-- Block 5 -->
    <div class="card lesson-card">
      <h3>
        <a class="block-link" href="/modeling/diagnostics/">Block 5 — Diagnostics</a>
      </h3>
      <a class="btn btn-outline block-link" href="/modeling/diagnostics/">Open block</a>
    </div>

    <!-- Block 6 -->
    <div class="card lesson-card">
      <h3>
        <a class="block-link" href="/modeling/model-fit-comparison/">Block 6 — Model Fit & Comparison</a>
      </h3>
      <a class="btn btn-outline block-link" href="/modeling/model-fit-comparison/">Open block</a>
    </div>

    <!-- Block 7 -->
    <div class="card lesson-card">
      <h3>
        <a class="block-link" href="/modeling/extensions/">Block 7 — Extensions</a>
      </h3>
      <a class="btn btn-outline block-link" href="/modeling/extensions/">Open block</a>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <h2>Goal of this unit</h2>
    <ul>
      <li>Understand models as representations of relationships</li>
      <li>Interpret coefficients correctly</li>
      <li>Diagnose assumptions</li>
      <li>Avoid overfitting</li>
    </ul>
  </div>
</section>

<!-- ✅ READ LAST BLOCK -->
<script>
(function () {
  var KEY = "esa_continue_modeling_last_block_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url) return;

    var wrap = document.getElementById("continue-reading-modeling");
    var label = document.getElementById("continue-reading-modeling-label");
    var btn = document.getElementById("continue-reading-modeling-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML = 'You last visited: <strong>' + (data.label || "block") + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>

<!-- ✅ WRITE LAST BLOCK (FIXED) -->
<script>
(function () {
  var KEY = "esa_continue_modeling_last_block_v0";

  var links = document.querySelectorAll('.block-link');

  links.forEach(function(link) {
    link.addEventListener("click", function () {

      var label = link.textContent.trim();
      var url = link.getAttribute("href");

      localStorage.setItem(KEY, JSON.stringify({
        url: url,
        label: label
      }));

    });
  });
})();
</script>