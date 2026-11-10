---
layout: default
title: اختبار t لعينة واحدة لمتوسط المجتمع
description: درس عربي في اختبار ستودنت لعينة واحدة عند جهل الانحراف المعياري السكاني، مع حساب القيمة الاحتمالية وفترة الثقة ومختبر تفاعلي.
permalink: /ar/inference/classical-tests/one-sample-t-test-for-mean/
lang: ar
math: true
sidebar: false
translation_pair: one-sample-student-t-mean
learning_resource: true
---
<section class="hero hero-section"><div class="hero-card">
<h1>اختبار t لعينة واحدة لمتوسط المجتمع</h1>
<p class="lead">نستخدم اختبار ستودنت لعينة واحدة لفحص فرضية حول متوسط مجتمع \(\mu\) عندما يكون انحرافه المعياري \(\sigma\) مجهولاً، فنستعمل الانحراف المعياري للعينة \(s\) ونأخذ عدم اليقين في تقديره في الحسبان.</p>
<p><a lang="en" dir="ltr" href="/inference/classical-tests/one-sample-t-test-for-mean/">Read in English: One-Sample t Test for a Mean</a></p>
</div></section>
<section class="section"><div class="content-narrow" dir="rtl">
<h2>1. صياغة الفرضيات</h2>
<p>تحدد الفرضية الصفرية القيمة المرجعية لمتوسط المجتمع، ويُختار اتجاه الفرضية البديلة مسبقاً، لا بعد معرفة النتائج.</p>
<div class="esa-st-math" dir="ltr" tabindex="0" role="region" aria-label="صيغ الفرضيات">\[H_0:\mu=\mu_0,\quad H_1:\mu\ne\mu_0\ \text{أو}\ \mu>\mu_0\ \text{أو}\ \mu<\mu_0.\]</div>
<h2>2. إحصائية t ودرجات الحرية</h2>
<p>لمجموعة من \(n\ge2\) ملاحظات مستقلة، نحسب متوسط العينة \(\overline X\) والانحراف المعياري للعينة \(s\) باستخدام المقام \(n-1\):</p>
<div class="esa-st-math" dir="ltr" tabindex="0" role="region" aria-label="صيغ الانحراف المعياري وإحصائية ستودنت">\[
s^2=\frac{\sum_{i=1}^{n}(X_i-\overline X)^2}{n-1},\qquad
T=\frac{\overline X-\mu_0}{s/\sqrt n},\qquad df=n-1.
\]</div>
<p>إذا كانت الملاحظات مستقلة ومأخوذة من مجتمع طبيعي، فإن إحصائية الاختبار تحت \(H_0\) تتبع توزيع ستودنت بدرجات حرية \(n-1\)؛ وتستند صلاحية التقريب في عينات أكبر إلى طبيعة البيانات والتصميم، ولا يضمنها كبر العينة دائماً.</p>
<h2>3. القيمة الاحتمالية واتخاذ القرار</h2>
<p>في الاختبار ثنائي الطرف تحسب القيمة الاحتمالية من طرفَي توزيع t، أما الاختبار أحادي الطرف فيعتمد الطرف المحدد في \(H_1\). عند مستوى \(\alpha=0.05\)، نرفض \(H_0\) عندما \(p\le0.05\) بشرط ملاءمة الافتراضات. لا تعني القيمة الاحتمالية احتمال صحة \(H_0\)، وعدم الرفض لا يثبت تساوي المتوسطين.</p>
<h2>4. مثال محلول</h2>
<p>إذا كان \(n=25\) و\(\overline x=18\) و\(s=4\) وأردنا اختبار \(H_0:\mu=20\) مقابل البديلة الثنائية:</p>
<div class="esa-st-math" dir="ltr" tabindex="0" role="region" aria-label="حساب مثال ستودنت">\[
\widehat{\mathrm{SE}}=\frac4{\sqrt{25}}=0.8,\qquad
t=\frac{18-20}{0.8}=-2.5,\quad df=24.
\]</div>
<p>القيمة الاحتمالية ثنائية الطرف نحو \(0.0197\)، وهي أقل من 5%، لذا نرفض \(H_0\) مع مراعاة الافتراضات. مقدار الفرق المشاهد \(-2\) بوحدة المتغير، ويجب تفسيره عملياً مع عدم اليقين، لا بالاكتفاء بقرار الرفض.</p>
<h2>5. فترة الثقة للمتوسط</h2>
<div class="esa-st-math" dir="ltr" tabindex="0" role="region" aria-label="صيغة فترة الثقة">\[
\overline x\ \pm\ t_{0.975,n-1}\frac{s}{\sqrt n}.
\]</div>
<p>في المثال \(t_{0.975,24}\approx2.0639\)، فتكون فترة الثقة 95% تقريباً \([16.349,\ 19.651]\). وهي تستبعد 20، وهذا متوافق مع قرار اختبار ثنائي الطرف عند 5%. فترة الثقة هنا للمتوسط السكاني، وليست فترة تنبؤ بملاحظة مستقبلية واحدة. تبقى الفترة المعروضة في المختبر ثنائية الطرف حتى لو اختيرت بديلة أحادية الطرف.</p>
<h2>6. المختبر التفاعلي</h2>
<section class="concept-box" id="esa-student-t-lab" data-locale="ar" aria-labelledby="esa-st-heading">
<h3 id="esa-st-heading">جرّب اختبار ستودنت لعينة واحدة</h3>
<p>غيّر حجم العينة ومتوسطها وانحرافها المعياري والفرضية البديلة لرؤية إحصائية t والقيمة الاحتمالية وفترة الثقة. يستخدم المختبر المحرك الحسابي نفسه المستخدم في الدرس الإنجليزي.</p>
<div class="esa-st-grid">
<div><label for="esa-st-n">حجم العينة \(n\) (اثنان على الأقل)</label><input id="esa-st-n" type="number" min="2" max="1000000" step="1" value="10" aria-describedby="esa-st-error"></div>
<div><label for="esa-st-mean">متوسط العينة \(\overline x\)</label><input id="esa-st-mean" type="number" step="any" value="12" aria-describedby="esa-st-error"></div>
<div><label for="esa-st-sd">انحراف العينة \(s\) (بمقام \(n-1\))</label><input id="esa-st-sd" type="number" min="0" step="any" value="3" aria-describedby="esa-st-error"></div>
<div><label for="esa-st-mu0">المتوسط المفترض \(\mu_0\)</label><input id="esa-st-mu0" type="number" step="any" value="10" aria-describedby="esa-st-error"></div>
<div><label for="esa-st-alternative">الفرضية البديلة</label><select id="esa-st-alternative"><option value="two-sided">ثنائي الطرف</option><option value="greater">أكبر من القيمة المرجعية</option><option value="less">أصغر من القيمة المرجعية</option></select></div>
</div>
<button id="esa-st-reset" class="btn btn-outline" type="button">استعادة قيم المثال التفاعلي</button>
<p id="esa-st-error" role="alert" hidden></p>
<section id="esa-st-results" role="status" aria-live="polite" aria-label="نتائج اختبار ستودنت">
<div class="table-wrap"><table><caption>إحصائية t وفترة الثقة عند 95%</caption><tbody>
<tr><th scope="row">درجات الحرية</th><td dir="ltr" id="esa-st-df">—</td></tr>
<tr><th scope="row">الخطأ المعياري</th><td dir="ltr" id="esa-st-se">—</td></tr>
<tr><th scope="row">إحصائية t</th><td dir="ltr" id="esa-st-t">—</td></tr>
<tr><th scope="row">القيمة الاحتمالية</th><td dir="ltr" id="esa-st-pvalue">—</td></tr>
<tr><th scope="row">قيمة t الحرجة عند 95%</th><td dir="ltr" id="esa-st-critical">—</td></tr>
<tr><th scope="row">الحد الأدنى لفترة الثقة</th><td dir="ltr" id="esa-st-lower">—</td></tr>
<tr><th scope="row">الحد الأعلى لفترة الثقة</th><td dir="ltr" id="esa-st-upper">—</td></tr>
</tbody></table></div>
<svg id="esa-st-plot" role="img" viewBox="0 0 620 235" aria-label="توزيع ستودنت ومناطق القيمة الاحتمالية" style="display:block;max-width:100%;height:auto;width:100%"></svg>
<p id="esa-st-decision"></p><p id="esa-st-assumptions"></p><p id="esa-st-limits"></p>
</section>
</section>
<h2>7. افتراضات وأخطاء شائعة</h2>
<ul class="bullets">
<li>يجب أن يكون تصميم المعاينة والاستقلال مناسبين؛ وتعد القيم المتطرفة مهمة خاصة في العينات الصغيرة.</li>
<li>الاختبار يستخدم انحراف العينة \(s\)، وليس انحراف المجتمع المعلوم \(\sigma\) كما في اختبار Z.</li>
<li>لا يمكن استنتاج غياب الالتواء أو القيم المتطرفة من الإحصاءات الملخصة وحدها.</li>
<li>لا تعني الدلالة الإحصائية بالضرورة أهمية عملية أو وجود علاقة سببية.</li>
</ul>
<div class="lesson-nav"><a class="btn btn-outline" href="/ar/inference/classical-tests/one-sample-z-test-for-mean/">السابق: اختبار Z</a><a class="btn" lang="en" href="/inference/classical-tests/paired-t-test/">التالي: اختبار t للعينات المزدوجة (English)</a></div>
</div></section>
<style>
#esa-student-t-lab,#esa-student-t-lab *{box-sizing:border-box}
#esa-student-t-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-student-t-lab .esa-st-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,215px),1fr));gap:12px;margin:14px 0}
#esa-student-t-lab label{display:block;font-weight:650;margin-bottom:6px}
#esa-student-t-lab :is(input,select){display:block;width:100%;min-width:0;padding:10px;border:1px solid #777;border-radius:7px;font:inherit}
#esa-student-t-lab [hidden]{display:none!important}
#esa-student-t-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-student-t-lab :is(input,select,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
@media(max-width:650px){#esa-student-t-lab .esa-st-grid{grid-template-columns:minmax(0,1fr)}}
.esa-st-math{direction:ltr;max-width:100%;overflow-x:auto;padding:8px 0}
</style>
<script defer src="/js/student-t-one-sample-explorer.js"></script>