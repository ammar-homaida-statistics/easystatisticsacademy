---
layout: default
title: "Winsorized Mean (Outlier Control Without Deletion)"
description: "How Winsorization reduces the influence of extreme values without removing observations."
permalink: /descriptive/center/winsorized-mean/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/center/trimmed-mean/">
    ← Previous Lesson: Trimmed Mean
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
        Visual comparisons, simulation examples, and software demonstrations (SPSS, R, Python, Excel) will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Winsorized Mean</h1>
    <p class="lead">
      The Winsorized mean reduces the influence of extreme values 
      by replacing them instead of removing them.
    </p>
  </div>

  <hr>

  <h2>1. Why Not Simply Delete Outliers?</h2>

  <p>
    Removing extreme values (as in trimmed mean) reduces sensitivity,
    but it also reduces sample size.
  </p>

  <p>
    In some contexts, deleting observations is undesirable because:
  </p>

  <ul>
    <li>It changes sample size</li>
    <li>It discards real data</li>
    <li>It may introduce bias</li>
  </ul>

  <p>
    Winsorization offers a compromise.
  </p>

  <hr>

  <h2>2. What Is a Winsorized Mean?</h2>

  <p>
    Instead of removing extreme observations, we replace them 
    with the nearest remaining values after trimming.
  </p>

  <p>
    Example: 10% Winsorization replaces the lowest 10% 
    with the next smallest value and the highest 10% 
    with the next largest value.
  </p>

  <hr>

  <h2>3. Example</h2>

  <p><strong>Data:</strong></p>

  <p>
    10, 12, 13, 14, 15, 100
  </p>

  <p>
    Arithmetic mean:
  </p>

  <p>
    27.33
  </p>

  <p>
    Trimmed mean (remove 10 and 100):
  </p>

  <p>
    13.5
  </p>

  <p>
    Winsorized version:
  </p>

  <p>
    Replace 10 → 12  
    Replace 100 → 15
  </p>

  <p>
    New dataset:
  </p>

  <p>
    12, 12, 13, 14, 15, 15
  </p>

  <p>
    Winsorized mean:
  </p>

  <p>
    (12 + 12 + 13 + 14 + 15 + 15) / 6 = 13.5
  </p>

  <p>
    Notice that the sample size remains 6.
  </p>

  <hr>

  <h2>4. When Is Winsorization Appropriate?</h2>

  <ul>
    <li>When extreme values exist but should not be deleted</li>
    <li>In robust statistical procedures</li>
    <li>When preserving sample size is important</li>
  </ul>

  <hr>

  <h2>5. Comparison: Mean vs Trimmed vs Winsorized</h2>

  <ul>
    <li><strong>Mean:</strong> Fully sensitive to extremes</li>
    <li><strong>Trimmed mean:</strong> Deletes extremes</li>
    <li><strong>Winsorized mean:</strong> Replaces extremes</li>
  </ul>

  <hr>

  <h2>6. Advantages</h2>

  <ul>
    <li>Reduces outlier influence</li>
    <li>Maintains sample size</li>
    <li>More stable than the mean</li>
  </ul>

  <hr>

  <h2>7. Limitations</h2>

  <ul>
    <li>Requires choosing a Winsorization level</li>
    <li>Still modifies original data</li>
    <li>Not appropriate if extremes are meaningful signals</li>
  </ul>

  <hr>

  <h2>8. Interpretation</h2>

  <p>
    The Winsorized mean represents a robust average 
    that limits the influence of extreme values 
    without discarding observations.
  </p>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>Winsorization replaces extreme values instead of removing them.</li>
    <li>It reduces sensitivity to outliers.</li>
    <li>It preserves sample size.</li>
    <li>Often used in robust statistical methods.</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/center/center-for-ordinal-data/">
    Next Lesson → Center for Ordinal Data
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_center_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/center/winsorized-mean/",
    label:"Lesson 8 — Winsorized Mean",
    ts:Date.now()
  }));
})();
</script>