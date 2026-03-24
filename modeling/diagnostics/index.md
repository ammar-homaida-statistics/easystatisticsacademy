---
layout: default
title: Block 5 — Diagnostics
permalink: /modeling/diagnostics/
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
    url: "/modeling/diagnostics/",
    label: "Block 5 — Diagnostics"
  }));
})();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Block 5 — Diagnostics</h1>
  </div>
</section>

<section id="continue-reading-diagnostics" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-diagnostics-label"></p>
    <a class="btn" id="continue-reading-diagnostics-btn">Continue</a>
  </div>
</section>

<section class="section">
  <div class="grid grid-2">

    <div class="card lesson-card"><h3><a href="/modeling/diagnostics/residual-plots/">1. Residual Plots</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/diagnostics/outliers/">2. Outliers</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/diagnostics/leverage/">3. Leverage</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/diagnostics/influence/">4. Influence</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/diagnostics/cooks-distance/">5. Cook’s Distance</a></h3></div>

  </div>
</section>

<script>
(function () {
  var raw = localStorage.getItem("esa_continue_modeling_diagnostics_lesson_v0");
  if (!raw) return;
  var data = JSON.parse(raw);

  document.getElementById("continue-reading-diagnostics-label").innerHTML =
    'You last visited: <strong>' + data.label + '</strong>';
  document.getElementById("continue-reading-diagnostics-btn").href = data.url;
  document.getElementById("continue-reading-diagnostics").style.display = "block";
})();
</script>