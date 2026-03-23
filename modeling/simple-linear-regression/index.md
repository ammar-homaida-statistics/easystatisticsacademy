---
layout: default
title: Simple Linear Regression
permalink: /modeling/simple-linear-regression/
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:1.5rem; border-radius:10px;">
    <h2 style="color:#e65100;">🚧 Under Construction</h2>
    <p>Lessons will be added progressively.</p>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Simple Linear Regression</h1>
    <p class="lead">
      Learn the simplest statistical model connecting one predictor to an outcome.
    </p>
  </div>
</section>

<div id="continue-reading-slr" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-slr-label"></p>
    <a class="btn" id="continue-reading-slr-btn">Continue</a>
  </div>
</div>

<section class="section">
  <p class="muted-mini">Lessons coming soon.</p>
</section>

<script>
(function () {
  var KEY = "esa_continue_modeling_slr_last_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data.url || !data.label) return;

    document.getElementById("continue-reading-slr-label").innerHTML =
      'You last visited: <strong>' + data.label + '</strong>';
    document.getElementById("continue-reading-slr-btn").href = data.url;
    document.getElementById("continue-reading-slr").style.display = "block";
  } catch (e) {}
})();
</script>