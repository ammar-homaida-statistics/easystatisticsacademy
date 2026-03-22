---
layout: default
title: Outliers
description: A conceptual introduction to outliers, natural versus erroneous outliers, why deleting data is dangerous, and when outliers matter.
permalink: /foundations/outliers-conceptual-introduction/
section: foundations
lesson_order: 28
---

<meta name="esa-section" content="foundations">
<meta name="esa-lesson-title" content="Outliers">
<meta name="esa-lesson-url" content="/foundations/outliers-conceptual-introduction/">

<a class="btn btn-primary" href="/foundations/missing-data/">
  Previous: Missing Data
</a>

<section class="hero hero-lesson">
  <div class="hero-card">
    <h1>Outliers</h1>

    <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
      <strong>🚧 Under Construction</strong> — Formal detection methods (IQR, z-scores) will be introduced later.
    </div>

    <p class="lead">
      Outliers are extreme observations, but they are not automatically errors.
      Removing them without understanding their origin can distort results
      and hide important information.
    </p>

    <p class="muted-mini">
      Section: <strong>Statistics Foundations</strong> • Lesson 28
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What you will learn</h2>

    <ul class="bullets">
      <li>What outliers are in a dataset.</li>
      <li>The difference between natural and erroneous outliers.</li>
      <li>Why deleting outliers can be misleading.</li>
      <li>How to think about outliers before taking action.</li>
    </ul>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why this topic matters</h2>

    <p>
      Outliers often trigger immediate reactions during analysis.
    </p>

    <p>
      They can strongly influence results,
      especially averages and statistical models.
    </p>

    <p>
      Incorrect handling of outliers can lead
      to misleading conclusions and false confidence.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>What outliers are</h2>

    <p>
      An outlier is an observation that lies far from
      the bulk of the data.
    </p>

    <p>
      Outliers are defined relative to the dataset,
      not by a universal numerical threshold.
    </p>

    <p>
      What counts as an outlier depends on context,
      variability, and measurement.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Outliers are not automatically errors</h2>

    <p>
      A common mistake is to assume that extreme values
      must be incorrect.
    </p>

    <p>
      In many cases, outliers represent real but rare events.
    </p>

    <p style="font-weight:600;">
      Extreme does not mean wrong.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Natural vs erroneous outliers</h2>

    <p>
      <strong>Natural outliers</strong> reflect genuine variation
      in the real world.
    </p>

    <p>
      <strong>Erroneous outliers</strong> arise from mistakes,
      such as data entry errors or faulty measurements.
    </p>

    <p>
      Distinguishing between them requires
      context and domain knowledge,
      not just statistical rules.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Why deleting data is dangerous</h2>

    <p>
      Removing outliers changes the dataset
      and therefore changes the conclusions.
    </p>

    <p>
      Deletion may hide important variability
      or remove meaningful rare events.
    </p>

    <p>
      In some cases, removing outliers
      removes exactly the phenomenon of interest.
    </p>

    <p style="font-weight:600;">
      Deleting data is a modeling decision,
      not a cleaning step.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>Conceptual example</h2>

    <p>
      Suppose income data include a small number
      of very high earners.
    </p>

    <p>
      Removing these values may produce a more “stable” average,
      but it no longer represents the true distribution.
    </p>

    <p>
      The outliers are not errors.
      They are part of the population.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>When outliers matter</h2>

    <p>
      Outliers can strongly influence means,
      correlations, and regression models.
    </p>

    <p>
      In risk analysis, finance, and safety studies,
      extreme values may be the most important observations.
    </p>

    <p>
      Whether outliers matter depends on
      the question being asked.
    </p>
  </div>
</section>



<section class="section">
  <div class="content-narrow">
    <h2>How to think before acting</h2>

    <p>
      Before removing an outlier, ask:
    </p>

    <ul class="bullets">
      <li>Is this value plausible in the real world?</li>
      <li>Could this be a measurement or recording error?</li>
      <li>What happens to results if it is removed?</li>
      <li>Does the research question require including extremes?</li>
    </ul>

    <p>
      These questions are more important
      than any automatic rule.
    </p>
  </div>
</section>



<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Outliers require explanation, not reflexive removal.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Outliers are extreme observations that may represent
      real variation or errors.
      Removing them without understanding their origin
      can distort analysis and conclusions.
    </p>
  </div>
</section>



<section class="section section-next">
  <div class="content-narrow">
    <h2>What comes next</h2>

    <p>
      The next lesson introduces <strong>descriptive statistics</strong>,
      explaining what summaries like means and medians capture,
      and what they fail to reveal.
    </p>

    <a class="btn btn-primary" href="/foundations/descriptive-statistics-conceptual-overview/">
      Next: Descriptive Statistics
    </a>
  </div>
</section>

<script>
  try {
    localStorage.setItem("esa:lastLesson", window.location.pathname);
  } catch (e) {}
</script>
