---
layout: default
title: Normal Distribution
description: Learn why the normal distribution is the most important distribution in statistics and how it models many natural phenomena.
permalink: /probability/distributions/normal-distribution/
sidebar: false
translation_pair: normal-distribution
math: true
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/normal-distribution/",
    label: "Normal Distribution",
    ts: Date.now()
    }));
  } catch (_) {
    // Storage may be disabled; the page still works without saved progress.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 5</span>
      <span class="badge">Distributions</span>
      <span class="badge">Continuous</span>
    </div>

    <h1>Normal Distribution</h1>
    <p><a href="/ar/probability/distributions/normal-distribution/" lang="ar" dir="rtl">اقرأ هذا الدرس بالعربية</a></p>

    <p class="lead">
      The normal distribution is the most widely used probability distribution in statistics.
    </p>

    <p class="lead">
      Its appearance throughout science, engineering, economics, psychology, and data science makes it one of the most important concepts in quantitative analysis.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/beta-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/lognormal-distribution/">
         Next: Lognormal Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Normal Distribution?</h2>

    <p>
      A normal distribution is a continuous probability distribution with a symmetric bell-shaped curve.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        The normal distribution is a continuous distribution characterized by its mean and standard deviation.
      </p>

    </div>

    <h2>Why It Is Famous</h2>

    <p>
      Many natural and human-made measurements approximately follow a normal distribution.
    </p>

    <div class="example-box">

      <p>
        Human heights
      </p>

      <p>
        IQ scores
      </p>

      <p>
        Measurement errors
      </p>

      <p>
        Manufacturing dimensions
      </p>

      <p>
        Test scores
      </p>

    </div>

    <p>
      This widespread appearance makes the normal distribution central to statistics.
    </p>

    <h2>The Bell Curve</h2>

    <p>
      The graph of a normal distribution is commonly called a bell curve.
    </p>

    <p>
      It has several important characteristics:
    </p>

    <ul class="bullets">

      <li>Symmetric around the mean</li>

      <li>Single peak</li>

      <li>Smooth shape</li>

      <li>Tails extend infinitely in both directions</li>

    </ul>

    <h2>The Parameters</h2>

    <p>
      A normal distribution is completely determined by two parameters:
    </p>

    <ul class="bullets">

      <li>μ (mean)</li>

      <li>σ (standard deviation)</li>

    </ul>

    <p>
      The mean controls location.
    </p>

    <p>
      The standard deviation controls spread.
    </p>

    <h2>Notation</h2>

    <p>
      A normal random variable is written as:
    </p>

    <div class="example-box">

      <p>
        X ~ N(μ, σ²)
      </p>

    </div>

    <p>
      The notation uses variance rather than standard deviation.
    </p>

    <h2>The Probability Density Function</h2>

    <p>
      The normal density function is:
    </p>

    \[
f_X(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right),
\qquad x\in\mathbb{R},\quad \sigma>0
\]

    <p>
      Here μ is the real-valued mean and σ is the strictly positive
      standard deviation. The density integrates to one over the real line.
    </p>

    <p>
      Although the formula appears complex,
      the distribution has simple and powerful properties.
    </p>

    <h2>Symmetry</h2>

    <p>
      The normal distribution is perfectly symmetric.
    </p>

    <p>
      This implies:
    </p>

    <div class="example-box">

      <p>
        Mean = Median = Mode
      </p>

    </div>

    <p>
      All three measures of center occur at the same location.
    </p>

    <h2>The Role of the Mean</h2>

    <p>
      The mean determines where the bell curve is centered.
    </p>

    <div class="example-box">

      <p>
        Larger μ shifts the curve right.
      </p>

      <p>
        Smaller μ shifts the curve left.
      </p>

    </div>

    <p>
      The overall shape remains unchanged.
    </p>

    <h2>The Role of Standard Deviation</h2>

    <p>
      The standard deviation determines spread.
    </p>

    <div class="example-box">

      <p>
        Small σ → narrow curve
      </p>

      <p>
        Large σ → wider curve
      </p>

    </div>

    <p>
      Greater variability produces a flatter distribution.
    </p>

    <h2>Total Probability Equals One</h2>

    <p>
      As with all probability distributions,
      the total area under the normal curve equals one.
    </p>

    <p>
      Probabilities correspond to areas under the curve.
    </p>


    <section class="example-box" id="esa-normal-probability-explorer" aria-labelledby="esa-normal-title">
      <h2 id="esa-normal-title">Interactive Normal Probability Explorer</h2>
      <p>Adjust the normal model and shade the probability to the left of a, to the right of b, or between a and b. The curve displays the range μ ± 4σ; probabilities always use the full, unbounded normal distribution.</p>
      <div class="esa-normal-controls">
        <label>Mean μ <input id="esa-normal-mu" type="number" step="any" value="0"></label>
        <label>Standard deviation σ (&gt; 0) <input id="esa-normal-sigma" type="number" step="any" min="0.000001" value="1"></label>
        <label>Lower bound a <input id="esa-normal-a" type="number" step="any" value="-1"></label>
        <label>Upper bound b <input id="esa-normal-b" type="number" step="any" value="1"></label>
        <label>Probability region
          <select id="esa-normal-mode">
            <option value="between" selected>Between a and b</option>
            <option value="left">Left of a</option>
            <option value="right">Right of b</option>
          </select>
        </label>
      </div>
      <p role="alert" id="esa-normal-error" hidden></p>
      <svg width="440" height="245" viewBox="0 0 440 245" id="esa-normal-chart" role="img"
           aria-label="Standard normal bell curve with probability shaded between negative one and positive one">
        <line x1="34" x2="404" y1="200" y2="200" stroke="currentColor"></line>
        <path id="esa-normal-shade" fill="#0d9488" fill-opacity="0.35"></path>
        <path id="esa-normal-density" fill="none" stroke="#0d9488" stroke-width="2.5"></path>
        <line id="esa-normal-bound-a" stroke="#64748b" stroke-dasharray="4 3" y1="40" y2="200"></line>
        <line id="esa-normal-bound-b" stroke="#64748b" stroke-dasharray="4 3" y1="40" y2="200"></line>
        <text x="34" y="226" fill="currentColor" font-size="12">μ − 4σ</text>
        <text x="219" y="226" fill="currentColor" font-size="12" text-anchor="middle">μ</text>
        <text x="404" y="226" fill="currentColor" font-size="12" text-anchor="end">μ + 4σ</text>
      </svg>
      <div role="status" aria-live="polite" aria-atomic="true">
        <p>Standardized lower bound z(a) = <output id="esa-normal-za">−1.0000</output>;
           upper bound z(b) = <output id="esa-normal-zb">1.0000</output>.</p>
        <p><span id="esa-normal-prob-label">P(a ≤ X ≤ b)</span> =
           <output id="esa-normal-probability">0.682689</output>
           (<output id="esa-normal-percent">68.2689</output>%).</p>
      </div>
      <p id="esa-normal-warning" class="muted-mini">The displayed curve is truncated at four standard deviations on each side; probability calculations include the tails outside the visible chart.</p>
      <button type="button" class="btn btn-outline" id="esa-normal-reset">Reset standard normal example</button>
      <p class="muted-mini">Uses a numerical approximation to the normal cumulative distribution with absolute error below approximately 2 × 10⁻⁷. Continuous endpoints have zero probability; left/right inequalities may be written as strict or inclusive without changing the result. No simulation is involved.</p>
    </section>
    <style>
      #esa-normal-probability-explorer{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-normal-probability-explorer .esa-normal-controls{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,170px),1fr));gap:12px;margin:14px 0}
      #esa-normal-probability-explorer label{display:flex;flex-direction:column;gap:6px;font-weight:600;min-width:0}
      #esa-normal-probability-explorer input,#esa-normal-probability-explorer select{box-sizing:border-box;font:inherit;padding:8px;width:100%;max-width:100%;min-width:0}
      #esa-normal-probability-explorer svg{display:block;width:100%;height:auto;max-width:550px;margin:10px auto}
      #esa-normal-probability-explorer [hidden]{display:none!important}
      #esa-normal-probability-explorer p{margin:10px 0}
      @media print{#esa-normal-probability-explorer .esa-normal-controls,#esa-normal-probability-explorer button{display:none}}
    </style>
    <script defer src="/js/normal-probability-explorer.js"></script>

    <h2>The Standard Normal Distribution</h2>

    <p>
      A particularly important normal distribution has:
    </p>

    \[
\mu=0,\qquad \sigma=1,\qquad Z\sim N(0,1)
\]

    <p>
      This distribution is called the standard normal distribution.
    </p>

    <h2>The Standard Normal Variable</h2>

    <p>
      A standard normal random variable is often denoted:
    </p>

    <div class="example-box">

      <p>
        Z
      </p>

    </div>

    <p>
      and follows:
    </p>

    <div class="example-box">

      <p>
        Z ~ N(0,1)
      </p>

    </div>

    <h2>Z-Scores</h2>

    <p>
      Any normal observation can be converted into a standard normal value using:
    </p>

    \[
Z=\frac{X-\mu}{\sigma}\sim N(0,1)
\quad\text{if }X\sim N(\mu,\sigma^2),\ \sigma>0
\]

    <p>
      This transformation measures how many standard deviations an observation lies from the mean.
      A z-score can be computed for any distribution with a finite, positive
      standard deviation, but it is exactly standard normal only when X is normal.
    </p>

    <h2>Interpreting Z-Scores</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Z-Score</th>
            <th>Interpretation</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>0</td>
            <td>At the mean</td>
          </tr>

          <tr>
            <td>+1</td>
            <td>One standard deviation above the mean</td>
          </tr>

          <tr>
            <td>-1</td>
            <td>One standard deviation below the mean</td>
          </tr>

          <tr>
            <td>+2</td>
            <td>Two standard deviations above the mean</td>
          </tr>

          <tr>
            <td>-2</td>
            <td>Two standard deviations below the mean</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Empirical Rule</h2>

    <p>
      One of the most famous properties of the normal distribution is the 68–95–99.7 Rule.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Range</th>
            <th>Approximate Probability</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>μ ± 1σ</td>
            <td>68%</td>
          </tr>

          <tr>
            <td>μ ± 2σ</td>
            <td>95%</td>
          </tr>

          <tr>
            <td>μ ± 3σ</td>
            <td>99.7%</td>
          </tr>

        </tbody>

      </table>

    </div>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Almost all observations in a normal distribution fall within three standard deviations of the mean.
      </p>

    </div>

    <p>
      The 68%, 95%, and 99.7% figures are rounded probabilities under
      a normal model (about 68.27%, 95.45%, and 99.73%).
      They are not guaranteed percentages in a finite sample or for a nonnormal distribution.
    </p>

    <h2>The Central Limit Theorem</h2>

    <p>
      One reason the normal distribution appears so often is the Central Limit Theorem.
    </p>

    <p>
      This theorem states that averages of many independent observations tend to become approximately normal.
    </p>

    <p>
      Even when the original data are not normally distributed.
    </p>

    <h2>Why This Matters</h2>

    <p>
      The Central Limit Theorem allows statisticians to use normal methods in a wide variety of situations.
    </p>

    <p>
      It forms the foundation of many statistical procedures.
    </p>

    <h2>Applications of the Normal Distribution</h2>

    <ul class="bullets">

      <li>Confidence intervals</li>

      <li>Hypothesis testing</li>

      <li>Quality control</li>

      <li>Measurement systems</li>

      <li>Forecasting</li>

      <li>Machine learning</li>

      <li>Risk analysis</li>

    </ul>

    <p>
      Few distributions are used more extensively.
    </p>

    <h2>When the Normal Distribution Is Not Appropriate</h2>

    <p>
      Some variables cannot be negative.
    </p>

    <div class="example-box">

      <p>
        Income
      </p>

      <p>
        Company size
      </p>

      <p>
        Stock prices
      </p>

      <p>
        Biological concentrations
      </p>

    </div>

    <p>
      These variables are often strongly right-skewed.
    </p>

    <p>
      The normal distribution may not fit them well.
    </p>

    <h2>Why the Normal Distribution Matters</h2>

    <p>
      The normal distribution is often called the "workhorse" of statistics.
    </p>

    <p>
      Its mathematical simplicity,
      widespread applicability,
      and connection to the Central Limit Theorem make it indispensable.
    </p>

    <p>
      A strong understanding of the normal distribution is essential for advanced statistics.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Many real-world measurements are positive and right-skewed rather than symmetric.
    </p>

    <p>
      The next lesson introduces the lognormal distribution,
      which models positive quantities whose logarithms follow a normal distribution.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The normal distribution is a symmetric bell-shaped distribution</li>

        <li>It is determined by a mean μ and standard deviation σ</li>

        <li>Mean, median, and mode are equal</li>

        <li>The standard normal distribution has μ = 0 and σ = 1</li>

        <li>Z-scores standardize observations</li>

        <li>The 68–95–99.7 rule summarizes normal probabilities</li>

        <li>The Central Limit Theorem explains the widespread importance of normal distributions</li>

        <li>The normal distribution underlies much of modern statistical inference</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/beta-distribution/">
         ← Previous: Beta Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/lognormal-distribution/">
         Next: Lognormal Distribution →
      </a>

    </div>

  </div>

</section>