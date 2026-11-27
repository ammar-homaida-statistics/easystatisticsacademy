---
layout: default
title: فترة الثقة للمتوسط عندما يكون σ مجهولًا — فترة t
description: "شرح عربي لفترة t للمتوسط عندما يكون الانحراف المعياري للمجتمع مجهولًا: استبدال σ بـ s، ودرجات الحرية n − 1، والصيغة x̄ ± t·s/√n، ومثال محسوب بمستويات 90% و95% و99%، ومقارنة بفترة z."
permalink: /ar/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: ci-for-mean-sigma-unknown-t
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاستدلال</span><span class="badge">فترات الثقة</span><span class="badge">المتوسط</span></div>
<h1>فترة الثقة للمتوسط عندما يكون σ مجهولًا — فترة t</h1>
<p class="lead">في العمل الإحصائي الحقيقي لا يكون الانحراف المعياري للمجتمع معلومًا تقريبًا أبدًا.</p>
<p class="lead">لذلك نقدّره من العيّنة، وهذا يضيف عدم يقين إضافيًا، ولهذا نستخدم توزيع t بدل التوزيع الطبيعي.</p>
<p><a href="/inference/confidence-intervals/ci-for-mean-sigma-unknown-t/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/confidence-intervals/ci-for-mean-sigma-known-z/">الدرس السابق: فترة z للمتوسط</a></p>
</div></section>
<section><div class="content-narrow">

<h2>1. لماذا تكون فترة z غير واقعية عادةً؟</h2>
<p>تفترض <a href="/ar/inference/confidence-intervals/ci-for-mean-sigma-known-z/">فترة z</a> أن الانحراف المعياري للمجتمع \(\sigma\) معلوم، وهذا نادر في الممارسة؛ ففي معظم الحالات لا نملك إلا بيانات العيّنة، فيجب تقدير تباين المجتمع.</p>

<h2>2. استبدال σ بـ s</h2>
<p>لأن \(\sigma\) مجهول نستبدل به الانحراف المعياري للعيّنة \(s\). ويضيف هذا التقدير عدم يقين إضافيًا، لأن متوسط العيّنة يتغير من عيّنة إلى أخرى، والانحراف المعياري للعيّنة يتغير كذلك؛ فيجب أخذ المصدرين في الحسبان.</p>

<h2>3. لماذا يظهر توزيع t؟</h2>
<p>عند استبدال \(s\) بـ \(\sigma\) لا تعود الإحصاءة المعيارية تتبع التوزيع الطبيعي المعياري. فإذا كانت المشاهدات مستقلة من مجتمع طبيعي، فإنها تتبع توزيع t بـ \(n-1\) درجة حرية تمامًا:</p>
<div dir="ltr">\[T=\frac{\bar X-\mu}{S/\sqrt n}\sim t_{n-1}.\]</div>
<p>وللمجتمعات غير الطبيعية يكون هذا تقريبًا، تتحسن دقته مع ازدياد حجم العيّنة.</p>
<div class="concept-box"><strong>الفكرة الرئيسة:</strong><p>يأخذ توزيع t في الحسبان عدم اليقين الناتج عن تقدير تباين المجتمع.</p></div>

<h2>4. توزيع t من جديد</h2>
<p>يشبه توزيع t التوزيع الطبيعي لكن ذيوله أثقل، فيخصص احتمالًا أكبر للقيم المتطرفة، وهذا الاحتمال الإضافي يعكس عدم اليقين الناتج عن تقدير \(\sigma\).</p>

<h2>5. الخطأ المعياري</h2>
<p>عندما يكون \(\sigma\) مجهولًا يصبح الخطأ المعياري المقدَّر:</p>
<div dir="ltr">\[\widehat{\operatorname{SE}}(\bar X)=\frac{s}{\sqrt n}.\]</div>

