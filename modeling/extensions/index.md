---
layout: default
title: Extensions
permalink: /modeling/extensions/
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800;">
    <h2>🚧 Under Construction</h2>
    <p>Advanced models will be introduced gradually.</p>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card">
    <h1>Extensions</h1>
    <p class="lead">Go beyond linear models toward generalized modeling approaches.</p>
  </div>
</section>

<div id="continue-reading-extensions" style="display:none;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-extensions-label"></p>
    <a class="btn" id="continue-reading-extensions-btn">Continue</a>
  </div>
</div>

<section class="section">
  <p class="muted-mini">Lessons coming soon.</p>
</section>

<script>
(function () {
  var KEY = "esa_continue_modeling_extensions_last_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data.url || !data.label) return;

    document.getElementById("continue-reading-extensions-label").innerHTML =
      'You last visited: <strong>' + data.label + '</strong>';
    document.getElementById("continue-reading-extensions-btn").href = data.url;
    document.getElementById("continue-reading-extensions").style.display = "block";
  } catch (e) {}
})();
</script>