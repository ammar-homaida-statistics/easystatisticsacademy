---
layout: default
title: "Variance"
description: "Understanding variance as the average squared deviation from the mean."
permalink: /descriptive/spread/variance/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/spread/interquartile-range/">
    ← Previous Lesson: Interquartile Range (IQR)
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
        Step-by-step derivations, geometric intuition visuals, and software demonstrations (SPSS, R, Python, Excel) will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Variance</h1>
    <p class="lead">
      Variance measures how far observations deviate from the mean — on average —
      using squared deviations.
    </p>
  </div>

  <hr>

  <h2>1. Why Not Just Use Range?</h2>

  <ul>
    <li>Range uses only two values (min & max)</li>
    <li>It ignores most observations</li>
  </ul>

  <p>
    We need a measure that uses <strong>all observations</strong>.
  </p>

  <hr>

  <h2>2. Deviation from the Mean</h2>

  <p>
    For each observation:
  </p>

  <p><strong>Deviation = x − mean</strong></p>

  <p>
    If we simply average deviations, they cancel out (sum = 0).
  </p>

  <p>
    Solution: square them.
  </p>

  <hr>

  <h2>3. Population Variance Formula</h2>

  <p>
    σ² = Σ(x − μ)² / N
  </p>

  <ul>
    <li>μ = population mean</li>
    <li>N = population size</li>
  </ul>

  <hr>

  <h2>4. Sample Variance Formula</h2>

  <p>
    s² = Σ(x − x̄)² / (n − 1)
  </p>

  <ul>
    <li>x̄ = sample mean</li>
    <li>n = sample size</li>
    <li>n − 1 = degrees of freedom</li>
  </ul>

  <p>
    Dividing by (n − 1) corrects bias in sample estimation.
  </p>

  <hr>

  <h2>5. Example</h2>

  <p><strong>Dataset:</strong> 4, 6, 8</p>

  <p>
    Mean = 6
  </p>

  <p>
    Deviations:
  </p>

  <ul>
    <li>4 − 6 = −2 → squared = 4</li>
    <li>6 − 6 = 0 → squared = 0</li>
    <li>8 − 6 = 2 → squared = 4</li>
  </ul>

  <p>
    Sum of squared deviations = 8
  </p>

  <p>
    Sample variance:
  </p>

  <p>
    s² = 8 / (3 − 1) = 8 / 2 = 4
  </p>

  <hr>

  <h2>6. Interpretation</h2>

  <p>
    Variance measures the average squared distance from the mean.
  </p>

  <p>
    Larger variance → greater dispersion.
  </p>

  <hr>

  <h2>7. Important Properties</h2>

  <ul>
    <li>Always non-negative</li>
    <li>Uses all observations</li>
    <li>Sensitive to extreme values</li>
    <li>Unit is squared (e.g., cm², dollars²)</li>
  </ul>

  <hr>

  <h2>8. Why Squared Units Matter</h2>

  <p>
    Variance is not in the original measurement unit.
  </p>

  <p>
    This makes interpretation less intuitive.
  </p>

  <p>
    Solution → take the square root.
  </p>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>Variance = average squared deviation from mean</li>
    <li>Uses all data points</li>
    <li>Sensitive to outliers</li>
    <li>Measured in squared units</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/spread/standard-deviation/">
    Next Lesson → Standard Deviation
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_spread_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/spread/variance/",
    label:"Lesson 4 — Variance",
    ts:Date.now()
  }));
})();
</script>