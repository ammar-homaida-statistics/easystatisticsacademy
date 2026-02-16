---
layout: default
title: "Coefficient of Variation"
description: "Relative variability: comparing spread across different scales and units using the coefficient of variation."
permalink: /descriptive/spread/coefficient-of-variation/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/spread/standard-deviation/">
    ← Previous Lesson: Standard Deviation
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
        Real business comparisons, risk interpretation examples, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Coefficient of Variation (CV)</h1>
    <p class="lead">
      The coefficient of variation measures relative variability.
      It expresses standard deviation as a proportion of the mean.
    </p>
  </div>

  <hr>

  <h2>1. Why Do We Need CV?</h2>

  <p>
    Standard deviation depends on the measurement unit.
  </p>

  <p>
    Example:
  </p>

  <ul>
    <li>SD of income (dollars)</li>
    <li>SD of height (cm)</li>
  </ul>

  <p>
    These cannot be directly compared.
  </p>

  <p>
    CV removes units.
  </p>

  <hr>

  <h2>2. Formula</h2>

  <p style="font-weight:bold;">
    CV = (Standard Deviation / Mean) × 100%
  </p>

  <p>
    Or in symbols:
  </p>

  <p>
    CV = (s / x̄) × 100%
  </p>

  <ul>
    <li>Unit-free (dimensionless)</li>
    <li>Usually expressed as a percentage</li>
  </ul>

  <hr>

  <h2>3. Example</h2>

  <p><strong>Company A:</strong></p>
  <ul>
    <li>Mean salary = 1,000</li>
    <li>SD = 100</li>
  </ul>

  <p>
    CV = 100 / 1,000 = 0.10 → 10%
  </p>

  <p><strong>Company B:</strong></p>
  <ul>
    <li>Mean salary = 10,000</li>
    <li>SD = 500</li>
  </ul>

  <p>
    CV = 500 / 10,000 = 0.05 → 5%
  </p>

  <p>
    Although Company B has larger SD,
    it has lower relative variability.
  </p>

  <hr>

  <h2>4. Interpretation</h2>

  <ul>
    <li>Low CV → stable / consistent data</li>
    <li>High CV → high relative dispersion</li>
    <li>Useful in finance and risk analysis</li>
  </ul>

  <hr>

  <h2>5. When NOT to Use CV</h2>

  <ul>
    <li>When mean ≈ 0 (unstable ratio)</li>
    <li>With interval scales lacking true zero</li>
    <li>With negative means (interpretation problem)</li>
  </ul>

  <hr>

  <h2>6. Comparison with Other Measures</h2>

  <ul>
    <li>Range → simple, unstable</li>
    <li>IQR → robust</li>
    <li>SD → absolute variability</li>
    <li>CV → relative variability</li>
  </ul>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>CV compares variability across scales.</li>
    <li>Unit-free measure.</li>
    <li>Common in finance and economics.</li>
    <li>Unstable when mean is near zero.</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/spread/reporting-spread-properly/">
    Next Lesson → Reporting Spread Properly
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_spread_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/spread/coefficient-of-variation/",
    label:"Lesson 6 — Coefficient of Variation",
    ts:Date.now()
  }));
})();
</script>