---
layout: default
title: "Skewness and Choosing Mean vs Median"
description: "How skewness affects the mean and why the median is often more reliable in skewed data."
permalink: /descriptive/shape/skewness-and-center-choice/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/shape/symmetry-and-skewness/">
    ← Previous Lesson: Symmetry and Skewness
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
        Visual comparisons and software demonstrations (SPSS, R, Python, Excel) will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">

  <div class="section-head">
    <h1>Skewness and Choosing Mean vs Median</h1>
    <p class="lead">
      Skewness changes how we interpret center.  
      In skewed distributions, the mean can become unstable — and the median often becomes the safer summary.
    </p>
  </div>

  <hr>

  <h2>1. Why Skewness Affects the Mean</h2>

  <p>
    The mean uses all values in the dataset.
    Because it is calculated from numerical magnitudes, it is pulled toward extreme values.
  </p>

  <p>
    In a right-skewed distribution:
  </p>

  <ul>
    <li>Large values stretch the right tail</li>
    <li>The mean shifts upward</li>
    <li>The mean becomes larger than the median</li>
  </ul>

  <p>
    In a left-skewed distribution:
  </p>

  <ul>
    <li>Small extreme values stretch the left tail</li>
    <li>The mean shifts downward</li>
    <li>The mean becomes smaller than the median</li>
  </ul>

  <hr>

  <h2>2. The Median Is Position-Based</h2>

  <p>
    The median depends only on order — not magnitude.
  </p>

  <p>
    Extreme values change the mean significantly,  
    but they barely affect the median.
  </p>

  <p>
    This makes the median a <strong>robust measure of center</strong>.
  </p>

  <hr>

  <h2>3. Practical Example — Income</h2>

  <p>
    Suppose a neighborhood has incomes:
  </p>

  <p>
    30, 35, 40, 45, 50, 200
  </p>

  <p>
    Mean = (30 + 35 + 40 + 45 + 50 + 200) / 6 = 66.7  
    Median = (40 + 45) / 2 = 42.5
  </p>

  <p>
    The single extreme income inflates the mean.
  </p>

  <p>
    The median better reflects the “typical” resident.
  </p>

  <hr>

  <h2>4. Decision Rule</h2>

  <ul>
    <li>Symmetric distribution → mean is appropriate</li>
    <li>Mild skewness → mean and median may both be reported</li>
    <li>Strong skewness or outliers → median is safer</li>
  </ul>

  <hr>

  <h2>5. Mean vs Median Pattern</h2>

  <ul>
    <li>Right-skewed → Mean &gt; Median</li>
    <li>Left-skewed → Mean &lt; Median</li>
    <li>Symmetric → Mean ≈ Median</li>
  </ul>

  <hr>

  <h2>6. Interpretation Warning</h2>

  <p>
    Reporting only the mean in skewed data can mislead.
  </p>

  <p>
    Always check distribution shape before choosing your summary.
  </p>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>Skewness pulls the mean toward the tail.</li>
    <li>The median is resistant to extreme values.</li>
    <li>Distribution shape determines the appropriate measure of center.</li>
    <li>Never choose a summary blindly.</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/shape/tails-outliers-and-extremes/">
    Next Lesson → Tails, Outliers, and Extreme Values
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_shape_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/shape/skewness-and-center-choice/",
    label:"Lesson 3 — Skewness and Choosing Mean vs Median",
    ts:Date.now()
  }));
})();
</script>