---
layout: default
title: اختبار Z لنسبتين مستقلتين — شرح عربي ومختبر تفاعلي
description: مقارنة نسبتي مجتمعين مستقلين مع شرح الخطأ المعياري المشترك لاختبار فرضية التساوي وفترة والد غير المشتركة والتفسير المسؤول.
permalink: /ar/inference/classical-tests/two-proportion-z-test/
lang: ar
math: true
sidebar: false
translation_pair: two-proportion-z
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<h1>اختبار Z للمقارنة بين نسبتين مستقلتين</h1>
<p class="lead">نقارن بين نسبتي النجاح في مجتمعين مختلفين باستخدام عينتين مستقلتين، ونفهم الفرق بين الخطأ المعياري للاختبار والفترة التقديرية.</p>
<p><a href="/inference/classical-tests/two-proportion-z-test/" lang="en" dir="ltr">English — Two-Proportion Z Test</a></p>
</div></section>
<section><div class="content-narrow" dir="rtl">
<h2>1. شروط استخدام الاختبار</h2>
<p>تتضمن كل مجموعة مشاهدات ثنائية (نجاح أو فشل)، مستقلة بين المجموعتين وداخل كل مجموعة حسب التصميم. إذا كان \(x_i\) عدد النجاحات و\(n_i\) حجم العينة، فإن \(\hat p_i=x_i/n_i\). نهتم بالفارق \(p_1-p_2\)، ونختبر \(H_0:p_1=p_2\)، مقابل البديلة الثنائية \(p_1\ne p_2\) أو البديلتين الاتجاهيتين المحددتين مسبقاً.</p>
<h2>2. الخطأ المعياري للاختبار</h2>
<p>تحت فرضية تساوي النسبتين نستخدم تقدير النسبة المشتركة (المجمّعة)، وليس الخطأ المعياري غير المشترك المستخدم لتكوين فترة والد التقريبية.</p>
<div dir="ltr" class="esa-t91-equation" role="region" tabindex="0" aria-label="معادلات اختبار النسبتين">
\[
\hat p=\frac{x_1+x_2}{n_1+n_2},\quad
Z=\frac{\hat p_1-\hat p_2}{\sqrt{\hat p(1-\hat p)(1/n_1+1/n_2)}}.
\]
</div>
<p>نُراجع الأعداد المتوقعة للنجاح والفشل في كل مجموعة باستخدام \(\hat p\). من الشروط التقريبية المعتادة ألا يقل أي عدد متوقع عن 10. إذا كانت جميع المشاهدات نجاحات أو إخفاقات، فإن تباين الاختبار المشترك يساوي صفراً وتكون الإحصائية المعتادة غير معرّفة.</p>
<h2>3. فترة الثقة ومشكلة التقريب</h2>
<div dir="ltr" class="esa-t91-equation" role="region" tabindex="0" aria-label="فترة الثقة التقريبية">
\[
(\hat p_1-\hat p_2)\pm z_{0.975}
\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1}+\frac{\hat p_2(1-\hat p_2)}{n_2}}.
\]
</div>
<p>فترة والد غير المشتركة المعروضة ثنائية الطرف 95%، وقد تتجاوز مجال الفروق الممكن [−1،1]، كما يمكن أن تضعف تغطيتها في العينات الصغيرة أو قرب الحدود. اختبار Z المجمّع ليس عكس هذه الفترة بالضرورة؛ وقد تختلف قراراتهما قرب مستوى الدلالة. طرق فترات الثقة المحسّنة مناسبة عند الحاجة.</p>
<h2>4. مثال ومختبر تفاعلي</h2>
<p>مثال: 120 نجاحاً من أصل 200 في المجموعة أ، و90 نجاحاً من أصل 200 في المجموعة ب. الفرق المشاهد \(0.15\)؛ النسبة المشتركة \(\hat p=0.525\). يمكن تغيير الأعداد أدناه لفحص أثر حجم العينتين والنسب.</p>
<section class="concept-box" id="esa-two-proportion-lab" data-locale="ar" aria-labelledby="esa-2p-heading">
<h3 id="esa-2p-heading">مختبر اختبار النسبتين</h3>
<div class="esa-2p-fields">
<label for="esa-2p-x1">نجاحات المجموعة أ \(x_1\)<input id="esa-2p-x1" type="number" min="0" step="1" value="120" aria-invalid="false" aria-describedby="esa-2p-error"></label>
<label for="esa-2p-n1">حجم المجموعة أ \(n_1\)<input id="esa-2p-n1" type="number" min="1" step="1" value="200" aria-invalid="false" aria-describedby="esa-2p-error"></label>
<label for="esa-2p-x2">نجاحات المجموعة ب \(x_2\)<input id="esa-2p-x2" type="number" min="0" step="1" value="90" aria-invalid="false" aria-describedby="esa-2p-error"></label>
<label for="esa-2p-n2">حجم المجموعة ب \(n_2\)<input id="esa-2p-n2" type="number" min="1" step="1" value="200" aria-invalid="false" aria-describedby="esa-2p-error"></label>
<label for="esa-2p-alternative">الفرضية البديلة<select id="esa-2p-alternative"><option value="two-sided">ثنائية الطرف</option><option value="greater">أكبر: نسبة أ أعلى</option><option value="less">أصغر: نسبة أ أدنى</option></select></label>
</div>
<div class="esa-2p-controls"><button class="btn btn-outline" type="button" id="esa-2p-reset">استعادة المثال</button><button class="btn btn-outline" type="button" id="esa-2p-swap">تبديل المجموعتين</button></div>
<p id="esa-2p-error" role="alert" hidden></p>
<div id="esa-2p-results" aria-live="polite" aria-atomic="true">
<div class="table-wrap"><table><caption>النسبتان المشاهدتان</caption><thead><tr><th scope="col">المقياس</th><th scope="col">أ</th><th scope="col">ب</th></tr></thead>
<tbody><tr><th scope="row">نسبة النجاح</th><td><output id="esa-2p-p1"></output></td><td><output id="esa-2p-p2"></output></td></tr></tbody></table></div>
<p>فرق النسبتين: <output id="esa-2p-diff"></output>؛ النسبة المشتركة: <output id="esa-2p-pooled"></output>؛ الخطأ المعياري تحت الفرضية الصفرية: <output id="esa-2p-pooledSE"></output>.</p>
<p>إحصائية Z: <output id="esa-2p-z"></output>؛ القيمة الاحتمالية: <output id="esa-2p-p"></output>؛ الخطأ المعياري غير المشترك لفترة الثقة: <output id="esa-2p-seCI"></output>.</p>
<p>فترة والد الثنائية 95%: [<output id="esa-2p-lower"></output>، <output id="esa-2p-upperCI"></output>].</p>
<svg id="esa-2p-plot" viewBox="0 0 620 185" role="img" aria-label="فرق النسبتين وفترة الثقة" style="display:block;width:100%;height:auto;max-width:100%"></svg>
<p id="esa-2p-conditions"></p><p id="esa-2p-conclusion"></p><p id="esa-2p-interpretation"></p>
</div></section>
<h2>5. التفسير</h2>
<p>رفض الفرضية الصفرية يدل على دليل إحصائي ضد مساواة نسبتي المجتمعين ضمن افتراضات الاختبار، ولا يثبت السببية. عدم رفضها لا يثبت التساوي. مع البيانات المتفرقة والجداول الصغيرة، انظر <a href="/inference/classical-tests/fisher-exact-vs-chi-square/">اختبار فيشر الدقيق ومقارنته بمربع كاي</a>، مع مراعاة اختلاف النموذج والفرضية.</p>
<p><a href="/ar/inference/classical-tests/one-proportion-z-test/">الدرس السابق: اختبار نسبة واحدة</a> · <a href="/inference/classical-tests/two-proportion-z-test/" lang="en">English counterpart</a></p>
</div></section>
<style>
#esa-two-proportion-lab{box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere}
#esa-two-proportion-lab .esa-2p-fields{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:14px 0}
#esa-two-proportion-lab label{display:block;min-width:0;font-weight:600}
#esa-two-proportion-lab :is(input,select){display:block;box-sizing:border-box;min-width:0;max-width:100%;width:100%;font:inherit;padding:10px;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text)}
#esa-two-proportion-lab .esa-2p-controls{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
#esa-two-proportion-lab .table-wrap{display:block;max-width:100%;overflow-x:auto}
#esa-two-proportion-lab [hidden]{display:none!important}
#esa-two-proportion-lab :is(input,select,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-t91-equation{max-width:100%;overflow-x:auto;padding:8px 0}
@media(max-width:650px){#esa-two-proportion-lab .esa-2p-fields{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/two-proportion-z-explorer.js"></script>
