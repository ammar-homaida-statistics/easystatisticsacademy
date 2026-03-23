---
layout: default
title: Model Fit & Comparison
permalink: /modeling/model-fit-comparison/
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800;">
    <h2>🚧 Under Construction</h2>
    <p>Evaluation methods will be added.</p>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Model Fit & Comparison</h1>
    <p class="lead">Compare models and understand performance vs complexity.</p>
  </div>
</section>

<div id="continue-reading-fit" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-fit-label"></p>
    <a class="btn" id="continue-reading-fit-btn">Continue</a>
  </div>
</div>

<section class="section">
  <p class="muted-mini">Lessons coming soon.</p>
</section>

<script>
(function () {
  var KEY = "esa_continue_modeling_fit_last_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data.url || !data.label) return;

    document.getElementById("continue-reading-fit-label").innerHTML =
      'You last visited: <strong>' + data.label + '</strong>';
    document.getElementById("continue-reading-fit-btn").href = data.url;
    document.getElementById("continue-reading-fit").style.display = "block";
  } catch (e) {}
})();
</script>