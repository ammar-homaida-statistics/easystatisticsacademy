---
layout: default
title: Diagnostics
permalink: /modeling/diagnostics/
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800;">
    <h2>🚧 Under Construction</h2>
    <p>Diagnostic tools will be added step by step.</p>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Model Diagnostics</h1>
    <p class="lead">Evaluate whether your model is valid and trustworthy.</p>
  </div>
</section>

<div id="continue-reading-diagnostics" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-diagnostics-label"></p>
    <a class="btn" id="continue-reading-diagnostics-btn">Continue</a>
  </div>
</div>

<section class="section">
  <p class="muted-mini">Lessons coming soon.</p>
</section>

<script>
(function () {
  var KEY = "esa_continue_modeling_diagnostics_last_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data.url || !data.label) return;

    document.getElementById("continue-reading-diagnostics-label").innerHTML =
      'You last visited: <strong>' + data.label + '</strong>';
    document.getElementById("continue-reading-diagnostics-btn").href = data.url;
    document.getElementById("continue-reading-diagnostics").style.display = "block";
  } catch (e) {}
})();
</script>