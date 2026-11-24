---
layout: default
title: البدائل الحصينة والطرق اللامعلمية
description: "شرح عربي للطرق الحصينة واللامعلمية: الوسيط والمتوسط المشذّب، واختبارات الرتب (مان–ويتني وويلكوكسون وكروسكال–واليس) مع مختبرين تفاعليين، ومتى نستخدم هذه البدائل."
permalink: /ar/inference/assumptions-robustness/robust-alternatives-nonparametric/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: robust-alternatives
---
<section class="hero hero-section"><div class="hero-card">
<div class="badge-row"><span class="badge">الاستدلال</span><span class="badge">الافتراضات والحصانة</span><span class="badge">الطرق الحصينة</span></div>
<h1>البدائل الحصينة والطرق اللامعلمية</h1>
{% include lab-noscript.html %}
<p class="lead">تعمل الإجراءات الإحصائية الكلاسيكية جيدًا في حالات كثيرة، لكنها تعتمد على افتراضات قد لا تتحقق دائمًا في التطبيق.</p>
<p class="lead">وتوفّر الطرق الحصينة (Robust) واللامعلمية (Nonparametric) بدائل مفيدة عندما تحتوي البيانات على قيم متطرفة أو التواء أو تباينات غير متساوية أو انتهاكات أخرى للافتراضات.</p>
<p><a href="/inference/assumptions-robustness/robust-alternatives-nonparametric/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/assumptions-robustness/bootstrap-as-robust-tool/">الدرس التالي: بوتستراب أداة حصينة</a></p>
</div></section>
<section><div class="content-narrow">

<h2>1. لماذا نحتاج إلى بدائل؟</h2>
<p>تفترض طرق كلاسيكية كثيرة ما يلي:</p>
<ul class="bullets"><li>التوزيع الطبيعي</li><li>تساوي التباينات</li><li>غياب القيم المتطرفة الشديدة</li><li>نموذجًا احتماليًا محددًا</li></ul>
<p>وعندما تصبح هذه الافتراضات موضع شك، قد يبحث المحلل عن إجراءات أقل حساسية لانتهاكها.</p>
<div class="concept-box"><strong>الفكرة الرئيسة:</strong><p>تسعى الطرق الحصينة واللامعلمية إلى تقديم استنتاجات موثوقة حتى عندما لا تتحقق الافتراضات الكلاسيكية تحققًا تامًا.</p></div>

<h2>2. ما الذي يجعل الطريقة حصينة؟</h2>
<p>الطريقة الحصينة هي التي يبقى أداؤها مقبولًا عندما تتحقق الافتراضات تحققًا تقريبيًا فقط. وتتأثر الطرق الحصينة عادةً بدرجة أقل بما يلي:</p>
<ul class="bullets"><li>القيم المتطرفة</li><li>التوزيعات الملتوية</li><li>عدم تجانس التباين الخفيف</li><li>الانحرافات الصغيرة عن النماذج النظرية</li></ul>
<p>والحصانة مسألة درجة، وليست خاصية إما أن توجد كاملة أو تغيب كليًا.</p>

<h2>3. ما الطرق اللامعلمية؟</h2>
<div class="concept-box"><strong>تعريف:</strong><p>الطرق اللامعلمية إجراءات تضع افتراضات أقل حول الشكل الدقيق لتوزيع المجتمع.</p></div>
<p>وتكون مفيدة غالبًا عندما يكون شكل التوزيع الأساسي مجهولًا أو يصعب تبريره. ولا يعني «لامعلمي» غياب الافتراضات كليًا؛ فاختبارات الرتب مثلًا ما زالت تفترض استقلال المشاهدات.</p>

<h2>4. المعلمية مقابل اللامعلمية</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">الخاصية</th><th scope="col">الطرق المعلمية</th><th scope="col">الطرق اللامعلمية</th></tr></thead>
<tbody>
<tr><td>افتراضات التوزيع</td><td>أقوى</td><td>أضعف</td></tr>
<tr><td>الكفاءة في الظروف المثالية</td><td>أعلى غالبًا</td><td>أقل غالبًا</td></tr>
<tr><td>الحصانة</td><td>أقل عادةً</td><td>أعلى عادةً</td></tr>
</tbody></table></div>
<p>ولكل منهجين نقاط قوة وحدود.</p>

<h2>5. موازنة شائعة</h2>
<p>تستخلص الطرق المعلمية معلومات أكثر غالبًا عندما تكون الافتراضات صحيحة، بينما تتنازل الطرق اللامعلمية عن شيء من الكفاءة مقابل مرونة وحصانة أكبر.</p>

