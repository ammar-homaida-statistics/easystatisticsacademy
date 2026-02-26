---
layout: default
title: Statistical Models
description: Parametric models, parameter spaces, identifiability, and modeling assumptions.
permalink: /mathematical-statistics/statistical-models/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#f3f6ff; border:2px solid #3f51b5; padding:1.5rem; border-radius:10px;">
    <h2 style="margin-top:0; color:#1a237e;">🚧 This Block Is Under Construction</h2>
    <p style="margin:0; line-height:1.6;">
      This block defines statistical models rigorously: parametric families, parameter spaces,
      identifiability, and the assumptions that make estimation meaningful.
    </p>
  </div>
</section>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Block 1 — Statistical Models</h1>
    <p class="lead">
      Build the formal foundation for estimation by understanding what a model is,
      what the parameter represents, and when a model is identifiable.
    </p>
  </div>
</section>

<div id="continue-reading-ms-models" style="display:none; margin-top:1rem;">
  <div class="callout">
    <h2>Continue reading</h2>
    <p id="continue-reading-ms-models-label" class="muted-mini"></p>
    <a class="btn" id="continue-reading-ms-models-btn" href="#">Continue</a>
  </div>
</div>

<script>
(function () {
  var KEY = "esa_continue_ms_statistical_models_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;
  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;
    document.getElementById("continue-reading-ms-models-label").innerHTML =
      'You last visited: <strong>' + data.label + '</strong>';
    document.getElementById("continue-reading-ms-models-btn").href = data.url;
    document.getElementById("continue-reading-ms-models").style.display = "block";
  } catch(e){}
})();
</script>