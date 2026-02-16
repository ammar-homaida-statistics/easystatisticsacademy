---
layout: default
title: "Standard Deviation"
description: "Understanding standard deviation as the square root of variance and the most interpretable measure of spread."
permalink: /descriptive/spread/standard-deviation/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/spread/variance/">
    ← Previous Lesson: Variance
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
        Visual distribution comparisons, empirical rule demonstrations, and software implementations (SPSS, R, Python, Excel) will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Standard Deviation</h1>
    <p class="lead">
      Standard deviation measures the typical distance of observations from the mean,
      expressed in the original measurement unit.
    </p>
  </div>

  <hr>

  <h2>1. Why Do We Need Standard Deviation?</h2>

  <p>
    Variance uses squared units (e.g., cm², dollars²).
  </p>

  <p>
    This makes interpretation unintuitive.
  </p>

  <p>
    Solution:
  </p>

  <p><strong>Standard Deviation = √Variance</strong></p>

  <hr>

  <h2>2. Formulas</h2>

  <h3>Population Standard Deviation</h3>

  <p>
    σ = √[ Σ(x − μ)² / N ]
  </p>

  <h3>Sample Standard Deviation</h3>

  <p>
    s = √[ Σ(x − x̄)² / (n − 1) ]
  </p>

  <ul>
    <li>Uses same logic as variance</li>
    <li>Expressed in original unit</li>
  </ul>

  <hr>

  <h2>3. Example</h2>

  <p><strong>Dataset:</strong> 4, 6, 8</p>

  <p>
    From previous lesson:
  </p>

  <ul>
    <li>Mean = 6</li>
    <li>Sample variance = 4</li>
  </ul>

  <p>
    Standard deviation:
  </p>

  <p>
    s = √4 = 2
  </p>

  <p>
    Interpretation:
  </p>

  <p>
    On average, values are about 2 units away from the mean.
  </p>

  <hr>

  <h2>4. Interpretation</h2>

  <ul>
    <li>Small SD → values are tightly clustered around mean</li>
    <li>Large SD → values are widely spread</li>
    <li>Same unit as original data</li>
  </ul>

  <hr>

  <h2>5. Conceptual Meaning</h2>

  <p>
    Standard deviation approximates the “typical distance” from the mean.
  </p>

  <p>
    It is not the maximum distance.
  </p>

  <hr>

  <h2>6. Sensitivity to Outliers</h2>

  <p>
    Because it is based on squared deviations,
    extreme values increase SD substantially.
  </p>

  <p>
    Compare:
  </p>

  <ul>
    <li>4, 6, 8 → small SD</li>
    <li>4, 6, 20 → much larger SD</li>
  </ul>

  <hr>

  <h2>7. Relationship to Normal Distribution</h2>

  <p>
    In approximately normal data:
  </p>

  <ul>
    <li>~68% within ±1 SD</li>
    <li>~95% within ±2 SD</li>
    <li>~99.7% within ±3 SD</li>
  </ul>

  <p>
    (Empirical Rule — detailed later)
  </p>

  <hr>

  <h2>8. Comparison with IQR</h2>

  <ul>
    <li>Standard deviation → mean-based, sensitive to outliers</li>
    <li>IQR → median-based, resistant to outliers</li>
  </ul>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>SD = square root of variance</li>
    <li>Measured in original unit</li>
    <li>Represents typical distance from mean</li>
    <li>Sensitive to extreme values</li>
    <li>Central for inferential statistics</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/spread/coefficient-of-variation/">
    Next Lesson → Coefficient of Variation
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_spread_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/spread/standard-deviation/",
    label:"Lesson 5 — Standard Deviation",
    ts:Date.now()
  }));
})();
</script>