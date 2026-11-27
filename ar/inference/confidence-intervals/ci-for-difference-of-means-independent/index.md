---
layout: default
title: فترة الثقة للفرق بين متوسطين (عيّنتان مستقلتان)
description: "شرح عربي لفترة الثقة للفرق بين متوسطي مجتمعين مستقلين: المقدِّر، والخطأ المعياري، وفترة ويلش ودرجات حرية ساترثويت، ومثال محسوب، ومعنى الصفر، مع مختبر تفاعلي لفترة ويلش."
permalink: /ar/inference/confidence-intervals/ci-for-difference-of-means-independent/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: ci-for-difference-of-means-independent
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاستدلال</span><span class="badge">فترات الثقة</span><span class="badge">مقارنة مجموعتين</span></div>
<h1>فترة الثقة للفرق بين متوسطين (عيّنتان مستقلتان)</h1>
{% include lab-noscript.html %}
<p class="lead">تركّز أسئلة بحثية كثيرة على مقارنة مجموعتين بدل تقدير متوسط واحد.</p>
<p class="lead">وتساعد فترات الثقة للفرق بين متوسطين على قياس مقدار اختلاف مجتمعين ومدى عدم اليقين في هذا الفرق المقدَّر.</p>
<p><a href="/inference/confidence-intervals/ci-for-difference-of-means-independent/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/confidence-intervals/ci-for-difference-of-proportions/">الدرس التالي: فترة الثقة للفرق بين نسبتين</a></p>
</div></section>
<section><div class="content-narrow">

<section class="concept-box" id="esa-welch-explorer" data-locale="ar" aria-labelledby="esa-welch-heading">
<h2 id="esa-welch-heading">مستكشف تفاعلي لفترة ويلش</h2>
<p>أدخل إحصاءات ملخّصة من مجموعتين مستقلتين. تقدّر الفترة \(\mu_1-\mu_2\) دون افتراض تساوي تبايني المجتمعين.</p>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr));gap:12px">
<label>متوسط المجموعة 1<input id="esa-welch-m1" type="number" value="82" step="any" dir="ltr" style="width:100%"></label>
<label>الانحراف المعياري للمجموعة 1<input id="esa-welch-s1" type="number" value="10" step="any" dir="ltr" style="width:100%"></label>
<label>حجم عيّنة المجموعة 1<input id="esa-welch-n1" type="number" value="40" min="2" max="1000000" step="1" dir="ltr" style="width:100%"></label>
<label>متوسط المجموعة 2<input id="esa-welch-m2" type="number" value="76" step="any" dir="ltr" style="width:100%"></label>
<label>الانحراف المعياري للمجموعة 2<input id="esa-welch-s2" type="number" value="12" step="any" dir="ltr" style="width:100%"></label>
<label>حجم عيّنة المجموعة 2<input id="esa-welch-n2" type="number" value="35" min="2" max="1000000" step="1" dir="ltr" style="width:100%"></label>
<label>مستوى الثقة<select id="esa-welch-confidence"><option value="90">90%</option><option value="95" selected>95%</option><option value="99">99%</option></select></label></div>
<p id="esa-welch-error" role="status" hidden>أدخل متوسطات منتهية، وانحرافات معيارية غير سالبة، وأحجام مجموعات صحيحة لا تقل عن 2، وتباينًا مقدَّرًا كليًا غير صفري.</p>
<div id="esa-welch-results" aria-live="polite"><p>الفرق: <output id="esa-welch-diff" dir="ltr"></output>؛ الخطأ المعياري: <output id="esa-welch-se" dir="ltr"></output>؛ درجات حرية ويلش: <output id="esa-welch-df" dir="ltr"></output>.</p><p>قيمة t الحرجة: <output id="esa-welch-critical" dir="ltr"></output>؛ هامش الخطأ: <output id="esa-welch-margin" dir="ltr"></output>.</p><p>فترة الثقة: <span dir="ltr">[<output id="esa-welch-lower"></output>, <output id="esa-welch-upper"></output>]</span>.</p></div>
<svg id="esa-welch-chart" role="img" viewBox="0 0 620 135" style="display:block;width:100%;height:auto;direction:ltr" aria-label="رسم توضيحي لفترة ويلش"></svg>
<p class="muted-mini">الافتراضات: مشاهدات مستقلة داخل المجموعتين وبينهما، وتوزيعات معاينة طبيعية تقريبًا لمتوسطي العيّنتين (مجتمعات طبيعية أو شروط مناسبة للعيّنات الكبيرة). هذه ليست فترة للعيّنات الزوجية. والعيّنات الصغيرة جدًا أو شديدة الالتواء تتطلب حذرًا خاصًا، وإذا كان التباين صفرًا في المجموعتين تكون الفترة غير معرّفة. النتائج تطابق الدالة <code dir="ltr">ttest_ind_from_stats</code> في SciPy مع <code dir="ltr">equal_var=False</code>.</p>
</section><script defer src="/js/welch-ci-explorer.js"></script>

