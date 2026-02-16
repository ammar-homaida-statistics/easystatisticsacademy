---
layout: default
title: "Center for Ordinal Data (What Is Valid?)"
description: "Which measures of center are valid for ordinal variables and why mean is often inappropriate."
permalink: /descriptive/center/center-for-ordinal-data/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/center/winsorized-mean/">
    ← Previous Lesson: Winsorized Mean
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
        Visual examples, Likert-scale datasets, and software demonstrations (SPSS, R, Python, Excel) will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Center for Ordinal Data</h1>
    <p class="lead">
      Not all measures of center are valid for all variable types.
      Ordinal variables require careful interpretation.
    </p>
  </div>

  <hr>

  <h2>1. What Is Ordinal Data?</h2>

  <p>
    Ordinal variables have categories with order,
    but the distances between categories are not equal.
  </p>

  <p><strong>Examples:</strong></p>

  <ul>
    <li>Education level: High school, Bachelor, Master, PhD</li>
    <li>Likert scale: Strongly disagree → Strongly agree</li>
    <li>Pain scale: Mild → Moderate → Severe</li>
  </ul>

  <hr>

  <h2>2. Why the Mean Is Problematic</h2>

  <p>
    The mean assumes equal spacing between values.
  </p>

  <p>
    But in ordinal data:
  </p>

  <ul>
    <li>The gap between “Agree” and “Strongly Agree” is unknown</li>
    <li>Numerical coding (1,2,3,4,5) does not guarantee equal distance</li>
  </ul>

  <p>
    Therefore, arithmetic mean may not be conceptually valid.
  </p>

  <hr>

  <h2>3. Appropriate Measures of Center for Ordinal Data</h2>

  <h3>✔ Median</h3>

  <ul>
    <li>Based on order, not distance</li>
    <li>Always valid for ordinal variables</li>
  </ul>

  <h3>✔ Mode</h3>

  <ul>
    <li>Most frequent category</li>
    <li>Always valid</li>
  </ul>

  <h3>⚠ Mean (With Caution)</h3>

  <ul>
    <li>Often used for Likert scales in practice</li>
    <li>Technically assumes equal spacing</li>
    <li>Should be justified carefully</li>
  </ul>

  <hr>

  <h2>4. Example — Likert Scale</h2>

  <p>
    1 = Strongly disagree  
    2 = Disagree  
    3 = Neutral  
    4 = Agree  
    5 = Strongly agree
  </p>

  <p>
    Responses:
  </p>

  <p>
    4, 4, 3, 5, 4, 2, 4
  </p>

  <p>
    Median = 4 (Agree)  
    Mode = 4  
    Mean ≈ 3.71
  </p>

  <p>
    The median communicates the central category more clearly.
  </p>

  <hr>

  <h2>5. Reporting Recommendation</h2>

  <ul>
    <li>Primary: Report median and distribution</li>
    <li>Optional: Report mean with caution (if justified)</li>
    <li>Always show category percentages</li>
  </ul>

  <hr>

  <h2>6. Conceptual Rule</h2>

  <p style="font-weight:bold;">
    If distances are unknown → Avoid mean.
  </p>

  <p>
    If scale behaves approximately interval (e.g., validated Likert index),
    mean may be acceptable with justification.
  </p>

  <hr>

  <h2>Common Mistakes</h2>

  <ul>
    <li>Automatically calculating mean for ordinal variables</li>
    <li>Ignoring distribution shape</li>
    <li>Failing to report category percentages</li>
  </ul>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>Median and mode are valid for ordinal data.</li>
    <li>Mean assumes equal spacing.</li>
    <li>Always consider the measurement scale before computing center.</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/center/reporting-center-properly/">
    Next Lesson → Reporting Center Properly
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_center_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/center/center-for-ordinal-data/",
    label:"Lesson 9 — Center for Ordinal Data",
    ts:Date.now()
  }));
})();
</script>