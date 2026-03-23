---
layout: default
title: Multiple Regression
permalink: /modeling/multiple-regression/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:1.5rem; border-radius:10px;">
    <h2 style="color:#e65100;">🚧 This Block Is Under Construction</h2>
    <p>Lessons will be added gradually.</p>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Multiple Regression</h1>
    <p class="lead">
      Understand models with multiple predictors and interpret adjusted effects correctly.
    </p>
  </div>
</section>

<div id="continue-reading-mr" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-mr-label"></p>
    <a class="btn" id="continue-reading-mr-btn">Continue</a>
  </div>
</div>

<section class="section">
  <p class="muted-mini">Lessons coming soon.</p>
</section>

<script>
(function () {
  var KEY = "esa_continue_modeling_mr_last_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url) return;

    document.getElementById("continue-reading-mr-label").innerHTML =
      'You last visited: <strong>' + (data.label || "lesson") + '</strong>';

    document.getElementById("continue-reading-mr-btn").href = data.url;
    document.getElementById("continue-reading-mr").style.display = "block";
  } catch (e) {}
})();
</script>