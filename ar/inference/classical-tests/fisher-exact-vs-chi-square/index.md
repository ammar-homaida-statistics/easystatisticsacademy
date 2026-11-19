---
layout: default
title: اختبار فيشر الدقيق مقابل كاي تربيع لبيرسون في جداول 2×2
description: "شرح عربي لاختبار فيشر الدقيق واختبار كاي تربيع لبيرسون وتصحيح ييتس في جداول التوافق 2×2، مع مختبر تفاعلي يقبل الخلايا الصفرية."
permalink: /ar/inference/classical-tests/fisher-exact-vs-chi-square/
lang: ar
sidebar: false
math: true
learning_resource: true
translation_pair: fisher-exact
---
<section class="hero hero-section"><div class="hero-card">
<h1>اختبار فيشر الدقيق مقابل كاي تربيع لبيرسون</h1>
<p class="lead">لماذا يمكن أن يعطي إجراءان إحصائيان صحيحان قيمتين احتماليتين مختلفتين لجدول التوافق 2×2 نفسه؟</p>
<p><a href="/inference/classical-tests/fisher-exact-vs-chi-square/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/classical-tests/chi-square-independence-test/">درس اختبار كاي تربيع للاستقلال</a> · <a href="/ar/inference/classical-tests/">الاختبارات الكلاسيكية</a></p>
</div></section>
<section><div class="content-narrow">
<h2>1. مقاربتان لاختبار الارتباط في جدول 2×2</h2>
<p>تحت فرضية عدم وجود ارتباط، يقارن <strong>اختبار χ² لبيرسون</strong> التكرارات المشاهدة بالمتوقعة، ويستخدم توزيعًا مرجعيًا تقاربيًا بدرجة حرية واحدة. أما <strong>اختبار فيشر الدقيق</strong> فيشترط على مجاميع الصفوف والأعمدة المشاهدة، ويقيّم الجداول الممكنة باستخدام التوزيع فوق الهندسي. لا يتطلب حساب فيشر الدقيق تكرارات متوقعة كبيرة، وإن كان كلا الإجراءين يعتمد على نموذج معاينة مناسب وعلى الاستقلال.</p>
<div class="esa-fc-equation" dir="ltr" tabindex="0" role="region" aria-label="معادلة كاي تربيع لبيرسون">
\[
\chi^2=\sum_{i=1}^{2}\sum_{j=1}^{2}\frac{(O_{ij}-E_{ij})^2}{E_{ij}},
\quad E_{ij}=\frac{(\mathrm{row\ total})_i(\mathrm{column\ total})_j}{N}.
\]
</div>
<h2>2. التوزيع فوق الهندسي الشرطي</h2>
<p>إذا ثُبّتت المجاميع الهامشية، يحدد عدد الخلية العلوية اليسرى \(a\) الجدول كله. وتحت فرضية الاستقلال يكون احتماله:</p>
<div class="esa-fc-equation" dir="ltr" tabindex="0" role="region" aria-label="الاحتمال فوق الهندسي">
\[
P(a)=\frac{\binom{a+c}{a}\binom{b+d}{b}}{\binom{N}{a+b}} .
\]
</div>
<h2>3. اصطلاح القيمة الاحتمالية الدقيقة</h2>
<p>تستخدم <strong>القيمة الاحتمالية الثنائية لفيشر</strong> ترتيب الاحتمالات: نجمع الاحتمالات الشرطية لجميع الجداول ذات المجاميع الهامشية الثابتة التي لا يزيد احتمالها على احتمال الجدول المشاهد، كما في الاصطلاح الافتراضي لدالة <code dir="ltr">fisher_exact</code> في SciPy. وهي ليست عمومًا ضعف أصغر قيمة أحادية الطرف. وتُعرَّف البدائل بدلالة عدد الخلية العلوية اليسرى: «أكبر» تعني ارتباطًا موجبًا (نسبة أرجحية أكبر من 1)، و«أصغر» تعني ارتباطًا سالبًا.</p>
<h2>4. مختبر فيشر–بيرسون التفاعلي</h2>
<section id="esa-fisher-chi-lab" class="concept-box" data-locale="ar" aria-labelledby="esa-fc-heading">
<h3 id="esa-fc-heading">أدخل التكرارات المشاهدة</h3>
{% include lab-noscript.html %}
<p>أعداد صحيحة غير سالبة؛ يجب أن يكون مجموع كل صف وكل عمود موجبًا، والحجم الكلي N ≤ 2,000 ليبقى الحساب الدقيق سريعًا. الجدول الافتراضي هو 1، 9، 11، 3.</p>
<div class="esa-fc-grid">
<label for="esa-fc-a">الصف 1، العمود 1<input id="esa-fc-a" dir="ltr" type="number" min="0" max="2000" step="1" value="1" aria-invalid="false" aria-describedby="esa-fc-error"></label>
<label for="esa-fc-b">الصف 1، العمود 2<input id="esa-fc-b" dir="ltr" type="number" min="0" max="2000" step="1" value="9" aria-invalid="false" aria-describedby="esa-fc-error"></label>
<label for="esa-fc-c">الصف 2، العمود 1<input id="esa-fc-c" dir="ltr" type="number" min="0" max="2000" step="1" value="11" aria-invalid="false" aria-describedby="esa-fc-error"></label>
<label for="esa-fc-d">الصف 2، العمود 2<input id="esa-fc-d" dir="ltr" type="number" min="0" max="2000" step="1" value="3" aria-invalid="false" aria-describedby="esa-fc-error"></label>
<label for="esa-fc-side">الفرضية البديلة لفيشر<select id="esa-fc-side"><option value="two-sided">ثنائية الطرف</option><option value="greater">نسبة أرجحية أكبر</option><option value="less">نسبة أرجحية أصغر</option></select></label>
</div>
<button id="esa-fc-reset" class="btn btn-outline" type="button">إعادة المثال</button>
<p id="esa-fc-error" role="alert" hidden></p>
<div id="esa-fc-results" aria-live="polite" aria-atomic="true">
<p>عدد المشاهدات: <output id="esa-fc-N" dir="ltr"></output> · χ² لبيرسون: <output id="esa-fc-chi" dir="ltr"></output>.</p>
<div class="table-wrap"><table><caption>التكرارات المتوقعة تحت الاستقلال</caption><thead><tr><th scope="col">الصف</th><th scope="col">العمود 1</th><th scope="col">العمود 2</th></tr></thead><tbody>
<tr><th scope="row">الصف 1</th><td><output id="esa-fc-aexpected" dir="ltr"></output></td><td><output id="esa-fc-bexpected" dir="ltr"></output></td></tr>
<tr><th scope="row">الصف 2</th><td><output id="esa-fc-cexpected" dir="ltr"></output></td><td><output id="esa-fc-dexpected" dir="ltr"></output></td></tr>
</tbody></table></div>
<div class="table-wrap"><table><caption>الاستدلال الإحصائي</caption><thead><tr><th scope="col">الطريقة</th><th scope="col">القيمة الاحتمالية</th></tr></thead><tbody>
<tr><th scope="row">فيشر الدقيق (البديل المختار)</th><td><output id="esa-fc-fisher" dir="ltr"></output></td></tr>
<tr><th scope="row">χ² لبيرسون (ارتباط ثنائي الطرف، تقاربي)</th><td><output id="esa-fc-pearson" dir="ltr"></output></td></tr>
<tr><th scope="row">χ² لبيرسون مع تصحيح ييتس للاستمرارية</th><td><output id="esa-fc-yates" dir="ltr"></output></td></tr>
</tbody></table></div>
<svg id="esa-fc-plot" viewBox="0 0 620 125" role="img" dir="ltr" aria-label="القيمتان الاحتماليتان لفيشر وبيرسون" style="display:block;max-width:100%;width:100%;height:auto"></svg>
<p id="esa-fc-warning" role="status"></p><p id="esa-fc-meaning"></p>
</div></section>
<h2>5. التفسير والحدود</h2>
<p>للجدول المثال، القيم المرجعية المستقلة من SciPy هي: قيمة فيشر الثنائية ≈ 0.00275946، وإحصائية بيرسون χ² ≈ 10.971429، وقيمة بيرسون الاحتمالية ≈ 0.00092527، ومع تصحيح ييتس ≈ 0.00375221. لا يُشترط أن تتفق الطريقتان في القيمة الاحتمالية الدقيقة؛ فقد يكون تقريب بيرسون غير موثوق عندما تكون التكرارات المتوقعة صغيرة. وتغيير بديل فيشر إلى بديل أحادي الطرف <em>لا</em> يغيّر نتيجة بيرسون الثنائية؛ إذ يجيب الاختباران حينئذ عن سؤالين مختلفي الاتجاه، فلا يُعامَلان على أنهما متكافئان.</p>
<p>تُقبل الخلايا المشاهدة الصفرية ما دامت المجاميع الهامشية موجبة. أما صف أو عمود مجموعه صفر فيجعل حساب الارتباط المعتاد في جدول 2×2 غير معرّف. ولا تثبت أيّ الطريقتين السببية، وتبقى افتراضات الاستقلال والمعاينة حاسمة.</p>
<h2>6. تصحيح ييتس للاستمرارية</h2>
<p>يُنقص تصحيح ييتس كل \(|O_{ij}-E_{ij}|\) بمقدار \(\min(0.5,\,|O_{ij}-E_{ij}|)\) قبل التربيع، فيقرّب القيمة الاحتمالية لبيرسون من قيمة فيشر. لكنه محافظ غالبًا: ففي الجدول المثال تكون القيمة المصححة (0.00375) أكبر من قيمة فيشر الدقيقة الثنائية (0.00276). ويفضّل كثير من الإحصائيين اليوم الاختبار الدقيق، أو χ² دون تصحيح عندما تكون التكرارات المتوقعة كافية، على الاختبار المصحح؛ وأيًّا كان المستخدم فينبغي ذكره.</p>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets">
<li>يقيس اختبارا فيشر وبيرسون الارتباط في جدول 2×2 بطريقتين مختلفتين.</li>
<li>فيشر دقيق شرطيًا ولا يحتاج إلى تكرارات متوقعة كبيرة.</li>
<li>بيرسون تقاربي، وقد يكون غير موثوق مع تكرارات متوقعة أقل من 5.</li>
<li>القيمة الثنائية لفيشر تُبنى على ترتيب الاحتمالات، لا على مضاعفة طرف واحد.</li>
<li>تصحيح ييتس يقرّب بيرسون من فيشر لكنه محافظ غالبًا.</li>
</ul></div>
</div></section>
<style>
#esa-fisher-chi-lab{box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere}
#esa-fisher-chi-lab .esa-fc-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:14px 0}
#esa-fisher-chi-lab label{display:block;font-weight:600;min-width:0}
#esa-fisher-chi-lab :is(input,select){display:block;box-sizing:border-box;width:100%;max-width:100%;min-width:0;padding:9px;font:inherit;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text)}
#esa-fisher-chi-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-fisher-chi-lab [hidden]{display:none!important}
#esa-fisher-chi-lab :is(input,select,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-fc-equation{max-width:100%;overflow-x:auto;padding:8px 0}
@media(max-width:650px){#esa-fisher-chi-lab .esa-fc-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/fisher-chi-square-2x2.js"></script>
