---
layout: default
title: Outliers
description: Understand what outliers are, how they arise, and when they should be investigated, kept, or removed.
permalink: /foundations/outliers-conceptual-introduction/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Data quality</span>
      <span class="badge">Extreme values</span>
      <span class="badge">Interpretation</span>
    </div>

    <h1>Outliers</h1>

    <p class="lead">
      Outliers are extreme observations — they can reveal important insights or serious data problems.
    </p>

    <div class="hero-actions">
      <a class="btn" href="#content">Start lesson</a>
      <a class="btn btn-outline" href="/foundations/">Back to Foundations</a>
    </div>

  </div>
</section>

<!-- CONTENT -->
<section class="section" id="content">

  <!-- WHAT IS -->
  <div class="section-block">
    <h2>What Is an Outlier?</h2>

    <p>
      An outlier is a data point that is unusually far from the rest of the data.
    </p>

    <p>
      It does not follow the general pattern of the dataset.
    </p>

    <p>
  What counts as an outlier depends on the distribution of the data.
  A value that is unusual in one context may be normal in another.
</p>
  </div>

  <!-- EXAMPLE -->
  <div class="section-block">
    <h2>Simple Example</h2>

    <p>
      Consider the following values:
    </p>

    <ul class="bullets">
      <li>10, 12, 11, 13, 12, 95</li>
    </ul>

    <p>
      The value <strong>95</strong> is much larger than the others — this is an outlier.
    </p>
  </div>

  <div class="section-block">
  <h2>Conceptual View</h2>

  <p>
    Most data points form a central cluster,
    while outliers lie far from this central region.
  </p>

  <p>
    These extreme values can disproportionately affect summaries.
  </p>

  <img src="{{ '/foundations/images/boxplot-outliers.png' | relative_url }}" 
     alt="Boxplot showing outliers" 
     style="margin-top:15px; max-width:100%; height:auto;">
     <p>
A boxplot summarizes the distribution and highlights potential outliers as points beyond the main range.
</p>

<p>
In later lessons, we use the interquartile range (IQR) to formally identify outliers.
</p>
</div>

  <!-- TYPES -->
  <div class="section-block">
    <h2>Types of Outliers</h2>

    <p><strong>1. Natural Outliers</strong></p>
    <ul class="bullets">
      <li>Genuine observations</li>
      <li>Example: extremely high income</li>
    </ul>

    <p><strong>2. Error Outliers</strong></p>
    <ul class="bullets">
      <li>Caused by mistakes</li>
      <li>Example: data entry error (extra zero)</li>
    </ul>
  </div>

  <div class="section-block">
  <h2>Outliers vs Errors</h2>

  <p>
    Not all outliers are errors.
  </p>

  <ul class="bullets">
    <li>Errors → should be corrected or removed</li>
    <li>True outliers → may carry important information</li>
  </ul>

  <p>
    Treating all outliers as mistakes leads to incorrect analysis.
  </p>
</div>

  <!-- WHY IMPORTANT -->
  <div class="section-block">
    <h2>Why Outliers Matter</h2>

    <ul class="bullets">
      <li>Can strongly affect averages (mean)</li>
      <li>Can distort statistical analysis</li>
      <li>May indicate important real-world phenomena</li>
    </ul>
  </div>

  <!-- EFFECT -->
  <div class="section-block">
    <h2>Effect on the Mean</h2>

    <p>
      Without outlier:
    </p>

    <ul class="bullets">
      <li>10, 11, 12, 12, 13 → mean = 11.6</li>
    </ul>

    <p>
      With outlier:
    </p>

    <ul class="bullets">
      <li>10, 11, 12, 12, 13, 95 → mean = 25.5</li>
    </ul>

    <p>
      The outlier drastically changes the result.
    </p>
  </div>

  <div class="section-block">
  <h2>Robust vs Non-Robust Measures</h2>

  <p>
    Some statistical measures are more sensitive to outliers than others.
  </p>

  <ul class="bullets">
    <li><strong>Mean:</strong> highly affected by outliers</li>
    <li><strong>Median:</strong> more robust</li>
  </ul>

  <p>
    Choosing appropriate summaries is important when outliers are present.
  </p>
</div>

  <!-- COMMON MISTAKE -->
  <div class="section-block">
  <h2>Common Mistake</h2>

  <p>
    Automatically removing outliers without investigation.
  </p>

  <p>
    Problem:
  </p>

  <ul class="bullets">
    <li>You may remove valid observations</li>
    <li>You introduce bias into the dataset</li>
    <li>You distort the true distribution</li>
  </ul>
</div>

  <!-- CORRECT APPROACH -->
  <div class="section-block">
    <h2>Correct Approach</h2>

    <ul class="bullets">
      <li>Investigate the outlier</li>
      <li>Determine if it is an error or real</li>
      <li>Decide based on context — not rules</li>
      <li>Consider how the outlier affects your analysis</li>
    </ul>
  </div>

  <!-- WHEN REMOVE -->
  <div class="section-block">
    <h2>When Should You Remove an Outlier?</h2>

    <ul class="bullets">
      <li>If it is clearly a measurement or data entry error</li>
      <li>If it is impossible (physically or logically)</li>
    </ul>

    <p>
      Otherwise, it should usually be kept.
    </p>
  </div>

  <!-- WHEN KEEP -->
  <div class="section-block">
    <h2>When Should You Keep an Outlier?</h2>

    <ul class="bullets">
      <li>If it reflects real variation</li>
      <li>If it provides important information</li>
      <li>If it is part of the population of interest</li>
    </ul>
  </div>

  <div class="section-block">
  <h2>Key Insight</h2>

  <p>
    Outliers can influence conclusions, especially in small samples.
  </p>

  <p>
    Understanding their origin is more important than simply removing them.
  </p>
</div>

  <!-- BIG IDEA -->
  <div class="section-block">
    <h2>The Big Idea</h2>

    <p>
      Outliers are not just “bad data.”
    </p>

    <p>
      They are signals that require investigation.
    </p>
  </div>

  <!-- NEXT -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Now we move from data issues to summarizing data.
    </p>

    <ul class="bullets">
      <li>Descriptive statistics</li>
      <li>Summaries</li>
      <li>Understanding patterns</li>
    </ul>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/missing-data/">
          ← Previous: Missing Data
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/descriptive-statistics-conceptual-overview/">
          Next: Descriptive Statistics →
        </a>

      </div>

    </div>

  </div>
</section>
