---
layout: default
title: Parameters vs Statistics
description: Understand the difference between population parameters and sample statistics, and why this distinction is central to statistical inference.
permalink: /foundations/parameters-vs-statistics/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Foundations</span>
      <span class="badge">Core concept</span>
      <span class="badge">Inference bridge</span>
    </div>

    <h1>Parameters vs Statistics</h1>

    <p class="lead">
      Learn the fundamental distinction between population values and sample estimates —
      and why this difference defines statistical inference.
    </p>

    <div class="hero-actions">
      <a class="btn" href="#content">Start lesson</a>
      <a class="btn btn-outline" href="/foundations/">Back to Foundations</a>
    </div>

  </div>
</section>

<!-- CONTENT -->
<section class="section" id="content">

  <!-- CORE IDEA -->
  <div class="section-block">
    <h2>The Core Idea</h2>

    <p>
      Statistics is built on one key distinction:
    </p>

    <ul class="bullets">
      <li><strong>Population → Parameter</strong></li>
      <li><strong>Sample → Statistic</strong></li>
    </ul>

    <p>
      Understanding this difference is essential for all statistical reasoning.
    </p>

    <p>
  Statistical inference is the process of using statistics
  to draw conclusions about unknown parameters.
</p>
  </div>

  <!-- DEFINITIONS -->
  <div class="section-block">
    <h2>Definitions</h2>

    <p><strong>Parameter:</strong></p>
    <ul class="bullets">
      <li>A numerical value describing a population</li>
      <li>Fixed but usually unknown</li>
    </ul>

    <p><strong>Statistic:</strong></p>
    <ul class="bullets">
      <li>A numerical value calculated from a sample</li>
      <li>Varies from sample to sample</li>
      <li>Can be viewed as a random variable</li>
    </ul>
  </div>

  <!-- EXAMPLE -->
  <div class="section-block">
  <h2>Simple Example</h2>

  <p>
    Suppose we want to know the average income of all adults in a country.
  </p>

  <ul class="bullets">
    <li>True average (unknown) → <strong>population parameter</strong></li>
    <li>Sample average → <strong>sample statistic</strong></li>
  </ul>

  <p>
    The statistic is used to estimate the parameter,
    but it will not be exactly equal to it.
  </p>
</div>

  <!-- NOTATION -->
  <div class="section-block">
    <h2>Common Notation</h2>

    <p>
      In statistics, we use different symbols:
    </p>

    <ul class="bullets">
      <li>Population mean → μ (mu)</li>
      <li>Sample mean → x̄ (x-bar)</li>
      <li>Population proportion → p</li>
      <li>Sample proportion → p̂ (p-hat)</li>
    </ul>

    <p>
      This notation helps distinguish what is known vs estimated.
    </p>
  </div>

  <!-- KEY DIFFERENCE -->
  <div class="section-block">
    <h2>Key Differences</h2>

    <ul class="bullets">
      <li>Parameter → fixed but unknown</li>
      <li>Statistic → random and variable</li>
    </ul>

    <p>
      Different samples produce different statistics.
    </p>

    <p>
      This connects directly to <strong>sampling variability</strong>.
    </p>
  </div>

  <!-- NUMERICAL EXAMPLE -->
  <div class="section-block">
  <h2>Numerical Example</h2>

  <p>
    Suppose the true population mean is unknown.
  </p>

  <p>
    We take two samples:
  </p>

  <ul class="bullets">
    <li>Sample 1 → mean = 168</li>
    <li>Sample 2 → mean = 172</li>
  </ul>

  <p>
    Both are statistics — different estimates of the same unknown parameter.
  </p>
</div>

  <!-- WHY IMPORTANT -->
  <div class="section-block">
    <h2>Why This Matters</h2>

    <p>
      The goal of statistics is:
    </p>

    <ul class="bullets">
      <li>Use statistics (sample data)</li>
      <li>To learn about parameters (population)</li>
    </ul>

    <p>
  Because statistics vary from sample to sample,
  all conclusions include uncertainty.
</p>

    <p>
      This process is called:
    </p>

    <ul class="bullets">
      <li><strong>Statistical inference</strong></li>
    </ul>
  </div>

  <!-- COMMON MISTAKE -->
  <div class="section-block">
    <h2>Common Mistake</h2>

    <p>
  Treating a sample statistic as if it were the exact population parameter.
</p>

    <p>
      Reality:
    </p>

    <ul class="bullets">
      <li>Statistics are estimates</li>
      <li>They contain uncertainty</li>
    </ul>
  </div>

  <div class="section-block">
  <h2>Conceptual Flow</h2>

  <p>
    The logic of statistical inference:
  </p>

  <ul class="bullets">
    <li>Population → unknown parameter</li>
    <li>Sample → observed data</li>
    <li>Statistic → estimate</li>
  </ul>

  <p>
    The goal is to connect the sample back to the population.
  </p>
</div>

  <!-- BIG PICTURE -->
  <div class="section-block">
    <h2>The Big Picture</h2>

    <p>
      We never observe the entire population.
    </p>

    <p>
      So we:
    </p>

    <ul class="bullets">
      <li>Collect a sample</li>
      <li>Compute statistics</li>
      <li>Estimate parameters</li>
    </ul>

    <p>
      This is the foundation of all statistical methods.
    </p>

    <p>
  The challenge is to quantify how close our statistics are to the true parameters.
</p>
  </div>

  <!-- NEXT -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Now we explore how data is collected in practice.
    </p>

    <p>
      This leads to:
    </p>

    <ul class="bullets">
      <li>Surveys</li>
      <li>Sampling methods</li>
      <li>Data collection quality</li>
    </ul>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/sampling-variability/">
          ← Previous: Sampling Variability
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/surveys/">
          Next: Surveys →
        </a>

      </div>

    </div>

  </div>
</section>
