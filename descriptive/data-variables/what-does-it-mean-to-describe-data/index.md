---
layout: default
title: "What Does It Mean to “Describe” Data?"
description: "Descriptive vs inferential statistics, description vs explanation, and why correct description matters."
permalink: /descriptive/data-variables/what-does-it-mean-to-describe-data/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/data-variables/">
    ← Back to Block 1 — Data & Variables
  </a>
</section>

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This lesson is being developed. Content will be expanded while preserving the structure and examples.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>What Does It Mean to “Describe” Data?</h1>
    <p>
      Descriptive statistics is the foundation of all statistical work.
      Before modeling, testing, or predicting, we must first describe the data correctly.
    </p>
  </div>

  <h2>1. Descriptive vs Inferential Statistics</h2>

  <p><strong>Descriptive statistics</strong> summarizes and organizes data.</p>
  <p><strong>Inferential statistics</strong> uses data to make conclusions about a larger population.</p>

  <p>Example:</p>
  <ul>
    <li>“The average exam score of these 40 students is 72.” → Descriptive</li>
    <li>“The average score of all students in the university is likely around 72.” → Inferential</li>
  </ul>

  <p>
    Descriptive statistics does <strong>not</strong> go beyond the data you have.
    It does not generalize, predict, or test hypotheses.
  </p>

  <h2>2. Description ≠ Explanation</h2>

  <p>
    Describing a pattern is not the same as explaining it.
  </p>

  <p>Example:</p>
  <ul>
    <li>“Students who studied more hours had higher scores.” → Description</li>
    <li>“Studying more hours caused higher scores.” → Explanation (requires more evidence)</li>
  </ul>

  <p>
    Descriptive statistics shows patterns.
    It does not prove cause-and-effect relationships.
  </p>

  <h2>3. Population vs Sample Description</h2>

  <p>
    You can describe:
  </p>

  <ul>
    <li>A <strong>population</strong> (all units of interest)</li>
    <li>A <strong>sample</strong> (a subset of the population)</li>
  </ul>

  <p>Example:</p>

  <ul>
    <li>If you measure the heights of all students in one classroom → population description.</li>
    <li>If you measure only 20 selected students → sample description.</li>
  </ul>

  <p>
    Describing a sample does not automatically describe the population.
    That step belongs to inference.
  </p>

  <h2>4. What Does Good Description Look Like?</h2>

  <p>A good description is:</p>

  <ul>
    <li>Clear</li>
    <li>Accurate</li>
    <li>Appropriate for the variable type</li>
    <li>Free of causal language</li>
  </ul>

  <p>Example dataset (5 exam scores):</p>

  <p><code>65, 70, 72, 90, 93</code></p>

  <p>Basic descriptive summary:</p>

  <ul>
    <li>Minimum: 65</li>
    <li>Maximum: 93</li>
    <li>Mean: 78</li>
    <li>Range: 28</li>
  </ul>

  <p>
    This tells us the center and spread.
    It does not explain why some students scored higher.
  </p>

  <h2>5. Why Poor Description Leads to Wrong Conclusions</h2>

  <p>
    If data are poorly described, everything that follows becomes unstable.
  </p>

  <p>Common mistakes:</p>

  <ul>
    <li>Using the mean for ordinal data</li>
    <li>Ignoring extreme values</li>
    <li>Mislabeling axes in graphs</li>
    <li>Interpreting correlation as causation</li>
  </ul>

  <p>
    Most statistical errors originate at the descriptive stage.
  </p>

</section>

<!-- Next Button -->
<section class="section section-slim">
  <a class="btn" href="/descriptive/data-variables/units-observations-and-variables/">
    Next Lesson → Units, Observations & Variables
  </a>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_data_variables_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/data-variables/what-does-it-mean-to-describe-data/",
      label: "Lesson 1 — What Does It Mean to “Describe” Data?",
      ts: Date.now()
    }));
  })();
</script>