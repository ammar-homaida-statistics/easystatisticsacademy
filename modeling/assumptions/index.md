---
layout: default
title: Block 4 — Model Assumptions
permalink: /modeling/assumptions/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem;">
    <h2 style="color:#e65100;">🚧 Under Construction</h2>
    <p>Assumptions are being developed with strong conceptual clarity.</p>
  </div>
</section>

<script>
(function () {
  localStorage.setItem("esa_continue_modeling_last_block_v0", JSON.stringify({
    url: "/modeling/assumptions/",
    label: "Block 4 — Model Assumptions"
  }));
})();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Block 4 — Model Assumptions</h1>
    <p class="lead">Understand the conditions required for valid models.</p>
  </div>
</section>

<section id="continue-reading-assumptions" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-assumptions-label"></p>
    <a class="btn" id="continue-reading-assumptions-btn">Continue</a>
  </div>
</section>

<section class="section">
  <div class="grid grid-2">

    <div class="card lesson-card"><h3><a href="/modeling/assumptions/why-assumptions/">1. Why Assumptions Matter</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/assumptions/linearity/">2. Linearity</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/assumptions/independence/">3. Independence</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/assumptions/homoscedasticity/">4. Homoscedasticity</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/assumptions/normality/">5. Normality</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/assumptions/violations/">6. Violations & Consequences</a></h3></div>

  </div>
</section>

<script>
(function () {
  var raw = localStorage.getItem("esa_continue_modeling_assumptions_lesson_v0");
  if (!raw) return;
  var data = JSON.parse(raw);

  document.getElementById("continue-reading-assumptions-label").innerHTML =
    'You last visited: <strong>' + data.label + '</strong>';
  document.getElementById("continue-reading-assumptions-btn").href = data.url;
  document.getElementById("continue-reading-assumptions").style.display = "block";
})();
</script>