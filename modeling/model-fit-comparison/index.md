---
layout: default
title: Block 6 — Model Fit & Comparison
permalink: /modeling/model-fit-comparison/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800;">
    <h2>🚧 Under Construction</h2>
  </div>
</section>

<script>
(function () {
  localStorage.setItem("esa_continue_modeling_last_block_v0", JSON.stringify({
    url: "/modeling/model-fit-comparison/",
    label: "Block 6 — Model Fit & Comparison"
  }));
})();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Block 6 — Model Fit & Comparison</h1>
  </div>
</section>

<section id="continue-reading-fit" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-fit-label"></p>
    <a class="btn" id="continue-reading-fit-btn">Continue</a>
  </div>
</section>

<section class="section">
  <div class="grid grid-2">

    <div class="card lesson-card"><h3><a href="/modeling/model-fit-comparison/r-squared/">1. R² vs Adjusted R²</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/model-fit-comparison/aic-bic/">2. AIC / BIC</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/model-fit-comparison/overfitting/">3. Overfitting</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/model-fit-comparison/model-selection/">4. Model Selection</a></h3></div>

  </div>
</section>

<script>
(function () {
  var raw = localStorage.getItem("esa_continue_modeling_fit_lesson_v0");
  if (!raw) return;
  var data = JSON.parse(raw);

  document.getElementById("continue-reading-fit-label").innerHTML =
    'You last visited: <strong>' + data.label + '</strong>';
  document.getElementById("continue-reading-fit-btn").href = data.url;
  document.getElementById("continue-reading-fit").style.display = "block";
})();
</script>