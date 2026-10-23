---
layout: default
title: Lognormal Distribution
description: Learn how the lognormal distribution models positive, right-skewed variables and why it appears frequently in economics, finance, biology, and data science.
permalink: /probability/distributions/lognormal-distribution/
sidebar: false
translation_pair: lognormal-distribution
math: true
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/lognormal-distribution/",
    label: "Lognormal Distribution",
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

    <h1>Lognormal Distribution</h1><p><a href="/ar/probability/distributions/lognormal-distribution/" lang="ar" dir="rtl">اقرأ هذا الدرس بالعربية</a></p>

    <p class="lead">
      Many real-world variables are positive, highly right-skewed, and cannot take negative values.
    </p>

    <p class="lead">
      The lognormal distribution provides a natural model for such quantities and appears throughout finance, biology, economics, engineering, and data science.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/normal-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/lln-clt/">
         Next: LLN & CLT →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Lognormal Distribution?</h2>

    <p>
      A random variable follows a lognormal distribution when its logarithm follows a normal distribution.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A variable X is lognormally distributed if ln(X) follows a normal distribution.
      </p>

    </div>

    <h2>The Core Idea</h2>

    <p>
      Instead of modeling X directly,
      we model its logarithm.
    </p>

    <p>
      If:
    </p>

    
    \[
    \ln X\sim N(\mu,\sigma^2),\qquad \sigma>0
    \]


    <p>
      then:
    </p>

    <div class="example-box">

      <p>
        X follows a lognormal distribution.
      </p>

    </div>

    <h2>Why Logarithms Matter</h2>

    <p>
      Many processes grow multiplicatively rather than additively.
    </p>

    <div class="example-box">

      <p>
        Investment growth
      </p>

      <p>
        Population growth
      </p>

      <p>
        Company revenue growth
      </p>

      <p>
        Biological growth
      </p>

    </div>

    <p>
      Repeated multiplication naturally leads to lognormal behavior.
    </p>

    <h2>Examples of Lognormal Variables</h2>

    <ul class="bullets">

      <li>Personal income</li>

      <li>Stock prices</li>

      <li>Company sizes</li>

      <li>House prices</li>

      <li>Biological concentrations</li>

      <li>Internet traffic volumes</li>

      <li>Insurance claim amounts</li>

    </ul>

    <p>
      These variables are positive and often strongly right-skewed.
    </p>

    <h2>Notation</h2>

    <p>
      A lognormal random variable is often written as:
    </p>

    <div class="example-box">

      <p>
        X ~ Lognormal(μ, σ²)
      </p>

    </div>

    <p>
      The parameters μ and σ describe the normal distribution of ln(X), not X itself.
    </p>

    <h2>The Probability Density Function</h2>

    <p>
      The lognormal density is:
    </p>

    
    \[
    f_X(x)=\frac{1}{x\sigma\sqrt{2\pi}}\exp\!\left(-\frac{(\ln x-\mu)^2}{2\sigma^2}\right)
    \]


    <p>
      for:
    </p>

    
    \[
    x>0
    \]


    <p>
      and zero otherwise.
    </p>

    <h2>Key Characteristics</h2>

    <ul class="bullets">

      <li>Only positive values are possible.</li>

      <li>Strong right skewness is common.</li>

      <li>Large values occur occasionally.</li>

      <li>The distribution is asymmetric.</li>

    </ul>

    <h2>The Shape</h2>

    <p>
      A lognormal distribution typically has:
    </p>

    <div class="example-box">

      <p>
        A peak near smaller values
      </p>

      <p>
        A long right tail
      </p>

      <p>
        No negative values
      </p>

    </div>

    <p>
      This shape often resembles real-world financial and economic data.
    </p>

    <section class="example-box" id="esa-lognormal-lab" aria-labelledby="esa-ln-heading">
