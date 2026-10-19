---
layout: default
title: Missing Data
description: Understand why data is missing, different types of missingness, and why naive fixes can lead to incorrect conclusions.
permalink: /foundations/missing-data/
sidebar: false
translation_pair: missing-data
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Data quality</span>
      <span class="badge">Real-world issue</span>
      <span class="badge">Analysis risk</span>
    </div>

    <h1>Missing Data</h1>
    <p><a href="/ar/foundations/missing-data/" lang="ar" dir="rtl">اقرأ هذا الدرس بالعربية</a></p>

    <p class="lead">
      Missing data is unavoidable in real datasets — but how you handle it can strongly affect your conclusions.
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
    <h2>What Is Missing Data?</h2>

    <p>
      Missing data occurs when some values in a dataset are not observed or recorded.
    </p>

    <ul class="bullets">
      <li>Skipped survey questions</li>
      <li>Measurement failures</li>
      <li>Data entry errors</li>
    </ul>

    <p>
      It is a normal part of real-world data.
    </p>
  </div>

  <!-- EXAMPLE -->
  <div class="section-block">
  <h2>Simple Example</h2>

  <p>
    A dataset of incomes:
  </p>

  <ul class="bullets">
    <li>50,000</li>
    <li>62,000</li>
    <li>Missing</li>
    <li>71,000</li>
  </ul>

  <p>
    If we ignore the missing value,
    the calculated mean may not reflect the true average.
  </p>
</div>

  <!-- WHY IT MATTERS -->
  <div class="section-block">
    <h2>Why Missing Data Matters</h2>

    <ul class="bullets">
      <li>Reduces available information</li>
      <li>Can distort results</li>
      <li>May introduce bias</li>
    </ul>

    <p>
      Ignoring missing data can lead to incorrect conclusions.
    </p>

    <p>
  Depending on the mechanism and analysis, nonrandom missingness can bias estimates.
  Even random missingness reduces information, and a single incomplete dataset cannot establish the mechanism.
</p>
  </div>

  <!-- TYPES -->
  <div class="section-block">
    <h2>Types of Missing Data</h2>

    <p><strong>1. Missing Completely at Random (MCAR)</strong></p>
    <ul class="bullets">
      <li>Missingness is unrelated to any variable</li>
      <li>Example: random technical failure</li>
    </ul>

    <p><strong>2. Missing at Random (MAR)</strong></p>
    <ul class="bullets">
      <li>Missingness depends on observed data</li>
      <li>Example: younger people skip income questions more often</li>
    </ul>

    <p><strong>3. Missing Not at Random (MNAR)</strong></p>
    <ul class="bullets">
      <li>Missingness depends on the missing value itself</li>
      <li>Example: high-income individuals choose not to report income</li>
    </ul>
  </div>

  <div class="section-block">
  <h2>Conceptual View</h2>

  <p>
    Think of missing data as removing part of the distribution.
  </p>

  <p>
    When records are missing independently of their values, complete-case estimators can remain unbiased over repeated sampling, but individual samples still fluctuate.
    When missingness is selective, the observed distribution can differ systematically from the target distribution.
  </p>
</div>

  <div class="section-block">
  <h2>Missing Data and Bias</h2>

  <p>
    Missing data can introduce bias depending on why values are missing.
  </p>

  <ul class="bullets">
    <li>MCAR → under valid sampling, complete-case means are unbiased on average, though less precise</li>
    <li>MAR → may introduce bias if not handled correctly</li>
    <li>MNAR → can cause substantial bias and generally needs sensitivity analysis</li>
  </ul>
