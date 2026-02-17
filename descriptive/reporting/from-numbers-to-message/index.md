---
layout: default
title: "From Numbers to Message (What Reporting Really Is)"
description: "How to transform descriptive outputs into a clear, decision-ready statement."
permalink: /descriptive/reporting/from-numbers-to-message/
sidebar: false
---

<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/reporting/">
    ← Back to Block 7 — Reporting & Practical Integration
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
        This lesson structure is finalized. Examples, visuals, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>From Numbers to Message</h1>
    <p class="lead">
      Reporting is not listing numbers. Reporting means turning descriptive results into a clear message
      that a reader can understand and use.
    </p>
  </div>

  <hr>

  <h2>1) What “Reporting” Means</h2>
  <p>
    Descriptive statistics produce outputs: tables, graphs, means, medians, standard deviations, and percentages.
    Reporting is the step where you answer:
    <strong>“So what does this mean in words?”</strong>
  </p>

  <hr>

  <h2>2) The Reporting Pipeline (Always the Same)</h2>
  <ol>
    <li><strong>Define the context</strong> (population/unit, time, source).</li>
    <li><strong>Describe the data quality</strong> (n, missingness, outliers).</li>
    <li><strong>Summarize center + spread + shape</strong> (with correct measures).</li>
    <li><strong>Make comparisons carefully</strong> (groups/time) using correct denominators.</li>
    <li><strong>Write a message</strong> that is accurate, limited, and decision-ready.</li>
  </ol>

  <hr>

  <h2>3) A Bad Report vs a Good Report</h2>

  <h3>Bad (numbers only)</h3>
  <ul>
    <li>Mean = 83.3, SD = 12.1, Median = 86</li>
    <li>20% are missing</li>
    <li>Group A = 90, Group B = 80</li>
  </ul>

  <h3>Good (message with evidence)</h3>
  <p>
    <strong>Overall performance is high</strong> (median 86), but variability is moderate (SD 12).
    <strong>Results should be interpreted carefully</strong> because 20% of values are missing.
    <strong>Group A scores higher than Group B</strong> by about 10 points, and this comparison uses the same scoring scale.
  </p>

  <hr>

  <h2>4) The “Minimum Reporting Set” (Do Not Skip)</h2>
  <ul>
    <li><strong>What is being measured</strong> (variable + unit).</li>
    <li><strong>Who/what</strong> (observational unit) and <strong>where/when</strong>.</li>
    <li><strong>n</strong> (sample size) and <strong>missingness</strong> (how many, how handled).</li>
    <li><strong>Center</strong> (mean/median/mode — choose valid one).</li>
    <li><strong>Spread</strong> (SD/IQR/range — choose valid one).</li>
    <li><strong>Shape</strong> (skewness/outliers if relevant).</li>
  </ul>

  <hr>

  <h2>5) Safe Language Rules (Avoid Overclaiming)</h2>
  <ul>
    <li>Say <strong>“is higher”</strong> not <strong>“causes”</strong>.</li>
    <li>Say <strong>“in this dataset”</strong> not <strong>“in general”</strong>.</li>
    <li>Say <strong>“associated with”</strong> not <strong>“leads to”</strong>.</li>
    <li>If missingness/outliers exist, mention them explicitly.</li>
  </ul>

  <hr>

  <h2>6) Summary</h2>
  <ul>
    <li>Reporting = numbers + meaning.</li>
    <li>Always include context, n/missingness, center, spread, and shape.</li>
    <li>Use safe language and avoid causal claims.</li>
    <li>A good report is a short message supported by clear evidence.</li>
  </ul>
</section>

<section class="section section-slim">
  <a class="btn" href="/descriptive/reporting/complete-description-checklist/">
    Next Lesson → Complete Description Checklist
  </a>
</section>

<script>
(function(){
  var KEY="esa_continue_descriptive_reporting_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/reporting/from-numbers-to-message/",
    label:"Lesson 1 — From Numbers to Message",
    ts:Date.now()
  }));
})();
</script>