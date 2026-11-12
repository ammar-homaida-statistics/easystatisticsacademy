---
layout: default
title: اختبار Z لنسبة مجتمع واحد — شرح عربي ومختبر تفاعلي
description: درس عربي في اختبار Z لنسبة واحدة والفرضيات والافتراضات وفترتَي والد وويلسون ومقارنة الاختبار الثنائي الحدين الدقيق.
permalink: /ar/inference/classical-tests/one-proportion-z-test/
lang: ar
math: true
sidebar: false
translation_pair: one-proportion-z
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<h1>اختبار Z لنسبة مجتمع واحد</h1>
<p class="lead">نستخدم الاختبار لاستقصاء نسبة نجاح سكانية مجهولة من مشاهدات مستقلة ثنائية النتيجة، ومقارنتها بنسبة مفترضة مسبقاً.</p>
<p><a lang="en" dir="ltr" href="/inference/classical-tests/one-proportion-z-test/">English — One-Proportion Z Test</a></p>
</div></section>
<section><div class="content-narrow" dir="rtl">
<h2>1. المسألة والفرضيات</h2>
<p>لنفترض أننا سجلنا \(x\) نجاحات من أصل \(n\) تجارب برنولية مستقلة ذات احتمال نجاح مشترك \(p\). إذا كانت العينة عشوائية وملائمة للتصميم، فإن \(X\sim\operatorname{Binomial}(n,p)\) ويكون التقدير \(\hat p=x/n\).</p>
<p>تختبر الفرضية الصفرية \(H_0:p=p_0\)، مقابل البديلة الثنائية \(H_1:p\ne p_0\)، أو أحادية الطرف \(p>p_0\) أو \(p<p_0\). يجب تحديد البديلة قبل النظر في البيانات.</p>
<h2>2. إحصائية الاختبار وتقييم التقريب</h2>
<div dir="ltr" class="esa-t90-equation" role="region" tabindex="0" aria-label="معادلة اختبار النسبة">
\[
 \mathrm{SE}_0=\sqrt{\frac{p_0(1-p_0)}{n}},\qquad
 Z=\frac{\hat p-p_0}{\mathrm{SE}_0}.
\]
</div>
<p>تقريب التوزيع الطبيعي يعتمد على مشاهدات مستقلة وثنائية، ويستحسن عادةً وجود عدد متوقع لا يقل عن عشرة لكل من النجاح والفشل تحت الفرضية الصفرية: \(np_0\ge10\) و\(n(1-p_0)\ge10\). هذه قاعدة تقريبية لا ضمانة مطلقة، ولا تصح إذا كانت البيانات مترابطة دون نمذجة الترابط.</p>
<h2>3. مثال محسوب</h2>
<p>إذا كان \(n=200\)، و\(x=120\)، و\(p_0=0.50\)، فإن \(\hat p=0.60\)، والخطأ المعياري الصفري يساوي تقريباً \(0.035355\)، و\(Z\approx2.828427\)، والقيمة الاحتمالية الطبيعية الثنائية \(\approx0.004678\). النتيجة إحصائية، ولا تعني وحدها وجود أثر سببي أو أهمية عملية.</p>
<h2>4. فترتا الثقة والدلالة العملية</h2>
<p>تُحسب فترة والد الثنائية 95% باستخدام \(\hat p\) وخطئها المعياري، لكنها قد تتجاوز [0،1] أو تسوء تغطيتها قرب الحدود. فترة ويلسون (Wilson score) غالباً أفضل أداء من حيث التغطية. الفترتان المعروضتان ثنائيتا الطرف حتى عند اختبار فرضية أحادية الطرف. لا تساوي القيمة الاحتمالية احتمال صحة الفرضية الصفرية.</p>
<div dir="ltr" class="esa-t90-equation" role="region" tabindex="0" aria-label="فترة والد">
\[
 \mathrm{CI}_{Wald}=\hat p\pm z_{0.975}\sqrt{\frac{\hat p(1-\hat p)}{n}}.
\]
</div>
<h2>5. مختبر اختبار Z وفترتَي والد وويلسون</h2>
<section class="concept-box" id="esa-one-proportion-lab" data-locale="ar" aria-labelledby="esa-op-heading">
<h3 id="esa-op-heading">غيّر البيانات ولاحظ النتائج فوراً</h3>
<p>أدخل عدد النجاحات وحجم العينة والنسبة الصفرية. يَستخدِم الاختبار خطأً معيارياً محسوباً تحت الفرضية الصفرية، وتستعمل فترة والد خطأً مختلفاً.</p>
<div class="esa-op-grid">
<label for="esa-op-x">عدد النجاحات \(x\)<input id="esa-op-x" type="number" min="0" max="1000000" step="1" value="120" aria-invalid="false" aria-describedby="esa-op-error"></label>
<label for="esa-op-n">حجم العينة \(n\)<input id="esa-op-n" type="number" min="1" max="1000000" step="1" value="200" aria-invalid="false" aria-describedby="esa-op-error"></label>
<label for="esa-op-p0">النسبة المفترضة \(p_0\)<input id="esa-op-p0" type="number" min="0" max="1" step="any" value="0.50" aria-invalid="false" aria-describedby="esa-op-error"></label>
<label for="esa-op-alternative">الفرضية البديلة<select id="esa-op-alternative"><option value="two-sided">ثنائية الطرف</option><option value="greater">النسبة أكبر</option><option value="less">النسبة أصغر</option></select></label>
</div>
<button type="button" class="btn btn-outline" id="esa-op-reset">استعادة المثال</button>
<p id="esa-op-error" role="alert" hidden></p>
<section id="esa-op-results" aria-live="polite" aria-atomic="true" aria-label="نتائج اختبار النسبة">
<p>النسبة المشاهدة: <output id="esa-op-phat"></output>؛ خطأ الفرضية الصفرية: <output id="esa-op-se0"></output>؛ إحصائية Z: <output id="esa-op-z"></output>؛ القيمة الاحتمالية: <output id="esa-op-pvalue"></output>.</p>
<p>خطأ والد المعياري: <output id="esa-op-seWald"></output>.</p>
<div class="table-wrap"><table><caption>فترتا الثقة الثنائيتان 95%</caption><thead><tr><th scope="col">الطريقة</th><th scope="col">الحد الأدنى</th><th scope="col">الحد الأعلى</th></tr></thead><tbody>
<tr><th scope="row">والد (Wald)</th><td><output id="esa-op-waldLower"></output></td><td><output id="esa-op-waldUpper"></output></td></tr>
<tr><th scope="row">ويلسون (Wilson)</th><td><output id="esa-op-wilsonLower"></output></td><td><output id="esa-op-wilsonUpper"></output></td></tr>
</tbody></table></div>
<svg id="esa-op-plot" viewBox="0 0 620 185" role="img" aria-label="فترتا والد وويلسون مقابل النسبة المفترضة"></svg>
<p id="esa-op-conditions"></p><p id="esa-op-decision"></p><p id="esa-op-interpretation"></p>
</section>
<p>عند ضعف شروط التقريب الطبيعي، انتقل إلى <a href="/inference/classical-tests/exact-binomial-vs-z-test/">مختبر المقارنة مع الاختبار الثنائي الحدين الدقيق</a>. الاختبار الدقيق يعتمد على نموذج ثنائي الحدين الصحيح، ولا يعالج بحد ذاته تحيز اختيار العينة أو الاعتماد بين المشاهدات.</p>
<h2>6. حدود التفسير</h2>
<p>عدم رفض \(H_0\) لا يثبت التساوي؛ ورفضها لا يثبت سببية العلاقة. تُفهم النتائج مع تصميم الدراسة وحجم الأثر وفترات الثقة. لا تُخزن المدخلات على الخادم.</p>
<p><a lang="en" href="/inference/classical-tests/one-proportion-z-test/">النسخة الإنجليزية</a> · <a href="/ar/inference/classical-tests/two-sample-t-test-independent/">الدرس السابق</a></p>
</div></section>
<style>
#esa-one-proportion-lab{box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere}
#esa-one-proportion-lab .esa-op-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:14px 0}
#esa-one-proportion-lab label{display:block;font-weight:600;min-width:0}
#esa-one-proportion-lab :is(input,select){display:block;box-sizing:border-box;min-width:0;max-width:100%;width:100%;padding:9px;font:inherit;border:1px solid var(--border);border-radius:8px;color:var(--text);background:var(--surface)}
#esa-one-proportion-lab [hidden]{display:none!important}
#esa-one-proportion-lab svg{display:block;width:100%;height:auto;max-width:640px;margin:10px auto}
#esa-one-proportion-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-one-proportion-lab :is(input,select,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-t90-equation{max-width:100%;overflow-x:auto;padding:8px 0}
@media(max-width:650px){#esa-one-proportion-lab .esa-op-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/one-proportion-z-explorer.js"></script>