</div>


  <!-- FINITE DATASET MISSINGNESS LABORATORY -->
  <div class="section-block" id="esa-md-lab" style="min-width:0;overflow-wrap:anywhere">
    <h2>Interactive Missing Data and Bias Laboratory</h2>
    <p>Use a <strong>known, fixed population of 10 values</strong> with an observed A/B group label.
    Each simulated missingness mechanism hides some values while retaining the true values for comparison.
    MCAR does not depend on records; MAR depends on the <em>observed group</em>; MNAR depends on the
    potentially missing <em>outcome value itself</em>. The examples illustrate mechanisms rather than
    proving a mechanism from a single incomplete dataset.</p>
    <div style="display:flex;flex-wrap:wrap;gap:1rem;align-items:end">
      <label style="flex:1 1 150px">Missingness mechanism
        <select id="esa-md-mode" style="max-width:100%">
          <option value="mcar">MCAR</option><option value="mar">MAR</option><option value="mnar">MNAR</option>
        </select>
      </label>
      <label style="flex:1 1 150px">Baseline probability
        <select id="esa-md-level" style="max-width:100%">
          <option value="0.1">10%</option><option value="0.3" selected>30%</option><option value="0.5">50%</option>
        </select>
      </label>
      <label style="flex:1 1 150px">Random seed
        <input id="esa-md-seed" type="number" inputmode="numeric" min="0" max="4294967295" step="1" value="2026" style="width:100%;max-width:160px">
      </label>
      <button class="btn" id="esa-md-run" type="button">Generate missingness</button>
      <button class="btn btn-outline" id="esa-md-reset" type="button">Reset</button>
    </div>
    <p id="esa-md-status" role="status" aria-live="polite"></p>
    <dl style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,165px),1fr));gap:.6rem">
      <div><dt>Known population mean</dt><dd id="esa-md-true">—</dd></div>
      <div><dt>Missing observations</dt><dd id="esa-md-fraction">—</dd></div>
      <div><dt>Complete-case mean</dt><dd id="esa-md-observed">—</dd></div>
      <div><dt>Mean-imputed mean</dt><dd id="esa-md-imputed">—</dd></div>
      <div><dt>Signed estimation error (observed − true)</dt><dd id="esa-md-error">—</dd></div>
      <div><dt>Variance after mean imputation (sample)</dt><dd id="esa-md-variance">—</dd></div>
    </dl>
    <div style="max-width:100%;overflow-x:auto" tabindex="0" role="region" aria-label="Observed and missing data table">
      <table style="min-width:420px;width:100%">
        <caption>Missing entries are hidden from the estimator; the true values are shown for teaching only.</caption>
        <thead><tr><th>Record</th><th>Observed group</th><th>True value</th><th>Available value</th><th>Mean-imputed value</th></tr></thead>
        <tbody id="esa-md-table"></tbody>
      </table>
    </div>
    <p id="esa-md-notes"></p>
    <div class="concept-box">
      <p><strong>Important:</strong> In this single-variable demonstration, replacing all missing outcomes
      with the complete-case mean leaves the overall mean <em>exactly unchanged</em> when any observations exist.
      It does not correct missingness bias and typically understates variability. MCAR implies unbiased
      complete-case means <em>over repeated samples</em> under valid random sampling, not zero error in each realization.
      MAR may be handled using appropriate observed-data models, weighting or multiple imputation under assumptions;
      MNAR generally requires extra untestable assumptions or sensitivity analysis.</p>
      <p>The baseline probability is a control, not a promise of exactly that percentage missing.
      MAR uses group A probability 0.55 × baseline and group B 1.6 × baseline (capped at 0.95).
      MNAR uses value ≥ 70 probability 1.8 × baseline (capped at 0.95), otherwise 0.3 × baseline.
      The examples do not prove that a mechanism can be identified from observed data alone.</p>
    </div>
  </div>
  <script src="/js/missing-data-lab.js" defer></script>

  <!-- KEY INSIGHT -->
  <div class="section-block">
    <h2>Key Insight</h2>

    <p>
      Not all missing data is equal.
    </p>

    <p>
      The reason data is missing determines how serious the problem is.
    </p>
  </div>

  <!-- COMMON MISTAKE -->
  <div class="section-block">
  <h2>Common Mistake</h2>

  <p>
    Simply removing all rows with missing values (complete-case analysis).
  </p>

  <p>
    Problem:
  </p>

  <ul class="bullets">
    <li>Reduces sample size</li>
    <li>May introduce bias if missingness is not random</li>
    <li>Changes the distribution of the data</li>
  </ul>

  <p>
Example:
</p>

<ul class="bullets">
  <li>Data: 50,000, 60,000, Missing, 100,000</li>
</ul>

<p>
If we remove the missing value:
</p>

<ul class="bullets">
  <li>New data: 50,000, 60,000, 100,000</li>
</ul>

<p>
The average changes depending on what value was missing.
If high values are more likely to be missing,
the result becomes systematically biased.
</p>
</div>

  <!-- NAIVE FIXES -->
  <div class="section-block">
    <h2>Naive Fixes (Dangerous)</h2>

    <ul class="bullets">
      <li>Replacing missing values with the mean</li>
      <li>Filling with zeros</li>
      <li>Ignoring missingness entirely</li>
    </ul>

    <p>
      These methods often distort relationships in the data.
    </p>

    <p>
  These approaches may reduce missingness but introduce distortion.
</p>

<p>
Simple fixes may make the data look complete, but they can hide important bias.
</p>
  </div>

  <!-- REAL WORLD -->
  <div class="section-block">
    <h2>Real-World Example</h2>

    <p>
      Income surveys:
    </p>

    <ul class="bullets">
      <li>High-income individuals may not respond</li>
      <li>Average income becomes underestimated</li>
    </ul>

    <p>
      This creates systematic bias.
    </p>

    <p>
  This is an example of Missing Not at Random (MNAR).
</p>
  </div>

  <div class="section-block">
  <h2>Key Insight</h2>

  <p>
    Missing data is not just about missing values —
    it is about missing information.
  </p>

  <p>
    Understanding the mechanism of missingness is essential
    for valid statistical conclusions.
  </p>
</div>

  <!-- BIG IDEA -->
  <div class="section-block">
    <h2>The Big Idea</h2>

    <p>
      Missing data is not just a technical issue —
      it is a conceptual problem.
    </p>

    <p>
      Understanding why data is missing is more important than just “fixing” it.
    </p>
  </div>

  <!-- NEXT -->
  <div class="section-block">
    <h2>What Comes Next?</h2>

    <p>
      Another common data issue is extreme values.
    </p>

    <ul class="bullets">
      <li>Outliers</li>
      <li>Unusual observations</li>
      <li>Data errors vs real phenomena</li>
    </ul>
  </div>

</section>

<!-- NAVIGATION -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Next steps</h2>

      <div class="hero-actions">

        <a class="btn btn-outline" href="/foundations/bias/">
          ← Previous: Bias
        </a>

        <a class="btn btn-outline" href="/foundations/">
          Foundations Home
        </a>

        <a class="btn" href="/foundations/outliers-conceptual-introduction/">
          Next: Outliers →
        </a>

      </div>

    </div>

  </div>
</section>
