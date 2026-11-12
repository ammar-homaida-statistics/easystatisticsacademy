---
layout: default
title: Exact Binomial Test vs One-Proportion Z Test
description: Compare exact binomial p-values with normal-approximation one-proportion Z p-values, using probability-ordering two-sided tests and accessible interactive examples.
permalink: /inference/classical-tests/exact-binomial-vs-z-test/
sidebar: false
math: true
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<h1>Exact Binomial Test vs. One-Proportion Z Test</h1>
<p class="lead">Explore what changes when a discrete exact test replaces a normal approximation, particularly with small samples and extreme proportions.</p>
<p><a href="/inference/classical-tests/one-proportion-z-test/">Review the one-proportion Z-test lesson</a> · <a href="/ar/inference/classical-tests/one-proportion-z-test/" lang="ar" dir="rtl">الشرح العربي لاختبار النسبة</a></p>
</div></section>
<section><div class="content-narrow">
<h2>What do the two tests assume?</h2>
<p>Under the null hypothesis, the number of successes is modeled as \(X\sim\mathrm{Binomial}(n,p_0)\), requiring independent Bernoulli observations with the same success probability. The <strong>exact binomial test</strong> uses this discrete distribution without a normal approximation. The usual <strong>one-proportion Z-test</strong> uses the null-based standard error \(\sqrt{p_0(1-p_0)/n}\) and approximates the null sampling distribution using a standard normal distribution.</p>
<h2>Two-sided exact p-value definition</h2>
<p>Two-sided exact binomial tests have multiple legitimate conventions. This laboratory uses <strong>probability ordering</strong>, as in the default two-sided SciPy <code>scipy.stats.binomtest</code>: it adds probabilities of all binomial outcomes whose null probability is less than or equal to the probability of the observed count, with numerical tolerance only for ties. It does <strong>not</strong> universally equal twice the smaller one-sided tail.</p>
<div class="esa-eb-equation" dir="ltr" tabindex="0" role="region" aria-label="Probability-ordering exact binomial p-value">
\[
P_{\mathrm{exact}}=\sum_{\{k:\Pr_{p_0}(X=k)\leq\Pr_{p_0}(X=x)\}}\Pr_{p_0}(X=k).
\]
</div>
<p>For a greater alternative use \(\Pr_{p_0}(X\ge x)\); for a less alternative use \(\Pr_{p_0}(X\le x)\). The approximate Z-test uses corresponding standard normal tails. Small expected counts \(np_0\) or \(n(1-p_0)\) can make the approximation unreliable.</p>
<h2>Interactive exact-versus-approximate comparison</h2>
<section id="esa-exact-binomial-lab" class="concept-box" aria-labelledby="esa-eb-heading">
<h3 id="esa-eb-heading">Compare two p-values using the same null and alternative</h3>
<p>Exact calculations are limited to \(n\le 2{,}000\) for responsive browser performance; the ordinary Z-only calculator supports larger samples. No values leave your browser.</p>
<div class="esa-eb-grid">
<label for="esa-eb-x">Observed successes \(x\)<input id="esa-eb-x" type="number" min="0" step="1" value="2" aria-invalid="false" aria-describedby="esa-eb-error"></label>
<label for="esa-eb-n">Sample size \(n\) (1–2000)<input id="esa-eb-n" type="number" min="1" max="2000" step="1" value="10" aria-invalid="false" aria-describedby="esa-eb-error"></label>
<label for="esa-eb-p0">Null probability \(p_0\)<input id="esa-eb-p0" type="number" min="0" max="1" step="any" value="0.5" aria-invalid="false" aria-describedby="esa-eb-error"></label>
<label for="esa-eb-side">Alternative hypothesis<select id="esa-eb-side"><option value="two-sided">Two-sided</option><option value="greater">Greater</option><option value="less">Less</option></select></label>
</div>
<button id="esa-eb-reset" class="btn btn-outline" type="button">Reset example</button>
<p id="esa-eb-error" role="alert" hidden></p>
<div id="esa-eb-results" aria-live="polite" aria-atomic="true">
<div class="table-wrap"><table><caption>Exact and approximate p-values under the same hypothesis</caption><thead><tr><th scope="col">Method</th><th scope="col">p-value</th></tr></thead><tbody>
<tr><th scope="row">Exact binomial</th><td><output id="esa-eb-exact"></output></td></tr>
<tr><th scope="row">Normal Z approximation, no continuity correction</th><td><output id="esa-eb-approx"></output></td></tr>
<tr><th scope="row">Absolute difference</th><td><output id="esa-eb-difference"></output></td></tr>
</tbody></table></div>
<p id="esa-eb-counts"></p>
<svg id="esa-eb-plot" viewBox="0 0 620 125" role="img" aria-label="Two p-value comparisons" style="display:block;width:100%;max-width:100%;height:auto"></svg>
<p id="esa-eb-warning" role="status"></p><p id="esa-eb-interpret"></p>
</div></section>
<h2>Worked numerical example</h2>
<p>For \(x=2\), \(n=10\), and \(p_0=0.5\), the exact two-sided probability-ordering p-value is \(0.109375\). The Z approximation is different because the sample size is small. Increasing \(n\) and avoiding very small expected counts often improves approximation quality, but does not make the two definitions identical for every discrete outcome.</p>
<p>For comparisons between <strong>two independent groups</strong>, review the <a href="/inference/classical-tests/two-proportion-z-test/">two-proportion Z-test</a> and the <a href="/inference/classical-tests/fisher-exact-vs-chi-square/">conditional Fisher exact versus chi-square 2×2 laboratory</a>. The one-proportion exact binomial test is not a substitute for those distinct designs.</p>
<h2>Interpretation limits</h2>
<p>The exact calculation is exact <em>conditional on a correct independent binomial model</em>; it does not fix observational bias, clustered data, dependence, or unplanned hypothesis selection. Neither p-value measures the probability that the null hypothesis is true. Confidence-interval methods should be considered separately.</p>
</div></section>
<style>
#esa-exact-binomial-lab{box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere}
#esa-exact-binomial-lab .esa-eb-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:14px 0}
#esa-exact-binomial-lab label{display:block;min-width:0;font-weight:600}
#esa-exact-binomial-lab :is(input,select){display:block;width:100%;min-width:0;max-width:100%;box-sizing:border-box;font:inherit;padding:9px;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text)}
#esa-exact-binomial-lab [hidden]{display:none!important}
#esa-exact-binomial-lab .table-wrap{display:block;max-width:100%;overflow-x:auto}
#esa-exact-binomial-lab :is(input,select,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-eb-equation{max-width:100%;overflow-x:auto;padding:8px 0}
@media(max-width:650px){#esa-exact-binomial-lab .esa-eb-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/one-proportion-z-explorer.js"></script>
<script defer src="/js/exact-binomial-vs-z.js"></script>
