---
layout: default
title: Block 7 — Extensions
permalink: /modeling/extensions/
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
    url: "/modeling/extensions/",
    label: "Block 7 — Extensions"
  }));
})();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Block 7 — Extensions</h1>
  </div>
</section>

<section id="continue-reading-extensions" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-extensions-label"></p>
    <a class="btn" id="continue-reading-extensions-btn">Continue</a>
  </div>
</section>

<section class="section">
  <div class="grid grid-2">

    <div class="card lesson-card"><h3><a href="/modeling/extensions/logistic-regression/">1. Logistic Regression</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/extensions/odds/">2. Odds Interpretation</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/extensions/glm/">3. Generalized Linear Models</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/extensions/link-functions/">4. Link Functions</a></h3></div>

  </div>
</section>

<script>
(function () {
  var raw = localStorage.getItem("esa_continue_modeling_extensions_lesson_v0");
  if (!raw) return;
  var data = JSON.parse(raw);

  document.getElementById("continue-reading-extensions-label").innerHTML =
    'You last visited: <strong>' + data.label + '</strong>';
  document.getElementById("continue-reading-extensions-btn").href = data.url;
  document.getElementById("continue-reading-extensions").style.display = "block";
})();
</script>