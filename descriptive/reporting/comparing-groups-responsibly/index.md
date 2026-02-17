---
layout: default
title: "Comparing Groups Responsibly"
description: "How to compare groups using context, correct denominators, spread, and careful language."
permalink: /descriptive/reporting/comparing-groups-responsibly/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/reporting/reporting-graphs-properly/">
    ← Previous Lesson: Reporting Graphs Properly
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
        Real comparison examples, matched-denominator demonstrations, and misleading comparison case studies will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Comparing Groups Responsibly</h1>
    <p class="lead">
      Comparing groups is one of the most common statistical tasks.
      It is also one of the most frequently misreported.
    </p>
  </div>

  <hr>

  <h2>1. Always Compare Like with Like</h2>

  <p>
    Before comparing groups, ask:
  </p>

  <ul>
    <li>Are units measured in the same way?</li>
    <li>Are denominators comparable?</li>
    <li>Are sample sizes very different?</li>
  </ul>

  Comparing percentages with raw counts is incorrect.  
  Comparing means without checking spread can be misleading.

  <hr>

  <h2>2. Report Center and Spread Together</h2>

  Weak comparison:

  ❌ “Group A scored 80, Group B scored 75.”

  Strong comparison:

  ✔ “Group A had a higher mean score (80 vs 75), but also showed greater variability (SD = 12 vs 6).”

  Center alone does not describe performance stability.

  <hr>

  <h2>3. Consider Distribution Shape</h2>

  If one group is skewed and the other is symmetric:
  - The mean comparison may be unstable.
  - The median may be more appropriate.

  Distribution shape affects fairness of comparison.

  <hr>

  <h2>4. Use Matched Denominators</h2>

  Example mistake:

  ❌ Comparing total hospital cases to regional population without standardization.

  Correct approach:

  ✔ Compare rates (per 1000 people).  
  ✔ Use proportions when denominators differ.

  Always align scales before comparing.

  <hr>

  <h2>5. Avoid Overstating Differences</h2>

  Words matter.

  Avoid:
  - “Much higher”
  - “Dramatically larger”
  - “Significantly different” (unless inferential test used)

  Prefer:
  - “Higher by 5 points”
  - “Moderately larger”
  - “Slight difference observed”

  Descriptive statistics should describe — not exaggerate.

  <hr>

  <h2>6. Visual Comparisons Must Be Honest</h2>

  <ul>
    <li>Same axis scale for both groups</li>
    <li>No truncation that exaggerates difference</li>
    <li>Clear labeling of group sizes</li>
  </ul>

  A small scaling change can visually double a perceived difference.

  <hr>

  <h2>7. Context Always Matters</h2>

  A difference of 5 units:
  - Might be large in test scores.
  - Might be negligible in income data.

  Interpretation depends on domain context.

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>Compare matched quantities.</li>
    <li>Report center and spread together.</li>
    <li>Check distribution shape before choosing mean vs median.</li>
    <li>Avoid exaggerated language.</li>
    <li>Always interpret within context.</li>
  </ul>

</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/reporting/association-not-causation/">
    Next Lesson → Association ≠ Causation (Safe Interpretation)
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_reporting_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/reporting/comparing-groups-responsibly/",
    label:"Lesson 6 — Comparing Groups Responsibly",
    ts:Date.now()
  }));
})();
</script>