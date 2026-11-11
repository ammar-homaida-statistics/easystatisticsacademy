---
layout: default
title: Welch vs Pooled t Tests — Monte Carlo Type I Error
description: Explore how unequal variances and unequal sample sizes affect Welch and pooled two-sample t-test rejection rates with a reproducible Monte Carlo simulation.
permalink: /inference/classical-tests/welch-pooled-monte-carlo/
sidebar: false
math: true
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<h1>Welch vs Pooled t Tests — Monte Carlo Simulation</h1>
<p class="lead">Investigate how unequal sample sizes and population variances affect the rejection rates of independent-sample Welch and pooled t tests.</p>
<p><a href="/inference/classical-tests/two-sample-t-test-independent/">Read the independent two-sample t-test lesson</a>.</p>
</div></section>
<section class="section"><div class="content-narrow">
<h2>The statistical experiment</h2>
<p>We generate <strong>independent normal observations</strong> in two populations with chosen standard deviations \(\sigma_1\) and \(\sigma_2\). For the null simulation, both population means equal zero. For the alternative simulation, population 1 has mean equal to the chosen effect \(\Delta\), and population 2 has mean zero. Each replication applies two-sided Welch and pooled-variance t tests at <strong>α = 0.05</strong>.</p>
<p><strong>Estimated Type I error:</strong> the fraction rejecting a true null hypothesis (when \(\Delta=0\)). <strong>Estimated rejection probability under the alternative:</strong> the fraction rejecting when the simulated mean difference is the selected effect. If the effect is zero, these quantities coincide; otherwise the second is estimated power for the specified alternative.</p>
<h2>Configure the simulation</h2>
<section id="esa-t89-simulation" class="concept-box" aria-labelledby="esa-sim-heading">
<h3 id="esa-sim-heading">Interactive reproducible Monte Carlo experiment</h3>
<p>Normal populations · independent samples · two-sided tests · α = 0.05. The same random samples are reused with and without the mean shift for a fair comparison.</p>
<div class="esa-sim-grid">
<div><label for="esa-sim-n1">Group A sample size (5–100)</label><input id="esa-sim-n1" type="number" min="5" max="100" step="1" value="12" aria-describedby="esa-sim-status"></div>
<div><label for="esa-sim-n2">Group B sample size (5–100)</label><input id="esa-sim-n2" type="number" min="5" max="100" step="1" value="30" aria-describedby="esa-sim-status"></div>
<div><label for="esa-sim-sd1">Population SD A (0.2–5)</label><input id="esa-sim-sd1" type="number" min="0.2" max="5" step="any" value="1" aria-describedby="esa-sim-status"></div>
<div><label for="esa-sim-sd2">Population SD B (0.2–5)</label><input id="esa-sim-sd2" type="number" min="0.2" max="5" step="any" value="2" aria-describedby="esa-sim-status"></div>
<div><label for="esa-sim-effect">Alternative mean difference Δ (−3 to 3)</label><input id="esa-sim-effect" type="number" min="-3" max="3" step="any" value="1" aria-describedby="esa-sim-status"></div>
<div><label for="esa-sim-reps">Monte Carlo replications (100–1200)</label><input id="esa-sim-reps" type="number" min="100" max="1200" step="1" value="300" aria-describedby="esa-sim-status"></div>
<div><label for="esa-sim-seed">Random seed (1–2147483647)</label><input id="esa-sim-seed" type="number" min="1" max="2147483647" step="1" value="2026" aria-describedby="esa-sim-status"></div>
</div>
<div class="esa-sim-actions"><button class="btn" id="esa-sim-run" type="button">Run simulation</button><button class="btn btn-outline" id="esa-sim-reset" type="button">Restore example</button></div>
<p id="esa-sim-status" role="status" aria-live="polite"></p>
<section id="esa-sim-results" aria-live="polite" aria-atomic="true">
<h3>Estimated rejection rates</h3>
<div class="table-wrap"><table><caption>Monte Carlo rejection rate, Monte Carlo standard error, and rejection count</caption>
<thead><tr><th scope="col">Data-generating condition</th><th scope="col">Welch</th><th scope="col">Pooled equal variance</th></tr></thead>
<tbody><tr><th scope="row">True null (Type I error)</th><td><output id="esa-sim-nullWelch">—</output></td><td><output id="esa-sim-nullPooled">—</output></td></tr>
<tr><th scope="row">Specified alternative (rejection probability)</th><td><output id="esa-sim-altWelch">—</output></td><td><output id="esa-sim-altPooled">—</output></td></tr></tbody></table></div>
<svg id="esa-sim-chart" viewBox="0 0 610 190" role="img" aria-label="Simulated rejection proportions for Welch and pooled tests" style="display:block;width:100%;height:auto;max-width:100%"></svg>
<p class="muted-mini">Dashed line: nominal 5% test size. Each displayed MC SE is \(\sqrt{\hat p(1-\hat p)/B}\), in percentage points, where \(B\) is the number of Monte Carlo replications. It quantifies simulation variability only, not sampling uncertainty in the original observations.</p>
</section>
</section>
<h2>How to interpret these results</h2>
<p>Under the null, each method ideally rejects near 5% over repeated samples. Monte Carlo fluctuations are expected, especially with a small number of replications. Under unequal population variances, pooled testing can have inflated or deflated Type I error, particularly when sample sizes also differ. Welch avoids the equal-variance assumption, but still relies on the sampling design and an appropriate distributional approximation. Rejection probability under the alternative is not the same as a measure of effect magnitude.</p>
<p>Repeat using equal variances, then unequal variances with balanced and unbalanced sample sizes; retain the same seed for reproducible comparisons. Do not claim that a single short Monte Carlo run establishes a universal ranking of tests.</p>
<p><a href="/inference/classical-tests/two-sample-t-test-independent/">Return to Welch vs pooled comparison</a></p>
</div></section>
<style>
#esa-t89-simulation{box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere}
#esa-t89-simulation .esa-sim-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:14px 0}
#esa-t89-simulation label{display:block;font-weight:650;margin-bottom:6px}
#esa-t89-simulation input{display:block;box-sizing:border-box;width:100%;min-width:0;max-width:100%;padding:9px;font:inherit;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text)}
#esa-t89-simulation .esa-sim-actions{display:flex;flex-wrap:wrap;gap:10px}
#esa-t89-simulation .table-wrap{display:block;max-width:100%;overflow-x:auto}
#esa-t89-simulation :is(button,input):focus-visible{outline:2px solid #0f766e;outline-offset:2px}
#esa-t89-simulation [hidden]{display:none!important}
@media(max-width:650px){#esa-t89-simulation .esa-sim-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/welch-two-sample-explorer.js"></script>
<script defer src="/js/pooled-two-sample-comparison.js"></script>
<script defer src="/js/welch-pooled-monte-carlo.js"></script>
