---
layout: default
title: "Z-scores (Standardization)"
description: "Transforming values into standard deviation units for comparison across distributions."
permalink: /descriptive/shape/z-scores/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/shape/empirical-rule/">
    ← Previous Lesson: The Empirical Rule (68–95–99.7)
  </a>
</section>

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5;border:2px solid #ff9800;padding:2rem;border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0;color:#e65100;font-size:1.8rem;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0;font-size:1.05rem;color:#5d4037;line-height:1.6;">
        Visual standardization diagrams, cross-scale comparison examples, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

  <div class="section-head">
    <h1>Z-scores (Standardization)</h1>
    <p class="lead">
      A z-score expresses how far a value lies from the mean in standard deviation units.
    </p>
  </div>

  <hr>

  <h2>1. Why Standardize?</h2>

  <p>
    Raw values cannot always be compared directly.
  </p>

  <p>
    For example:
  </p>

  <ul>
    <li>Student A scores 85 in a class with mean 70.</li>
    <li>Student B scores 1200 on an exam with mean 1000.</li>
  </ul>

  <p>
    Which student performed better relative to their group?
  </p>

  <p>
    To answer this, we convert scores into standardized units.
  </p>

  <hr>

  <h2>2. The Z-score Formula</h2>

  <p style="font-weight:bold;">
    z = (x − μ) / σ
  </p>

  <ul>
    <li>x = observed value</li>
    <li>μ = mean</li>
    <li>σ = standard deviation</li>
  </ul>

  <hr>

  <h2>3. Interpretation</h2>

  <ul>
    <li>z = 0 → value equals the mean</li>
    <li>z = 1 → one SD above the mean</li>
    <li>z = -2 → two SDs below the mean</li>
    <li>|z| > 3 → potentially unusual value</li>
  </ul>

  <hr>

  <h2>4. Example</h2>

  <p>
    Suppose:
  </p>

  <ul>
    <li>Mean = 70</li>
    <li>Standard deviation = 10</li>
    <li>Student score = 85</li>
  </ul>

  <p>
    z = (85 − 70) / 10  
    z = 15 / 10  
    z = 1.5
  </p>

  <p>
    The student scored 1.5 standard deviations above the mean.
  </p>

  <hr>

  <h2>5. Why Z-scores Matter</h2>

  <ul>
    <li>Enable comparison across different scales.</li>
    <li>Identify outliers.</li>
    <li>Used in probability calculations.</li>
    <li>Foundation for hypothesis testing.</li>
  </ul>

  <hr>

  <h2>6. Important Notes</h2>

  <ul>
    <li>Interpretation assumes approximate normality.</li>
    <li>In skewed distributions, z-scores may mislead.</li>
    <li>Standardization does not change distribution shape.</li>
  </ul>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>Z-scores convert values into SD units.</li>
    <li>Allow meaningful cross-scale comparison.</li>
    <li>Central to probability and inference.</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/shape/standardization-when-and-when-not/">
    Next Lesson → Standardization: When It Helps and When It Misleads
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_shape_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/shape/z-scores/",
    label:"Lesson 7 — Z-scores (Standardization)",
    ts:Date.now()
  }));
})();
</script>