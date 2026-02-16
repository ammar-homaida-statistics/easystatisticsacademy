---
layout: default
title: "Trimmed Mean (Robust Alternative to the Mean)"
description: "How trimming extreme values stabilizes the mean and when it is statistically justified."
permalink: /descriptive/center/trimmed-mean/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/center/weighted-mean/">
    ← Previous Lesson: Weighted Mean
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
        Visual demonstrations, outlier simulations, and software examples (SPSS, R, Python, Excel) will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Trimmed Mean</h1>
    <p class="lead">
      The trimmed mean improves stability by removing extreme observations 
      before calculating the average.
    </p>
  </div>

  <hr>

  <h2>1. Why Trim the Mean?</h2>

  <p>
    The arithmetic mean is highly sensitive to outliers.
  </p>

  <p>
    A single extreme value can significantly shift the average, even if 
    it represents an unusual or accidental observation.
  </p>

  <p>
    The trimmed mean reduces this sensitivity.
  </p>

  <hr>

  <h2>2. What Is a Trimmed Mean?</h2>

  <p>
    A trimmed mean removes a fixed percentage of the smallest and largest values,
    then computes the mean of the remaining data.
  </p>

  <p>
    Common trimming levels:
  </p>

  <ul>
    <li>5% trimmed mean</li>
    <li>10% trimmed mean</li>
    <li>20% trimmed mean</li>
  </ul>

  <p>
    Trimming is always symmetric (same proportion removed from both ends).
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
    (10 + 12 + 13 + 14 + 15 + 100) / 6 = 27.33
  </p>

  <p>
    The value 100 strongly inflates the mean.
  </p>

  <p>
    If we trim one lowest and one highest value:
  </p>

  <p>
    Remaining data: 12, 13, 14, 15
  </p>

  <p>
    Trimmed mean:
  </p>

  <p>
    (12 + 13 + 14 + 15) / 4 = 13.5
  </p>

  <p>
    This better reflects the central pattern.
  </p>

  <hr>

  <h2>4. When Is Trimmed Mean Appropriate?</h2>

  <ul>
    <li>When data contain outliers</li>
    <li>When distribution is moderately skewed</li>
    <li>In robust statistical analysis</li>
  </ul>

  <p>
    It is commonly used in:
  </p>

  <ul>
    <li>Psychological research</li>
    <li>Economic income data</li>
    <li>Experimental studies</li>
  </ul>

  <hr>

  <h2>5. Advantages</h2>

  <ul>
    <li>More robust than the mean</li>
    <li>Uses most of the data (unlike median)</li>
    <li>Balances stability and efficiency</li>
  </ul>

  <hr>

  <h2>6. Limitations</h2>

  <ul>
    <li>Requires arbitrary trimming percentage choice</li>
    <li>Removes real data values</li>
    <li>Still sensitive to remaining extreme values</li>
  </ul>

  <hr>

  <h2>7. Conceptual Comparison</h2>

  <ul>
    <li>Mean → fully sensitive to extremes</li>
    <li>Trimmed mean → partially robust</li>
    <li>Median → fully robust to extreme magnitude</li>
  </ul>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>Trimmed mean removes extreme observations symmetrically.</li>
    <li>It stabilizes the average in skewed data.</li>
    <li>It balances robustness and efficiency.</li>
    <li>Often preferred in applied research when outliers exist.</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/center/winsorized-mean/">
    Next Lesson → Winsorized Mean
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_center_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/center/trimmed-mean/",
    label:"Lesson 7 — Trimmed Mean",
    ts:Date.now()
  }));
})();
</script>