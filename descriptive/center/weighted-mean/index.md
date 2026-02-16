---
layout: default
title: "Weighted Mean"
description: "How and when to use the weighted mean for grouped data, grades, and index construction."
permalink: /descriptive/center/weighted-mean/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/center/mode/">
    ← Previous Lesson: Mode
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
        Real datasets, grouped-data applications, and software demonstrations (SPSS, R, Python, Excel) will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Weighted Mean</h1>
    <p class="lead">
      The weighted mean adjusts the average when observations do not contribute equally.
      Some values carry more importance (weight) than others.
    </p>
  </div>

  <hr>

  <h2>1. Why Do We Need a Weighted Mean?</h2>

  <p>
    The regular mean assumes that all observations contribute equally.
  </p>

  <p>
    But in many real situations:
  </p>

  <ul>
    <li>Courses have different credit hours</li>
    <li>Survey responses have sampling weights</li>
    <li>Grouped data represents multiple observations per class</li>
  </ul>

  <p>
    In these cases, a simple average is incorrect.
  </p>

  <hr>

  <h2>2. Formula</h2>

  <p>
    If values are x<sub>i</sub> and weights are w<sub>i</sub>, the weighted mean is:
  </p>

  <p style="font-weight:bold;">
    Weighted Mean = Σ(wᵢ xᵢ) / Σ(wᵢ)
  </p>

  <p>
    The weights determine the influence of each value.
  </p>

  <hr>

  <h2>3. Example — Course Grades</h2>

  <p><strong>Student grades:</strong></p>

  <ul>
    <li>Statistics: 90 (3 credits)</li>
    <li>Economics: 80 (2 credits)</li>
    <li>History: 70 (1 credit)</li>
  </ul>

  <p>
    Simple mean:
  </p>

  <p>
    (90 + 80 + 70) / 3 = 80
  </p>

  <p>
    Weighted mean:
  </p>

  <p>
    (90×3 + 80×2 + 70×1) / (3+2+1)
  </p>

  <p>
    = (270 + 160 + 70) / 6  
    = 500 / 6  
    = 83.33
  </p>

  <p>
    The weighted mean better reflects academic performance.
  </p>

  <hr>

  <h2>4. Weighted Mean for Grouped Data</h2>

  <p>
    In grouped frequency tables, the class midpoint acts as the value,
    and frequency acts as the weight.
  </p>

  <p>
    Mean ≈ Σ(midpoint × frequency) / total frequency
  </p>

  <p>
    This is how we estimate the mean from binned data.
  </p>

  <hr>

  <h2>5. Properties</h2>

  <ul>
    <li>If all weights are equal → weighted mean = regular mean</li>
    <li>Larger weights increase influence</li>
    <li>Still sensitive to extreme values</li>
  </ul>

  <hr>

  <h2>6. Common Mistakes</h2>

  <ul>
    <li>Forgetting to divide by total weight</li>
    <li>Using frequencies incorrectly</li>
    <li>Confusing weighted mean with simple mean</li>
  </ul>

  <hr>

  <h2>7. Interpretation</h2>

  <p>
    The weighted mean represents the central value after accounting for importance or frequency.
  </p>

  <p>
    It answers:
    <strong>“What is the average when some observations count more than others?”</strong>
  </p>

  <hr>

  <h2>Conceptual Comparison</h2>

  <ul>
    <li>Mean → equal contribution</li>
    <li>Weighted mean → unequal contribution</li>
    <li>Median → position-based</li>
    <li>Mode → frequency-based</li>
  </ul>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>Weighted mean adjusts for unequal importance.</li>
    <li>Essential for grouped data and academic grading.</li>
    <li>Still sensitive to outliers.</li>
    <li>Reduces bias when contributions differ.</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/center/comparing-mean-median-mode/">
    Next Lesson → Comparing Mean, Median & Mode
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_center_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/center/weighted-mean/",
    label:"Lesson 5 — Weighted Mean",
    ts:Date.now()
  }));
})();
</script>