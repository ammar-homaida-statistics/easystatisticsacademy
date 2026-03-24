---
layout: default
title: Block 1 — Modeling Foundations
permalink: /modeling/foundations/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 This Block Is Under Construction</h2>
    <p>Conceptual foundation of statistical modeling is being developed.</p>
  </div>
</section>

<script>
(function () {
  localStorage.setItem("esa_continue_modeling_last_block_v0", JSON.stringify({
    url: "/modeling/foundations/",
    label: "Block 1 — Modeling Foundations"
  }));
})();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <h1>Block 1 — Modeling Foundations</h1>
      <p class="lead">Understand what models are and why they exist.</p>
    </div>
  </div>
</section>

<section id="continue-reading-foundations" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-foundations-label"></p>
    <a class="btn" id="continue-reading-foundations-btn">Continue</a>
  </div>
</section>

<section class="section">
  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/modeling/foundations/what-is-a-model/">1. What Is a Model?</a></h3>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/foundations/variables/">2. Variables and Relationships</a></h3>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/foundations/signal-noise/">3. Signal vs Noise</a></h3>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/foundations/parameters/">4. Parameters</a></h3>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/foundations/prediction-vs-explanation/">5. Prediction vs Explanation</a></h3>
    </div>

  </div>
</section>

<script>
(function () {
  var raw = localStorage.getItem("esa_continue_modeling_foundations_lesson_v0");
  if (!raw) return;
  var data = JSON.parse(raw);

  document.getElementById("continue-reading-foundations-label").innerHTML =
    'You last visited: <strong>' + data.label + '</strong>';

  document.getElementById("continue-reading-foundations-btn").href = data.url;
  document.getElementById("continue-reading-foundations").style.display = "block";
})();
</script>