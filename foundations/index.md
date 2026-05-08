---
layout: default
title: Statistics Foundations
description: Core concepts: data types, variables, populations vs samples, and the basic logic behind statistical reasoning.
permalink: /foundations/
sidebar: true
---

<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Start here</span>
        <span class="badge">Beginner-friendly</span>
        <span class="badge">Correct theory</span>
      </div>

      <h1>Statistics Foundations</h1>

      <p class="lead">
        Build the core mental model of statistics: data, variables, sampling,
        and how we reason under uncertainty.
      </p>

      <p class="muted-mini">
        ~30 lessons • Concept-first • No prerequisites
      </p>

      <div class="hero-actions">
        <a class="btn" href="#lessons">Start Foundations</a>
        <a class="btn btn-outline" href="/descriptive/">Next: Descriptive</a>
      </div>

    </div>

    <div class="hero-panel">
      <div class="panel-card">

        <h2 class="panel-title">Start here</h2>

        <ol class="quickstart">
          <li><a href="/foundations/what-is-statistics/">What Is Statistics?</a></li>
          <li><a href="/foundations/statistical-thinking-vs-deterministic-thinking/">Statistical Thinking</a></li>
          <li><a href="/foundations/what-is-data/">What Is Data?</a></li>
        </ol>

      </div>
    </div>

  </div>
</section>

<div id="continue-reading" style="display:none;"></div>

<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons</h2>
    <p>Follow in order. Each concept builds on the previous one.</p>
  </div>

  <!-- GROUP 1 -->
  <h3>1. Core Concepts</h3>
  <div class="grid grid-2">
    <div class="card lesson-card"><h3><a href="/foundations/what-is-statistics/">What Is Statistics?</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/what-statistics-is-not/">What Statistics Is Not</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/statistical-thinking-vs-deterministic-thinking/">Statistical Thinking vs Deterministic Thinking</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/statistical-questions/">Statistical Questions</a></h3></div>
  </div>

  <!-- GROUP 2 -->
  <h3>2. Data and Structure</h3>
  <div class="grid grid-2">
    <div class="card lesson-card"><h3><a href="/foundations/what-is-data/">What Is Data?</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/observational-units/">Observational Units</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/variables/">Variables</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/datasets-as-structures/">Datasets as Structures</a></h3></div>
  </div>

  <!-- GROUP 3 -->
  <h3>3. Types and Measurement</h3>
  <div class="grid grid-2">
    <div class="card lesson-card"><h3><a href="/foundations/types-of-data/">Types of Data</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/discrete-vs-continuous-data/">Discrete vs Continuous</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/binary-data/">Binary Data</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/measurement-scales/">Measurement Scales</a></h3></div>
  </div>

  <!-- GROUP 4 -->
  <h3>4. Sampling and Inference Basics</h3>
  <div class="grid grid-2">
    <div class="card lesson-card"><h3><a href="/foundations/populations/">Populations</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/samples/">Samples</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/sampling-variability/">Sampling Variability</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/parameters-vs-statistics/">Parameters vs Statistics</a></h3></div>
  </div>

  <!-- GROUP 5 -->
  <h3>5. Data Collection</h3>
  <div class="grid grid-2">
    <div class="card lesson-card"><h3><a href="/foundations/surveys/">Surveys</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/observational-studies/">Observational Studies</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/experiments/">Experiments</a></h3></div>
  </div>

  <!-- GROUP 6 -->
  <h3>6. Errors and Issues</h3>
  <div class="grid grid-2">
    <div class="card lesson-card"><h3><a href="/foundations/bias/">Bias</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/missing-data/">Missing Data</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/outliers-conceptual-introduction/">Outliers</a></h3></div>
  </div>

  <!-- GROUP 7 -->
  <h3>7. Big Picture</h3>
  <div class="grid grid-2">
    <div class="card lesson-card"><h3><a href="/foundations/descriptive-statistics-conceptual-overview/">Descriptive Overview</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/inferential-statistics-conceptual-overview/">Inferential Overview</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/why-probability-is-needed/">Why Probability</a></h3></div>
    <div class="card lesson-card"><h3><a href="/foundations/how-all-of-this-fits-together/">How It All Fits Together</a></h3></div>
  </div>

</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Goal of this section</h2>
      <ul class="bullets">
        <li>Understand the language of statistics</li>
        <li>Build correct intuition about data and uncertainty</li>
        <li>Avoid mistakes that break analysis</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Next</div>
        <div class="mini-body">
          Continue to <a href="/descriptive/"><strong>Descriptive Statistics</strong></a>
        </div>
      </div>
    </div>
  </div>
</section>

<script>
(function () {
  try {
    const path = window.location.pathname;

    if (path.startsWith("/foundations/") && path !== "/foundations/") {
      localStorage.setItem("esa:lastFoundationLesson", path);
    }

    const last = localStorage.getItem("esa:lastFoundationLesson");
    const container = document.getElementById("continue-reading");

    if (last && container) {
      function getLabel(url) {
        const parts = url.split("/").filter(Boolean);
        let name = parts[parts.length - 1] || "";
        name = name.replace(/-/g, " ");
        name = name.charAt(0).toUpperCase() + name.slice(1);
        return name;
      }

      const label = getLabel(last);

      container.innerHTML = `
        <div class="card" style="margin:20px 0;">
          <strong>Continue Reading</strong><br>
          <a href="${last}" class="btn" style="margin-top:10px;">
            ${label}
          </a>
        </div>
      `;

      container.style.display = "block";
    }

  } catch (e) {}
})();
</script>