<h2>6. صيغة فترة t</h2>
<p>بتطبيق <a href="/ar/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/">مخطط فترة الثقة</a>:</p>
<div dir="ltr">\[\bar x\pm t_{n-1,\,1-\alpha/2}\,\frac{s}{\sqrt n}.\]</div>
<p>هذه فترة t لمتوسط مجتمع من عيّنة واحدة.</p>

<h2>7. مكوّنات الصيغة</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">الرمز</th><th scope="col">المعنى</th></tr></thead>
<tbody>
<tr><td dir="ltr">x̄</td><td>متوسط العيّنة</td></tr>
<tr><td dir="ltr">t*</td><td>القيمة الحرجة من توزيع t</td></tr>
<tr><td dir="ltr">s</td><td>الانحراف المعياري للعيّنة</td></tr>
<tr><td dir="ltr">n</td><td>حجم العيّنة</td></tr>
</tbody></table></div>

<h2>8. درجات الحرية</h2>
<p>بخلاف قيم z الحرجة، تعتمد قيم t الحرجة على درجات الحرية؛ ولفترة متوسط عيّنة واحدة يكون <span dir="ltr">df = n − 1</span>. والعيّنات الصغيرة تقدّم معلومات أقل عن تباين المجتمع، لذلك:</p>
<ul class="bullets"><li>درجات حرية قليلة ← قيم t حرجة أكبر</li><li>درجات حرية كثيرة ← t يقترب من z</li></ul>
<p>وهكذا يُضبط عرض الفترة تلقائيًا حسب حجم العيّنة (انظر جدول <a href="/ar/inference/confidence-intervals/critical-values-z-and-t/">القيم الحرجة</a>).</p>

<h2>9. مثال محسوب</h2>
<p>لنفترض: متوسط العيّنة 80، والانحراف المعياري للعيّنة 15، وحجم العيّنة 25، ومستوى الثقة 95%.</p>
<h3>الخطوة 1: الخطأ المعياري</h3>
<div dir="ltr">\[\widehat{\operatorname{SE}}(\bar X)=\frac{15}{\sqrt{25}}=3.\]</div>
<h3>الخطوة 2: درجات الحرية</h3>
<div dir="ltr">\[\operatorname{df}=25-1=24.\]</div>
<h3>الخطوة 3: القيمة الحرجة</h3>
<p>لثقة 95% و24 درجة حرية: <span dir="ltr">t* ≈ 2.064</span> (وبدقة أكبر <span dir="ltr">2.0639</span>).</p>
<h3>الخطوة 4: هامش الخطأ</h3>
<div dir="ltr">\[\operatorname{ME}\approx2.064\times3=6.192\approx6.19.\]</div>
<h3>الخطوة 5: بناء الفترة</h3>
<div dir="ltr">\[80\pm6.192\approx[\,73.81,\ 86.19\,].\]</div>
<div class="table-wrap"><table>
<caption>الفترة نفسها بمستويات ثقة مختلفة (<span dir="ltr">x̄ = 80, SE = 3, df = 24</span>)</caption>
<thead><tr><th scope="col">مستوى الثقة</th><th scope="col">t*</th><th scope="col">هامش الخطأ</th><th scope="col">الفترة</th></tr></thead>
<tbody dir="ltr">
<tr><td>90%</td><td>1.711</td><td>5.13</td><td>[74.87, 85.13]</td></tr>
<tr><td>95%</td><td>2.064</td><td>6.19</td><td>[73.81, 86.19]</td></tr>
<tr><td>99%</td><td>2.797</td><td>8.39</td><td>[71.61, 88.39]</td></tr>
</tbody></table></div>

