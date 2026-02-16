---
layout: default
title: "Symmetry and Skewness"
description: "Understand symmetric vs skewed distributions and how skewness affects interpretation of mean and median."
permalink: /descriptive/shape/symmetry-and-skewness/
sidebar: false
---

<!-- Previous Button -->
<section class="section section-slim">
  <a class="btn btn-outline" href="/descriptive/shape/why-shape-matters/">
    ← Previous Lesson: Why Distribution Shape Matters
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
        Conceptual structure is finalized. Visual graphs and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h1>Symmetry and Skewness</h1>
    <p class="lead">
      Distribution shape is often described using <strong>symmetry</strong> or <strong>skewness</strong>.
      Skewness explains whether extreme values stretch the distribution more on one side.
    </p>
  </div>

  <hr>

  <h2>1. Symmetric Distributions</h2>

  <p>
    A distribution is <strong>symmetric</strong> if the left and right sides are mirror images.
  </p>

  <ul>
    <li>Mean ≈ Median ≈ Mode</li>
    <li>Tails are balanced</li>
    <li>Common in approximately normal distributions</li>
  </ul>

  <p>
    In symmetric distributions, the mean is a good representation of the “typical” value.
  </p>

  <hr>

  <h2>2. Positive (Right) Skewness</h2>

  <p>
    A distribution is <strong>positively skewed</strong> (right-skewed) when:
  </p>

  <ul>
    <li>The right tail is longer</li>
    <li>Extreme large values pull the mean upward</li>
    <li>Mean &gt; Median</li>
  </ul>

  <h3>Common Examples</h3>
  <ul>
    <li>Income distributions</li>
    <li>Housing prices</li>
    <li>Hospital stay length</li>
  </ul>

  <p>
    In right-skewed data, the mean may exaggerate the “typical” value.
    The median is often more representative.
  </p>

  <hr>

  <h2>3. Negative (Left) Skewness</h2>

  <p>
    A distribution is <strong>negatively skewed</strong> (left-skewed) when:
  </p>

  <ul>
    <li>The left tail is longer</li>
    <li>Extreme small values pull the mean downward</li>
    <li>Mean &lt; Median</li>
  </ul>

  <h3>Common Examples</h3>
  <ul>
    <li>Very easy exam scores</li>
    <li>Retirement age in some populations</li>
  </ul>

  <p>
    In left-skewed data, again the median is often more stable than the mean.
  </p>

  <hr>

  <h2>4. Mean–Median Relationship Rule</h2>

  <p>
    A useful interpretation rule:
  </p>

  <ul>
    <li>If <strong>Mean ≈ Median</strong> → likely symmetric</li>
    <li>If <strong>Mean &gt; Median</strong> → right-skewed</li>
    <li>If <strong>Mean &lt; Median</strong> → left-skewed</li>
  </ul>

  <p>
    This is not a strict mathematical law, but a strong practical guideline.
  </p>

  <hr>

  <h2>5. Why Skewness Matters</h2>

  <ul>
    <li>Determines whether mean or median should be reported</li>
    <li>Affects interpretation of standard deviation</li>
    <li>Impacts modeling assumptions (especially later in inference)</li>
    <li>Reveals inequality or extreme concentration</li>
  </ul>

  <hr>

  <h2>Common Mistakes</h2>

  <ul>
    <li>Using the mean as “typical” in highly skewed data.</li>
    <li>Ignoring skewness when comparing two groups.</li>
    <li>Assuming all real-world data are symmetric.</li>
  </ul>

  <hr>

  <h2>Summary</h2>

  <ul>
    <li>Symmetric distributions are balanced around the center.</li>
    <li>Right skew → large values stretch the right tail.</li>
    <li>Left skew → small values stretch the left tail.</li>
    <li>Mean–median comparison helps detect skewness.</li>
    <li>Skewness influences which measure of center is appropriate.</li>
  </ul>

</section>

<!-- Continue Reading Update -->
<script>
(function(){
  var KEY="esa_continue_descriptive_shape_lesson_v0";
  localStorage.setItem(KEY,JSON.stringify({
    url:"/descriptive/shape/symmetry-and-skewness/",
    label:"Lesson 2 — Symmetry and Skewness",
    ts:Date.now()
  }));
})();
</script>

<section class="section section-slim">
  <a class="btn" href="/descriptive/shape/skewness-and-center-choice/">
    Next Lesson → Skewness and Choosing Mean vs Median
  </a>
</section>