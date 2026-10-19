---
layout: default
title: Sampling Variability
description: Understand why different samples give different results and why variability is fundamental to statistical inference.
permalink: /foundations/sampling-variability/
sidebar: false
translation_pair: sampling-variability
math: true
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
    <p><a href="/ar/foundations/sampling-variability/" lang="ar" dir="rtl">اقرأ هذا الدرس بالعربية</a></p>

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

    <p>
  Because of this variability, we cannot rely on a single sample.
  Instead, we use probability to understand how sample results behave.
</p>
  </div>

  <div class="section-block">
  <h2>Simple Example</h2>

  <p>
    Suppose the true population average height is unknown.
  </p>

  <p>
    We take three different random samples:
  </p>

  <ul class="bullets">
    <li>Sample 1 → mean = 170</li>
    <li>Sample 2 → mean = 168</li>
    <li>Sample 3 → mean = 172</li>
  </ul>

  <p>
    Each sample gives a different estimate of the same population value.
  </p>

  <p>
    This difference is not a mistake — it is sampling variability.
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

  <div class="section-block">
  <h2>Random Variation vs Bias</h2>

  <p>
    Not all differences in results come from the same source.
  </p>

  <ul class="bullets">
    <li><strong>Sampling variability:</strong> natural randomness between samples</li>
    <li><strong>Bias:</strong> systematic error due to poor sampling</li>
  </ul>

  <p>
    Increasing sample size reduces variability,
    but it does not fix bias.
  </p>
</div>

  <!-- VISUAL THINKING -->
  <div class="section-block">
  <h2>Conceptual Understanding</h2>

  <p>
    Think of the population as a full distribution of values.
  </p>

  <img src="{{ '/foundations/images/sampling-variability.png' | relative_url }}" alt="Sampling variability illustration" style="margin-top:15px;">

  <p>
    Each sample captures only a part of that distribution.
  </p>

  <p>
    Different samples capture different parts,
    leading to different results.
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
      Variability persists for partial random samples, but it disappears for a complete census drawn without replacement.
    </p>

    <p>
  Larger random samples tend to yield more precise estimates; size alone cannot correct nonrepresentative selection.
</p>
  </div>

  <!-- NUMERICAL EXAMPLE -->
  <div class="section-block">
  <h2>Numerical Example</h2>

  <p>
    Suppose a population contains:
  </p>

  <ul class="bullets">
    <li>160, 165, 170, 175, 180</li>
  </ul>

  <p>
    We take two different samples:
  </p>

  <ul class="bullets">
    <li>Sample A: 160, 165 → mean = 162.5</li>
    <li>Sample B: 175, 180 → mean = 177.5</li>
  </ul>

  <p>
    Both come from the same population,
    but produce very different estimates.
  </p>
</div>


