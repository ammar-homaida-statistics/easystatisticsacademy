---
layout: default
title: توزيع برنولي
description: شرح عربي شامل لتوزيع برنولي للنتائج الثنائية ودالة الكتلة الاحتمالية والمتوسط والتباين مع مختبر تفاعلي.
permalink: /ar/probability/distributions/bernoulli-distribution/
lang: ar
sidebar: false
math: true
translation_pair: bernoulli-distribution
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">توزيعات متقطعة</span><span class="badge">نتائج ثنائية</span></div>
<h1>توزيع برنولي (Bernoulli Distribution)</h1>
<p><a lang="en" dir="ltr" href="/probability/distributions/bernoulli-distribution/">English — Bernoulli Distribution</a></p>
<p class="lead">يمثل توزيع برنولي تجربة عشوائية واحدة لها نتيجتان فقط، مثل نجاح تجربة أو إخفاقها، بشرط أن نعرف احتمال النجاح.</p>
</div></section>
<section class="section"><div class="content-narrow">
<h2>تعريف متغير برنولي</h2>
<p>لنرمز إلى النجاح بالقيمة 1 والإخفاق بالقيمة 0. إذا كان احتمال النجاح p، فإن احتمال الإخفاق 1−p، مع الشرط <span dir="ltr">0 ≤ p ≤ 1</span>. عندئذ نكتب:</p>
<div dir="ltr" class="esa-bern-math">\[
X\sim\operatorname{Bernoulli}(p),\qquad X\in\{0,1\}.
\]</div>
<h2>دالة الكتلة الاحتمالية (PMF)</h2>
<div dir="ltr" class="esa-bern-math">\[
P(X=x)=p^x(1-p)^{1-x},\qquad x\in\{0,1\},
\]</div>
<p>تكون الدالة صفرًا خارج القيمتين 0 و1. الصيغة السابقة تُستخدم بمعناها المكافئ المجزأ عند الحالتين الحديتين p=0 وp=1، تجنبًا للالتباس العددي حول التعبير 0 للأس 0.</p>
<div dir="ltr" class="esa-bern-math">\[
P(X=0)=1-p,\quad P(X=1)=p,\quad P(X=0)+P(X=1)=1.
\]</div>
<h2>المتوسط والتباين</h2>
<p>يمكن إيجاد المتوسط بجمع حاصل ضرب كل قيمة في احتمالها، ثم حساب التباين عن طريق مربعات الانحراف عن المتوسط:</p>
<div dir="ltr" class="esa-bern-math">\[
E(X)=0(1-p)+1(p)=p.
\]</div>
<div dir="ltr" class="esa-bern-math">\[
\operatorname{Var}(X)=E(X^2)-[E(X)]^2
=p-p^2=p(1-p).
\]</div>
<p>أكبر تباين يساوي 0.25 عندما p=0.5. وعند p=0 أو p=1 يصبح المتغير ثابتًا، ويصبح تباينه صفرًا.</p>
<h2>مثال محلول</h2>
<p>إذا كان احتمال نجاح محاولة واحدة 0.3، فإن احتمال عدم النجاح 0.7، ومتوسط عدد النجاحات في هذه المحاولة 0.3، وتباينه <span dir="ltr">0.3(0.7)=0.21</span>. المتوسط هنا قيمة متوقعة عبر عدد كبير من المحاولات، وليس نتيجة ممكنة للتجربة الواحدة.</p>
<h2>المتغيرات المؤشِّرة</h2>
<p>يُستخدم متغير المؤشر \(I(A)\) للدلالة على وقوع حدث A: يأخذ 1 إذا وقع الحدث و0 خلاف ذلك. لذا يتبع توزيع برنولي بمعلمة \(p=P(A)\). وتُستخدم المؤشرات في التصنيف الثنائي ومعدلات الاستجابة وتحليل الاستبيانات.</p>
<h2>علاقة برنولي بتوزيع ذي الحدين</h2>
<p>إذا كررنا التجربة نفسها n مرات مستقلة مع احتمال نجاح ثابت p، كان مجموع النجاحات ذا توزيع ثنائي الحدين <span dir="ltr">Binomial(n,p)</span>. أما برنولي فيمثل تجربة واحدة فقط؛ فهو الحالة الخاصة <span dir="ltr">Binomial(1,p)</span>. عدم الاستقلال أو تغير p بين المحاولات يمنع عادة استخدام النموذج الثنائي القياسي دون شروط إضافية.</p>
<div class="example-box"><strong>متى يكون مناسبًا؟</strong><p>عندما تمثل الملاحظة نتيجة ثنائية واحدة مُعرَّفة بوضوح. ولا يلائم هذا التوزيع مباشرة قياسات مستمرة أو نتائج بثلاث فئات فأكثر دون إعادة تعريف المتغير.</p></div>
</div></section>
<section class="section"><div class="content-narrow"><!-- Batch #72: نفس محرك الاحتمالات المستخدم في النسخة الإنجليزية -->
<section class="concept-box esa-bern-lab" id="esa-bernoulli-explorer" aria-labelledby="esa-bern-heading">
<h2 id="esa-bern-heading">مختبر تفاعلي لتوزيع برنولي</h2>
<p>غيّر احتمال النجاح p وشاهد احتمالي الإخفاق والنجاح والمتوسط والتباين. عند p=0 أو p=1 تصبح النتيجة يقينية ويكون التباين صفرًا.</p>
<label for="esa-bern-p">احتمال النجاح p (من 0 إلى 1)</label>
<input id="esa-bern-p" type="number" min="0" max="1" step="any" value="0.3" inputmode="decimal" dir="ltr">
<button id="esa-bern-reset" type="button" class="btn btn-outline">استعادة المثال</button>
<p id="esa-bern-error" role="alert" hidden></p>
<div class="table-wrap"><table><caption>نتائج توزيع برنولي (ست منازل عشرية)</caption>
<tbody><tr><th scope="row">P(X=0) = 1−p</th><td id="esa-bern-p0">—</td></tr>
<tr><th scope="row">P(X=1) = p</th><td id="esa-bern-p1">—</td></tr>
<tr><th scope="row">المتوسط E(X) = p</th><td id="esa-bern-mean">—</td></tr>
<tr><th scope="row">التباين Var(X) = p(1−p)</th><td id="esa-bern-variance">—</td></tr></tbody></table></div>
<svg id="esa-bern-chart" role="img" viewBox="0 0 610 260" aria-label="احتمالات توزيع برنولي للنجاح والإخفاق" dir="ltr"></svg>
<p class="muted-mini">الأعمدة تمثل كتلًا احتمالية عند الصفر والواحد، وليست دالة كثافة متصلة. تستخدم هذه الصفحة والنسخة الإنجليزية المحرك الحسابي نفسه.</p>
</section>
<script src="/js/bernoulli-explorer.js" defer></script><style>
.esa-bern-lab{max-width:100%;min-width:0;box-sizing:border-box;overflow-wrap:anywhere}
.esa-bern-lab *{box-sizing:border-box}
.esa-bern-lab label{display:block;font-weight:650;margin-bottom:6px}
.esa-bern-lab input{display:block;width:min(100%,290px);padding:10px;font:inherit;border:1px solid #777;border-radius:6px;margin-bottom:12px}
.esa-bern-lab .table-wrap{max-width:100%;overflow-x:auto}
.esa-bern-lab svg{display:block;width:100%;height:auto;max-width:610px}
.esa-bern-lab [hidden]{display:none!important}
.esa-bern-lab :is(input,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
</style>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>قيم متغير برنولي هي 0 و1 فقط.</li>
<li>احتمالا النجاح والإخفاق هما p و1−p.</li>
<li>المتوسط يساوي p والتباين يساوي p(1−p).</li>
<li>مجموع تجارب برنولي المستقلة المتطابقة يتبع توزيعًا ذا الحدين.</li>
</ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/distributions/binomial-distribution/">التالي: التوزيع ذو الحدين ←</a>
<a class="btn" lang="en" dir="ltr" href="/probability/distributions/bernoulli-distribution/">English lesson →</a></div>
</div></section>