---
layout: default
title: Modeling Foundations
permalink: /modeling/foundations/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100;">🚧 This Block Is Under Construction</h2>
      <p>
        The Modeling Foundations block is being developed in a structured, lesson-by-lesson format.
      </p>
    </div>
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

<div id="continue-reading-foundations" style="display:none; margin-top:0.75rem;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p id="continue-reading-foundations-label"></p>
      <a class="btn" id="continue-reading-foundations-btn" href="#">Continue</a>
    </div>
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
    if (!data || !data.url) return;

    document.getElementById("continue-reading-foundations-label").innerHTML =
      'You last visited: <strong>' + (data.label || "lesson") + '</strong>';

    document.getElementById("continue-reading-foundations-btn").href = data.url;
    document.getElementById("continue-reading-foundations").style.display = "block";
  } catch (e) {}
})();
</script>