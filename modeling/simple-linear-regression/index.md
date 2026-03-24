---
layout: default
title: Block 2 — Simple Linear Regression
permalink: /modeling/simple-linear-regression/
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
    url: "/modeling/simple-linear-regression/",
    label: "Block 2 — Simple Linear Regression"
  }));
})();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Block 2 — Simple Linear Regression</h1>
  </div>
</section>

<section id="continue-reading-slr" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-slr-label"></p>
    <a class="btn" id="continue-reading-slr-btn">Continue</a>
  </div>
</section>

<section class="section">
  <div class="grid grid-2">

    <div class="card lesson-card"><h3><a href="/modeling/simple-linear-regression/what-is-regression/">1. What Is Regression?</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/simple-linear-regression/slope/">2. Slope Interpretation</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/simple-linear-regression/intercept/">3. Intercept</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/simple-linear-regression/residuals/">4. Residuals</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/simple-linear-regression/least-squares/">5. Least Squares</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/simple-linear-regression/r-squared/">6. R²</a></h3></div>

  </div>
</section>

<script>
(function () {
  var raw = localStorage.getItem("esa_continue_modeling_slr_lesson_v0");
  if (!raw) return;
  var data = JSON.parse(raw);

  document.getElementById("continue-reading-slr-label").innerHTML =
    'You last visited: <strong>' + data.label + '</strong>';

  document.getElementById("continue-reading-slr-btn").href = data.url;
  document.getElementById("continue-reading-slr").style.display = "block";
})();
</script>