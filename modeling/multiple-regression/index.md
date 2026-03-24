---
layout: default
title: Block 3 — Multiple Regression
permalink: /modeling/multiple-regression/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 This Block Is Under Construction</h2>
    <p>Multiple regression concepts and interpretation are being developed carefully.</p>
  </div>
</section>

<script>
(function () {
  localStorage.setItem("esa_continue_modeling_last_block_v0", JSON.stringify({
    url: "/modeling/multiple-regression/",
    label: "Block 3 — Multiple Regression"
  }));
})();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <h1>Block 3 — Multiple Regression</h1>
      <p class="lead">
        Extend modeling to multiple predictors and understand adjusted effects.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none;">
          <li><strong>Multiple predictors</strong></li>
          <li><strong>Adjusted effects</strong></li>
          <li><strong>Confounding</strong></li>
          <li><strong>Interpretation</strong></li>
          <li><strong>Multicollinearity</strong></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="continue-reading-mr" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-mr-label"></p>
    <a class="btn" id="continue-reading-mr-btn">Continue</a>
  </div>
</section>

<section class="section">
  <div class="grid grid-2">

    <div class="card lesson-card"><h3><a href="/modeling/multiple-regression/why-multiple/">1. Why Multiple Regression?</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/multiple-regression/adjusted-effects/">2. Adjusted Effects</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/multiple-regression/confounding/">3. Confounding</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/multiple-regression/coefficients/">4. Interpreting Coefficients</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/multiple-regression/multicollinearity/">5. Multicollinearity</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/multiple-regression/dummy-variables/">6. Dummy Variables</a></h3></div>
    <div class="card lesson-card"><h3><a href="/modeling/multiple-regression/interactions/">7. Interaction Effects</a></h3></div>

  </div>
</section>

<script>
(function () {
  var raw = localStorage.getItem("esa_continue_modeling_mr_lesson_v0");
  if (!raw) return;
  var data = JSON.parse(raw);

  document.getElementById("continue-reading-mr-label").innerHTML =
    'You last visited: <strong>' + data.label + '</strong>';
  document.getElementById("continue-reading-mr-btn").href = data.url;
  document.getElementById("continue-reading-mr").style.display = "block";
})();
</script>