<!-- An exact finite-population sampling experiment, shared with the Arabic lesson. -->
<div class="section-block" id="esa-sv-lab" style="min-width:0;overflow-wrap:anywhere">
  <h2>Interactive Sampling Variability Laboratory</h2>
  <p>Sample repeatedly from the <strong>fixed finite population</strong>
    <span dir="ltr">160, 165, 170, 175, 180</span> (<span dir="ltr">N = 5</span>).
    Each run uses the same population, not bootstrap resampling from one observed sample.
    All samples are independent of one another; choose whether values can repeat <em>within</em> a sample.</p>
  <div style="display:flex;flex-wrap:wrap;align-items:end;gap:1rem">
    <label>Sample size (<span dir="ltr">n</span>)
      <select id="esa-sv-size"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option></select>
    </label>
    <label>Sampling method
      <select id="esa-sv-method"><option value="without" selected>Without replacement</option><option value="with">With replacement</option></select>
    </label>
    <label>Number of samples
      <select id="esa-sv-reps"><option>100</option><option selected>500</option><option>2000</option></select>
    </label>
    <label>Random seed <input id="esa-sv-seed" type="number" min="0" max="4294967295" step="1" value="2026" style="max-width:135px"></label>
    <button class="btn" type="button" id="esa-sv-run">Run simulation</button>
    <button class="btn btn-outline" type="button" id="esa-sv-reset">Reset</button>
  </div>
  <p id="esa-sv-status" role="status" aria-live="polite"></p>
  <dl style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr));gap:.45rem">
    <div><dt>Population mean</dt><dd id="esa-sv-mu">—</dd></div>
    <div><dt>Population variance (divide by N)</dt><dd id="esa-sv-sigma2">—</dd></div>
    <div><dt>Exact theoretical SE of sample mean</dt><dd id="esa-sv-theory">—</dd></div>
    <div><dt>Simulated SE (B−1 divisor)</dt><dd id="esa-sv-simulated">—</dd></div>
    <div><dt>Average simulated sample mean</dt><dd id="esa-sv-average">—</dd></div>
    <div><dt>Monte Carlo difference (average − μ)</dt><dd id="esa-sv-bias">—</dd></div>
  </dl>
  <p>First sample drawn: <span id="esa-sv-preview" dir="ltr"></span></p>
  <svg id="esa-sv-plot" role="img" aria-label="Histogram of repeated sample means" viewBox="0 0 680 276" style="display:block;width:100%;max-width:680px"></svg>
  <div class="concept-box">
    <p><strong>Analytical reference:</strong> Let population variance be
    \(\sigma_N^2=\sum_{i=1}^N(x_i-\mu)^2/N\). For independent draws
    <em>with replacement</em>, \(\operatorname{SE}(\bar X)=\sqrt{\sigma_N^2/n}\).
    For simple random sampling <em>without replacement</em>,
    \(\operatorname{SE}(\bar X)=\sqrt{(\sigma_N^2/n)\,(N-n)/(N-1)}\).
    The finite-population correction applies only to the second design.</p>
    <p>The exact theoretical standard error is fixed by the design. The simulated standard
    deviation approximates it and may differ due to the finite number of runs.
    At <span dir="ltr">n=N</span> without replacement, every draw is a census
    and the standard error is exactly zero. With replacement, even <span dir="ltr">n=N</span>
    can include repeated population members and has nonzero uncertainty here.</p>
    <p>Sampling variability is variation across new population samples;
    an ordinary bootstrap instead resamples an already observed sample to estimate an
    unknown sampling distribution. Neither method repairs selection bias.</p>
  </div>
</div>
<script src="/js/sampling-variability-lab.js" defer></script>

<div class="section-block">
  <h2>Try It Yourself</h2>

  <p>
    You can observe sampling variability directly using simple tools.
  </p>

  <p><strong>SPSS:</strong></p>
  <ul class="bullets">
    <li>Go to Analyze → Descriptive Statistics → Explore</li>
    <li>Run the analysis on different subsets of your data</li>
    <li>Compare how the mean changes each time</li>
  </ul>

  <p><strong>Excel:</strong></p>
  <ul class="bullets">
    <li>Use =RANDBETWEEN(1,100) to generate values</li>
    <li>Take the average of 10 numbers</li>
    <li>Repeat several times — the result will vary</li>
  </ul>

  <p>

    <p><strong>Python (optional):</strong></p>

<pre><code>import numpy as np

for _ in range(5):
    sample = np.random.randint(1, 101, 10)
    print(sample.mean())
</code></pre>

    Even with the same process, results change — this is sampling variability.
  </p>
</div>

<div class="section-block">
  <h2>Thought Experiment</h2>

  <p>
    Imagine repeatedly taking samples of size 50 from the same population.
  </p>

  <p>
    Each time, you compute the sample mean.
  </p>

  <p>
    You would get a distribution of sample means,
    not a single value.
  </p>

  <p>
    This idea leads to the concept of the sampling distribution.
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
  <li>Why we cannot trust a single sample result</li>
</ul>

    <p>
      It is the reason statistical inference exists.
    </p>
    
  </div>

  <!-- COMMON MISTAKE -->
  <div class="section-block">
    <h2>Common Mistake</h2>

    <p>
  Believing that one sample result represents the exact population value.
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
    Statistical inference is built on understanding variability.
  </p>

  <p>
    We do not eliminate variability — we model and quantify it.
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
