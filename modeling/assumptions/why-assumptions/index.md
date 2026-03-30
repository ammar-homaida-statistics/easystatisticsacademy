---
layout: default
title: 1. Why Assumptions Matter
permalink: /modeling/assumptions/why-assumptions/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding why assumptions are necessary.
      Specific assumptions will be developed in the following lessons.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_assumptions_lesson_v0", JSON.stringify({
    url: "/modeling/assumptions/why-assumptions/",
    label: "Lesson 1 — Why Assumptions Matter",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 4</span>
      <span class="badge">Lesson 1</span>
      <span class="badge">Assumptions</span>
      <span class="badge">Validity</span>
    </div>

    <h1>1. Why Assumptions Matter</h1>

    <p class="lead">
      Regression models rely on assumptions to produce valid and reliable results.
      Without these assumptions, model conclusions can be misleading.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/assumptions/">Back to Block 4</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual foundation before studying individual assumptions.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand why regression assumptions exist
    and how they affect the validity of model results.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Assumptions define the conditions under which a regression model produces
      trustworthy results.
    </p>
  </div>

  <h2>1) What are assumptions?</h2>
  <div class="card">
    <p>
      Assumptions are conditions about the data and the model that must hold
      for the model to work correctly.
    </p>
  </div>

  <h2>2) Why models need assumptions</h2>
  <div class="card">
    <p>
      Regression models are simplified representations of reality.
      Assumptions allow us to make valid conclusions from these models.
    </p>
  </div>

  <h2>3) What happens if assumptions fail?</h2>
  <div class="card">
    <ul>
      <li>Estimates may be biased</li>
      <li>Predictions may be unreliable</li>
      <li>Interpretation may be incorrect</li>
    </ul>
  </div>

  <h2>4) Not all assumptions are equally critical</h2>
  <div class="card">
    <p>
      Some violations have minor effects,
      while others can severely damage model validity.
    </p>
  </div>

  <h2>5) Assumptions vs reality</h2>
  <div class="card">
    <p>
      In practice, assumptions are rarely perfectly satisfied.
      The goal is to assess whether violations are serious.
    </p>
  </div>

  <h2>6) Role of diagnostics</h2>
  <div class="card">
    <p>
      Diagnostics help us check whether assumptions are reasonable
      and identify potential problems.
    </p>
  </div>

  <h2>7) Common misconception</h2>
  <div class="card">
    <p>
      Assumptions are not optional.
      Ignoring them can lead to incorrect conclusions.
    </p>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Understanding assumptions is essential for responsible use of regression models
      in research and real-world applications.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand what assumptions are</li>
      <li>Understand why assumptions are needed</li>
      <li>Recognize consequences of violations</li>
      <li>Understand role of diagnostics</li>
      <li>Prepare for specific assumptions</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now begin with the first key assumption:
      linearity.
    </p>
    <a class="btn" href="/modeling/assumptions/linearity/">
      Next lesson: Linearity →
    </a>
  </div>

</section>