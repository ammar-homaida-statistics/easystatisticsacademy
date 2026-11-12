---
layout: default
title: اختبار t لعينتين مستقلتين — ويلش والتباين المشترك
description: شرح عربي مقارن لاختبار t لعينتين مستقلتين مع اختبار ويلش والتباين المشترك، الافتراضات والقيمة الاحتمالية وفترة الثقة ومختبر تفاعلي.
permalink: /ar/inference/classical-tests/two-sample-t-test-independent/
lang: ar
math: true
sidebar: false
translation_pair: independent-two-sample-t
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<h1>اختبار t لعينتين مستقلتين: ويلش والتباين المشترك</h1>
<p class="lead">نقارن متوسطَي مجتمعين مستقلين باستخدام اختبار ويلش أو الاختبار التقليدي ذي التباين المشترك. اختيار الطريقة يعتمد على الافتراضات وليس على القيمة الاحتمالية وحدها.</p>
<p><a href="/inference/classical-tests/two-sample-t-test-independent/" lang="en" dir="ltr">English: Independent Two-Sample t Test</a></p>
</div></section>
<section class="section"><div class="content-narrow" dir="rtl">
<h2>1. متى نستخدم هذا الاختبار؟</h2>
<p>نستخدم اختبار العينتين المستقلتين عندما تكون مشاهدات المجموعة الأولى مستقلة عن الثانية، وكذلك المشاهدات داخل كل مجموعة وفق تصميم الدراسة. الأمثلة: مجموعتان مختلفتان من الطلاب أو المشاركين في تجربة مضبوطة. أما قياسات الشخص نفسه قبل وبعد التدخل، فتحتاج <a href="/ar/inference/classical-tests/paired-t-test/">اختبار t للعينات المزدوجة</a>.</p>
<h2>2. الفرضيات واتجاه الفرق</h2>
<p>المعلمة محل الاهتمام هي \(\Delta=\mu_1-\mu_2\). تكون الفرضية الصفرية \(H_0:\Delta=\delta_0\)، ويمكن أن تكون البديلة ثنائية الطرف \(\Delta\ne\delta_0\)، أو أحادية الطرف أكبر/أصغر حسب سؤال البحث المحدد مسبقاً. تفسير الإشارة دائماً حسب «المجموعة أ − المجموعة ب».</p>
<h2>3. اختبار ويلش (Welch)</h2>
<p>لا يفترض ويلش تساوي التباينين السكانيين، لذلك يكون خياراً افتراضياً مناسباً لكثير من المقارنات المستقلة.</p>
<div dir="ltr" role="region" tabindex="0" class="esa-t89-equation" aria-label="معادلات اختبار ويلش">
\[
 t_W=\frac{\bar x_1-\bar x_2-\delta_0}{\sqrt{s_1^2/n_1+s_2^2/n_2}},\quad
 \nu_W=\frac{(s_1^2/n_1+s_2^2/n_2)^2}
 {(s_1^2/n_1)^2/(n_1-1)+(s_2^2/n_2)^2/(n_2-1)}.
\]
</div>
<p>قد تكون درجات الحرية التقريبية لويلش كسرية. تعتمد جودة التقريب، خاصةً مع العينات الصغيرة، على خصائص التوزيع ووجود القيم المتطرفة.</p>
<h2>4. الاختبار باستخدام التباين المشترك (Pooled)</h2>
<p>يفترض هذا الاختبار تساوي التباينين السكانيين بالإضافة إلى الاستقلال وشروط الاستدلال المعتادة؛ ولا يكفي تقارب تباينات العينات لإثبات ذلك.</p>
<div dir="ltr" role="region" tabindex="0" class="esa-t89-equation" aria-label="معادلات التباين المشترك">
\[
 s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2},
 \quad
 t_P=\frac{\bar x_1-\bar x_2-\delta_0}{s_p\sqrt{1/n_1+1/n_2}},
 \quad \nu_P=n_1+n_2-2.
