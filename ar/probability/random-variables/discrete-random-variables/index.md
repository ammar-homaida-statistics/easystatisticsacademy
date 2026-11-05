---
layout: default
title: المتغيرات العشوائية المنفصلة ودالة الكتلة الاحتمالية
description: درس عربي عن المتغيرات المنفصلة ودوال الكتلة الاحتمالية وحساب المتوسط والتباين مع مختبر تفاعلي.
permalink: /ar/probability/random-variables/discrete-random-variables/
lang: ar
sidebar: false
translation_pair: discrete-random-variables
math: true
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">نظرية الاحتمالات</span><span class="badge">دالة الكتلة الاحتمالية</span></div>
<h1>المتغيرات العشوائية المنفصلة ودالة الكتلة الاحتمالية</h1>
<p class="lead">نستخدم المتغير العشوائي المنفصل لوصف عدد النتائج أو الأحداث، وتحدد دالة الكتلة الاحتمالية فرصة كل قيمة.</p>
<p><a href="/probability/random-variables/discrete-random-variables/" lang="en" dir="ltr">English: Discrete Random Variables &amp; PMF</a></p>
</div></section>
<section><div class="content-narrow" dir="rtl">
<h2>الفرق بين نتيجة التجربة وقيمة المتغير</h2>
<p>عند رمي قطعتين من النقود، قد تكون النتيجة <span dir="ltr">HT</span> أو <span dir="ltr">TH</span>؛ لكن إذا عرّفنا X بأنه عدد الصور، فإن القيمتين تُمثَّلان بالقيمة نفسها <span dir="ltr">X=1</span>. النتيجة عنصر من فضاء العينة، بينما المتغير العشوائي دالة عددية على هذا الفضاء.</p>
<h2>ما المتغير العشوائي المنفصل؟</h2>
<p>هو متغير عشوائي له مجموعة قيم محدودة أو قابلة للعدّ، مثل عدد الزبائن في ساعة أو عدد النجاحات في سلسلة من التجارب. ليست جميع القيم بالضرورة متساوية الاحتمال.</p>
<h2>دالة الكتلة الاحتمالية (PMF)</h2>
<p>نسمي احتمال أخذ X للقيمة x دالة الكتلة الاحتمالية:</p>
<div class="esa-pmf-math" dir="ltr">\[p_X(x)=P(X=x).\]</div>
<p>لكي تكون الدالة صالحة، يلزم أن تكون الاحتمالات غير سالبة ومجموعها واحداً عبر جميع قيم المتغير.</p>
<div class="esa-pmf-math" dir="ltr">\[p_X(x)\geq0,\qquad \sum_{x}p_X(x)=1.\]</div>
<h2>المتوسط والتباين</h2>
<p>التوقع هو المتوسط المرجح لقيم المتغير باحتمالاتها، والتباين هو المتوسط المرجح لمربعات الانحراف عن التوقع.</p>
<div class="esa-pmf-math" dir="ltr">\[\mu=E(X)=\sum_x xp_X(x),\qquad \mathrm{Var}(X)=\sum_x(x-\mu)^2p_X(x).\]</div>
<p>على سبيل المثال، لقيم X=0 و1 و2 واحتمالات 0.2 و0.5 و0.3، فإن التوقع يساوي 1.1 والتباين يساوي 0.49. لأن \(0.2(0-1.1)^2+0.5(1-1.1)^2+0.3(2-1.1)^2=0.49\).</p>
<noscript><p role="status">يتطلب المختبر التفاعلي تفعيل جافاسكريبت؛ تبقى المعادلات والشرح متاحين دونها.</p></noscript>
<section class="concept-box" id="esa-three-pmf-lab" aria-labelledby="esa-pmf-title" style="min-width:0;overflow-wrap:anywhere">
<h2 id="esa-pmf-title">مختبر تفاعلي: ثلاثة احتمالات</h2>
<p>عدّل احتمالات X=0 وX=1 وX=2؛ يجب أن يكون كل احتمال بين الصفر والواحد وأن يساوي مجموعها واحداً. الإدخالات غير الصالحة لا تُطبَّع تلقائياً.</p>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,145px),1fr));gap:12px">
<label for="esa-pmf-p0"><span dir="ltr">P(X=0)</span><input id="esa-pmf-p0" aria-describedby="esa-pmf-error" type="number" min="0" max="1" step="any" inputmode="decimal" dir="ltr" value="0.2" style="width:100%"></label>
<label for="esa-pmf-p1"><span dir="ltr">P(X=1)</span><input id="esa-pmf-p1" aria-describedby="esa-pmf-error" type="number" min="0" max="1" step="any" inputmode="decimal" dir="ltr" value="0.5" style="width:100%"></label>
<label for="esa-pmf-p2"><span dir="ltr">P(X=2)</span><input id="esa-pmf-p2" aria-describedby="esa-pmf-error" type="number" min="0" max="1" step="any" inputmode="decimal" dir="ltr" value="0.3" style="width:100%"></label>
</div>
<p role="alert" id="esa-pmf-error" hidden>أدخل ثلاثة احتمالات صالحة مجموعها واحد.</p>
<div id="esa-pmf-results" aria-live="polite">
<p>مجموع الاحتمالات: <output id="esa-pmf-sum" dir="ltr">1.0000</output>؛ التوقع: <output id="esa-pmf-mean" dir="ltr">1.1000</output>؛ التباين: <output id="esa-pmf-variance" dir="ltr">0.4900</output>.</p>
</div>
<svg id="esa-pmf-chart" role="img" viewBox="0 0 480 220" style="width:100%;height:auto;display:block" aria-label="مخطط أعمدة دالة الكتلة الاحتمالية"></svg>
<button class="btn btn-outline" id="esa-pmf-reset" type="button">إعادة المثال</button>
</section>
<h2>مقارنة بالمتغير المتصل</h2>
<p>في التوزيع المنفصل يمكن أن يكون احتمال قيمة مفردة موجباً. أما التوزيع المستمر ذي الكثافة فاحتمال النقطة المفردة يساوي صفراً، وتحسب احتمالات الفترات بتكامل دالة الكثافة.</p>
<div class="summary-box"><h2>الخلاصة</h2><ul class="bullets"><li>قيم المتغير المنفصل محدودة أو قابلة للعدّ.</li><li>كل احتمال غير سالب، ومجموع الكتل يساوي واحداً.</li><li>حساب التوقع والتباين يعتمد على الاحتمالات المرجحة.</li><li>النتائج الأولية المختلفة قد تؤدي إلى قيمة المتغير نفسها.</li></ul></div>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/probability/random-variables/what-is-a-random-variable/">السابق: ما المتغير العشوائي؟</a><a class="btn" href="/ar/probability/random-variables/continuous-random-variables/">التالي: المتغيرات العشوائية المتصلة</a></div>
</div></section>
<style>.esa-pmf-math{direction:ltr;max-width:100%;overflow-x:auto}.esa-pmf-math mjx-container[display="true"]{width:max-content;min-width:100%;text-align:left}</style>
<script defer src="/js/three-point-pmf-explorer.js"></script>
