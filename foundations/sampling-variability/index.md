---
layout: default
title: Sampling Variability
description: Understand why different samples give different results and why variability is fundamental to statistical inference.
permalink: /foundations/sampling-variability/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Foundations</span>
      <span class="badge">Core concept</span>
      <span class="badge">Critical insight</span>
    </div>

    <h1>Sampling Variability</h1>

    <p class="lead">
      Learn why different samples produce different results — and why this variability
      is the foundation of statistical inference.
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
      If we take multiple samples from the same population,
      we will get different results.
    </p>

    <p>
      This natural variation is called:
    </p>

    <ul class="bullets">
      <li><strong>Sampling variability</strong></li>
    </ul>

    <p>
      It is not a mistake — it is a fundamental property of data.
    </p>
  </div>

  <!-- SIMPLE EXAMPLE -->
  <div class="section-block">
    <h2>Simple Example</h2>

    <p>
      Suppose the true population average height is unknown.
    </p>

    <p>
      We take three samples:
    </p>

    <ul class="bullets">
      <li>Sample 1 → mean = 170</li>
      <li>Sample 2 → mean = 168</li>
      <li>Sample 3 → mean = 172</li>
    </ul>

    <p>
      All are different — even though they come from the same population.
    </p>
  </div>

  <!-- WHY IT HAPPENS -->
  <div class="section-block">
    <h2>Why Does This Happen?</h2>

    <p>
      Because each sample contains different observations.
    </p>

    <p>
      Even with random sampling:
    </p>

    <ul class="bullets">
      <li>Some samples include higher values</li>
      <li>Some include lower values</li>
    </ul>

    <p>
      This creates variation in results.
    </p>
  </div>

  <!-- NOT AN ERROR -->
  <div class="section-block">
    <h2>Important Insight</h2>

    <p>
      Sampling variability is not an error.
    </p>

    <p>
      It exists even when:
    </p>

    <ul class="bullets">
      <li>The sample is perfectly random</li>
      <li>There is no bias</li>
    </ul>

    <p>
      It is unavoidable.
    </p>
  </div>

  <!-- VISUAL THINKING -->
  <div class="section-block">
    <h2>Conceptual Understanding</h2>

    <p>
      Think of the population as a large distribution.
    </p>

    <p>
      Each sample is like taking a small portion of it.
    </p>

    <p>
      Different portions → different results.
    </p>
  </div>

  <!-- SAMPLE SIZE -->
  <div class="section-block">
    <h2>Effect of Sample Size</h2>

    <p>
      Larger samples reduce variability.
    </p>

    <p><strong>Small sample:</strong></p>

    <ul class="bullets">
      <li>More variation</li>
      <li>Less stable results</li>
    </ul>

    <p><strong>Large sample:</strong></p>

    <ul class="bullets">
      <li>Less variation</li>
      <li>More stable results</li>
    </ul>

    <p>
      But variability never disappears completely.
    </p>
  </div>

  <!-- NUMERICAL EXAMPLE -->
  <div class="section-block">
    <h2>Numerical Example</h2>

    <p>
      Population values (unknown to us):
    </p>

    <ul class="bullets">
      <li>160, 165, 170, 175, 180</li>
    </ul>

    <p>
      Sample A: 160, 165 → mean = 162.5  
      Sample B: 175, 180 → mean = 177.5
    </p>

    <p>
      Same population — very different results.
    </p>
  </div>

  <!-- WHY IMPORTANT -->
  <div class="section-block">
    <h2>Why This Matters</h2>

    <p>
      Sampling variability explains:
    </p>

    <ul class="bullets">
      <li>Why results are uncertain</li>
      <li>Why estimates are not exact</li>
      <li>Why we need probability</li>
    </ul>

    <p>
      It is the reason statistical inference exists.
    </p>
  </div>

  <!-- COMMON MISTAKE -->
  <div class="section-block">
    <h2>Common Mistake</h2>

    <p>
      Assuming one sample gives the true answer.
    </p>

    <p>
      Reality:
    </p>

    <ul class="bullets">
      <li>Every sample is only an approximation</li>
    </ul>
  </div>

  <!-- KEY INSIGHT -->
  <div class="section-block">
    <h2>Key Insight</h2>

    <p>
      Variability is not noise to ignore.
    </p>

    <p>
      It is the central object of statistical reasoning.
    </p>
  </div>

  <!-- NEXT -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Now we connect everything:
    </p>

    <ul class="bullets">
      <li>Parameters (population values)</li>
      <li>Statistics (sample values)</li>
    </ul>

    <p>
      This distinction is essential for inference.
    </p>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/samples/">
          ← Previous: Samples
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/parameters-vs-statistics/">
          Next: Parameters vs Statistics →
        </a>

      </div>

    </div>

  </div>
</section>
