---
layout: default
title: اختبار Z لعينة واحدة لمتوسط المجتمع
description: شرح عربي لاختبار Z لمتوسط واحد عند معرفة الانحراف المعياري للمجتمع مع القيمة الاحتمالية وفترة الثقة ومختبر إحصائي تفاعلي.
permalink: /ar/inference/classical-tests/one-sample-z-test-for-mean/
lang: ar
math: true
sidebar: false
translation_pair: one-sample-z-test-mean
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<h1>اختبار Z لعينة واحدة لمتوسط المجتمع</h1>
<p class="lead">نختبر فرضية عن متوسط المجتمع \(\mu\) باستخدام متوسط العينة عندما يكون الانحراف المعياري السكاني \(\sigma\) معلوماً، مع مراعاة استقلال الملاحظات وشروط التوزيع الطبيعي أو التقريب بنظرية الحد المركزي.</p>
<p><a href="/inference/classical-tests/one-sample-z-test-for-mean/" lang="en" dir="ltr">Read in English: One-Sample Z Test for a Mean</a></p>
</div></section>
<section class="section"><div class="content-narrow" dir="rtl">
<h2>1. الفرضيتان الصفرية والبديلة</h2>
<p>نحدد القيمة المرجعية \(\mu_0\) قبل تحليل البيانات. ويمكن أن يكون الاختبار ثنائي الطرف أو ذا طرف واحد حسب سؤال البحث:</p>
<div class="esa-z-math" dir="ltr" tabindex="0" role="region" aria-label="صيغ الفرضيات الإحصائية">\[
H_0:\mu=\mu_0,\qquad
H_1:\mu\ne\mu_0\ \text{ أو }\ \mu>\mu_0\ \text{ أو }\ \mu<\mu_0.
\]</div>
<h2>2. متى يصح استخدام اختبار Z؟</h2>
<p>يشترط معرفة <strong>الانحراف المعياري السكاني</strong> \(\sigma>0\)، وليس مجرد تقدير الانحراف المعياري للعينة \(s\). مع ملاحظات مستقلة مأخوذة بتصميم مناسب، يكون الاختبار دقيقاً عند السحب من مجتمع طبيعي ذي \(\sigma\) معلوم. وعند غياب الطبيعية قد يكون تقريبياً لعينات كبيرة تستوفي شروط نظرية الحد المركزي. معرفة \(\sigma\) وحدها لا تضمن صحة التقريب للعينات الصغيرة، ولا يعالج حجم العينة الكبير انحياز اختيار العينة.</p>
<h2>3. إحصائية الاختبار وخطؤها المعياري</h2>
<div class="esa-z-math" dir="ltr" tabindex="0" role="region" aria-label="صيغة الخطأ المعياري وإحصائية Z">\[
\operatorname{SE}(\overline X)=\frac{\sigma}{\sqrt n},\qquad
Z=\frac{\overline X-\mu_0}{\sigma/\sqrt n}.
\]</div>
<p>في ظل \(H_0\) ومع تحقق الافتراضات، يتبع \(Z\) التوزيع الطبيعي المعياري بالضبط أو تقريباً حسب حالة المجتمع وحجم العينة.</p>
<h2>4. مثال محلول</h2>
<p>لنفترض أن متوسط قياس حجم تعبئة العبوات المرجعي هو \(500\) مل، وأن متوسط عينة من \(100\) عبوة هو \(492\) مل، مع انحراف معياري سكاني معلوم قدره \(20\) مل. في اختبار ثنائي الطرف عند مستوى معنوية \(0.05\):</p>
<div class="esa-z-math" dir="ltr" tabindex="0" role="region" aria-label="حساب إحصائية المثال">\[
\operatorname{SE}=\frac{20}{\sqrt{100}}=2,\qquad
Z=\frac{492-500}{2}=-4.
\]</div>
<p>القيمة الاحتمالية الثنائية تقارب \(0.00006334\)، وهي أصغر من \(0.05\)، لذا نرفض \(H_0\) بشرط سلامة التصميم والافتراضات. لا يعني ذلك أن احتمال صحة \(H_0\) يساوي القيمة الاحتمالية، ولا يثبت الاختبار وجود أثر سببي.</p>
<h2>5. فترة الثقة 95% للمتوسط</h2>
<div class="esa-z-math" dir="ltr" tabindex="0" role="region" aria-label="حساب فترة الثقة للمثال">\[
\overline x\pm z_{0.975}\frac{\sigma}{\sqrt n}
=492\pm1.9599639845(2)
\approx[488.0801,\ 495.9199]\ \text{mL}.
\]</div>
<p>تستبعد الفترةُ \(500\)، بما يتفق مع قرار الاختبار ثنائي الطرف عند \(\alpha=0.05\). وتبقى فترة الثقة الموضحة في المختبر ثنائية الطرف حتى إذا اختيرت فرضية بديلة أحادية الطرف للاختبار؛ ولا يجوز خلط القرار الأحادي الطرف بتفسير فترة ثقة ثنائية الطرف على أنهما متكافئان.</p>
<h2>6. مختبر تفاعلي لاختبار Z</h2>
<section class="concept-box" id="esa-one-mean-z-lab" data-locale="ar" aria-labelledby="esa-omz-heading" style="max-width:100%;min-width:0">
<h3 id="esa-omz-heading">جرّب متوسط العينة وحجمها والانحراف المعياري</h3>
<p>أدخل المعطيات لمعرفة إحصائية الاختبار والقيمة الاحتمالية وفترة الثقة. جميع العمليات الحسابية تُنفَّذ بواسطة محرك الاختبار نفسه المستخدم في الدرس الإنجليزي.</p>
<div class="esa-omz-grid">
<div><label for="esa-omz-n">حجم العينة \(n\)</label><input id="esa-omz-n" type="number" min="1" max="1000000" step="1" value="100" inputmode="numeric" aria-describedby="esa-omz-error"></div>
<div><label for="esa-omz-mean">متوسط العينة \(\overline x\)</label><input id="esa-omz-mean" type="number" step="any" value="492" aria-describedby="esa-omz-error"></div>
<div><label for="esa-omz-sigma">الانحراف المعياري السكاني المعلوم \(\sigma\)</label><input id="esa-omz-sigma" type="number" min="0" step="any" value="20" aria-describedby="esa-omz-error"></div>
<div><label for="esa-omz-mu0">المتوسط المفترض \(\mu_0\)</label><input id="esa-omz-mu0" type="number" step="any" value="500" aria-describedby="esa-omz-error"></div>
<div><label for="esa-omz-side">الفرضية البديلة</label><select id="esa-omz-side">
<option value="two-sided">ثنائي الطرف: \(\mu\ne\mu_0\)</option>
<option value="greater">الطرف الأيمن: \(\mu>\mu_0\)</option>
<option value="less">الطرف الأيسر: \(\mu<\mu_0\)</option></select></div>
</div>
<button type="button" class="btn btn-outline" id="esa-omz-reset">استعادة قيم المثال</button>
<p id="esa-omz-error" role="alert" hidden></p>
<section id="esa-omz-results" role="status" aria-live="polite" aria-label="نتائج اختبار Z لعينة واحدة">
<div class="table-wrap"><table><caption>إحصائية Z وفترة الثقة الثنائية عند 95%</caption><tbody>
<tr><th scope="row">الخطأ المعياري</th><td dir="ltr" id="esa-omz-se">—</td></tr>
<tr><th scope="row">إحصائية Z</th><td dir="ltr" id="esa-omz-z">—</td></tr>
<tr><th scope="row">القيمة الاحتمالية للبديلة المختارة</th><td dir="ltr" id="esa-omz-pvalue">—</td></tr>
<tr><th scope="row">الحد الأدنى لفترة الثقة 95%</th><td dir="ltr" id="esa-omz-lower">—</td></tr>
<tr><th scope="row">الحد الأعلى لفترة الثقة 95%</th><td dir="ltr" id="esa-omz-upper">—</td></tr>
</tbody></table></div>
<svg id="esa-omz-plot" role="img" viewBox="0 0 620 235" aria-label="التوزيع الطبيعي المعياري والقيم الاحتمالية" style="display:block;width:100%;height:auto;max-width:100%"></svg>
<p id="esa-omz-decision"></p>
<p id="esa-omz-assumptions"></p>
<p id="esa-omz-interpretation"></p>
</section>
</section>
<style>
#esa-one-mean-z-lab,#esa-one-mean-z-lab *{box-sizing:border-box}
#esa-one-mean-z-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-one-mean-z-lab .esa-omz-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,215px),1fr));gap:12px;margin:14px 0}
#esa-one-mean-z-lab label{display:block;font-weight:650;margin-bottom:6px}
#esa-one-mean-z-lab :is(input,select){display:block;width:100%;min-width:0;padding:10px;border:1px solid #777;border-radius:7px;font:inherit}
#esa-one-mean-z-lab [hidden]{display:none!important}
#esa-one-mean-z-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-one-mean-z-lab td{font-variant-numeric:tabular-nums}
#esa-one-mean-z-lab :is(input,select,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
@media(max-width:650px){#esa-one-mean-z-lab .esa-omz-grid{grid-template-columns:minmax(0,1fr)}}
.esa-z-math{direction:ltr;max-width:100%;overflow-x:auto;padding:6px 0}
</style>
<script defer src="/js/one-mean-z-explorer.js"></script>
<h2>7. أخطاء يجب تجنبها</h2>
<ul class="bullets">
<li>استخدام الانحراف المعياري للعينة \(s\) وكأنه \(\sigma\) المعلوم من المجتمع.</li>
<li>اعتبار عدم رفض الفرضية الصفرية دليلاً على صحتها.</li>
<li>اختيار طرف الاختبار بعد الاطلاع على النتائج.</li>
<li>اعتبار فترة الثقة للمتوسط فترة تنبؤ لملاحظة مستقبلية واحدة.</li>
<li>إهمال الاستقلال أو افتراض طبيعية المجتمع من دون مبرر.</li>
</ul>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/inference/classical-tests/decision-framework-and-assumptions/">السابق: إطار اختبار الفرضيات</a><a class="btn" href="/inference/classical-tests/one-sample-t-test-for-mean/" lang="en">التالي: اختبار t لعينة واحدة (إنجليزي)</a></div>
</div></section>