<h2>1. السؤال البحثي</h2>
<p>بدل تقدير متوسط مجتمع واحد نقارن الآن متوسطي مجتمعين، مثل: متوسط درجات طلاب طريقة تدريس A مقابل طريقة B، أو متوسط ضغط الدم في مجموعتي العلاج والضبط، أو متوسط الدخل في منطقتين. والهدف تقدير مقدار اختلاف المتوسطين.</p>

<h2>2. المعلمة والمقدِّر</h2>
<p>ليكن \(\mu_1\) متوسط المجتمع في المجموعة 1 و\(\mu_2\) متوسطه في المجموعة 2. المعلمة المطلوبة:</p>
<div dir="ltr">\[\Delta=\mu_1-\mu_2,\qquad \widehat{\Delta}=\bar X_1-\bar X_2.\]</div>

<h2>3. تفسير الفرق</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">الفرق</th><th scope="col">التفسير</th></tr></thead>
<tbody>
<tr><td>موجب</td><td>متوسط المجموعة 1 أكبر</td></tr>
<tr><td>سالب</td><td>متوسط المجموعة 2 أكبر</td></tr>
<tr><td>صفر</td><td>لا فرق بين المتوسطين</td></tr>
</tbody></table></div>

<h2>4. المخطط والخطأ المعياري للفرق</h2>
<p>تبقى بنية الفترة نفسها (التقدير ± هامش الخطأ)، ويتغير التقدير والخطأ المعياري فقط. وعندما تكون العيّنتان مستقلتين يسهم تباين المجموعتين كلتيهما في عدم اليقين:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="الخطأ المعياري للفرق بين متوسطين">\[\widehat{\operatorname{SE}}(\bar X_1-\bar X_2)=\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}\]</div>
<p>حيث \(s_1,s_2\) الانحرافان المعياريان للعيّنتين، و\(n_1,n_2\) حجماهما.</p>

<h2>5. لماذا تُجمع التباينات؟</h2>
<p>تسهم العيّنتان المستقلتان في عدم اليقين كلٌّ على حدة، وتباين الفرق بين مقدِّرين مستقلين يساوي مجموع تبايناتهما؛ فعدم يقين الفرق يأتي من العيّنتين معًا لا من واحدة فقط.</p>

<h2>6. صيغة فترة ويلش</h2>
<p>فترة t لويلش، التي لا تتطلب تساوي تبايني المجتمعين، هي:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="فترة ويلش">\[(\bar X_1-\bar X_2)\pm t_{1-\alpha/2,\,\widehat{\nu}}\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}\]</div>
<p>حيث \(\widehat{\nu}\) درجات حرية ويلش–ساترثويت:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="درجات حرية ويلش–ساترثويت">\[\widehat{\nu}=\frac{\left(s_1^2/n_1+s_2^2/n_2\right)^2}{\dfrac{(s_1^2/n_1)^2}{n_1-1}+\dfrac{(s_2^2/n_2)^2}{n_2-1}}\]</div>

<h2>7. مثال محسوب</h2>
<p>لنفترض أن باحثين قارنوا طريقتي تدريس: متوسط المجموعة 1 = 82، ومتوسط المجموعة 2 = 76، و<span dir="ltr">s₁ = 10, s₂ = 12, n₁ = 40, n₂ = 35</span>.</p>
<h3>الخطوة 1: الفرق المقدَّر</h3>
<div dir="ltr">\[\bar x_1-\bar x_2=82-76=6.\]</div>
<h3>الخطوة 2: الخطأ المعياري</h3>
<div dir="ltr">\[\widehat{\operatorname{SE}}=\sqrt{\frac{10^2}{40}+\frac{12^2}{35}}\approx2.5718.\]</div>
<h3>الخطوة 3: القيمة الحرجة</h3>
<p>درجات حرية ويلش–ساترثويت هنا نحو <span dir="ltr">66.48</span>، والقيمة الحرجة ثنائية الطرف لـ 95% نحو <span dir="ltr">1.9963</span> (نقرّبها هنا إلى 2 للتوضيح).</p>
<h3>الخطوة 4: هامش الخطأ</h3>
<div dir="ltr">\[\text{ME}\approx1.9963\times2.5718\approx5.13.\]</div>
<h3>الخطوة 5: بناء الفترة</h3>
<div dir="ltr">\[6\pm5.13\approx(0.87,\,11.13).\]</div>
<p>وبالتقريب إلى <span dir="ltr">t* ≈ 2</span> نحصل على <span dir="ltr">(0.86, 11.14)</span>؛ والفرق في المنزلة الثانية فقط. والقيمة الاحتمالية لاختبار ويلش المقابل <span dir="ltr">p ≈ 0.0227</span>، بما يتسق مع استبعاد الفترة للصفر.</p>

