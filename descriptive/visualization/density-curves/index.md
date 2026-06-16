---
layout: default
title: Density Curves
description: Learn what density curves are, how they represent distributions, and how they help statisticians think beyond individual observations.
permalink: /descriptive/visualization/density-curves/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_visualization_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/visualization/density-curves/",
    label: "Density Curves",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 3</span>
      <span class="badge">Visualization</span>
      <span class="badge">Distributions</span>
    </div>

    <h1>Density Curves</h1>

    <p class="lead">
      Histograms show how data are distributed using bars.
    </p>

    <p class="lead">
      Density curves take the next step by representing distributions
      as smooth continuous shapes.
      They help statisticians focus on the overall structure of a distribution
      rather than individual observations.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/visualization/histograms/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/visualization/boxplots/">
         Next: Boxplots →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>Why Move Beyond Histograms?</h2>

    <p>
      Histograms are excellent tools for exploring numerical data,
      but they depend on choices such as:
    </p>

    <ul class="bullets">

      <li>Bin width</li>

      <li>Number of bins</li>

      <li>Bin boundaries</li>

    </ul>

    <p>
      Different choices can make the same dataset appear somewhat different.
    </p>

    <p>
      Density curves provide a smoother representation
      of the underlying distribution.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Density curves describe the overall shape of a distribution
        using a smooth continuous curve.
      </p>

    </div>

    <h2>What Is a Density Curve?</h2>

    <p>
      A <strong>density curve</strong>
      is a smooth curve that represents how observations
      are distributed across values.
    </p>

    <p>
      Areas under the curve represent proportions of observations.
    </p>

    <p>
  The probability of an interval is found from the area under the curve
  over that interval, not from the height at a single point.
</p>

    <p>
      Unlike histograms,
      density curves do not display frequencies directly.
    </p>

    <p>
      Instead,
      they emphasize the distribution's shape.
    </p>

    <h2>A Conceptual Example</h2>

    <p>
      Imagine measuring the heights of thousands of adults.
    </p>

    <p>
      A histogram might show many bars.
    </p>

    <p>
      A density curve would smooth those bars into a single continuous shape,
      revealing the overall pattern more clearly.
    </p>

    <div class="example-box">

      <p>
        Think of a density curve as a smoothed histogram.
      </p>

    </div>

    <img src="{{ 'descriptive/images/histogram-vs-density-curve.png' | relative_url }}"
     alt="Histogram compared with density curve"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
  The histogram shows grouped observed data,
  while the density curve shows the overall distribution pattern.
</p>

    <div class="concept-box">

  <strong>Important insight:</strong>

  <p>
    A density curve is not a picture of individual observations.
    It is a model of how observations are distributed across values.
  </p>

</div>

    <h2>The Area Under a Density Curve</h2>

    <p>
      One of the most important properties of a density curve
      is that the total area underneath it equals 1.
    </p>

    <div class="formula-box">
  Total Area Under the Density Curve = 1
</div>

<img src="{{ 'descriptive/images/area-under-density-curve.png' | relative_url }}"
     alt="Area under a density curve"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      This represents 100% of all observations.
    </p>

    <p>
      Every observation is accounted for somewhere under the curve.
    </p>

    <h2>Area Represents Proportion</h2>

    <p>
      In a density curve,
      probabilities and proportions correspond to areas.
    </p>

    <p>
      Example:
    </p>

    <ul class="bullets">

      <li>Area = 0.25 means 25% of observations</li>

      <li>Area = 0.50 means 50% of observations</li>

      <li>Area = 0.75 means 75% of observations</li>

    </ul>

    <p>
      This idea becomes extremely important in probability and inference.
    </p>

    <h2>Density Does Not Mean Frequency</h2>

    <p>
      Beginners often interpret curve height as frequency.
    </p>

    <p>
      This is not entirely correct.
    </p>

    <p>
      The important quantity is area,
      not height alone.
    </p>

    <p>
      Taller sections indicate greater concentration of observations,
      but proportions are determined by area.
    </p>

    <h2>Common Shapes of Density Curves</h2>

    <p>
      Density curves can take many forms.
    </p>

    <div class="grid grid-2">

      <div class="card">

        <h3>Symmetric</h3>

        <p>
          Left and right sides mirror one another.
        </p>

      </div>

      <div class="card">

        <h3>Right-Skewed</h3>

        <p>
          Long tail extends toward larger values.
        </p>

      </div>

      <div class="card">

        <h3>Left-Skewed</h3>

        <p>
          Long tail extends toward smaller values.
        </p>

      </div>

      <div class="card">

        <h3>Multimodal</h3>

        <p>
          Multiple peaks appear.
        </p>

      </div>

    </div>

    <img src="{{ 'descriptive/images/common-density-shapes.png' | relative_url }}"
     alt="Common density curve shapes"
     style="margin-top:15px; max-width:100%; height:auto;">

    <h2>Symmetric Density Curves</h2>

    <p>
      A symmetric density curve has similar shapes on both sides of its center.
    </p>

    <p>
      Many natural phenomena approximately follow symmetric distributions.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Some measurement errors</li>

      <li>Certain biological characteristics</li>

      <li>Standardized test scores</li>

    </ul>

    <h2>Skewed Density Curves</h2>

    <p>
      Many real-world datasets are not symmetric.
    </p>

    <p>
      Income is a classic example.
    </p>

    <p>
      Most people earn moderate incomes,
      while a small number earn extremely large incomes.
    </p>

    <p>
      This produces a long right tail.
    </p>

    <h2>Multiple Peaks</h2>

    <p>
      Some density curves show multiple peaks.
    </p>

    <p>
      This may indicate:
    </p>

    <ul class="bullets">

      <li>Several groups in the data</li>

      <li>Different populations combined together</li>

      <li>Important underlying structure</li>

    </ul>

    <p>
      Multiple peaks often deserve further investigation.
    </p>

    <h2>Density Curves and Histograms</h2>

    <p>
      Histograms and density curves are closely related.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Histogram</th>
            <th>Density Curve</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Uses bars</td>
            <td>Uses a smooth curve</td>
          </tr>

          <tr>
            <td>Depends on bins</td>
            <td>Less dependent on bins</td>
          </tr>

          <tr>
            <td>Shows frequencies</td>
            <td>Shows density</td>
          </tr>

          <tr>
            <td>Observed counts</td>
            <td>Underlying shape</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both tools help us understand distributions,
      but from slightly different perspectives.
    </p>

    <p>
  Because density curves smooth the data,
  they may hide small gaps, spikes, or unusual observations
  that are visible in a histogram.
