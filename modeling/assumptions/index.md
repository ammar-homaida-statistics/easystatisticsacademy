---
layout: default
title: Model Assumptions
permalink: /modeling/assumptions/
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800;">
    <h2>🚧 Under Construction</h2>
    <p>Assumption-focused lessons will be added.</p>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Model Assumptions</h1>
    <p class="lead">Understand the conditions required for valid modeling.</p>
  </div>
</section>

<div id="continue-reading-assumptions" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-assumptions-label"></p>
    <a class="btn" id="continue-reading-assumptions-btn">Continue</a>
  </div>
</div>

<section class="section">
  <p class="muted-mini">Lessons coming soon.</p>
</section>

<script>
(function () {
  var KEY = "esa_continue_modeling_assumptions_last_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data.url || !data.label) return;

    document.getElementById("continue-reading-assumptions-label").innerHTML =
      'You last visited: <strong>' + data.label + '</strong>';
    document.getElementById("continue-reading-assumptions-btn").href = data.url;
    document.getElementById("continue-reading-assumptions").style.display = "block";
  } catch (e) {}
})();
</script>