<h2>8. تفسير الفترة</h2>
<p>تشير الفترة إلى أن القيم المعقولة لـ \(\mu_1-\mu_2\) تقع بين نحو 0.87 و11.13؛ أي إن البيانات توحي بأن المجموعة 1 قد تتفوق على المجموعة 2 بما بين نقطة واحدة و11 نقطة تقريبًا.</p>

<h2>9. أهمية الصفر</h2>
<div class="concept-box"><strong>الفرق الصفري:</strong><p>فرق قدره صفر يعني أن متوسطي المجتمعين متساويان.</p></div>
<ul class="bullets"><li>الصفر غير موجود في <span dir="ltr">(0.87, 11.13)</span>، فالبيانات تقدّم دليلًا على اختلاف المتوسطين.</li><li>لو كانت الفترة <span dir="ltr">(−3, 8)</span> لكان الصفر داخلها، فيبقى تساوي المتوسطين معقولًا، ولا يوجد دليل قوي على الفرق.</li></ul>

<h2>10. شروط الفترة</h2>
<ul class="bullets"><li>معاينة عشوائية أو تعيين عشوائي.</li><li>استقلال داخل كل عيّنة.</li><li>استقلال بين المجموعتين.</li><li>توزيعات معاينة طبيعية تقريبًا (انظر <a href="/ar/inference/confidence-intervals/conditions-normality-clt-independence/">الشروط</a>).</li></ul>
<p>وتساعد مبرهنة النهاية المركزية غالبًا على تبرير التقريب الطبيعي عندما تكون أحجام العيّنات كبيرة بما يكفي.</p>

<h2>11. العيّنات المستقلة مقابل الزوجية</h2>
<p>يفترض هذا الدرس أن العيّنتين مستقلتان، كطلاب مختلفين في صفّين أو مرضى مختلفين في مجموعتي العلاج والضبط. أما القياسات الزوجية فتتطلب طرقًا مختلفة تأخذ بنية المطابقة في الحسبان، لأن الارتباط داخل الأزواج يؤثر في الدقة.</p>

<h2>12. أين تُستخدم هذه الفترات؟</h2>
<p>في التجارب السريرية، والدراسات التربوية، وتجارب الأعمال، ومقارنات التصنيع، وبحوث العلوم الاجتماعية؛ فمقارنة متوسطات المجموعات من أكثر مهام الاستدلال شيوعًا.</p>
<div class="concept-box"><strong>الرسالة الأساسية:</strong><p>تقدّر فترات الثقة للفرق بين متوسطين مستقلين مقدار تباعد متوسطي المجتمعين مع أخذ عدم اليقين من العيّنتين في الحسبان.</p></div>

<h2>13. ماذا بعد؟</h2>
<p>يقارن الباحثون النسب المئوية أيضًا، كما في الاستطلاعات والدراسات الطبية واختبارات A/B. ويطوّر الدرس التالي فترات الثقة للفرق بين نسبتي مجتمعين.</p>

<div class="summary-box">
<h2>خلاصة الدرس</h2>
<ul class="bullets">
<li>المعلمة المطلوبة \(\mu_1-\mu_2\).</li>
<li>المقدِّر \(\bar x_1-\bar x_2\).</li>
<li>عدم اليقين يأتي من العيّنتين.</li>
<li>يجمع الخطأ المعياري تباين المجموعتين.</li>
<li>تستخدم فترة ويلش قيمة t بدرجات حرية ساترثويت.</li>
<li>الصفر يمثّل عدم وجود فرق بين المتوسطين.</li>
<li>إذا كان الصفر خارج الفترة فالبيانات توحي بفرق حقيقي.</li>
<li>تُستخدم هذه الفترات على نطاق واسع لمقارنة المجموعات.</li>
</ul>
</div>

<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/inference/confidence-intervals/ci-for-proportion/">→ السابق: فترة الثقة للنسبة</a>
<a class="btn" href="/ar/inference/confidence-intervals/ci-for-difference-of-proportions/">التالي: فترة الثقة للفرق بين نسبتين ←</a>
</div>
</div></section>
