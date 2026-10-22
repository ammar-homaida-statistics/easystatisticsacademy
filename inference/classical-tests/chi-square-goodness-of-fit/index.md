---
layout: default
title: Chi-Square Goodness-of-Fit Test
description: Learn how the chi-square goodness-of-fit test evaluates whether observed categorical data match an expected distribution.
permalink: /inference/classical-tests/chi-square-goodness-of-fit/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_classical_tests_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/classical-tests/chi-square-goodness-of-fit/",
    label: "Chi-Square Goodness-of-Fit Test",
    ts: Date.now()
  }));
  } catch (_) {
    // Disabled browser storage must not interrupt the lesson.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 4</span>
      <span class="badge">Classical Tests</span>
      <span class="badge">Categorical Data</span>
    </div>

    <h1>Chi-Square Goodness-of-Fit Test</h1>

    <p class="lead">
      Many statistical questions involve determining whether observed categorical data match an expected pattern.
    </p>

    <p class="lead">
      The chi-square goodness-of-fit test evaluates whether observed category frequencies are consistent with a specified distribution.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/classical-tests/two-proportion-z-test/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/classical-tests/chi-square-independence-test/">
         Next: Chi-Square Test of Independence →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Research Question</h2>

    <p>
      Suppose a six-sided die is rolled many times.
    </p>

    <p>
      We might ask:
    </p>

    <div class="example-box">

      <p>
        Are the outcomes consistent with a fair die?
      </p>
    </div>

    <p>
      Or suppose a company expects customer preferences to be distributed across several product categories in known proportions.
    </p>

    <p>
      We may ask:
    </p>

    <div class="example-box">

      <p>
        Do the observed preferences match the expected distribution?
      </p>
    </div>

    <p>
      These are goodness-of-fit problems.
    </p>

    <h2>What Does "Goodness of Fit" Mean?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A goodness-of-fit test evaluates how well observed frequencies agree with frequencies predicted by a hypothesized distribution.
      </p>

    </div>

    <p>
      The goal is to determine whether differences between observed and expected counts are larger than would be expected from random sampling alone.
    </p>

    <h2>Observed and Expected Counts</h2>

    <p>
      Every goodness-of-fit test compares:
    </p>

    <ul class="bullets">

      <li>Observed counts</li>

      <li>Expected counts</li>

    </ul>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Category</th>
            <th>Observed</th>
            <th>Expected</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>A</td>
            <td>O₁</td>
            <td>E₁</td>
          </tr>

          <tr>
            <td>B</td>
            <td>O₂</td>
            <td>E₂</td>
          </tr>

          <tr>
            <td>...</td>
            <td>...</td>
            <td>...</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Hypotheses</h2>

    <p>
      The null hypothesis states that the population follows the specified distribution.
    </p>

    <div class="example-box">

      <p>
        H₀: The category probabilities match the hypothesized values.
      </p>
    </div>

    <p>
      The alternative hypothesis states:
    </p>

    <div class="example-box">

      <p>
        Hₐ: The distribution differs from the hypothesized distribution.
      </p>
    </div>

    <h2>Example: Fair Die</h2>

    <p>
      For a fair six-sided die:
    </p>

    <p>
      Each face should occur with probability:
    </p>

    <div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Chi-square goodness-of-fit mathematical formula 1">
\[
p_i=\frac16,\qquad i=1,\ldots,6
\]
</div>

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        H₀: p₁ = p₂ = p₃ = p₄ = p₅ = p₆ = 1/6
      </p>
    </div>

    <h2>Computing Expected Counts</h2>

    <p>
      Expected counts are obtained from:
    </p>

    <div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Chi-square goodness-of-fit mathematical formula 2">
\[
E_i=n\,p_i,\qquad i=1,\ldots,k
\]
</div>

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>n = total sample size</li>

      <li>pᵢ = hypothesized probability for category i</li>

    </ul>

    <h2>Example Expected Counts</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        n = 120 die rolls
      </p>
    </div>

    <p>
      Then for each face:
    </p>

    <div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Chi-square goodness-of-fit mathematical formula 3">
\[
E_i=120\times\frac16=20
\]
</div>

    <p>
      Every category has an expected count of 20.
    </p>

    <h2>The Chi-Square Statistic</h2>

    <p>
      The goodness-of-fit test statistic is:
    </p>

    <div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Chi-square goodness-of-fit mathematical formula 4">
\[
\chi^2=\sum_{i=1}^{k}\frac{(O_i-E_i)^2}{E_i}
\]
</div>

    <p>
      Here \(O_i\) is the observed count and \(E_i\) the expected count for category \(i\). The sum requires positive expected counts and measures discrepancy between observed and expected frequencies.
    </p>

    <h2>Understanding the Formula</h2>

    <p>
      For each category:
    </p>

    <ul class="bullets">

      <li>Compute the difference between observed and expected counts</li>

      <li>Square the difference</li>

      <li>Scale by the expected count</li>

      <li>Add contributions across categories</li>

    </ul>

    <p>
      Larger discrepancies produce larger chi-square values.
    </p>

    <h2>Interpreting χ²</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>χ² Value</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Small</td>
            <td>Observed counts close to expected counts</td>
          </tr>

          <tr>
            <td>Large</td>
            <td>Observed counts differ substantially from expectations</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Example Calculation</h2>

    <p>
      Suppose a die is rolled 60 times.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Face</th>
            <th>Observed</th>
            <th>Expected</th>
          </tr>
        </thead>

        <tbody>

          <tr><td>1</td><td>8</td><td>10</td></tr>
          <tr><td>2</td><td>11</td><td>10</td></tr>
          <tr><td>3</td><td>9</td><td>10</td></tr>
          <tr><td>4</td><td>13</td><td>10</td></tr>
          <tr><td>5</td><td>10</td><td>10</td></tr>
          <tr><td>6</td><td>9</td><td>10</td></tr>

        </tbody>

      </table>

    </div>

    <p>
      The six observed counts sum to 60 and all six expected counts equal 10. Their contributions are 0.4, 0.1, 0.1, 0.9, 0 and 0.1, summing to \(\chi^2=1.6\).
    </p>


    <!-- Batch #66: Chi-square goodness-of-fit lab with fixed null probabilities. -->
    <section id="esa-gof-explorer" class="concept-box" aria-labelledby="esa-gof-heading">
      <h2 id="esa-gof-heading">Interactive Chi-Square Goodness-of-Fit Explorer</h2>
      <p>Enter observed whole-number category frequencies and <strong>pre-specified</strong> null probabilities. The calculator computes expected counts, each Pearson contribution, the chi-square statistic, degrees of freedom, and the <strong>upper-tail asymptotic p-value</strong>.</p>
      <div class="esa-gof-fields">
        <div>
          <label for="esa-gof-counts">Observed counts (comma-separated)</label>
          <textarea id="esa-gof-counts" rows="3" spellcheck="false">8, 11, 9, 13, 10, 9</textarea>
        </div>
        <div>
          <label for="esa-gof-probs">Null category probabilities (decimals, sum to 1)</label>
          <textarea id="esa-gof-probs" rows="3" spellcheck="false">0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.1666666665</textarea>
        </div>
      </div>
      <div class="esa-gof-controls">
        <button type="button" class="btn btn-outline" id="esa-gof-die">Fair die example</button>
        <button type="button" class="btn btn-outline" id="esa-gof-uneven">Unequal null probabilities</button>
        <button type="button" class="btn btn-outline" id="esa-gof-reset">Reset</button>
      </div>
      <p id="esa-gof-error" role="alert" hidden></p>
      <div id="esa-gof-results" role="status" aria-live="polite" aria-atomic="true">
        <h3>Observed and expected counts</h3>
        <svg id="esa-gof-chart" viewBox="0 0 540 205" role="img"
          aria-label="Observed and expected counts by category"></svg>
        <p class="muted-mini"><strong>Legend:</strong> teal = observed; grey = expected.</p>
        <div class="table-wrap"><table>
          <caption>Category contributions to Pearson's chi-square statistic</caption>
          <thead><tr><th>Category</th><th>Observed</th><th>Null probability</th><th>Expected</th><th>(O−E)²/E</th></tr></thead>
          <tbody id="esa-gof-table"></tbody>
        </table></div>
        <p><strong>Total observations:</strong> <output id="esa-gof-n">60</output>.
        <strong>Statistic χ²:</strong> <output id="esa-gof-chi">1.600000</output>.
        <strong>Degrees of freedom:</strong> <output id="esa-gof-df">5</output>.
        <strong>Upper-tail p-value:</strong> <output id="esa-gof-p">0.901249</output>.</p>
        <p id="esa-gof-warning">All expected counts are at least 5.</p>
        <p id="esa-gof-decision">At α=0.05 do not reject the pre-specified null distribution.</p>
      </div>
      <p class="muted-mini">The displayed derivations elsewhere in this lesson use expected counts Eᵢ = n × pᵢ, Pearson's χ² = Σ (Oᵢ − Eᵢ)²/Eᵢ and degrees of freedom k − 1 when probabilities are fixed in advance. Each contribution is shown in the table above.</p>
      <p class="muted-mini">Assumptions: independent categorical outcomes, mutually exclusive and exhaustive categories, strictly positive <strong>null probabilities selected before observing the data</strong>, and adequate expected counts. The p-value is an <strong>asymptotic chi-square approximation</strong>, not an exact small-sample multinomial probability. If parameters are estimated from the same data, the reference degrees of freedom may need adjustment; this tool does <strong>not</strong> perform fitted-parameter GOF tests. A large p-value does not prove the null true, and rejecting it does not establish causality.</p>
    </section>
    <style>
      #esa-gof-explorer{box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere}
      #esa-gof-explorer .esa-gof-fields{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
      #esa-gof-explorer label{display:block;font-weight:650;margin-bottom:8px}
      #esa-gof-explorer textarea{display:block;box-sizing:border-box;width:100%;max-width:100%;
        min-width:0;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text);
        font:inherit;padding:10px;resize:vertical}
      #esa-gof-explorer .esa-gof-controls{display:flex;flex-wrap:wrap;gap:9px;margin:14px 0}
      #esa-gof-explorer .esa-gof-controls button{max-width:100%;white-space:normal}
      #esa-gof-explorer [hidden]{display:none!important}
      #esa-gof-explorer #esa-gof-error{font-weight:650;color:#b42318}
      #esa-gof-explorer #esa-gof-warning{font-weight:600}
      #esa-gof-explorer #esa-gof-chart{display:block;width:100%;height:auto;max-width:560px;margin:auto}
      #esa-gof-explorer output{font-variant-numeric:tabular-nums}
      #esa-gof-explorer .esa-gof-equation{box-sizing:border-box;max-width:100%;min-width:0;overflow-x:auto}
      #esa-gof-explorer .esa-gof-equation mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
      #esa-gof-explorer :is(textarea,button):focus-visible,.esa-gof-equation:focus-visible{
        outline:2px solid var(--accent);outline-offset:2px}
      @media(max-width:650px){#esa-gof-explorer .esa-gof-fields{grid-template-columns:minmax(0,1fr)}}
    </style>
    <script src="{{ '/js/chi-square-gof-explorer.js' | relative_url }}" defer></script>

    <h2>The Chi-Square Distribution</h2>

    <p>
      Under:
    </p>

    <div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Chi-square goodness-of-fit mathematical formula 5">
\[
H_0:\ p_i=p_i^{(0)}\quad(i=1,\ldots,k)
\]
</div>

    <p>
      with independently sampled categorical outcomes, fixed pre-specified category probabilities, and sufficiently large expected counts, the Pearson statistic is approximately chi-square distributed with \(k-1\) degrees of freedom. This is an asymptotic approximation, not an exact finite-sample distribution.
    </p>

    <p>
      This distribution is:
    </p>

    <ul class="bullets">

      <li>Nonnegative (zero is possible if observed and expected counts match)</li>

      <li>Right-skewed</li>

      <li>Defined by degrees of freedom</li>

    </ul>

    <h2>Degrees of Freedom</h2>

    <p>
      When all \(k\) null probabilities are specified before observing the data:
    </p>

    <div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Chi-square goodness-of-fit mathematical formula 6">
\[
\mathrm{df}=k-1\quad\text{(all probabilities specified in advance)}
\]
</div>

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>\(k\) = number of mutually exclusive, exhaustive categories with positive null probabilities</li>
      <li>If parameters are estimated from the same data, the degrees of freedom may need adjustment, depending on the model and estimation procedure.</li>

    </ul>

    <h2>Example Degrees of Freedom</h2>

    <p>
      For a six-sided die:
    </p>

    <div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Chi-square goodness-of-fit mathematical formula 7">
\[
\mathrm{df}=6-1=5
\]
</div>

    <h2>The p-Value</h2>

    <p>
      Once:
    </p>

    <div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Chi-square goodness-of-fit mathematical formula 8">
\[
\chi^2_{\mathrm{obs}}=\frac{4+1+1+9+0+1}{10}=1.6
\]
</div>

    <p>
      and degrees of freedom are known, the p-value is obtained from the chi-square distribution.
    </p>

    <p>
      Under the specified six-category null model, the upper-tail p-value is \(P(\chi^2_5\ge 1.6)\approx0.901\). Larger observed chi-square values yield smaller upper-tail p-values for a fixed reference distribution.
    </p>

    <h2>Decision Rule</h2>

    <div class="concept-box">

      <strong>Decision Rule:</strong>

      <p>
        Reject H₀ if p ≤ α.
      </p>

      <p>
        Fail to reject H₀ if p > α.
      </p>

    </div>

    <h2>Assumptions</h2>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Independent observations drawn under a fixed categorical probability model</li>

      <li>Mutually exclusive, exhaustive categories with positive expected counts</li>

      <li>Expected counts sufficiently large</li>

    </ul>

    <h2>Expected Count Rule</h2>

    <p>
      A common guideline is:
    </p>

    <div class="example-box">

      <p>
        Every expected count should be at least 5.
      </p>
    </div>

    <p>
      This is a conservative rule of thumb rather than an absolute mathematical requirement. The quality of the approximation depends on the expected-count pattern and model; sparse counts may require an exact or simulation-based approach.
    </p>

    <h2>Common Applications</h2>

    <div class="example-box">

      <p>
        Testing fairness of dice or random generators
      </p>

      <p>
        Genetics and inheritance studies
      </p>

      <p>
        Market-share distributions
      </p>

      <p>
        Consumer preference categories
      </p>

      <p>
        Quality-control classification data
      </p>

    </div>

    <h2>Goodness-of-Fit vs Proportion Tests</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Proportion Tests</th>
            <th>Goodness-of-Fit Test</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Categories</td>
            <td>Usually 2</td>
            <td>2 or More</td>
          </tr>

          <tr>
            <td>Parameter</td>
            <td>Proportion(s)</td>
            <td>Entire distribution</td>
          </tr>

          <tr>
            <td>Data Type</td>
            <td>Binary</td>
            <td>Categorical</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      The chi-square goodness-of-fit test broadens statistical inference from binary outcomes to general categorical distributions.
    </p>

    <p>
      Instead of comparing means or proportions, it evaluates whether an entire pattern of observed frequencies matches theoretical expectations.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        The chi-square goodness-of-fit test evaluates whether observed categorical frequencies match a hypothesized distribution. It measures discrepancies between observed and expected counts using the chi-square statistic and determines whether those discrepancies are larger than expected by chance.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Goodness-of-fit tests compare observed counts to a known distribution.
    </p>

    <p>
      Another important question is whether two categorical variables are related.
    </p>

    <p>
      The next lesson introduces the chi-square test of independence, which evaluates relationships between categorical variables.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The goodness-of-fit test compares observed and expected frequencies</li>

        <li>The null hypothesis specifies a categorical distribution</li>

        <li>Expected counts are computed as n × pᵢ</li>

        <li>The chi-square statistic measures overall discrepancy</li>

        <li>Large χ² values indicate stronger evidence against H₀</li>

        <li>Degrees of freedom equal k − 1</li>

        <li>Expected counts should generally be at least 5</li>

        <li>The test evaluates entire categorical distributions rather than single proportions</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/classical-tests/two-proportion-z-test/">
         ← Previous: Two-Proportion Z Test
      </a>

      <a class="btn"
         href="/inference/classical-tests/chi-square-independence-test/">
         Next: Chi-Square Test of Independence →
      </a>

    </div>

  </div>

</section>
<style>
.esa-long-math{box-sizing:border-box;max-width:100%;min-width:0;overflow-x:auto;direction:ltr}
.esa-long-math mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
.esa-long-math:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
</style>
