---
layout: default
title: McNemar Test for Paired Proportions
description: Learn when and how to use the McNemar test for paired binary data, with discordant pairs, exact binomial and chi-square p-values, and an interactive laboratory.
permalink: /inference/classical-tests/mcnemar-test/
sidebar: false
math: true
learning_resource: true
translation_pair: mcnemar-test
---
<section class="hero hero-section"><div class="hero-card">
<h1>McNemar Test for Paired Proportions</h1>
<p class="lead">When the same people are classified twice (before and after a course, by two raters, or by two diagnostic tests), the two proportions are not independent. The McNemar test compares them using only the pairs that changed.</p>
<p><a href="/inference/classical-tests/two-proportion-z-test/">Independent proportions: two-proportion z test</a> · <a href="/inference/classical-tests/paired-t-test/">Paired continuous outcomes: paired t test</a> · <a href="/inference/classical-tests/chi-square-independence-test/">Chi-square test of independence</a> · <a href="/ar/inference/classical-tests/mcnemar-test/" lang="ar" dir="rtl">النسخة العربية</a></p>
</div></section>
<section><div class="content-narrow">
<h2>The research question</h2>
<p>A training programme is evaluated on 100 employees. Each employee takes the same pass/fail skills check <strong>before</strong> and <strong>after</strong> training. Did the pass rate change? Because each person contributes two linked outcomes, the two-proportion z test and the chi-square test of independence are not appropriate: both assume the two groups are independent samples.</p>
<h2>The paired 2 × 2 table</h2>
<p>Each <em>pair</em> (one person, two measurements) is counted once:</p>
<div class="table-wrap"><table><caption>Paired outcomes for 100 employees</caption><thead><tr><th scope="col">Before \ After</th><th scope="col">Pass after</th><th scope="col">Fail after</th><th scope="col">Total</th></tr></thead><tbody><tr><th scope="row">Pass before</th><td>a = 45</td><td>b = 5</td><td>50</td></tr><tr><th scope="row">Fail before</th><td>c = 20</td><td>d = 30</td><td>50</td></tr><tr><th scope="row">Total</th><td>65</td><td>35</td><td>100</td></tr></tbody></table></div>
<p>The pass rate is \((a+b)/n=0.50\) before and \((a+c)/n=0.65\) after. Their difference is</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Difference in paired proportions">
\[
\hat p_{\text{after}}-\hat p_{\text{before}}=\frac{a+c}{n}-\frac{a+b}{n}=\frac{c-b}{n}=\frac{20-5}{100}=0.15.
\]</div>
<p>The concordant cells \(a\) and \(d\) cancel: people who passed both times or failed both times say nothing about <em>change</em>. Only the <strong>discordant pairs</strong> \(b\) and \(c\) matter.</p>
<h2>Hypotheses</h2>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="McNemar hypotheses">
\[
H_0:\ P(\text{pass before})=P(\text{pass after})\iff \pi_b=\pi_c,
\qquad H_a:\ \pi_b\ne\pi_c .
\]</div>
<p>This is called <strong>marginal homogeneity</strong>. Under \(H_0\), a discordant pair is equally likely to be of type \(b\) or type \(c\). Conditional on \(n_d=b+c\) discordant pairs,</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Exact conditional distribution">
\[
b \mid n_d \sim \operatorname{Binomial}\!\left(n_d,\tfrac12\right).
\]</div>
<h2>Three ways to compute the p-value</h2>
<h3>1. Exact binomial (conditional) test</h3>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Exact McNemar p-value">
\[
p_{\text{exact}}=\min\!\left\{1,\ 2\,P\!\left(X\le \min(b,c)\right)\right\},\qquad X\sim\operatorname{Binomial}\!\left(b+c,\tfrac12\right).
\]</div>
<p>Because the null distribution is symmetric, doubling the smaller tail is the usual two-sided p-value. It is valid for any number of discordant pairs.</p>
<h3>2. Asymptotic chi-square statistic</h3>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="McNemar chi-square statistic">
\[
\chi^2_{\text{McN}}=\frac{(b-c)^2}{b+c},\qquad df=1 .
\]</div>
<p>This is the square of the normal approximation \(z=(b-c)/\sqrt{b+c}\) to the binomial distribution above, so it needs a reasonable number of discordant pairs.</p>
<h3>3. Continuity-corrected chi-square (Edwards)</h3>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Continuity corrected McNemar statistic">
\[
\chi^2_{\text{cc}}=\frac{\left(\max\{|b-c|-1,\,0\}\right)^2}{b+c}.
\]</div>
<p>The correction moves the approximate p-value closer to the exact one in small samples, at the cost of being conservative. With modern software the exact test is usually preferred when \(b+c\) is small; a common rule of thumb is \(b+c<25\). Some software omits the \(\max\{\cdot,0\}\) safeguard, which changes the result only when \(b=c\).</p>
<h2>Worked example</h2>
<p>Here \(b=5\), \(c=20\) and \(n_d=25\).</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Worked McNemar example">
\[
\chi^2_{\text{McN}}=\frac{(5-20)^2}{25}=9,\ p\approx0.00270;\qquad
\chi^2_{\text{cc}}=\frac{14^2}{25}=7.84,\ p\approx0.00511;\qquad
p_{\text{exact}}=2P(X\le5)\approx0.00408 .
\]</div>
<p>All three versions reject \(H_0\) at \(\alpha=0.05\): the pass rate after training differs from the pass rate before. Fifteen more employees changed from fail to pass than from pass to fail. Note that this design alone cannot attribute the change to training; practice effects or other events between the two checks could also explain it.</p>
<h2>Interactive McNemar laboratory</h2>
<section id="esa-mcnemar-lab" class="concept-box" aria-labelledby="esa-mcn-heading">
<h3 id="esa-mcn-heading">Enter paired counts</h3>
<noscript><p class="esa-noscript" role="note">This interactive lab requires JavaScript. Without JavaScript the numbers shown are the fixed worked example; the formulas and interpretation in the lesson remain available.</p></noscript>
<p>Rows are the first measurement and columns the second. Enter whole-number counts of <strong>pairs</strong>, not of individual measurements.</p>
<div class="esa-mcn-grid">
<label>a: + then + <input id="esa-mcn-a" type="number" min="0" max="10000000" step="1" value="45" inputmode="numeric" aria-invalid="false" aria-describedby="esa-mcn-error"></label>
<label>b: + then − <input id="esa-mcn-b" type="number" min="0" max="10000000" step="1" value="5" inputmode="numeric" aria-invalid="false" aria-describedby="esa-mcn-error"></label>
<label>c: − then + <input id="esa-mcn-c" type="number" min="0" max="10000000" step="1" value="20" inputmode="numeric" aria-invalid="false" aria-describedby="esa-mcn-error"></label>
<label>d: − then − <input id="esa-mcn-d" type="number" min="0" max="10000000" step="1" value="30" inputmode="numeric" aria-invalid="false" aria-describedby="esa-mcn-error"></label>
</div>
<div class="esa-mcn-controls"><button type="button" class="btn btn-outline" id="esa-mcn-example">Training example</button><button type="button" class="btn btn-outline" id="esa-mcn-small">Few discordant pairs</button><button type="button" class="btn btn-outline" id="esa-mcn-none">No discordant pairs</button></div>
<p id="esa-mcn-error" role="alert" hidden></p>
<div class="esa-mcn-results" role="status" aria-live="polite" aria-atomic="true">
<p>Pairs n = <output id="esa-mcn-n">100</output>; discordant pairs b + c = <output id="esa-mcn-nd">25</output>.</p>
<p>Proportion positive: first = <output id="esa-mcn-p1">0.5000</output>, second = <output id="esa-mcn-p2">0.6500</output>; first − second = <output id="esa-mcn-diff">-0.1500</output>.</p>
<div class="table-wrap"><table><caption>McNemar statistics and two-sided p-values</caption><thead><tr><th scope="col">Method</th><th scope="col">Statistic</th><th scope="col">p-value</th></tr></thead><tbody>
<tr><th scope="row">Exact binomial</th><td>—</td><td><output id="esa-mcn-exact">0.004077</output></td></tr>
<tr><th scope="row">Chi-square, no correction</th><td><output id="esa-mcn-chi">9.000000</output></td><td><output id="esa-mcn-p">0.002700</output></td></tr>
<tr><th scope="row">Chi-square, continuity-corrected</th><td><output id="esa-mcn-chicc">7.840000</output></td><td><output id="esa-mcn-pcc">0.005110</output></td></tr>
</tbody></table></div>
</div>
<p id="esa-mcn-advice" role="status" aria-live="polite">With 25 discordant pairs the chi-square approximation is usually adequate; the exact p-value remains valid and can always be reported.</p>
<p class="muted-mini">Changing a or d does not change any McNemar statistic or p-value; it only changes the two marginal proportions. The chi-square p-values use one degree of freedom; the exact p-value is the doubled smaller binomial tail.</p>
</section>
<h2>Assumptions and limitations</h2>
<ul class="bullets"><li>Each pair is a matched unit (the same person measured twice, or a deliberately matched pair), and pairs are independent of one another.</li><li>The outcome is binary at both measurements, with the same categories.</li><li>The test addresses a change in marginal proportions, not agreement. For agreement between two raters, <a href="/inference/classical-tests/cohens-kappa/">Cohen's kappa</a> answers a different question.</li><li>Without a control group, a significant change does not establish that an intervention caused it.</li></ul>
<h2>Choosing among related tests</h2>
<ul class="bullets"><li><strong>Two independent groups, binary outcome:</strong> <a href="/inference/classical-tests/two-proportion-z-test/">two-proportion z test</a> or <a href="/inference/classical-tests/fisher-exact-vs-chi-square/">Fisher's exact test</a>.</li><li><strong>Same units twice, binary outcome:</strong> McNemar test (this lesson).</li><li><strong>Same units twice, continuous outcome:</strong> <a href="/inference/classical-tests/paired-t-test/">paired t test</a>.</li></ul>
<div class="summary-box"><h2>Lesson takeaways</h2><ul class="bullets"><li>Paired binary data violate the independence assumed by two-sample proportion tests.</li><li>Only the discordant pairs b and c carry information about change.</li><li>Exact p-value: \(\min\{1,2P(X\le\min(b,c))\}\) with \(X\sim\operatorname{Bin}(b+c,1/2)\).</li><li>Asymptotic statistic: \((b-c)^2/(b+c)\) with 1 df; prefer the exact test when \(b+c\) is small.</li></ul></div>
</div></section>
<style>
#esa-mcnemar-lab{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-mcnemar-lab .esa-mcn-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,160px),1fr));gap:12px;margin:14px 0}
#esa-mcnemar-lab label{display:flex;flex-direction:column;gap:6px;min-width:0;font-weight:600}
#esa-mcnemar-lab input{box-sizing:border-box;width:100%;max-width:100%;padding:8px;font:inherit}
#esa-mcnemar-lab .esa-mcn-controls{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
#esa-mcnemar-lab .esa-mcn-controls button{max-width:100%;white-space:normal}
#esa-mcnemar-lab .table-wrap{display:block;max-width:100%;overflow-x:auto}
#esa-mcnemar-lab [hidden]{display:none!important}
#esa-mcnemar-lab [role="alert"]{color:#b42318;font-weight:700}
#esa-mcnemar-lab :is(input,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-long-math{max-width:100%;overflow-x:auto}
</style>
<script defer src="/js/mcnemar-test-lab.js"></script>
