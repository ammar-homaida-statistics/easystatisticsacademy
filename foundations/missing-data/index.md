---
layout: default
title: Missing Data
description: Understanding why data are missing, the consequences of ignoring missingness, and why naive fixes often fail.
permalink: /foundations/missing-data/
section: foundations
lesson_order: 27
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Missing Data">
<meta name="esa-lesson-url" content="/foundations/missing-data/">

<a class="btn btn-primary" href="/foundations/random-error-vs-systematic-error/">
  Previous: Random Error vs Systematic Error
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Missing Data</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Types of missingness (MCAR, MAR, MNAR) will be introduced later.
    </div>

    <p class="lead">
      Missing data are not just gaps.
      They are part of the data-generating process.
      Ignoring how data go missing can lead to misleading conclusions.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 27
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>Why data are missing in real datasets.</li>
      <li>The consequences of ignoring missing values.</li>
      <li>Why naive fixes are appealing but flawed.</li>
      <li>Why missingness is a data problem, not just a technical issue.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why this topic matters</h2>

    <p>
      Missing data are present in almost every real-world dataset.
    </p>

    <p>
      How missing values are handled can change results
      as much as the choice of statistical method.
    </p>

    <p>
      Ignoring missingness can introduce bias,
      even when analysis is otherwise correct.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why data are missing</h2>

    <p>
      Data may be missing because measurements failed,
      responses were skipped, or information was unavailable.
    </p>

    <p>
      People may avoid sensitive questions,
      drop out of studies, or be excluded from data collection.
    </p>

    <p>
      Missingness often reflects real-world behavior,
      not random accidents.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Missingness is not neutral</h2>

    <p>
      Missing values are rarely distributed evenly across data.
    </p>

    <p>
      Certain groups, conditions, or outcomes
      may be more likely to be missing.
    </p>

    <p style="font-weight:600;">
      When data are missing in a patterned way,
      results become biased.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Consequences of ignoring missingness</h2>

    <p>
      Ignoring missing data can distort summaries,
      relationships, and conclusions.
    </p>

    <p>
      Analyses may reflect only the observed subset,
      not the full population.
    </p>

    <p>
      This creates a hidden form of selection bias.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Naive fixes</h2>

    <p>
      Common quick fixes include:
    </p>

    <ul class="bullets">
      <li>Deleting observations with missing values</li>
      <li>Filling missing values with averages</li>
      <li>Replacing values with zeros or defaults</li>
    </ul>

    <p>
      These approaches are easy to apply
      and often supported by software.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why naive fixes fail</h2>

    <p>
      Deleting data reduces sample size
      and may systematically exclude certain groups.
    </p>

    <p>
      Filling in values hides uncertainty
      and artificially reduces variability.
    </p>

    <p>
      These methods treat missing data as a nuisance,
      rather than as part of the problem.
    </p>

    <p style="font-weight:600;">
      Simple fixes often make results look cleaner,
      but less truthful.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Conceptual example</h2>

    <p>
      Suppose income data are missing more often
      for high-income individuals.
    </p>

    <p>
      Calculating the average income
      using only observed data
      will underestimate the true value.
    </p>

    <p>
      The problem is not missing values alone,
      but who is missing.
    </p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Missing data are informative.
      How values go missing matters as much as the values themselves.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Missing data are common and often systematic.
      Ignoring or casually fixing them can introduce bias
      and distort conclusions.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>outliers</strong>,
      explaining what they are, why deleting data is dangerous,
      and when outliers genuinely matter.
    </p>

    <a class="btn btn-primary" href="/foundations/outliers-conceptual-introduction/">
      Next: Outliers
    </a>
  </div>
</section>

<script>
  try {
    localStorage.setItem("esa:lastLesson", window.location.pathname);
  } catch (e) {}
</script>