<h2>10. مقارنة فترتي z وt</h2>
<p>لو استخدمنا خطأً معياريًا قدره 3 مع قيمة z الحرجة 1.960 لكان هامش الخطأ 5.88 بدل 6.19؛ فعند قيمة الخطأ المعياري نفسها تكون فترة t أعرض، وهذا يعكس عدم اليقين الإضافي من تقدير \(\sigma\). (ولأن \(s\) نفسه يتغير من عيّنة إلى أخرى، فقد تكون فترة t في عيّنة معيّنة أضيق من فترة z المبنية على \(\sigma\) الحقيقي، لكنها أعرض في المتوسط.)</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">الخاصية</th><th scope="col">فترة z</th><th scope="col">فترة t</th></tr></thead>
<tbody>
<tr><td>الانحراف المعياري للمجتمع معلوم؟</td><td>نعم</td><td>لا</td></tr>
<tr><td>القيم الحرجة</td><td>z</td><td>t</td></tr>
<tr><td>تعتمد على درجات الحرية؟</td><td>لا</td><td>نعم</td></tr>
<tr><td>القيمة الحرجة أكبر؟</td><td>لا</td><td>نعم</td></tr>
</tbody></table></div>

<h2>11. ماذا يحدث مع ازدياد حجم العيّنة؟</h2>
<p>تقدّر العيّنات الأكبر تباين المجتمع بدقة أكبر؛ فمع ازدياد حجم العيّنة تزداد درجات الحرية، وتنخفض قيم t الحرجة، ويقترب توزيع t من التوزيع الطبيعي، حتى يصبح الفرق بين z وt صغيرًا جدًا.</p>

<h2>12. لماذا هذه أهم فترة للمتوسط؟</h2>
<p>لأن \(\sigma\) نادرًا ما يكون معلومًا، فإن فترة t هي الطريقة المعيارية لتقدير متوسطات المجتمعات، ومن أكثر فترات الثقة استخدامًا في الإحصاء.</p>

<h2>13. متى تكون فترة t مناسبة؟</h2>
<ul class="bullets"><li>البيانات من عيّنة عشوائية</li><li>المشاهدات مستقلة (انظر <a href="/ar/inference/assumptions-robustness/independence-and-dependence/">الاستقلال والاعتماد</a>)</li><li>توزيع المعاينة طبيعي تقريبًا: مجتمع طبيعي، أو عيّنة كبيرة بما يكفي لشكل المجتمع</li></ul>
<div class="concept-box"><strong>الرسالة الأساسية:</strong><p>عندما يكون تباين المجتمع مجهولًا، تستخدم فترات الثقة للمتوسط الانحراف المعياري للعيّنة، وقيمة t الحرجة، والخطأ المعياري المقدَّر \(s/\sqrt n\).</p></div>

<h2>14. ماذا بعد؟</h2>
<p>تعتمد كل صيغة لفترة الثقة على افتراضات، وأهمها لفترات المتوسط: الاستقلال، والطبيعية، ومبرهنة النهاية المركزية. ويتناول الدرس التالي متى تكون فترات المتوسط جديرة بالثقة ومتى يجب الحذر.</p>

<div class="summary-box">
<h2>خلاصة الدرس</h2>
<ul class="bullets">
<li>تُستخدم فترة t عندما يكون الانحراف المعياري للمجتمع مجهولًا.</li>
<li>يُقدَّر الخطأ المعياري بـ \(s/\sqrt n\).</li>
<li>صيغة الفترة: <span dir="ltr">x̄ ± t*·SE</span>.</li>
<li>تعتمد قيم t الحرجة على درجات الحرية.</li>
<li>درجات الحرية لفترة متوسط عيّنة واحدة تساوي <span dir="ltr">n − 1</span>.</li>
<li>عند الخطأ المعياري نفسه تكون فترات t أعرض من فترات z.</li>
<li>مع ازدياد حجم العيّنة يقترب توزيع t من التوزيع الطبيعي.</li>
<li>فترة t أكثر فترات الثقة للمتوسط استخدامًا.</li>
</ul>
</div>

<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/inference/confidence-intervals/ci-for-mean-sigma-known-z/">→ السابق: فترة z للمتوسط</a>
<a class="btn" href="/ar/inference/confidence-intervals/conditions-normality-clt-independence/">التالي: الشروط ←</a>
</div>
</div></section>