<h2>6. المتوسط مقابل الوسيط</h2>
<p>من أبسط الأمثلة مقاييس النزعة المركزية:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">الإحصاءة</th><th scope="col">الحساسية للقيم المتطرفة</th></tr></thead>
<tbody><tr><td>المتوسط</td><td>عالية</td></tr><tr><td>الوسيط</td><td>منخفضة</td></tr></tbody></table></div>
<p>لذلك يُعدّ الوسيط غالبًا مقياسًا أكثر حصانة للنزعة المركزية.</p>

<h2>7. المتوسطات المشذّبة</h2>
<p>من البدائل الحصينة الأخرى المتوسط المشذّب (Trimmed mean)، وهو يحذف نسبة صغيرة من أكبر المشاهدات وأصغرها قبل حساب المتوسط؛ فيقلّ تأثّره بالقيم المتطرفة.</p>

<h2>8. الطرق القائمة على الرتب</h2>
<p>تستخدم إجراءات لامعلمية كثيرة الرتب بدل القيم العددية الأصلية. ويقلّل الترتيب تأثير المشاهدات المتطرفة لأنه لا يستعمل إلا الترتيب النسبي للقيم.</p>

<h2>9. اختبار مان–ويتني</h2>
<p>من البدائل الشائعة لاختبار <a href="/ar/inference/classical-tests/two-sample-t-test-independent/">t لعيّنتين مستقلتين</a>:</p>
<div class="example-box"><p>اختبار مان–ويتني U (Mann–Whitney U)</p></div>
<p>يقارن هذا الإجراء المجموعات باستخدام الرتب بدل الاعتماد المباشر على المتوسطات والانحرافات المعيارية.</p>

<h2>10. اختبار ويلكوكسون للرتب ذات الإشارة</h2>
<p>وللبيانات المزدوجة، من البدائل الشائعة لاختبار <a href="/ar/inference/classical-tests/paired-t-test/">t للأزواج</a>:</p>
<div class="example-box"><p>اختبار ويلكوكسون للرتب ذات الإشارة (Wilcoxon signed-rank)</p></div>
<p>ويفيد هذا الاختبار عندما تكون افتراضات اختبار t للأزواج موضع شك.</p>

