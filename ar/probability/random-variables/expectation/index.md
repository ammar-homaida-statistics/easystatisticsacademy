---
layout: default
title: القيمة المتوقعة والمتوسط للمتغير العشوائي
description: شرح عربي للقيمة المتوقعة للمتغيرات العشوائية المنفصلة والمتصلة، وخاصية الخطية، وحساب التباين مع مختبر تفاعلي لثلاث نتائج.
permalink: /ar/probability/random-variables/expectation/
lang: ar
math: true
sidebar: false
translation_pair: random-variable-expectation
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاحتمالات</span><span class="badge">المتغيرات العشوائية</span><span class="badge">مختبر تفاعلي</span></div>
<h1>القيمة المتوقعة للمتغير العشوائي</h1>
<p class="lead">تختصر القيمة المتوقعة مركز التوزيع الاحتمالي بوصفه متوسطاً موزوناً بالقيم الاحتمالية، ولا تعني بالضرورة القيمة التي سنشاهدها في تجربة واحدة.</p>
<p><a href="/probability/random-variables/expectation/" lang="en" dir="ltr">Read in English: Expectation</a></p>
</div></section>
<section><div class="content-narrow" dir="rtl">
<h2>المتوسط الاحتمالي للمتغير المنفصل</h2>
<p>إذا كان \(X\) متغيراً منفصلاً بقيم \(x_i\) واحتمالات \(p_i=P(X=x_i)\)، وكانت السلسلة متقاربة تقارباً مطلقاً، فإن:</p>
<div class="esa-ar-expectation-math" dir="ltr">\[E(X)=\sum_i x_i p_i,\qquad p_i\geq0,\quad\sum_i p_i=1.\]</div>
<p>مثلاً عند النتائج صفر وواحد واثنين، باحتمالات 0.2 و0.5 و0.3، نحصل على:</p>
<div class="esa-ar-expectation-math" dir="ltr">\[E(X)=0(0.2)+1(0.5)+2(0.3)=1.1.\]</div>
<p>القيمة 1.1 ليست نتيجة ممكنة لهذا المتغير، لكنها المتوسط النظري طويل الأجل إذا تكرر السحب المستقل من التوزيع نفسه.</p>
<h2>المتغير المتصل</h2>
<p>عندما يكون للمتغير كثافة احتمالية \(f(x)\)، ويكون \(E(|X|)\) منتهياً، نحسب متوسطه بالتكامل:</p>
<div class="esa-ar-expectation-math" dir="ltr">\[E(X)=\int_{-\infty}^{\infty}xf(x)\,dx.\]</div>
<p>إذا كان المتغير منتظماً على الفترة \([a,b]\)، فإن \(E(X)=(a+b)/2\).</p>
<h2>خاصية الخطية</h2>
<p>إذا كانت التوقعات موجودة ومنتهية، فإن:</p>
<div class="esa-ar-expectation-math" dir="ltr">\[E(aX+b)=aE(X)+b,\qquad E(X+Y)=E(X)+E(Y).\]</div>
<p>لا تتطلب خطية التوقع الاستقلال بين \(X\) و\(Y\)، لكن وجود التوقعات شرط مهم.</p>
<h2>التباين والانحراف المعياري</h2>
<p>يقيس التباين متوسط مربع بُعد القيم عن المتوسط، بشرط أن يكون العزم الثاني منتهياً:</p>
<div class="esa-ar-expectation-math" dir="ltr">\[\operatorname{Var}(X)=E\!\left[(X-E(X))^2\right]=E(X^2)-[E(X)]^2,\qquad \operatorname{SD}(X)=\sqrt{\operatorname{Var}(X)}.\]</div>
<p>في مثالنا، \(E(X^2)=0+0.5+4(0.3)=1.7\)، والتباين \(1.7-1.1^2=0.49\)، والانحراف المعياري \(0.7\).</p>
<noscript><p>يحتاج المختبر التفاعلي إلى جافاسكريبت. تبقى الأمثلة والمعادلات متاحة دونها.</p></noscript>
<section class="concept-box" id="esa-moments-lab" lang="ar" aria-labelledby="esa-mom-title">
<h2 id="esa-mom-title">مختبر تفاعلي: القيمة المتوقعة والتباين لثلاث نتائج</h2>
<p>غيّر القيم والاحتمالات. يشترط ألا يكون أي احتمال سالباً وأن يساوي مجموع الاحتمالات واحداً.</p>
<div class="esa-mom-grid">
<label for="esa-mom-x0">النتيجة الأولى \(x_1\)<input id="esa-mom-x0" type="number" step="any" value="0" dir="ltr" aria-describedby="esa-mom-error"></label>
<label for="esa-mom-p0">احتمالها \(p_1\)<input id="esa-mom-p0" type="number" step="any" value="0.2" min="0" max="1" dir="ltr" aria-describedby="esa-mom-error"></label>
<label for="esa-mom-x1">النتيجة الثانية \(x_2\)<input id="esa-mom-x1" type="number" step="any" value="1" dir="ltr" aria-describedby="esa-mom-error"></label>
<label for="esa-mom-p1">احتمالها \(p_2\)<input id="esa-mom-p1" type="number" step="any" value="0.5" min="0" max="1" dir="ltr" aria-describedby="esa-mom-error"></label>
<label for="esa-mom-x2">النتيجة الثالثة \(x_3\)<input id="esa-mom-x2" type="number" step="any" value="2" dir="ltr" aria-describedby="esa-mom-error"></label>
<label for="esa-mom-p2">احتمالها \(p_3\)<input id="esa-mom-p2" type="number" step="any" value="0.3" min="0" max="1" dir="ltr" aria-describedby="esa-mom-error"></label>
</div>
<p id="esa-mom-error" role="alert" hidden></p>
<div id="esa-mom-results" aria-live="polite">
<p>مجموع الاحتمالات: <output id="esa-mom-sum" dir="ltr">1.000000</output> · القيمة المتوقعة: <strong><output id="esa-mom-mean" dir="ltr">1.100000</output></strong></p>
<p>العزم الثاني: <output id="esa-mom-second" dir="ltr">1.700000</output> · التباين: <output id="esa-mom-variance" dir="ltr">0.490000</output> · الانحراف المعياري: <output id="esa-mom-sd" dir="ltr">0.700000</output></p>
</div>
<svg id="esa-mom-chart" role="img" viewBox="0 0 480 215" aria-label="مخطط توزيع الكتل الاحتمالية" style="width:100%;height:auto;display:block"></svg>
<button type="button" id="esa-mom-reset" class="btn btn-outline">استعادة المثال</button>
<p>قد تكون القيمة المتوقعة خارج مجموعة النتائج الممكنة، كما لا ينبغي الخلط بين التباين النظري وتباين العينة المحسوب من بيانات مشاهدة. يمكن للقيم السالبة أن تدخل في المتوسط بشكل طبيعي.</p>
</section>
<style>.esa-ar-expectation-math{direction:ltr;max-width:100%;overflow-x:auto}.esa-mom-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.esa-mom-grid label{min-width:0}.esa-mom-grid input{display:block;box-sizing:border-box;width:100%;min-width:0;background:var(--surface);color:var(--text);padding:9px;border:1px solid var(--border-strong);border-radius:8px}#esa-moments-lab{min-width:0;overflow-wrap:anywhere}#esa-moments-lab [hidden]{display:none!important}@media(max-width:480px){.esa-mom-grid{grid-template-columns:minmax(0,1fr)}}</style>
<script defer src="/js/three-point-moments-lab.js"></script>
<h2>أخطاء شائعة</h2>
<ul class="bullets"><li>اعتبار القيمة المتوقعة نتيجة حتمية في تجربة واحدة.</li><li>جمع القيم دون وزنها باحتمالاتها.</li><li>إدخال احتمالات لا مجموعها واحداً.</li><li>اعتبار خطية التوقع مشروطة بالاستقلال.</li><li>استخدام صيغة التباين دون تحقق وجود العزم الثاني.</li></ul>
<div class="summary-box"><h2>الخلاصة</h2><p>القيمة المتوقعة متوسط نظري موزون بالاحتمالات. تساعدنا التباينات والعزوم على وصف انتشار النتائج حول هذا المركز.</p></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/random-variables/cumulative-distribution-function/">السابق: دالة التوزيع التراكمي</a><a class="btn" href="/probability/random-variables/variance-and-standard-deviation/" lang="en" dir="ltr">Next: Variance and Standard Deviation (English)</a></div>
</div></section>
