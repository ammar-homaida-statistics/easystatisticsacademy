---
layout: default
title: اختبار ماكنمار للنسب المزدوجة
description: شرح عربي لاختبار ماكنمار للبيانات الثنائية المزدوجة، مع الأزواج المتغيّرة والقيمة الاحتمالية الدقيقة وكاي تربيع ومختبر تفاعلي.
permalink: /ar/inference/classical-tests/mcnemar-test/
lang: ar
sidebar: false
learning_resource: true
translation_pair: mcnemar-test
---
<section class="hero hero-section"><div class="hero-card">
<h1>اختبار ماكنمار للنسب المزدوجة</h1>
<p class="lead">عندما يُصنَّف الأشخاص أنفسهم مرتين (قبل دورة تدريبية وبعدها، أو بواسطة مقيّمَين، أو باختبارين تشخيصيين)، لا تكون النسبتان مستقلتين. يقارن اختبار ماكنمار (McNemar) بينهما باستخدام الأزواج التي تغيّرت فقط.</p>
<p><a href="/inference/classical-tests/mcnemar-test/" lang="en" dir="ltr">English version</a> · <a href="/ar/inference/classical-tests/two-proportion-z-test/">النسب المستقلة: اختبار Z لنسبتين</a> · <a href="/ar/inference/classical-tests/paired-t-test/">البيانات الكمية المزدوجة: اختبار t للعينات المزدوجة</a></p>
</div></section>
<section><div class="content-narrow">
<h2>1. سؤال البحث</h2>
<p>يُقيَّم برنامج تدريبي على 100 موظف. يخضع كل موظف لاختبار مهارات (نجاح/رسوب) <strong>قبل</strong> التدريب و<strong>بعده</strong>. هل تغيّرت نسبة النجاح؟ لأن كل شخص يقدّم نتيجتين مترابطتين، فإن اختبار Z لنسبتين واختبار كاي تربيع للاستقلال غير مناسبين؛ فكلاهما يفترض عينتين مستقلتين.</p>
<h2>2. جدول الأزواج 2 × 2</h2>
<p>يُعدّ كل <em>زوج</em> (شخص واحد وقياسان) مرة واحدة:</p>
<div class="table-wrap"><table><caption>نتائج 100 موظف قبل التدريب وبعده</caption><thead><tr><th scope="col">قبل \ بعد</th><th scope="col">نجاح بعد</th><th scope="col">رسوب بعد</th><th scope="col">المجموع</th></tr></thead><tbody><tr><th scope="row">نجاح قبل</th><td dir="ltr">a = 45</td><td dir="ltr">b = 5</td><td>50</td></tr><tr><th scope="row">رسوب قبل</th><td dir="ltr">c = 20</td><td dir="ltr">d = 30</td><td>50</td></tr><tr><th scope="row">المجموع</th><td>65</td><td>35</td><td>100</td></tr></tbody></table></div>
<p>نسبة النجاح قبل التدريب \((a+b)/n=0.50\) وبعده \((a+c)/n=0.65\)، والفرق بينهما:</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="الفرق بين النسبتين المزدوجتين">
\[
\hat p_{\text{after}}-\hat p_{\text{before}}=\frac{a+c}{n}-\frac{a+b}{n}=\frac{c-b}{n}=\frac{20-5}{100}=0.15 .
\]</div>
<p>تختفي الخليتان المتوافقتان \(a\) و\(d\): فمن نجح في المرتين أو رسب في المرتين لا يقدّم أي معلومة عن <em>التغيّر</em>. الذي يهمّ هو <strong>الأزواج المتغيّرة</strong> \(b\) و\(c\) فقط.</p>
<h2>3. الفرضيتان</h2>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="فرضيتا ماكنمار">
\[
H_0:\ P(\text{pass before})=P(\text{pass after})\iff \pi_b=\pi_c,
\qquad H_a:\ \pi_b\ne\pi_c .
\]</div>
<p>تُسمّى الفرضية الصفرية <strong>تجانس الهوامش</strong>. تحت \(H_0\) يكون الزوج المتغيّر من النوع \(b\) أو النوع \(c\) باحتمال متساوٍ. وبشرط عدد الأزواج المتغيّرة \(n_d=b+c\):</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="التوزيع الشرطي الدقيق">
\[
b \mid n_d \sim \operatorname{Binomial}\!\left(n_d,\tfrac12\right).
\]</div>
<h2>4. ثلاث طرق لحساب القيمة الاحتمالية</h2>
<h3>أ. الاختبار الدقيق لذات الحدين</h3>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="القيمة الاحتمالية الدقيقة">
\[
p_{\text{exact}}=\min\!\left\{1,\ 2\,P\!\left(X\le \min(b,c)\right)\right\},\qquad X\sim\operatorname{Binomial}\!\left(b+c,\tfrac12\right).
\]</div>
<p>لأن التوزيع الصفري متماثل، فإن مضاعفة الطرف الأصغر هي القيمة الاحتمالية الثنائية المعتادة، وهي صحيحة مهما كان عدد الأزواج المتغيّرة.</p>
<h3>ب. إحصائية كاي تربيع التقاربية</h3>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="إحصائية ماكنمار">
\[
\chi^2_{\text{McN}}=\frac{(b-c)^2}{b+c},\qquad df=1 .
\]</div>
<p>هي مربع التقريب الطبيعي \(z=(b-c)/\sqrt{b+c}\) لتوزيع ذات الحدين أعلاه، لذا تحتاج إلى عدد معقول من الأزواج المتغيّرة.</p>
<h3>ج. كاي تربيع مع تصحيح الاستمرارية (إدواردز)</h3>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="الإحصائية المصححة">
\[
\chi^2_{\text{cc}}=\frac{\left(\max\{|b-c|-1,\,0\}\right)^2}{b+c}.
\]</div>
<p>يقرّب التصحيح القيمة الاحتمالية من الدقيقة في العينات الصغيرة لكنه متحفظ. ومع البرمجيات الحديثة يُفضَّل الاختبار الدقيق عندما يكون \(b+c\) صغيرًا؛ والقاعدة الإرشادية الشائعة \(b+c&lt;25\). بعض البرمجيات لا تستخدم الحد \(\max\{\cdot,0\}\)، ولا يغيّر ذلك النتيجة إلا عندما \(b=c\).</p>
<h2>5. مثال محلول</h2>
<p>هنا \(b=5\) و\(c=20\) و\(n_d=25\):</p>
<div class="esa-long-math" dir="ltr" tabindex="0" role="region" aria-label="المثال المحلول">
\[
\chi^2_{\text{McN}}=\frac{(5-20)^2}{25}=9,\ p\approx0.00270;\qquad
\chi^2_{\text{cc}}=\frac{14^2}{25}=7.84,\ p\approx0.00511;\qquad
p_{\text{exact}}=2P(X\le5)\approx0.00408 .
\]</div>
<p>ترفض الطرق الثلاث \(H_0\) عند \(\alpha=0.05\): نسبة النجاح بعد التدريب تختلف عنها قبله، إذ تحوّل 15 موظفًا من الرسوب إلى النجاح أكثر من العكس. لكن هذا التصميم وحده لا يكفي لنسب التغيّر إلى التدريب؛ فقد يفسّره أثر التمرّن على الاختبار أو أحداث أخرى بين القياسين.</p>
<h2>6. مختبر ماكنمار التفاعلي</h2>
<section id="esa-mcnemar-lab" class="concept-box" data-locale="ar" aria-labelledby="esa-mcn-heading">
<h3 id="esa-mcn-heading">أدخل أعداد الأزواج</h3>
<noscript><p class="esa-noscript" role="note">يتطلب هذا المختبر التفاعلي تفعيل JavaScript. من دونه تبقى الأرقام المعروضة هي المثال المحلول الثابت، وتظل الصيغ والتفسير في الدرس متاحة.</p></noscript>
<p>الصفوف للقياس الأول والأعمدة للقياس الثاني. أدخل أعدادًا صحيحة لـ<strong>الأزواج</strong> لا للقياسات المنفردة.</p>
<div class="esa-mcn-grid">
<label>a: + ثم + <input id="esa-mcn-a" dir="ltr" type="number" min="0" max="10000000" step="1" value="45" inputmode="numeric" aria-invalid="false" aria-describedby="esa-mcn-error"></label>
<label>b: + ثم − <input id="esa-mcn-b" dir="ltr" type="number" min="0" max="10000000" step="1" value="5" inputmode="numeric" aria-invalid="false" aria-describedby="esa-mcn-error"></label>
<label>c: − ثم + <input id="esa-mcn-c" dir="ltr" type="number" min="0" max="10000000" step="1" value="20" inputmode="numeric" aria-invalid="false" aria-describedby="esa-mcn-error"></label>
<label>d: − ثم − <input id="esa-mcn-d" dir="ltr" type="number" min="0" max="10000000" step="1" value="30" inputmode="numeric" aria-invalid="false" aria-describedby="esa-mcn-error"></label>
</div>
<div class="esa-mcn-controls"><button type="button" class="btn btn-outline" id="esa-mcn-example">مثال التدريب</button><button type="button" class="btn btn-outline" id="esa-mcn-small">أزواج متغيّرة قليلة</button><button type="button" class="btn btn-outline" id="esa-mcn-none">لا توجد أزواج متغيّرة</button></div>
<p id="esa-mcn-error" role="alert" hidden></p>
<div class="esa-mcn-results" role="status" aria-live="polite" aria-atomic="true">
<p>عدد الأزواج n = <output id="esa-mcn-n" dir="ltr">100</output>؛ الأزواج المتغيّرة b + c = <output id="esa-mcn-nd" dir="ltr">25</output>.</p>
<p>نسبة الموجب: القياس الأول = <output id="esa-mcn-p1" dir="ltr">0.5000</output>، القياس الثاني = <output id="esa-mcn-p2" dir="ltr">0.6500</output>؛ الأول − الثاني = <output id="esa-mcn-diff" dir="ltr">-0.1500</output>.</p>
<div class="table-wrap"><table><caption>إحصاءات ماكنمار والقيم الاحتمالية الثنائية</caption><thead><tr><th scope="col">الطريقة</th><th scope="col">الإحصائية</th><th scope="col">القيمة الاحتمالية</th></tr></thead><tbody>
<tr><th scope="row">ذات الحدين الدقيق</th><td>—</td><td><output id="esa-mcn-exact" dir="ltr">0.004077</output></td></tr>
<tr><th scope="row">كاي تربيع دون تصحيح</th><td><output id="esa-mcn-chi" dir="ltr">9.000000</output></td><td><output id="esa-mcn-p" dir="ltr">0.002700</output></td></tr>
<tr><th scope="row">كاي تربيع مع تصحيح الاستمرارية</th><td><output id="esa-mcn-chicc" dir="ltr">7.840000</output></td><td><output id="esa-mcn-pcc" dir="ltr">0.005110</output></td></tr>
</tbody></table></div>
</div>
<p id="esa-mcn-advice" role="status" aria-live="polite">مع 25 زوجًا متغيّرًا يكون تقريب كاي تربيع مقبولًا عادة؛ وتبقى القيمة الاحتمالية الدقيقة صحيحة ويمكن ذكرها دائمًا.</p>
<p class="muted-mini">تغيير a أو d لا يغيّر أي إحصائية أو قيمة احتمالية لماكنمار؛ بل يغيّر النسبتين الهامشيتين فقط. تستخدم قيم كاي تربيع درجة حرية واحدة، والقيمة الدقيقة هي ضعف الطرف الأصغر لذات الحدين.</p>
</section>
<h2>7. الافتراضات والقيود</h2>
<ul class="bullets"><li>كل زوج وحدة متطابقة (الشخص نفسه مرتين، أو زوج مطابَق عمدًا)، والأزواج مستقلة بعضها عن بعض.</li><li>النتيجة ثنائية في القياسين وبالفئات نفسها.</li><li>يختبر ماكنمار تغيّر النسب الهامشية، لا الاتفاق؛ أما الاتفاق بين مقيّمَين فيقيسه <a href="/inference/classical-tests/cohens-kappa/">معامل كوهين كابا (بالإنجليزية)</a>.</li><li>دون مجموعة ضابطة، لا يثبت التغيّر الدال أن التدخل هو سببه.</li></ul>
<h2>8. الاختيار بين الاختبارات المتقاربة</h2>
<ul class="bullets"><li><strong>مجموعتان مستقلتان ونتيجة ثنائية:</strong> <a href="/ar/inference/classical-tests/two-proportion-z-test/">اختبار Z لنسبتين</a>.</li><li><strong>الوحدات نفسها مرتين ونتيجة ثنائية:</strong> اختبار ماكنمار (هذا الدرس).</li><li><strong>الوحدات نفسها مرتين ونتيجة كمية:</strong> <a href="/ar/inference/classical-tests/paired-t-test/">اختبار t للعينات المزدوجة</a>.</li></ul>
<div class="summary-box"><h2>خلاصة الدرس</h2><ul class="bullets"><li>البيانات الثنائية المزدوجة تخالف افتراض الاستقلال في اختبارات النسبتين.</li><li>الأزواج المتغيّرة \(b\) و\(c\) وحدها تحمل المعلومة عن التغيّر.</li><li>القيمة الدقيقة: \(\min\{1,2P(X\le\min(b,c))\}\) حيث \(X\sim\operatorname{Bin}(b+c,1/2)\).</li><li>الإحصائية التقاربية: \((b-c)^2/(b+c)\) بدرجة حرية واحدة؛ ويُفضَّل الاختبار الدقيق عندما يكون \(b+c\) صغيرًا.</li></ul></div>
</div></section>
<style>
#esa-mcnemar-lab{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-mcnemar-lab .esa-mcn-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,160px),1fr));gap:12px;margin:14px 0}
#esa-mcnemar-lab label{display:flex;flex-direction:column;gap:6px;min-width:0;font-weight:600}
#esa-mcnemar-lab input{box-sizing:border-box;width:100%;max-width:100%;padding:8px;font:inherit}
#esa-mcnemar-lab .esa-mcn-controls{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
#esa-mcnemar-lab .esa-mcn-controls button{max-width:100%;white-space:normal}
#esa-mcnemar-lab .table-wrap{display:block;max-width:100%;overflow-x:auto}
#esa-mcnemar-lab output{unicode-bidi:isolate}
#esa-mcnemar-lab [hidden]{display:none!important}
#esa-mcnemar-lab [role="alert"]{color:#b42318;font-weight:700}
#esa-mcnemar-lab :is(input,button):focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.esa-long-math{max-width:100%;overflow-x:auto;direction:ltr}
</style>
<script defer src="/js/mcnemar-test-lab.js"></script>