<!-- مختبر مان–ويتني وويلكوكسون (Batch #100، النسخة العربية) -->
<section class="concept-box" id="esa-rt-lab" data-locale="ar" aria-labelledby="esa-rt-heading">
  <h3 id="esa-rt-heading">مختبر تفاعلي لاختبارات الرتب: مان–ويتني وويلكوكسون</h3>
  <p>في عيّنتين مستقلتين تكون إحصاءة <strong>مان–ويتني</strong> هي \(U_1=R_1-n_1(n_1+1)/2\)، حيث \(R_1\) مجموع رتب العيّنة الأولى في البيانات المدمجة. وفي البيانات المزدوجة تكون إحصاءة <strong>ويلكوكسون للرتب ذات الإشارة</strong> \(T^+\) هي مجموع رتب \(|d_i|\) للفروق الموجبة \(d_i=x_i-y_i\)، مع حذف الفروق الصفرية.</p>
  <div class="esa-rt-math" dir="ltr" tabindex="0" role="region" aria-label="التقريبان الطبيعيان لاختباري الرتب">
  \[
  z_U=\frac{U_1-\tfrac{n_1n_2}{2}\mp\tfrac12}{\sqrt{\tfrac{n_1n_2}{12}\left[(N+1)-\tfrac{\sum(t^3-t)}{N(N-1)}\right]}},\qquad
  z_T=\frac{T^+-\tfrac{n(n+1)}{4}}{\sqrt{\tfrac{n(n+1)(2n+1)-\sum(t^3-t)/2}{24}}}.
  \]
  </div>
  <p>تُحسب القيم الاحتمالية الدقيقة من توزيعات العدم الدقيقة عندما لا توجد قيم متساوية (ولا فروق صفرية في اختبار ويلكوكسون). وتطابق الاصطلاحات دالتي <code>mannwhitneyu</code> (مع تصحيح الاستمرارية) و<code>wilcoxon</code> (من دونه) في SciPy.</p>
  <div class="esa-rt-grid">
    <label for="esa-rt-test">الاختبار<select id="esa-rt-test"><option value="mann-whitney" selected>مان–ويتني U (عيّنتان مستقلتان)</option><option value="wilcoxon">ويلكوكسون للرتب ذات الإشارة (عيّنتان مزدوجتان)</option></select></label>
    <label for="esa-rt-side">الفرضية البديلة<select id="esa-rt-side"><option value="two-sided" selected>ثنائية الطرف</option><option value="greater">قيم العيّنة 1 تميل إلى أن تكون أكبر</option><option value="less">قيم العيّنة 1 تميل إلى أن تكون أصغر</option></select></label>
  </div>
  <label for="esa-rt-x">العيّنة 1 (قيم مفصولة بفواصل)</label>
  <textarea id="esa-rt-x" dir="ltr" rows="2" spellcheck="false" aria-invalid="false" aria-describedby="esa-rt-error">12.1, 14.3, 11.8, 15.2, 13.9, 12.7</textarea>
  <label for="esa-rt-y">العيّنة 2 (قيم مفصولة بفواصل)</label>
  <textarea id="esa-rt-y" dir="ltr" rows="2" spellcheck="false" aria-invalid="false" aria-describedby="esa-rt-error">15.8, 16.4, 14.9, 17.2, 18.1</textarea>
  <div class="esa-rt-controls"><button class="btn btn-outline" type="button" id="esa-rt-mw">مثال مان–ويتني</button><button class="btn btn-outline" type="button" id="esa-rt-wx">مثال الأزواج</button><button class="btn btn-outline" type="button" id="esa-rt-ties">مثال مع قيم متساوية</button></div>
  <p id="esa-rt-error" role="alert" hidden></p>
  <section id="esa-rt-results" aria-label="نتائج اختبار الرتب" role="status" aria-live="polite" aria-atomic="true">
    <div class="table-wrap"><table><caption>نتائج اختبار الرتب</caption><tbody id="esa-rt-body">
      <tr id="esa-rt-row-mw"><th scope="row">U₁ · U₂ · إزاحة هودجز–ليمان</th><td dir="ltr"><output id="esa-rt-u1">1</output> · <output id="esa-rt-u2">29</output> · <output id="esa-rt-hl">-3.1000</output></td></tr>
      <tr id="esa-rt-row-wx" hidden><th scope="row">n (غير الصفرية) · الأصفار المحذوفة · T⁺ · T⁻</th><td dir="ltr"><output id="esa-rt-n">—</output> · <output id="esa-rt-zeros">—</output> · <output id="esa-rt-tplus">—</output> · <output id="esa-rt-tminus">—</output></td></tr>
      <tr><th scope="row">z للتقريب الطبيعي</th><td><output id="esa-rt-z" dir="ltr">-2.4648</output></td></tr>
      <tr><th scope="row">القيمة الاحتمالية بالتقريب الطبيعي</th><td><output id="esa-rt-papprox" dir="ltr">0.013711</output></td></tr>
      <tr><th scope="row">القيمة الاحتمالية الدقيقة</th><td><output id="esa-rt-pexact" dir="ltr">0.008658</output></td></tr>
      <tr><th scope="row">معامل ارتباط الرتب الثنائي r</th><td><output id="esa-rt-r" dir="ltr">-0.9333</output></td></tr>
    </tbody></table></div>
    <p id="esa-rt-note"></p>
  </section>
  <p class="muted-mini">يتراوح معامل ارتباط الرتب الثنائي بين −1 و1؛ وفي اختبار مان–ويتني يساوي \(r=2U_1/(n_1n_2)-1\)، أي احتمال أن تتجاوز قيمة من العيّنة 1 قيمة من العيّنة 2 مطروحًا منه الاحتمال المعاكس. وإزاحة هودجز–ليمان هي وسيط جميع الفروق الثنائية \(x_i-y_j\). ويدل اختبار مان–ويتني الدال على أن أحد التوزيعين يميل إلى إعطاء قيم أكبر؛ ولا يكون اختبارًا للوسيطين إلا إذا تماثل شكلا التوزيعين.</p>
</section>
<style>
#esa-rt-lab,#esa-rt-lab *{box-sizing:border-box}
#esa-rt-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-rt-lab label{display:block;font-weight:650;margin:10px 0 5px}
#esa-rt-lab :is(textarea,select){display:block;width:100%;min-width:0;font:inherit;padding:8px;border:1px solid #777;border-radius:6px}
#esa-rt-lab .esa-rt-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr));gap:8px}
#esa-rt-lab .esa-rt-controls{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
#esa-rt-lab .table-wrap,.esa-rt-math{max-width:100%;overflow-x:auto}
.esa-rt-math{direction:ltr}
#esa-rt-lab [hidden]{display:none!important}
#esa-rt-lab :is(textarea,select,button):focus-visible,.esa-rt-math:focus-visible{outline:2px solid #0f766e;outline-offset:3px}
</style>
<script defer src="/js/rank-tests-lab.js"></script>

<h2>11. اختبار كروسكال–واليس</h2>
<p>ولمقارنة أكثر من مجموعتين، يُعدّ اختبار كروسكال–واليس (Kruskal–Wallis) بديلًا لامعلميًا لتحليل <a href="/ar/inference/classical-tests/one-way-anova-f-test/">التباين الأحادي</a>:</p>
<div class="example-box"><p>اختبار كروسكال–واليس</p></div>
<p>ويقيّم هذا الإجراء الفروق بين المجموعات باستخدام الرتب.</p>

<!-- مختبر كروسكال–واليس (Batch #100، النسخة العربية) -->
<section class="concept-box" id="esa-kw-lab" data-locale="ar" aria-labelledby="esa-kw-heading">
  <h3 id="esa-kw-heading">مختبر كروسكال–واليس التفاعلي</h3>
  <p>تُرتَّب المشاهدات الـ \(N\) كلها معًا (وتأخذ القيم المتساوية متوسط رتبها). إذا كان \(R_i\) مجموع الرتب و\(n_i\) الحجم في المجموعة \(i\) فإن:</p>
  <div class="esa-kw-math" dir="ltr" tabindex="0" role="region" aria-label="إحصاءة كروسكال–واليس">
  \[
  H=\frac{12}{N(N+1)}\sum_{i=1}^{k}\frac{R_i^2}{n_i}-3(N+1),\qquad
  H_c=\frac{H}{1-\sum_t (t^3-t)/(N^3-N)},\qquad
  \varepsilon^2=\frac{H_c}{N-1}.
  \]
  </div>
  <p>تحت فرضية العدم القائلة إن جميع المجموعات مأخوذة من التوزيع المتصل نفسه، تتوزع \(H_c\) تقريبيًا وفق \(\chi^2_{k-1}\). ويعرض المختبر أيضًا قيمة احتمالية بالتبديل بطريقة مونت كارلو من 10,000 إعادة توزيع عشوائية للرتب المدمجة (ببذرة ثابتة، فالنتائج قابلة لإعادة الإنتاج)، مع خطئها المعياري.</p>
  <label for="esa-kw-input">المجموعات (مجموعة في كل سطر، من 2 إلى 6 مجموعات)</label>
  <textarea id="esa-kw-input" dir="ltr" rows="4" spellcheck="false" aria-invalid="false" aria-describedby="esa-kw-error">2.1, 3.4, 1.9, 5.6, 2.8
4.2, 6.1, 5.5, 7.3, 4.9
8.8, 6.7, 9.4, 7.9, 12.5</textarea>
  <div class="esa-kw-controls"><button class="btn btn-outline" type="button" id="esa-kw-example">مثال</button><button class="btn btn-outline" type="button" id="esa-kw-ties">قيم متساوية كثيرة</button><button class="btn btn-outline" type="button" id="esa-kw-small">مجموعات صغيرة</button></div>
  <p id="esa-kw-error" role="alert" hidden></p>
  <section id="esa-kw-results" aria-label="نتائج كروسكال–واليس" role="status" aria-live="polite" aria-atomic="true">
    <div class="table-wrap"><table><caption>الرتب حسب المجموعة</caption>
      <thead><tr><th scope="col">المجموعة</th><th scope="col">n</th><th scope="col">مجموع الرتب</th><th scope="col">متوسط الرتب</th></tr></thead>
      <tbody id="esa-kw-rows" dir="ltr"></tbody></table></div>
    <div class="table-wrap"><table><caption>اختبار كروسكال–واليس</caption><tbody>
      <tr><th scope="row">عدد المجموعات k · المشاهدات N · درجات الحرية</th><td dir="ltr"><output id="esa-kw-k">3</output> · <output id="esa-kw-N">15</output> · <output id="esa-kw-df">2</output></td></tr>
      <tr><th scope="row">H (من دون تصحيح التساوي)</th><td><output id="esa-kw-h" dir="ltr">10.6400</output></td></tr>
      <tr><th scope="row">عامل تصحيح التساوي C</th><td><output id="esa-kw-c" dir="ltr">1.000000</output></td></tr>
      <tr><th scope="row">H<sub>c</sub> = H / C</th><td><output id="esa-kw-hc" dir="ltr">10.6400</output></td></tr>
      <tr><th scope="row">القيمة الاحتمالية بتقريب χ²</th><td><output id="esa-kw-p" dir="ltr">0.004893</output></td></tr>
      <tr><th scope="row">القيمة الاحتمالية بالتبديل ± خطأ مونت كارلو المعياري</th><td><output id="esa-kw-pperm" dir="ltr">0.000300 ± 0.0002</output></td></tr>
      <tr><th scope="row">حجم الأثر ε²</th><td><output id="esa-kw-eps" dir="ltr">0.7600</output></td></tr>
    </tbody></table></div>
    <p id="esa-kw-note"></p>
    <p id="esa-kw-decision"></p>
  </section>
  <p class="muted-mini">في البيانات الافتراضية تساوي القيمة الاحتمالية الدقيقة بالتبديل، المحسوبة من جميع إعادات التوزيع البالغة 756,756، القيمة 0.00027؛ لذا فتقريب χ² (0.0049) محافظ في هذا الذيل البعيد حتى مع خمس مشاهدات في كل مجموعة. وتعني النتيجة الدالة أن مجموعة واحدة على الأقل تميل إلى إعطاء قيم أكبر من مجموعة أخرى؛ ومن دون افتراضات إضافية مثل تماثل الأشكال فهي ليست اختبارًا لتساوي الوسيطات. وتحتاج المقارنات الثنائية اللاحقة (مثل اختبار دَن) إلى تعديل للمقارنات المتعددة.</p>
</section>
<style>
#esa-kw-lab,#esa-kw-lab *{box-sizing:border-box}
#esa-kw-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-kw-lab label{display:block;font-weight:650;margin:10px 0 5px}
#esa-kw-lab textarea{display:block;width:100%;min-width:0;font:inherit;padding:10px;border:1px solid #777;border-radius:6px}
#esa-kw-lab .esa-kw-controls{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0}
#esa-kw-lab .table-wrap,.esa-kw-math{max-width:100%;overflow-x:auto}
.esa-kw-math{direction:ltr}
#esa-kw-lab [hidden]{display:none!important}
#esa-kw-lab :is(textarea,button):focus-visible,.esa-kw-math:focus-visible{outline:2px solid #0f766e;outline-offset:3px}
</style>
<script defer src="/js/kruskal-wallis-lab.js"></script>

<h2>12. الانحدار الحصين</h2>
<p>يمكن أيضًا تعديل طرق الانحدار لتقليل حساسيتها للمشاهدات غير المعتادة؛ إذ تقلّل إجراءات الانحدار الحصين تأثير النقاط المتطرفة في العلاقات المقدّرة.</p>

<h2>13. مزايا الطرق اللامعلمية</h2>
<ul class="bullets"><li>افتراضات أقل حول التوزيع</li><li>مقاومة أكبر للقيم المتطرفة</li><li>مناسبة للبيانات الملتوية</li><li>قابلة للتطبيق عندما تكون مقاييس القياس محدودة (مثل البيانات الترتيبية)</li></ul>
<p>وتجعل هذه المزايا الطرق اللامعلمية قيّمة في كثير من المواقف العملية.</p>

<h2>14. حدود الطرق اللامعلمية</h2>
<ul class="bullets"><li>قد تكون قوتها الإحصائية أقل في الظروف المعلمية المثالية</li><li>قد تقدّم معلومات نمذجة أقل تفصيلًا</li><li>قد تجيب عن أسئلة علمية مختلفة قليلًا</li><li>ليست متفوقة تلقائيًا على الطرق المعلمية</li></ul>
<p>ويتطلب اختيار الطريقة فهم أهداف التحليل.</p>

<h2>15. الحصين لا يعني الأفضل</h2>
<p>من المفاهيم الخاطئة الشائعة أن الطرق الحصينة أو اللامعلمية مفضّلة دائمًا. وفي الواقع:</p>
<ul class="bullets"><li>تعمل الطرق الكلاسيكية جيدًا جدًا في حالات كثيرة</li><li>تعالج الطرق الحصينة مشكلات محددة</li><li>يعتمد الاختيار الأفضل على البيانات والأهداف</li></ul>

<h2>16. دور حجم العيّنة</h2>
<p>تقلّل العيّنات الكبيرة غالبًا من القلق بشأن الانتهاكات المعتدلة للافتراضات. فمع زيادة حجم العيّنة:</p>
<ul class="bullets"><li>تصبح الطرق الكلاسيكية أكثر حصانة</li><li>تستقر توزيعات المعاينة</li><li>توفّر مبرهنة النهاية المركزية حماية</li></ul>
<p>وتصبح البدائل الحصينة مفيدة خصوصًا عندما تكون العيّنات صغيرة أو تكون الافتراضات منتهكة انتهاكًا شديدًا.</p>

<h2>17. تحليل الحساسية</h2>
<p>من الاستراتيجيات المفيدة مقارنة الاستنتاجات عبر عدة طرق، مثل:</p>
<ul class="bullets"><li>اختبار t الكلاسيكي</li><li>اختبار t لويلش</li><li>اختبار مان–ويتني</li></ul>
<p>فإذا بقيت الاستنتاجات متقاربة ازدادت الثقة في النتائج.</p>

<h2>18. الحصانة فلسفةً</h2>
<p>ليست الطرق الحصينة مجرد صيغ بديلة؛ بل تعكس فلسفة إحصائية أوسع:</p>
<div class="example-box"><p>ينبغي ألا تعتمد الاستنتاجات اعتمادًا مفرطًا على افتراضات هشّة.</p></div>
<p>وهذه الفكرة محورية في الإحصاء التطبيقي الحديث.</p>

<h2>19. متى ينبغي التفكير في البدائل؟</h2>
<p>تستحق الطرق الحصينة أو اللامعلمية النظر عندما:</p>
<ul class="bullets"><li>توجد قيم متطرفة شديدة</li><li>يوجد التواء قوي</li><li>تكون أحجام العيّنات صغيرة</li><li>تبدو افتراضات التوزيع غير معقولة</li><li>يكشف تحليل الحساسية عن عدم استقرار</li></ul>

<h2>20. الصورة الأشمل</h2>
<p>تختلف الطرق الإحصائية في مدى اعتمادها على الافتراضات، وتوفّر الطرق الحصينة واللامعلمية بدائل قيّمة عندما تصبح الافتراضات موضع شك. وبدل البحث عن طريقة مثلى في كل الأحوال، ينبغي للمحلل أن يقيّم الإجراءات التي تعطي استنتاجات موثوقة للمسألة المطروحة.</p>
<div class="concept-box"><strong>الرسالة الأساسية:</strong><p>تقلّل الطرق الحصينة واللامعلمية الحساسية لانتهاك الافتراضات لأنها تعتمد بدرجة أقل على نماذج توزيعية محددة، وهي بدائل مفيدة عندما يصعب تبرير الافتراضات الكلاسيكية.</p></div>

<h2>21. ماذا بعد؟</h2>
<p>من الأساليب الحديثة القوية أسلوب يتجنب كثيرًا من افتراضات التوزيع التقليدية: طرق بوتستراب، التي تعيد المعاينة من البيانات المرصودة لتقدير عدم اليقين مباشرة. ويقدّم الدرس التالي هذه الطريقة ويشرح لماذا أصبحت من أكثر أدوات الحصانة استخدامًا.</p>

<div class="summary-box">
<h2>خلاصة الدرس</h2>
<ul class="bullets">
<li>الطرق الحصينة أقل حساسية لانتهاك الافتراضات.</li>
<li>الطرق اللامعلمية تضع افتراضات أقل حول التوزيع.</li>
<li>بين الطرق المعلمية واللامعلمية موازنات يجب فهمها.</li>
<li>الوسيط أكثر حصانة للقيم المتطرفة من المتوسط.</li>
<li>تقلّل الإجراءات القائمة على الرتب تأثير المشاهدات المتطرفة.</li>
<li>مان–ويتني وويلكوكسون وكروسكال–واليس اختبارات لامعلمية شائعة.</li>
<li>الطرق الحصينة ليست متفوقة تلقائيًا على الطرق الكلاسيكية.</li>
<li>يعتمد اختيار الطريقة على جودة البيانات والافتراضات والأهداف العلمية.</li>
</ul>
</div>

<div class="lesson-nav">
<a class="btn btn-outline" href="/ar/inference/assumptions-robustness/outliers-and-influence/">→ السابق: القيم المتطرفة والمشاهدات المؤثرة</a>
<a class="btn" href="/ar/inference/assumptions-robustness/bootstrap-as-robust-tool/">التالي: بوتستراب أداة حصينة ←</a>
</div>
</div></section>
