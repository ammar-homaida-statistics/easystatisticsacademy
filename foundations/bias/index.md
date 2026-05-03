---
layout: default
title: Bias
description: Understand bias as systematic error in data collection and analysis, and why it cannot be fixed by increasing sample size.
permalink: /foundations/bias/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Core concept</span>
      <span class="badge">Systematic error</span>
      <span class="badge">Critical thinking</span>
    </div>

    <h1>Bias</h1>

    <p class="lead">
      Bias is systematic error that distorts results — and unlike random error, it cannot be fixed by larger samples.
    </p>

    <div class="hero-actions">
      <a class="btn" href="#content">Start lesson</a>
      <a class="btn btn-outline" href="/foundations/">Back to Foundations</a>
    </div>

  </div>
</section>

<!-- CONTENT -->
<section class="section" id="content">

  <!-- DEFINITION -->
  <div class="section-block">
    <h2>What Is Bias?</h2>

    <p>
      Bias is a systematic deviation from the truth.
    </p>

    <p>
  In statistical terms, bias refers to the difference between the expected value of an estimate and the true population parameter.
</p>

    <p>
      It occurs when data collection, measurement, or analysis consistently pushes results in a particular direction.
    </p>

    <ul class="bullets">
      <li>Not random</li>
      <li>Not balanced</li>
      <li>Not reduced by larger samples</li>
    </ul>
  </div>

  <!-- EXAMPLE -->
  <div class="section-block">
  <h2>Simple Example</h2>

  <p>
    Suppose we estimate average height using only basketball players.
  </p>

  <ul class="bullets">
    <li>The sample is not representative of the population</li>
    <li>The estimate will be consistently too high</li>
  </ul>

  <p>
    This systematic overestimation is bias.
  </p>
</div>

  <!-- TYPES -->
  <div class="section-block">
    <h2>Common Types of Bias</h2>

    <p><strong>1. Sampling Bias</strong></p>
    <ul class="bullets">
      <li>Sample does not represent the population</li>
    </ul>

    <p><strong>2. Measurement Bias</strong></p>
    <ul class="bullets">
      <li>Data is measured incorrectly</li>
      <li>Example: faulty instrument</li>
    </ul>

    <p><strong>3. Response Bias</strong></p>
    <ul class="bullets">
      <li>Participants give inaccurate answers</li>
    </ul>

    <p><strong>4. Selection Bias</strong></p>
    <ul class="bullets">
      <li>How individuals are included affects results</li>
    </ul>
  </div>

  <!-- KEY PROPERTY -->
  <div class="section-block">
    <h2>Key Property of Bias</h2>

    <p>
      Bias does NOT disappear with larger sample size.
    </p>

    <p>
      Example:
    </p>

    <ul class="bullets">
      <li>Small biased sample → wrong</li>
      <li>Large biased sample → still wrong</li>
    </ul>

    <p>
  Bias affects accuracy, not just precision.
</p>
  </div>

  <!-- CONTRAST -->
  <div class="section-block">
    <h2>Bias vs Random Error</h2>

    <ul class="bullets">
      <li>Bias → systematic, directional error</li>
      <li>Random error → unpredictable variation</li>
    </ul>

    <p>
      Random error decreases with sample size.
    </p>

    <p>
      Bias does not.
    </p>
  </div>

  <div class="section-block">
  <h2>Bias vs Random Error (Summary)</h2>

  <ul class="bullets">
    <li>Bias → systematic, directional</li>
    <li>Random error → varies around the truth</li>
    <li>Large samples reduce random error</li>
    <li>Bias requires better design, not more data</li>
  </ul>
</div>

  <div class="section-block">
  <h2>Bias vs Variability</h2>

  <p>
    Two key sources of error in statistics:
  </p>

  <ul class="bullets">
    <li><strong>Bias:</strong> shifts results in one direction</li>
    <li><strong>Variability:</strong> causes results to fluctuate</li>
  </ul>

  <p>
    Good statistical methods aim to reduce both,
    but they require different solutions.
  </p>
</div>

  <!-- REAL WORLD -->
  <div class="section-block">
    <h2>Real-World Example</h2>

    <p>
      Online surveys:
    </p>

    <ul class="bullets">
      <li>Exclude people without internet access</li>
      <li>Overrepresent certain groups</li>
    </ul>

    <p>
      This creates systematic distortion.
    </p>
  </div>

  <!-- WHY IMPORTANT -->
  <div class="section-block">
    <h2>Why Bias Is Dangerous</h2>

    <ul class="bullets">
      <li>Leads to incorrect conclusions</li>
      <li>Cannot be fixed later by analysis</li>
      <li>Often hidden and unnoticed</li>
    </ul>

    <li>Can produce confident but misleading results</li>
  </div>

  <div class="section-block">
  <h2>Key Insight</h2>

  <p>
    More data does not fix bad data.
  </p>

  <p>
    A large biased dataset can produce highly confident but incorrect conclusions.
  </p>
</div>

  <!-- BIG IDEA -->
  <div class="section-block">
    <h2>The Big Idea</h2>

    <p>
      Good statistics starts with good data.
    </p>

    <p>
      If data is biased:
    </p>

    <ul class="bullets">
      <li>All results are unreliable</li>
    </ul>
  </div>

  <!-- NEXT -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Data problems go beyond bias.
    </p>

    <p>
      Next, we study:
    </p>

    <ul class="bullets">
      <li>Missing data</li>
      <li>Incomplete observations</li>
      <li>Why ignoring missingness leads to errors</li>
    </ul>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/experiments/">
          ← Previous: Experiments
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/missing-data/">
          Next: Missing Data →
        </a>

      </div>

    </div>

  </div>
</section>
