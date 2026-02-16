---
layout: default
title: "Interquartile Range (IQR)"
description: "A robust measure of spread based on quartiles and the middle 50% of the data."
permalink: /descriptive/spread/interquartile-range/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/spread/range/">
    ← Previous Lesson: Range
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
        Step-by-step quartile calculations, boxplot visuals, and software demonstrations (SPSS, R, Python, Excel) will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Interquartile Range (IQR)</h1>
    <p class="lead">
      The Interquartile Range (IQR) measures the spread of the middle 50% of the data.
      Unlike the range, it is resistant to extreme values.
    </p>
  </div>

  <hr>

  <h2>1. Quartiles Review</h2>

  <ul>
    <li><strong>Q1</strong> = 25th percentile</li>
    <li><strong>Q2</strong> = Median (50th percentile)</li>
    <li><strong>Q3</strong> = 75th percentile</li>
  </ul>

  <p>
    Quartiles divide ordered data into four equal parts.
  </p>

  <hr>

  <h2>2. Definition of IQR</h2>

  <p><strong>IQR = Q3 − Q1</strong></p>

  <p>
    It measures the spread of the central half of the data.
  </p>

  <hr>

  <h2>3. Example</h2>

  <p><strong>Dataset (ordered):</strong></p>

  <p>5, 7, 8, 10, 12, 15, 18, 20</p>

  <p>
    Q1 = 7.5  
    Q3 = 16.5
  </p>

  <p>
    IQR = 16.5 − 7.5 = 9
  </p>

  <hr>

  <h2>4. Interpretation</h2>

  <p>
    The IQR describes the variability of the typical observations.
  </p>

  <p>
    It answers:
    <strong>“How spread out are the middle 50% of values?”</strong>
  </p>

  <hr>

  <h2>5. Why IQR Is Important</h2>

  <ul>
    <li>Resistant to outliers</li>
    <li>Better for skewed distributions</li>
    <li>Foundation of boxplots</li>
  </ul>

  <hr>

  <h2>6. Outlier Detection Rule</h2>

  <p>
    Lower bound = Q1 − 1.5 × IQR  
    Upper bound = Q3 + 1.5 × IQR
  </p>

  <p>
    Values outside these limits are considered potential outliers.
  </p>

  <hr>

  <h2>7. Comparison with Range</h2>

  <ul>
    <li>Range uses only extremes</li>
    <li>IQR uses central distribution</li>
    <li>IQR is robust; range is not</li>
  </ul>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>IQR = Q3 − Q1</li>
    <li>Measures middle 50% spread</li>
    <li>Robust to outliers</li>
    <li>Essential for boxplot interpretation</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/spread/variance/">
    Next Lesson → Variance
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_spread_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/spread/interquartile-range/",
    label:"Lesson 3 — Interquartile Range (IQR)",
    ts:Date.now()
  }));
})();
</script>