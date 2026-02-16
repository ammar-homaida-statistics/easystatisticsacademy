---
layout: default
title: "Range"
description: "The simplest measure of spread: difference between the maximum and minimum values."
permalink: /descriptive/spread/range/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/spread/what-is-variability/">
    ← Previous Lesson: What Is Variability?
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
        Visual comparisons, outlier demonstrations, and software examples (SPSS, R, Python, Excel) will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Range</h1>
    <p class="lead">
      The range is the simplest measure of variability.
      It captures the total spread of a dataset using only two values.
    </p>
  </div>

  <hr>

  <h2>1. Definition</h2>

  <p>
    <strong>Range = Maximum − Minimum</strong>
  </p>

  <p>
    It measures the distance between the smallest and largest observations.
  </p>

  <hr>

  <h2>2. Example</h2>

  <p><strong>Dataset:</strong> 12, 15, 18, 20, 25</p>

  <p>
    Maximum = 25  
    Minimum = 12
  </p>

  <p>
    Range = 25 − 12 = 13
  </p>

  <hr>

  <h2>3. Interpretation</h2>

  <p>
    The range tells us how wide the data extend.
  </p>

  <p>
    It answers:
    <strong>“How far apart are the extreme values?”</strong>
  </p>

  <hr>

  <h2>4. Strengths</h2>

  <ul>
    <li>Very easy to compute</li>
    <li>Easy to interpret</li>
    <li>Useful for quick comparisons</li>
  </ul>

  <hr>

  <h2>5. Weaknesses</h2>

  <ul>
    <li>Uses only two observations</li>
    <li>Highly sensitive to outliers</li>
    <li>Ignores distribution shape</li>
  </ul>

  <p>
    If one extreme value changes, the range changes dramatically.
  </p>

  <hr>

  <h2>6. Outlier Sensitivity Example</h2>

  <p><strong>Dataset A:</strong> 10, 12, 14, 16, 18</p>
  <p>Range = 18 − 10 = 8</p>

  <p><strong>Dataset B:</strong> 10, 12, 14, 16, 50</p>
  <p>Range = 50 − 10 = 40</p>

  <p>
    A single extreme value increased the range fivefold.
  </p>

  <hr>

  <h2>7. When Is Range Useful?</h2>

  <ul>
    <li>Preliminary data exploration</li>
    <li>Quality control limits</li>
    <li>Temperature variation reports</li>
  </ul>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>Range = max − min.</li>
    <li>Simple but limited.</li>
    <li>Extremely sensitive to outliers.</li>
    <li>Should not be used alone for serious analysis.</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/spread/interquartile-range/">
    Next Lesson → Interquartile Range (IQR)
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_spread_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/spread/range/",
    label:"Lesson 2 — Range",
    ts:Date.now()
  }));
})();
</script>