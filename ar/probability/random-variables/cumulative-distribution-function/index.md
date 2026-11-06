---
layout: default
title: دالة التوزيع التراكمي للمتغيرات العشوائية (CDF)
description: شرح عربي دقيق لدالة التوزيع التراكمي للمتغيرات المنفصلة والمتصلة مع مختبر تفاعلي لبرنولي والتوزيع المنتظم.
permalink: /ar/probability/random-variables/cumulative-distribution-function/
lang: ar
math: true
sidebar: false
translation_pair: cumulative-distribution-function
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">المتغيرات العشوائية</span><span class="badge">درس تفاعلي</span></div>
<h1>دالة التوزيع التراكمي (CDF)</h1>
<p class="lead">تصف دالة التوزيع التراكمي احتمال أن يأخذ المتغير العشوائي قيمة أقل من أو تساوي حداً محدداً، سواء أكان متغيراً منفصلاً أم متصلاً.</p>
<p><a href="/probability/random-variables/cumulative-distribution-function/" lang="en" dir="ltr">Read in English: Cumulative Distribution Function</a></p>
</div></section>
<section><div class="content-narrow" dir="rtl">
<h2>التعريف</h2>
<p>لكل متغير عشوائي حقيقي \(X\)، نعرّف دالة التوزيع التراكمي عند \(x\) كما يلي:</p>
<div class="esa-ar-cdf-math" dir="ltr">\[F_X(x)=P(X\leq x).\]</div>
<p>تُحسب دالة المتغير المنفصل بتجميع كتل الاحتمال عند القيم الأقل من \(x\) أو المساوية له، أما للمتغير المتصل ذي الكثافة \(f\) فتساوي مساحة الكثافة إلى يسار \(x\):</p>
<div class="esa-ar-cdf-math" dir="ltr">\[F_X(x)=\sum_{t\leq x}P(X=t),\qquad F_X(x)=\int_{-\infty}^x f(t)\,dt\quad\text{(عند وجود كثافة)}.\]</div>
<h2>خصائص أساسية</h2>
<ul class="bullets"><li>دالة التوزيع التراكمي غير متناقصة وتأخذ قيماً بين صفر وواحد.</li><li>دالة التوزيع التراكمي <strong>مستمرة من اليمين</strong>؛ وقد تقفز عند القيم التي تمتلك كتلة احتمالية موجبة.</li><li>نهايتها عندما يتجه \(x\) إلى سالب ما لا نهاية تساوي صفراً، وعندما يتجه إلى موجب ما لا نهاية تساوي واحداً.</li><li>لا يُشترط أن تكون كل دالة توزيع تراكمي متصلة أو قابلة للاشتقاق.</li></ul>
<div class="esa-ar-cdf-math" dir="ltr">\[P(L<X\leq R)=F_X(R)-F_X(L)\qquad (L<R).\]</div>
<p>الحد الأيسر مستبعد والحد الأيمن مشمول. لهذا الفرق أهمية في المتغيرات المنفصلة؛ أما في التوزيعات ذات الكثافة فلا يؤثر إدراج نقطة منفردة في الاحتمال.</p>
<h2>مثال برنولي</h2>
<p>إذا كان \(X\sim\mathrm{Bernoulli}(p)\)، فإن احتمال القيمة صفر هو \(1-p\) واحتمال القيمة واحد هو \(p\). لذلك تكون الدالة صفرًا قبل الصفر، و\(1-p\) من الصفر إلى ما قبل الواحد، وواحدًا ابتداءً من الواحد:</p>
<div class="esa-ar-cdf-math" dir="ltr">\[F_X(x)=\begin{cases}0,&x<0,\\1-p,&0\leq x<1,\\1,&x\geq1.\end{cases}\]</div>
<p>عند \(p=0.35\)، نجد \(F_X(0)=0.65\)، بينما \(P(0<X\leq1)=0.35\).</p>
<h2>مثال: التوزيع المنتظم المتصل</h2>
<p>إذا كان \(X\sim U(a,b)\) و\(a<b\)، يكون التراكم خطيًا داخل المجال:</p>
<div class="esa-ar-cdf-math" dir="ltr">\[F_X(x)=\begin{cases}0,&x<a,\\(x-a)/(b-a),&a\leq x<b,\\1,&x\geq b.\end{cases}\]</div>
<p>للتوزيع المنتظم على \([0,2]\)، نحصل على \(F_X(0.5)=0.25\)، واحتمال الفترة \(0<X\leq1\) يساوي \(0.5\).</p>
<noscript><p>تحتاج الأداة التفاعلية إلى جافاسكريبت، بينما يبقى الشرح الرياضي متاحاً دونها.</p></noscript>
<section class="concept-box" id="esa-cdf-explorer" lang="ar" aria-labelledby="esa-cdf-explorer-title">
<h2 id="esa-cdf-explorer-title">مختبر تفاعلي: مقارنة برنولي والتوزيع المنتظم</h2>
<p>غيّر نوع التوزيع ومعلماته وقيمة \(x\) وحدّي الفترة لتشاهد \(F(x)\) واحتمال الفترة.</p>
<div class="esa-cdf-grid">
<div><label for="esa-cdf-kind">نوع التوزيع</label><select id="esa-cdf-kind"><option value="bernoulli">برنولي (منفصل)</option><option value="uniform">منتظم (متصل)</option></select></div>
<div id="esa-cdf-bernoulli-options"><label for="esa-cdf-p">احتمال النجاح p: <output id="esa-cdf-p-label">0.35</output></label><input id="esa-cdf-p" type="range" min="0" max="1" step="0.05" value="0.35"></div>
<div id="esa-cdf-uniform-options" hidden><label for="esa-cdf-a">الحد الأدنى a: <output id="esa-cdf-a-label">0.0</output></label><input id="esa-cdf-a" type="range" min="-1" max="1.5" step="0.5" value="0"><label for="esa-cdf-b">الحد الأعلى b: <output id="esa-cdf-b-label">2.0</output></label><input id="esa-cdf-b" type="range" min="0" max="3" step="0.5" value="2"></div>
<div><label for="esa-cdf-x">احسب عند x = <output id="esa-cdf-x-label">0.50</output></label><input id="esa-cdf-x" type="range" min="-1.5" max="3.5" step="0.05" value="0.5"></div>
<div><label for="esa-cdf-left">بداية الفترة L (مستبعدة)</label><input id="esa-cdf-left" dir="ltr" type="number" step="any" value="0" aria-describedby="esa-cdf-error"></div>
<div><label for="esa-cdf-right">نهاية الفترة R (مشمولة)</label><input id="esa-cdf-right" dir="ltr" type="number" step="any" value="1" aria-describedby="esa-cdf-error"></div>
</div>
<p id="esa-cdf-error" role="alert" hidden></p>
<div class="esa-cdf-figure"><svg id="esa-cdf-chart" role="img" viewBox="0 0 400 242" aria-label="منحنى دالة التوزيع التراكمي"></svg></div>
<div id="esa-cdf-results" role="status" aria-live="polite" aria-atomic="true"><p>الاحتمال التراكمي F(x): <strong><output id="esa-cdf-fx" dir="ltr">—</output></strong></p><p>احتمال الفترة P(L&lt;X≤R): <output id="esa-cdf-interval" dir="ltr">—</output></p><p id="esa-cdf-description"></p></div>
<button type="button" class="btn btn-outline" id="esa-cdf-reset">استعادة القيم الأصلية</button>
<p>دالة برنولي درجية مستمرة من اليمين، بينما دالة التوزيع المنتظم متصلة. يختلف تضمين الحد الأيسر بالنسبة إلى متغير منفصل عندما توجد كتلة احتمالية عنده.</p>
</section>
<style>
#esa-cdf-explorer{min-width:0;max-width:100%;overflow-wrap:anywhere}
#esa-cdf-explorer .esa-cdf-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:12px 0}
#esa-cdf-explorer .esa-cdf-grid>div{min-width:0}
#esa-cdf-explorer label{display:block;font-weight:650;margin:4px 0 8px}
#esa-cdf-explorer input,#esa-cdf-explorer select{box-sizing:border-box;display:block;width:100%;min-width:0;max-width:100%;font:inherit;background:var(--surface);color:var(--text)}
#esa-cdf-explorer input[type=number],#esa-cdf-explorer select{border:1px solid var(--border-strong);border-radius:8px;padding:10px}
#esa-cdf-explorer :is(input,select,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#esa-cdf-explorer svg{display:block;width:100%;height:auto;margin:10px auto}
#esa-cdf-explorer [hidden]{display:none!important}
#esa-cdf-explorer output{font-variant-numeric:tabular-nums}
.esa-ar-cdf-math{direction:ltr;max-width:100%;overflow-x:auto}
@media(max-width:600px){#esa-cdf-explorer .esa-cdf-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/cdf-bernoulli-uniform-explorer.js"></script>
<h2>متى نستخدم دالة التوزيع التراكمي؟</h2>
<p>تُستخدم لحساب احتمالات المجالات والقيم المئينية، وتحديد التوزيعات الاحتمالية، وصياغة مسائل الموثوقية والمخاطر والاستدلال الإحصائي.</p>
<div class="summary-box"><h2>الخلاصة</h2><p>يوحّد تعريف \(F_X(x)=P(X\leq x)\) المتغيرات المنفصلة والمتصلة. الفرق بين قيمتين للدالة يعطي احتمال الفترة المفتوحة يساراً والمغلقة يميناً، مع ضرورة مراعاة القفزات في الحالة المنفصلة.</p></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/random-variables/continuous-random-variables/">السابق: المتغيرات المتصلة</a><a class="btn" href="/probability/random-variables/expectation/" lang="en" dir="ltr">Next: Expectation (English)</a></div>
</div></section>
