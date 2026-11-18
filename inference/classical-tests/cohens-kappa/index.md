---
layout: default
title: Cohen's Kappa for Rater Agreement
description: Learn how Cohen's kappa measures agreement between two raters beyond chance, why high agreement can give low kappa, and how to interpret it, with an interactive laboratory.
permalink: /inference/classical-tests/cohens-kappa/
sidebar: false
math: true
learning_resource: true
translation_pair: cohens-kappa
---
<section class="hero hero-section"><div class="hero-card">
<h1>Cohen's Kappa for Rater Agreement</h1>
<p class="lead">Two clinicians classify the same patients, or two coders label the same interviews. How well do they agree, beyond the agreement we would expect by chance alone?</p>
<p><a href="/ar/inference/classical-tests/cohens-kappa/" lang="ar" dir="rtl" hreflang="ar">النسخة العربية</a> · <a href="/inference/classical-tests/mcnemar-test/">McNemar test: did the proportion change?</a> · <a href="/inference/classical-tests/chi-square-independence-test/">Chi-square test of independence</a></p>
</div></section>
<section><div class="content-narrow">
<h2>Agreement is a different question from change</h2>
<p>The <a href="/inference/classical-tests/mcnemar-test/">McNemar test</a> asks whether two paired classifications have the same <em>marginal</em> proportions. Two raters can have identical marginal proportions and still disagree on many individual cases. <strong>Cohen's kappa</strong> instead measures how often the two raters put the <em>same case</em> in the <em>same category</em>, corrected for chance.</p>
<h2>The agreement table</h2>
<p>Fifty X-rays are read by two radiologists as "abnormal" or "normal":</p>
<div class="table-wrap"><table><caption>Agreement between two radiologists (N = 50)</caption><thead><tr><th scope="col">Rater A \ Rater B</th><th scope="col">Abnormal</th><th scope="col">Normal</th><th scope="col">Total</th></tr></thead><tbody><tr><th scope="row">Abnormal</th><td>20</td><td>5</td><td>25</td></tr><tr><th scope="row">Normal</th><td>10</td><td>15</td><td>25</td></tr><tr><th scope="row">Total</th><td>30</td><td>20</td><td>50</td></tr></tbody></table></div>
<h2>Observed and chance agreement</h2>
<p>The <strong>observed agreement</strong> is the proportion of cases on the diagonal. The <strong>chance agreement</strong> is the agreement expected if the raters classified independently with their own marginal proportions \(r_i\) and \(c_i\):</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Observed and expected agreement">
\[
p_o=\sum_{i=1}^{k}p_{ii}=\frac{20+15}{50}=0.70,\qquad
p_e=\sum_{i=1}^{k}r_i\,c_i=0.5\times0.6+0.5\times0.4=0.50 .
\]</div>
<h2>Cohen's kappa</h2>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Cohen's kappa">
\[
\kappa=\frac{p_o-p_e}{1-p_e}=\frac{0.70-0.50}{1-0.50}=0.40 .
\]</div>
<p>Kappa is the share of the <em>possible</em> improvement over chance that the raters actually achieve: \(\kappa=1\) is perfect agreement, \(\kappa=0\) is agreement no better than chance, and \(\kappa&lt;0\) is systematic disagreement. Kappa is undefined when \(p_e=1\), which happens only if both raters always use the same single category.</p>
<h2>The maximum attainable kappa</h2>
<p>If the two raters' marginal proportions differ, even the best possible arrangement of cases cannot reach \(\kappa=1\):</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Maximum kappa">
\[
\kappa_{\max}=\frac{\sum_i\min(r_i,c_i)-p_e}{1-p_e}=\frac{0.5+0.4-0.5}{0.5}=0.80 .
\]</div>
<p>Here rater B calls more X-rays abnormal (60%) than rater A (50%), so the ceiling is 0.80. Reporting \(\kappa\) next to \(\kappa_{\max}\) separates disagreement caused by different overall tendencies from case-by-case disagreement.</p>
<h2>The kappa paradox</h2>
<p>Suppose 85 of 100 cases are rated "normal" by both raters, 5 "abnormal" by both, and 10 are split evenly. Observed agreement is 0.90, yet</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Kappa paradox example">
\[
p_e=0.9^2+0.1^2=0.82,\qquad \kappa=\frac{0.90-0.82}{1-0.82}\approx0.444 .
\]</div>
<p>When one category dominates, chance agreement is already high, so the same disagreements cost more kappa. This is why kappa should always be reported with the table or with \(p_o\) and the category prevalences.</p>
<h2>Standard error and confidence interval</h2>
<p>For large samples, Fleiss, Cohen and Everitt (1969) give the variance of \(\hat\kappa\):</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Kappa variance">
\[
\widehat{\operatorname{Var}}(\hat\kappa)=\frac{A+B-C}{N(1-p_e)^2},\quad
A=\sum_i p_{ii}\bigl[1-(r_i+c_i)(1-\hat\kappa)\bigr]^2,\quad
B=(1-\hat\kappa)^2\sum_{i\ne j}p_{ij}(c_i+r_j)^2,\quad
C=\bigl[\hat\kappa-p_e(1-\hat\kappa)\bigr]^2 .
\]</div>
<p>For the X-ray example, \(SE\approx0.127\) and the approximate 95% interval is \(0.40\pm1.96\times0.127=[0.151,\,0.649]\). This Wald interval is a large-sample approximation: it can be poor for small \(N\) or for \(\kappa\) near \(\pm1\), and it collapses to a single point when agreement is perfect.</p>
<h2>Weighted kappa for ordered categories</h2>
<p>Unweighted kappa counts a "mild versus severe" disagreement exactly like "mild versus moderate". When the categories are <strong>ordered</strong>, weighted kappa gives partial credit to near misses. With categories numbered \(1,\dots,k\), the usual agreement weights are</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="Weighted kappa">
\[
w_{ij}^{\text{lin}}=1-\frac{|i-j|}{k-1},\qquad
w_{ij}^{\text{quad}}=1-\frac{(i-j)^2}{(k-1)^2},\qquad
\kappa_w=\frac{\sum_{ij}w_{ij}p_{ij}-\sum_{ij}w_{ij}r_ic_j}{1-\sum_{ij}w_{ij}r_ic_j}.
\]</div>
<p>For the three-category preset in the laboratory below (read as mild, moderate and severe), unweighted \(\hat\kappa=0.720\), linear \(\hat\kappa_w=0.771\) and quadratic \(\hat\kappa_w=0.824\): most disagreements are between adjacent categories, so weighting raises the coefficient. Quadratic-weighted kappa is closely related to the intraclass correlation coefficient. With two categories both weightings equal unweighted kappa. Choose the weighting <em>before</em> looking at the data, report which one was used, and do not use weights for unordered (nominal) categories. The laboratory's standard error for \(\hat\kappa_w\) uses the large-sample variance of Fleiss, Cohen and Everitt (1969), with the same small-sample caveats as above.</p>
<h2>Interactive kappa laboratory</h2>
<section id="esa-kappa-lab" class="concept-box" aria-labelledby="esa-kappa-heading">
<h3 id="esa-kappa-heading">Enter an agreement table</h3>
<noscript><p class="esa-noscript" role="note">This interactive lab requires JavaScript. Without JavaScript the numbers shown are the fixed worked example; the formulas and interpretation in the lesson remain available.</p></noscript>
<p>Each line is one category of rater A; each column is the same category of rater B. Separate whole-number counts with commas (2–5 categories).</p>
<label for="esa-kappa-input">Agreement counts (rater A rows × rater B columns)</label>
<textarea id="esa-kappa-input" rows="5" spellcheck="false" aria-describedby="esa-kappa-error" aria-invalid="false">20, 5
10, 15</textarea>
<label for="esa-kappa-weights">Weighting</label>
<select id="esa-kappa-weights"><option value="none" selected>Unweighted (nominal categories)</option><option value="linear">Linear weights (ordered categories)</option><option value="quadratic">Quadratic weights (ordered categories)</option></select>
<div class="esa-kappa-controls"><button type="button" class="btn btn-outline" id="esa-kappa-example">X-ray example</button><button type="button" class="btn btn-outline" id="esa-kappa-paradox">Kappa paradox</button><button type="button" class="btn btn-outline" id="esa-kappa-three">Three categories</button></div>
<p id="esa-kappa-error" role="alert" hidden></p>
<div class="table-wrap" role="status" aria-live="polite" aria-atomic="true"><table><caption>Agreement summary</caption><tbody>
<tr><th scope="row">Cases N</th><td><output id="esa-kappa-n">50</output></td></tr>
<tr><th scope="row">Observed agreement pₒ</th><td><output id="esa-kappa-po">0.7000</output></td></tr>
<tr><th scope="row">Chance agreement pₑ</th><td><output id="esa-kappa-pe">0.5000</output></td></tr>
<tr><th scope="row">Cohen's κ (selected weighting)</th><td><output id="esa-kappa-kappa">0.4000</output></td></tr>
<tr><th scope="row">Maximum attainable κ</th><td><output id="esa-kappa-kmax">0.8000</output></td></tr>
<tr><th scope="row">Large-sample SE</th><td><output id="esa-kappa-se">0.1270</output></td></tr>
<tr><th scope="row">Approximate 95% CI</th><td><output id="esa-kappa-ci">[0.1511, 0.6489]</output></td></tr>
</tbody></table></div>
<p id="esa-kappa-note" role="status" aria-live="polite"></p>
</section>
<h2>Interpreting kappa</h2>
<p>Verbal benchmarks such as "0.41–0.60 = moderate" (Landis and Koch, 1977) are widely quoted but arbitrary; they were not derived from data and ignore prevalence, the number of categories and the consequences of disagreement. Report \(\hat\kappa\), its confidence interval, \(p_o\) and the agreement table, and judge adequacy in the context of the application.</p>
<h2>Assumptions and limitations</h2>
<ul class="bullets"><li>The same N cases are rated independently by exactly two raters, using the same mutually exclusive categories.</li><li>Unweighted kappa treats every disagreement as equally serious. For ordered categories (mild/moderate/severe), weighted kappa gives partial credit to near misses; the result depends on the chosen weights.</li><li>Kappa depends on prevalence and on each rater's marginal tendencies, so values from populations with different prevalences are not directly comparable.</li><li>For more than two raters, use a multi-rater coefficient such as Fleiss' kappa.</li></ul>
<div class="summary-box"><h2>Lesson takeaways</h2><ul class="bullets"><li>\(\kappa=(p_o-p_e)/(1-p_e)\) measures agreement beyond chance.</li><li>Different marginal tendencies cap the attainable \(\kappa\) below 1.</li><li>Dominant categories can make high agreement produce low \(\kappa\) (the kappa paradox).</li><li>Report the table, \(p_o\), \(\hat\kappa\) and its interval rather than a verbal label alone.</li></ul></div>
</div></section>
<style>
#esa-kappa-lab{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-kappa-lab label{display:block;font-weight:650;margin-bottom:8px}
#esa-kappa-lab select{display:block;box-sizing:border-box;width:100%;max-width:100%;padding:8px;margin-bottom:8px;font:inherit}
#esa-kappa-lab textarea{display:block;box-sizing:border-box;width:100%;max-width:100%;padding:10px;font:inherit;border:1px solid var(--border);border-radius:8px;resize:vertical}
#esa-kappa-lab .esa-kappa-controls{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
#esa-kappa-lab .esa-kappa-controls button{max-width:100%;white-space:normal}
#esa-kappa-lab .table-wrap{display:block;max-width:100%;overflow-x:auto}
#esa-kappa-lab [hidden]{display:none!important}
#esa-kappa-lab [role="alert"]{color:#b42318;font-weight:700}
#esa-kappa-lab :is(textarea,button,select):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-long-math{max-width:100%;overflow-x:auto}
</style>
<script defer src="/js/cohens-kappa-lab.js"></script>