<h2 id="esa-ln-heading">Interactive Lognormal Probability Explorer</h2><p>Change the log-scale mean and standard deviation, then select an interval or a tail. Probability is calculated on the full positive support, including tails outside the plot.</p>
<div class="esa-ln-fields">
<label>Log-scale mean μ<input id="esa-ln-mu" type="number" value="0" step="any" dir="ltr"></label>
<label>Log-scale SD σ<input id="esa-ln-sigma" type="number" value=".5" min=".000001" step="any" dir="ltr"></label>
<label>Lower bound a<input id="esa-ln-a" type="number" value="1" min="0" step="any" dir="ltr"></label>
<label>Upper bound b<input id="esa-ln-b" type="number" value="2" min="0" step="any" dir="ltr"></label>
<label>Probability region<select id="esa-ln-mode"><option value="between">Between a and b</option><option value="left">Left of a</option><option value="right">Right of b</option></select></label>
</div><p id="esa-ln-error" role="alert" hidden></p>
<div id="esa-ln-results" aria-live="polite" aria-atomic="true">
<p><strong><span id="esa-ln-region">P(a ≤ X ≤ b)</span>:</strong> <output id="esa-ln-probability"></output>
(<output id="esa-ln-percent"></output>%).</p>
<svg id="esa-ln-plot" viewBox="0 0 620 225" role="img" aria-label="Interactive Lognormal Probability Explorer" dir="ltr"></svg>
<p id="esa-ln-warning" class="muted-mini"></p>
<p>Mean: <output id="esa-ln-mean"></output>; Median: <output id="esa-ln-median"></output>; Mode: <output id="esa-ln-modeValue"></output>.</p>
<p>Variance: <output id="esa-ln-variance"></output>; Standard deviation: <output id="esa-ln-sd"></output>.</p></div>
<button type="button" class="btn btn-outline" id="esa-ln-reset">Restore example</button>
<p class="muted-mini">μ and σ describe ln(X), not the arithmetic mean and SD of X. Numerical CDF calculations are approximations; no inputs are stored.</p>
</section><style>
#esa-lognormal-lab{max-width:100%;min-width:0;box-sizing:border-box;overflow-wrap:anywhere}
#esa-lognormal-lab .esa-ln-fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,155px),1fr));gap:12px;margin:12px 0}
#esa-lognormal-lab label{display:block;font-weight:600}
#esa-lognormal-lab input,#esa-lognormal-lab select{display:block;box-sizing:border-box;width:100%;max-width:100%;min-width:0;padding:9px;font:inherit;border:1px solid var(--border);border-radius:8px}
#esa-lognormal-lab [hidden]{display:none!important}
#esa-lognormal-lab svg{width:100%;height:auto;max-width:640px;display:block;margin:10px auto}
#esa-lognormal-lab output{font-variant-numeric:tabular-nums}
#esa-lognormal-lab :is(input,select,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-ln-equation{max-width:100%;overflow-x:auto;direction:ltr}.esa-ln-equation mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}
@media print{#esa-lognormal-lab .esa-ln-fields,#esa-lognormal-lab button{display:none}}
</style><script defer src="/js/lognormal-probability-explorer.js"></script>
<h2>Mean, Median, and Mode</h2>

    <p>
      Unlike the normal distribution,
      these measures are not equal.
    </p>

    <div class="concept-box">

      <strong>Ordering:</strong>

      <p>
        Mode &lt; Median &lt; Mean
      </p>

    </div>

    <p>
      The right tail pulls the mean upward.
    </p>

    <h2>The Median</h2>

    <p>
      The median of a lognormal distribution is:
    </p>

    
    \[
    \operatorname{Median}(X)=e^\mu
    \]


    <p>
      Half the observations lie below this value.
    </p>

    <h2>The Mean</h2>

    <p>
      The expected value is:
    </p>

    
    \[
    E[X]=e^{\mu+\sigma^2/2}
    \]


    <p>
      Notice that the mean exceeds the median whenever:
    </p>

    
    \[
    \sigma>0
    \]


    <h2>The Variance</h2>

    <p>
      The variance is:
    </p>

    
    \[
    \operatorname{Var}(X)=(e^{\sigma^2}-1)e^{2\mu+\sigma^2}
    \]


    <p>
      Larger σ values create dramatically larger variability.
    </p>

    <h2>Why Log Transformation Is Useful</h2>

    <p>
      Many skewed datasets become approximately normal after taking logarithms.
    </p>

    <div class="example-box">

      <p>
        Income data
      </p>

      <p>
        Sales revenue
      </p>

      <p>
        Biological measurements
      </p>

      <p>
        Financial quantities
      </p>

    </div>

    <p>
      This transformation often simplifies statistical analysis.
    </p>

    <h2>Normal Versus Lognormal</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Normal</th>
            <th>Lognormal</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Support</td>
            <td>All real numbers</td>
            <td>Positive values only</td>
          </tr>

          <tr>
            <td>Symmetry</td>
            <td>Symmetric</td>
            <td>Right-skewed</td>
          </tr>

          <tr>
            <td>Mean = Median?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Negative Values Possible?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Applications in Finance</h2>

    <p>
      Financial analysts frequently use lognormal models because prices and values cannot fall below zero.
    </p>

    <ul class="bullets">

      <li>Stock prices</li>

      <li>Asset values</li>

      <li>Investment growth</li>

      <li>Risk modeling</li>

    </ul>

    <p>
      Many classical financial models assume lognormal behavior.
    </p>

    <h2>Applications in Science and Engineering</h2>

    <ul class="bullets">

      <li>Particle sizes</li>

      <li>Environmental concentrations</li>

      <li>Biological growth processes</li>

      <li>Reliability measurements</li>

    </ul>

    <p>
      Lognormal distributions appear whenever growth occurs through repeated multiplicative effects.
    </p>

    <h2>Why the Lognormal Distribution Matters</h2>

    <p>
      Many datasets encountered in practice are positive and skewed.
    </p>

    <p>
      The lognormal distribution often provides a much better description than the normal distribution.
    </p>

    <p>
      Understanding lognormal behavior is particularly important in finance, economics, and applied data science.
    </p>

    <h2>From Individual Distributions to Fundamental Theorems</h2>

    <p>
      We have now studied many of the most important probability distributions.
    </p>

    <p>
      The next block introduces two foundational results that explain why probability and statistics work so well:
    </p>

    <div class="example-box">

      <p>
        Law of Large Numbers (LLN)
      </p>

      <p>
        Central Limit Theorem (CLT)
      </p>

    </div>

    <p>
      These theorems connect probability theory to statistical inference and data analysis.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A lognormal variable has a normally distributed logarithm</li>

        <li>Lognormal distributions are positive and right-skewed</li>

        <li>They naturally model multiplicative growth processes</li>

        <li>Mean, median, and mode are not equal</li>

        <li>The median equals e<sup>μ</sup></li>

        <li>The mean equals e<sup>μ + σ²/2</sup></li>

        <li>Log transformations often make skewed data approximately normal</li>

        <li>Lognormal models are widely used in finance, economics, biology, and engineering</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/normal-distribution/">
         ← Previous: Normal Distribution
      </a>

      <a class="btn"
         href="/probability/lln-clt/">
         Next: LLN & CLT →
      </a>

    </div>

  </div>

</section>