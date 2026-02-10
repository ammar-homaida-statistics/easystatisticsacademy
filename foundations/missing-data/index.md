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

    <p class="lead">
      This lesson explains why data are missing, why ignoring missingness
      can distort conclusions, and why simple fixes often make problems worse.
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
      Missing data are common in almost every real-world dataset.
    </p>

    <p>
      Decisions about how to handle missing values
      directly affect conclusions.
    </p>

    <p>
      Treating missingness casually can introduce bias
      even when analysis is otherwise correct.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Why data are missing</h2>

    <p>
      Data may be missing because measurements failed,
      questions were skipped, or information was unavailable.
    </p>

    <p>
      People may refuse to answer sensitive questions
      or drop out of studies.
    </p>

    <p>
      Missingness often reflects real-world processes,
      not random accidents.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Consequences of ignoring missingness</h2>

    <p>
      Ignoring missing data can distort summaries
      and relationships.
    </p>

    <p>
      If missingness is systematic,
      results may become biased.
    </p>

    <p>
      Conclusions may reflect who is observed,
      not the full population.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Naive fixes</h2>

    <p>
      Common quick fixes include deleting missing values
      or filling them with averages.
    </p>

    <p>
      These approaches are easy to apply
      and often supported by software.
    </p>

    <p>
      However, simplicity does not imply correctness.
    </p>
  </div>
</section>

<section class="section">
  <div class="content-narrow">
    <h2>Why naive fixes fail</h2>

    <p>
      Deleting data reduces sample size
      and may change who is represented.
    </p>

    <p>
      Filling in values can hide uncertainty
      and distort variability.
    </p>

    <p>
      Naive fixes treat symptoms
      without addressing underlying causes.
    </p>
  </div>
</section>

<section class="section section-soft">
  <div class="content-narrow">
    <h2>Key idea to remember</h2>

    <p>
      Missing data are informative.
      How values go missing matters.
    </p>
  </div>
</section>

<section class="section section-next">
  <div class="content-narrow">
    <h2>Simple summary</h2>

    <p>
      Missing data are common and consequential.
      Ignoring or casually fixing them can bias results
      and reduce reliability.
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