</p>

    <h2>Density Curves and Probability</h2>

    <p>
      Density curves provide a bridge between
      descriptive statistics and probability theory.
    </p>

    <p>
      Later courses will use density curves to calculate:
    </p>

    <ul class="bullets">

      <li>Probabilities</li>

      <li>Percentiles</li>

      <li>Confidence intervals</li>

      <li>Statistical significance</li>

    </ul>

    <p>
      Understanding the basic concept now
      makes those topics much easier later.
    </p>

    <h2>The Normal Curve</h2>

    <p>
      The most famous density curve in statistics
      is the normal curve.
    </p>

    <p>
      It is:
    </p>

    <ul class="bullets">

      <li>Symmetric</li>

      <li>Bell-shaped</li>

      <li>Centered around a mean</li>

    </ul>

    <div style="display:flex; gap:20px; align-items:flex-start; flex-wrap:wrap;">

  <div style="flex:1; min-width:300px;">
    <img src="{{ 'descriptive/images/spss_histogram_normal_curve.png' | relative_url }}"
         alt="Histogram with normal curve"
         style="width:100%; height:auto;">
    <p style="text-align:center;">
      Histogram with normal curve overlay
    </p>
  </div>

</div>

    <p>
      Entire fields of statistics rely on properties of this distribution.
    </p>

    <p>
      You will study it in detail later.
    </p>

    <h2>Why Density Curves Matter</h2>

    <p>
      Density curves encourage statistical thinking.
    </p>

    <p>
      Rather than focusing on individual observations,
      they emphasize:
    </p>

    <ul class="bullets">

      <li>Patterns</li>

      <li>Shapes</li>

      <li>Concentrations</li>

      <li>Variability</li>

      <li>Probabilistic behavior</li>

    </ul>

    <p>
      This perspective is central to modern statistics.
    </p>

    <div class="concept-box">

  <strong>Key insight:</strong>

  <p>
    Density curves help connect visual descriptions of data
    to probability, where areas represent proportions and probabilities.
  </p>

</div>

<h2>Density Curves in Software</h2>

<p>
  Some statistical software can overlay a smooth curve on a histogram
  to help compare observed data with an idealized distribution.
</p>

<p>
  In SPSS, histograms can often be displayed with a normal curve overlay.
</p>

  <div style="flex:1; min-width:300px;">
    <img src="{{ 'descriptive/images/spss_histogram_normal_curve.png' | relative_url }}"
         alt="Histogram with normal curve"
         style="width:100%; height:auto;">
    <p style="text-align:center;">
      Histogram with normal curve overlay
    </p>
  </div>

  <h3>Python Example</h3>

<p>
This example creates a histogram and overlays a density curve.
</p>

<pre><code>import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

x = np.random.normal(size=500)

plt.hist(x, density=True)

density = gaussian_kde(x)

xs = np.linspace(min(x), max(x), 200)

plt.plot(xs, density(xs))

plt.show()
</code></pre>

<h3>R Example</h3>

<p>
This example creates a histogram and overlays a density curve.
</p>

<pre><code>x <- rnorm(500)

hist(x,
     probability = TRUE)

lines(density(x),
      lwd = 2)
</code></pre>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Density curves are smooth representations of distributions</li>

        <li>They help reveal the overall shape of data</li>

        <li>The total area under a density curve equals 1</li>

        <li>Areas correspond to proportions and probabilities</li>

        <li>Density curves may be symmetric, skewed, or multimodal</li>

        <li>They complement histograms rather than replace them</li>

        <li>Density curves form a bridge between descriptive statistics and probability</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/visualization/histograms/">
         ← Previous: Histograms
      </a>

      <a class="btn"
         href="/descriptive/visualization/boxplots/">
         Next: Boxplots →
      </a>

    </div>

  </div>

</section>
