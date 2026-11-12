---
layout: default
title: Fisher's Exact Test vs Pearson Chi-Square for 2×2 Tables
description: Compare Fisher's conditional exact test and Pearson's chi-square approximation in interactive 2×2 contingency tables, including zero cells.
permalink: /inference/classical-tests/fisher-exact-vs-chi-square/
sidebar: false
math: true
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<h1>Fisher's Exact Test vs. Pearson Chi-Square</h1>
<p class="lead">Why can two valid statistical procedures report different p-values for the same 2×2 contingency table?</p>
<p><a href="/inference/classical-tests/chi-square-independence-test/">Read the chi-square independence lesson</a> · <a href="/inference/classical-tests/two-proportion-z-test/">Compare independent proportions</a></p>
</div></section>
<section><div class="content-narrow">
<h2>Two approaches to association in a 2×2 table</h2>
<p>Under the hypothesis of no association, <strong>Pearson's χ² test</strong> compares observed and expected frequencies and uses an asymptotic reference distribution with one degree of freedom (no continuity correction here). <strong>Fisher's exact test</strong> conditions on the observed row and column totals and evaluates the possible tables using the hypergeometric distribution. Fisher's exact calculation does not require large expected cell counts, although both procedures rely on an appropriate sampling model and independence.</p>
<div class="esa-fc-equation" dir="ltr" tabindex="0" role="region" aria-label="Pearson chi-square equation">
\[
\chi^2=\sum_{i=1}^{2}\sum_{j=1}^{2}\frac{(O_{ij}-E_{ij})^2}{E_{ij}},
\quad E_{ij}=\frac{(\mathrm{row\ total})_i(\mathrm{column\ total})_j}{N}.
\]
</div>
<h2>Exact p-value convention</h2>
<p>The <strong>two-sided Fisher p-value</strong> uses probability ordering: sum the conditional probabilities of all fixed-margin tables that are no more probable than the observed table, as in the default SciPy <code>fisher_exact</code> two-sided convention. It is not generally twice the smaller one-sided tail. Alternatives are defined using the top-left cell count and fixed margins: "greater" favors positive association (odds ratio greater than 1), "less" favors negative association.</p>
<h2>Interactive Fisher–Pearson laboratory</h2>
<section id="esa-fisher-chi-lab" class="concept-box" aria-labelledby="esa-fc-heading">
<h3 id="esa-fc-heading">Enter observed counts</h3>
<p>Nonnegative integers; both row and column totals must be positive; total N ≤ 2,000 for responsive exact enumeration. The demonstration uses 1, 9, 11, 3 as its default table.</p>
<div class="esa-fc-grid">
<label for="esa-fc-a">Row 1, column 1<input id="esa-fc-a" type="number" min="0" max="2000" step="1" value="1" aria-invalid="false" aria-describedby="esa-fc-error"></label>
<label for="esa-fc-b">Row 1, column 2<input id="esa-fc-b" type="number" min="0" max="2000" step="1" value="9" aria-invalid="false" aria-describedby="esa-fc-error"></label>
<label for="esa-fc-c">Row 2, column 1<input id="esa-fc-c" type="number" min="0" max="2000" step="1" value="11" aria-invalid="false" aria-describedby="esa-fc-error"></label>
<label for="esa-fc-d">Row 2, column 2<input id="esa-fc-d" type="number" min="0" max="2000" step="1" value="3" aria-invalid="false" aria-describedby="esa-fc-error"></label>
<label for="esa-fc-side">Fisher alternative<select id="esa-fc-side"><option value="two-sided">Two-sided</option><option value="greater">Greater odds ratio</option><option value="less">Less odds ratio</option></select></label>
</div>
<button id="esa-fc-reset" class="btn btn-outline" type="button">Restore example</button>
<p id="esa-fc-error" role="alert" hidden></p>
<div id="esa-fc-results" aria-live="polite" aria-atomic="true">
<p>Total observations: <output id="esa-fc-N"></output> · Pearson χ²: <output id="esa-fc-chi"></output>.</p>
<div class="table-wrap"><table><caption>Expected counts under independence</caption><thead><tr><th scope="col">Row</th><th scope="col">Column 1</th><th scope="col">Column 2</th></tr></thead><tbody>
<tr><th scope="row">Row 1</th><td><output id="esa-fc-aexpected"></output></td><td><output id="esa-fc-bexpected"></output></td></tr>
<tr><th scope="row">Row 2</th><td><output id="esa-fc-cexpected"></output></td><td><output id="esa-fc-dexpected"></output></td></tr>
</tbody></table></div>
<div class="table-wrap"><table><caption>Statistical inference</caption><thead><tr><th scope="col">Method</th><th scope="col">p-value</th></tr></thead><tbody>
<tr><th scope="row">Fisher exact (selected alternative)</th><td><output id="esa-fc-fisher"></output></td></tr>
<tr><th scope="row">Pearson χ² (two-sided association, asymptotic)</th><td><output id="esa-fc-pearson"></output></td></tr>
</tbody></table></div>
<svg id="esa-fc-plot" viewBox="0 0 620 125" role="img" aria-label="Fisher exact and Pearson chi-square p-values" style="display:block;max-width:100%;width:100%;height:auto"></svg>
<p id="esa-fc-warning" role="status"></p><p id="esa-fc-meaning"></p>
</div></section>
<h2>Interpretation and limits</h2>
<p>For the example table, the independent SciPy references are Fisher two-sided p ≈ 0.00275946, Pearson χ² ≈ 10.971429, and Pearson p ≈ 0.00092527. The methods need not agree on the exact p-value; Pearson's large-sample approximation may be unreliable for small expected counts. Changing Fisher to a one-sided alternative does <em>not</em> change the two-sided Pearson result; they then answer differently directed questions and should not be treated as equivalent tests.</p>
<p>Zero observed cells are allowed when all margins remain positive. A row or column with total zero makes the usual 2×2 association calculation undefined. Neither method proves causality, and the underlying independence/sampling assumptions remain critical.</p>
</div></section>
<style>
#esa-fisher-chi-lab{box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere}
#esa-fisher-chi-lab .esa-fc-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:14px 0}
#esa-fisher-chi-lab label{display:block;font-weight:600;min-width:0}
#esa-fisher-chi-lab :is(input,select){display:block;box-sizing:border-box;width:100%;max-width:100%;min-width:0;padding:9px;font:inherit;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text)}
#esa-fisher-chi-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-fisher-chi-lab [hidden]{display:none!important}
#esa-fisher-chi-lab :is(input,select,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-fc-equation{max-width:100%;overflow-x:auto;padding:8px 0}
@media(max-width:650px){#esa-fisher-chi-lab .esa-fc-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/fisher-chi-square-2x2.js"></script>