\]
</div>
<h2>5. مثال عددي</h2>
<p>البيانات الأولى: \(73,77,80,78,82,79,84\)، والثانية: \(70,68,74,71,75,69\). متوسط الفرق \(\bar x_1-\bar x_2\approx7.833333\)، وتكون إحصائية ويلش \(t_W\approx4.446190\)، بدرجات حرية \(\nu_W\approx10.937907\)، وقيمة احتمالية ثنائية الطرف \(\approx0.000999\). أما اختبار التباين المشترك فيعطي \(t_P\approx4.357746\)، و\(\nu_P=11\)، وقيمة احتمالية \(\approx0.001141\). تُحسب فترات الثقة الثنائية 95% حول فرق المتوسطين باستخدام الخطأ المعياري والقيمة الحرجة الخاصة بكل طريقة.</p>
<h2>6. مختبر تفاعلي عربي للمقارنة</h2>
<section id="esa-welch-lab" data-locale="ar" class="concept-box" aria-labelledby="esa-w-heading">
<h3 id="esa-w-heading">ويلش والتباين المشترك على البيانات نفسها</h3>
<p>أدخل من 2 إلى 40 مشاهدة لكل مجموعة، مفصولة بفواصل أو مسافات. ليست هذه الأداة للقياسات المزدوجة.</p>
<div class="esa-w-fields">
<div><label for="esa-w-a">مشاهدات المجموعة أ</label><textarea id="esa-w-a" rows="4" spellcheck="false" aria-invalid="false" aria-describedby="esa-w-error">73, 77, 80, 78, 82, 79, 84</textarea></div>
<div><label for="esa-w-b">مشاهدات المجموعة ب</label><textarea id="esa-w-b" rows="4" spellcheck="false" aria-invalid="false" aria-describedby="esa-w-error">70, 68, 74, 71, 75, 69</textarea></div>
<div><label for="esa-w-alternative">الفرضية البديلة</label><select id="esa-w-alternative"><option value="two-sided">ثنائي الطرف</option><option value="greater">فرق المتوسطين أكبر من المفترض</option><option value="less">فرق المتوسطين أصغر من المفترض</option></select></div>
<div><label for="esa-w-null">فرق المتوسطين المفترض \(\delta_0\)</label><input id="esa-w-null" type="number" value="0" step="any" aria-invalid="false" aria-describedby="esa-w-error"></div>
</div>
<div class="esa-w-controls"><button type="button" class="btn btn-outline" id="esa-w-reset">استعادة المثال</button><button type="button" class="btn btn-outline" id="esa-w-reverse">تبديل المجموعتين</button></div>
<p id="esa-w-error" role="alert" hidden></p>
<section id="esa-w-results" aria-live="polite" aria-atomic="true" aria-label="نتائج اختبار ويلش">
<h4>النتائج الوصفية للمجموعتين</h4>
<div class="table-wrap"><table><caption>الإحصاءات الوصفية</caption><thead><tr><th>المقياس</th><th>أ</th><th>ب</th></tr></thead><tbody>
<tr><th scope="row">حجم العينة</th><td><output id="esa-w-n1">—</output></td><td><output id="esa-w-n2">—</output></td></tr>
<tr><th scope="row">المتوسط</th><td><output id="esa-w-mean1">—</output></td><td><output id="esa-w-mean2">—</output></td></tr>
<tr><th scope="row">الانحراف المعياري للعينة</th><td><output id="esa-w-sd1">—</output></td><td><output id="esa-w-sd2">—</output></td></tr>
</tbody></table></div>
<p>فرق المتوسطين أ − ب: <output id="esa-w-difference">—</output>؛ الخطأ المعياري لويلش: <output id="esa-w-se">—</output>؛ إحصائية t: <output id="esa-w-t">—</output>.</p>
<p>درجات الحرية التقريبية: <output id="esa-w-df">—</output>؛ القيمة الاحتمالية: <output id="esa-w-p">—</output>؛ القيمة الحرجة الثنائية 95%: <output id="esa-w-critical">—</output>.</p>
<p>فترة الثقة الثنائية 95%: [<output id="esa-w-lower">—</output>, <output id="esa-w-upper">—</output>].</p>
<svg id="esa-w-plot" viewBox="0 0 620 180" role="img" aria-label="فترة الثقة بطريقة ويلش" style="display:block;max-width:100%;width:100%;height:auto"></svg>
<p id="esa-w-conclusion"></p><p id="esa-w-interpret"></p>
</section>
<section class="concept-box" id="esa-pooled-comparison" aria-labelledby="esa-pool-heading">
<h4 id="esa-pool-heading">مقارنة مع اختبار التباين المشترك</h4>
<p>تستخدم الطريقتان البيانات والفرضية نفسها؛ يفترض الاختبار المشترك تساوي التباينين السكانيين، خلافاً لويلش.</p>
<div id="esa-w-pool-results" aria-live="polite" aria-atomic="true">
<div class="table-wrap"><table><caption>مخرجات اختبار التباين المشترك</caption><thead><tr><th>المقياس</th><th>القيمة</th></tr></thead><tbody>
<tr><th scope="row">الخطأ المعياري</th><td><output id="esa-w-pool-se">—</output></td></tr>
<tr><th scope="row">درجات الحرية</th><td><output id="esa-w-pool-df">—</output></td></tr>
<tr><th scope="row">إحصائية t</th><td><output id="esa-w-pool-t">—</output></td></tr>
<tr><th scope="row">القيمة الاحتمالية</th><td><output id="esa-w-pool-p">—</output></td></tr>
<tr><th scope="row">القيمة الحرجة الثنائية 95%</th><td><output id="esa-w-pool-critical">—</output></td></tr>
<tr><th scope="row">الحد الأدنى لفترة الثقة</th><td><output id="esa-w-pool-lower">—</output></td></tr>
<tr><th scope="row">الحد الأعلى لفترة الثقة</th><td><output id="esa-w-pool-upper">—</output></td></tr>
</tbody></table></div>
<svg id="esa-w-pool-plot" viewBox="0 0 610 130" role="img" aria-label="مقارنة فترتَي الثقة" style="display:block;max-width:100%;width:100%;height:auto"></svg>
<p id="esa-w-pool-warning" role="status" aria-live="polite"></p>
</div></section>
</section>
<h2>7. التفسير والقيود</h2>
<p>الفترة المعروضة ثنائية الطرف حتى عند اختيار بديلة أحادية الطرف. عدم رفض الفرضية لا يثبت تساوي المتوسطين أو التكافؤ الإحصائي. وجود دلالة إحصائية لا يثبت الأهمية العملية أو السببية. كل اختبار يفترض استقلال المشاهدات بين المجموعتين وداخل كل منهما، ويستلزم تقييماً لطبيعة البيانات والقيم المتطرفة.</p>
<p><a href="/ar/inference/classical-tests/paired-t-test/">الدرس السابق: العينات المزدوجة</a> · <a href="/inference/classical-tests/two-sample-t-test-independent/" lang="en">English counterpart</a></p>
</div></section>
<style>
#esa-welch-lab{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-welch-lab .esa-w-fields{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:12px 0}
#esa-welch-lab label{display:block;font-weight:650;margin-bottom:6px}
#esa-welch-lab :is(textarea,input,select){display:block;box-sizing:border-box;width:100%;min-width:0;max-width:100%;padding:10px;font:inherit;border:1px solid var(--border);border-radius:8px;color:var(--text);background:var(--surface)}
#esa-welch-lab .esa-w-controls{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}
#esa-welch-lab .table-wrap{display:block;box-sizing:border-box;max-width:100%;overflow-x:auto}
#esa-welch-lab #esa-pooled-comparison{max-width:100%;min-width:0;overflow:hidden;overflow-wrap:anywhere}
#esa-welch-lab #esa-pooled-comparison table{width:max-content;min-width:100%;max-width:none}
#esa-welch-lab :is(button,textarea,input,select):focus-visible{outline:2px solid #0f766e;outline-offset:2px}
#esa-welch-lab [hidden]{display:none!important}
.esa-t89-equation{max-width:100%;overflow-x:auto;padding:8px 0}
@media(max-width:650px){#esa-welch-lab .esa-w-fields{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/welch-two-sample-explorer.js"></script>
<script defer src="/js/pooled-two-sample-comparison.js"></script>
