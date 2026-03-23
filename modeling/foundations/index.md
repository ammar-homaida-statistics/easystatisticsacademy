---
layout: default
title: Modeling Foundations
permalink: /modeling/foundations/
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:1.5rem; border-radius:10px;">
    <h2 style="margin-top:0; color:#e65100;">🚧 Under Construction</h2>
    <p>This block is being developed carefully. Lessons will be published in order.</p>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Modeling Foundations</h1>
    <p class="lead">
      Understand what statistical models are, why they exist, and how they represent relationships in data.
    </p>
  </div>
</section>

<div id="continue-reading-foundations" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-foundations-label"></p>
    <a class="btn" id="continue-reading-foundations-btn">Continue</a>
  </div>
</div>

<section class="section">
  <p class="muted-mini">Lessons will appear here.</p>
</section>

<script>
(function () {
  var KEY = "esa_continue_modeling_foundations_last_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data.url || !data.label) return;

    document.getElementById("continue-reading-foundations-label").innerHTML =
      'You last visited: <strong>' + data.label + '</strong>';
    document.getElementById("continue-reading-foundations-btn").href = data.url;
    document.getElementById("continue-reading-foundations").style.display = "block";
  } catch (e) {}
})();
</script>